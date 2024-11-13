import argparse
import json
import logging
import lzma
import sys
from collections.abc import Iterable
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from win32generator import resources
from win32generator.metadata import Metadata
from win32generator.preprocessor import Preprocessor

logger = logging.getLogger(__name__)


def xread_text(path: str) -> str:
    if path.endswith(".xz"):
        return lzma.decompress(Path(path).read_bytes()).decode()
    return Path(path).read_text()


def load_files(metadata_files: list[str]) -> Metadata:
    js = []
    for file in metadata_files:
        js.extend(json.loads(xread_text(file)))
    return Metadata(js)


def load_resources(metadata_files: list[str]) -> Metadata:
    js = []
    for file in metadata_files:
        js.extend(json.loads(resources.read_text(file)))
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
    parser = argparse.ArgumentParser(description="Metadata to Python generator")
    parser.add_argument("--loglevel", default="WARNING")
    parser.add_argument("-o", "--out", help="out file")
    parser.add_argument("metadata", nargs="*", help="metadata.json")
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)

    if args.metadata:
        meta = load_files(args.metadata)
    else:
        meta = load_resources(
            ["metadata/Windows.Win32.json.xz", "metadata/WindowsSDK.json.xz", "metadata/WindowsAppSDK.json.xz"]
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
