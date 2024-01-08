import keyword
import logging

from .backport import removeprefix
from .metadata import Metadata, TypeDefinition

logger = logging.getLogger(__name__)


class Preprocessor:
    def filter_public(self, meta: Metadata) -> Metadata:
        return Metadata(td for td in meta if self.is_public(td))

    def is_public(self, td: TypeDefinition) -> bool:
        if td.is_winrt:
            return td.namespace != "" and td.basetype != "System.Attribute"
        else:
            return td.namespace != "" and "Public" in td.attributes

    def sort(self, meta: Metadata) -> Metadata:
        return Metadata(sorted(meta, key=lambda td: (td.namespace, td.name)))

    def patch_name_conflict(self, meta: Metadata) -> None:
        names = self._names_without_constant_and_non_scoped_enum(meta)
        for td in meta:
            if td.name == "Apis":
                for fd in td.fields:
                    if f"{td.namespace}.{fd.name}" in names:
                        logger.warning(f"constant name conflict '{td.namespace}.{fd.name}'")
                        fd["Name"] = f"{fd['Name']}_CONSTANT"
            elif td.basetype == "System.Enum":
                if td.is_winrt or td.custom_attributes.has_scoped_enum():
                    continue
                if td.fullname == "Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY":
                    for fd in td.fields[1:]:
                        if fd.name == "VK_F":
                            # VK_F is manually added by win32metadata/.../enums.json and is conflict with struct VK_F.
                            #   enum Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY.VK_F
                            # struct Windows.Win32.UI.Input.KeyboardAndMouse.VK_F
                            logger.info(f"enum rename '{td.fullname}.{fd.name}'")
                            fd["Name"] = f"{fd['Name']}_"
                            break
                # assert
                for fd in td.fields[1:]:
                    if f"{fd.name}" in names:
                        logger.error(f"enum name conflict '{td.fullname}.{fd.name}'")
                        raise ValueError()

    def _names_without_constant_and_non_scoped_enum(self, meta: Metadata) -> set[str]:
        names = set()
        for td in meta:
            if td.name == "Apis":
                for md in td.method_definitions:
                    names.add(f"{td.namespace}.{md.name}")
            else:
                names.add(td.fullname)
        return names

    def patch_keyword_name(self, meta: Metadata) -> None:
        for td in meta:
            self.patch_keyword_name_td(td, td.fullname)

    def patch_keyword_name_td(self, td: TypeDefinition, namespace: str) -> None:
        for md in td.method_definitions:
            if "SpecialName" in md.attributes:
                for prefix in ("get_", "put_", "add_", "remove_"):
                    if md.name.startswith(prefix) and keyword.iskeyword(removeprefix(md.name, prefix)):
                        logger.debug(f"keyword name {namespace}.{md.name}")
                        md["Name"] = md["Name"] + "_"
                        break
            for pa in md.parameters:
                if keyword.iskeyword(pa["Name"]):
                    logger.debug(f"keyword name {namespace}.{md.name}.{pa.name}")
                    pa["Name"] = pa["Name"] + "_"
        for fd in td.fields:
            if keyword.iskeyword(fd["Name"]):
                logger.debug(f"keyword name {namespace}.{fd.name}")
                fd["Name"] = fd["Name"] + "_"
        for nested_type in td.nested_types:
            self.patch_keyword_name_td(nested_type, namespace=namespace + "." + nested_type.name)
