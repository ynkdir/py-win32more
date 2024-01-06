from __future__ import annotations

import functools
import logging
from collections import Counter, defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from io import StringIO

from .backport import removeprefix
from .metadata import InterfaceImplementation, MethodDefinition, TType, TypeDefinition
from .package import ApiItem, Module, Package
from .win32 import BASE_EXPORTS_CSV

logger = logging.getLogger(__name__)

WINRT_EXPORTS = [
    "Annotated",
    "Generic",
    "K",
    "MulticastDelegate",
    "SZArray",
    "T",
    "TProgress",
    "TResult",
    "TSender",
    "V",
    "WinRT_String",
    "winrt_activatemethod",
    "winrt_classmethod",
    "winrt_commethod",
    "winrt_factorymethod",
    "winrt_mixinmethod",
    "winrt_overload",
]
WINRT_EXPORTS_CSV = ", ".join(WINRT_EXPORTS)


@dataclass
class Method:
    name: str
    nargs: int
    invoke: str
    declare: str
    default_overload: bool


class Parser:
    def __init__(self, package: Package) -> None:
        self._package = package

    def parse(self, td: TypeDefinition) -> None:
        if td.namespace not in self._package:
            self._package[td.namespace] = WinrtModule(td.namespace, self._package)

        module = self._package[td.namespace]

        formatter = Formatter(self._package)

        if td.basetype is None or td.basetype == "System.Object" or td.basetype.startswith(("Windows.", "Microsoft.")):
            module.add(Com(td, self._package, formatter))
        elif td.basetype == "System.MulticastDelegate":
            module.add(Delegate(td, self._package, formatter))
        elif td.basetype == "System.Enum":
            module.add(Enum(td, formatter))
        elif td.basetype == "System.ValueType":
            if td.fields:
                module.add(Struct(td, formatter))
            elif td.custom_attributes.has("Windows.Foundation.Metadata.ContractVersionAttribute"):
                module.add(ContractVersion(td, formatter))
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
            return f"SZArray[{self.pytype(ttype.type)}]"
        elif ttype.kind == "Type":
            if ttype.is_guid:
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
            if type_.kind == "SZArray":
                attrs = []
                if "Out" in pa.attributes:
                    attrs.append("'Out'")
                if "In" in pa.attributes:
                    attrs.append("'In'")
                annotated = ", ".join([self.pytype(type_)] + attrs)
                pytype = f"Annotated[{annotated}]"
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
    def add(self, item: ApiItem) -> None:
        assert self.namespace == item.namespace
        assert item.name not in self._items
        self._items[item.name] = item

    def imported_namespaces(self) -> set[str]:
        return {fullname.rsplit(".", 1)[0] for fullname in self.enumerate_dependencies()}

    def emit_header(self) -> str:
        writer = StringIO()
        writer.write("from __future__ import annotations\n")
        writer.write(f"from {self._package.name} import {BASE_EXPORTS_CSV}\n")
        writer.write(f"from {self._package.name}._winrt import {WINRT_EXPORTS_CSV}\n")
        for namespace in sorted(self.imported_namespaces() | {self.namespace}):
            writer.write(f"import {self._package.name}.{namespace}\n")
        return writer.getvalue()

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
        yield from self._td.fields[0].enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        type_field, *value_fields = self._td.fields
        writer.write(f"class {self._td.name}({self._formatter.pytype(type_field.signature)}):  # enum\n")
        for fd in value_fields:
            writer.write(f"    {fd.name} = {fd.default_value.value}\n")
        return writer.getvalue()


class Struct:
    def __init__(self, td: TypeDefinition, formatter: Formatter) -> None:
        assert td.fields
        assert not td.nested_types
        assert "SequentialLayout" in td.attributes
        assert not td.custom_attributes.has_winrt_guid()
        assert not any(fd for fd in td.fields if {"Static", "HasDefault"} <= set(td.attributes))
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
        yield from self._td.enumerate_dependencies()

    # _fields_ and _anonymous_ is defined at runtime.
    def emit(self) -> str:
        writer = StringIO()
        writer.write(f"class {self._td.name}(EasyCastStructure):\n")
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
        yield from self._td.enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        if self._has_classproperty():
            writer.write(f"class {self._metaclass_name()}(ComPtr.__class__):\n")
            writer.write("    pass\n")
        writer.write(f"class {self._td.generic_name}({self._basetype()}):\n")
        writer.write(f"    extends: {self._extends()}\n")
        if self._has_default_interface():
            writer.write(f"    default_interface: {self._default_interface()}\n")
        writer.write(f"    _classid_ = '{self._td.generic_fullname}'\n")
        if self._td.custom_attributes.has_winrt_guid():
            guid = self._td.custom_attributes.get_winrt_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        writer.write(self._constructor())
        writer.write(self._methods())
        writer.write(self._properties())
        writer.write(self._await_method())
        return writer.getvalue()

    def _metaclass_name(self) -> str:
        return f"_{self._td.generic_name}_Meta_"

    def _basetype(self) -> str:
        if self._td.is_generic:
            generic_parameters = self._formatter.generic_parameters(self._td)
            base = f"Generic[{generic_parameters}], ComPtr"
        else:
            base = "ComPtr"
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
        for md in self._td.method_definitions:
            if md.name == ".ctor":
                continue
            is_static = "Static" in md.attributes
            is_special = "SpecialName" in md.attributes
            is_property = md.name.startswith(("get_", "put_"))
            if is_static and is_special and is_property:
                return True
        return False

    def _properties(self) -> str:
        writer = StringIO()
        properties: dict[str, dict[str, str | bool | None]] = defaultdict(lambda: {"get": None, "put": None})
        for md in self._td.method_definitions:
            if md.name == ".ctor":
                continue
            if "SpecialName" in md.attributes:
                if md.name.startswith("get_"):
                    property_name = removeprefix(md.name, "get_")
                    properties[property_name]["get"] = md.name
                    properties[property_name]["is_static"] = "Static" in md.attributes
                elif md.name.startswith("put_"):
                    property_name = removeprefix(md.name, "put_")
                    properties[property_name]["put"] = md.name
                    properties[property_name]["is_static"] = "Static" in md.attributes
                elif md.name.startswith("add_"):
                    # add event
                    pass
                elif md.name.startswith("remove_"):
                    # remove event
                    pass
                elif md.name == "Invoke":
                    # callback handler
                    pass
                else:
                    raise NotImplementedError()
        for name, attrs in properties.items():
            if attrs["is_static"]:
                if attrs["get"] is None:
                    getter = "None"
                else:
                    getter = f"{attrs['get']}.__wrapped__"
                if attrs["put"] is None:
                    setter = "None"
                else:
                    setter = f"{attrs['put']}.__wrapped__"
                writer.write(f"    {self._metaclass_name()}.{name} = property({getter}, {setter})\n")
            else:
                writer.write(f"    {name} = property({attrs['get']}, {attrs['put']})\n")
        return writer.getvalue()

    def _await_method(self) -> str:
        writer = StringIO()
        if self._td.generic_fullname == "Windows.Foundation.IAsyncOperation":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {self._package.name}._winrt import IAsyncOperation___await__\n")
            writer.write("        return IAsyncOperation___await__(self)\n")
        elif self._td.generic_fullname == "Windows.Foundation.IAsyncOperationWithProgress":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {self._package.name}._winrt import IAsyncOperation___await__\n")
            writer.write("        return IAsyncOperation___await__(self)\n")
        elif self._td.generic_fullname == "Windows.Foundation.IAsyncAction":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {self._package.name}._winrt import IAsyncAction___await__\n")
            writer.write("        return IAsyncAction___await__(self)\n")
        elif self._td.generic_fullname == "Windows.Foundation.IAsyncActionWithProgress":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {self._package.name}._winrt import IAsyncAction___await__\n")
            writer.write("        return IAsyncAction___await__(self)\n")
        return writer.getvalue()

    def _count_interface_method(self) -> int:
        if self._td.basetype is None or self._td.basetype == "System.Object":
            return 6  # count of IInspectable
        namespace, name = self._td.basetype.rsplit(".", 1)
        com = self._package[namespace][name]
        if not isinstance(com, Com):
            raise TypeError()
        return len(com._td.method_definitions) + com._count_interface_method()

    def _constructor(self) -> str:
        writer = StringIO()
        methods = []
        if self._td.custom_attributes.has_composable():
            ca = self._td.custom_attributes.get_composable()
            methods.extend(self._composable_methods(ca.fixed_arguments[0].value))
        for ca in self._td.custom_attributes.get_activatable():
            if ca.fixed_arguments[0].type.kind == "Type":
                methods.extend(self._activatable_methods(ca.fixed_arguments[0].value))
            else:
                methods.append(
                    Method(
                        name="CreateInstance",
                        nargs=0,
                        invoke=f"{self._formatter.fullname(self._td)}.CreateInstance(*args)",
                        declare=self._activatemethod(),
                        default_overload=False,
                    )
                )
        if not methods:
            return ""
        methods.sort(key=lambda method: method.nargs)
        writer.write("    def __new__(cls, *args, **kwargs):\n")
        writer.write("        if kwargs:\n")
        writer.write("            return super().__new__(cls, **kwargs)\n")
        for i, method in enumerate(methods):
            writer.write(f"        elif len(args) == {method.nargs}:\n")
            writer.write(f"            return {method.invoke}\n")
        writer.write("        else:\n")
        writer.write("            raise ValueError('no matched constructor')\n")
        writer.write(self._methods_overload(methods))
        return writer.getvalue()

    def _composable_methods(self, fullname: str) -> list[Method]:
        namespace, name = fullname.rsplit(".", 1)
        com = self._package[namespace][name]
        if not isinstance(com, Com):
            raise TypeError()
        td = com._td
        methods = []
        for md in td.method_definitions:
            assert md.signature.return_type.fullname == self._td.fullname
            methods.append(
                Method(
                    name=md.name_overload,
                    nargs=len(md.get_parameter_names()) - 2,
                    invoke=f"{self._formatter.fullname(self._td)}.{md.name_overload}(*args, None, None)",
                    declare=self._factorymethod(td, md),
                    default_overload=False,
                )
            )
        return methods

    def _activatable_methods(self, fullname: str) -> list[Method]:
        namespace, name = fullname.rsplit(".", 1)
        com = self._package[namespace][name]
        if not isinstance(com, Com):
            raise TypeError()
        td = com._td
        methods = []
        for md in td.method_definitions:
            assert md.signature.return_type.fullname == self._td.fullname
            methods.append(
                Method(
                    name=md.name_overload,
                    nargs=len(md.get_parameter_names()),
                    invoke=f"{self._formatter.fullname(self._td)}.{md.name_overload}(*args)",
                    declare=self._factorymethod(td, md),
                    default_overload=False,
                )
            )
        return methods

    def _factorymethod(self, td: TypeDefinition, md: MethodDefinition) -> str:
        writer = StringIO()
        clsname = self._formatter.generic_name_with_parameters(td)
        restype = self._formatter.pytype(md.signature.return_type)
        params = ", ".join([f"cls: {clsname}"] + self._formatter.method_parameters_annotated(md))
        writer.write("    @winrt_factorymethod\n")
        writer.write(f"    def {md.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()

    def _activatemethod(self) -> str:
        writer = StringIO()
        clsname = self._formatter.generic_name_with_parameters(self._td)
        writer.write("    @winrt_activatemethod\n")
        writer.write(f"    def CreateInstance(cls) -> {clsname}: ...\n")
        return writer.getvalue()

    def _methods(self) -> str:
        writer = StringIO()
        methods = []
        default_overload = set()
        vtbl_index = self._count_interface_method()
        for md in self._td.method_definitions:
            if md.name == ".ctor":
                continue
            if "Static" in md.attributes:
                method_declare = self._classmethod(md)
            elif "Abstract" in self._td.attributes:
                method_declare = self._commethod(md, vtbl_index)
                vtbl_index += 1
            else:
                method_declare = self._mixinmethod(md)
            method = Method(
                name=md.name_overload,
                nargs=len(md.get_parameter_names()),
                invoke="",
                declare=method_declare,
                default_overload=md.custom_attributes.has_default_overload(),
            )
            methods.append(method)
            if method.default_overload:
                default_overload.add((method.name, method.nargs))

        # Remove colliding method
        # FIXME: Need strongly typed dispatch?
        # Windows.Globalization.NumberFormatting.CurrencyFormatter has Format(Int64) (overload_name=FormatInt) and FormatInt(Int64).
        methods = list(
            {
                method.declare: method
                for method in methods
                if method.default_overload or ((method.name, method.nargs) not in default_overload)
            }.values()
        )

        writer.write(self._methods_overload(methods))
        return writer.getvalue()

    def _classmethod(self, md: MethodDefinition) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(md.signature.return_type)
        interface = self._get_static_interface_for_method(md.name_overload, len(md.get_parameter_names()))
        params = ", ".join([f"cls: {interface}"] + self._formatter.method_parameters_annotated(md))
        writer.write("    @winrt_classmethod\n")
        writer.write(f"    def {md.name_overload}({params}) -> {restype}: ...\n")
        return writer.getvalue()

    def _get_static_interface_for_method(self, method_name: str, method_nargs: int) -> str:
        for ca in self._td.custom_attributes.get_static():
            namespace, name = ca.fixed_arguments[0].value.rsplit(".", 1)
            com = self._package[namespace][name]
            if not isinstance(com, Com):
                raise TypeError()
            td_static = com._td
            for md in td_static.method_definitions:
                if md.custom_attributes.has_overload():
                    static_method_name = md.custom_attributes.get_overload()
                else:
                    static_method_name = md.name
                if static_method_name == method_name and len(md.get_parameter_names()) == method_nargs:
                    return self._formatter.fullname(ca.fixed_arguments[0].value)
        raise KeyError()

    def _commethod(self, md: MethodDefinition, vtbl_index: int) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(md.signature.return_type)
        params = ", ".join(["self"] + self._formatter.method_parameters_annotated(md))
        writer.write(f"    @winrt_commethod({vtbl_index})\n")
        writer.write(f"    def {md.name_overload}({params}) -> {restype}: ...\n")
        return writer.getvalue()

    def _mixinmethod(self, md: MethodDefinition) -> str:
        writer = StringIO()
        restype = self._formatter.pytype(md.signature.return_type)
        interface = self._get_interface_for_method(md.name_overload, md.get_parameter_names())
        params = ", ".join([f"self: {interface}"] + self._formatter.method_parameters_annotated(md))
        writer.write("    @winrt_mixinmethod\n")
        writer.write(f"    def {md.name_overload}({params}) -> {restype}: ...\n")
        return writer.getvalue()

    def _get_interface_for_method(self, method_name: str, params: list[str]) -> str:
        for ii in self._td.interface_implementations:
            com = self._package[ii.namespace][ii.name]
            if not isinstance(com, Com):
                raise TypeError()
            td_interface = com._td
            for md in td_interface.method_definitions:
                if md.custom_attributes.has_overload():
                    interface_method_name = md.custom_attributes.get_overload()
                else:
                    interface_method_name = md.name
                if interface_method_name == method_name:
                    if md.get_parameter_names() == params:
                        return self._formatter.generic_name_with_arguments(ii)
        raise KeyError()

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
            writer.write(method.declare)
            assert (method.name, method.nargs) not in overload_same_name_and_nargs
            overload_same_name_and_nargs.add((method.name, method.nargs))
        return writer.getvalue()


class Delegate:
    def __init__(self, td: TypeDefinition, package: Package, formatter: Formatter) -> None:
        assert len(td.method_definitions) == 2
        assert td.method_definitions[0].name == ".ctor"
        assert td.method_definitions[1].name == "Invoke"
        assert td.custom_attributes.has_winrt_guid()
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
        yield from self._td.enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        writer.write(f"class {self._td.generic_name}({self._basetype()}):\n")
        writer.write(f"    extends: {self._formatter.fullname('Windows.Win32.System.Com.IUnknown')}\n")
        guid = self._td.custom_attributes.get_winrt_guid()
        writer.write(f"    _iid_ = Guid('{guid}')\n")
        writer.write(self._method(self._td.method_definitions[1]))
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
        writer.write(f"    def {md.name}({params}) -> {restype}: ...\n")
        return writer.getvalue()
