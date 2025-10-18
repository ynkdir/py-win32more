# Build WindowsAppSDK self contained package
#
# Requires:
#   Python install manager
#   https://docs.python.org/dev/using/windows.html#python-install-manager

import argparse
import io
import logging
import shutil
import subprocess
import tempfile
import urllib.request
import xml.etree.ElementTree as ElementTree
from zipfile import ZipFile
from collections.abc import Iterable
from pathlib import Path
from tempfile import TemporaryDirectory

logger = logging.getLogger(__name__)

buildtools_nupkg_url = "https://api.nuget.org/v3-flatcontainer/microsoft.windows.sdk.buildtools/10.0.26100.6584/microsoft.windows.sdk.buildtools.10.0.26100.6584.nupkg"


def run(*cmd):
    logger.debug(f"run {cmd}")
    subprocess.run(cmd, check=True)


def download(url: str) -> bytes:
    logger.debug(f"download: {url}")
    with urllib.request.urlopen(url) as f:
        return f.read()


def download_zip(url: str) -> ZipFile:
    data = download(url)
    file = io.BytesIO(data)
    return ZipFile(file)


def download_nupkg_all_dependencies(id: str, version: str, tmpdir: Path) -> Iterable[tuple[str, str]]:
    nupkgdir = tmpdir / f"{id}.{version}"

    if nupkgdir.exists():
        return

    nupkg = download_zip(f"https://api.nuget.org/v3-flatcontainer/{id.lower()}/{version}/{id.lower()}.{version}.nupkg")

    nupkg.extractall(nupkgdir)

    yield (id, version)

    nuspec = (nupkgdir / f"{id}.nuspec").read_text(encoding="utf-8")
    root = ElementTree.fromstring(nuspec)
    ns = {"n": "http://schemas.microsoft.com/packaging/2013/05/nuspec.xsd"}
    for e in root.findall(".//n:dependency", namespaces=ns):
        id = e.attrib["id"]
        version = e.attrib["version"].strip("[]")
        yield from download_nupkg_all_dependencies(id, version, tmpdir)


# AddMicrosoftWindowsAppSDKPayloadFilesFromMsix
def appsdk_runtimefiles(msixdir: Path) -> Iterable[Path]:
    yield from msixdir.glob("**/*.dll")
    yield from msixdir.glob("**/workloads*.json")
    yield from msixdir.glob("**/RestartAgent.exe")
    yield from msixdir.glob("**/map.html")
    yield from msixdir.glob("**/*.mui")
    yield from msixdir.glob("**/*.png")
    yield from msixdir.glob("*.winmd")
    yield from msixdir.glob("**/*.xaml")
    yield from msixdir.glob("**/*.xbf")
    # <MicrosoftWindowsAppSDKFiles Remove="@(MicrosoftWindowsAppSDKFilesExcluded)"/>
    yield from msixdir.glob("**/*.pri")


# Microsoft.WindowsAppSDK.Base.*/build/Microsoft.WindowsAppSDK.SelfContained.targets
# GenerateAppManifestFromAppx
def appsdk_generate_menifest(appx_manifest: Path) -> str:
    writer = io.StringIO()

    writer.write("""<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<assembly manifestVersion='1.0'
    xmlns:asmv3='urn:schemas-microsoft-com:asm.v3'
    xmlns:winrtv1='urn:schemas-microsoft-com:winrt.v1'
    xmlns='urn:schemas-microsoft-com:asm.v1'>
""")

    ns = {"m": "http://schemas.microsoft.com/appx/manifest/foundation/windows10"}

    package = ElementTree.fromstring(appx_manifest.read_text(encoding="utf-8"))

    for winrt_factory in package.findall("m:Extensions/m:Extension/m:InProcessServer", namespaces=ns):
        dllfile = winrt_factory.findtext("m:Path", namespaces=ns)
        writer.write(f"    <asmv3:file name='{dllfile}'>\n")
        for typenode in winrt_factory.findall("m:ActivatableClass", namespaces=ns):
            typename = typenode.attrib["ActivatableClassId"]
            writer.write(f"        <winrtv1:activatableClass name='{typename}' threadingModel='both'/>\n")
        writer.write("    </asmv3:file>\n")

    for proxystub in package.findall("m:Extensions/m:Extension/m:ProxyStub", namespaces=ns):
        dllfile = proxystub.findtext("m:Path", namespaces=ns)
        # exclude PushNotificationsLongRunningTask, which requires the Singleton (which is unavailable for self-contained apps)
        # exclude Widgets entries unless/until they have been tested and verified by the Widgets team
        if dllfile == "PushNotificationsLongRunningTask.ProxyStub.dll" or dllfile == "Microsoft.Windows.Widgets.dll":
            continue
        writer.write(f"    <asmv3:file name='{dllfile}'>\n")
        clsid = proxystub.attrib["ClassId"]
        writer.write(f"        <asmv3:comClass clsid='{{{clsid}}}'/>\n")
        for typenode in proxystub.findall("m:Interface", namespaces=ns):
            interfaceid = typenode.attrib["InterfaceId"]
            name = typenode.attrib["Name"]
            writer.write(f"        <asmv3:comInterfaceProxyStub name='{name}' iid='{{{interfaceid}}}'/>\n")
        writer.write("    </asmv3:file>\n")

    writer.write("</assembly>")

    return writer.getvalue()


def download_appsdk(appsdk_version: str, target: Path) -> None:
    major, minor, _ = appsdk_version.split(".")

    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        for id, version in download_nupkg_all_dependencies("Microsoft.WindowsAppSDK", appsdk_version, tmpdir):
            pkgdir = tmpdir / f"{id}.{version}"

            if id == "Microsoft.WindowsAppSDK.Runtime":
                msix = pkgdir / f"tools/MSIX/win10-x64/Microsoft.WindowsAppRuntime.{major}.{minor}.msix"
                msixdir = tmpdir / msix.stem

                ZipFile(msix).extractall(msixdir)
                manifest = appsdk_generate_menifest(msixdir / "AppxManifest.xml")
                (target / "WindowsAppSDK.manifest").write_text(manifest)

                for runtimefile in appsdk_runtimefiles(msixdir):
                    if not runtimefile.is_file():
                        continue
                    relative = runtimefile.relative_to(msixdir)
                    logger.debug(f"runtime: {relative}")
                    dst = target / relative
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    runtimefile.copy(dst)

            elif id == "Microsoft.Web.WebView2":
                runtimefile = pkgdir / "runtimes/win-x64/native_uap/Microsoft.Web.WebView2.Core.dll"
                logger.debug(f"runtime: {runtimefile.name}")
                runtimefile.copy(target / runtimefile.name)


def main():
    logging.basicConfig(level=logging.DEBUG, force=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default="python", type=Path)
    parser.add_argument("--version", default="3.14")
    parser.add_argument("--appsdk", default="1.8.251003001")
    args = parser.parse_args()

    # Install Python
    run("pymanager.exe", "install", "--target", args.target, args.version)

    # Install win32more
    run(args.target / "python.exe", "-m", "pip", "install", "-r", "test_requirements.txt")

    # Install WindowsAppSDK Runtime
    download_appsdk(args.appsdk, args.target)

    # Edit python.exe's manifest
    # WindowsAppSDK.manifest was generated for C++ self contained project by Visual Studio.
    tmp = None
    mt = "mt.exe"
    if shutil.which("mt.exe") is None:
        tmp = tempfile.TemporaryDirectory()
        buildtools = download_zip(buildtools_nupkg_url)
        buildtools.extractall(tmp.name)
        mt = tmp.name + "/bin/10.0.26100.0/x64/mt.exe"

    run(
        mt,
        f"-inputresource:{args.target / 'python.exe'};#1",
        "-manifest",
        args.target / "WindowsAppSDK.manifest",
        f"-outputresource:{args.target / 'python.exe'};#1",
    )
    if tmp is not None:
        tmp.cleanup()

    # Run your script: <target>/python.exe winui3app.py


if __name__ == "__main__":
    main()
