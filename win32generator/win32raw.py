from __future__ import annotations

import logging
import re
import textwrap
from collections.abc import Iterable
from io import StringIO
from typing import no_type_check

from .metadata import FieldDefinition, MethodDefinition, TType, TypeDefinition
from .package import ApiItem

logger = logging.getLogger(__name__)


class Parser:
    def __init__(self, module: Win32RawModule) -> None:
        self._module = module
        self._formatter = Formatter()

    def parse(self, td: TypeDefinition) -> None:
        if td.basetype is None:
            self._module.add(Com(td, self._module, self._formatter))
        elif td.basetype == "System.Object":
            for fd in td.fields:
                self._module.add(Constant(td, fd, self._formatter))
            for md in td.method_definitions:
                if md.custom_attributes.has_constant():
                    self._module.add(InlineFunction(td, md, self._formatter))
                else:
                    self._module.add(ExternalFunction(td, md, self._formatter))
        elif td.basetype == "System.MulticastDelegate":
            self._module.add(FunctionPointer(td, self._formatter))
        elif td.basetype == "System.Enum":
            self._module.add(Enum(td, self._formatter))
        elif td.basetype == "System.ValueType":
            if td.custom_attributes.has_native_typedef():
                self._module.add(NativeTypedef(td, self._formatter))
            elif td.custom_attributes.has_guid() and not td.fields:
                self._module.add(Clsid(td, self._formatter))
            elif "SequentialLayout" in td.attributes:
                self._module.add(StructUnion(td, self._formatter))  # struct
            elif "ExplicitLayout" in td.attributes:
                self._module.add(StructUnion(td, self._formatter))  # union
            else:
                raise NotImplementedError()
        elif td.basetype == "System.Attribute":
            self._module.add(Attribute(td, self._formatter))
        else:
            raise NotImplementedError()


class Formatter:
    def __init__(self) -> None:
        self._primitives = {
            "Byte": "c_ubyte",
            "SByte": "c_byte",
            "Char": "c_wchar",
            "Int16": "c_int16",
            "UInt16": "c_uint16",
            "Int32": "c_int32",
            "UInt32": "c_uint32",
            "Int64": "c_int64",
            "UInt64": "c_uint64",
            "IntPtr": "c_ssize_t",
            "UIntPtr": "c_size_t",
            "Single": "c_float",
            "Double": "c_double",
            "Bytes": "c_char_p",
            "String": "c_wchar_p",
            "Boolean": "c_bool",
            "Void": "None",
        }

    def pytype(self, ttype: TType) -> str:
        if ttype.kind == "Primitive":
            return self._primitives[ttype.name]
        elif ttype.kind == "Pointer":
            if ttype.type.kind == "Primitive" and ttype.type.name == "Void":
                return "c_void_p"
            else:
                return f"POINTER({self.pytype(ttype.type)})"
        elif ttype.kind == "Array":
            return f"{self.pytype(ttype.type)} * {ttype.size}"
        elif ttype.kind == "Type":
            if ttype.is_nested:
                return ttype.name
            elif ttype.is_guid:
                return "Guid"
            elif not ttype.namespace.startswith("Windows.Win32."):
                # Some win32 api depends on winrt namespace.  Ignore it.
                return "c_void_p"
            return ttype.name
        else:
            raise NotImplementedError()

    def pyvalue(self, fd: FieldDefinition) -> str:
        if "HasDefault" in fd.attributes:
            return ascii(fd.default_value.value)
        elif fd.signature.kind == "Type" and fd.signature.fullname == "System.Guid":
            return self.guid(fd.custom_attributes.get_guid())
        elif fd.signature.kind == "Type" and fd.signature.fullname == "Windows.Win32.Devices.Properties.DEVPROPKEY":
            guid, pid = fd.custom_attributes.get_property_key()
            return f"DEVPROPKEY({self.guid(guid)}, {pid})"
        elif (
            fd.signature.kind == "Type"
            and fd.signature.fullname == "Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY"
        ):
            guid, pid = fd.custom_attributes.get_property_key()
            return f"PROPERTYKEY({self.guid(guid)}, {pid})"
        elif fd.signature.kind == "Type" and fd.signature.fullname == "Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY":
            value = fd.custom_attributes.get_constant()
            return f"SID_IDENTIFIER_AUTHORITY({value})"
        elif (
            fd.signature.kind == "Type" and fd.signature.fullname == "Windows.Win32.System.Threading.CONDITION_VARIABLE"
        ):
            value = fd.custom_attributes.get_constant()
            return f"CONDITION_VARIABLE({value})"
        elif fd.signature.kind == "Type" and fd.signature.fullname == "Windows.Win32.System.Threading.SRWLOCK":
            value = fd.custom_attributes.get_constant()
            return f"SRWLOCK({value})"
        elif fd.signature.kind == "Type" and fd.signature.fullname == "Windows.Win32.System.Threading.INIT_ONCE":
            value = fd.custom_attributes.get_constant()
            return f"INIT_ONCE({value})"
        else:
            # FIXME:
            raise NotImplementedError()

    def guid(self, guid_str: str) -> str:
        s = guid_str.replace("{", "").replace("}", "").replace("-", "")
        return f"Guid(0x{s[0:8]}, 0x{s[8:12]}, 0x{s[12:16]}, (0x{s[16:18]}, 0x{s[18:20]}, 0x{s[20:22]}, 0x{s[22:24]}, 0x{s[24:26]}, 0x{s[26:28]}, 0x{s[28:30]}, 0x{s[30:32]}))"


class Win32RawModule:
    def __init__(self) -> None:
        self._items: dict[str, ApiItem] = {}

    def __getitem__(self, name: str) -> ApiItem:
        return self._items[name]

    def __contains__(self, name: str) -> bool:
        return name in self._items

    def items(self) -> Iterable[ApiItem]:
        return self._items.values()

    def add(self, item: ApiItem) -> None:
        if item.name in self._items:
            assert item.supported_architecture
            archtecture_variant = self._items[item.name]
            if not isinstance(archtecture_variant, ArchitectureVariant):
                raise TypeError()
            archtecture_variant.add(item)
        elif item.supported_architecture:
            self._items[item.name] = ArchitectureVariant(item)
        else:
            self._items[item.name] = item

    def emit_header(self) -> str:
        writer = StringIO()
        writer.write(
            "from ctypes import CFUNCTYPE, WINFUNCTYPE, POINTER, Structure, Union, c_ubyte, c_byte, c_wchar, c_int16, c_uint16, c_int32, c_uint32, c_int64, c_uint64, c_ssize_t, c_size_t, c_float, c_double, c_char_p, c_wchar_p, c_bool, c_void_p, cdll, windll\n"
        )
        writer.write("import types\n")
        writer.write("import sys\n")
        writer.write("if '(arm64)' in sys.version.lower():\n")
        writer.write("    ARCH = 'ARM64'\n")
        writer.write("elif '(amd64)' in sys.version.lower():\n")
        writer.write("    ARCH = 'X64'\n")
        writer.write("else:\n")
        writer.write("    ARCH = 'X86'\n")
        writer.write("class Guid(Structure):\n")
        writer.write(
            "    _fields_ = [('Data1', c_uint32), ('Data2', c_uint16), ('Data3', c_uint16), ('Data4', c_ubyte * 8)]\n"
        )
        writer.write("def define(cls):\n")
        writer.write("    def decorator(clsdef):\n")
        writer.write("        for key, attr in clsdef.__dict__.items():\n")
        writer.write("            if key not in cls.__dict__:\n")
        writer.write("                setattr(cls, key, attr)\n")
        writer.write("        return cls\n")
        writer.write("    return decorator\n")
        writer.write("class COMMETHOD:\n")
        writer.write("    def __init__(self, vtbl_index, name, *types):\n")
        writer.write("        self._proc = WINFUNCTYPE(*types)(vtbl_index, name)\n")
        writer.write("    def __get__(self, instance, owner=None):\n")
        writer.write("        if instance is None:\n")
        writer.write("            return self._proc\n")
        writer.write("        return types.MethodType(self._proc, instance)\n")
        return writer.getvalue()

    def emit(self) -> str:
        writer = StringIO()
        writer.write(self.emit_header())
        items = list(self._sort())
        for item in items:
            if isinstance(item, (StructUnion, Com, ArchitectureVariant)):
                writer.write(item.emit_head())
        for item in items:
            writer.write(item.emit())
        return writer.getvalue()

    def _sort(self) -> Iterable[ApiItem]:
        return self._sort_by_type(self._topological_sort(self._items.values()))

    def _topological_sort(self, items: Iterable[ApiItem]) -> Iterable[ApiItem]:
        ns = {item.name: item for item in items}
        visited: set[str] = set()
        for item in ns.values():
            yield from self._topological_sort_visit(item, visited, ns)

    def _topological_sort_visit(self, item: ApiItem, visited: set[str], ns: dict[str, ApiItem]) -> Iterable[ApiItem]:
        if item.name in visited:
            return
        visited.add(item.name)
        for name in self._topological_sort_dependencies(item):
            yield from self._topological_sort_visit(ns[name], visited, ns)
        yield item

    def _topological_sort_dependencies(self, item: ApiItem) -> Iterable[str]:
        if isinstance(item, Com):
            name = item._extends()
            if name == "c_void_p":
                return []
            else:
                return [name]
        elif self._item_type(item) is StructUnion and isinstance(item, (StructUnion, ArchitectureVariant)):
            return [fullname.rsplit(".", 1)[1] for fullname in item.enumerate_dependencies_exclude_pointer()]
        else:
            return [fullname.rsplit(".", 1)[1] for fullname in item.enumerate_dependencies()]

    def _sort_by_type(self, items: Iterable[ApiItem]) -> Iterable[ApiItem]:
        return sorted(items, key=self._type_order)

    def _type_order(self, item: ApiItem) -> int:
        order = {
            NativeTypedef: 0,
            Enum: 1,
            FunctionPointer: 2,
            Attribute: 3,
            StructUnion: 4,
            Com: 5,
            Clsid: 6,
            ExternalFunction: 7,
            InlineFunction: 8,
            Constant: 9,
        }
        return order[self._item_type(item)]

    def _item_type(self, item) -> type:
        if isinstance(item, ArchitectureVariant):
            return type(item._items[0])
        return type(item)


class Constant:
    def __init__(self, td: TypeDefinition, fd: FieldDefinition, formatter: Formatter) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._fd = fd
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._fd.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._fd.enumerate_dependencies()

    def emit(self) -> str:
        return f"{self._fd.name} = {self._formatter.pyvalue(self._fd)}\n"


class InlineFunction:
    def __init__(self, td: TypeDefinition, md: MethodDefinition, formatter: Formatter) -> None:
        assert not md.parameters_with_type
        self._td = td
        self._md = md
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._md.name

    @property
    def supported_architecture(self) -> list[str]:
        if self._md.custom_attributes.has_supported_architecture():
            return self._md.custom_attributes.get_supported_architecture()
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._md.enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(self._md.signature.return_type)
        value = self._md.custom_attributes.get_constant()
        writer.write(f"def {self._md.name}() -> {restype}:\n")
        writer.write(f"    return {restype}({value})\n")
        return writer.getvalue()


class ExternalFunction:
    def __init__(self, td: TypeDefinition, md: MethodDefinition, formatter: Formatter) -> None:
        self._td = td
        self._md = md
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._md.name

    @property
    def supported_architecture(self) -> list[str]:
        if self._md.custom_attributes.has_supported_architecture():
            return self._md.custom_attributes.get_supported_architecture()
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._md.enumerate_dependencies()

    def emit(self) -> str:
        name = self._md.name
        entry_point = self._entry_point()
        dll = self._dlltype()
        library = self._md.import_.module.name
        functype = self._functype()
        restype = self._md.signature.return_type
        paramtypes = self._md.signature.parameter_types
        types = ", ".join(self._formatter.pytype(t) for t in [restype] + paramtypes)
        return f"{name} = {functype}({types})(({entry_point}, {dll}['{library}']))\n"

    def _functype(self) -> str:
        if "CallingConventionWinApi" in self._md.import_.attributes:
            return "WINFUNCTYPE"
        elif "CallingConventionCDecl" in self._md.import_.attributes:
            return "CFUNCTYPE"
        else:
            raise NotImplementedError()

    def _dlltype(self) -> str:
        if "CallingConventionWinApi" in self._md.import_.attributes:
            return "windll"
        elif "CallingConventionCDecl" in self._md.import_.attributes:
            return "cdll"
        else:
            raise NotImplementedError()

    def _entry_point(self) -> str:
        if self._md.import_.name.startswith("#"):
            # ordinal number  (e.g. #123)
            return self._md.import_.name[1:]
        else:
            return f"'{self._md.import_.name}'"


class FunctionPointer:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        self._td = td
        self._md = td.method_definitions[1]  # [0]=.ctor, [1]=Invoke
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        if self._td.custom_attributes.has_supported_architecture():
            return self._td.custom_attributes.get_supported_architecture()
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._md.enumerate_dependencies()

    def emit(self) -> str:
        functype = self._functype()
        restype = self._md.signature.return_type
        paramtypes = self._md.signature.parameter_types
        types = ", ".join(self._formatter.pytype(t) for t in [restype] + paramtypes)
        return f"{self._td.name} = {functype}({types})\n"

    def _functype(self) -> str:
        calling_convention = self._td.custom_attributes.get_unmanaged_function_pointer()
        if calling_convention == "Winapi":
            return "WINFUNCTYPE"
        elif calling_convention == "Cdecl":
            return "CFUNCTYPE"
        else:
            raise NotImplementedError()


class Enum:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._td.fields[0].enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        type_field, *value_fields = self._td.fields
        writer.write(f"class {self._td.name}({self._formatter.pytype(type_field.signature)}):\n")
        if self._td.custom_attributes.has_scoped_enum():
            for fd in value_fields:
                writer.write(f"    {fd.name} = {fd.default_value.value}\n")
        else:
            writer.write("    pass\n")
            for fd in value_fields:
                writer.write(f"{fd.name}: {self._td.name} = {fd.default_value.value}\n")
        return writer.getvalue()


class NativeTypedef:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._td.fields[0].enumerate_dependencies()

    def emit(self) -> str:
        if self._td.name == "PSTR":  # POINTER(Byte)
            pytype = "c_char_p"
        elif self._td.name in ["PWSTR", "BSTR"]:  # POINTER(Char)
            pytype = "c_wchar_p"
        else:
            pytype = self._formatter.pytype(self._td.fields[0].signature)
            assert pytype not in ["POINTER(Byte)", "POINTER(Char)"]
        return f"{self._td.name} = {pytype}\n"


class Clsid:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        return []

    def emit(self) -> str:
        guid = self._formatter.guid(self._td.custom_attributes.get_guid())
        return f"{self._td.name} = {guid}\n"


class StructUnion:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert td.fields or not td.custom_attributes.has_guid()
        self._td = td
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        if self._td.custom_attributes.has_supported_architecture():
            return self._td.custom_attributes.get_supported_architecture()
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._td.enumerate_dependencies()

    def enumerate_dependencies_exclude_pointer(self) -> Iterable[str]:
        yield from self._td.enumerate_dependencies(exclude_pointer=True)

    def emit_head(self) -> str:
        return self._emit_head_td(self._td)

    def _emit_head_td(self, td: TypeDefinition) -> str:
        writer = StringIO()
        writer.write(f"class {td.name}({self._basetype(td)}):\n")
        writer.write("    pass\n")
        return writer.getvalue()

    def emit(self) -> str:
        return self._emit_td(self._td)

    def _emit_td(self, td: TypeDefinition) -> str:
        writer = StringIO()

        if td is self._td:
            writer.write(f"@define({td.name})\n")
        writer.write(f"class {td.name}({self._basetype(td)}):\n")

        for nested_type in td.nested_types:
            writer.write(textwrap.indent(self._emit_td(nested_type), "    "))

        if td.custom_attributes.has_guid():
            guid = self._formatter.guid(td.custom_attributes.get_guid())
            writer.write(f"    _uuid_ = {guid}\n")

        for fd in td.fields:
            if self._is_static(fd):
                writer.write(f"    {fd.name} = {self._formatter.pyvalue(fd)}\n")

        anonymous = ", ".join(f"'{fd.name}'" for fd in td.fields if re.match(r"^Anonymous\d*$", fd.name))
        if anonymous:
            writer.write(f"    _anonymous_ = [{anonymous}]\n")

        if td.layout.packing_size != 0:
            writer.write(f"    _pack_ = {td.layout.packing_size}\n")

        writer.write("    _fields_ = [\n")
        for fd in td.fields:
            if not self._is_static(fd):
                writer.write(f"        ('{fd.name}', {self._formatter.pytype(fd.signature)}),\n")
        writer.write("    ]\n")

        return writer.getvalue()

    def _basetype(self, td) -> str:
        if "SequentialLayout" in td.attributes:
            return "Structure"
        elif "ExplicitLayout" in td.attributes:
            return "Union"
        else:
            raise ValueError()

    def _is_static(self, fd: FieldDefinition) -> bool:
        return {"Static", "HasDefault"} <= set(fd.attributes)


class Com:
    def __init__(self, td: TypeDefinition, module: Win32RawModule, formatter: Formatter) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._module = module
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._td.enumerate_dependencies()

    def emit_head(self) -> str:
        writer = StringIO()
        writer.write(f"class {self._td.name}({self._extends()}):\n")
        writer.write("    pass\n")
        return writer.getvalue()

    def emit(self) -> str:
        assert len(self._td.interface_implementations) <= 1
        writer = StringIO()
        writer.write(f"@define({self._td.name})\n")
        writer.write(f"class {self._td.name}({self._extends()}):\n")
        if not self._td.custom_attributes.has_guid() and not self._td.method_definitions:
            writer.write("    pass\n")
            return writer.getvalue()
        if self._td.custom_attributes.has_guid():
            guid = self._formatter.guid(self._td.custom_attributes.get_guid())
            writer.write(f"    _iid_ = {guid}\n")
        vtbl_index = self._count_interface_method()
        for md in self._td.method_definitions:
            writer.write(self._method(md, vtbl_index))
            vtbl_index += 1
        return writer.getvalue()

    def _extends(self) -> str:
        if not self._td.interface_implementations:
            return "c_void_p"
        return self._td.interface_implementations[0].name

    def _count_interface_method(self) -> int:
        return sum(len(com._td.method_definitions) for com in self._enumerate_interfaces())

    def _enumerate_interfaces(self) -> Iterable[Com]:
        for ii in self._td.interface_implementations:
            com = self._module[ii.name]
            if not isinstance(com, Com):
                raise TypeError()
            yield com
            yield from com._enumerate_interfaces()

    def _method(self, md: MethodDefinition, vtbl_index: int) -> str:
        restype = md.signature.return_type
        paramtypes = md.signature.parameter_types
        types = ", ".join(self._formatter.pytype(t) for t in [restype] + paramtypes)
        return f"    {md.name} = COMMETHOD({vtbl_index}, '{md.name}', {types})\n"


class Attribute:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._formatter = formatter

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[str]:
        return []

    def emit(self) -> str:
        writer = StringIO()
        md = self._td.method_definitions[0]  # [0]=.ctor
        writer.write(f"class {self._td.name}(Structure):\n")
        writer.write("    _fields_ = [\n")
        for pa, type_ in md.parameters_with_type:
            writer.write(f"        ('{pa.name}', {self._formatter.pytype(type_)}),\n")
        writer.write("    ]\n")
        return writer.getvalue()


class ArchitectureVariant:
    def __init__(self, item: ApiItem) -> None:
        self._items = [item]
        self._namespace = item.namespace
        self._name = item.name

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def name(self) -> str:
        return self._name

    @property
    def supported_architecture(self) -> list[str]:
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        for item in self._items:
            yield from item.enumerate_dependencies()

    @no_type_check
    def enumerate_dependencies_exclude_pointer(self) -> Iterable[str]:
        for item in self._items:
            yield from item.enumerate_dependencies_exclude_pointer()

    def emit_head(self) -> str:
        if not isinstance(self._items[0], (StructUnion, Com)):
            return ""
        writer = StringIO()
        for i, item in self._emit_head_no_type_check_enumerate():
            if i == 0:
                ifelif = "if"
            else:
                ifelif = "elif"
            arch = ",".join(item.supported_architecture).upper()
            writer.write(f"{ifelif} ARCH in '{arch}':\n")
            writer.write(textwrap.indent(item.emit_head(), "    "))
        return writer.getvalue()

    @no_type_check
    def _emit_head_no_type_check_enumerate(self):
        return enumerate(item for item in self._items if item.emit_head() != "")

    def emit(self) -> str:
        writer = StringIO()
        for i, item in enumerate(self._items):
            if i == 0:
                ifelif = "if"
            else:
                ifelif = "elif"
            arch = ",".join(item.supported_architecture).upper()
            writer.write(f"{ifelif} ARCH in '{arch}':\n")
            writer.write(textwrap.indent(item.emit(), "    "))
        return writer.getvalue()

    def add(self, item: ApiItem) -> None:
        assert self.namespace == item.namespace
        assert self.name == item.name
        assert item.supported_architecture
        self._items.append(item)
