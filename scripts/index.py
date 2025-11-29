import argparse
import io
import json
import logging
import os.path
import sys
import urllib.request
import zipfile
from collections.abc import Iterable

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from win32generator.metadata import Metadata
from win32generator.preprocessor import Preprocessor

logger = logging.getLogger(__name__)


def download(url: str) -> bytes:
    logger.debug(f"download: {url}")
    with urllib.request.urlopen(url) as f:
        return f.read()


def download_zip(url: str) -> zipfile.ZipFile:
    data = download(url)
    file = io.BytesIO(data)
    return zipfile.ZipFile(file)


def load_files(metadata_files: list[zipfile.ZipPath]) -> Metadata:
    js = []
    for zfile in metadata_files:
        for zname in zfile.namelist():
            zpath = zipfile.Path(zfile, zname)
            js.extend(json.loads(zpath.read_text()))
    return Metadata(js)


def preprocess(meta: Metadata) -> Metadata:
    pp = Preprocessor()
    meta = pp.filter_public(meta)
    meta = pp.sort(meta)
    pp.patch_name_conflict(meta)
    pp.patch_keyword_name(meta)
    return meta


def enumerate_name(meta: Metadata) -> Iterable[str]:
    for td in meta.type_definitions:
        if td.name == "Apis":
            for fd in td.fields:
                yield f"{td.namespace}.{fd.name}"
            for md in td.methods:
                yield f"{td.namespace}.{md.name}"
        elif td.is_win32 and td.basetype == "System.Enum" and not td.custom_attributes.has_scoped_enum():
            yield td.fullname
            for fd in td.fields[1:]:
                yield f"{td.namespace}.{fd.name}"
        else:
            yield td.fullname


def main() -> None:
    parser = argparse.ArgumentParser(description="API index")
    parser.add_argument("--loglevel", default="WARNING")
    parser.add_argument("-o", "--out", help="out file")
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, force=True)

    meta = load_files(
        [
            download_zip(
                "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Windows.SDK.Win32Metadata.68.0.4-preview.zip"
            ),
            download_zip(
                "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Windows.SDK.Contracts.10.0.26100.7175.zip"
            ),
            download_zip(
                "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.WindowsAppSDK.1.8.251106002.zip"
            ),
            download_zip(
                "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Web.WebView2.1.0.3595.46.zip"
            ),
            download_zip(
                "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Graphics.Win2D.1.3.2.zip"
            ),
        ]
    )

    meta = preprocess(meta)

    if args.out is None:
        writer = sys.stdout
    else:
        writer = open(args.out, "w")

    with writer:
        for name in sorted(enumerate_name(meta)):
            writer.write(f"{name}\n")


if __name__ == "__main__":
    main()
