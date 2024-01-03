import argparse
import json
import logging
import lzma
from pathlib import Path
from typing import TextIO

from . import win32, winrt
from .metadata import Metadata, TypeDefinition
from .package import Package
from .preprocessor import Preprocessor
from .selector import Selector


def xopen(path: str) -> TextIO | lzma.LZMAFile:
    if path.endswith(".xz"):
        return lzma.open(path)
    return open(path)


def load(metadata_files: list[str]) -> Metadata:
    js = []
    for file in metadata_files:
        with xopen(file) as f:
            js.extend(json.load(f))
    return Metadata(TypeDefinition(typedef) for typedef in js)


def preprocess(meta: Metadata) -> Metadata:
    pp = Preprocessor()
    meta = pp.filter_public(meta)
    meta = pp.sort(meta)
    pp.patch_enum(meta)
    pp.patch_name_conflict(meta)
    pp.patch_keyword_name(meta)
    return meta


def select(meta: Metadata, selector_file: str) -> Metadata:
    selector = Selector()
    selector.read_selector(Path(selector_file))
    return Metadata(selector.select(meta))


def parse(meta: Metadata) -> Package:
    package = Package()
    win32_parser = win32.Parser(package)
    winrt_parser = winrt.Parser(package)
    for td in meta:
        if td.is_win32:
            win32_parser.parse(td)
        else:
            winrt_parser.parse(td)
    return package


def make_module_path_for_write(namespace) -> TextIO:
    root = Path(Package.directory)
    p = root / Package.name / namespace.replace(".", "/")
    p.mkdir(parents=True, exist_ok=True)
    d = p
    while d != root:
        if not (d / "__init__.py").exists():
            (d / "__init__.py").write_text("")
        d = d.parent
    return (p / "__init__.py").open("w")


def generate(package: Package) -> None:
    for module in package.modules():
        import_namespaces = set(module.enumerate_imported_namespaces()) | {module.namespace}
        with make_module_path_for_write(module.namespace) as writer:
            writer.write(module.emit_header(import_namespaces))
            for item in module.items():
                writer.write(item.emit())
            writer.write("\n\nmake_ready(__name__)\n")


# FIXME: not work for winrt
def generate_one(package: Package, writer: TextIO) -> None:
    for i, module in enumerate(package.modules()):
        if i == 0:
            writer.write(module.emit_header(set()))
        writer.write(f"\n\n# {module.namespace}\n")
        for item in module.items():
            writer.write(item.emit())
    writer.write("\n\nmake_ready(__name__)\n")


def build(metadata_files, selector_file=None, one=None) -> None:
    meta = load(metadata_files)

    meta = preprocess(meta)

    if selector_file is not None:
        meta = select(meta, selector_file)

    package = parse(meta)

    if one is None:
        generate(package)
    else:
        with open(one, "w") as writer:
            generate_one(package, writer)


def main() -> None:
    parser = argparse.ArgumentParser(description="Metadata to Python generator")
    parser.add_argument("--loglevel", default="WARNING")
    parser.add_argument("-o", "--one", help="out to one file")
    parser.add_argument("-s", "--selector", help="selector.txt")
    parser.add_argument("--package-name", default="win32more")
    parser.add_argument("--package-directory", default=".")
    parser.add_argument("metadata", nargs="+", help="metadata.json")
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)

    Package.name = args.package_name
    Package.directory = args.package_directory
    Package.is_onefile = args.one is not None

    if not Path(Package.directory).is_dir():
        raise RuntimeError(f"{Package.directory} is not directory")

    build(args.metadata, args.selector, args.one)


if __name__ == "__main__":
    main()
