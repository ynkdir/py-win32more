import argparse
import ast
import io
from glob import glob
from pathlib import Path


def find_import(file: str) -> list[str]:
    dependencies = []
    tree = ast.parse(Path(file).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                dependencies.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            names = []
            p = Path(file)
            for _ in range(node.level):
                p = p.parent
                names.insert(0, p.name)
            if node.module is None:
                for alias in node.names:
                    module = ".".join(names + [alias.name])
                    dependencies.append(module)
            else:
                module = ".".join(names + [node.module])
                dependencies.append(module)
    return dependencies


def filename_to_modulename(file: str) -> str:
    p = Path(file)
    module = p.stem
    while (p.parent / "__init__.py").exists():
        p = p.parent
        module = f"{p.name}.{module}"
    return module


def graph_import(files: list[str]) -> str:
    graph = {}
    for file in files:
        module = filename_to_modulename(file)
        graph[module] = find_import(file)
    return graph


def remove_external(graph: dict, files: list[str]) -> dict:
    toplevels = set()
    for file in files:
        toplevels.add(filename_to_modulename(file).split(".")[0])

    filtered = {}
    for module, dependencies in graph.items():
        deps = [name for name in dependencies if name.split(".")[0] in toplevels]
        if deps:
            filtered[module] = deps
    return filtered


def render_graph(graph: dict) -> str:
    writer = io.StringIO()
    writer.write("graph TB\n")
    for module, dependencies in graph.items():
        for dependency in dependencies:
            writer.write(f"    {module}-->{dependency}\n")
    return writer.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    files = []
    for file in args.files:
        files.extend(glob(file, recursive=True))

    graph = graph_import(files)
    graph = remove_external(graph, files)
    print(render_graph(graph))


if __name__ == "__main__":
    main()
