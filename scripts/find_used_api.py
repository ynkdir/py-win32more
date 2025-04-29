import argparse
import ast
from collections.abc import Iterable

PACKAGE_NAME = "win32more"


def find_used_api(tree: ast.AST) -> set[str]:
    names = set()

    modules = {}
    for asname, name in find_imported_modules(tree):
        if name.startswith(PACKAGE_NAME):
            modules[asname] = name
    modules_sorted = sorted(modules.items(), key=lambda x: len(x[0]), reverse=True)

    for fullname in find_imported_names(tree):
        if fullname.startswith(PACKAGE_NAME):
            names.add(fullname)

    for fullname in find_attributes(tree):
        for asname, name in modules_sorted:
            if fullname.startswith(f"{asname}."):
                # fullname can be Foo.Bar.Class.StaticMethod
                attr_index = len(asname.split("."))
                attr = fullname.split(".")[attr_index]
                names.add(f"{name}.{attr}")
                break

    return names


def find_imported_modules(tree: ast.AST) -> Iterable[tuple[str, str]]:
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname is None:
                    yield alias.name, alias.name
                else:
                    yield alias.asname, alias.name


def find_imported_names(tree: ast.AST) -> Iterable[str]:
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                yield f"{node.module}.{alias.name}"


def find_attributes(tree: ast.AST) -> Iterable[str]:
    visited: set[ast.AST] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            if node in visited:
                continue
            try:
                yield attribute_str(node, visited)
            except ValueError:
                pass


def attribute_str(node: ast.AST, visited: set[ast.AST]) -> str:
    visited.add(node)
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return attribute_str(node.value, visited) + "." + node.attr
    else:
        raise ValueError("not simple context")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("pyfile")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    with open(args.pyfile) as f:
        src = f.read()

    tree = ast.parse(src)

    for name in sorted(find_used_api(tree)):
        print(name)


if __name__ == "__main__":
    main()
