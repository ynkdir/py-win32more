import keyword
import logging

from .backport import removeprefix
from .metadata import Metadata, MethodDefinition, TypeDefinition

logger = logging.getLogger(__name__)


class Preprocessor:
    def preprocess(self, meta: Metadata) -> Metadata:
        meta = self.filter_public(meta)
        meta = self.sort(meta)
        self.patch_name_conflict(meta)
        self.patch_keyword_name(meta)
        self.patch_unicode_alias(meta)
        self.patch_UniversalBGTask_Task(meta)
        return meta

    def filter_public(self, meta: Metadata) -> Metadata:
        return Metadata([td.js for td in meta.type_definitions if self.is_public(td)])

    def is_public(self, td: TypeDefinition) -> bool:
        if td.is_winrt:
            return td.namespace != "" and td.basetype != "System.Attribute"
        else:
            return td.namespace != "" and "Public" in td.attributes

    def sort(self, meta: Metadata) -> Metadata:
        return Metadata(sorted(meta.js, key=lambda td: (td["Namespace"], td["Name"])))

    def patch_name_conflict(self, meta: Metadata) -> None:
        names = self._names_without_constant_and_non_scoped_enum(meta)
        for td in meta.type_definitions:
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
        for td in meta.type_definitions:
            if td.name == "Apis":
                for md in td.methods:
                    names.add(f"{td.namespace}.{md.name}")
            else:
                names.add(td.fullname)
        return names

    def patch_keyword_name(self, meta: Metadata) -> None:
        for td in meta.type_definitions:
            self.patch_keyword_name_td(td, td.fullname)

    def patch_keyword_name_td(self, td: TypeDefinition, namespace: str) -> None:
        for md in td.methods:
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

    # Remove "name" to be overwritten with "nameW".
    # Except: RoOriginateError(HSTRING), RoTransformError(HSTRING)
    # Some api have no A name.  e.g. GetEnvironmentStrings(ANSI) and GetEnvironmentStringsW(UNICODE)
    # FIXME: name conflict Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY(enum) Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W(struct)
    def patch_unicode_alias(self, meta: Metadata) -> None:
        type_definitions = []
        td_basetype = {td.fullname: td.basetype for td in meta.type_definitions}
        for td in meta.type_definitions:
            if td.fullname == "Windows.Win32.System.WinRT.Apis":
                for md in td.methods:
                    if md.name in {"RoOriginateErrorW", "RoTransformErrorW"}:
                        logger.debug(f"unicode alias: remove UnicodeAttribute: {td.namespace}.{md.name}")
                        self._remove_unicode_attribute(md)
            elif td.custom_attributes.has_unicode():
                if td.name.endswith("_W"):
                    alias_name = td.fullname.removesuffix("_W")
                elif td.name.endswith("W"):
                    alias_name = td.fullname.removesuffix("W")
                else:
                    assert False
                if alias_name in td_basetype and td.basetype != td_basetype[alias_name]:
                    logger.warning(f"unicode alias: cannot overwrite: {alias_name}")
                    self._remove_unicode_attribute(td)
        td_unicode_names = {td.fullname for td in meta.type_definitions if td.custom_attributes.has_unicode()}
        for td in meta.type_definitions:
            if {f"{td.fullname}W", f"{td.fullname}_W"} & td_unicode_names:
                logger.debug(f"unicode alias: overwrite: {td.fullname}")
            else:
                type_definitions.append(td.js)
            if td.name == "Apis":
                for fd in td.fields:
                    assert not fd.custom_attributes.has_ansi() and not fd.custom_attributes.has_unicode()
                methods = []
                md_unicode_names = {md.name for md in td.methods if md.custom_attributes.has_unicode()}
                for md in td.methods:
                    if {f"{md.name}W", f"{md.name}_W"} & md_unicode_names:
                        logger.debug(f"unicode alias: overwrite: {td.namespace}.{md.name}")
                    else:
                        methods.append(md.js)
                td["Methods"] = methods
        meta.js = type_definitions

    def _remove_unicode_attribute(self, df: TypeDefinition | MethodDefinition) -> None:
        df["CustomAttributes"] = [
            ca for ca in df["CustomAttributes"] if ca["Type"] != "Windows.Win32.Foundation.Metadata.UnicodeAttribute"
        ]

    # Workaround for invalid method name.  How to handle this?
    def patch_UniversalBGTask_Task(self, meta: Metadata) -> None:
        for td in meta.type_definitions:
            if td.fullname == "Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.Task":
                methods = []
                for md in td["Methods"]:
                    if md["Name"] == "Windows.ApplicationModel.Background.IBackgroundTask.Run":
                        # remove
                        continue
                    if md["Name"] == "Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.ITask.Run":
                        md["Name"] = "Run"
                    methods.append(md)
                td["Methods"] = methods
                break
