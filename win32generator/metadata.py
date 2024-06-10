from __future__ import annotations

import re
from collections.abc import Iterator
from typing import Any, Collection

from .backport import TypeAlias

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
    def generic_name(self) -> str:
        return self.name.split("`")[0]

    @property
    def generic_fullname(self) -> str:
        return f"{self.namespace}.{self.generic_name}"

    @property
    def type(self) -> TType:
        if self["Type"] is None:
            raise KeyError()
        return TType(self["Type"])

    @property
    def lower_bounds(self) -> list[int]:
        if self["LowerBounds"] is None:
            raise KeyError()
        return self["LowerBounds"]

    @property
    def rank(self) -> int:
        if self["Rank"] is None:
            raise KeyError()
        return self["Rank"]

    @property
    def sizes(self) -> list[int]:
        if self["Sizes"] is None:
            raise KeyError()
        return self["Sizes"]

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
    def is_nested(self) -> bool:
        return self.kind == "Type" and self.namespace == ""


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
    def generic_name(self) -> str:
        return self.name.split("`")[0]

    @property
    def generic_fullname(self) -> str:
        return f"{self.namespace}.{self.generic_name}"

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
    def methods(self) -> list[MethodDefinition]:
        return [MethodDefinition(md) for md in self["Methods"]]

    @property
    def nested_types(self) -> list[TypeDefinition]:
        return [TypeDefinition(td) for td in self["NestedTypes"]]

    @property
    def generic_parameters(self) -> list[GenericParameter]:
        return [GenericParameter(gp) for gp in self["GenericParameters"]]

    @property
    def is_winrt(self) -> bool:
        return "WindowsRuntime" in self.attributes

    @property
    def is_win32(self) -> bool:
        return not self.is_winrt

    @property
    def is_generic(self) -> bool:
        return "`" in self.name


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

    def has_winrt_guid(self) -> bool:
        return self.has("Windows.Foundation.Metadata.GuidAttribute")

    def get_winrt_guid(self) -> str:
        v = [fa.value for fa in self.get("Windows.Foundation.Metadata.GuidAttribute").fixed_arguments]
        assert len(v) == 11
        return self.format_guid(v)

    def get_contract_version(self) -> CustomAttributeFixedArgument:
        return self.get("Windows.Foundation.Metadata.ContractVersionAttribute").fixed_arguments[0]

    def has_default_overload(self) -> bool:
        return self.has("Windows.Foundation.Metadata.DefaultOverloadAttribute")

    def has_overload(self) -> bool:
        return self.has("Windows.Foundation.Metadata.OverloadAttribute")

    def get_overload(self) -> str:
        return self.get("Windows.Foundation.Metadata.OverloadAttribute").fixed_arguments[0].value

    def has_static(self) -> bool:
        return self.has("Windows.Foundation.Metadata.StaticAttribute")

    def get_static(self) -> list[CustomAttribute]:
        return [ca for ca in self.get_list("Windows.Foundation.Metadata.StaticAttribute")]

    def has_activatable(self) -> bool:
        return self.has("Windows.Foundation.Metadata.ActivatableAttribute")

    def get_activatable(self) -> list[CustomAttribute]:
        return [ca for ca in self.get_list("Windows.Foundation.Metadata.ActivatableAttribute")]

    def has_default(self) -> bool:
        return self.has("Windows.Foundation.Metadata.DefaultAttribute")

    def has_composable(self) -> bool:
        return self.has("Windows.Foundation.Metadata.ComposableAttribute")

    def get_composable(self) -> CustomAttribute:
        return self.get("Windows.Foundation.Metadata.ComposableAttribute")

    def has_scoped_enum(self) -> bool:
        return self.has("Windows.Win32.Foundation.Metadata.ScopedEnumAttribute")

    def has_ansi(self) -> bool:
        return self.has("Windows.Win32.Foundation.Metadata.AnsiAttribute")

    def has_unicode(self) -> bool:
        return self.has("Windows.Win32.Foundation.Metadata.UnicodeAttribute")


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
    def namespace(self) -> str:
        if self.interface.kind == "TypeReference":
            return self.interface.type_reference.namespace
        elif self.interface.kind == "TypeSpecification":
            return self.interface.type_specification.signature.type.namespace
        else:
            raise NotImplementedError()

    @property
    def name(self) -> str:
        if self.interface.kind == "TypeReference":
            return self.interface.type_reference.name
        elif self.interface.kind == "TypeSpecification":
            return self.interface.type_specification.signature.type.name
        else:
            raise NotImplementedError()

    @property
    def fullname(self) -> str:
        if self.interface.kind == "TypeReference":
            return self.interface.type_reference.fullname
        elif self.interface.kind == "TypeSpecification":
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

    # SequenceNumber == 0 is return type and it can be missing.
    @property
    def parameters_with_type(self) -> list[tuple[Parameter, TType]]:
        types = self.signature.parameter_types
        return [(pa, types[pa.sequence_number - 1]) for pa in self.parameters if pa.sequence_number != 0]

    def get_parameter_names(self) -> list[str]:
        return [pa.name for pa in self.parameters if pa.sequence_number != 0]

    @property
    def name_overload(self) -> str:
        if self.custom_attributes.has_overload():
            return self.custom_attributes.get_overload()
        return self.name


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


class Metadata:
    def __init__(self, js: JsonType) -> None:
        self.js = js

    def __getitem__(self, key: int) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: int, value: JsonType) -> None:
        self.js[key] = value

    @property
    def type_definitions(self) -> list[TypeDefinition]:
        return [TypeDefinition(td) for td in self.js]
