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
from typing import TYPE_CHECKING, Any, Collection, MutableSequence, TextIO, overload

if sys.version_info < (3, 11):
    from typing_extensions import Self, TypeAlias
else:
    from typing import Self, TypeAlias

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
    "EasyCastStructure",
    "EasyCastUnion",
    "ComPtr",
]
BASE_EXPORTS_CSV = ", ".join(BASE_EXPORTS)

WINRT_EXPORTS = [
    "WinRT_String",
    "winrt_commethod",
    "winrt_mixinmethod",
    "winrt_classmethod",
    "winrt_factorymethod",
    "winrt_activatemethod",
]
WINRT_EXPORTS_CSV = ", ".join(WINRT_EXPORTS)


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
    def modifier_type(self) -> TType:
        if self["ModifierType"] is None:
            raise KeyError()
        return TType(self["ModifierType"])

    @property
    def unmodified_type(self) -> TType:
        if self["UnmodifiedType"] is None:
            raise KeyError()
        return TType(self["UnmodifiedType"])

    @property
    def is_required(self) -> bool:
        if self["IsRequired"] is None:
            raise KeyError()
        return self["IsRequired"]

    @property
    def pytype(self) -> str:
        if self.kind == "Primitive":
            if self.name == "Object":
                return "Windows.Win32.System.WinRT.IInspectable_head"
            elif self.name == "String":
                return "WinRT_String"
            else:
                return self.name
        elif self.kind == "Pointer" or self.kind == "Reference" or self.kind == "SZArray":
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
        elif self.kind == "Array":
            return f"{self.type.pytype} * {self.size}"
        elif self.kind == "Type":
            if self.is_nested:
                return self.name
            elif self.is_guid:
                return "Guid"
            elif self.is_missing:
                sys.stderr.write(f"DEBUG: missing type '{self.fullname}'\n")
                return self.fullname
            elif self.is_com:
                return f"{self.fullname}"
            else:
                return self.fullname
        elif self.kind == "Generic":
            return self.generic_fullname
        elif self.kind == "GenericParameter":
            return self.name
        elif self.kind == "Modified" and self.modifier_type.fullname == "System.Runtime.CompilerServices.IsConst":
            return self.unmodified_type.pytype
        else:
            raise NotImplementedError()

    @property
    def generic_fullname(self) -> str:
        fullname = self.generic_strip_suffix(self.type.fullname)
        parameters = self.format_generic_parameters()
        return f"{fullname}[{parameters}]"

    def format_generic_parameters(self) -> str:
        return ", ".join(ta.pytype for ta in self.type_arguments)

    def generic_strip_suffix(self, name) -> str:
        return name.split("`")[0]

    def get_element_type(self) -> TType:
        if self.kind in ["Pointer", "SZArray", "Array", "Reference"]:
            return self.type.get_element_type()
        elif self.kind in ["Primitive", "Type", "Generic", "GenericParameter"]:
            return self
        elif self.kind == "Modified" and self.modifier_type.fullname == "System.Runtime.CompilerServices.IsConst":
            return self.unmodified_type
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

    def enumerate_types(self) -> Iterable[TType]:
        yield self
        if self.kind == "Generic":
            yield from self.type.enumerate_types()
            for t in self.type_arguments:
                yield from t.enumerate_types()
        elif self.kind == "Pointer":
            yield from self.type.enumerate_types()
        elif self.kind == "SZArray":
            yield from self.type.enumerate_types()
        elif self.kind == "Reference":
            yield from self.type.enumerate_types()
        elif self.kind == "Modified":
            yield from self.unmodified_type.enumerate_types()


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
    def generic_parameters(self) -> list[GenericParameter]:
        return [GenericParameter(gp) for gp in self["GenericParameters"]]

    @property
    def is_generic(self) -> bool:
        return "`" in self.name

    def format_generic_parameters(self) -> str:
        return ", ".join(gp.name for gp in self.generic_parameters)

    def generic_strip_suffix(self, name) -> str:
        return name.split("`")[0]

    @property
    def generic_fullname(self) -> str:
        fullname = self.generic_strip_suffix(self.fullname)
        parameters = self.format_generic_parameters()
        return f"{fullname}[{parameters}]"

    @property
    def name_no_generic(self) -> str:
        return self.name.split("`")[0]

    @property
    def kind(self) -> str:
        if self.basetype is None or self.basetype == "System.Object" or self.basetype.startswith("Windows."):
            return "com"
        elif self.basetype == "System.MulticastDelegate":
            return "com"
        elif self.basetype == "System.Enum":
            return "enum"
        elif self.basetype == "System.ValueType":
            if self.fields:
                return "struct"
            else:
                assert self.custom_attributes.has("Windows.Foundation.Metadata.ContractVersionAttribute")
                return "contract_version"
        else:
            raise NotImplementedError()

    def enumerate_types(self) -> Iterable[TType]:
        for fd in self.fields:
            yield from fd.signature.enumerate_types()
        for md in self.method_definitions:
            yield from md.signature.return_type.enumerate_types()
            for t in md.signature.parameter_types:
                yield from t.enumerate_types()
        for nested_type in self.nested_types:
            yield from nested_type.enumerate_types()

    def enumerate_importing_namespaces(self) -> Iterable[str]:
        for ii in self.interface_implementations:
            yield ii.namespace
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


class GenericParameter:
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
    def index(self) -> int:
        return self["Index"]

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def constraints(self) -> list[GenericParameterConstraint]:
        return [GenericParameterConstraint(gc) for gc in self["Constraints"]]

    @property
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])


class GenericParameterConstraint:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def type(self) -> EntityHandle:
        return EntityHandle(self["Type"])

    @property
    def custom_attributes(self) -> CustomAttributeCollection:
        return CustomAttributeCollection(self["CustomAttributes"])


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

    def get_list(self, type_: str) -> list[CustomAttribute]:
        return [ca for ca in self if ca.type == type_]

    def has_native_typedef(self) -> bool:
        return self.has("Windows.Win32.Interop.NativeTypedefAttribute")

    def has_supported_architecture(self) -> bool:
        return self.has("Windows.Win32.Interop.SupportedArchitectureAttribute")

    def get_supported_architecture(self) -> list[str]:
        return self.get("Windows.Win32.Interop.SupportedArchitectureAttribute").fixed_arguments[0].value

    def has_guid(self) -> bool:
        return self.has("Windows.Foundation.Metadata.GuidAttribute")

    def get_guid(self) -> str:
        v = [fa.value for fa in self.get("Windows.Foundation.Metadata.GuidAttribute").fixed_arguments]
        assert len(v) == 11
        return self.format_guid(v)

    def format_guid(self, v: list[int]) -> str:
        return f"{v[0]:08x}-{v[1]:04x}-{v[2]:04x}-{v[3]:02x}-{v[4]:02x}-{v[5]:02x}-{v[6]:02x}-{v[7]:02x}-{v[8]:02x}-{v[9]:02x}-{v[10]:02x}"

    def get_property_key(self) -> tuple[str, int]:
        value = self.get("Windows.Win32.Interop.ConstantAttribute").fixed_arguments[0].value
        m = re.fullmatch(r"{(\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)}, (\d+)", value)
        if not m:
            raise ValueError()
        v = [int(d) for d in m.groups()]
        assert len(v) == 12
        guid = self.format_guid(v[:11])
        pid = v[11]
        return guid, pid

    def has_constant(self) -> bool:
        return self.has("Windows.Win32.Interop.ConstantAttribute")

    def get_constant(self) -> str:
        # value is like "{0, 0, 0, 0, 0, 5}"
        value = self.get("Windows.Win32.Interop.ConstantAttribute").fixed_arguments[0].value
        value_csv = value.translate({ord("{"): "(", ord("}"): ")"})
        return value_csv

    def get_unmanaged_function_pointer(self) -> str:
        return self.get("System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute").fixed_arguments[0].value

    def get_contract_version(self) -> CustomAttributeFixedArgument:
        return self.get("Windows.Foundation.Metadata.ContractVersionAttribute").fixed_arguments[0]

    def has_overload(self) -> bool:
        return self.has("Windows.Foundation.Metadata.OverloadAttribute")

    def get_overload(self) -> str:
        return self.get("Windows.Foundation.Metadata.OverloadAttribute").fixed_arguments[0].value

    def get_static(self) -> list[CustomAttribute]:
        return [ca for ca in self.get_list("Windows.Foundation.Metadata.StaticAttribute")]

    def get_activatable(self) -> list[CustomAttribute]:
        return [ca for ca in self.get_list("Windows.Foundation.Metadata.ActivatableAttribute")]


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

    @property
    def kind(self) -> str:
        return self.interface.kind

    @property
    def namespace(self) -> str:
        if self.kind == "TypeReference":
            return self.interface.type_reference.namespace
        elif self.kind == "TypeSpecification":
            return self.interface.type_specification.signature.type.namespace
        else:
            raise NotImplementedError()

    @property
    def name(self) -> str:
        if self.kind == "TypeReference":
            return self.interface.type_reference.name
        elif self.kind == "TypeSpecification":
            return self.interface.type_specification.signature.type.name
        else:
            raise NotImplementedError()

    @property
    def fullname(self) -> str:
        if self.kind == "TypeReference":
            return self.interface.type_reference.fullname
        elif self.kind == "TypeSpecification":
            return self.interface.type_specification.signature.type.fullname
        else:
            raise NotImplementedError()

    @property
    def generic_fullname(self) -> str:
        if self.kind == "TypeReference":
            return self.interface.type_reference.fullname
        elif self.kind == "TypeSpecification":
            if self.interface.type_specification.signature.kind == "Generic":
                return self.interface.type_specification.signature.generic_fullname
            return self.interface.type_specification.signature.type.fullname
        else:
            raise NotImplementedError()


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
        return Metadata(td for td in meta if self.is_public(td))

    def is_public(self, td: TypeDefinition) -> bool:
        if td.namespace == "":
            return False
        elif td.basetype == "System.Attribute":
            return False
        return True

    def sort(self, meta: Metadata) -> Metadata:
        return Metadata(sorted(meta, key=lambda td: (td.namespace, td.name)))

    def patch_link_typedef(self, meta: Metadata) -> None:
        # FIXME: ns's key can be duplicated with arch variation.  Don't care for now.
        ns = {td.fullname: td for td in meta}
        for td in meta:
            if TYPE_CHECKING:
                assert td.basetype is not None
            td["_basetype_typedef"] = ns.get(td.basetype)
            for ii in td.interface_implementations:
                ii["_typedef"] = ns[ii.fullname]
                if ii.kind == "TypeSpecification":
                    for t in ii.interface.type_specification.signature.enumerate_types():
                        t = t.get_element_type()
                        if t.kind == "Type":
                            t["_typedef"] = ns.get(t.fullname)
            for ca in td.custom_attributes.get_activatable():
                if ca.fixed_arguments[0].type.kind == "Type":
                    ca["_typedef"] = ns.get(ca.fixed_arguments[0].value)
            for ca in td.custom_attributes.get_static():
                ca["_typedef"] = ns.get(ca.fixed_arguments[0].value)
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
                vtbl_index = self.count_interface_method(td)
                for md in td.method_definitions:
                    if md.name == ".ctor":
                        continue
                    md["_vtbl_index"] = vtbl_index
                    vtbl_index += 1

    def count_interface_method(self, td: TypeDefinition) -> int:
        if td.basetype is None or td.basetype == "System.Object":
            return 6  # count of IInspectable
        elif td.basetype == "System.MulticastDelegate":
            return 3  # count of IUnknown
        basetype = td["_basetype_typedef"]
        return len(td.method_definitions) + self.count_interface_method(basetype)

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
                if ii.kind == "TypeReference":
                    ii.interface.type_reference["Namespace"] = namespace
                elif ii.kind == "TypeSpecification":
                    ii.interface.type_specification.signature.type["Namespace"] = namespace
                else:
                    raise NotImplementedError()
            for t in td.enumerate_types():
                t = t.get_element_type()
                if t.kind == "Type" and t.namespace != "System" and t.namespace != "":
                    t["Namespace"] = namespace


class PyGenerator:
    def emit(self, td: TypeDefinition) -> str:
        if td.kind == "function_pointer":
            return self.emit_function_pointer(td)
        elif td.kind == "enum":
            return self.emit_enum(td)
        elif td.kind == "struct":
            return self.emit_struct_union(td)
        elif td.kind == "contract_version":
            return self.emit_contract_version(td)
        elif td.kind == "com":
            return self.emit_com(td)
        else:
            raise NotImplementedError()

    def emit_function_pointer(self, td: TypeDefinition) -> str:
        writer = StringIO()
        indent = self.write_architecture_specific_block_if_necessary(writer, td.custom_attributes)
        functype = self.function_pointer_functype(td)
        md = td.method_definitions[1]  # [0]=.ctor, [1]=Invoke
        restype = md.signature.return_type.pytype
        params_csv = md.format_parameters()
        name = td.generic_strip_suffix(td.name)
        writer.write(f"{indent}@{functype}\n")
        writer.write(f"{indent}def {name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def function_pointer_functype(self, td: TypeDefinition) -> str:
        if "WindowsRuntime" in td.attributes:
            return "winfunctype_pointer"
        raise NotImplementedError()

    def emit_enum(self, td: TypeDefinition) -> str:
        writer = StringIO()
        type_field, *value_fields = td.fields
        writer.write(f"{td.name} = {type_field.signature.pytype}\n")
        for fd in value_fields:
            writer.write(f"{fd.name}: {td.name} = {fd.default_value.value}\n")
        return writer.getvalue()

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

    def emit_contract_version(self, td: TypeDefinition) -> str:
        contract_version = td.custom_attributes.get_contract_version()
        return f"{td.name}: {contract_version.type.name} = {contract_version.value}\n"

    def emit_com(self, td: TypeDefinition) -> str:
        writer = StringIO()
        if td.is_generic:
            generic_parameters = td.format_generic_parameters()
            name = td.generic_strip_suffix(td.name)
            base = f"Generic[{generic_parameters}], ComPtr"
        else:
            name = td.name
            base = "ComPtr"
        extends = self.com_base_type(td)
        writer.write(f"class {name}({base}):\n")
        writer.write(f"    extends: {extends}\n")
        if td.custom_attributes.has_guid():
            guid = td.custom_attributes.get_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        if "Sealed" in td.attributes:
            writer.write(f"    _classid_ = '{td.namespace}.{name}'\n")
        for ca in td.custom_attributes.get_activatable():
            if ca.fixed_arguments[0].type.kind == "Type":
                factory = ca["_typedef"]
                for md in factory.method_definitions:
                    assert md.signature.return_type.fullname == td.fullname
                    writer.write(self.winrt_factorymethod(factory, md))
            else:
                writer.write(self.winrt_activatemethod(td))
        properties: dict[str, dict[str, str | None]] = defaultdict(lambda: {"get": None, "put": None})
        for md in td.method_definitions:
            if md.name == ".ctor":
                continue
            if "SpecialName" in md.attributes:
                if md.name.startswith("get_"):
                    properties[md.name.removeprefix("get_")]["get"] = md.name
                elif md.name.startswith("put_"):
                    properties[md.name.removeprefix("put_")]["put"] = md.name
            writer.write(self.winrt_method(td, md))
        for name, funcs in properties.items():
            writer.write(f"    {name} = property({funcs['get']}, {funcs['put']})\n")
        return writer.getvalue()

    def com_base_type(self, td: TypeDefinition) -> str:
        if td.basetype is None:
            return "Windows.Win32.System.WinRT.IInspectable"
        elif td.basetype == "System.Object":
            return "Windows.Win32.System.WinRT.IInspectable"
        elif td.basetype == "System.MulticastDelegate":
            return "Windows.Win32.System.Com.IUnknown"
        else:
            return td.basetype

    def com_implement_types(self, td: TypeDefinition) -> str:
        return ", ".join(ii.generic_fullname for ii in td.interface_implementations)

    def com_static_types(self, td: TypeDefinition) -> str:
        return ", ".join(ca.fixed_arguments[0].value for ca in td.custom_attributes.get_static())

    def com_get_interface_for_method(self, td: TypeDefinition, method_name: str) -> str:
        for ii in td.interface_implementations:
            td_interface = ii["_typedef"]
            for md in td_interface.method_definitions:
                if md.custom_attributes.has_overload():
                    static_method_name = md.custom_attributes.get_overload()
                else:
                    static_method_name = md.name
                if static_method_name == method_name:
                    return ii.generic_fullname
        raise KeyError()

    def com_get_static_for_method(self, td: TypeDefinition, method_name: str) -> str:
        for ca in td.custom_attributes.get_static():
            for md in ca["_typedef"].method_definitions:
                if md.custom_attributes.has_overload():
                    static_method_name = md.custom_attributes.get_overload()
                else:
                    static_method_name = md.name
                if static_method_name == method_name:
                    return ca.fixed_arguments[0].value
        raise KeyError()

    def winrt_method(self, td: TypeDefinition, md: MethodDefinition) -> str:
        writer = StringIO()
        if md.custom_attributes.has_overload():
            method_name = md.custom_attributes.get_overload()
        else:
            method_name = md.name
        params = md.format_parameters_list()
        restype = md.signature.return_type.pytype
        if td.basetype == "System.MulticastDelegate":
            vtbl_index = md["_vtbl_index"]
            writer.write(f"    @winrt_commethod({vtbl_index})\n")
            params.insert(0, "self")
        elif "Static" in md.attributes:
            writer.write(f"    @winrt_classmethod\n")
            interface = self.com_get_static_for_method(td, method_name)
            params.insert(0, f"cls: {interface}")
        elif "Sealed" in td.attributes:
            writer.write(f"    @winrt_mixinmethod\n")
            interface = self.com_get_interface_for_method(td, method_name)
            params.insert(0, f"self: {interface}")
        else:
            vtbl_index = md["_vtbl_index"]
            writer.write(f"    @winrt_commethod({vtbl_index})\n")
            params.insert(0, "self")
        params_csv = ", ".join(params)
        writer.write(f"    def {method_name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def winrt_factorymethod(self, td: TypeDefinition, md: MethodDefinition) -> str:
        writer = StringIO()
        if td.is_generic:
            name = td.generic_fullname
        else:
            name = td.fullname
        params = [f"cls: {name}"]
        params.extend(md.format_parameters_list())
        params_csv = ", ".join(params)
        restype = md.signature.return_type.pytype
        writer.write(f"    @winrt_factorymethod\n")
        writer.write(f"    def {md.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def winrt_activatemethod(self, td: TypeDefinition) -> str:
        writer = StringIO()
        if td.is_generic:
            name = td.generic_fullname
        else:
            name = td.fullname
        writer.write(f"    @winrt_activatemethod\n")
        writer.write(f"    def New(cls) -> {name}: ...\n")  # FIXME: proper name?
        return writer.getvalue()

    def emit_header(self, import_namespaces: set[str]) -> str:
        writer = StringIO()
        writer.write(self.emit_import_annotations())
        writer.write(self.emit_import_ctypes())
        writer.write(self.emit_import_typing())
        writer.write(self.emit_import_base())
        writer.write(self.emit_import_winrt())
        writer.write(self.emit_import_namespaces(import_namespaces))
        writer.write(self.emit_getattr())
        return writer.getvalue()

    def emit_header_one(self) -> str:
        writer = StringIO()
        writer.write(self.emit_import_annotations())
        writer.write(self.emit_import_ctypes())
        writer.write(self.emit_import_typing())
        writer.write(self.emit_include_base())
        writer.write(self.emit_getattr())
        return writer.getvalue()

    def emit_import_annotations(self) -> str:
        return "from __future__ import annotations\n"

    def emit_import_ctypes(self) -> str:
        return "from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll\n"

    # FIXME: WORKAROUND
    def emit_import_typing(self) -> str:
        return "".join(
            [
                "from typing import Generic, TypeVar\n",
                "K = TypeVar('T')\n",
                "T = TypeVar('T')\n",
                "V = TypeVar('V')\n",
                "TProgress = TypeVar('TProgress')\n",
                "TResult = TypeVar('TResult')\n",
                "TSender = TypeVar('TSender')\n",
            ]
        )

    def emit_import_base(self) -> str:
        return f"from Windows import {BASE_EXPORTS_CSV}\n"

    def emit_import_winrt(self) -> str:
        return f"from Windows._winrt import {WINRT_EXPORTS_CSV}\n"

    def emit_include_base(self) -> str:
        return (Path(__file__).parent / "Windows\\__init__.py").read_text()

    def emit_import_namespaces(self, import_namespaces: set[str]) -> str:
        writer = StringIO()
        writer.write("import Windows.Win32.System.WinRT\n")
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
            writer.write(f"{indent}make_head(_module, '{td.name_no_generic}')\n")
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
            yield ii.fullname
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
    # FIXME: --one not work for now
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
