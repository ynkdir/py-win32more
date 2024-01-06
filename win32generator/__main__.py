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

logger = logging.getLogger(__name__)


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


def parse(meta: Metadata, package: Package) -> None:
    win32_parser = win32.Parser(package)
    winrt_parser = winrt.Parser(package)
    for td in meta:
        if td.is_win32:
            win32_parser.parse(td)
        else:
            winrt_parser.parse(td)


def make_module_path_for_write(namespace: str, package_directory: Path) -> TextIO:
    p = package_directory / namespace.replace(".", "/")
    p.mkdir(parents=True, exist_ok=True)
    d = p
    while d != package_directory:
        if not (d / "__init__.py").exists():
            (d / "__init__.py").write_text("")
        d = d.parent
    return (p / "__init__.py").open("w")


def generate(package: Package, package_directory: Path) -> None:
    missing_types = set()
    for module in package.modules():
        import_namespaces = {module.namespace}
        for fullname in module.enumerate_dependencies():
            namespace, name = fullname.rsplit(".", 1)
            if namespace not in package or name not in package[namespace]:
                missing_types.add(fullname)
            import_namespaces.add(namespace)
        with make_module_path_for_write(module.namespace, package_directory) as writer:
            writer.write(module.emit_header(import_namespaces))
            for item in module.items():
                writer.write(item.emit())
            writer.write("\n\nmake_ready(__name__)\n")
    for fullname in sorted(missing_types):
        logger.warning(f"missing type: {fullname}")


# FIXME: not work for winrt
def generate_one(package: Package, writer: TextIO) -> None:
    missing_types = set()
    for i, module in enumerate(package.modules()):
        for fullname in module.enumerate_dependencies():
            namespace, name = fullname.rsplit(".", 1)
            if namespace not in package or name not in package[namespace]:
                missing_types.add(fullname)
        if i == 0:
            writer.write(module.emit_header(set()))
        writer.write(f"\n\n# {module.namespace}\n")
        for item in module.items():
            writer.write(item.emit())
    writer.write("\n\nmake_ready(__name__)\n")
    for fullname in sorted(missing_types):
        logger.warning(f"missing type: {fullname}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Metadata to Python generator")
    parser.add_argument("--loglevel", default="WARNING")
    parser.add_argument("-o", "--one", help="out to one file")
    parser.add_argument("-s", "--selector", help="selector.txt")
    parser.add_argument("--package-name", default="win32more")
    parser.add_argument("--output-directory", default=".")
    parser.add_argument("metadata", nargs="+", help="metadata.json")
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)

    output_directory = Path(args.output_directory)

    if not output_directory.is_dir():
        raise RuntimeError(f"{output_directory} is not directory")

    meta = load(args.metadata)

    meta = preprocess(meta)

    if args.selector is not None:
        meta = select(meta, args.selector)

    package = Package(args.package_name, bool(args.one))

    parse(meta, package)

    if args.one is None:
        generate(package, output_directory / package.name)
    else:
        with open(args.one, "w") as writer:
            generate_one(package, writer)


if __name__ == "__main__":
    main()
