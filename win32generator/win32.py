from __future__ import annotations

import logging
import textwrap
from collections.abc import Iterable
from io import StringIO

from .metadata import FieldDefinition, MethodDefinition, TType, TypeDefinition
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
    "MissingType",
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


def ttype_pytype(self: TType) -> str:
    if self.kind == "Primitive":
        return self.name
    elif self.kind == "Pointer":
        if self.type.kind == "Primitive" and self.type.name == "Void":
            return "VoidPtr"
        elif ttype_is_struct(self.type):
            return f"POINTER({Package.abs_pkg(self.type.fullname)})"
        else:
            return f"POINTER({ttype_pytype(self.type)})"
    elif self.kind == "Array":
        return f"{ttype_pytype(self.type)} * {self.size}"
    elif self.kind == "Type":
        if self.is_nested:
            return self.name
        elif self.is_guid:
            return "Guid"
        elif ttype_is_missing(self):
            logger.warning(f"missing type '{self.fullname}'")
            return "MissingType"
        elif ttype_is_com(self):
            return f"{Package.abs_pkg(self.fullname)}"
        else:
            return f"{Package.abs_pkg(self.fullname)}"
    else:
        raise NotImplementedError()


# missing type which is not defined in current winmd.
def ttype_is_missing(self: TType) -> bool:
    return self.kind == "Type" and not (
        self.namespace in Package.current and self.name in Package.current[self.namespace]
    )


def ttype_is_struct(self: TType) -> bool:
    if self.kind == "Type" and not self.is_nested and not self.is_guid and not ttype_is_missing(self):
        item = Package.current[self.namespace][self.name]
        return isinstance(item, StructUnion)
    return False


def ttype_is_com(self: TType) -> bool:
    if self.kind == "Type" and not self.is_nested and not self.is_guid and not ttype_is_missing(self):
        item = Package.current[self.namespace][self.name]
        return isinstance(item, Com)
    return False


def ttype_enumerate_dependencies(self: TType) -> Iterable[ApiItem]:
    if self.kind == "Type" and self.namespace not in ["", "System"]:
        try:
            item = Package.current[self.namespace][self.name]
        except KeyError:
            # missing type
            return
        yield item


def td_kind(self: TypeDefinition) -> str:
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


def md_parameter_names_annotated(self: MethodDefinition) -> list[str]:
    return [f"{pa.name}: {ttype_pytype(type_)}" for pa, type_ in self.parameters_with_type]


def fd_pyvalue(self: FieldDefinition) -> str:
    if "HasDefault" in self.attributes:
        return ascii(self.default_value.value)
    elif self.signature.kind == "Type" and self.signature.fullname == "System.Guid":
        guid = self.custom_attributes.get_guid()
        return f"Guid('{guid}')"
    elif self.signature.kind == "Type" and self.signature.fullname == "Windows.Win32.Devices.Properties.DEVPROPKEY":
        guid, pid = self.custom_attributes.get_property_key()
        return f"ConstantLazyLoader(fmtid=Guid('{guid}'), pid={pid})"
    elif (
        self.signature.kind == "Type"
        and self.signature.fullname == "Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY"
    ):
        guid, pid = self.custom_attributes.get_property_key()
        return f"ConstantLazyLoader(fmtid=Guid('{guid}'), pid={pid})"
    elif self.signature.kind == "Type" and self.signature.fullname == "Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY":
        value = self.custom_attributes.get_constant()
        return f"ConstantLazyLoader({value})"
    else:
        # FIXME:
        raise NotImplementedError()


class Parser:
    def __init__(self, package: Package) -> None:
        self._package = package

    def parse(self, td: TypeDefinition) -> None:
        if td.namespace not in self._package:
            self._package[td.namespace] = Win32Module(td.namespace)

        module = self._package[td.namespace]

        if td_kind(td) == "object":  # CONSTANT, FUNCTION
            for fd in td.fields:
                module.add(Constant(td, fd))
            for md in td.method_definitions:
                if md.custom_attributes.has_constant():
                    module.add(InlineFunction(td, md))
                else:
                    module.add(ExternalFunction(td, md))
        elif td_kind(td) == "function_pointer":
            module.add(FunctionPointer(td))
        elif td_kind(td) == "enum":
            module.add(Enum(td))
        elif td_kind(td) == "native_typedef":
            module.add(NativeTypedef(td))
        elif td_kind(td) == "clsid":
            module.add(Clsid(td))
        elif td_kind(td) == "union":
            module.add(StructUnion(td))
        elif td_kind(td) == "struct":
            module.add(StructUnion(td))
        elif td_kind(td) == "com":
            module.add(Com(td))
        elif td_kind(td) == "attribute":
            module.add(Attribute(td))
        else:
            raise NotImplementedError()


class Win32Module(Module):
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

    def emit_header(self, import_namespaces: set[str]) -> str:
        writer = StringIO()
        writer.write("from __future__ import annotations\n")
        writer.write(f"from {Package.name} import {BASE_EXPORTS_CSV}\n")
        if not Package.is_onefile:
            for namespace in sorted(import_namespaces):
                writer.write(f"import {Package.name}.{namespace}\n")
        return writer.getvalue()


class Constant:
    def __init__(self, td: TypeDefinition, fd: FieldDefinition) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td
        self._fd = fd

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._fd.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        yield from ttype_enumerate_dependencies(self._fd.signature)

    def emit(self) -> str:
        writer = StringIO()
        if "HasDefault" in self._fd.attributes:
            # primitive
            writer.write(f"{self._fd.name}: {ttype_pytype(self._fd.signature)} = {fd_pyvalue(self._fd)}\n")
        elif self._fd.signature.is_guid:
            writer.write(f"{self._fd.name}: Guid = {fd_pyvalue(self._fd)}\n")
        else:
            # composite type
            writer.write(f"{self._fd.name}: {ttype_pytype(self._fd.signature)} = {fd_pyvalue(self._fd)}\n")
        return writer.getvalue()


class InlineFunction:
    def __init__(self, td: TypeDefinition, md: MethodDefinition) -> None:
        assert not md.parameters_with_type
        self._td = td
        self._md = md

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

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        yield from ttype_enumerate_dependencies(self._md.signature.return_type.get_element_type())

    def emit(self) -> str:
        writer = StringIO()
        restype = ttype_pytype(self._md.signature.return_type)
        value = self._md.custom_attributes.get_constant()
        # FIXME: Should result be python primitive?  (e.g. -4 insted of HANDLE(-4))
        writer.write(f"def {self._md.name}() -> {restype}:\n")
        writer.write(f"    return {restype}({value})\n")
        return writer.getvalue()


class ExternalFunction:
    def __init__(self, td: TypeDefinition, md: MethodDefinition) -> None:
        self._td = td
        self._md = md

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

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        types = [self._md.signature.return_type] + self._md.signature.parameter_types
        for t in types:
            yield from ttype_enumerate_dependencies(t.get_element_type())

    def emit(self) -> str:
        writer = StringIO()
        library = self._md.import_.module.name
        functype = self._functype()
        restype = ttype_pytype(self._md.signature.return_type)
        params = md_parameter_names_annotated(self._md)
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
    def __init__(self, td: TypeDefinition) -> None:
        self._td = td
        self._md = td.method_definitions[1]  # [0]=.ctor, [1]=Invoke

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

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        types = [self._md.signature.return_type] + self._md.signature.parameter_types
        for t in types:
            yield from ttype_enumerate_dependencies(t.get_element_type())

    def emit(self) -> str:
        writer = StringIO()
        functype = self._functype()
        restype = ttype_pytype(self._md.signature.return_type)
        params_csv = ", ".join(md_parameter_names_annotated(self._md))
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
    def __init__(self, td: TypeDefinition) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        yield from ttype_enumerate_dependencies(self._td.fields[0].signature.get_element_type())

    def emit(self) -> str:
        writer = StringIO()
        type_field, *value_fields = self._td.fields
        writer.write(f"{self._td.name} = {ttype_pytype(type_field.signature)}\n")
        for fd in value_fields:
            writer.write(f"{fd.name}: {Package.abs_pkg(self._td.fullname)} = {fd.default_value.value}\n")
        return writer.getvalue()


class NativeTypedef:
    def __init__(self, td: TypeDefinition) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        yield from ttype_enumerate_dependencies(self._td.fields[0].signature.get_element_type())

    def emit(self) -> str:
        pytype = ttype_pytype(self._td.fields[0].signature)
        if pytype == "POINTER(Byte)":
            pytype = "Bytes"
        elif pytype == "POINTER(Char)":
            pytype = "String"
        return f"{self._td.name} = {pytype}\n"


class Clsid:
    def __init__(self, td: TypeDefinition) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        return []

    def emit(self) -> str:
        guid = self._td.custom_attributes.get_guid()
        return f"{self._td.name} = Guid('{guid}')\n"


class StructUnion:
    def __init__(self, td: TypeDefinition) -> None:
        self._td = td

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

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        yield from self._enumerate_dependencies_nested(self._td)

    def _enumerate_dependencies_nested(self, td: TypeDefinition) -> Iterable[ApiItem]:
        for fd in td.fields:
            yield from ttype_enumerate_dependencies(fd.signature.get_element_type())
        for nested_type in td.nested_types:
            yield from self._enumerate_dependencies_nested(nested_type)

    def emit(self) -> str:
        return self._emit_struct_union(self._td)

    # _fields_ and _anonymous_ is defined at runtime.
    def _emit_struct_union(self, td: TypeDefinition) -> str:
        writer = StringIO()
        base = self._base_type(td)
        writer.write(f"class {td.name}({base}):\n")
        if self._is_empty(td):
            writer.write("    pass\n")
            return writer.getvalue()
        if td.custom_attributes.has_guid():
            # FIXME: What id?
            guid = td.custom_attributes.get_guid()
            writer.write(f"    _uuid_ = Guid('{guid}')\n")
        for fd in self._static_fields(td):
            writer.write(f"    {fd.name} = {fd_pyvalue(fd)}\n")
        for fd in self._member_fields(td):
            writer.write(f"    {fd.name}: {ttype_pytype(fd.signature)}\n")
        if td.layout.packing_size != 0:
            writer.write(f"    _pack_ = {td.layout.packing_size}\n")
        for nested_type in td.nested_types:
            writer.write(textwrap.indent(self._emit_struct_union(nested_type), "    "))
        return writer.getvalue()

    def _base_type(self, td: TypeDefinition) -> str:
        if td_kind(td) == "struct":
            return "EasyCastStructure"
        elif td_kind(td) == "union":
            return "EasyCastUnion"
        else:
            raise NotImplementedError()

    def _static_fields(self, td: TypeDefinition) -> Iterable[FieldDefinition]:
        for fd in td.fields:
            if self._is_static(fd):
                yield fd

    def _member_fields(self, td: TypeDefinition) -> Iterable[FieldDefinition]:
        for fd in td.fields:
            if not self._is_static(fd):
                yield fd

    def _is_static(self, fd: FieldDefinition) -> bool:
        return {"Static", "HasDefault"} <= set(fd.attributes)

    def _is_empty(self, td: TypeDefinition) -> bool:
        if td.fields:
            return False
        assert not td.custom_attributes.has_guid()
        return True


class Com:
    def __init__(self, td: TypeDefinition) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        for ii in self._td.interface_implementations:
            item = Package.current[ii.namespace][ii.name]
            yield item
        for md in self._td.method_definitions:
            types = [md.signature.return_type] + md.signature.parameter_types
            for t in types:
                yield from ttype_enumerate_dependencies(t.get_element_type())

    def emit(self) -> str:
        assert len(self._td.interface_implementations) <= 1
        writer = StringIO()
        base = self._base_type()
        writer.write(f"class {self._td.name}(ComPtr):\n")
        writer.write(f"    extends: {base}\n")
        if self._td.custom_attributes.has_guid():
            guid = self._td.custom_attributes.get_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        vtbl_index = self._count_interface_method()
        for md in self._td.method_definitions:
            restype = ttype_pytype(md.signature.return_type)
            params = ["self"]
            params.extend(md_parameter_names_annotated(md))
            params_csv = ", ".join(params)
            writer.write(f"    @commethod({vtbl_index})\n")
            writer.write(f"    def {md.name}({params_csv}) -> {restype}: ...\n")
            vtbl_index += 1
        return writer.getvalue()

    def _base_type(self) -> str:
        if not self._td.interface_implementations:
            return "None"
        base = self._td.interface_implementations[0].interface.type_reference.fullname
        return Package.abs_pkg(base)

    def _count_interface_method(self) -> int:
        return sum(len(com._td.method_definitions) for com in self._enumerate_interfaces())

    def _enumerate_interfaces(self) -> Iterable[Com]:
        for ii in self._td.interface_implementations:
            com = Package.current[ii.namespace][ii.name]
            if not isinstance(com, Com):
                raise TypeError()
            yield com
            yield from com._enumerate_interfaces()


class Attribute:
    def __init__(self, td: TypeDefinition) -> None:
        assert not td.custom_attributes.has_supported_architecture()
        self._td = td

    @property
    def namespace(self) -> str:
        return self._td.namespace

    @property
    def name(self) -> str:
        return self._td.name

    @property
    def supported_architecture(self) -> list[str]:
        return []

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
        return []

    def emit(self) -> str:
        writer = StringIO()
        md = self._td.method_definitions[0]  # [0]=.ctor
        params = md_parameter_names_annotated(md)
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

    def enumerate_dependencies(self) -> Iterable[ApiItem]:
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
