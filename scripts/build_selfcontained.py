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
import zipfile
from pathlib import Path

logger = logging.getLogger(__name__)

__dir__ = Path(__file__).parent

# TODO: version select
appsdk_redist_url = "https://aka.ms/windowsappsdk/1.8/1.8.251003001/Microsoft.WindowsAppRuntime.Redist.1.8.zip"
webview2_nupkg_url = (
    "https://api.nuget.org/v3-flatcontainer/microsoft.web.webview2/1.0.3485.44/microsoft.web.webview2.1.0.3485.44.nupkg"
)
buildtools_nupkg_url = "https://api.nuget.org/v3-flatcontainer/microsoft.windows.sdk.buildtools/10.0.26100.6584/microsoft.windows.sdk.buildtools.10.0.26100.6584.nupkg"


def run(*cmd):
    logger.debug(f"run {cmd}")
    subprocess.run(cmd, check=True)


def download(url: str) -> bytes:
    logger.debug(f"download: {url}")
    with urllib.request.urlopen(url) as f:
        return f.read()


def download_zip(url: str) -> zipfile.ZipFile:
    data = download(url)
    file = io.BytesIO(data)
    return zipfile.ZipFile(file)


def main():
    logging.basicConfig(level=logging.DEBUG, force=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default="python", type=Path)
    parser.add_argument("--version", default="3.14")
    args = parser.parse_args()

    # Install Python
    run("py.exe", "install", "--target", args.target, args.version)

    # Install win32more
    run(args.target / "python.exe", "-m", "pip", "install", "win32more")

    # Install WindowsAppSDK Runtime
    redist = download_zip(appsdk_redist_url)
    msix = redist.read("MSIX/win10-x64/Microsoft.WindowsAppRuntime.1.8.msix")
    zipfile.ZipFile(io.BytesIO(msix)).extractall(args.target)

    # Install WebView2
    webview2 = download_zip(webview2_nupkg_url)
    (args.target / "Microsoft.Web.WebView2.Core.dll").write_bytes(
        webview2.read("runtimes/win-x64/native_uap/Microsoft.Web.WebView2.Core.dll")
    )

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
        __dir__ / "WindowsAppSDK.manifest",
        f"-outputresource:{args.target / 'python.exe'};#1",
    )
    if tmp is not None:
        tmp.cleanup()

    # Run your script: <target>/python.exe winui3app.py


if __name__ == "__main__":
    main()
