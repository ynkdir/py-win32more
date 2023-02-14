from __future__ import annotations
import argparse
import json
import keyword
import lzma
import re
import sys
from collections import defaultdict
from collections.abc import Collection, Iterable, Iterator
from pathlib import Path
from typing import TypeAlias, Any, TextIO, Self

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
    def namespace(self) -> str:
        if self["Namespace"] is None:
            raise KeyError()
        return self["Namespace"]

    @property
    def name(self) -> str:
        if self["Name"] is None:
            raise KeyError()
        return self["Name"]

    @property
    def fullname(self) -> str:
        return f"{self.namespace}.{self.name}"

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
                    return f"POINTER({self.type.fullname}_head)"
                else:
                    return f"POINTER({self.type.pytype})"
            case "SZArray":
                raise NotImplementedError()
            case "Array":
                return f"{self.type.pytype} * {self.size}"
            case "Type":
                if self.is_nested:
                    return self.name
                elif self.is_guid:
                    return "Guid"
                elif self.is_missing:
                    sys.stderr.write(f"DEBUG: missing type '{self.fullname}'\n")
                    return "MissingType"
                elif self.is_com:
                    return f"{self.fullname}_head"
                else:
                    return self.fullname
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

    @property
    def is_nested(self) -> bool:
        return self.kind == "Type" and self.namespace == ""

    @property
    def is_guid(self) -> bool:
        return self.kind == "Type" and self.fullname == "System.Guid"

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
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])

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
                if self.custom_attributes.has("Windows.Win32.Interop.NativeTypedefAttribute"):
                    return "native_typedef"
                # FIXME: CLSID_ComClass is defined as attribute like [uuid(...)] struct ComClass {}.
                elif self.custom_attributes.has("Windows.Win32.Interop.GuidAttribute") and not self.fields:
                    return "clsid"
                elif "ExplicitLayout" in self.attributes:
                    return "union"
                else:
                    return "struct"
            case _:
                raise NotImplementedError()

    def enumerate_types(self) -> Iterable[TType]:
        for fd in self.fields:
            yield fd.signature
        for md in self.method_definitions:
            yield md.signature.return_type
            yield from md.signature.parameter_types
        for nested_type in self.nested_types:
            yield from nested_type.enumerate_types()

    def enumerate_importing_namespaces(self) -> Iterable[str]:
        for ii in self.interface_implementations:
            yield ii.interface.type_reference.namespace
        for t in self.enumerate_types():
            t = t.get_element_type()
            if t.kind == "Type" and not t.is_nested and not t.is_guid and not t.is_missing:
                yield t.namespace

    def enumerate_exporting_names(self) -> Iterable[str]:
        match self.kind:
            case "object":
                for fd in self.fields:
                    yield fd.name
                for md in self.method_definitions:
                    yield md.name
            case "enum":
                yield self.name
                for fd in self.fields[1:]:
                    yield fd.name
            case "function_pointer" | "native_typedef" | "clsid" | "union" | "struct" | "com":
                yield self.name
            case _:
                raise NotImplementedError()

    def enumerate_names_having_architecture_attribute(self) -> Iterable[tuple[str, str]]:
        if self.custom_attributes.has("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            archs = self.custom_attributes.get("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value
            for arch in archs:
                yield self.name, arch.upper()
        if self.kind == "object":
            for md in self.method_definitions:
                if md.custom_attributes.has("Windows.Win32.Interop.SupportedArchitectureAttribute"):
                    archs = md.custom_attributes.get("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value
                    for arch in archs:
                        yield md.name, arch.upper()


class CustomAttributeCollection(Collection):
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __contains__(self, value: object) -> bool:
        for ca in self:
            if value == ca:
                return True
        return False

    def __iter__(self) -> Iterator[CustomAttribute]:
        return (CustomAttribute(ca) for ca in self.js)

    def __len__(self) -> int:
        return len(self.js)

    def has(self, type_: str) -> bool:
        for ca in self:
            if ca.type == type_:
                return True
        return False

    def get(self, type_: str) -> CustomAttribute:
        for ca in self:
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
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])

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
        elif self.signature.kind == "Type" and self.signature.fullname == "System.Guid":
            guid, rest = self.custom_attributes.get("Windows.Win32.Interop.GuidAttribute").guid_value()
            assert len(rest) == 0
            return f"Guid('{guid}')"
        elif self.signature.kind == "Type" and self.signature.fullname == f"Windows.Win32.Devices.Properties.DEVPROPKEY":
            guid, rest = self.custom_attributes.get("Windows.Win32.Interop.PropertyKeyAttribute").guid_value()
            assert len(rest) == 1
            return f"{self.signature.fullname}(fmtid=Guid('{guid}'), pid={rest[0]})"
        elif self.signature.kind == "Type" and self.signature.fullname == f"Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY":
            guid, rest = self.custom_attributes.get("Windows.Win32.Interop.PropertyKeyAttribute").guid_value()
            assert len(rest) == 1
            return f"{self.signature.fullname}(fmtid=Guid('{guid}'), pid={rest[0]})"
        else:
            # FIXME:
            raise NotImplementedError()


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
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])


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
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])


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
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])

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
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])

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
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])


class Preprocessor:
    def filter_public(self, typedefs: list[TypeDefinition]) -> list[TypeDefinition]:
        return [td for td in typedefs if td.namespace != "" and "Public" in td.attributes]

    def sort(self, typedefs: list[TypeDefinition]) -> list[TypeDefinition]:
        return sorted(typedefs, key=lambda td: (td.namespace, td.name))

    def patch_link_typedef(self, typedefs: list[TypeDefinition]) -> None:
        # FIXME: ns's key can be duplicated with arch variation.  Don't care for now.
        ns = {td.fullname: td for td in typedefs}
        for td in typedefs:
            for ii in td.interface_implementations:
                ii.interface.type_reference["_typedef"] = ns[ii.interface.type_reference.fullname]
            for t in td.enumerate_types():
                t = t.get_element_type()
                if t.kind == "Type":
                    t["_typedef"] = ns.get(t.fullname)
            self.patch_link_nestedtype(td)

    def patch_link_nestedtype(self, td: TypeDefinition) -> None:
        ns = {nested_type.name: nested_type for nested_type in td.nested_types}
        for fd in td.fields:
            t = fd.signature.get_element_type()
            if t.is_nested:
                t["_typedef"] = ns[t.name]
        for nested_type in td.nested_types:
            self.patch_link_nestedtype(nested_type)

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

    def patch_namespace_one(self, typedefs: list[TypeDefinition], namespace: str) -> None:
        for td in typedefs:
            td["Namespace"] = namespace
            for ii in td.interface_implementations:
                ii.interface.type_reference["Namespace"] = namespace
            for t in td.enumerate_types():
                t = t.get_element_type()
                if t.kind == "Type" and t.namespace != "System" and t.namespace != "":
                    t["Namespace"] = namespace


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
        if md.custom_attributes.has("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            arch = ",".join(md.custom_attributes.get("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
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
        if td.custom_attributes.has("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            arch = ",".join(td.custom_attributes.get("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
            writer.write(f"if ARCH in '{arch}':\n")
            indent = "    "
        else:
            indent = ""
        callconv = td.custom_attributes.get("System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute").fixed_arguments[0].value
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
        guid, rest = td.custom_attributes.get("Windows.Win32.Interop.GuidAttribute").guid_value()
        writer.write(f"{td.name} = Guid('{guid}')\n")

    # _fields_ and _anonymous_ is defined at runtime.
    def emit_struct_union(self, writer: TextIO, td: TypeDefinition, indent="") -> None:
        if td.custom_attributes.has("Windows.Win32.Interop.SupportedArchitectureAttribute"):
            arch = ",".join(td.custom_attributes.get("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
            writer.write(f"if ARCH in '{arch}':\n")
            indent = indent + "    "
        if td.kind == "struct":
            base = "Structure"
        elif td.kind == "union":
            base = "Union"
        else:
            raise NotImplementedError()
        if td.custom_attributes.has("Windows.Win32.Interop.GuidAttribute"):
            guid, rest = td.custom_attributes.get("Windows.Win32.Interop.GuidAttribute").guid_value()
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
        if td.custom_attributes.has("Windows.Win32.Interop.GuidAttribute"):
            guid, rest = td.custom_attributes.get("Windows.Win32.Interop.GuidAttribute").guid_value()
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
        if td.custom_attributes.has("Windows.Win32.Interop.GuidAttribute"):
            guid, rest = td.custom_attributes.get("Windows.Win32.Interop.GuidAttribute").guid_value()
            writer.write(f"    Guid = Guid('{guid}')\n")
        for md in td.method_definitions:
            restype = md.signature.return_type.pytype
            params_csv = ", ".join(f"{name}: {type_.pytype}" for name, type_ in md.get_parameter_names_with_type())
            vtbl_index = md["_vtbl_index"]
            writer.write(f"    @commethod({vtbl_index})\n")
            writer.write(f"    def {md.name}({params_csv}) -> {restype}: ...\n")

    def write_header(self, writer: TextIO, import_namespaces: set[str]) -> None:
        self.write_import_annotations(writer)
        self.write_import_ctypes(writer)
        self.write_import_base(writer)
        self.write_import_namespaces(writer, import_namespaces)
        self.write_getattr(writer)
        self.write_dir(writer)

    def write_header_one(self, writer: TextIO) -> None:
        self.write_import_annotations(writer)
        self.write_import_ctypes(writer)
        self.write_include_base(writer)
        self.write_getattr(writer)
        self.write_dir(writer)

    def write_import_annotations(self, writer: TextIO) -> None:
        writer.write("from __future__ import annotations\n")

    def write_import_ctypes(self, writer: TextIO) -> None:
        writer.write("from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll\n")

    def write_import_base(self, writer: TextIO) -> None:
        writer.write(f"from Windows.base import {BASE_EXPORTS_CSV}\n")

    def write_include_base(self, writer: TextIO) -> None:
        writer.write((Path(__file__).parent / "Windows\\base.py").read_text())

    def write_import_namespaces(self, writer: TextIO, import_namespaces: set[str]) -> None:
        for namespace in sorted(import_namespaces):
            writer.write(f"import {namespace}\n")

    def write_getattr(self, writer: TextIO) -> None:
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

    def write_dir(self, writer: TextIO) -> None:
        writer.write("def __dir__():\n")
        writer.write("    return __all__\n")

    def write_make_head(self, writer: TextIO, td: TypeDefinition) -> None:
        match td.kind:
            case "object":  # CONSTANT, FUNCTION
                for fd in td.fields:
                    if "HasDefault" not in fd.attributes and not fd.signature.is_guid:
                        writer.write(f"make_head(_module, '{fd.name}')\n")
            case "function_pointer" | "union" | "struct" | "com":
                if td.custom_attributes.has("Windows.Win32.Interop.SupportedArchitectureAttribute"):
                    arch = ",".join(td.custom_attributes.get("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value).upper()
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
            writer.write(f"'{name}': 'Windows.base',\n")
        for namespace in sorted(export_names_groupby_namespace):
            for name in sorted(export_names_groupby_namespace[namespace]):
                writer.write(f"'{name}': '{namespace}',\n")
        writer.write("}\n")
        writer.write("__all__ = sorted(nameindex)\n")


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

    def select(self, typedefs: Iterable[TypeDefinition]) -> Iterable[TypeDefinition]:
        ns: dict[str, list[TypeDefinition]] = {}
        for td in typedefs:
            if td.fullname not in ns:
                ns[td.fullname] = []
            ns[td.fullname].append(td)
        selected = set()
        for td in self.find_match(typedefs):
            if id(td) in selected:
                continue
            selected.add(id(td))
            yield td
            yield from self.select_dependencies(td, ns, selected)

    def select_dependencies(self, td: TypeDefinition, ns: dict[str, list[TypeDefinition]], selected: set[int]) -> Iterable[TypeDefinition]:
        for name in self.find_dependencies(td):
            if name not in ns:
                continue
            for td_depended in ns[name]:
                if id(td_depended) in selected:
                    continue
                selected.add(id(td_depended))
                yield td_depended
                yield from self.select_dependencies(td_depended, ns, selected)

    def find_match(self, typedefs: Iterable[TypeDefinition]) -> Iterable[TypeDefinition]:
        for td in typedefs:
            if self.is_match(td.namespace):
                yield td
            elif self.is_match(td.name):
                yield td
            elif self.is_match(td.fullname):
                yield td
            elif td.kind == "object":  # Apis
                fields = []
                for fd in td.fields:  # constants
                    if self.is_match(fd.name):
                        fields.append(fd.js)
                    elif self.is_match(f"{td.namespace}.{fd.name}"):
                        fields.append(fd.js)
                method_definitions = []
                for md in td.method_definitions:  # functions
                    if self.is_match(md.name):
                        method_definitions.append(md.js)
                    elif self.is_match(f"{td.namespace}.{md.name}"):
                        method_definitions.append(md.js)
                if fields or method_definitions:
                    td["Fields"] = fields
                    td["MethodDefinitions"] = method_definitions
                    yield td
            elif td.kind == "enum":
                for fd in td.fields:
                    if self.is_match(fd.name):
                        yield td
                        break
                    elif self.is_match(f"{td.namespace}.{fd.name}"):
                        yield td
                        break

    def find_dependencies(self, td: TypeDefinition) -> Iterable[str]:
        for ii in td.interface_implementations:
            yield ii.interface.type_reference.fullname
        for t in td.enumerate_types():
            t = t.get_element_type()
            if t.kind == "Type":
                yield t.fullname


def generate(typedefs: list[TypeDefinition]) -> None:
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
        export_names_arch = defaultdict(set)
        for td in ns_mod[namespace]:
            import_namespaces |= set(td.enumerate_importing_namespaces())
            export_names |= set(td.enumerate_exporting_names())
            for name, arch in td.enumerate_names_having_architecture_attribute():
                export_names_arch[name].add(arch)
        export_names_optional = [name for name, archs in export_names_arch.items() if archs and archs != {"X86", "X64", "ARM64"}]
        with (p / "__init__.py").open("w") as writer:
            pg.write_header(writer, import_namespaces)
            for td in ns_mod[namespace]:
                pg.emit(writer, td)
            for td in ns_mod[namespace]:
                pg.write_make_head(writer, td)
            pg.write_footer(writer, export_names, export_names_optional)
        export_names_groupby_namespace[namespace] = export_names
    with open(f"Windows/all.py", "w") as writer:
        pg.write_all(writer, export_names_groupby_namespace)


def generate_one(typedefs: list[TypeDefinition], writer: TextIO) -> None:
    pg = PyGenerator()
    export_names: set[str] = set()
    export_names_arch = defaultdict(set)
    for td in typedefs:
        export_names |= set(td.enumerate_exporting_names())
        for name, arch in td.enumerate_names_having_architecture_attribute():
            export_names_arch[name].add(arch)
    export_names_optional = [name for name, archs in export_names_arch.items() if archs and archs != {"X86", "X64", "ARM64"}]
    pg.write_header_one(writer)
    for td in typedefs:
        pg.emit(writer, td)
    for td in typedefs:
        pg.write_make_head(writer, td)
    pg.write_footer(writer, export_names, export_names_optional)


def xopen(path: str) -> TextIO:
    if path.endswith(".xz"):
        return lzma.open(path)
    return open(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Metadata to Python generator")
    parser.add_argument("-o", "--one", help="out to one file")
    parser.add_argument("-s", "--selector", help="selector.txt")
    parser.add_argument("metadata", help="metadata.json")
    args = parser.parse_args()

    with xopen(args.metadata) as f:
        typedefs = [TypeDefinition(typedef) for typedef in json.load(f)]

    pp = Preprocessor()
    typedefs = pp.filter_public(typedefs)
    typedefs = pp.sort(typedefs)

    if args.selector is not None:
        selector = Selector()
        selector.read_selector(Path(args.selector))
        typedefs = list(selector.select(typedefs))

    pp.patch_link_typedef(typedefs)
    pp.patch_enum(typedefs)
    pp.patch_com_vtbl_index(typedefs)
    pp.patch_name_conflict(typedefs)
    pp.patch_keyword_name(typedefs)

    if args.one is not None:
        pp.patch_namespace_one(typedefs, "_module")
        with open(args.one, "w") as writer:
            generate_one(typedefs, writer)
    else:
        generate(typedefs)


if __name__ == "__main__":
    main()
