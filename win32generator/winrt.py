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
                return f"{self.fullname(ttype)}"
        elif ttype.kind == "Generic":
            return f"{self.fullname(self.generic_name_with_arguments(ttype))}"
        elif ttype.kind == "GenericParameter":
            return ttype.name
        elif ttype.kind == "Modified" and ttype.modifier_type.fullname == "System.Runtime.CompilerServices.IsConst":
            return self.pytype(ttype.unmodified_type)
        else:
            raise NotImplementedError()

    @functools.singledispatchmethod
    def generic_name_with_arguments(self, ttype: TType) -> str:
        fullname = ttype.type.generic_fullname
        arguments = self.generic_arguments(ttype)
        return f"{fullname}[{arguments}]"

    @generic_name_with_arguments.register
    def _(self, ii: InterfaceImplementation) -> str:
        if ii.interface.kind == "TypeReference":
            return ii.interface.type_reference.fullname
        elif ii.interface.kind == "TypeSpecification":
            if ii.interface.type_specification.signature.kind == "Generic":
                return self.generic_name_with_arguments(ii.interface.type_specification.signature)
            return ii.interface.type_specification.signature.type.fullname
        else:
            raise NotImplementedError()

    def generic_arguments(self, ttype: TType) -> str:
        return ", ".join(self.pytype(ta) for ta in ttype.type_arguments)

    def generic_parameters(self, td: TypeDefinition) -> str:
        return ", ".join(gp.name for gp in td.generic_parameters)

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
        return self.fullname(ttype.fullname)

    @fullname.register
    def _(self, td: TypeDefinition) -> str:
        return self.fullname(td.fullname)

    @fullname.register
    def _(self, ii: InterfaceImplementation) -> str:
        return self.fullname(ii.fullname)


class WinrtModule(Module):
    def add(self, item: ApiItem) -> None:
        assert self.namespace == item.namespace
        assert item.name not in self._items
        self._items[item.name] = item

    def emit_header(self, import_namespaces: set[str]) -> str:
        writer = StringIO()

        writer.write("from __future__ import annotations\n")

        writer.write(f"from {self._package.name} import {BASE_EXPORTS_CSV}\n")

        writer.write(f"from {self._package.name}._winrt import {WINRT_EXPORTS_CSV}\n")

        if not self._package.is_onefile:
            for namespace in sorted(import_namespaces):
                writer.write(f"import {self._package.name}.{namespace}\n")

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
        writer.write(f"{self._td.name} = {self._formatter.pytype(type_field.signature)}\n")
        for fd in value_fields:
            writer.write(f"{fd.name}: {self._td.name} = {fd.default_value.value}\n")
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
        writer.write(f"class {self._generic_name}({self._basetype()}):\n")
        writer.write(f"    extends: {self._extends()}\n")
        if self._has_default_interface():
            writer.write(f"    default_interface: {self._default_interface()}\n")
        writer.write(f"    _classid_ = '{self._generic_fullname}'\n")
        if self._td.custom_attributes.has_winrt_guid():
            guid = self._td.custom_attributes.get_winrt_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        writer.write(self.winrt_constructor(self._td))
        writer.write(self.winrt_method_definitions(self._td))
        writer.write(self._properties())
        writer.write(self._await_method())
        return writer.getvalue()

    @property
    def _generic_name(self) -> str:
        if self._td.is_generic:
            return self._td.generic_name
        return self._td.name

    @property
    def _generic_fullname(self) -> str:
        return f"{self.namespace}.{self._generic_name}"

    def _metaclass_name(self) -> str:
        return f"_{self._generic_name}_Meta_"

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
                return self._formatter.fullname(self._formatter.generic_name_with_arguments(ii))
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

    def com_get_interface_for_method(self, td: TypeDefinition, method_name: str, params: list[str]) -> str:
        for ii in td.interface_implementations:
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

    def com_get_static_for_method(self, td: TypeDefinition, method_name: str, method_nargs: int) -> str:
        for ca in td.custom_attributes.get_static():
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
                    return ca.fixed_arguments[0].value
        raise KeyError()

    def winrt_method(self, td: TypeDefinition, md: MethodDefinition, p_vtbl_index: list[int]) -> str:
        writer = StringIO()
        method_name = md.name_overload
        params = ["self"] + self._formatter.method_parameters_annotated(md)
        restype = self._formatter.pytype(md.signature.return_type)
        if td.basetype == "System.MulticastDelegate":
            pass
        elif "Static" in md.attributes:
            writer.write("    @winrt_classmethod\n")
            interface = self.com_get_static_for_method(td, method_name, len(md.get_parameter_names()))
            params[0] = f"cls: {self._formatter.fullname(interface)}"
        elif "Abstract" not in td.attributes:
            writer.write("    @winrt_mixinmethod\n")
            interface = self.com_get_interface_for_method(td, method_name, md.get_parameter_names())
            params[0] = f"self: {self._formatter.fullname(interface)}"
        else:
            writer.write(f"    @winrt_commethod({p_vtbl_index[0]})\n")
            p_vtbl_index[0] += 1
        params_csv = ", ".join(params)
        writer.write(f"    def {method_name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def _count_interface_method(self) -> int:
        if self._td.basetype is None or self._td.basetype == "System.Object":
            return 6  # count of IInspectable
        elif self._td.basetype == "System.MulticastDelegate":
            return 3  # count of IUnknown
        namespace, name = self._td.basetype.rsplit(".", 1)
        com = self._package[namespace][name]
        if not isinstance(com, Com):
            raise TypeError()
        return len(com._td.method_definitions) + com._count_interface_method()

    def winrt_factorymethod(self, td: TypeDefinition, md: MethodDefinition) -> str:
        writer = StringIO()
        if td.is_generic:
            generic_parameters = self._formatter.generic_parameters(self._td)
            name = f"{td.generic_fullname}[{generic_parameters}]"
        else:
            name = td.fullname
        params = [f"cls: {self._formatter.fullname(name)}"] + self._formatter.method_parameters_annotated(md)
        params_csv = ", ".join(params)
        restype = self._formatter.pytype(md.signature.return_type)
        writer.write("    @winrt_factorymethod\n")
        writer.write(f"    def {md.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def winrt_activatemethod(self, td: TypeDefinition) -> str:
        writer = StringIO()
        if td.is_generic:
            generic_parameters = self._formatter.generic_parameters(self._td)
            name = f"{td.generic_fullname}[{generic_parameters}]"
        else:
            name = td.fullname
        writer.write("    @winrt_activatemethod\n")
        writer.write(f"    def CreateInstance(cls) -> {self._formatter.fullname(name)}: ...\n")
        return writer.getvalue()

    def winrt_constructor(self, td: TypeDefinition) -> str:
        writer = StringIO()
        methods = []
        if td.custom_attributes.has_composable():
            ca = td.custom_attributes.get_composable()
            namespace, name = ca.fixed_arguments[0].value.rsplit(".", 1)
            com = self._package[namespace][name]
            if not isinstance(com, Com):
                raise TypeError()
            factory = com._td
            for md in factory.method_definitions:
                assert md.signature.return_type.fullname == td.fullname
                methods.append(
                    Method(
                        name=md.name_overload,
                        nargs=len(md.get_parameter_names()) - 2,
                        invoke=f"{self._formatter.fullname(td)}.{md.name_overload}(*args, None, None)",
                        declare=self.winrt_factorymethod(factory, md),
                        default_overload=False,
                    )
                )
        for ca in td.custom_attributes.get_activatable():
            if ca.fixed_arguments[0].type.kind == "Type":
                namespace, name = ca.fixed_arguments[0].value.rsplit(".", 1)
                com = self._package[namespace][name]
                if not isinstance(com, Com):
                    raise TypeError()
                factory = com._td
                for md in factory.method_definitions:
                    assert md.signature.return_type.fullname == td.fullname
                    methods.append(
                        Method(
                            name=md.name_overload,
                            nargs=len(md.get_parameter_names()),
                            invoke=f"{self._formatter.fullname(td)}.{md.name_overload}(*args)",
                            declare=self.winrt_factorymethod(factory, md),
                            default_overload=False,
                        )
                    )
            else:
                methods.append(
                    Method(
                        name="CreateInstance",
                        nargs=0,
                        invoke=f"{self._formatter.fullname(td)}.CreateInstance(*args)",
                        declare=self.winrt_activatemethod(td),
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

    def winrt_method_definitions(self, td: TypeDefinition) -> str:
        writer = StringIO()
        methods = []
        default_overload = set()
        p_vtbl_index = [self._count_interface_method()]
        for md in td.method_definitions:
            if md.name == ".ctor":
                continue
            method = Method(
                name=md.name_overload,
                nargs=len(md.get_parameter_names()),
                invoke="",
                declare=self.winrt_method(td, md, p_vtbl_index),
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
        if self._td.is_generic:
            generic_parameters = self._formatter.generic_parameters(self._td)
            name = self._td.generic_name
            base = f"Generic[{generic_parameters}], MulticastDelegate"
        else:
            name = self._td.name
            base = "MulticastDelegate"
        writer.write(f"class {name}({base}):\n")
        writer.write(f"    extends: {self._formatter.fullname('Windows.Win32.System.Com.IUnknown')}\n")
        if self._td.custom_attributes.has_winrt_guid():
            guid = self._td.custom_attributes.get_winrt_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        com = Com(self._td, self._package, self._formatter)  # FIXME
        p_vtbl_index = [3]  # count of IUnknown
        for md in self._td.method_definitions:
            if md.name == ".ctor":
                continue
            writer.write(com.winrt_method(self._td, md, p_vtbl_index))
        return writer.getvalue()
