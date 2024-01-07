import re
from collections import defaultdict
from collections.abc import Iterable, Mapping
from pathlib import Path

from .metadata import Metadata, TypeDefinition


class Selector:
    def __init__(self, path: Path) -> None:
        self._selectors = self._read_selector(path)
        self._selected: set[str] = set()
        self._ns: Mapping[str, list[TypeDefinition]] = defaultdict(list)

    def _read_selector(self, path: Path) -> set[str]:
        selectors = set()
        for line in path.read_text().splitlines():
            line = re.sub(r"#.*", "", line).strip()
            if line != "":
                selectors.add(line)
        return selectors

    def _is_match(self, name) -> bool:
        return name in self._selectors

    def select(self, meta: Metadata) -> Iterable[TypeDefinition]:
        self._init_namespace(meta)
        for td in meta:
            self._select_match_and_dependencies(td)
        return [td for td in meta if self._is_selected(td)]

    def _init_namespace(self, meta: Metadata) -> None:
        self._ns = defaultdict(list)
        for td in meta:
            if td.name == "Apis":
                continue
            self._ns[td.fullname].append(td)

    def _select_match_and_dependencies(self, td: TypeDefinition) -> None:
        if self._is_match(td.namespace):
            self._selected.add(td.namespace)
        elif self._is_match(td.name) or self._is_match(td.fullname):
            self._selected.add(td.fullname)
            self._select_dependencies(list(td.enumerate_dependencies()))
        elif td.name == "Apis":
            for fd in td.fields:
                if self._is_match(fd.name) or self._is_match(f"{td.namespace}.{fd.name}"):
                    self._selected.add(f"{td.namespace}.{fd.name}")
                    self._select_dependencies(list(fd.enumerate_dependencies()))
            for md in td.method_definitions:
                if self._is_match(md.name) or self._is_match(f"{td.namespace}.{md.name}"):
                    self._selected.add(f"{td.namespace}.{md.name}")
                    self._select_dependencies(list(md.enumerate_dependencies()))
        elif td.basetype == "System.Enum":
            if td.is_winrt or not td.custom_attributes.has_scoped_enum():
                return
            for fd in td.fields[1:]:
                if self._is_match(fd.name) or self._is_match(f"{td.fullname}.{fd.name}"):
                    self._selected.add(td.fullname)
                    break

    def _select_dependencies(self, dependencies: list[str]) -> None:
        for fullname in dependencies:
            if fullname in self._selected:
                continue
            if fullname not in self._ns:
                continue
            self._selected.add(fullname)
            for td in self._ns[fullname]:
                self._select_dependencies(list(td.enumerate_dependencies()))

    def _is_selected(self, td: TypeDefinition) -> bool:
        if td.namespace in self._selected:
            return True
        elif td.fullname in self._selected:
            return True
        elif td.name == "Apis":
            td["Fields"] = [fd for fd in td["Fields"] if f"{td['Namespace']}.{fd['Name']}" in self._selected]
            td["MethodDefinitions"] = [
                md for md in td["MethodDefinitions"] if f"{td['Namespace']}.{md['Name']}" in self._selected
            ]
            if td["Fields"] or td["MethodDefinitions"]:
                return True
        return False
