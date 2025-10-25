from __future__ import annotations

import argparse
import contextlib
import json
import logging
import os
import re
import shutil
import stat
import subprocess
import urllib.request
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import tomllib

logger = logging.getLogger(__name__)

package_dir: Path
build_dir: Path
win32more_version: list[int]
nupkg_winrt: Nupkg


def version_tuple(version_str: str) -> tuple[int]:
    return tuple(int(n) for n in re.sub("-.*$", "", version_str).split("."))


class Version:
    def __init__(self, id: str, version_range: str) -> None:
        self._id = id
        self._version_range = version_range

    def id(self) -> str:
        return self._id

    def version_range(self) -> str:
        return self._version_range

    def version(self) -> str:
        if self.is_exact():
            return self._version_range[1:-1]
        return self._version_range

    def is_exact(self) -> bool:
        return self._version_range.startswith("[") and self._version_range.endswith("]")

    def is_preview(self) -> bool:
        return self.version().endswith("-preview")

    def pyname(self) -> str:
        return f"win32more-{self._id}"

    def pyversion(self) -> str:
        if self.is_preview():
            if self._id == "Microsoft.Windows.SDK.Win32Metadata":
                version = self.version().removesuffix("-preview")
            else:
                version = self.version().removesuffix("-preview") + "a"
        else:
            version = self.version()
        return f"{win32more_version[0]}.{win32more_version[1]}.{version}"

    def pyversion_max(self) -> str:
        return f"{win32more_version[0]}.{win32more_version[1] + 1}"

    def pydependency(self) -> str:
        if self.is_exact():
            return f"{self.pyname()}=={self.pyversion()}"
        else:
            return f"{self.pyname()}>={self.pyversion()},<{self.pyversion_max()}"


@dataclass(frozen=True)
class AppSDKVersionInfo:
    WINDOWSAPPSDK_RELEASE_MAJORMINOR: str
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W: str
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64: str

    def format(self) -> str:
        return f"""WINDOWSAPPSDK_RELEASE_MAJORMINOR = {self.WINDOWSAPPSDK_RELEASE_MAJORMINOR}
WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W = '{self.WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W}'
WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 = {self.WINDOWSAPPSDK_RUNTIME_VERSION_UINT64}"""

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

        return AppSDKVersionInfo(major_minor, shorttag, version)


@dataclass(frozen=True)
class Asset:
    dst: str
    data: bytes


class NuspecParser:
    def __init__(self, xml) -> None:
        self._root = ET.fromstring(xml)

    def dependencies(self) -> Iterable[Version]:
        ns = {"n": "http://schemas.microsoft.com/packaging/2013/05/nuspec.xsd"}
        for dependency in self._root.findall("n:metadata/n:dependencies/n:dependency", ns):
            id = dependency.get("id")
            if id is None:
                raise RuntimeError("cannot get id")
            version = dependency.get("version")
            if version is None:
                raise RuntimeError("cannot get version")
            yield Version(id, version)


class MetadataParser:
    def __init__(self, metadata: list[dict]) -> None:
        self._metadata = metadata

    def namespaces(self) -> Iterable[str]:
        return {td["Namespace"] for td in self._metadata if self._is_public(td)}

    def _is_public(self, td: dict) -> bool:
        is_winrt = "WindowsRuntime" in td["Attributes"]
        if is_winrt:
            return td["Namespace"] != "" and td["BaseType"] != "System.Attribute"
        else:
            return td["Namespace"] != "" and "Public" in td["Attributes"]


class NupkgStrategy(ABC):
    def __init__(self, nupkg: Nupkg) -> None:
        self._nupkg = nupkg

    @abstractmethod
    def known_dependencies(self) -> set[str]:
        pass

    @abstractmethod
    def runtime_dependencies(self) -> set[str]:
        pass

    @abstractmethod
    def assets(self) -> Iterable[Asset]:
        pass

    @abstractmethod
    def winmd_files(self) -> Iterable[Path]:
        pass

    @staticmethod
    def create(nupkg: Nupkg) -> NupkgStrategy:
        if nupkg.id() == "Microsoft.Windows.SDK.Win32Metadata":
            return NupkgWin32Metadata(nupkg)
        elif nupkg.id() == "Microsoft.Windows.SDK.Contracts":
            return NupkgWindowsSDKContracts(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK":
            if nupkg.version().startswith("1.8."):
                return NupkgWindowsAppSDK_1_8(nupkg)
            return NupkgWindowsAppSDK(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.Base":
            return NupkgWindowsAppSDKBase(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.Foundation":
            return NupkgWindowsAppSDKFoundation(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.InteractiveExperiences":
            return NupkgWindowsAppSDKInteractiveExperiences(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.WinUI":
            return NupkgWindowsAppSDKWinUI(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.DWrite":
            return NupkgWindowsAppSDKDWrite(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.Widgets":
            return NupkgWindowsAppSDKWidgets(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.AI":
            return NupkgWindowsAppSDKAI(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.Runtime":
            return NupkgWindowsAppSDKRuntime(nupkg)
        elif nupkg.id() == "Microsoft.WindowsAppSDK.ML":
            return NupkgWindowsAppSDKML(nupkg)
        elif nupkg.id() == "Microsoft.Web.WebView2":
            return NupkgWebView2(nupkg)
        elif nupkg.id() == "Microsoft.Graphics.Win2D":
            return NupkgWin2D(nupkg)
        elif nupkg.id() == "Microsoft.Windows.SDK.BuildTools":
            return NupkgWindowsSDKBuildTools(nupkg)
        elif nupkg.id() == "Microsoft.Windows.SDK.BuildTools.MSIX":
            return NupkgWindowsSDKBuildToolsMSIX(nupkg)
        raise RuntimeError(f"Unknown package '{nupkg.id()}'")


class NupkgWin32Metadata(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return set()

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        return [self._nupkg.nupkg_dir() / "Windows.Win32.winmd"]


class NupkgWindowsSDKContracts(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {
            "System.Runtime.WindowsRuntime",
            "System.Runtime.InteropServices.WindowsRuntime",
            "System.Runtime.WindowsRuntime.UI.Xaml",
        }

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("ref/netstandard2.0/*.winmd")


class NupkgWindowsAppSDK(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        if self._nupkg.version().startswith("1.5."):
            return {"Microsoft.Windows.SDK.BuildTools"}
        return {"Microsoft.Windows.SDK.BuildTools", "Microsoft.Web.WebView2"}

    def runtime_dependencies(self) -> set[str]:
        if self._nupkg.version().startswith("1.5."):
            return set()
        return {"Microsoft.Web.WebView2"}

    def assets(self) -> Iterable[Asset]:
        yield Asset("LICENSE (Microsoft.WindowsAppSDK).txt", (self._nupkg.nupkg_dir() / "license.txt").read_bytes())

        for p in self._nupkg.nupkg_dir().glob("runtimes/**/*.dll"):
            if "win-x86" in str(p):
                yield Asset(f"src/win32more/dll/x86/{p.name}", p.read_bytes())
            elif "win-x64" in str(p):
                yield Asset(f"src/win32more/dll/x64/{p.name}", p.read_bytes())
            elif "win-arm64" in str(p):
                yield Asset(f"src/win32more/dll/arm64/{p.name}", p.read_bytes())

        appver = AppSDKVersionInfo.parse(self._nupkg.nupkg_dir() / "WindowsAppSDK-VersionInfo.xml")
        yield Asset("src/win32more/appsdk/versioninfo.py", appver.format().encode("utf-8"))

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("lib/uap10.0.18362/*.winmd")
        yield from self._nupkg.nupkg_dir().glob("lib/uap10.0/*.winmd")


class NupkgWindowsAppSDK_1_8(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        if version_tuple(self._nupkg.version()) < version_tuple("1.8.250916003"):
            return {
                "Microsoft.WindowsAppSDK.Base",
                "Microsoft.WindowsAppSDK.Foundation",
                "Microsoft.WindowsAppSDK.InteractiveExperiences",
                "Microsoft.WindowsAppSDK.WinUI",
                "Microsoft.WindowsAppSDK.DWrite",
                "Microsoft.WindowsAppSDK.Widgets",
                "Microsoft.WindowsAppSDK.AI",
                "Microsoft.WindowsAppSDK.Runtime",
            }
        else:
            return {
                "Microsoft.WindowsAppSDK.Base",
                "Microsoft.WindowsAppSDK.Foundation",
                "Microsoft.WindowsAppSDK.InteractiveExperiences",
                "Microsoft.WindowsAppSDK.WinUI",
                "Microsoft.WindowsAppSDK.DWrite",
                "Microsoft.WindowsAppSDK.Widgets",
                "Microsoft.WindowsAppSDK.AI",
                "Microsoft.WindowsAppSDK.Runtime",
                "Microsoft.WindowsAppSDK.ML",
            }

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        yield Asset("LICENSE (Microsoft.WindowsAppSDK).txt", (self._nupkg.nupkg_dir() / "license.txt").read_bytes())

    def winmd_files(self) -> Iterable[Path]:
        return []


class NupkgWindowsAppSDKBase(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {
            "Microsoft.Windows.SDK.BuildTools",
            "Microsoft.Windows.SDK.BuildTools.MSIX",
        }

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        return []


class NupkgWindowsAppSDKFoundation(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {
            "Microsoft.WindowsAppSDK.Base",
            "Microsoft.WindowsAppSDK.InteractiveExperiences",
        }

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        for p in self._nupkg.nupkg_dir().glob("runtimes/**/*.dll"):
            if "win-x86" in str(p):
                yield Asset(f"src/win32more/dll/x86/{p.name}", p.read_bytes())
            elif "win-x64" in str(p):
                yield Asset(f"src/win32more/dll/x64/{p.name}", p.read_bytes())
            elif "win-arm64" in str(p):
                yield Asset(f"src/win32more/dll/arm64/{p.name}", p.read_bytes())

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("metadata/*.winmd")


class NupkgWindowsAppSDKInteractiveExperiences(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK.Base"}

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("metadata/10.0.18362.0/*.winmd")


class NupkgWindowsAppSDKWinUI(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {
            "Microsoft.Web.WebView2",
            "Microsoft.WindowsAppSDK.Base",
            "Microsoft.WindowsAppSDK.Foundation",
            "Microsoft.WindowsAppSDK.InteractiveExperiences",
        }

    def runtime_dependencies(self) -> set[str]:
        return {"Microsoft.Web.WebView2"}

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("metadata/*.winmd")


class NupkgWindowsAppSDKDWrite(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK.Base"}

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        return []


class NupkgWindowsAppSDKWidgets(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK.Base"}

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("metadata/*.winmd")


class NupkgWindowsAppSDKAI(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK.Base", "Microsoft.WindowsAppSDK.Foundation"}

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("metadata/*.winmd")


class NupkgWindowsAppSDKRuntime(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK.Base"}

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        appver = AppSDKVersionInfo.parse(self._nupkg.nupkg_dir() / "WindowsAppSDK-VersionInfo.xml")
        yield Asset("src/win32more/appsdk/versioninfo.py", appver.format().encode("utf-8"))

    def winmd_files(self) -> Iterable[Path]:
        return []


class NupkgWindowsAppSDKML(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK.Base", "Microsoft.WindowsAppSDK.Foundation"}

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("metadata/*.winmd")


class NupkgWebView2(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return set()

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        yield Asset("LICENSE (Microsoft.Web.WebView2).txt", (self._nupkg.nupkg_dir() / "LICENSE.txt").read_bytes())

        for p in self._nupkg.nupkg_dir().glob("runtimes/*/native_uap/*.dll"):
            if "win-x86" in str(p):
                yield Asset(f"src/win32more/dll/x86/{p.name}", p.read_bytes())
            elif "win-x64" in str(p):
                yield Asset(f"src/win32more/dll/x64/{p.name}", p.read_bytes())
            elif "win-arm64" in str(p):
                yield Asset(f"src/win32more/dll/arm64/{p.name}", p.read_bytes())

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("lib/*.winmd")


class NupkgWin2D(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK"}

    def runtime_dependencies(self) -> set[str]:
        return {"Microsoft.WindowsAppSDK"}

    def assets(self) -> Iterable[Asset]:
        for p in self._nupkg.nupkg_dir().glob("runtimes/**/*.dll"):
            if "win-x86" in str(p):
                yield Asset(f"src/win32more/dll/x86/{p.name}", p.read_bytes())
            elif "win-x64" in str(p):
                yield Asset(f"src/win32more/dll/x64/{p.name}", p.read_bytes())
            elif "win-arm64" in str(p):
                yield Asset(f"src/win32more/dll/arm64/{p.name}", p.read_bytes())

    def winmd_files(self) -> Iterable[Path]:
        yield from self._nupkg.nupkg_dir().glob("lib/uap10.0/*.winmd")


class NupkgWindowsSDKBuildTools(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return set()

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        return []


class NupkgWindowsSDKBuildToolsMSIX(NupkgStrategy):
    def known_dependencies(self) -> set[str]:
        return set()

    def runtime_dependencies(self) -> set[str]:
        return set()

    def assets(self) -> Iterable[Asset]:
        return []

    def winmd_files(self) -> Iterable[Path]:
        return []


class Nupkg:
    def __init__(self, id: str, version: str) -> None:
        self._id = id
        self._version = version
        self._strategy = NupkgStrategy.create(self)
        self.download()
        self.verify()
        self.compile()

    def id(self) -> str:
        return self._id

    def version(self) -> str:
        return self._version

    def url(self) -> str:
        return f"https://api.nuget.org/v3-flatcontainer/{self._id.lower()}/{self._version}/{self._id.lower()}.{self._version}.nupkg"

    def nupkg_file(self) -> Path:
        return build_dir / "nupkg" / f"{self._id}.{self._version}.nupkg"

    def nupkg_dir(self) -> Path:
        return build_dir / "nupkg" / f"{self._id}.{self._version}"

    def json_dir(self) -> Path:
        return build_dir / "json" / f"{self._id}.{self._version}"

    def json_files(self) -> Iterable[Path]:
        for _, json_file in self.winmd_json_files():
            yield json_file

    def winmd_json_files(self) -> Iterable[tuple[Path, Path]]:
        for winmd_file in self.winmd_files():
            json_file = self.json_dir() / winmd_file.with_suffix(".json").name
            yield winmd_file, json_file

    def download(self) -> None:
        if self.nupkg_file().exists():
            return
        download(self.url(), self.nupkg_file())
        shutil.unpack_archive(self.nupkg_file(), self.nupkg_dir(), "zip")

    def verify(self) -> None:
        deps = {ver.id() for ver in self.dependencies()}
        if deps != self.known_dependencies():
            raise RuntimeError(f"Unexpected dependencies: {self._id}.{self._version}: {deps}")

    def compile(self) -> None:
        if self.json_dir().exists():
            return
        self.json_dir().mkdir()
        for winmd_file, json_file in self.winmd_json_files():
            winmd_printer(winmd_file, json_file)

    def namespaces(self) -> Iterable[str]:
        metadata = []
        for p in self.json_files():
            metadata.extend(json.loads(p.read_text()))
        return MetadataParser(metadata).namespaces()

    def dependencies(self) -> Iterable[Version]:
        nuspec = (self.nupkg_dir() / f"{self._id}.nuspec").read_text(encoding="utf-8-sig")
        return NuspecParser(nuspec).dependencies()

    def known_dependencies(self) -> set[str]:
        return self._strategy.known_dependencies()

    def runtime_dependencies(self) -> set[str]:
        return self._strategy.runtime_dependencies()

    def assets(self) -> Iterable[Asset]:
        return self._strategy.assets()

    def winmd_files(self) -> Iterable[Path]:
        return self._strategy.winmd_files()


class Pypkg:
    def __init__(self, id: str, version: str) -> None:
        self._id = id
        self._version = version
        self._nupkg = Nupkg(id, version)

    def generate_dir(self) -> Path:
        return build_dir / "generate" / f"{self._id}.{self._version}"

    def package_dir(self) -> Path:
        return package_dir / f"{self._id}.{self._version}"

    def build_dependencies(self) -> Iterable[Version]:
        yield from self.collect_build_dependencies(self._nupkg, set())

    def collect_build_dependencies(self, nupkg: Nupkg, sentinel: set[str]) -> Iterable[Version]:
        if nupkg.id() in sentinel:
            return
        sentinel.add(nupkg.id())
        yield Version(nupkg.id(), nupkg.version())
        for ver in nupkg.dependencies():
            if ver.id().startswith("System."):
                continue
            yield from self.collect_build_dependencies(Nupkg(ver.id(), ver.version()), sentinel)

    def runtime_dependencies(self) -> Iterable[Version]:
        yield from self.collect_runtime_dependencies(self._nupkg, set())

    def collect_runtime_dependencies(self, nupkg: Nupkg, sentinel: set[str]) -> Iterable[Version]:
        if nupkg.id() in sentinel:
            return
        sentinel.add(nupkg.id())
        for ver in nupkg.dependencies():
            if ver.id().startswith("System."):
                continue
            if ver.id() in nupkg.runtime_dependencies():
                yield ver
                continue
            yield from self.collect_runtime_dependencies(Nupkg(ver.id(), ver.version()), sentinel)

    def dist_dependencies(self) -> Iterable[Version]:
        yield from self.collect_dist_dependencies(self._nupkg, set())

    def collect_dist_dependencies(self, nupkg: Nupkg, sentinel: set[str]) -> Iterable[Version]:
        if nupkg.id() in sentinel:
            return
        sentinel.add(nupkg.id())
        yield Version(nupkg.id(), nupkg.version())
        for ver in nupkg.dependencies():
            if ver.id().startswith("System."):
                continue
            if ver.id() in nupkg.runtime_dependencies():
                continue
            yield from self.collect_dist_dependencies(Nupkg(ver.id(), ver.version()), sentinel)

    def namespaces(self) -> Iterable[str]:
        for ver in self.dist_dependencies():
            yield from Nupkg(ver.id(), ver.version()).namespaces()

    def assets(self) -> Iterable[Asset]:
        for ver in self.dist_dependencies():
            yield from Nupkg(ver.id(), ver.version()).assets()

    def build(self) -> None:
        logger.debug(f"Pypkg.build: {self._id}.{self._version}")
        self.generate()
        self.assemble()

    def generate(self) -> None:
        if self.generate_dir().exists():
            rmtree_force(self.generate_dir())
        self.generate_dir().mkdir()
        json_files: list[Path] = []
        for ver in self.build_dependencies():
            json_files.extend(Nupkg(ver.id(), ver.version()).json_files())
        if self._nupkg.id() != "Microsoft.Windows.SDK.Contracts":
            json_files.extend(nupkg_winrt.json_files())
        subprocess.run(
            ["py", "-m", "win32generator", "--output-directory", self.generate_dir(), *json_files], check=True
        )

    def assemble(self) -> None:
        if self.package_dir().exists():
            rmtree_force(self.package_dir())
        self.package_dir().mkdir()
        self.copy_modules()
        self.copy_assets()
        self.write_pyproject()

    def copy_modules(self) -> None:
        for namespace in self.namespaces():
            module = namespace.replace(".", "/") + "/__init__.py"
            src = self.generate_dir() / "win32more" / module
            dst = self.package_dir() / "src/win32more" / module
            copyfile(src, dst)

    def copy_assets(self) -> None:
        for asset in self.assets():
            writebytes(self.package_dir() / asset.dst, asset.data)

    def pyproject_dependencies(self) -> str:
        deps = [f'"win32more=={win32more_version[0]}.{win32more_version[1]}.*"']
        for ver in self.runtime_dependencies():
            deps.append(f'"{ver.pydependency()}"')
        return ", ".join(deps)

    def write_pyproject(self) -> None:
        version = Version(self._id, self._version)
        dst = self.package_dir() / "pyproject.toml"
        writefile(
            dst,
            f"""[project]
name = "{version.pyname()}"
version = "{version.pyversion()}"
dependencies = [{self.pyproject_dependencies()}]

[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/win32more"]
""",
        )


def winmd_printer(winmd_file: Path, json_file: Path) -> None:
    winmd_printer_exe = build_dir / "winmd-printer/bin/winmd-printer.exe"

    if not winmd_printer_exe.exists():
        logger.debug("winmd_printer: compile")
        with contextlib.chdir(build_dir):
            subprocess.run(["git", "clone", "--depth", "1", "https://github.com/ynkdir/winmd-printer.git"], check=True)
        with contextlib.chdir(build_dir / "winmd-printer"):
            subprocess.run(["dotnet", "build", "--configuration", "Release", "--output", "bin"], check=True)

    logger.debug(f"winmd_printer: {winmd_file} {json_file}")
    json_file.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([winmd_printer_exe, "-o", json_file, winmd_file], check=True)


def download(url: str, dst: Path) -> None:
    logger.debug(f"download: {url} {dst}")
    with urllib.request.urlopen(url) as f:
        dst.write_bytes(f.read())


def copyfile(src: Path, dst: Path) -> None:
    logger.debug(f"copyfile: {src} {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def writefile(dst: Path, txt: str) -> None:
    logger.debug(f"writefile: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(txt)


def writebytes(dst: Path, data: bytes) -> None:
    logger.debug(f"writebytes: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)


def rmtree_force(path: Path) -> None:
    def onexc(func, path, exc):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    shutil.rmtree(path, onexc=onexc)


def main() -> None:
    global package_dir, build_dir, win32more_version, nupkg_winrt

    logging.basicConfig(level=logging.DEBUG, force=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("--builddir", default="build", type=Path)
    parser.add_argument("--packagedir", default="packages", type=Path)
    parser.add_argument("--win32more-version")
    parser.add_argument("--winrt-version", default="10.0.26100.4948")
    parser.add_argument("--name", required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    package_dir = args.packagedir
    build_dir = args.builddir

    if not package_dir.exists():
        package_dir.mkdir()

    if not build_dir.exists():
        build_dir.mkdir()

    if not (build_dir / "nupkg").exists():
        (build_dir / "nupkg").mkdir()

    if not (build_dir / "json").exists():
        (build_dir / "json").mkdir()

    if not (build_dir / "generate").exists():
        (build_dir / "generate").mkdir()

    if args.win32more_version is not None:
        win32more_version = args.win32more_version
    else:
        pyproject = tomllib.loads(Path("pyproject.toml").read_text())
        win32more_version = [int(x) for x in pyproject["project"]["version"].split(".")]

    nupkg_winrt = Nupkg("Microsoft.Windows.SDK.Contracts", args.winrt_version)

    Pypkg(args.name, args.version).build()


if __name__ == "__main__":
    main()
