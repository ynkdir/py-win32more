import argparse
import contextlib
import json
import logging
import math
import os
import re
import shutil
import stat
import subprocess
import tomllib
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Self

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class NuGetVersion:
    major: int
    minor: int
    patch: int
    revision: int | None = None
    prerelease: str | None = None

    @classmethod
    def parse(cls, version_str: str) -> Self:
        m = re.match(
            r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:\.(?P<revision>0|[1-9]\d*))?(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$",
            version_str,
        )
        if not m:
            raise ValueError(f"cannot parse version string: '{version_str}'")
        # ignore buildmetadata
        if m["revision"] is None:
            revision = None
        else:
            revision = int(m["revision"])
        return cls(int(m["major"]), int(m["minor"]), int(m["patch"]), revision, m["prerelease"])

    def __lt__(self, other: Self) -> bool:
        return self._comparetuple() < other._comparetuple()

    def _comparetuple(self) -> tuple:
        revision = self.revision
        if revision is None:
            revision = 0
        prerelease = self.prerelease
        if prerelease is None:
            prerelease = math.inf
        return (self.major, self.minor, self.patch, revision, prerelease)

    def __str__(self):
        if self.revision is None:
            revision = ""
        else:
            revision = f".{self.revision}"
        if self.prerelease is None:
            prerelease = ""
        else:
            prerelease = "-" + self.prerelease
        return f"{self.major}.{self.minor}.{self.patch}{revision}{prerelease}"


@dataclass(frozen=True)
class PackageSpec:
    spec: str
    id: str
    version: str

    @classmethod
    def parse(cls, spec: str) -> Self:
        id, version = re.split(r"\.(?=\d)", spec, maxsplit=1)
        return cls(spec, id, version)


@dataclass(frozen=True)
class AppSDKVersionInfo:
    WINDOWSAPPSDK_RELEASE_MAJORMINOR: str
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W: str
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64: str
    WINDOWSAPPSDK_FRAMEWORK_PACKAGE_FAMILY_NAME: str

    def format(self) -> str:
        return f"""WINDOWSAPPSDK_RELEASE_MAJORMINOR = {self.WINDOWSAPPSDK_RELEASE_MAJORMINOR}
WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W = '{self.WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W}'
WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 = {self.WINDOWSAPPSDK_RUNTIME_VERSION_UINT64}
WINDOWSAPPSDK_FRAMEWORK_PACKAGE_FAMILY_NAME = '{self.WINDOWSAPPSDK_FRAMEWORK_PACKAGE_FAMILY_NAME}'"""

    @staticmethod
    def parse(xml: Path) -> AppSDKVersionInfo:
        def _find_and_get_text(xmlpath) -> str:
            e = root.find(xmlpath)
            if e is None:
                raise RuntimeError(f"cannot find '{xmlpath}'")
            return e.text or ""

        root = ET.parse(xml).getroot()

        major_minor = _find_and_get_text("Release/MajorMinor/HexUInt32")
        if not major_minor.startswith("0x"):
            major_minor = f"0x{major_minor}"

        shorttag = _find_and_get_text("Release/ShortTag")

        version = _find_and_get_text("Runtime/Version/HexUInt16")

        framework_package_family_name = _find_and_get_text("Runtime/Packages/Framework/PackageFamilyName")

        return AppSDKVersionInfo(major_minor, shorttag, version, framework_package_family_name)


class MetadataParser:
    def __init__(self, metadata: list[dict]) -> None:
        self._metadata = metadata

    def namespaces(self) -> set[str]:
        return {td["Namespace"] for td in self._metadata if self._is_public(td)}

    def _is_public(self, td: dict) -> bool:
        is_winrt = "WindowsRuntime" in td["Attributes"]
        if is_winrt:
            return td["Namespace"] != "" and td["BaseType"] != "System.Attribute"
        else:
            return td["Namespace"] != "" and "Public" in td["Attributes"]


class Builder:
    def __init__(
        self,
        build_dir: Path,
        dist_dir: Path,
        win32more_major: int,
        win32more_minor: int,
    ) -> None:
        self._build_dir = build_dir
        self._dist_dir = dist_dir
        self._win32more_major = win32more_major
        self._win32more_minor = win32more_minor

        if build_dir.exists():
            self.rmtree_force(build_dir)
        self.mkdir(build_dir)

        if dist_dir.exists():
            self.rmtree_force(dist_dir)
        self.mkdir(dist_dir)

        self._nupkg_dir = self.mkdir(build_dir / "nupkg")
        self._json_dir = self.mkdir(build_dir / "json")
        self._generate_dir = self.mkdir(build_dir / "generate")

    def build(self, id: str, version: str) -> None:
        recipe = self.recipe(id, version)
        self.download(recipe, version)
        self.generate(recipe)
        self.assets(recipe)
        self.versioninfo(recipe)
        self.pyproject(recipe, version)

    def recipe(self, id: str, version: str) -> dict:
        if id == "Microsoft.Windows.SDK.Win32Metadata":
            return RECIPES["Microsoft.Windows.SDK.Win32Metadata"]
        elif id == "Microsoft.Windows.SDK.Contracts":
            return RECIPES["Microsoft.Windows.SDK.Contracts"]
        elif id == "Microsoft.WindowsAppSDK":
            if NuGetVersion.parse(version) < NuGetVersion.parse("1.6.0"):
                return RECIPES["Microsoft.WindowsAppSDK.1.5"]
            elif NuGetVersion.parse(version) < NuGetVersion.parse("1.7.0"):
                return RECIPES["Microsoft.WindowsAppSDK.1.6"]
            elif NuGetVersion.parse(version) < NuGetVersion.parse("1.8.0"):
                return RECIPES["Microsoft.WindowsAppSDK.1.7"]
            elif NuGetVersion.parse(version) < NuGetVersion.parse("1.8.250916003"):
                return RECIPES["Microsoft.WindowsAppSDK.1.8"]
            elif NuGetVersion.parse(version) < NuGetVersion.parse("2.0.1"):
                return RECIPES["Microsoft.WindowsAppSDK.1.8.250916003"]
            else:
                return RECIPES["Microsoft.WindowsAppSDK.2.0.1"]
        elif id == "Microsoft.Web.WebView2":
            return RECIPES["Microsoft.Web.WebView2"]
        elif id == "Microsoft.Graphics.Win2D":
            if NuGetVersion.parse(version) < NuGetVersion.parse("1.3.0"):
                return RECIPES["Microsoft.Graphics.Win2D.1.2"]
            elif NuGetVersion.parse(version) < NuGetVersion.parse("1.4.0"):
                return RECIPES["Microsoft.Graphics.Win2D.1.3"]
            else:
                return RECIPES["Microsoft.Graphics.Win2D.1.4"]
        else:
            raise RuntimeError(f"cannot build {id}.{version}")

    def download(self, recipe: dict, version: str) -> None:
        self.nuget_install(recipe["id"], version)

        for nupkg_id, nupkg_version in recipe["extra_install"]:
            self.nuget_install(nupkg_id, nupkg_version)

        assert self.nupkg_names() == self.known_packages(recipe)

    def generate(self, recipe: dict) -> None:
        metadata = self.metadata(recipe)

        dependencies_metadata = self.dependencies_metadata(recipe)

        self.win32generator(metadata + dependencies_metadata)

        for namespace in self.namespaces(metadata):
            self.copymodule(namespace)

    def assets(self, recipe: dict) -> None:
        for id, nupkg_path, dist_path in recipe["assets"]:
            self.copyfile(id, nupkg_path, dist_path)

    def versioninfo(self, recipe: dict) -> None:
        if recipe["versioninfo"] is not None:
            id, nupkg_path, dist_path = recipe["versioninfo"]
            self.writefile(AppSDKVersionInfo.parse(self.nupkg_path(id) / nupkg_path).format(), dist_path)

    def pyproject(self, recipe: dict, version: str):
        major = self._win32more_major
        minor = self._win32more_minor

        v = NuGetVersion.parse(version)
        if v.prerelease is not None:
            release = NuGetVersion(v.major, v.minor, v.patch, v.revision)
            if recipe["prerelease_is_release"]:
                version = f"{release}"
            else:
                version = f"{release}a"

        dependencies = []

        for core in recipe["core_dependencies"]:
            dependencies.append(f'"win32more-{core}=={major}.{minor}.*"')

        for recipe_id in recipe["dependencies"]:
            nupkg_id = RECIPES[recipe_id]["id"]
            nupkg_version = self.nupkg_version(nupkg_id)
            dependencies.append(f'"win32more-{nupkg_id}>={major}.{minor}.{nupkg_version},<{major}.{minor + 1}"')

        dependencies_csv = ", ".join(dependencies)

        self.writefile(
            f"""[project]
name = "win32more-{recipe["id"]}"
version = "{major}.{minor}.{version}"
dependencies = [{dependencies_csv}]

[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/win32more"]
""",
            "pyproject.toml",
        )

    def dependencies(self, recipe: dict) -> set[str]:
        dependencies = set(recipe["dependencies"])
        for recipe_id in recipe["dependencies"]:
            dependencies |= self.dependencies(RECIPES[recipe_id])
        return dependencies

    def known_packages(self, recipe: dict) -> set[str]:
        known_packages = set(recipe["known_packages"])
        for recipe_id in recipe["dependencies"]:
            known_packages |= self.known_packages(RECIPES[recipe_id])
        return known_packages

    def metadata(self, recipe: dict) -> list[Path]:
        metadata = []
        for nupkg_id, pattern in recipe["metadata"]:
            for winmd_file in self.nupkg_path(nupkg_id).glob(pattern):
                json_file = self.winmd_printer(winmd_file)
                metadata.append(json_file)
        return metadata

    def dependencies_metadata(self, recipe: dict) -> list[Path]:
        metadata = []
        for recipe_id in self.dependencies(recipe):
            metadata.extend(self.metadata(RECIPES[recipe_id]))
        return metadata

    def nupkg_path(self, id: str) -> Path:
        for p in self._nupkg_dir.iterdir():
            spec = PackageSpec.parse(p.name)
            if spec.id == id:
                return p
        raise KeyError(f"cannot find {id}")

    def nupkg_version(self, id: str) -> str:
        for p in self._nupkg_dir.iterdir():
            spec = PackageSpec.parse(p.name)
            if spec.id == id:
                return spec.version
        raise KeyError(f"cannot find {id}")

    def nupkg_names(self) -> set[str]:
        return {PackageSpec.parse(p.name).id for p in self._nupkg_dir.iterdir()}

    def nuget_install(self, id: str, version: str) -> None:
        logger.debug(f"nuget_install: {id}.{version}")
        subprocess.run(
            ["nuget.exe", "install", id, "-OutputDirectory", self._nupkg_dir, "-Version", version], check=True
        )

    def win32generator(self, json_files: list[Path]) -> None:
        subprocess.run(
            ["py", "-m", "win32generator", "--output-directory", self._generate_dir, *json_files], check=True
        )

    def winmd_printer(self, winmd_file: Path) -> Path:
        winmd_printer_exe = self._build_dir / "winmd-printer/bin/winmd-printer.exe"

        json_file = self._json_dir / winmd_file.with_suffix(".json").name

        if not winmd_printer_exe.exists():
            logger.debug("winmd_printer: compile")
            with contextlib.chdir(self._build_dir):
                subprocess.run(
                    ["git", "clone", "--depth", "1", "https://github.com/ynkdir/winmd-printer.git"], check=True
                )
            with contextlib.chdir(self._build_dir / "winmd-printer"):
                subprocess.run(["dotnet.exe", "build", "--configuration", "Release", "--output", "bin"], check=True)

        logger.debug(f"winmd_printer: {winmd_file} {json_file}")
        json_file.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([winmd_printer_exe, "-o", json_file, winmd_file], check=True)

        return json_file

    def namespaces(self, json_files: list[Path]) -> set[str]:
        metadata = []
        for p in json_files:
            metadata.extend(json.loads(p.read_text()))
        return MetadataParser(metadata).namespaces()

    def copymodule(self, namespace: str) -> None:
        module = namespace.replace(".", "/") + "/__init__.py"
        src = self._generate_dir / "win32more" / module
        dst = self._dist_dir / "src/win32more" / module
        logger.debug(f"copymodule: {src} {dst}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)

    def copyfile(self, id: str, nupkg_path: str, dist_path: str) -> None:
        src = self.nupkg_path(id) / nupkg_path
        dst = self._dist_dir / dist_path
        logger.debug(f"copyfile: {src} {dst}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)

    def writefile(self, txt: str, dist_path: str) -> None:
        dst = self._dist_dir / dist_path
        logger.debug(f"writefile: {dst}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(txt, newline="")

    def rmtree_force(self, path: Path) -> None:
        def onexc(func, path, exc):
            os.chmod(path, stat.S_IWRITE)
            func(path)

        shutil.rmtree(path, onexc=onexc)

    def mkdir(self, path: Path) -> Path:
        path.mkdir(parents=True, exist_ok=True)
        return path


RECIPES = {
    "Microsoft.Windows.SDK.Win32Metadata": {
        "id": "Microsoft.Windows.SDK.Win32Metadata",
        "dependencies": ["Microsoft.Windows.SDK.Contracts"],
        "core_dependencies": ["core"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": ["Microsoft.Windows.SDK.Win32Metadata"],
        "metadata": [("Microsoft.Windows.SDK.Win32Metadata", "Windows.Win32.winmd")],
        "assets": [],
        "versioninfo": None,
        "prerelease_is_release": True,
    },
    "Microsoft.Windows.SDK.Contracts": {
        "id": "Microsoft.Windows.SDK.Contracts",
        "dependencies": [],
        "core_dependencies": ["core"],
        "extra_install": [],
        "known_packages": [
            "Microsoft.Windows.SDK.Contracts",
            "System.Runtime.WindowsRuntime",
            "System.Runtime.InteropServices.WindowsRuntime",
            "System.Runtime.WindowsRuntime.UI.Xaml",
        ],
        "metadata": [("Microsoft.Windows.SDK.Contracts", "ref/netstandard2.0/*.winmd")],
        "assets": [],
        "versioninfo": None,
        "prerelease_is_release": False,
    },
    "Microsoft.WindowsAppSDK.1.5": {
        "id": "Microsoft.WindowsAppSDK",
        "dependencies": ["Microsoft.Windows.SDK.Contracts"],
        "core_dependencies": ["core", "appsdk"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": ["Microsoft.WindowsAppSDK", "Microsoft.Windows.SDK.BuildTools"],
        "metadata": [
            ("Microsoft.WindowsAppSDK", "lib/uap10.0.18362/*.winmd"),
            ("Microsoft.WindowsAppSDK", "lib/uap10.0/*.winmd"),
        ],
        "assets": [
            ("Microsoft.WindowsAppSDK", "license.txt", "LICENSE (Microsoft.WindowsAppSDK).txt"),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x86/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x86/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-arm64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/arm64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
        ],
        "versioninfo": (
            "Microsoft.WindowsAppSDK",
            "WindowsAppSDK-VersionInfo.xml",
            "src/win32more/appsdk/versioninfo.py",
        ),
        "prerelease_is_release": False,
    },
    "Microsoft.WindowsAppSDK.1.6": {
        "id": "Microsoft.WindowsAppSDK",
        "dependencies": ["Microsoft.Windows.SDK.Contracts", "Microsoft.Web.WebView2"],
        "core_dependencies": ["core", "appsdk"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": ["Microsoft.WindowsAppSDK", "Microsoft.Windows.SDK.BuildTools"],
        "metadata": [
            ("Microsoft.WindowsAppSDK", "lib/uap10.0.18362/*.winmd"),
            ("Microsoft.WindowsAppSDK", "lib/uap10.0/*.winmd"),
        ],
        "assets": [
            ("Microsoft.WindowsAppSDK", "license.txt", "LICENSE (Microsoft.WindowsAppSDK).txt"),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x86/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x86/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-arm64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/arm64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
        ],
        "versioninfo": (
            "Microsoft.WindowsAppSDK",
            "WindowsAppSDK-VersionInfo.xml",
            "src/win32more/appsdk/versioninfo.py",
        ),
        "prerelease_is_release": False,
    },
    "Microsoft.WindowsAppSDK.1.7": {
        "id": "Microsoft.WindowsAppSDK",
        "dependencies": ["Microsoft.Windows.SDK.Contracts", "Microsoft.Web.WebView2"],
        "core_dependencies": ["core", "appsdk"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": ["Microsoft.WindowsAppSDK", "Microsoft.Windows.SDK.BuildTools"],
        "metadata": [
            ("Microsoft.WindowsAppSDK", "lib/uap10.0.18362/*.winmd"),
            ("Microsoft.WindowsAppSDK", "lib/uap10.0/*.winmd"),
        ],
        "assets": [
            ("Microsoft.WindowsAppSDK", "license.txt", "LICENSE (Microsoft.WindowsAppSDK).txt"),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x86/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x86/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-arm64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/arm64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x86/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x86/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-x64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK",
                "runtimes/win-arm64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/arm64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
        ],
        "versioninfo": (
            "Microsoft.WindowsAppSDK",
            "WindowsAppSDK-VersionInfo.xml",
            "src/win32more/appsdk/versioninfo.py",
        ),
        "prerelease_is_release": False,
    },
    "Microsoft.WindowsAppSDK.1.8": {
        "id": "Microsoft.WindowsAppSDK",
        "dependencies": ["Microsoft.Windows.SDK.Contracts", "Microsoft.Web.WebView2"],
        "core_dependencies": ["core", "appsdk"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": [
            "Microsoft.WindowsAppSDK",
            "Microsoft.WindowsAppSDK.Base",
            "Microsoft.WindowsAppSDK.Foundation",
            "Microsoft.WindowsAppSDK.InteractiveExperiences",
            "Microsoft.WindowsAppSDK.WinUI",
            "Microsoft.WindowsAppSDK.DWrite",
            "Microsoft.WindowsAppSDK.Widgets",
            "Microsoft.WindowsAppSDK.AI",
            "Microsoft.WindowsAppSDK.Runtime",
            "Microsoft.Windows.SDK.BuildTools",
            "Microsoft.Windows.SDK.BuildTools.MSIX",
        ],
        "metadata": [
            ("Microsoft.WindowsAppSDK.Foundation", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.InteractiveExperiences", "metadata/10.0.18362.0/*.winmd"),
            ("Microsoft.WindowsAppSDK.WinUI", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.Widgets", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.AI", "metadata/*.winmd"),
        ],
        "assets": [
            ("Microsoft.WindowsAppSDK", "license.txt", "LICENSE (Microsoft.WindowsAppSDK).txt"),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x86/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x86/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-arm64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/arm64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x86/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x86/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-arm64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/arm64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
        ],
        "versioninfo": (
            "Microsoft.WindowsAppSDK.Runtime",
            "WindowsAppSDK-VersionInfo.xml",
            "src/win32more/appsdk/versioninfo.py",
        ),
        "prerelease_is_release": False,
    },
    "Microsoft.WindowsAppSDK.1.8.250916003": {
        "id": "Microsoft.WindowsAppSDK",
        "dependencies": ["Microsoft.Windows.SDK.Contracts", "Microsoft.Web.WebView2"],
        "core_dependencies": ["core", "appsdk"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": [
            "Microsoft.WindowsAppSDK",
            "Microsoft.WindowsAppSDK.Base",
            "Microsoft.WindowsAppSDK.Foundation",
            "Microsoft.WindowsAppSDK.InteractiveExperiences",
            "Microsoft.WindowsAppSDK.WinUI",
            "Microsoft.WindowsAppSDK.DWrite",
            "Microsoft.WindowsAppSDK.Widgets",
            "Microsoft.WindowsAppSDK.AI",
            "Microsoft.WindowsAppSDK.Runtime",
            "Microsoft.WindowsAppSDK.ML",
            "Microsoft.Windows.SDK.BuildTools",
            "Microsoft.Windows.SDK.BuildTools.MSIX",
        ],
        "metadata": [
            ("Microsoft.WindowsAppSDK.Foundation", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.InteractiveExperiences", "metadata/10.0.18362.0/*.winmd"),
            ("Microsoft.WindowsAppSDK.WinUI", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.Widgets", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.AI", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.ML", "metadata/*.winmd"),
        ],
        "assets": [
            ("Microsoft.WindowsAppSDK", "license.txt", "LICENSE (Microsoft.WindowsAppSDK).txt"),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x86/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x86/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-arm64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/arm64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x86/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x86/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-arm64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/arm64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
        ],
        "versioninfo": (
            "Microsoft.WindowsAppSDK.Runtime",
            "WindowsAppSDK-VersionInfo.xml",
            "src/win32more/appsdk/versioninfo.py",
        ),
        "prerelease_is_release": False,
    },
    "Microsoft.WindowsAppSDK.2.0.1": {
        "id": "Microsoft.WindowsAppSDK",
        "dependencies": ["Microsoft.Windows.SDK.Contracts", "Microsoft.Web.WebView2"],
        "core_dependencies": ["core", "appsdk"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": [
            "Microsoft.WindowsAppSDK",
            "Microsoft.WindowsAppSDK.Base",
            "Microsoft.WindowsAppSDK.Foundation",
            "Microsoft.WindowsAppSDK.InteractiveExperiences",
            "Microsoft.WindowsAppSDK.WinUI",
            "Microsoft.WindowsAppSDK.DWrite",
            "Microsoft.WindowsAppSDK.Widgets",
            "Microsoft.WindowsAppSDK.AI",
            "Microsoft.WindowsAppSDK.Runtime",
            "Microsoft.WindowsAppSDK.ML",
            "Microsoft.Windows.SDK.BuildTools",
            "Microsoft.Windows.SDK.BuildTools.MSIX",
            "Microsoft.Windows.AI.MachineLearning",
            "Microsoft.Bcl.Numerics",
            "System.Buffers",
            "System.Memory",
            "System.Numerics.Tensors",
            "System.Numerics.Vectors",
            "System.Runtime.CompilerServices.Unsafe",
        ],
        "metadata": [
            ("Microsoft.WindowsAppSDK.Foundation", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.InteractiveExperiences", "metadata/10.0.18362.0/*.winmd"),
            ("Microsoft.WindowsAppSDK.WinUI", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.Widgets", "metadata/*.winmd"),
            ("Microsoft.WindowsAppSDK.AI", "metadata/*.winmd"),
            ("Microsoft.Windows.AI.MachineLearning", "metadata/*.winmd"),
        ],
        "assets": [
            ("Microsoft.WindowsAppSDK", "license.txt", "LICENSE (Microsoft.WindowsAppSDK).txt"),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x86/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x86/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/x64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-arm64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
                "src/win32more/dll/arm64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x86/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x86/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-x64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/x64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
            (
                "Microsoft.WindowsAppSDK.Foundation",
                "runtimes/win-arm64/native/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
                "src/win32more/dll/arm64/Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.dll",
            ),
        ],
        "versioninfo": (
            "Microsoft.WindowsAppSDK.Runtime",
            "WindowsAppSDK-VersionInfo.xml",
            "src/win32more/appsdk/versioninfo.py",
        ),
        "prerelease_is_release": False,
    },
    "Microsoft.Web.WebView2": {
        "id": "Microsoft.Web.WebView2",
        "dependencies": ["Microsoft.Windows.SDK.Contracts"],
        "core_dependencies": ["core"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": ["Microsoft.Web.WebView2"],
        "metadata": [("Microsoft.Web.WebView2", "lib/*.winmd")],
        "assets": [
            ("Microsoft.Web.WebView2", "LICENSE.txt", "LICENSE (Microsoft.Web.WebView2).txt"),
            (
                "Microsoft.Web.WebView2",
                "runtimes/win-x86/native_uap/Microsoft.Web.WebView2.Core.dll",
                "src/win32more/dll/x86/Microsoft.Web.WebView2.Core.dll",
            ),
            (
                "Microsoft.Web.WebView2",
                "runtimes/win-x64/native_uap/Microsoft.Web.WebView2.Core.dll",
                "src/win32more/dll/x64/Microsoft.Web.WebView2.Core.dll",
            ),
            (
                "Microsoft.Web.WebView2",
                "runtimes/win-arm64/native_uap/Microsoft.Web.WebView2.Core.dll",
                "src/win32more/dll/arm64/Microsoft.Web.WebView2.Core.dll",
            ),
        ],
        "versioninfo": None,
        "prerelease_is_release": False,
    },
    "Microsoft.Graphics.Win2D.1.2": {
        "id": "Microsoft.Graphics.Win2D",
        "dependencies": ["Microsoft.WindowsAppSDK.1.5"],
        "core_dependencies": ["core"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": ["Microsoft.Graphics.Win2D"],
        "metadata": [("Microsoft.Graphics.Win2D", "lib/uap10.0/*.winmd")],
        "assets": [
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-x86/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/x86/Microsoft.Graphics.Canvas.dll",
            ),
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-x64/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/x64/Microsoft.Graphics.Canvas.dll",
            ),
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-arm64/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/arm64/Microsoft.Graphics.Canvas.dll",
            ),
        ],
        "versioninfo": None,
        "prerelease_is_release": False,
    },
    "Microsoft.Graphics.Win2D.1.3": {
        "id": "Microsoft.Graphics.Win2D",
        "dependencies": ["Microsoft.WindowsAppSDK.1.6"],
        "core_dependencies": ["core"],
        "extra_install": [("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705")],
        "known_packages": ["Microsoft.Graphics.Win2D"],
        "metadata": [("Microsoft.Graphics.Win2D", "lib/uap10.0/*.winmd")],
        "assets": [
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-x86/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/x86/Microsoft.Graphics.Canvas.dll",
            ),
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-x64/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/x64/Microsoft.Graphics.Canvas.dll",
            ),
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-arm64/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/arm64/Microsoft.Graphics.Canvas.dll",
            ),
        ],
        "versioninfo": None,
        "prerelease_is_release": False,
    },
    "Microsoft.Graphics.Win2D.1.4": {
        "id": "Microsoft.Graphics.Win2D",
        # FIXME: Win2D actually depends on Microsoft.WindowsAppSDK.WinUI
        "dependencies": ["Microsoft.WindowsAppSDK.1.8.250916003"],
        "core_dependencies": ["core"],
        "extra_install": [
            ("Microsoft.Windows.SDK.Contracts", "10.0.26100.7705"),
            ("Microsoft.WindowsAppSDK", "1.8.260209005"),
        ],
        "known_packages": ["Microsoft.Graphics.Win2D"],
        "metadata": [("Microsoft.Graphics.Win2D", "lib/uap10.0/*.winmd")],
        "assets": [
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-x86/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/x86/Microsoft.Graphics.Canvas.dll",
            ),
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-x64/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/x64/Microsoft.Graphics.Canvas.dll",
            ),
            (
                "Microsoft.Graphics.Win2D",
                "runtimes/win-arm64/native/Microsoft.Graphics.Canvas.dll",
                "src/win32more/dll/arm64/Microsoft.Graphics.Canvas.dll",
            ),
        ],
        "versioninfo": None,
        "prerelease_is_release": False,
    },
}


def main() -> None:
    logging.basicConfig(level=logging.DEBUG, force=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("--builddir", type=Path)
    parser.add_argument("--distdir", type=Path)
    parser.add_argument("--win32more-version")
    parser.add_argument("--name", required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    build_dir = args.builddir
    if build_dir is None:
        build_dir = Path(f"build/{args.name}.{args.version}")

    dist_dir = args.distdir
    if dist_dir is None:
        dist_dir = Path(f"packages/{args.name}.{args.version}")

    if args.win32more_version is not None:
        win32more_version = args.win32more_version.split(".")
    else:
        pyproject = tomllib.loads(Path("pyproject.toml").read_text())
        win32more_version = [int(x) for x in pyproject["project"]["version"].split(".")]
    win32more_major, win32more_minor, *_ = win32more_version

    Builder(
        build_dir,
        dist_dir,
        win32more_major,
        win32more_minor,
    ).build(args.name, args.version)


if __name__ == "__main__":
    main()
