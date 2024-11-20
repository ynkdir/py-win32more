import argparse
import json
import re
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

    def readjson(self, zippath):
        # return json.loads(self._zipfile.read(zippath).decode("utf-8-sig"))
        # WORKAROUND:
        s = self._zipfile.read(zippath).decode("utf-8-sig")
        s = re.sub(r'"HexUInt32": (\d+)', r'"HexUInt32": "0x\1"', s)
        return json.loads(s)


class Edit:
    def __init__(self, path):
        self._path = path
        self._text = Path(path).read_text()

    def substitute(self, pattern, substitution):
        self._text = re.sub(pattern, substitution, self._text, flags=re.MULTILINE)

    def write(self):
        Path(self._path).write_text(self._text, newline="")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args()

    nupkg = NupkgDownload(
        f"https://api.nuget.org/v3-flatcontainer/microsoft.windowsappsdk/{args.version}/microsoft.windowsappsdk.{args.version}.nupkg"
    )
    version_info = nupkg.readjson("WindowsAppSDK-VersionInfo.json")

    nupkg.extract(
        "runtimes/win-arm64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
        "win32more/dll/arm64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
    )
    nupkg.extract(
        "runtimes/win-x64/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
        "win32more/dll/x64/Microsoft.WindowsAppRuntime.Bootstrap.dll",
    )
    nupkg.extract(
        "runtimes/win-x86/native/Microsoft.WindowsAppRuntime.Bootstrap.dll",
        "win32more/dll/x86/Microsoft.WindowsAppRuntime.Bootstrap.dll",
    )
    nupkg.extract(
        "license.txt",
        "LICENSE (Microsoft.WindowsAppRuntime.Bootstrap.dll).txt",
    )

    ed = Edit("win32more/mddbootstrap.py")
    ed.substitute("^# VERSION: .*$", f"# VERSION: {args.version}")
    ed.substitute(
        "^WINDOWSAPPSDK_RELEASE_MAJORMINOR = .*$",
        f"WINDOWSAPPSDK_RELEASE_MAJORMINOR = {version_info['Release']['MajorMinor']['HexUInt32']}",
    )
    ed.substitute(
        "^WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W = .*$",
        f"WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W = \"{version_info['Release']['VersionShortTag']}\"",
    )
    # MEMO: Runtime.Version.UInt16 and HexUInt16 are 64bit value.
    ed.substitute(
        "^WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 = .*$",
        f"WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 = {version_info['Runtime']['Version']['HexUInt16']}",
    )
    ed.write()


if __name__ == "__main__":
    main()
