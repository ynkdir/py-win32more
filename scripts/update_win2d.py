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

    nupkg = NupkgDownload(
        f"https://api.nuget.org/v3-flatcontainer/microsoft.graphics.win2d/{args.version}/microsoft.graphics.win2d.{args.version}.nupkg"
    )

    nupkg.extract(
        "runtimes/win-arm64/native/Microsoft.Graphics.Canvas.dll",
        "win32more/dll/arm64/Microsoft.Graphics.Canvas.dll",
    )
    nupkg.extract(
        "runtimes/win-x64/native/Microsoft.Graphics.Canvas.dll",
        "win32more/dll/x64/Microsoft.Graphics.Canvas.dll",
    )
    nupkg.extract(
        "runtimes/win-x86/native/Microsoft.Graphics.Canvas.dll",
        "win32more/dll/x86/Microsoft.Graphics.Canvas.dll",
    )


if __name__ == "__main__":
    main()
