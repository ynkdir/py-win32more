from __future__ import annotations
import json
import keyword
import re
import sys
from pathlib import Path
from typing import TypeAlias, Generator, Any, TextIO, Self

PACKAGE_NAME = "win32more"
BASE_EXPORTS = [
    "ARCH",
    "MissingType",
    "c_char_p_no",
    "c_wchar_p_no",
    "Byte",
    "SByte",
    "Char",
    "Int16",
    "UInt16",
    "Int32",
    "UInt32",
    "Int64",
    "UInt64",
    "IntPtr",
    "UIntPtr",
    "Single",
    "Double",
    "String",
    "Boolean",
    "Void",
    "Guid",
    "SUCCEEDED",
    "FAILED",
    "cfunctype",
    "winfunctype",
    "commethod",
    "cfunctype_pointer",
    "winfunctype_pointer",
    "press",
    "make_head",
]
BASE_EXPORTS_CSV = ", ".join(BASE_EXPORTS)

JsonType: TypeAlias = Any


class TType:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def kind(self) -> str:
        return self["Kind"]

    @property
    def name(self) -> str:
        if self["Name"] is None:
            raise KeyError()
        return self["Name"]

    @property
    def type(self) -> TType:
        if self["Type"] is None:
            raise KeyError()
        return TType(self["Type"])

    @property
    def size(self) -> int:
        if self["Size"] is None:
            raise KeyError()
        return self["Size"]

    @property
    def type_arguments(self) -> list[Self]:
        if self["TypeArguments"] is None:
            raise KeyError()
        return [TType(ta) for ta in self["TypeArguments"]]

    @property
    def is_required(self) -> bool:
        if self["IsRequired"] is None:
            raise KeyError()
        return self["IsRequired"]

    @property
    def pytype(self) -> str:
        match self.kind:
            case "Primitive":
                return self.name
            case "Pointer":
                if self.type.kind == "Primitive" and self.type.name == "Void":
                    return "c_void_p"
                elif self.type.kind == "Primitive" and self.type.name == "Byte":
                    return "c_char_p_no"  # safe?
                elif self.type.kind == "Primitive" and self.type.name == "Char":
                    return "c_wchar_p_no"  # safe?
                elif self.type.is_struct:
                    return f"POINTER({self.type.name}_head)"
                else:
                    return f"POINTER({self.type.pytype})"
            case "SZArray":
                raise NotImplementedError()
            case "Array":
                return f"{self.type.pytype} * {self.size}"
            case "Type":
                if self.is_nested:
                    return self.name[1:]  # remove first "."
                elif self.is_guid:
                    return "Guid"
                elif self.is_missing:
                    sys.stderr.write(f"DEBUG: missing type '{self.name}'\n")
                    return "MissingType"
                elif self.is_com:
                    return f"{self.name}_head"
                else:
                    return self.name
            case _:
                raise NotImplementedError()

    def get_element_type(self) -> TType:
        match self.kind:
            case "Pointer" | "SZArray" | "Array":
                return self.type.get_element_type()
            case "Primitive" | "Type":
                return self
            case _:
                raise NotImplementedError()

    # e.g. "._Anonymous_e_Struct"
    @property
    def is_nested(self) -> bool:
        return self.kind == "Type" and self.name.startswith(".")

    @property
    def is_guid(self) -> bool:
        return self.kind == "Type" and self.name == "System.Guid"

    # missing type which is not defined in current winmd.
    @property
    def is_missing(self) -> bool:
        return self.kind == "Type" and self["_typedef"] is None

    @property
    def is_struct(self) -> bool:
        if not self.is_nested and not self.is_guid and not self.is_missing:
            return self.kind == "Type" and self["_typedef"].kind in ("union", "struct")
        return False

    @property
    def is_com(self) -> bool:
        if not self.is_nested and not self.is_guid and not self.is_missing:
            return self.kind == "Type" and self["_typedef"].kind == "com"
        return False


class TypeDefinition:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def namespace(self) -> str:
        return self["Namespace"]

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def fullname(self) -> str:
        return f"{self.namespace}.{self.name}"

    @property
    def basetype(self) -> str | None:
        return self["BaseType"]

    @property
    def is_nested(self) -> bool:
        return self["IsNested"]

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(ca) for ca in self["CustomAttributes"]]

    @property
    def fields(self) -> list[FieldDefinition]:
        return [FieldDefinition(fd) for fd in self["Fields"]]

    @property
    def interface_implementations(self) -> list[InterfaceImplementation]:
        return [InterfaceImplementation(ii) for ii in self["InterfaceImplementations"]]

    @property
    def layout(self) -> TypeLayout:
        return TypeLayout(self["Layout"])

    @property
    def method_definitions(self) -> list[MethodDefinition]:
        return [MethodDefinition(md) for md in self["MethodDefinitions"]]

    @property
    def nested_types(self) -> list[TypeDefinition]:
        return [TypeDefinition(td) for td in self["NestedTypes"]]

    @property
    def kind(self) -> str:
        match self.basetype:
            case None:
                return "com"
            case "System.Object":
                return "object"  # CONSTANT, FUNCTION
            case "System.MulticastDelegate":
                return "function_pointer"
            case "System.Enum":
                return "enum"
            case "System.ValueType":
                if self.has_custom_attribute("Windows.Win32.Interop.NativeTypedefAttribute"):
                    return "native_typedef"
                # FIXME: CLSID_ComClass is defined as attribute like [uuid(...)] struct ComClass {}.
                elif self.has_custom_attribute("Windows.Win32.Interop.GuidAttribute") and not self.fields:
                    return "clsid"
                elif "ExplicitLayout" in self.attributes:
                    return "union"
                else:
                    return "struct"
            case _:
                raise NotImplementedError()

    def has_custom_attribute(self, type_: str) -> bool:
        for ca in self.custom_attributes:
            if ca.type == type_:
                return True
        return False

    def get_custom_attribute(self, type_: str) -> CustomAttribute:
        for ca in self.custom_attributes:
            if ca.type == type_:
                return ca
        raise KeyError()


class CustomAttribute:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def type(self) -> str:
        return self["Type"]

    @property
    def fixed_arguments(self) -> list[CustomAttributeFixedArgument]:
        return [CustomAttributeFixedArgument(ta) for ta in self["FixedArguments"]]

    @property
    def named_arguments(self) -> list[CustomAttributeNamedArgument]:
        return [CustomAttributeNamedArgument(na) for na in self["NamedArguments"]]

    def guid_value(self) -> tuple[str, list[JsonType]]:
        v = [fa.value for fa in self.fixed_arguments]
        guid = f"{v[0]:08x}-{v[1]:04x}-{v[2]:04x}-{v[3]:02x}-{v[4]:02x}-{v[5]:02x}-{v[6]:02x}-{v[7]:02x}-{v[8]:02x}-{v[9]:02x}-{v[10]:02x}"
        return guid, v[11:]


class CustomAttributeFixedArgument:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def type(self) -> TType:
        return TType(self["Type"])

    @property
    def value(self) -> JsonType:
        return self["Value"]


class CustomAttributeNamedArgument:
    def __init__(self, js: JsonType):
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def kind(self) -> str:
        return self["Kind"]

    @property
    def name(self) -> str | None:
        return self["Name"]

    @property
    def type(self) -> TType:
        return TType(self["Type"])

    @property
    def value(self) -> JsonType:
        return self["Value"]


class FieldDefinition:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def signature(self) -> TType:
        return TType(self["Signature"])

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(ca) for ca in self["CustomAttributes"]]

    @property
    def default_value(self) -> Constant:
        if self["DefaultValue"] is None:
            raise ValueError()
        return Constant(self["DefaultValue"])

    @property
    def offset(self) -> int:
        return self["Offset"]

    @property
    def pyvalue(self) -> str:
        if "HasDefault" in self.attributes:
            return ascii(self.default_value.value)
        elif self.signature.kind == "Type" and self.signature.name == "System.Guid":
            guid, rest = self.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
            assert len(rest) == 0
            return f"Guid('{guid}')"
        elif self.signature.kind == "Type" and self.signature.name == f"{PACKAGE_NAME}.Devices.Properties.DEVPROPKEY":
            guid, rest = self.get_custom_attribute("Windows.Win32.Interop.PropertyKeyAttribute").guid_value()
            assert len(rest) == 1
            return f"{self.signature.name}(fmtid=Guid('{guid}'), pid={rest[0]})"
        elif self.signature.kind == "Type" and self.signature.name == f"{PACKAGE_NAME}.UI.Shell.PropertiesSystem.PROPERTYKEY":
            guid, rest = self.get_custom_attribute("Windows.Win32.Interop.PropertyKeyAttribute").guid_value()
            assert len(rest) == 1
            return f"{self.signature.name}(fmtid=Guid('{guid}'), pid={rest[0]})"
        else:
            # FIXME:
            raise NotImplementedError()

    def get_custom_attribute(self, type_: str) -> CustomAttribute:
        for ca in self.custom_attributes:
            if ca.type == type_:
                return ca
        raise KeyError()


class Constant:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def type_code(self) -> str:
        return self["TypeCode"]

    @property
    def value(self) -> JsonType:
        return self["Value"]


class InterfaceImplementation:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def interface(self) -> EntiryHandle:
        return EntiryHandle(self["Interface"])

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(ca) for ca in self["CustomAttributes"]]


class EntiryHandle:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def kind(self) -> str:
        return self["Kind"]

    @property
    def type_reference(self) -> TypeReference:
        if self["TypeReference"] is None:
            raise KeyError()
        return TypeReference(self["TypeReference"])

    @property
    def type_specification(self) -> TypeSpecification:
        if self["TypeSpecification"] is None:
            raise KeyError()
        return TypeSpecification(self["TypeSpecification"])


class TypeReference:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def namespace(self) -> str:
        return self["Namespace"]

    @property
    def fullname(self) -> str:
        return f"{self.namespace}.{self.name}"


class TypeSpecification:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def signature(self) -> TType:
        return TType(self["Signature"])

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(ca) for ca in self["CustomAttributes"]]


class TypeLayout:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def is_default(self) -> bool:
        return self["IsDefault"]

    @property
    def packing_size(self) -> int:
        return self["PackingSize"]

    @property
    def size(self) -> int:
        return self["Size"]


class MethodDefinition:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(ca) for ca in self["CustomAttributes"]]

    @property
    def impl_attributes(self) -> list[str]:
        return self["ImplAttributes"]

    @property
    def import_(self) -> MethodImport:
        if self["Import"] is None:
            raise KeyError()
        return MethodImport(self["Import"])

    @property
    def signature(self) -> MethodSignature:
        return MethodSignature(self["Signature"])

    @property
    def parameters(self) -> list[Parameter]:
        return [Parameter(pa) for pa in self["Parameters"]]

    # SequenceNumber == 0 is return type and it can be missing.
    def get_parameter_names_with_type(self) -> list[tuple[str, TType]]:
        types = self.signature.parameter_types
        return [(pa.name, types[pa.sequence_number - 1]) for pa in self.parameters if pa.sequence_number != 0]

    def has_custom_attribute(self, type_: str) -> bool:
        for ca in self.custom_attributes:
            if ca.type == type_:
                return True
        return False

    def get_custom_attribute(self, type_: str) -> CustomAttribute:
        for ca in self.custom_attributes:
            if ca.type == type_:
                return ca
        raise KeyError()


class MethodSignature:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def generic_parameter_count(self) -> int:
        return self["GenericParameterCount"]

    @property
    def header(self) -> SignatureHeader:
        return SignatureHeader(self["Header"])

    @property
    def parameter_types(self) -> list[TType]:
        return [TType(pt) for pt in self["ParameterTypes"]]

    @property
    def required_parameter_count(self) -> int:
        return self["RequiredParameterCount"]

    @property
    def return_type(self) -> TType:
        return TType(self["ReturnType"])


class SignatureHeader:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def calling_convention(self) -> str:
        return self["CallingConvention"]

    @property
    def has_explicit_this(self) -> bool:
        return self["HasExplicitThis"]

    @property
    def is_generic(self) -> bool:
        return self["IsGeneric"]

    @property
    def is_instance(self) -> bool:
        return self["IsInstance"]

    @property
    def kind(self) -> str:
        return self["Kind"]


class Parameter:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def sequence_number(self) -> int:
        return self["SequenceNumber"]

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(ca) for ca in self["CustomAttributes"]]

    @property
    def default_value(self) -> Constant:
        if self["DefaultValue"] is None:
            raise ValueError()
        return Constant(self["DefaultValue"])


class MethodImport:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def module(self) -> ModuleReference:
        return ModuleReference(self["Module"])


class ModuleReference:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(ca) for ca in self["CustomAttributes"]]


class Preprocessor:
    def filter_public(self, typedefs: list[TypeDefinition]) -> list[TypeDefinition]:
        return [td for td in typedefs if td.namespace != "" and "Public" in td.attributes]

    def patch_link_typedef(self, typedefs: list[TypeDefinition]) -> None:
        # FIXME: ns's key can be duplicated with arch variation.  Don't care for now.
        ns = {td.fullname: td for td in typedefs}
        for td in typedefs:
            for ii in td.interface_implementations:
                ii.interface.type_reference["_typedef"] = ns[ii.interface.type_reference.fullname]
            for t in self.foreach_type(td):
                t = t.get_element_type()
                t["_typedef"] = ns.get(t["Name"])

    # FIXME: enum value name? (NAME or ENUM_NAME or ENUM.Name?)
    def patch_enum(self, typedefs: list[TypeDefinition]) -> None:
        for td in typedefs:
            if td.kind == "enum" and self.enum_need_prefix(td):
                for fd in td.fields:
                    fd["Name"] = f"{td['Name']}_{fd['Name']}"

    def enum_need_prefix(self, td: TypeDefinition) -> bool:
        for fd in td.fields:
            if not ("_" in fd.name or fd.name.isupper()):
                return True
        return False

    # Add vtbl_index to COM methods.
    def patch_com_vtbl_index(self, typedefs: list[TypeDefinition]) -> None:
        for td in typedefs:
            if td.kind == "com":
                vtbl_index = self.count_interface_method(td.interface_implementations)
                for md in td.method_definitions:
                    md["_vtbl_index"] = vtbl_index
                    vtbl_index += 1

    def count_interface_method(self, interfaces: list[InterfaceImplementation]) -> int:
        if not interfaces:
            return 0
        td = interfaces[0].interface.type_reference["_typedef"]
        return len(td.method_definitions) + self.count_interface_method(td.interface_implementations)

    def patch_name_conflict(self, typedefs: list[TypeDefinition]) -> None:
        ns = {td.fullname: td for td in typedefs}
        for td in typedefs:
            if td.name == "Apis":
                for fd in td.fields:
                    if f"{td.namespace}.{fd.name}" in ns:
                        sys.stderr.write(f"DEBUG: name conflict '{td.namespace}.{fd.name}'\n")
                        fd["Name"] = f"{fd['Name']}_CONSTANT"

    def patch_namespace(self, typedefs: list[TypeDefinition], packagename: str) -> None:
        def patch(name: str) -> str:
            return re.sub(r"^Windows.Win32.", f"{packagename}.", name)

        for td in typedefs:
            td["Namespace"] = patch(td["Namespace"])
            for ii in td.interface_implementations:
                ii.interface.type_reference["Namespace"] = patch(ii.interface.type_reference["Namespace"])
            for t in self.foreach_type(td):
                t = t.get_element_type()
                t["Name"] = patch(t["Name"])

    def patch_keyword_name(self, typedefs: list[TypeDefinition]) -> None:
        for td in typedefs:
            self.patch_keyword_name_td(td)

    def patch_keyword_name_td(self, td: TypeDefinition) -> None:
        for md in td.method_definitions:
            for pa in md.parameters:
                if keyword.iskeyword(pa["Name"]):
                    pa["Name"] = pa["Name"] + "_"
        for fd in td.fields:
            if keyword.iskeyword(fd["Name"]):
                fd["Name"] = fd["Name"] + "_"
        for nested_type in td.nested_types:
            self.patch_keyword_name_td(nested_type)

    def foreach_type(self, td: TypeDefinition) -> Generator[TType, None, None]:
        for fd in td.fields:
            yield fd.signature
        for md in td.method_definitions:
            yield md.signature.return_type
            yield from md.signature.parameter_types
        for nested_type in td.nested_types:
            yield from self.foreach_type(nested_type)

    def get_namespace(self, fullname: str) -> str:
        if "." not in fullname:
            return ""
        return fullname.rsplit(".", 1)[0]

    def collect_import_namespace(self, td: TypeDefinition, import_namespaces: set[str]) -> None:
        for ii in td.interface_implementations:
            import_namespaces.add(ii.interface.type_reference.namespace)
        for t in self.foreach_type(td):
            t = t.get_element_type()
            if t.kind == "Type" and not t.is_nested and not t.is_guid and not t.is_missing:
                import_namespaces.add(self.get_namespace(t.name))

    def collect_export_name(self, td: TypeDefinition, export_names: set[str]) -> None:
        match td.kind:
            case "object":
                for fd in td.fields:
                    export_names.add(fd.name)
                for md in td.method_definitions:
                    export_names.add(md.name)
            case "enum":
                export_names.add(td.name)
                for fd in td.fields[1:]:
                    export_names.add(fd.name)
            case "function_pointer" | "native_typedef" | "clsid" | "union" | "struct" | "com":
                export_names.add(td.name)
            case _:
                raise NotImplementedError()

    def collect_export_name_arch(self, td: TypeDefinition, export_names_arch: dict[str, set[str]]) -> None:
        if td.has_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            arch = td.get_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value
            if td.name not in export_names_arch:
                export_names_arch[td.name] = set()
            export_names_arch[td.name] |= {x.upper() for x in arch}
        if td.kind == "object":
            for md in td.method_definitions:
                if md.has_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute"):
                    arch = md.get_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value
                    if md.name not in export_names_arch:
                        export_names_arch[md.name] = set()
                    export_names_arch[md.name] |= {x.upper() for x in arch}


class PyGenerator:
    def emit(self, writer: TextIO, td: TypeDefinition) -> None:
        match td.kind:
            case "object":  # CONSTANT, FUNCTION
                self.emit_object(writer, td)
            case "function_pointer":
                self.emit_function_pointer(writer, td)
            case "enum":
                self.emit_enum(writer, td)
            case "native_typedef":
                self.emit_native_typedef(writer, td)
            case "clsid":
                self.emit_clsid(writer, td)
            case "union":
                self.emit_struct_union(writer, td)
            case "struct":
                self.emit_struct_union(writer, td)
            case "com":
                self.emit_com(writer, td)
            case _:
                raise NotImplementedError()

    def emit_object(self, writer: TextIO, td: TypeDefinition) -> None:
        for fd in td.fields:
            self.emit_constant(writer, fd)
        for md in td.method_definitions:
            self.emit_function(writer, md)

    def emit_constant(self, writer: TextIO, fd: FieldDefinition) -> None:
        if "HasDefault" in fd.attributes:
            # primitive
            writer.write(f"{fd.name}: {fd.signature.pytype} = {fd.pyvalue}\n")
        elif fd.signature.is_guid:
            writer.write(f"{fd.name}: Guid = {fd.pyvalue}\n")
        else:
            writer.write(f"def {fd.name}():\n")
            writer.write(f"    return {fd.pyvalue}\n")

    def emit_function(self, writer: TextIO, md: MethodDefinition) -> None:
        if md.has_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            arch = ",".join(md.get_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
            writer.write(f"if ARCH in '{arch}':\n")
            indent = "    "
        else:
            indent = ""
        library = md.import_.module.name
        if "CallingConventionWinApi" in md.import_.attributes:
            functype = "winfunctype"
        elif "CallingConventionCDecl" in md.import_.attributes:
            functype = "cfunctype"
        else:
            raise NotImplementedError()
        restype = md.signature.return_type.pytype
        params_csv = ", ".join(f"{name}: {type_.pytype}" for name, type_ in md.get_parameter_names_with_type())
        writer.write(f"{indent}@{functype}('{library}')\n")
        writer.write(f"{indent}def {md.name}({params_csv}) -> {restype}: ...\n")

    def emit_function_pointer(self, writer: TextIO, td: TypeDefinition) -> None:
        if td.has_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            arch = ",".join(td.get_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
            writer.write(f"if ARCH in '{arch}':\n")
            indent = "    "
        else:
            indent = ""
        callconv = td.get_custom_attribute("System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute").fixed_arguments[0].value
        if callconv == "Winapi":
            functype = "winfunctype_pointer"
        elif callconv == "Cdecl":
            functype = "cfunctype_pointer"
        else:
            raise NotImplementedError()
        md = td.method_definitions[1]  # [0]=.ctor, [1]=Invoke
        restype = md.signature.return_type.pytype
        params_csv = ", ".join(f"{name}: {type_.pytype}" for name, type_ in md.get_parameter_names_with_type())
        writer.write(f"{indent}@{functype}\n")
        writer.write(f"{indent}def {td.name}({params_csv}) -> {restype}: ...\n")

    def emit_enum(self, writer: TextIO, td: TypeDefinition) -> None:
        type_field, *value_fields = td.fields
        writer.write(f"{td.name} = {type_field.signature.pytype}\n")
        for fd in value_fields:
            writer.write(f"{fd.name}: {td.name} = {fd.default_value.value}\n")

    def emit_native_typedef(self, writer: TextIO, td: TypeDefinition) -> None:
        pytype = td.fields[0].signature.pytype
        writer.write(f"{td.name} = {pytype}\n")

    def emit_clsid(self, writer: TextIO, td: TypeDefinition) -> None:
        guid, rest = td.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
        writer.write(f"{td.name} = Guid('{guid}')\n")

    # _fields_ and _anonymous_ is defined at runtime.
    def emit_struct_union(self, writer: TextIO, td: TypeDefinition, indent="") -> None:
        if td.has_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            arch = ",".join(td.get_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
            writer.write(f"if ARCH in '{arch}':\n")
            indent = indent + "    "
        if td.kind == "struct":
            base = "Structure"
        elif td.kind == "union":
            base = "Union"
        else:
            raise NotImplementedError()
        if td.has_custom_attribute("Windows.Win32.Interop.GuidAttribute"):
            guid, rest = td.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
        else:
            guid = None
        fields = []
        static_fields = []
        for fd in td.fields:
            if {"Static", "HasDefault"} <= set(fd.attributes):
                static_fields.append(fd)
            else:
                fields.append(fd)
        writer.write(f"{indent}class {td.name}({base}):\n")
        if td.has_custom_attribute("Windows.Win32.Interop.GuidAttribute"):
            guid, rest = td.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
            writer.write(f"{indent}    Guid = Guid('{guid}')\n")
        elif not td.fields:
            writer.write(f"{indent}    pass\n")
            return
        for fd in static_fields:
            writer.write(f"{indent}    {fd.name} = {fd.pyvalue}\n")
        for fd in fields:
            writer.write(f"{indent}    {fd.name}: {fd.signature.pytype}\n")
        if td.layout.packing_size != 0:
            writer.write(f"{indent}    _pack_ = {td.layout.packing_size}\n")
        for nested_type in td.nested_types:
            self.emit_struct_union(writer, nested_type, indent + "    ")

    def emit_com(self, writer: TextIO, td: TypeDefinition) -> None:
        assert len(td.interface_implementations) <= 1
        if td.interface_implementations == []:
            base = "None"
        else:
            base = td.interface_implementations[0].interface.type_reference.fullname
        writer.write(f"class {td.name}(c_void_p):\n")
        writer.write(f"    extends: {base}\n")
        if td.has_custom_attribute("Windows.Win32.Interop.GuidAttribute"):
            guid, rest = td.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
            writer.write(f"    Guid = Guid('{guid}')\n")
        for md in td.method_definitions:
            restype = md.signature.return_type.pytype
            params_csv = ", ".join(f"{name}: {type_.pytype}" for name, type_ in md.get_parameter_names_with_type())
            vtbl_index = md["_vtbl_index"]
            writer.write(f"    @commethod({vtbl_index})\n")
            writer.write(f"    def {md.name}({params_csv}) -> {restype}: ...\n")

    def write_header(self, writer: TextIO, import_namespaces: set[str]) -> None:
        writer.write("from __future__ import annotations\n")
        writer.write("from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll\n")
        writer.write(f"from {PACKAGE_NAME}.base import {BASE_EXPORTS_CSV}\n")
        for namespace in sorted(import_namespaces):
            writer.write(f"import {namespace}\n")
        writer.write("import sys\n")
        writer.write("_module = sys.modules[__name__]\n")
        writer.write("def __getattr__(name):\n")
        writer.write("    try:\n")
        writer.write("        prototype = globals()[f'{name}_head']\n")
        writer.write("    except KeyError:\n")
        writer.write("        if name in _arch_optional:\n")
        writer.write("            return None\n")
        writer.write("        raise AttributeError(f\"module '{__name__}' has no attribute '{name}'\") from None\n")
        writer.write("    setattr(_module, name, press(prototype))\n")
        writer.write("    return getattr(_module, name)\n")
        writer.write("def __dir__():\n")
        writer.write("    return __all__\n")

    def write_make_head(self, writer: TextIO, td: TypeDefinition) -> None:
        match td.kind:
            case "object":  # CONSTANT, FUNCTION
                for fd in td.fields:
                    if "HasDefault" not in fd.attributes and not fd.signature.is_guid:
                        writer.write(f"make_head(_module, '{fd.name}')\n")
            case "function_pointer" | "union" | "struct" | "com":
                if td.has_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute"):
                    arch = ",".join(td.get_custom_attribute("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
                    writer.write(f"if ARCH in '{arch}':\n")
                    writer.write(f"    make_head(_module, '{td.name}')\n")
                else:
                    writer.write(f"make_head(_module, '{td.name}')\n")

    def write_footer(self, writer: TextIO, export_names: set[str], export_names_optional: list[str]) -> None:
        writer.write("__all__ = [\n")
        for name in sorted(export_names):
            writer.write(f'    "{name}",\n')
        writer.write("]\n")
        writer.write("_arch_optional = [\n")
        for name in sorted(export_names_optional):
            writer.write(f'    "{name}",\n')
        writer.write("]\n")

    def write_all(self, writer: TextIO, export_names_groupby_namespace: dict[str, set[str]]) -> None:
        writer.write("import importlib\n")
        writer.write("import sys\n")
        writer.write("_module = sys.modules[__name__]\n")
        writer.write("def __getattr__(name):\n")
        writer.write("    if name not in nameindex:\n")
        writer.write("        raise AttributeError(f\"module '{__name__}' has no attribute '{name}'\") from None\n")
        writer.write("    module = importlib.import_module(nameindex[name])\n")
        writer.write("    attr = getattr(module, name)\n")
        writer.write("    setattr(_module, name, attr)\n")
        writer.write("    return attr\n")
        writer.write("def __dir__():\n")
        writer.write("    return __all__\n")
        writer.write("nameindex = {\n")
        for name in BASE_EXPORTS:
            writer.write(f"'{name}': '{PACKAGE_NAME}.base',\n")
        for namespace in sorted(export_names_groupby_namespace):
            for name in sorted(export_names_groupby_namespace[namespace]):
                writer.write(f"'{name}': '{namespace}',\n")
        writer.write("}\n")
        writer.write("__all__ = sorted(nameindex)\n")


def main() -> None:
    with open(sys.argv[1]) as f:
        typedefs = [TypeDefinition(typedef) for typedef in json.load(f)]
    pp = Preprocessor()
    typedefs = pp.filter_public(typedefs)
    pp.patch_link_typedef(typedefs)
    pp.patch_enum(typedefs)
    pp.patch_com_vtbl_index(typedefs)
    pp.patch_name_conflict(typedefs)
    pp.patch_keyword_name(typedefs)
    pp.patch_namespace(typedefs, PACKAGE_NAME)
    ns_mod: dict[str, list[TypeDefinition]] = {}
    for td in typedefs:
        if td.namespace not in ns_mod:
            ns_mod[td.namespace] = []
        ns_mod[td.namespace].append(td)
    export_names_groupby_namespace = {}
    pg = PyGenerator()
    for namespace in ns_mod.keys():
        p = Path(namespace.replace(".", "/"))
        p.mkdir(parents=True, exist_ok=True)
        for d in p.parents[:-1]:
            if not (d / "__init__.py").exists():
                (d / "__init__.py").write_text("")
        import_namespaces: set[str] = {namespace}
        export_names: set[str] = set()
        export_names_arch: dict[str, set[str]] = {}
        for td in ns_mod[namespace]:
            pp.collect_import_namespace(td, import_namespaces)
            pp.collect_export_name(td, export_names)
            pp.collect_export_name_arch(td, export_names_arch)
        export_names_optional = [name for name, arch in export_names_arch.items() if arch and arch != {"X86", "X64", "ARM64"}]
        with (p / "__init__.py").open("w") as writer:
            pg.write_header(writer, import_namespaces)
            for td in ns_mod[namespace]:
                pg.emit(writer, td)
            for td in ns_mod[namespace]:
                pg.write_make_head(writer, td)
            pg.write_footer(writer, export_names, export_names_optional)
        export_names_groupby_namespace[namespace] = export_names
    with open(f"{PACKAGE_NAME}/all.py", "w") as writer:
        pg.write_all(writer, export_names_groupby_namespace)


if __name__ == "__main__":
    main()
