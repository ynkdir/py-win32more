from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from typing import TypeAlias, Generator, Any, TextIO

PACKAGE_NAME = "win32more"
ARCHITECTURE = "X64"
BASE_EXPORTS = ["MissingType", "c_char_p_no", "c_wchar_p_no", "Byte", "SByte", "Char", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64", "IntPtr", "UIntPtr", "Single", "Double", "String", "Boolean", "Void", "Guid", "COMMETHOD", "SUCCEEDED", "FAILED"]
BASE_EXPORTS_CSV = ", ".join(BASE_EXPORTS)

JsonType: TypeAlias = Any

class TType:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
        return TType(self.ns, self["Type"])

    @property
    def size(self) -> int:
        if self["Size"] is None:
            raise KeyError()
        return self["Size"]

    @property
    def pytype(self) -> str:
        match self.kind:
            case "Primitive":
                return self.name
            case "Pointer":
                if self.type.kind == "Primitive" and self.type.name == "Void":
                    return "c_void_p"
                elif self.type.kind == "Primitive" and self.type.name == "Byte":
                    return "c_char_p_no"    # safe?
                elif self.type.kind == "Primitive" and self.type.name == "Char":
                    return "c_wchar_p_no"   # safe?
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
                    return self.name[1:]    # remove first "."
                elif self.is_guid:
                    return "Guid"
                elif self.is_missing:
                    print(f"DEBUG: missing type '{self.name}'")
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

    @property
    def is_nested(self) -> bool:
        return self.kind == "Type" and self.name.startswith(".")    # e.g. "._Anonymous_e_Struct"

    @property
    def is_guid(self) -> bool:
        return self.kind == "Type" and self.name == "System.Guid"

    # missing type which is not defined in current winmd.
    @property
    def is_missing(self) -> bool:
        return self.kind == "Type" and self.name not in self.ns

    @property
    def is_struct(self) -> bool:
        if not self.is_nested and not self.is_guid and not self.is_missing:
            return self.kind == "Type" and self.ns[self.name].kind in ("union", "struct")
        return False

    @property
    def is_com(self) -> bool:
        if not self.is_nested and not self.is_guid and not self.is_missing:
            return self.kind == "Type" and self.ns[self.name].kind == "com"
        return False

class TypeDefinition:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
    def basetype(self) -> str:
        return self["BaseType"]

    @property
    def is_nested(self) -> bool:
        return self["IsNested"]

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(self.ns, ca) for ca in self["CustomAttributes"]]

    @property
    def fields(self) -> list[FieldDefinition]:
        return [FieldDefinition(self.ns, fd) for fd in self["Fields"]]

    @property
    def interface_implementations(self) -> list[InterfaceImplementation]:
        return [InterfaceImplementation(self.ns, ii) for ii in self["InterfaceImplementations"]]

    @property
    def layout(self) -> TypeLayout:
        return TypeLayout(self.ns, self["Layout"])

    @property
    def method_definitions(self) -> list[MethodDefinition]:
        return [MethodDefinition(self.ns, md) for md in self["MethodDefinitions"]]

    @property
    def nested_types(self) -> list[TypeDefinition]:
        return [TypeDefinition(self.ns, td) for td in self["NestedTypes"]]

    @property
    def kind(self) -> str:
        match self.basetype:
            case "System.Object":
                return "object" # CONSTANT, FUNCTION
            case "System.MulticastDelegate":
                return "function_pointer"
            case "System.Enum":
                return "enum"
            case "System.ValueType":
                if self.has_custom_attribute("Windows.Win32.Interop.NativeTypedefAttribute"):
                    return "native_typedef"
                # FIXME:
                elif self.has_custom_attribute("Windows.Win32.Interop.GuidAttribute") and not self.fields:
                    return "guid"
                elif "ExplicitLayout" in self.attributes:
                    return "union"
                else:
                    return "struct"
            case "TypeDefinition":
                return "com"
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
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
        return [CustomAttributeFixedArgument(self.ns, ta) for ta in self["FixedArguments"]]

    @property
    def named_arguments(self) -> list[CustomAttributeNamedArgument]:
        return [CustomAttributeNamedArgument(self.ns, na) for na in self["NamedArguments"]]

    def guid_value(self) -> tuple[str, list[JsonType]]:
        v = [fa.value for fa in self.fixed_arguments]
        guid = f"{v[0]:08x}-{v[1]:04x}-{v[2]:04x}-{v[3]:02x}-{v[4]:02x}-{v[5]:02x}-{v[6]:02x}-{v[7]:02x}-{v[8]:02x}-{v[9]:02x}-{v[10]:02x}"
        return guid, v[11:]

class CustomAttributeFixedArgument:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def type(self) -> TType:
        return TType(self.ns, self["Type"])

    @property
    def value(self) -> JsonType:
        return self["Value"]

class CustomAttributeNamedArgument:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType):
        self.ns = ns
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
        return TType(self.ns, self["Type"])

    @property
    def value(self) -> JsonType:
        return self["Value"]

class FieldDefinition:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def type(self) -> TType:
        return TType(self.ns, self["Type"])

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(self.ns, ca) for ca in self["CustomAttributes"]]

    @property
    def default_value(self) -> Constant:
        if self["DefaultValue"] is None:
            raise KeyError()
        return Constant(self.ns, self["DefaultValue"])

    @property
    def pyvalue(self) -> str:
        if "HasDefault" in self.attributes:
            return ascii(self.default_value.value)
        elif self.type.kind == "Type" and self.type.name == "System.Guid":
            guid, rest = self.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
            assert(len(rest) == 0)
            return f"Guid('{guid}')"
        elif self.type.kind == "Type" and self.type.name == f"{PACKAGE_NAME}.Devices.Properties.DEVPROPKEY":
            guid, rest = self.get_custom_attribute("Windows.Win32.Interop.PropertyKeyAttribute").guid_value()
            assert(len(rest) == 1)
            return f"{self.type.name}(fmtid=Guid('{guid}'), pid={rest[0]})"
        elif self.type.kind == "Type" and self.type.name == f"{PACKAGE_NAME}.UI.Shell.PropertiesSystem.PROPERTYKEY":
            guid, rest = self.get_custom_attribute("Windows.Win32.Interop.PropertyKeyAttribute").guid_value()
            assert(len(rest) == 1)
            return f"{self.type.name}(fmtid=Guid('{guid}'), pid={rest[0]})"
        else:
            # FIXME:
            raise NotImplementedError()

    def get_custom_attribute(self, type_: str) -> CustomAttribute:
        for ca in self.custom_attributes:
            if ca.type == type_:
                return ca
        raise KeyError()

class Constant:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def interface(self) -> str:
        return self["Interface"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(self.ns, ca) for ca in self["CustomAttributes"]]

class TypeLayout:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
        return [CustomAttribute(self.ns, ca) for ca in self["CustomAttributes"]]

    @property
    def impl_attributes(self) -> list[str]:
        return self["ImplAttributes"]

    @property
    def import_(self) -> MethodImport:
        if self["Import"] is None:
            raise KeyError()
        return MethodImport(self.ns, self["Import"])

    @property
    def signature_header(self) -> SignatureHeader:
        return SignatureHeader(self.ns, self["SignatureHeader"])

    @property
    def return_type(self) -> ReturnType:
        return ReturnType(self.ns, self["ReturnType"])

    @property
    def parameters(self) -> list[Parameter]:
        return [Parameter(self.ns, pa) for pa in self["Parameters"]]

class SignatureHeader:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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

class ReturnType:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def type(self) -> TType:
        return TType(self.ns, self["Type"])

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(self.ns, ca) for ca in self["CustomAttributes"]]

class Parameter:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
        self.js = js

    def __getitem__(self, key: str) -> JsonType:
        return self.js[key]

    def __setitem__(self, key: str, value: JsonType) -> None:
        self.js[key] = value

    @property
    def name(self) -> str:
        return self["Name"]

    @property
    def type(self) -> TType:
        return TType(self.ns, self["Type"])

    @property
    def sequence_number(self) -> int:
        return self["SequenceNumber"]

    @property
    def attributes(self) -> list[str]:
        return self["Attributes"]

    @property
    def custom_attributes(self) -> list[CustomAttribute]:
        return [CustomAttribute(self.ns, ca) for ca in self["CustomAttributes"]]

class MethodImport:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
        return ModuleReference(self.ns, self["Module"])

class ModuleReference:
    def __init__(self, ns: dict[str, TypeDefinition], js: JsonType) -> None:
        self.ns = ns
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
        return [CustomAttribute(self.ns, ca) for ca in self["CustomAttributes"]]

class Preprocessor:
    def filter_public(self, typedefs: list[TypeDefinition]) -> list[TypeDefinition]:
        return [td for td in typedefs if td.namespace != "" and "Public" in td.attributes]

    def filter_architecture(self, typedefs: list[TypeDefinition], arch: str) -> list[TypeDefinition]:
        typedefs = [td for td in typedefs if self.has_architecture(td["CustomAttributes"], arch)]
        for td in typedefs:
            if td.name == "Apis":
                td["MethodDefinitions"] = [md for md in td["MethodDefinitions"] if self.has_architecture(md["CustomAttributes"], arch)]
        return typedefs

    def has_architecture(self, custom_attributes: list[JsonType], arch: str) -> bool:
        for ca in custom_attributes:
            if ca["Type"] == "Windows.Win32.Interop.SupportedArchitectureAttribute":
                return arch in ca["FixedArguments"][0]["Value"]
        return True

    def patch_struct_nested_type(self, ns: dict[str, TypeDefinition]) -> None:
        for td in ns.values():
            self.patch_nested_type(td)

    # Rename nested type to {struct_name}_{nested_name}_e__{Struct|Union}
    def patch_nested_type(self, td: TypeDefinition) -> None:
        renamed = {}
        for nt in td.nested_types:
            newname = f"{td['Name']}_{nt['Name']}"
            renamed[f".{nt['Name']}"] = f".{newname}"
            nt["Name"] = newname
            self.patch_nested_type(nt)
        for fd in td.fields:
            t = fd.type.get_element_type()
            if t["Name"] in renamed:
                t["Name"] = renamed[t["Name"]]

    # FIXME: enum value name? (NAME or ENUM_NAME or ENUM.Name?)
    def patch_enum(self, ns: dict[str, TypeDefinition]) -> None:
        for td in ns.values():
            if td.basetype == "System.Enum" and self.enum_need_prefix(td):
                for fd in td.fields:
                    fd["Name"] = f"{td['Name']}_{fd['Name']}"

    def enum_need_prefix(self, td: TypeDefinition) -> bool:
        for fd in td.fields:
            if not ("_" in fd.name or fd.name.isupper()):
                return True
        return False

    # Add vtbl_index to COM methods.
    def patch_com_vtbl_index(self, ns: dict[str, TypeDefinition]) -> None:
        for td in ns.values():
            if td.basetype == "TypeDefinition":
                vtbl_index = self.count_interface_method(ns, td.interface_implementations)
                for md in td.method_definitions:
                    md["_vtbl_index"] = vtbl_index
                    vtbl_index += 1

    def count_interface_method(self, ns: dict[str, TypeDefinition], interfaces: list[InterfaceImplementation]) -> int:
        if not interfaces:
            return 0
        td = ns[interfaces[0]["Interface"]]
        return len(td.method_definitions) + self.count_interface_method(ns, td.interface_implementations)

    def patch_name_conflict(self, ns: dict[str, TypeDefinition]) -> None:
        for td in ns.values():
            if td.name == "Apis":
                for fd in td.fields:
                    if f"{td.namespace}.{fd.name}" in ns:
                        print(f"DEBUG: name conflict '{td.namespace}.{fd.name}'")
                        fd["Name"] = f"{fd['Name']}_CONSTANT"

    def patch_namespace(self, ns: dict[str, TypeDefinition], packagename: str) -> None:
        def patch(name: str) -> str:
            return re.sub(r"^Windows.Win32.", f"{packagename}.", name)
        newns = {}
        for td in ns.values():
            td["Namespace"] = patch(td["Namespace"])
            for ii in td.interface_implementations:
                ii["Interface"] = patch(ii["Interface"])
            for t in self.foreach_type(td):
                t = t.get_element_type()
                t["Name"] = patch(t["Name"])
            newns[td.fullname] = td
        ns.clear()
        ns.update(newns)

    def foreach_type(self, td: TypeDefinition) -> Generator[TType, None, None]:
        for fd in td.fields:
            yield fd.type
        for md in td.method_definitions:
            yield md.return_type.type
            for pa in md.parameters:
                yield pa.type
        for nested_type in td.nested_types:
            for t in self.foreach_type(nested_type):
                yield t

    def get_namespace(self, fullname: str) -> str:
        return fullname.rsplit(".", 1)[0]

    def collect_import_namespace(self, td: TypeDefinition, import_namespaces: set[str]) -> None:
        for ii in td.interface_implementations:
            import_namespaces.add(self.get_namespace(ii.interface))
        for t in self.foreach_type(td):
            t = t.get_element_type()
            if t.kind == "Type" and not t.is_nested and not t.is_guid and not t.is_missing:
                import_namespaces.add(self.get_namespace(t.name))

    def collect_export_name(self, td: TypeDefinition, export_names: set[str]) -> None:
        match td.kind:
            case "object":
                for field in td.fields:
                    export_names.add(field.name)
                for md in td.method_definitions:
                    export_names.add(md.name)
            case "enum":
                export_names.add(td.name)
                for field in td.fields[1:]:
                    export_names.add(field.name)
            case "function_pointer" | "native_typedef" | "guid" | "union" | "struct" | "com":
                export_names.add(td.name)
            case _:
                raise NotImplementedError()

class PyGenerator:
    def emit(self, writer: TextIO, td: TypeDefinition) -> None:
        match td.kind:
            case "object": # CONSTANT, FUNCTION
                self.emit_object(writer, td)
            case "function_pointer":
                self.emit_function_pointer(writer, td)
            case "enum":
                self.emit_enum(writer, td)
            case "native_typedef":
                self.emit_native_typedef(writer, td)
            case "guid":
                self.emit_guid(writer, td)
            case "union":
                self.emit_struct_union(writer, td)
            case "struct":
                self.emit_struct_union(writer, td)
            case "com":
                self.emit_com(writer, td)
            case _:
                raise NotImplementedError()

    def emit_object(self, writer: TextIO, td: TypeDefinition) -> None:
        for field in td.fields:
            self.emit_constant(writer, field)
        for md in td.method_definitions:
            self.emit_function(writer, md)

    def emit_constant(self, writer: TextIO, field: FieldDefinition) -> None:
        if "HasDefault" in field.attributes:
            # primitive
            writer.write(f"{field.name} = {field.pyvalue}\n")
        else:
            writer.write(f"def _define_{field.name}():\n")
            writer.write(f"    return {field.pyvalue}\n")

    def emit_function(self, writer: TextIO, md: MethodDefinition) -> None:
        dll = md.import_.module.name
        if "CallingConventionWinApi" in md.import_.attributes:
            functype = "WINFUNCTYPE"
            library = f"windll['{dll}']"
        elif "CallingConventionCDecl" in md.import_.attributes:
            functype = "CFUNCTYPE"
            library = f"cdll['{dll}']"
        else:
            raise NotImplementedError()
        restype = md.return_type.type.pytype
        argtypes = [pa.type.pytype for pa in md.parameters]
        argtypes_csv = ",".join(argtypes)
        inout = 1 # "pa.attributes has "In" (1) or "Out" (2) or both(3)
        paramflags = [(inout, pa.name) for pa in md.parameters]
        if paramflags:
            paramflags_csv = ",".join(f"({inout}, '{name}')" for inout, name in paramflags) + ","
        else:
            paramflags_csv = ""
        writer.write(f"def _define_{md.name}():\n")
        writer.write(f"    try:\n")
        writer.write(f"        return {functype}({restype},{argtypes_csv})(('{md.name}', {library}), ({paramflags_csv}))\n")
        writer.write(f"    except (FileNotFoundError, AttributeError):\n")
        writer.write(f"        return None\n")

    def emit_function_pointer(self, writer: TextIO, td: TypeDefinition) -> None:
        callconv = td.get_custom_attribute("System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute").fixed_arguments[0].value
        if callconv == "Winapi":
            functype = "WINFUNCTYPE"
        elif callconv == "Cdecl":
            functype = "CFUNCTYPE"
        else:
            raise NotImplementedError()
        md = td.method_definitions[1]     # [0]=.ctor, [1]=Invoke
        restype = md.return_type.type.pytype
        argtypes = [pa.type.pytype for pa in md.parameters]
        argtypes_csv = ",".join(argtypes)
        writer.write(f"def _define_{td.name}():\n")
        writer.write(f"    return {functype}({restype},{argtypes_csv})\n")

    def emit_enum(self, writer: TextIO, td: TypeDefinition) -> None:
        type_field, *value_fields = td.fields
        writer.write(f"{td.name} = {type_field.type.pytype}\n")
        for field in value_fields:
            writer.write(f"{field.name} = {field.default_value.value}\n")

    def emit_native_typedef(self, writer: TextIO, td: TypeDefinition) -> None:
        pytype = td.fields[0].type.pytype
        writer.write(f"{td.name} = {pytype}\n")

    def emit_guid(self, writer: TextIO, td: TypeDefinition) -> None:
        guid, rest = td.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
        writer.write(f"{td.name} = Guid('{guid}')\n")

    def emit_struct_union(self, writer: TextIO, td: TypeDefinition, nested: bool = False) -> None:
        if td.kind == "struct":
            base = "Structure"
        elif td.kind == "union":
            base = "Union"
        else:
            raise NotImplementedError()

        if not nested:
            writer.write(f"def _define_{td.name}_head():\n")
            writer.write(f"    class {td.name}({base}):\n")
            writer.write(f"        pass\n")
            writer.write(f"    return {td.name}\n")
            writer.write(f"def _define_{td.name}():\n")
            writer.write(f"    {td.name} = {td.fullname}_head\n")
        else:
            writer.write(f"    class {td.name}({base}):\n")
            writer.write(f"        pass\n")

        for nested_type in td.nested_types:
            self.emit_struct_union(writer, nested_type, nested=True)

        if td.layout.packing_size != 0:
            writer.write(f"    {td.name}._pack_ = {td.layout.packing_size}\n")

        anonymous = []
        for field in td.fields:
            if re.match(r"^Anonymous\d*$", field.name):
                anonymous.append(field.name)
        if anonymous:
            writer.write(f"    {td.name}._anonymous_ = [\n")
            for name in anonymous:
                writer.write(f"        '{name}',\n")
            writer.write("    ]\n")

        if td.fields:
            writer.write(f"    {td.name}._fields_ = [\n")
            for field in td.fields:
                writer.write(f"        ('{field.name}', {field.type.pytype}),\n")
            writer.write("    ]\n")

        if not nested:
            writer.write(f"    return {td.name}\n")

    def emit_com(self, writer: TextIO, td: TypeDefinition) -> None:
        assert(len(td.interface_implementations) <= 1)
        if td.interface_implementations == []:
            base = "c_void_p"
            base_head = "c_void_p"
        else:
            base = td.interface_implementations[0].interface
            base_head = f"{base}_head"
        if td.has_custom_attribute("Windows.Win32.Interop.GuidAttribute"):
            guid, rest = td.get_custom_attribute("Windows.Win32.Interop.GuidAttribute").guid_value()
        else:
            guid = None
        writer.write(f"def _define_{td.name}_head():\n")
        writer.write(f"    class {td.name}({base_head}):\n")
        if guid is None:
            writer.write(f"        pass\n")
        else:
            writer.write(f"        Guid = Guid('{guid}')\n")
        writer.write(f"    return {td.name}\n")
        writer.write(f"def _define_{td.name}():\n")
        writer.write(f"    {td.name} = {td.fullname}_head\n")
        for md in td.method_definitions:
            restype = md.return_type.type.pytype
            argtypes = [pa.type.pytype for pa in md.parameters]
            argtypes_csv = ",".join(argtypes)
            inout = 1
            paramflags = [(inout, pa.name) for pa in md.parameters]
            if paramflags:
                paramflags_csv = ",".join(f"({inout}, '{name}')" for inout, name in paramflags) + ","
            else:
                paramflags_csv = ""
            vtbl_index = md["_vtbl_index"]
            writer.write(f"    {td.name}.{md.name} = COMMETHOD(WINFUNCTYPE({restype},{argtypes_csv})({vtbl_index}, '{md.name}', ({paramflags_csv})))\n")
        # ensure base is defined
        if base != "c_void_p":
            writer.write(f"    {base}\n")
        writer.write(f"    return {td.name}\n")

    def write_header(self, writer, import_namespaces: set[str]) -> None:
        writer.write( "from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll\n")
        writer.write(f"from {PACKAGE_NAME}.base import {BASE_EXPORTS_CSV}\n")
        for namespace in sorted(import_namespaces):
            writer.write(f"import {namespace}\n")
        writer.write( "import sys\n")
        writer.write( "_module = sys.modules[__name__]\n")
        writer.write( "def __getattr__(name):\n")
        writer.write( "    try:\n")
        writer.write( "        f = globals()[f'_define_{name}']\n")
        writer.write( "    except KeyError:\n")
        writer.write( "        raise AttributeError(f\"module '{__name__}' has no attribute '{name}'\") from None\n")
        writer.write( "    setattr(_module, name, f())\n")
        writer.write( "    return getattr(_module, name)\n")
        writer.write( "def __dir__():\n")
        writer.write( "    return __all__\n")

    def write_footer(self, writer, export_names: set[str]) -> None:
        writer.write("__all__ = [\n")
        for name in sorted(export_names):
            writer.write(f'    "{name}",\n')
        writer.write("]\n")

    def write_all(self, writer, export_names_groupby_namespace: dict[str, set[str]]) -> None:
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
    ns: dict[str, TypeDefinition] = dict()
    with open(sys.argv[1]) as f:
        typedefs = [TypeDefinition(ns, typedef) for typedef in json.load(f)]
    pp = Preprocessor()
    typedefs = pp.filter_public(typedefs)
    typedefs = pp.filter_architecture(typedefs, ARCHITECTURE)
    for td in typedefs:
        ns[td.fullname] = td
    pp.patch_struct_nested_type(ns)
    pp.patch_enum(ns)
    pp.patch_com_vtbl_index(ns)
    pp.patch_name_conflict(ns)
    pp.patch_namespace(ns, PACKAGE_NAME)
    ns_mod: dict[str, dict[str, TypeDefinition]] = {}
    for td in typedefs:
        if td.namespace not in ns_mod:
            ns_mod[td.namespace] = {}
        ns_mod[td.namespace][td.name] = td
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
        for td in ns_mod[namespace].values():
            pp.collect_import_namespace(td, import_namespaces)
            pp.collect_export_name(td, export_names)
        with (p / "__init__.py").open("w") as writer:
            pg.write_header(writer, import_namespaces)
            for td in ns_mod[namespace].values():
                pg.emit(writer, td)
            pg.write_footer(writer, export_names)
        export_names_groupby_namespace[namespace] = export_names
    with open(f"{PACKAGE_NAME}/all.py", "w") as writer:
        pg.write_all(writer, export_names_groupby_namespace)

if __name__ == "__main__":
    main()

