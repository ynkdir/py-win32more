import argparse
import json
import logging
import lzma
import zipfile
from io import StringIO
from pathlib import Path
from typing import TextIO

from . import win32, win32raw, winrt
from .metadata import Metadata
from .package import Package
from .preprocessor import Preprocessor
from .selector import Selector

logger = logging.getLogger(__name__)


def xread_text(path: Path | zipfile.Path) -> str:
    if path.suffix == ".xz":
        return lzma.decompress(path.read_bytes()).decode()
    return path.read_text()


def load_files(metadata_files: list[Path]) -> Metadata:
    js = []
    for path in metadata_files:
        if path.suffix == ".zip":
            with zipfile.ZipFile(path) as zfile:
                for zname in zfile.namelist():
                    zpath = zipfile.Path(zfile, zname)
                    js.extend(json.loads(xread_text(zpath)))
        else:
            js.extend(json.loads(xread_text(path)))
    return Metadata(js)


def preprocess(meta: Metadata) -> Metadata:
    preprocessor = Preprocessor()
    return preprocessor.preprocess(meta)


def select(meta: Metadata, selector_file: Path) -> Metadata:
    selector = Selector(selector_file)
    return selector.select(meta)


def parse(meta: Metadata, package: Package) -> None:
    win32_parser = win32.Parser(package)
    winrt_parser = winrt.Parser(package)
    for td in meta.type_definitions:
        if td.is_win32:
            win32_parser.parse(td)
        else:
            winrt_parser.parse(td)


def make_module_path_for_write(namespace: str, package_directory: Path) -> TextIO:
    p = package_directory / namespace.replace(".", "/")
    p.mkdir(parents=True, exist_ok=True)
    return (p / "__init__.py").open("w")


def generate(package: Package, package_directory: Path) -> None:
    for module in package.modules():
        with make_module_path_for_write(module.namespace, package_directory) as writer:
            writer.write(module.emit_header())
            for item in module.items():
                writer.write(item.emit())
            writer.write("\n\nmake_ready(__name__)\n")


def generate_one(package: Package, out: Path) -> None:
    writer = StringIO()
    if has_winrt(package):
        # NOTE: winrt one module will not work mostly due to name conflict.
        writer.write(winrt.WinrtModule.emit_header_one(package.name))
    else:
        writer.write(win32.Win32Module.emit_header_one(package.name))
    for module in package.modules():
        writer.write(f"\n\n# {module.namespace}\n")
        for item in module.items():
            writer.write(item.emit())
    writer.write("\n\nmake_ready(__name__)\n")
    out.write_text(writer.getvalue())


def generate_raw(meta: Metadata, out: Path) -> None:
    module = win32raw.Win32RawModule()
    parser = win32raw.Parser(module)
    for td in meta.type_definitions:
        if td.is_winrt:
            raise NotImplementedError("Winrt is not supported")
        parser.parse(td)
    out.write_text(module.emit())


def has_winrt(package: Package) -> bool:
    for module in package.modules():
        if isinstance(module, winrt.WinrtModule):
            return True
    return False


def warn_missing_type(package: Package):
    missing_types = set()
    for module in package.modules():
        for fullname in module.enumerate_dependencies():
            namespace, name = fullname.rsplit(".", 1)
            if namespace not in package or name not in package[namespace]:
                missing_types.add(fullname)
    for fullname in sorted(missing_types):
        logger.warning(f"missing type: {fullname}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Metadata to Python generator")
    parser.add_argument("--loglevel", default="WARNING")
    parser.add_argument("-o", "--one", type=Path, help="out to one file")
    parser.add_argument("-s", "--selector", type=Path, help="selector.txt")
    parser.add_argument("--raw", action="store_true", help="generate raw bindings")
    parser.add_argument("--package-name", default="win32more")
    parser.add_argument("--output-directory", type=Path, default="src")
    parser.add_argument("metadata", nargs="+", type=Path, help="metadata.json")
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)

    if not args.output_directory.is_dir():
        raise RuntimeError(f"{args.output_directory} is not directory")

    if args.raw and args.one is None:
        raise RuntimeError("--raw requires --one option")

    if args.raw and args.selector is None:
        raise RuntimeError("--raw requires --selector option")

    meta = load_files(args.metadata)

    meta = preprocess(meta)

    if args.selector is not None:
        meta = select(meta, args.selector)

    if args.raw:
        generate_raw(meta, args.one)
        return

    package = Package(args.package_name, bool(args.one))

    parse(meta, package)

    if args.one is None:
        generate(package, args.output_directory / package.name)
    else:
        generate_one(package, args.one)

    warn_missing_type(package)


if __name__ == "__main__":
    main()
