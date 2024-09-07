import argparse
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile


class NupkgDownload:
    def __init__(self, url):
        with urlopen(url) as r:
            self._zipfile = ZipFile(BytesIO(r.read()))

    def extract(self, zippath, filepath):
        Path(filepath).write_bytes(self._zipfile.read(zippath))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args()

    nupkg = NupkgDownload(f"https://globalcdn.nuget.org/packages/microsoft.web.webview2.{args.version}.nupkg")

    nupkg.extract(
        "runtimes/win-arm64/native_uap/Microsoft.Web.WebView2.Core.dll",
        "win32more/dll/arm64/Microsoft.Web.WebView2.Core.dll",
    )
    nupkg.extract(
        "runtimes/win-x64/native_uap/Microsoft.Web.WebView2.Core.dll",
        "win32more/dll/x64/Microsoft.Web.WebView2.Core.dll",
    )
    nupkg.extract(
        "runtimes/win-x86/native_uap/Microsoft.Web.WebView2.Core.dll",
        "win32more/dll/x86/Microsoft.Web.WebView2.Core.dll",
    )


if __name__ == "__main__":
    main()
