from __future__ import annotations

import argparse
import json
import keyword
import lzma
import re
import sys
from collections import defaultdict
from collections.abc import Iterable, Iterator, Mapping
from io import StringIO
from pathlib import Path
from typing import Any, Collection, MutableSequence, TextIO, overload

if sys.version_info < (3, 11):
    from typing_extensions import TypeAlias
else:
    from typing import TypeAlias

BASE_EXPORTS = [
    "ARCH",
    "MissingType",
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
    "EasyCastStructure",
    "EasyCastUnion",
    "ComPtr",
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
    def type_arguments(self) -> list[TType]:
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
        if self.kind == "Primitive":
            return self.name
        elif self.kind == "Pointer":
            if self.type.kind == "Primitive" and self.type.name == "Void":
                return "c_void_p"
            elif self.type.is_struct:
                return f"POINTER({self.type.fullname}_head)"
            else:
                return f"POINTER({self.type.pytype})"
        elif self.kind == "SZArray":
            raise NotImplementedError()
        elif self.kind == "Array":
            return f"{self.type.pytype} * {self.size}"
        elif self.kind == "Type":
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
        else:
            raise NotImplementedError()

    def get_element_type(self) -> TType:
        if self.kind in ["Pointer", "SZArray", "Array"]:
            return self.type.get_element_type()
        elif self.kind in ["Primitive", "Type"]:
            return self
        else:
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
        if self.basetype is None:
            return "com"
        elif self.basetype == "System.Object":
            return "object"  # CONSTANT, FUNCTION
        elif self.basetype == "System.MulticastDelegate":
            return "function_pointer"
        elif self.basetype == "System.Enum":
            return "enum"
        elif self.basetype == "System.ValueType":
            if self.custom_attributes.has_native_typedef():
                return "native_typedef"
            # FIXME: CLSID_ComClass is defined as attribute like [uuid(...)] struct ComClass {}.
            elif self.custom_attributes.has_guid() and not self.fields:
                return "clsid"
            elif "ExplicitLayout" in self.attributes:
                return "union"
            else:
                return "struct"
        elif self.basetype == "System.Attribute":
            return "attribute"
        else:
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

    def enumerate_names_having_architecture_attribute(self) -> Iterable[tuple[str, str]]:
        if self.custom_attributes.has_supported_architecture():
            for arch in self.custom_attributes.get_supported_architecture():
                yield self.name, arch.upper()
        if self.kind == "object":
            for md in self.method_definitions:
                if md.custom_attributes.has_supported_architecture():
                    for arch in md.custom_attributes.get_supported_architecture():
                        yield md.name, arch.upper()


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


class CustomAttributeCollection(Collection[CustomAttribute]):
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

    def has_native_typedef(self) -> bool:
        return self.has("Windows.Win32.Foundation.Metadata.NativeTypedefAttribute")

    def has_supported_architecture(self) -> bool:
        return self.has("Windows.Win32.Foundation.Metadata.SupportedArchitectureAttribute")

    def get_supported_architecture(self) -> list[str]:
        return self.get("Windows.Win32.Foundation.Metadata.SupportedArchitectureAttribute").fixed_arguments[0].value

    def has_guid(self) -> bool:
        return self.has("Windows.Win32.Foundation.Metadata.GuidAttribute")

    def get_guid(self) -> str:
        v = [fa.value for fa in self.get("Windows.Win32.Foundation.Metadata.GuidAttribute").fixed_arguments]
        assert len(v) == 11
        return self.format_guid(v)

    def format_guid(self, v: list[int]) -> str:
        return f"{{{v[0]:08x}-{v[1]:04x}-{v[2]:04x}-{v[3]:02x}{v[4]:02x}-{v[5]:02x}{v[6]:02x}{v[7]:02x}{v[8]:02x}{v[9]:02x}{v[10]:02x}}}"

    def get_property_key(self) -> tuple[str, int]:
        value = self.get("Windows.Win32.Foundation.Metadata.ConstantAttribute").fixed_arguments[0].value
        m = re.fullmatch(r"{(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)}, (\d+)", value)
        if not m:
            raise ValueError()
        v = [int(d) for d in m.groups()]
        assert len(v) == 12
        guid = self.format_guid(v[:11])
        pid = v[11]
        return guid, pid

    def has_constant(self) -> bool:
        return self.has("Windows.Win32.Foundation.Metadata.ConstantAttribute")

    def get_constant(self) -> str:
        # value is like "{0, 0, 0, 0, 0, 5}"
        value = self.get("Windows.Win32.Foundation.Metadata.ConstantAttribute").fixed_arguments[0].value
        value_csv = value.translate({ord("{"): "(", ord("}"): ")"})
        return value_csv

    def get_unmanaged_function_pointer(self) -> str:
        return self.get("System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute").fixed_arguments[0].value


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
            guid = self.custom_attributes.get_guid()
            return f"Guid('{guid}')"
        elif self.signature.kind == "Type" and self.signature.fullname == "Windows.Win32.Devices.Properties.DEVPROPKEY":
            guid, pid = self.custom_attributes.get_property_key()
            return f"{self.signature.fullname}(fmtid=Guid('{guid}'), pid={pid})"
        elif self.signature.kind == "Type" and self.signature.fullname == "Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY":
            guid, pid = self.custom_attributes.get_property_key()
            return f"{self.signature.fullname}(fmtid=Guid('{guid}'), pid={pid})"
        elif self.signature.kind == "Type" and self.signature.fullname == "Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY":
            value = self.custom_attributes.get_constant()
            return f"{self.signature.fullname}({value})"
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
    def interface(self) -> EntityHandle:
        return EntityHandle(self["Interface"])

    @property
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])


class EntityHandle:
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

    def format_parameters(self) -> str:
        return ", ".join(self.format_parameters_list())

    def format_parameters_list(self) -> list[str]:
        return [f"{name}: {type_.pytype}" for name, type_ in self.get_parameter_names_with_type()]

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


class Metadata(MutableSequence[TypeDefinition]):
    def __init__(self, typedefs: Iterable[TypeDefinition] = []) -> None:
        self.typedefs = list(typedefs)

    def __len__(self) -> int:
        return len(self.typedefs)

    @overload
    def __getitem__(self, key: int) -> TypeDefinition:
        ...

    @overload
    def __getitem__(self, key: slice) -> MutableSequence[TypeDefinition]:
        ...

    def __getitem__(self, key):
        return self.typedefs[key]

    @overload
    def __setitem__(self, key: int, value: TypeDefinition) -> None:
        ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[TypeDefinition]) -> None:
        ...

    def __setitem__(self, key, value) -> None:
        self.typedefs[key] = value

    @overload
    def __delitem__(self, key: int) -> None:
        ...

    @overload
    def __delitem__(self, key: slice) -> None:
        ...

    def __delitem__(self, key) -> None:
        del self.typedefs[key]

    def insert(self, i: int, value: TypeDefinition) -> None:
        self.typedefs.insert(i, value)

    def group_by_namespace(self) -> Mapping[str, Metadata]:
        meta_group_by_namespace: Mapping[str, Metadata] = defaultdict(Metadata)
        for td in self:
            meta_group_by_namespace[td.namespace].append(td)
        return meta_group_by_namespace

    def group_by_fullname(self) -> Mapping[str, Metadata]:
        meta_group_by_fullname: Mapping[str, Metadata] = defaultdict(Metadata)
        for td in self:
            meta_group_by_fullname[td.fullname].append(td)
        return meta_group_by_fullname

    def enumerate_importing_namespaces(self) -> Iterable[str]:
        for td in self:
            yield from td.enumerate_importing_namespaces()

    def enumerate_names_having_architecture_attribute(self) -> Iterable[tuple[str, str]]:
        for td in self:
            yield from td.enumerate_names_having_architecture_attribute()


class Preprocessor:
    def filter_public(self, meta: Metadata) -> Metadata:
        return Metadata(td for td in meta if td.namespace != "" and "Public" in td.attributes)

    def sort(self, meta: Metadata) -> Metadata:
        return Metadata(sorted(meta, key=lambda td: (td.namespace, td.name)))

    def patch_link_typedef(self, meta: Metadata) -> None:
        # FIXME: ns's key can be duplicated with arch variation.  Don't care for now.
        ns = {td.fullname: td for td in meta}
        for td in meta:
            for ii in td.interface_implementations:
                ii.interface.type_reference["_typedef"] = ns[ii.interface.type_reference.fullname]
            for t in td.enumerate_types():
                t = t.get_element_type()
                if t.kind == "Type":
                    t["_typedef"] = ns.get(t.fullname)
            self.patch_link_nestedtype(td)

    def patch_link_nestedtype(self, td: TypeDefinition) -> None:
        nested_type_by_name = {nested_type.name: nested_type for nested_type in td.nested_types}
        for fd in td.fields:
            t = fd.signature.get_element_type()
            if t.is_nested:
                t["_typedef"] = nested_type_by_name[t.name]
        for nested_type in td.nested_types:
            self.patch_link_nestedtype(nested_type)

    # FIXME: enum value name? (NAME or ENUM_NAME or ENUM.Name?)
    def patch_enum(self, meta: Metadata) -> None:
        for td in meta:
            if td.kind == "enum" and self.enum_need_prefix(td):
                for fd in td.fields:
                    fd["Name"] = f"{td['Name']}_{fd['Name']}"

    def enum_need_prefix(self, td: TypeDefinition) -> bool:
        for fd in td.fields:
            if not ("_" in fd.name or fd.name.isupper()):
                return True
        return False

    # Add vtbl_index to COM methods.
    def patch_com_vtbl_index(self, meta: Metadata) -> None:
        for td in meta:
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

    def patch_name_conflict(self, meta: Metadata) -> None:
        meta_group_by_fullname = meta.group_by_fullname()
        for td in meta:
            if td.name == "Apis":
                for fd in td.fields:
                    if f"{td.namespace}.{fd.name}" in meta_group_by_fullname:
                        sys.stderr.write(f"DEBUG: name conflict '{td.namespace}.{fd.name}'\n")
                        fd["Name"] = f"{fd['Name']}_CONSTANT"

    def patch_keyword_name(self, meta: Metadata) -> None:
        for td in meta:
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

    def patch_namespace_one(self, meta: Metadata, namespace: str) -> None:
        for td in meta:
            td["Namespace"] = namespace
            for ii in td.interface_implementations:
                ii.interface.type_reference["Namespace"] = namespace
            for t in td.enumerate_types():
                t = t.get_element_type()
                if t.kind == "Type" and t.namespace != "System" and t.namespace != "":
                    t["Namespace"] = namespace


class PyGenerator:
    def emit(self, td: TypeDefinition) -> str:
        if td.kind == "object":  # CONSTANT, FUNCTION
            return self.emit_object(td)
        elif td.kind == "function_pointer":
            return self.emit_function_pointer(td)
        elif td.kind == "enum":
            return self.emit_enum(td)
        elif td.kind == "native_typedef":
            return self.emit_native_typedef(td)
        elif td.kind == "clsid":
            return self.emit_clsid(td)
        elif td.kind == "union":
            return self.emit_struct_union(td)
        elif td.kind == "struct":
            return self.emit_struct_union(td)
        elif td.kind == "com":
            return self.emit_com(td)
        elif td.kind == "attribute":
            return self.emit_attribute(td)
        else:
            raise NotImplementedError()

    def emit_object(self, td: TypeDefinition) -> str:
        writer = StringIO()
        for fd in td.fields:
            writer.write(self.emit_constant(fd))
        for md in td.method_definitions:
            writer.write(self.emit_function(md))
        return writer.getvalue()

    def emit_constant(self, fd: FieldDefinition) -> str:
        writer = StringIO()
        if "HasDefault" in fd.attributes:
            # primitive
            writer.write(f"{fd.name}: {fd.signature.pytype} = {fd.pyvalue}\n")
        elif fd.signature.is_guid:
            writer.write(f"{fd.name}: Guid = {fd.pyvalue}\n")
        else:
            writer.write(f"def {fd.name}():\n")
            writer.write(f"    return {fd.pyvalue}\n")
        return writer.getvalue()

    def emit_function(self, md: MethodDefinition) -> str:
        if md.custom_attributes.has_constant():
            return self.emit_inline_function(md)
        else:
            return self.emit_external_function(md)

    def emit_inline_function(self, md: MethodDefinition) -> str:
        writer = StringIO()
        indent = self.write_architecture_specific_block_if_necessary(writer, md.custom_attributes)
        restype = md.signature.return_type.pytype
        params_csv = md.format_parameters()
        value = md.custom_attributes.get_constant()
        writer.write(f"{indent}def {md.name}({params_csv}) -> {restype}:\n")
        writer.write(f"{indent}    return {restype}({value})\n")
        return writer.getvalue()

    def emit_external_function(self, md: MethodDefinition) -> str:
        writer = StringIO()
        indent = self.write_architecture_specific_block_if_necessary(writer, md.custom_attributes)
        library = md.import_.module.name
        functype = self.function_functype(md)
        restype = md.signature.return_type.pytype
        params = md.format_parameters_list()
        attrs = [f"'{library}'"]
        if md.name != md.import_.name:
            entry_point = self.function_entry_point(md)
            attrs.append(f"entry_point={entry_point}")
        if md.signature.header.calling_convention == "VarArgs":
            assert functype == "cfunctype"
            attrs.append("variadic=True")
            params.append("*__arglist")
        params_csv = ", ".join(params)
        attrs_csv = ", ".join(attrs)
        writer.write(f"{indent}@{functype}({attrs_csv})\n")
        writer.write(f"{indent}def {md.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def function_functype(self, md: MethodDefinition) -> str:
        if "CallingConventionWinApi" in md.import_.attributes:
            return "winfunctype"
        elif "CallingConventionCDecl" in md.import_.attributes:
            return "cfunctype"
        else:
            raise NotImplementedError()

    def function_entry_point(self, md: MethodDefinition) -> str:
        if md.import_.name.startswith("#"):
            # ordinal number  (e.g. #123)
            return md.import_.name[1:]
        else:
            return "'md.import_.name'"

    def emit_function_pointer(self, td: TypeDefinition) -> str:
        writer = StringIO()
        indent = self.write_architecture_specific_block_if_necessary(writer, td.custom_attributes)
        functype = self.function_pointer_functype(td)
        md = td.method_definitions[1]  # [0]=.ctor, [1]=Invoke
        restype = md.signature.return_type.pytype
        params_csv = md.format_parameters()
        writer.write(f"{indent}@{functype}\n")
        writer.write(f"{indent}def {td.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def function_pointer_functype(self, td: TypeDefinition) -> str:
        calling_convention = td.custom_attributes.get_unmanaged_function_pointer()
        if calling_convention == "Winapi":
            return "winfunctype_pointer"
        elif calling_convention == "Cdecl":
            return "cfunctype_pointer"
        else:
            raise NotImplementedError()

    def emit_enum(self, td: TypeDefinition) -> str:
        writer = StringIO()
        type_field, *value_fields = td.fields
        writer.write(f"{td.name} = {type_field.signature.pytype}\n")
        for fd in value_fields:
            writer.write(f"{fd.name}: {td.name} = {fd.default_value.value}\n")
        return writer.getvalue()

    def emit_native_typedef(self, td: TypeDefinition) -> str:
        pytype = td.fields[0].signature.pytype
        if pytype == "POINTER(Byte)":
            pytype = "c_char_p"
        elif pytype == "POINTER(Char)":
            pytype = "c_wchar_p"
        return f"{td.name} = {pytype}\n"

    def emit_clsid(self, td: TypeDefinition) -> str:
        guid = td.custom_attributes.get_guid()
        return f"{td.name} = Guid('{guid}')\n"

    # _fields_ and _anonymous_ is defined at runtime.
    def emit_struct_union(self, td: TypeDefinition, indent="") -> str:
        writer = StringIO()
        if not td.is_nested:
            indent = self.write_architecture_specific_block_if_necessary(writer, td.custom_attributes)
        base = self.struct_union_base_type(td)
        writer.write(f"{indent}class {td.name}({base}):\n")
        if self.struct_union_is_empty(td):
            writer.write(f"{indent}    pass\n")
            return writer.getvalue()
        if td.custom_attributes.has_guid():
            # FIXME: What id?
            guid = td.custom_attributes.get_guid()
            writer.write(f"{indent}    _uuid_ = Guid('{guid}')\n")
        for fd in self.struct_union_static_fields(td):
            writer.write(f"{indent}    {fd.name} = {fd.pyvalue}\n")
        for fd in self.struct_union_fields(td):
            writer.write(f"{indent}    {fd.name}: {fd.signature.pytype}\n")
        if td.layout.packing_size != 0:
            writer.write(f"{indent}    _pack_ = {td.layout.packing_size}\n")
        for nested_type in td.nested_types:
            writer.write(self.emit_struct_union(nested_type, indent + "    "))
        return writer.getvalue()

    def struct_union_base_type(self, td: TypeDefinition) -> str:
        if td.kind == "struct":
            return "EasyCastStructure"
        elif td.kind == "union":
            return "EasyCastUnion"
        else:
            raise NotImplementedError()

    def struct_union_static_fields(self, td: TypeDefinition) -> Iterable[FieldDefinition]:
        for fd in td.fields:
            if self.struct_union_field_is_static(fd):
                yield fd

    def struct_union_fields(self, td: TypeDefinition) -> Iterable[FieldDefinition]:
        for fd in td.fields:
            if not self.struct_union_field_is_static(fd):
                yield fd

    def struct_union_field_is_static(self, fd: FieldDefinition) -> bool:
        return {"Static", "HasDefault"} <= set(fd.attributes)

    def struct_union_is_empty(self, td: TypeDefinition) -> bool:
        if td.fields:
            return False
        assert not td.custom_attributes.has_guid()
        return True

    def emit_com(self, td: TypeDefinition) -> str:
        assert len(td.interface_implementations) <= 1
        writer = StringIO()
        base = self.com_base_type(td)
        writer.write(f"class {td.name}(ComPtr):\n")
        writer.write(f"    extends: {base}\n")
        if td.custom_attributes.has_guid():
            guid = td.custom_attributes.get_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        for md in td.method_definitions:
            restype = md.signature.return_type.pytype
            params = ["self"]
            params.extend(md.format_parameters_list())
            params_csv = ", ".join(params)
            vtbl_index = md["_vtbl_index"]
            writer.write(f"    @commethod({vtbl_index})\n")
            writer.write(f"    def {md.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def com_base_type(self, td: TypeDefinition) -> str:
        if not td.interface_implementations:
            return "None"
        return td.interface_implementations[0].interface.type_reference.fullname

    def emit_attribute(self, td: TypeDefinition) -> str:
        writer = StringIO()
        md = td.method_definitions[0]  # [0]=.ctor
        params = md.format_parameters_list()
        writer.write(f"class {td.name}(EasyCastStructure):\n")
        if not params:
            writer.write("    pass\n")
        else:
            for param in params:
                writer.write(f"    {param}\n")
        return writer.getvalue()

    def emit_header(self, import_namespaces: set[str]) -> str:
        writer = StringIO()
        writer.write(self.emit_import_annotations())
        writer.write(self.emit_import_ctypes())
        writer.write(self.emit_import_base())
        writer.write(self.emit_import_namespaces(import_namespaces))
        writer.write(self.emit_getattr())
        return writer.getvalue()

    def emit_header_one(self) -> str:
        writer = StringIO()
        writer.write(self.emit_import_annotations())
        writer.write(self.emit_import_ctypes())
        writer.write(self.emit_include_base())
        writer.write(self.emit_getattr())
        return writer.getvalue()

    def emit_import_annotations(self) -> str:
        return "from __future__ import annotations\n"

    def emit_import_ctypes(self) -> str:
        return "from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll\n"

    def emit_import_base(self) -> str:
        return f"from Windows import {BASE_EXPORTS_CSV}\n"

    def emit_include_base(self) -> str:
        return (Path(__file__).parent / "Windows\\__init__.py").read_text()

    def emit_import_namespaces(self, import_namespaces: set[str]) -> str:
        writer = StringIO()
        for namespace in sorted(import_namespaces):
            writer.write(f"import {namespace}\n")
        return writer.getvalue()

    def emit_getattr(self) -> str:
        writer = StringIO()
        writer.write("import sys\n")
        writer.write("_module = sys.modules[__name__]\n")
        writer.write("def __getattr__(name):\n")
        writer.write("    try:\n")
        writer.write("        prototype = globals()[f'{name}_head']\n")
        writer.write("    except KeyError:\n")
        writer.write("        raise AttributeError(f\"module '{__name__}' has no attribute '{name}'\") from None\n")
        writer.write("    setattr(_module, name, press(prototype))\n")
        writer.write("    return getattr(_module, name)\n")
        return writer.getvalue()

    def emit_make_head(self, td: TypeDefinition) -> str:
        writer = StringIO()
        if td.kind == "object":  # CONSTANT, FUNCTION
            for fd in td.fields:
                if "HasDefault" not in fd.attributes and not fd.signature.is_guid:
                    writer.write(f"make_head(_module, '{fd.name}')\n")
        elif td.kind in ["function_pointer", "union", "struct", "com"]:
            indent = self.write_architecture_specific_block_if_necessary(writer, td.custom_attributes)
            writer.write(f"{indent}make_head(_module, '{td.name}')\n")
        return writer.getvalue()

    def write_architecture_specific_block_if_necessary(self, writer: TextIO, custom_attributes: CustomAttributeCollection) -> str:
        if custom_attributes.has_supported_architecture():
            arch = ",".join(custom_attributes.get_supported_architecture()).upper()
            writer.write(f"if ARCH in '{arch}':\n")
            indent = "    "
        else:
            indent = ""
        return indent


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
        meta_group_by_fullname = meta.group_by_fullname()
        selected = set()
        for td in self.find_match(meta):
            if id(td) in selected:
                continue
            selected.add(id(td))
            if td.kind == "object":
                self.select_object_members_inplace(td)
            yield td
            yield from self.select_dependencies(td, meta_group_by_fullname, selected)

    def select_dependencies(self, td: TypeDefinition, meta_group_by_fullname: Mapping[str, Metadata], selected: set[int]) -> Iterable[TypeDefinition]:
        for fullname_depended in self.find_dependencies(td):
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
            elif td.kind == "object":  # Apis
                if self.is_match_any_fields(td):  # constants
                    yield td
                elif self.is_match_any_method_definitions(td):  # functions
                    yield td
            elif td.kind == "enum":
                if self.is_match_any_fields(td):
                    yield td

    def find_dependencies(self, td: TypeDefinition) -> Iterable[str]:
        for ii in td.interface_implementations:
            yield ii.interface.type_reference.fullname
        for t in td.enumerate_types():
            t = t.get_element_type()
            if t.kind == "Type":
                yield t.fullname


def make_module_path_for_write(namespace) -> TextIO:
    p = Path(namespace.replace(".", "/"))
    p.mkdir(parents=True, exist_ok=True)
    for i in range(len(p.parents) - 1):
        d = p.parents[i]
        if not (d / "__init__.py").exists():
            (d / "__init__.py").write_text("")
    return (p / "__init__.py").open("w")


def generate(meta: Metadata) -> None:
    pg = PyGenerator()
    for namespace, meta_group_by_namespace in meta.group_by_namespace().items():
        import_namespaces = set(meta_group_by_namespace.enumerate_importing_namespaces()) | {namespace}
        with make_module_path_for_write(namespace) as writer:
            writer.write(pg.emit_header(import_namespaces))
            for td in meta_group_by_namespace:
                writer.write(pg.emit(td))
            for td in meta_group_by_namespace:
                writer.write(pg.emit_make_head(td))


def generate_one(meta: Metadata, writer: TextIO) -> None:
    pg = PyGenerator()
    writer.write(pg.emit_header_one())
    for td in meta:
        writer.write(pg.emit(td))
    for td in meta:
        writer.write(pg.emit_make_head(td))


def xopen(path: str) -> TextIO | lzma.LZMAFile:
    if path.endswith(".xz"):
        return lzma.open(path)
    return open(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Metadata to Python generator")
    parser.add_argument("-o", "--one", help="out to one file")
    parser.add_argument("-s", "--selector", help="selector.txt")
    parser.add_argument("metadata", help="metadata.json")
    args = parser.parse_args()
    build(args.metadata, args.selector, args.one)


def build(metadata, selector=None, one=None) -> None:
    with xopen(metadata) as f:
        meta = Metadata(TypeDefinition(typedef) for typedef in json.load(f))

    pp = Preprocessor()
    meta = pp.filter_public(meta)
    meta = pp.sort(meta)

    if selector is not None:
        s = Selector()
        s.read_selector(Path(selector))
        meta = Metadata(s.select(meta))

    pp.patch_link_typedef(meta)
    pp.patch_enum(meta)
    pp.patch_com_vtbl_index(meta)
    pp.patch_name_conflict(meta)
    pp.patch_keyword_name(meta)

    if one is not None:
        pp.patch_namespace_one(meta, "_module")
        with open(one, "w") as writer:
            generate_one(meta, writer)
    else:
        generate(meta)


if __name__ == "__main__":
    main()
