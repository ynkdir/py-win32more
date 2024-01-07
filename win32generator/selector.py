import re
from collections.abc import Iterable, Mapping
from pathlib import Path

from .metadata import Metadata, TypeDefinition


class Selector:
    def __init__(self) -> None:
        self.selectors: set[str] = set()

    def read_selector(self, path: Path) -> None:
        for line in path.read_text().splitlines():
            line = re.sub(r"#.*", "", line).strip()
            if line != "":
                self.selectors.add(line)

    def is_match(self, name) -> bool:
        return name in self.selectors

    def is_match_any_fields(self, td: TypeDefinition) -> bool:
        for fd in td.fields:
            if self.is_match(fd.name):
                return True
            elif self.is_match(f"{td.namespace}.{fd.name}"):
                return True
        return False

    def is_match_any_method_definitions(self, td: TypeDefinition) -> bool:
        for md in td.method_definitions:
            if self.is_match(md.name):
                return True
            elif self.is_match(f"{td.namespace}.{md.name}"):
                return True
        return False

    def select(self, meta: Metadata) -> Iterable[TypeDefinition]:
        meta_group_by_fullname = self._group_by_fullname(meta)
        selected = set()
        for td in self.find_match(meta):
            if id(td) in selected:
                continue
            selected.add(id(td))
            if td.name == "Apis":
                self.select_object_members_inplace(td)
            yield td
            yield from self.select_dependencies(td, meta_group_by_fullname, selected)

    def _group_by_fullname(self, meta: Metadata) -> Mapping[str, Metadata]:
        meta_group_by_fullname = {}
        for td in meta:
            if td.fullname not in meta_group_by_fullname:
                meta_group_by_fullname[td.fullname] = Metadata()
            meta_group_by_fullname[td.fullname].append(td)
        return meta_group_by_fullname

    def select_dependencies(
        self, td: TypeDefinition, meta_group_by_fullname: Mapping[str, Metadata], selected: set[int]
    ) -> Iterable[TypeDefinition]:
        for fullname_depended in td.enumerate_dependencies():
            if fullname_depended not in meta_group_by_fullname:
                continue
            for td_depended in meta_group_by_fullname[fullname_depended]:
                if id(td_depended) in selected:
                    continue
                selected.add(id(td_depended))
                yield td_depended
                yield from self.select_dependencies(td_depended, meta_group_by_fullname, selected)

    def select_object_members_inplace(self, td: TypeDefinition) -> None:
        fields = []
        for fd in td["Fields"]:
            if self.is_match(fd["Name"]):
                fields.append(fd)
            elif self.is_match(f"{td.namespace}.{fd['Name']}"):
                fields.append(fd)
        td["Fields"] = fields
        method_definitions = []
        for md in td["MethodDefinitions"]:
            if self.is_match(md["Name"]):
                method_definitions.append(md)
            elif self.is_match(f"{td.namespace}.{md['Name']}"):
                method_definitions.append(md)
        td["MethodDefinitions"] = method_definitions

    def find_match(self, meta: Metadata) -> Iterable[TypeDefinition]:
        for td in meta:
            if self.is_match(td.namespace):
                yield td
            elif self.is_match(td.name):
                yield td
            elif self.is_match(td.fullname):
                yield td
            elif td.name == "Apis":
                if self.is_match_any_fields(td):  # constants
                    yield td
                elif self.is_match_any_method_definitions(td):  # functions
                    yield td
            elif td.basetype == "System.Enum":
                if self.is_match_any_fields(td):
                    yield td
