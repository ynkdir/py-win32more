from __future__ import annotations

import functools
import logging
from collections import Counter
from collections.abc import Iterable
from io import StringIO
from typing import Protocol

from .backport import removeprefix
from .dependencies import Dependencies
from .metadata import InterfaceImplementation, MethodDefinition, TType, TypeDefinition
from .package import ApiItem, Module, Package
from .win32 import BASE_EXPORTS_CSV

logger = logging.getLogger(__name__)

WINRT_EXPORTS = [
    "AwaitableProtocol",
    "ContextManagerProtocol",
    "FillArray",
    "Generic",
    "IterableProtocol",
    "K",
    "MappingProtocol",
    "MulticastDelegate",
    "PassArray",
    "ReceiveArray",
    "SequenceProtocol",
    "T",
    "TProgress",
    "TResult",
    "TSender",
    "Tuple",
    "V",
    "WinRT_String",
    "event",
    "winrt_activatemethod",
    "winrt_classmethod",
    "winrt_commethod",
    "winrt_factorymethod",
    "winrt_mixinmethod",
    "winrt_overload",
]
WINRT_EXPORTS_CSV = ", ".join(WINRT_EXPORTS)


class Parser:
    def __init__(self, package: Package) -> None:
        self._package = package
        self._formatter = Formatter(self._package)

    def parse(self, td: TypeDefinition) -> None:
        if td.namespace not in self._package:
            self._package[td.namespace] = WinrtModule(td.namespace, self._package)

        module = self._package[td.namespace]

        if td.basetype is None or td.basetype == "System.Object" or td.basetype.startswith(("Windows.", "Microsoft.")):
            module.add(Com(td, self._package, self._formatter))
        elif td.basetype == "System.MulticastDelegate":
            module.add(Delegate(td, self._formatter))
        elif td.basetype == "System.Enum":
            module.add(Enum(td, self._formatter))
        elif td.basetype == "System.ValueType":
            if td.fields:
                module.add(Struct(td, self._formatter))
            elif td.custom_attributes.has("Windows.Foundation.Metadata.ContractVersionAttribute"):
                module.add(ContractVersion(td, self._formatter))
            else:
                raise NotImplementedError()
        else:
            raise NotImplementedError()


class Formatter:
    def __init__(self, package: Package) -> None:
        self._package = package

    def pytype(self, ttype: TType) -> str:
        if ttype.kind == "Primitive":
            if ttype.name == "Object":
                return self.fullname("Windows.Win32.System.WinRT.IInspectable")
            elif ttype.name == "String":
                return "WinRT_String"
            else:
                return ttype.name
        elif ttype.kind == "Reference":
            return f"POINTER({self.pytype(ttype.type)})"
        elif ttype.kind == "SZArray":
            # Handle return type.  Parameters are handled in method_parameters_annotated().
            return f"ReceiveArray[{self.pytype(ttype.type)}]"
        elif ttype.kind == "Type":
            if ttype.fullname == "System.Guid":
                return "Guid"
            else:
                return self.fullname(ttype)
        elif ttype.kind == "Generic":
            return self.generic_name_with_arguments(ttype)
        elif ttype.kind == "GenericParameter":
            return ttype.name
        elif ttype.kind == "Modified" and ttype.modifier_type.fullname == "System.Runtime.CompilerServices.IsConst":
            return self.pytype(ttype.unmodified_type)
        else:
            raise NotImplementedError()

    @functools.singledispatchmethod
    def generic_name_with_arguments(self, ttype: TType) -> str:
        arguments = self.generic_arguments(ttype)
        return f"{self.fullname(ttype.type)}[{arguments}]"

    @generic_name_with_arguments.register
    def _(self, ii: InterfaceImplementation) -> str:
        if ii.interface.kind == "TypeReference":
            return self.fullname(ii.interface.type_reference.fullname)
        elif ii.interface.kind == "TypeSpecification":
            if ii.interface.type_specification.signature.kind == "Generic":
                return self.generic_name_with_arguments(ii.interface.type_specification.signature)
            return self.fullname(ii.interface.type_specification.signature.type)
        else:
            raise NotImplementedError()

    def generic_arguments(self, ttype: TType) -> str:
        return ", ".join(self.pytype(ta) for ta in ttype.type_arguments)

    def generic_parameters(self, td: TypeDefinition) -> str:
        return ", ".join(gp.name for gp in td.generic_parameters)

    def generic_name_with_parameters(self, td: TypeDefinition) -> str:
        if td.is_generic:
            return f"{self.fullname(td)}[{self.generic_parameters(td)}]"
        return self.fullname(td)

    def method_parameters_annotated(self, md: MethodDefinition) -> list[str]:
        r = []
        for pa, type_ in md.parameters_with_type:
            if type_.kind == "SZArray" and "In" in pa.attributes:
                pytype = f"PassArray[{self.pytype(type_.type)}]"
            elif type_.kind == "SZArray" and "Out" in pa.attributes:
                pytype = f"FillArray[{self.pytype(type_.type)}]"
            elif type_.kind == "Reference" and type_.type.kind == "SZArray" and "Out" in pa.attributes:
                pytype = f"ReceiveArray[{self.pytype(type_.type.type)}]"
            else:
                pytype = self.pytype(type_)
            r.append(f"{pa.name}: {pytype}")
        return r

    @functools.singledispatchmethod
    def fullname(self, name: str) -> str:
        return self._package.abs_pkg(name)

    @fullname.register
    def _(self, ttype: TType) -> str:
        return self.fullname(ttype.generic_fullname)

    @fullname.register
    def _(self, td: TypeDefinition) -> str:
        return self.fullname(td.generic_fullname)

    @fullname.register
    def _(self, ii: InterfaceImplementation) -> str:
        return self.fullname(ii.fullname)


class WinrtModule(Module):
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
        assert item.name not in self._items
        self._items[item.name] = item

    def emit_header(self) -> str:
        writer = StringIO()
        writer.write("from __future__ import annotations\n")
        writer.write(f"from {self._package.name} import {BASE_EXPORTS_CSV}\n")
        writer.write(f"from {self._package.name}._winrt import {WINRT_EXPORTS_CSV}\n")
        for namespace in sorted(self.imported_namespaces() | {self.namespace}):
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
        writer.write(f"from {package_name}._winrt import {WINRT_EXPORTS_CSV}\n")
        return writer.getvalue()


class Enum:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from Dependencies(self._td.fields[0])

    def emit(self) -> str:
        writer = StringIO()
        type_field, *value_fields = self._td.fields
        writer.write(f"class {self._td.name}(Enum, {self._formatter.pytype(type_field.signature)}):\n")
        for fd in value_fields:
            writer.write(f"    {fd.name} = {fd.default_value.value}\n")
        return writer.getvalue()


class Struct:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert td.fields
        assert not td.nested_types
        assert "SequentialLayout" in td.attributes
        assert not td.custom_attributes.has_winrt_guid()
        assert not any(fd for fd in td.fields if {"Static", "HasDefault"} <= set(fd.attributes))
        assert td.layout.packing_size == 0
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from Dependencies(self._td)

    # _fields_ and _anonymous_ is defined at runtime.
    def emit(self) -> str:
        writer = StringIO()
        writer.write(f"class {self._td.name}(Structure):\n")
        for fd in self._td.fields:
            writer.write(f"    {fd.name}: {self._formatter.pytype(fd.signature)}\n")
        return writer.getvalue()


class ContractVersion:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        return []

    def emit(self) -> str:
        contract_version = self._td.custom_attributes.get_contract_version()
        return f"{self._td.name}: {contract_version.type.name} = {contract_version.value}\n"


class Com:
    def __init__(self, td: TypeDefinition, package: Package, formatter: Formatter) -> None:
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from Dependencies(self._td)

    def emit(self) -> str:
        writer = StringIO()
        if self._has_classproperty():
            writer.write(f"class {self._metaclass_name()}(ComPtr.__class__):\n")
            writer.write("    pass\n")
        writer.write(f"class {self._td.generic_name}({self._basetype()}):\n")
        writer.write(f"    extends: {self._extends()}\n")
        writer.write(self._implements())
        if self._has_default_interface():
            writer.write(f"    default_interface: {self._default_interface()}\n")
        writer.write(f"    _classid_ = '{self._td.generic_fullname}'\n")
        if self._td.custom_attributes.has_winrt_guid():
            guid = self._td.custom_attributes.get_winrt_guid()
            if self._td.is_generic:
                writer.write(f"    _piid_ = Guid('{guid}')\n")
            else:
                writer.write(f"    _iid_ = Guid('{guid}')\n")
        writer.write(self._constructor())
        writer.write(self._methods())
        writer.write(self._properties())
        writer.write(self._class_properties())
        writer.write(self._events())
        return writer.getvalue()

    def _metaclass_name(self) -> str:
        return f"_{self._td.generic_name}_Meta_"

    def _basetype(self) -> str:
        base = "ComPtr"
        if self._td.is_generic:
            generic_parameters = self._formatter.generic_parameters(self._td)
            base = f"Generic[{generic_parameters}], {base}"
        if self._has_classproperty():
            base = f"{base}, metaclass={self._metaclass_name()}"
        return base

    def _extends(self) -> str:
        if self._td.basetype is None:
            # interface
            return self._formatter.fullname("Windows.Win32.System.WinRT.IInspectable")
        elif self._td.basetype == "System.Object":
            # runtime class
            return self._formatter.fullname("Windows.Win32.System.WinRT.IInspectable")
        else:
            return self._formatter.fullname(self._td.basetype)

    def _implements(self) -> str:
        writer = StringIO()

        implements = []

        if (
            self._td.fullname == "Windows.Foundation.IAsyncOperation`1"
            or self._td.fullname == "Windows.Foundation.IAsyncOperationWithProgress`2"
            or self._td.fullname == "Windows.Foundation.IAsyncAction"
            or self._td.fullname == "Windows.Foundation.IAsyncActionWithProgress`1"
            or self._has_interface("Windows.Foundation.IAsyncOperation`1")
            or self._has_interface("Windows.Foundation.IAsyncOperationWithProgress`2")
            or self._has_interface("Windows.Foundation.IAsyncAction")
            or self._has_interface("Windows.Foundation.IAsyncActionWithProgress`1")
        ):
            implements.append("AwaitableProtocol")

        if (
            self._td.fullname == "Windows.Foundation.Collections.IMapView`2"
            or self._td.fullname == "Windows.Foundation.Collections.IMap`2"
        ):
            implements.append("MappingProtocol[K, V]")
        elif self._has_interface("Windows.Foundation.Collections.IMapView`2"):
            args = self._generic_interface_args("Windows.Foundation.Collections.IMapView`2")
            implements.append(f"MappingProtocol[{args}]")
        elif self._has_interface("Windows.Foundation.Collections.IMap`2"):
            args = self._generic_interface_args("Windows.Foundation.Collections.IMap`2")
            implements.append(f"MappingProtocol[{args}]")
        elif (
            self._td.fullname == "Windows.Foundation.Collections.IVectorView`1"
            or self._td.fullname == "Windows.Foundation.Collections.IVector`1"
        ):
            implements.append("SequenceProtocol[T]")
        elif self._has_interface("Windows.Foundation.Collections.IVectorView`1"):
            args = self._generic_interface_args("Windows.Foundation.Collections.IVectorView`1")
            implements.append(f"SequenceProtocol[{args}]")
        elif self._has_interface("Windows.Foundation.Collections.IVector`1"):
            args = self._generic_interface_args("Windows.Foundation.Collections.IVector`1")
            implements.append(f"SequenceProtocol[{args}]")
        elif self._td.fullname == "Windows.Foundation.Collections.IIterable`1":
            implements.append("IterableProtocol[T]")
        elif self._has_interface("Windows.Foundation.Collections.IIterable`1"):
            args = self._generic_interface_args("Windows.Foundation.Collections.IIterable`1")
            implements.append(f"IterableProtocol[{args}]")

        if self._td.fullname == "Windows.Foundation.IClosable" or self._has_interface("Windows.Foundation.IClosable"):
            implements.append("ContextManagerProtocol")

        if implements:
            # FIXME: use Tuple for 3.8.
            writer.write(f"    implements: Tuple[{', '.join(implements)}]\n")

        return writer.getvalue()

    def _has_interface(self, fullname) -> bool:
        for ii in self._td.interface_implementations:
            if ii.fullname == fullname:
                return True
        return False

    def _generic_interface_args(self, fullname) -> str:
        for ii in self._td.interface_implementations:
            if ii.fullname == fullname:
                return self._formatter.generic_arguments(ii.interface.type_specification.signature)
        raise RuntimeError("No interface found")

    def _has_default_interface(self) -> bool:
        for ii in self._td.interface_implementations:
            if ii.custom_attributes.has_default():
                return True
        return False

    def _default_interface(self) -> str:
        for ii in self._td.interface_implementations:
            if ii.custom_attributes.has_default():
                return self._formatter.generic_name_with_arguments(ii)
        raise ValueError()

    def _has_classproperty(self) -> bool:
        return any(
            True for md in self._td.methods if "Static" in md.attributes and md.name.startswith(("get_", "put_"))
        )

    def _constructor(self) -> str:
        writer = StringIO()
        methods = list(self._enumerate_composable_method()) + list(self._enumerate_activatable_method())
        if not methods:
            return ""
        methods.sort(key=lambda method: method.nargs)
        writer.write("    def __init__(self, *args, **kwargs):\n")
        writer.write("        if kwargs:\n")
        writer.write("            super().__init__(**kwargs)\n")
        for method in methods:
            writer.write(f"        elif len(args) == {method.nargs}:\n")
            writer.write(f"            super().__init__(move={method.invoke()})\n")
        writer.write("        else:\n")
        writer.write("            raise ValueError('no matched constructor')\n")
        writer.write(self._methods_overload(methods))
        return writer.getvalue()

    def _methods(self) -> str:
        # weakly typed overloaded methods
        methods = {}
        for method in self._enumerate_method():
            key = (method.name, method.nargs)
            if key not in methods or method.default_overload:
                methods[key] = method
        return self._methods_overload(list(methods.values()))

    def _methods_overload(self, methods: list[Method]) -> str:
        writer = StringIO()
        overload_initialized = set()
        overload_count = Counter(method.name for method in methods)
        overload_same_name_and_nargs = set()
        for method in methods:
            if overload_count[method.name] > 1:
                if method.name not in overload_initialized:
                    overload_initialized.add(method.name)
                    writer.write("    @winrt_overload\n")
                else:
                    writer.write(f"    @{method.name}.register\n")
            writer.write(method.emit())
            assert (method.name, method.nargs) not in overload_same_name_and_nargs
            overload_same_name_and_nargs.add((method.name, method.nargs))
        return writer.getvalue()

    def _properties(self) -> str:
        getter = {}
        setter = {}
        for md in (md for md in self._td.methods if "Static" not in md.attributes):
            if md.name.startswith("get_"):
                getter[removeprefix(md.name, "get_")] = md.name
            elif md.name.startswith("put_"):
                setter[removeprefix(md.name, "put_")] = md.name
        writer = StringIO()
        for name in sorted(getter | setter):
            writer.write(f"    {name} = property({getter.get(name)}, {setter.get(name)})\n")
        return writer.getvalue()

    def _class_properties(self) -> str:
        getter = {}
        setter = {}
        for md in (md for md in self._td.methods if "Static" in md.attributes):
            if md.name.startswith("get_"):
                getter[removeprefix(md.name, "get_")] = md.name
            elif md.name.startswith("put_"):
                setter[removeprefix(md.name, "put_")] = md.name
        writer = StringIO()
        for name in sorted(getter | setter):
            writer.write(f"    {self._metaclass_name()}.{name} = property({getter.get(name)}, {setter.get(name)})\n")
        return writer.getvalue()

    def _events(self) -> str:
        writer = StringIO()
        for md in (md for md in self._td.methods if "Static" not in md.attributes):
            if md.name.startswith("add_"):
                name = removeprefix(md.name, "add_")
                writer.write(f"    {name} = event()\n")
        return writer.getvalue()

    def _enumerate_composable_method(self) -> Iterable[Method]:
        if not self._td.custom_attributes.has_composable():
            return
        ca = self._td.custom_attributes.get_composable()
        td = self._get_com(ca.fixed_arguments[0].value)._td
        for md in td.methods:
            assert md.signature.return_type.fullname == self._td.fullname
            yield CompositionMethod(self._td, td, md, self._formatter)

    def _enumerate_activatable_method(self) -> Iterable[Method]:
        for ca in self._td.custom_attributes.get_activatable():
            if ca.fixed_arguments[0].type.kind == "Type":
                td = self._get_com(ca.fixed_arguments[0].value)._td
                for md in td.methods:
                    yield FactoryActivationMethod(self._td, td, md, self._formatter)
            else:
                yield ActivationMethod(self._td, self._formatter)

    def _enumerate_method(self) -> Iterable[Method]:
        vtbl_index = self._count_interface_method()
        for md in self._td.methods:
            if md.name == ".ctor":
                pass
            elif "Static" in md.attributes:
                yield ClassMethod(self._get_static_interface_for_method(md), md, self._formatter)
            elif "Abstract" in md.attributes:
                yield ComMethod(md, vtbl_index, self._formatter)
                vtbl_index += 1
            else:
                yield MixinMethod(self._get_interface_for_method(md), md, self._formatter)

    def _get_static_interface_for_method(self, mymd: MethodDefinition) -> TypeDefinition:
        for ca in self._td.custom_attributes.get_static():
            td = self._get_com(ca.fixed_arguments[0].value)._td
            for md in td.methods:
                if md.name_overload == mymd.name_overload and md.get_parameter_names() == mymd.get_parameter_names():
                    return td
        raise KeyError()

    def _get_interface_for_method(self, mymd: MethodDefinition) -> InterfaceImplementation:
        for ii in self._td.interface_implementations:
            td = self._get_com(ii.fullname)._td
            for md in td.methods:
                if md.name_overload == mymd.name_overload and md.get_parameter_names() == mymd.get_parameter_names():
                    return ii
        raise KeyError()

    def _count_interface_method(self) -> int:
        if self._td.basetype is None or self._td.basetype == "System.Object":
            return 6  # count of IInspectable
        com = self._get_com(self._td.basetype)
        return len(com._td.methods) + com._count_interface_method()

    def _get_com(self, fullname: str) -> Com:
        namespace, name = fullname.rsplit(".", 1)
        com = self._package[namespace][name]
        if not isinstance(com, Com):
            raise TypeError()
        return com


class Method(Protocol):
    @property
    def name(self) -> str: ...

    @property
    def nargs(self) -> int: ...

    @property
    def default_overload(self) -> bool: ...

    def invoke(self) -> str: ...

    def emit(self) -> str: ...


class CompositionMethod:
    def __init__(
        self, class_td: TypeDefinition, interface_td: TypeDefinition, md: MethodDefinition, formatter: Formatter
    ) -> None:
        self._class_td = class_td
        self._interface_td = interface_td
        self._md = md
        self._formatter = formatter

    @property
    def name(self) -> str:
        return self._md.name_overload

    @property
    def nargs(self) -> int:
        return len(self._md.get_parameter_names()) - 2

    @property
    def default_overload(self) -> bool:
        return self._md.custom_attributes.has_default_overload()

    def invoke(self) -> str:
        return f"{self._formatter.fullname(self._class_td)}.{self.name}(*args, None, None)"

    def emit(self) -> str:
        writer = StringIO()
        clsname = self._formatter.generic_name_with_parameters(self._interface_td)
        restype = self._formatter.pytype(self._md.signature.return_type)
        params = ", ".join([f"cls: {clsname}"] + self._formatter.method_parameters_annotated(self._md))
        writer.write("    @winrt_factorymethod\n")
        writer.write(f"    def {self.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()


class FactoryActivationMethod:
    def __init__(
        self, class_td: TypeDefinition, interface_td: TypeDefinition, md: MethodDefinition, formatter: Formatter
    ) -> None:
        self._class_td = class_td
        self._interface_td = interface_td
        self._md = md
        self._formatter = formatter

    @property
    def name(self) -> str:
        return self._md.name_overload

    @property
    def nargs(self) -> int:
        return len(self._md.get_parameter_names())

    @property
    def default_overload(self) -> bool:
        return self._md.custom_attributes.has_default_overload()

    def invoke(self) -> str:
        return f"{self._formatter.fullname(self._class_td)}.{self.name}(*args)"

    def emit(self) -> str:
        writer = StringIO()
        clsname = self._formatter.generic_name_with_parameters(self._interface_td)
        restype = self._formatter.pytype(self._md.signature.return_type)
        params = ", ".join([f"cls: {clsname}"] + self._formatter.method_parameters_annotated(self._md))
        writer.write("    @winrt_factorymethod\n")
        writer.write(f"    def {self.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()


class ActivationMethod:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        self._td = td
        self._formatter = formatter

    @property
    def name(self) -> str:
        return "CreateInstance"

    @property
    def nargs(self) -> int:
        return 0

    @property
    def default_overload(self) -> bool:
        return False

    def invoke(self) -> str:
        return f"{self._formatter.fullname(self._td)}.CreateInstance(*args)"

    def emit(self) -> str:
        writer = StringIO()
        clsname = self._formatter.generic_name_with_parameters(self._td)
        writer.write("    @winrt_activatemethod\n")
        writer.write(f"    def CreateInstance(cls) -> {clsname}: ...\n")
        return writer.getvalue()


class ClassMethod:
    def __init__(self, td: TypeDefinition, md: MethodDefinition, formatter: Formatter) -> None:
        self._td = td
        self._md = md
        self._formatter = formatter

    @property
    def name(self) -> str:
        return self._md.name_overload

    @property
    def nargs(self) -> int:
        return len(self._md.get_parameter_names())

    @property
    def default_overload(self) -> bool:
        return self._md.custom_attributes.has_default_overload()

    def invoke(self) -> str:
        raise NotImplementedError()

    def emit(self) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(self._md.signature.return_type)
        interface = self._formatter.fullname(self._td)
        params = ", ".join([f"cls: {interface}"] + self._formatter.method_parameters_annotated(self._md))
        writer.write("    @winrt_classmethod\n")
        writer.write(f"    def {self.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()


class ComMethod:
    def __init__(self, md: MethodDefinition, vtbl_index: int, formatter: Formatter) -> None:
        self._md = md
        self._vtbl_index = vtbl_index
        self._formatter = formatter

    @property
    def name(self) -> str:
        return self._md.name_overload

    @property
    def nargs(self) -> int:
        return len(self._md.get_parameter_names())

    @property
    def default_overload(self) -> bool:
        return self._md.custom_attributes.has_default_overload()

    def invoke(self) -> str:
        raise NotImplementedError()

    def emit(self) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(self._md.signature.return_type)
        params = ", ".join(["self"] + self._formatter.method_parameters_annotated(self._md))
        writer.write(f"    @winrt_commethod({self._vtbl_index})\n")
        writer.write(f"    def {self.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()


class MixinMethod:
    def __init__(self, ii: InterfaceImplementation, md: MethodDefinition, formatter: Formatter) -> None:
        self._ii = ii
        self._md = md
        self._formatter = formatter

    @property
    def name(self) -> str:
        return self._md.name_overload

    @property
    def nargs(self) -> int:
        return len(self._md.get_parameter_names())

    @property
    def default_overload(self) -> bool:
        return self._md.custom_attributes.has_default_overload()

    def invoke(self) -> str:
        raise NotImplementedError()

    def emit(self) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(self._md.signature.return_type)
        interface = self._formatter.generic_name_with_arguments(self._ii)
        params = ", ".join([f"self: {interface}"] + self._formatter.method_parameters_annotated(self._md))
        writer.write("    @winrt_mixinmethod\n")
        writer.write(f"    def {self.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()


class Delegate:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert len(td.methods) == 2
        assert td.methods[0].name == ".ctor"
        assert td.methods[1].name == "Invoke"
        assert td.custom_attributes.has_winrt_guid()
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from Dependencies(self._td)

    def emit(self) -> str:
        writer = StringIO()
        writer.write(f"class {self._td.generic_name}({self._basetype()}):\n")
        writer.write(f"    extends: {self._formatter.fullname('Windows.Win32.System.Com.IUnknown')}\n")
        guid = self._td.custom_attributes.get_winrt_guid()
        if self._td.is_generic:
            writer.write(f"    _piid_ = Guid('{guid}')\n")
        else:
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        writer.write(self._method(self._td.methods[1]))
        return writer.getvalue()

    def _basetype(self) -> str:
        if self._td.is_generic:
            generic_parameters = self._formatter.generic_parameters(self._td)
            return f"Generic[{generic_parameters}], MulticastDelegate"
        return "MulticastDelegate"

    def _method(self, md: MethodDefinition) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(md.signature.return_type)
        params = ", ".join(["self"] + self._formatter.method_parameters_annotated(md))
        writer.write("    @winrt_commethod(3)\n")
        writer.write(f"    def {md.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()
