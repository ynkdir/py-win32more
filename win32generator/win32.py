from __future__ import annotations

import functools
import logging
import textwrap
from collections.abc import Iterable
from io import StringIO

from .metadata import FieldDefinition, InterfaceImplementation, MethodDefinition, TType, TypeDefinition
from .package import ApiItem, Module, Package

logger = logging.getLogger(__name__)

BASE_EXPORTS = [
    "ARCH",
    "Boolean",
    "Byte",
    "Bytes",
    "Char",
    "ComPtr",
    "ConstantLazyLoader",
    "Double",
    "EasyCastStructure",
    "EasyCastUnion",
    "FAILED",
    "Guid",
    "Int16",
    "Int32",
    "Int64",
    "IntPtr",
    "POINTER",
    "SByte",
    "SUCCEEDED",
    "Single",
    "String",
    "UInt16",
    "UInt32",
    "UInt64",
    "UIntPtr",
    "Void",
    "VoidPtr",
    "cfunctype",
    "cfunctype_pointer",
    "commethod",
    "make_ready",
    "winfunctype",
    "winfunctype_pointer",
]
BASE_EXPORTS_CSV = ", ".join(BASE_EXPORTS)


class Parser:
    def __init__(self, package: Package) -> None:
        self._package = package
        self._formatter = Formatter(self._package)

    def parse(self, td: TypeDefinition) -> None:
        if td.namespace not in self._package:
            self._package[td.namespace] = Win32Module(td.namespace, self._package)

        module = self._package[td.namespace]

        if td.basetype is None:
            module.add(Com(td, self._package, self._formatter))
        elif td.basetype == "System.Object":
            for fd in td.fields:
                module.add(Constant(td, fd, self._formatter))
            for md in td.method_definitions:
                if md.custom_attributes.has_constant():
                    module.add(InlineFunction(td, md, self._formatter))
                else:
                    module.add(ExternalFunction(td, md, self._formatter))
        elif td.basetype == "System.MulticastDelegate":
            module.add(FunctionPointer(td, self._formatter))
        elif td.basetype == "System.Enum":
            module.add(Enum(td, self._formatter))
        elif td.basetype == "System.ValueType":
            if td.custom_attributes.has_native_typedef():
                module.add(NativeTypedef(td, self._formatter))
            # FIXME: CLSID_ComClass is defined as attribute like [uuid(...)] struct ComClass {}.
            elif td.custom_attributes.has_guid() and not td.fields:
                module.add(Clsid(td, self._formatter))
            elif "SequentialLayout" in td.attributes:
                module.add(StructUnion(td, self._formatter))  # struct
            elif "ExplicitLayout" in td.attributes:
                module.add(StructUnion(td, self._formatter))  # union
            else:
                raise NotImplementedError()
        elif td.basetype == "System.Attribute":
            module.add(Attribute(td, self._formatter))
        else:
            raise NotImplementedError()


class Formatter:
    def __init__(self, package: Package) -> None:
        self._package = package

    def pytype(self, ttype: TType) -> str:
        if ttype.kind == "Primitive":
            return ttype.name
        elif ttype.kind == "Pointer":
            if ttype.type.kind == "Primitive" and ttype.type.name == "Void":
                return "VoidPtr"
            else:
                return f"POINTER({self.pytype(ttype.type)})"
        elif ttype.kind == "Array":
            return f"{self.pytype(ttype.type)} * {ttype.size}"
        elif ttype.kind == "Type":
            if ttype.is_nested:
                return ttype.name
            elif ttype.is_guid:
                return "Guid"
            else:
                return self.fullname(ttype)
        else:
            raise NotImplementedError()

    def method_parameters_annotated(self, md: MethodDefinition) -> list[str]:
        return [f"{pa.name}: {self.pytype(type_)}" for pa, type_ in md.parameters_with_type]

    def pyvalue(self, fd: FieldDefinition) -> str:
        if "HasDefault" in fd.attributes:
            return ascii(fd.default_value.value)
        elif fd.signature.kind == "Type" and fd.signature.fullname == "System.Guid":
            guid = fd.custom_attributes.get_guid()
            return f"Guid('{guid}')"
        elif fd.signature.kind == "Type" and fd.signature.fullname == "Windows.Win32.Devices.Properties.DEVPROPKEY":
            guid, pid = fd.custom_attributes.get_property_key()
            return f"ConstantLazyLoader(fmtid=Guid('{guid}'), pid={pid})"
        elif (
            fd.signature.kind == "Type"
            and fd.signature.fullname == "Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY"
        ):
            guid, pid = fd.custom_attributes.get_property_key()
            return f"ConstantLazyLoader(fmtid=Guid('{guid}'), pid={pid})"
        elif fd.signature.kind == "Type" and fd.signature.fullname == "Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY":
            value = fd.custom_attributes.get_constant()
            return f"ConstantLazyLoader({value})"
        else:
            # FIXME:
            raise NotImplementedError()

    @functools.singledispatchmethod
    def fullname(self, name: str) -> str:
        return self._package.abs_pkg(name)

    @fullname.register
    def _(self, ttype: TType) -> str:
        return self.fullname(ttype.fullname)

    @fullname.register
    def _(self, td: TypeDefinition) -> str:
        return self.fullname(td.fullname)

    @fullname.register
    def _(self, ii: InterfaceImplementation) -> str:
        return self.fullname(ii.fullname)


class Win32Module(Module):
    def __init__(self, namespace: str, package: Package) -> None:
        self._namespace = namespace
        self._package = package
        self._items: dict[str, ApiItem] = {}

    @property
    def namespace(self) -> str:
        return self._namespace

    def __getitem__(self, name: str) -> ApiItem:
        return self._items[name]

    def __contains__(self, name: str) -> bool:
        return name in self._items

    def items(self) -> Iterable[ApiItem]:
        return self._items.values()

    def add(self, item: ApiItem) -> None:
        assert self.namespace == item.namespace
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
        writer.write("from __future__ import annotations\n")
        writer.write(f"from {self._package.name} import {BASE_EXPORTS_CSV}\n")
        for namespace in sorted(self.imported_namespaces() | {self.namespace}):
            if not namespace.startswith("Windows.Win32."):
                # FIXME: _winrt.py doesn't support circular import
                continue
            writer.write(f"import {self._package.name}.{namespace}\n")
        return writer.getvalue()

    def enumerate_dependencies(self) -> Iterable[str]:
        for item in self._items.values():
            yield from item.enumerate_dependencies()

    def imported_namespaces(self) -> set[str]:
        return {fullname.rsplit(".", 1)[0] for fullname in self.enumerate_dependencies()}

    @classmethod
    def emit_header_one(cls, package_name: str) -> str:
        writer = StringIO()
        writer.write("from __future__ import annotations\n")
        writer.write(f"from {package_name} import {BASE_EXPORTS_CSV}\n")
        return writer.getvalue()


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
        writer = StringIO()
        if "HasDefault" in self._fd.attributes:
            # primitive
            writer.write(
                f"{self._fd.name}: {self._formatter.pytype(self._fd.signature)} = {self._formatter.pyvalue(self._fd)}\n"
            )
        elif self._fd.signature.is_guid:
            writer.write(f"{self._fd.name}: Guid = {self._formatter.pyvalue(self._fd)}\n")
        else:
            # composite type
            writer.write(
                f"{self._fd.name}: {self._formatter.pytype(self._fd.signature)} = {self._formatter.pyvalue(self._fd)}\n"
            )
        return writer.getvalue()


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
        # FIXME: Should result be python primitive?  (e.g. -4 insted of HANDLE(-4))
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
        writer = StringIO()
        library = self._md.import_.module.name
        functype = self._functype()
        restype = self._formatter.pytype(self._md.signature.return_type)
        params = self._formatter.method_parameters_annotated(self._md)
        attrs = [f"'{library}'"]
        if self._md.name != self._md.import_.name:
            entry_point = self._entry_point()
            attrs.append(f"entry_point={entry_point}")
        if self._md.signature.header.calling_convention == "VarArgs":
            assert functype == "cfunctype"
            attrs.append("variadic=True")
            params.append("*__arglist")
        params_csv = ", ".join(params)
        attrs_csv = ", ".join(attrs)
        writer.write(f"@{functype}({attrs_csv})\n")
        writer.write(f"def {self._md.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def _functype(self) -> str:
        if "CallingConventionWinApi" in self._md.import_.attributes:
            return "winfunctype"
        elif "CallingConventionCDecl" in self._md.import_.attributes:
            return "cfunctype"
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
        writer = StringIO()
        functype = self._functype()
        restype = self._formatter.pytype(self._md.signature.return_type)
        params_csv = ", ".join(self._formatter.method_parameters_annotated(self._md))
        writer.write(f"@{functype}\n")
        writer.write(f"def {self._td.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def _functype(self) -> str:
        calling_convention = self._td.custom_attributes.get_unmanaged_function_pointer()
        if calling_convention == "Winapi":
            return "winfunctype_pointer"
        elif calling_convention == "Cdecl":
            return "cfunctype_pointer"
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
        if self._td.custom_attributes.has_scoped_enum():
            writer.write(f"class {self._td.name}({self._formatter.pytype(type_field.signature)}):  # enum\n")
            for fd in value_fields:
                writer.write(f"    {fd.name} = {fd.default_value.value}\n")
        else:
            writer.write(f"{self._td.name} = {self._formatter.pytype(type_field.signature)}\n")
            for fd in value_fields:
                writer.write(f"{fd.name}: {self._formatter.fullname(self._td)} = {fd.default_value.value}\n")
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
            pytype = "Bytes"
        elif self._td.name in ["PWSTR", "BSTR"]:  # POINTER(Char)
            pytype = "String"
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
        guid = self._td.custom_attributes.get_guid()
        return f"{self._td.name} = Guid('{guid}')\n"


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

    # _fields_ and _anonymous_ is defined at runtime.
    def emit(self) -> str:
        writer = StringIO()
        writer.write(f"class {self._td.name}({self._basetype()}):\n")
        if self._is_empty():
            writer.write("    pass\n")
            return writer.getvalue()
        if self._td.custom_attributes.has_guid():
            # FIXME: What id?
            guid = self._td.custom_attributes.get_guid()
            writer.write(f"    _uuid_ = Guid('{guid}')\n")
        for fd in self._static_fields():
            writer.write(f"    {fd.name} = {self._formatter.pyvalue(fd)}\n")
        for fd in self._member_fields():
            writer.write(f"    {fd.name}: {self._formatter.pytype(fd.signature)}\n")
        if self._td.layout.packing_size != 0:
            writer.write(f"    _pack_ = {self._td.layout.packing_size}\n")
        for nested_type in self._td.nested_types:
            writer.write(textwrap.indent(StructUnion(nested_type, self._formatter).emit(), "    "))
        return writer.getvalue()

    def _basetype(self) -> str:
        if "SequentialLayout" in self._td.attributes:
            return "EasyCastStructure"
        elif "ExplicitLayout" in self._td.attributes:
            return "EasyCastUnion"
        else:
            raise ValueError()

    def _static_fields(self) -> Iterable[FieldDefinition]:
        for fd in self._td.fields:
            if self._is_static(fd):
                yield fd

    def _member_fields(self) -> Iterable[FieldDefinition]:
        for fd in self._td.fields:
            if not self._is_static(fd):
                yield fd

    def _is_static(self, fd: FieldDefinition) -> bool:
        return {"Static", "HasDefault"} <= set(fd.attributes)

    def _is_empty(self) -> bool:
        return not self._td.fields


class Com:
    def __init__(self, td: TypeDefinition, package: Package, formatter: Formatter) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._package = package
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

    def emit(self) -> str:
        assert len(self._td.interface_implementations) <= 1
        writer = StringIO()
        writer.write(f"class {self._td.name}(ComPtr):\n")
        writer.write(f"    extends: {self._extends()}\n")
        if self._td.custom_attributes.has_guid():
            guid = self._td.custom_attributes.get_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        vtbl_index = self._count_interface_method()
        for md in self._td.method_definitions:
            writer.write(self._method(md, vtbl_index))
            vtbl_index += 1
        return writer.getvalue()

    def _extends(self) -> str:
        if not self._td.interface_implementations:
            # non IUnknown interface
            return "None"
        return self._formatter.fullname(self._td.interface_implementations[0])

    def _count_interface_method(self) -> int:
        return sum(len(com._td.method_definitions) for com in self._enumerate_interfaces())

    def _enumerate_interfaces(self) -> Iterable[Com]:
        for ii in self._td.interface_implementations:
            com = self._package[ii.namespace][ii.name]
            if not isinstance(com, Com):
                raise TypeError()
            yield com
            yield from com._enumerate_interfaces()

    def _method(self, md: MethodDefinition, vtbl_index: int) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(md.signature.return_type)
        params = ", ".join(["self"] + self._formatter.method_parameters_annotated(md))
        writer.write(f"    @commethod({vtbl_index})\n")
        writer.write(f"    def {md.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()


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
        params = self._formatter.method_parameters_annotated(md)
        writer.write(f"class {self._td.name}(EasyCastStructure):\n")
        if not params:
            writer.write("    pass\n")
        else:
            for param in params:
                writer.write(f"    {param}\n")
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
