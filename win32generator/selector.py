import re
from collections import defaultdict
from collections.abc import Iterable, Mapping
from pathlib import Path

from .dependencies import Dependencies
from .metadata import Metadata, TypeDefinition


class Selector:
    def __init__(self, selector_file: Path) -> None:
        self._selectors = self._read_selector(selector_file)
        self._selected: set[str] = set()
        self._ns: Mapping[str, list[TypeDefinition]] = defaultdict(list)

    def _read_selector(self, selector_file: Path) -> set[str]:
        selectors = set()
        for line in selector_file.read_text().splitlines():
            line = re.sub(r"#.*", "", line).strip()
            if line != "":
                selectors.add(line)
        return selectors

    def _is_match(self, name) -> bool:
        return name in self._selectors

    def select(self, meta: Metadata) -> Metadata:
        self._init_namespace(meta)
        for td in meta.type_definitions:
            self._select_match_and_dependencies(td)
        for td in meta.type_definitions:
            self._select_members_inplace(td)
        return Metadata([td.js for td in meta.type_definitions if td.fullname in self._selected])

    def _init_namespace(self, meta: Metadata) -> None:
        self._ns = defaultdict(list)
        for td in meta.type_definitions:
            if td.name == "Apis":
                continue
            self._ns[td.fullname].append(td)

    def _select_match_and_dependencies(self, td: TypeDefinition) -> None:
        if self._is_match(td.namespace) or self._is_match(td.name) or self._is_match(td.fullname):
            self._selected.add(td.fullname)
            self._select_dependencies(Dependencies(td))

        if td.name == "Apis":
            for fd in td.fields:
                if self._is_match(fd.name) or self._is_match(f"{td.namespace}.{fd.name}"):
                    self._selected.add(td.fullname)
                    self._selected.add(f"{td.namespace}.{fd.name}")
                    self._select_dependencies(Dependencies(fd))
            for md in td.methods:
                if self._is_match(md.name) or self._is_match(f"{td.namespace}.{md.name}"):
                    self._selected.add(td.fullname)
                    self._selected.add(f"{td.namespace}.{md.name}")
                    self._select_dependencies(Dependencies(md))
        elif td.basetype == "System.Enum" and td.is_win32 and not td.custom_attributes.has_scoped_enum():
            for fd in td.fields[1:]:
                if self._is_match(fd.name) or self._is_match(f"{td.namespace}.{fd.name}"):
                    self._selected.add(td.fullname)
                    self._selected.add(f"{td.fullname}.{fd.name}")
                    self._select_dependencies(Dependencies(td))

    def _select_dependencies(self, dependencies: Iterable[str]) -> None:
        for fullname in dependencies:
            if fullname in self._selected:
                continue
            if fullname not in self._ns:
                continue
            self._selected.add(fullname)
            for td in self._ns[fullname]:
                self._select_dependencies(Dependencies(td))

    def _select_members_inplace(self, td: TypeDefinition) -> None:
        if td.name == "Apis":
            td["Fields"] = [fd for fd in td["Fields"] if f"{td['Namespace']}.{fd['Name']}" in self._selected]
            td["Methods"] = [md for md in td["Methods"] if f"{td['Namespace']}.{md['Name']}" in self._selected]
        elif td.basetype == "System.Enum" and td.is_win32 and not td.custom_attributes.has_scoped_enum():
            constants = [fd for fd in td["Fields"][1:] if f"{td.fullname}.{fd['Name']}" in self._selected]
            if constants:
                # Some constants are selected explicitly.  Export them only.
                td["Fields"] = [td["Fields"][0]] + constants
