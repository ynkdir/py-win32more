from __future__ import annotations

import logging
from collections import Counter, defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from io import StringIO

from .backport import removeprefix
from .metadata import FieldDefinition, InterfaceImplementation, MethodDefinition, TType, TypeDefinition
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


def ttype_pytype(self: TType) -> str:
    if self.kind == "Primitive":
        if self.name == "Object":
            return Package.abs_pkg("Windows.Win32.System.WinRT.IInspectable")
        elif self.name == "String":
            return "WinRT_String"
        else:
            return self.name
    elif self.kind == "Reference":
        return f"POINTER({ttype_pytype(self.type)})"
    elif self.kind == "SZArray":
        return f"SZArray[{ttype_pytype(self.type)}]"
    elif self.kind == "Type":
        if self.is_guid:
            return "Guid"
        else:
            return f"{Package.abs_pkg(self.fullname)}"
    elif self.kind == "Generic":
        return f"{Package.abs_pkg(ttype_generic_fullname(self))}"
    elif self.kind == "GenericParameter":
        return self.name
    elif self.kind == "Modified" and self.modifier_type.fullname == "System.Runtime.CompilerServices.IsConst":
        return ttype_pytype(self.unmodified_type)
    else:
        raise NotImplementedError()


def generic_strip_suffix(name) -> str:
    return name.split("`")[0]


def ttype_generic_fullname(self: TType) -> str:
    fullname = generic_strip_suffix(self.type.fullname)
    parameters = ttype_format_generic_parameters(self)
    return f"{fullname}[{parameters}]"


def ttype_format_generic_parameters(self: TType) -> str:
    return ", ".join(ttype_pytype(ta) for ta in self.type_arguments)


def md_parameter_names_annotated(self: MethodDefinition) -> list[str]:
    r = []
    for pa, type_ in self.parameters_with_type:
        if type_.kind == "SZArray":
            attrs = []
            if "Out" in pa.attributes:
                attrs.append("'Out'")
            if "In" in pa.attributes:
                attrs.append("'In'")
            annotated = ", ".join([ttype_pytype(type_)] + attrs)
            pytype = f"Annotated[{annotated}]"
        else:
            pytype = ttype_pytype(type_)
        r.append(f"{pa.name}: {pytype}")
    return r


def fd_pyvalue(self: FieldDefinition) -> str:
    if "HasDefault" in self.attributes:
        return ascii(self.default_value.value)
    elif self.signature.kind == "Type" and self.signature.fullname == "System.Guid":
        guid = self.custom_attributes.get_winrt_guid()
        return f"Guid('{guid}')"
    else:
        # FIXME:
        raise NotImplementedError()


def ii_generic_fullname(self: InterfaceImplementation) -> str:
    if self.interface.kind == "TypeReference":
        return self.interface.type_reference.fullname
    elif self.interface.kind == "TypeSpecification":
        if self.interface.type_specification.signature.kind == "Generic":
            return ttype_generic_fullname(self.interface.type_specification.signature)
        return self.interface.type_specification.signature.type.fullname
    else:
        raise NotImplementedError()


def td_format_generic_parameters(self: TypeDefinition) -> str:
    return ", ".join(gp.name for gp in self.generic_parameters)


def td_generic_fullname(self: TypeDefinition) -> str:
    fullname = generic_strip_suffix(self.fullname)
    parameters = td_format_generic_parameters(self)
    return f"{fullname}[{parameters}]"


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
            self._package[td.namespace] = WinrtModule(td.namespace)

        module = self._package[td.namespace]

        if td.basetype is None or td.basetype == "System.Object" or td.basetype.startswith(("Windows.", "Microsoft.")):
            module.add(Com(td))
        elif td.basetype == "System.MulticastDelegate":
            module.add(Delegate(td))
        elif td.basetype == "System.Enum":
            module.add(Enum(td))
        elif td.basetype == "System.ValueType":
            if td.fields:
                module.add(Struct(td))
            elif td.custom_attributes.has("Windows.Foundation.Metadata.ContractVersionAttribute"):
                module.add(ContractVersion(td))
            else:
                raise NotImplementedError()
        else:
            raise NotImplementedError()


class WinrtModule(Module):
    def add(self, item: ApiItem) -> None:
        assert self.namespace == item.namespace
        assert item.name not in self._items
        self._items[item.name] = item

    def emit_header(self, import_namespaces: set[str]) -> str:
        writer = StringIO()

        writer.write("from __future__ import annotations\n")

        writer.write(f"from {Package.name} import {BASE_EXPORTS_CSV}\n")

        writer.write(f"from {Package.name}._winrt import {WINRT_EXPORTS_CSV}\n")

        if not Package.is_onefile:
            for namespace in sorted(import_namespaces):
                writer.write(f"import {Package.name}.{namespace}\n")

        return writer.getvalue()


class Enum:
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._td.fields[0].enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        type_field, *value_fields = self._td.fields
        writer.write(f"{self._td.name} = {ttype_pytype(type_field.signature)}\n")
        for fd in value_fields:
            writer.write(f"{fd.name}: {self._td.name} = {fd.default_value.value}\n")
        return writer.getvalue()


class Struct:
    def __init__(self, td: TypeDefinition) -> None:
        assert td.fields
        assert not td.nested_types
        assert "SequentialLayout" in td.attributes
        assert not td.custom_attributes.has_winrt_guid()
        assert not any(fd for fd in td.fields if {"Static", "HasDefault"} <= set(td.attributes))
        assert td.layout.packing_size == 0
        self._td = td

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
            writer.write(f"    {fd.name}: {ttype_pytype(fd.signature)}\n")
        return writer.getvalue()


class ContractVersion:
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        return []

    def emit(self) -> str:
        contract_version = self._td.custom_attributes.get_contract_version()
        return f"{self._td.name}: {contract_version.type.name} = {contract_version.value}\n"


class Com:
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._td.enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        if self._td.is_generic:
            generic_parameters = td_format_generic_parameters(self._td)
            classname = generic_strip_suffix(self._td.name)
            base = f"Generic[{generic_parameters}], ComPtr"
        else:
            classname = self._td.name
            base = "ComPtr"
        if self.com_has_classproperty(self._td):
            metaclass = f"_{classname}_Meta_"
            metaclass_args = f", metaclass={metaclass}"
            writer.write(f"class {metaclass}(ComPtr.__class__):\n")
            writer.write("    pass\n")
        else:
            metaclass = ""
            metaclass_args = ""
        writer.write(f"class {classname}({base}{metaclass_args}):\n")
        writer.write(f"    extends: {self._extends()}\n")
        for ii in self._td.interface_implementations:
            if ii.custom_attributes.has_default():
                writer.write(f"    default_interface: {Package.abs_pkg(ii_generic_fullname(ii))}\n")
                break
        writer.write(f"    _classid_ = '{self._td.namespace}.{classname}'\n")
        if self._td.custom_attributes.has_winrt_guid():
            guid = self._td.custom_attributes.get_winrt_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        writer.write(self.winrt_constructor(self._td))
        writer.write(self.winrt_method_definitions(self._td))
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
                writer.write(f"    {metaclass}.{name} = property({getter}, {setter})\n")
            else:
                writer.write(f"    {name} = property({attrs['get']}, {attrs['put']})\n")
        if f"{self._td.namespace}.{classname}" == "Windows.Foundation.IAsyncOperation":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {Package.name}._winrt import IAsyncOperation___await__\n")
            writer.write("        return IAsyncOperation___await__(self)\n")
        elif f"{self._td.namespace}.{classname}" == "Windows.Foundation.IAsyncOperationWithProgress":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {Package.name}._winrt import IAsyncOperation___await__\n")
            writer.write("        return IAsyncOperation___await__(self)\n")
        elif f"{self._td.namespace}.{classname}" == "Windows.Foundation.IAsyncAction":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {Package.name}._winrt import IAsyncAction___await__\n")
            writer.write("        return IAsyncAction___await__(self)\n")
        elif f"{self._td.namespace}.{classname}" == "Windows.Foundation.IAsyncActionWithProgress":
            writer.write("    def __await__(self):\n")
            writer.write(f"        from {Package.name}._winrt import IAsyncAction___await__\n")
            writer.write("        return IAsyncAction___await__(self)\n")
        return writer.getvalue()

    def _extends(self) -> str:
        if self._td.basetype is None:
            # interface
            return Package.abs_pkg("Windows.Win32.System.WinRT.IInspectable")
        elif self._td.basetype == "System.Object":
            # runtime class
            return Package.abs_pkg("Windows.Win32.System.WinRT.IInspectable")
        else:
            return Package.abs_pkg(self._td.basetype)

    @classmethod
    def com_get_interface_for_method(cls, td: TypeDefinition, method_name: str, params: list[str]) -> str:
        for ii in td.interface_implementations:
            com = Package.current[ii.namespace][ii.name]
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
                        return ii_generic_fullname(ii)
        raise KeyError()

    @classmethod
    def com_get_static_for_method(cls, td: TypeDefinition, method_name: str, method_nargs: int) -> str:
        for ca in td.custom_attributes.get_static():
            namespace, name = ca.fixed_arguments[0].value.rsplit(".", 1)
            com = Package.current[namespace][name]
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

    def com_has_classproperty(self, td: TypeDefinition) -> bool:
        for md in td.method_definitions:
            if md.name == ".ctor":
                continue
            is_static = "Static" in md.attributes
            is_special = "SpecialName" in md.attributes
            is_property = md.name.startswith(("get_", "put_"))
            if is_static and is_special and is_property:
                return True
        return False

    @classmethod
    def winrt_method(cls, td: TypeDefinition, md: MethodDefinition, p_vtbl_index: list[int]) -> str:
        writer = StringIO()
        method_name = md.name_overload
        params = ["self"] + md_parameter_names_annotated(md)
        restype = ttype_pytype(md.signature.return_type)
        if td.basetype == "System.MulticastDelegate":
            pass
        elif "Static" in md.attributes:
            writer.write("    @winrt_classmethod\n")
            interface = cls.com_get_static_for_method(td, method_name, len(md.get_parameter_names()))
            params[0] = f"cls: {Package.abs_pkg(interface)}"
        elif "Abstract" not in td.attributes:
            writer.write("    @winrt_mixinmethod\n")
            interface = cls.com_get_interface_for_method(td, method_name, md.get_parameter_names())
            params[0] = f"self: {Package.abs_pkg(interface)}"
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
        com = Package.current[namespace][name]
        if not isinstance(com, Com):
            raise TypeError()
        return len(com._td.method_definitions) + com._count_interface_method()

    def winrt_factorymethod(self, td: TypeDefinition, md: MethodDefinition) -> str:
        writer = StringIO()
        if td.is_generic:
            name = td_generic_fullname(td)
        else:
            name = td.fullname
        params = [f"cls: {Package.abs_pkg(name)}"] + md_parameter_names_annotated(md)
        params_csv = ", ".join(params)
        restype = ttype_pytype(md.signature.return_type)
        writer.write("    @winrt_factorymethod\n")
        writer.write(f"    def {md.name}({params_csv}) -> {restype}: ...\n")
        return writer.getvalue()

    def winrt_activatemethod(self, td: TypeDefinition) -> str:
        writer = StringIO()
        if td.is_generic:
            name = td_generic_fullname(td)
        else:
            name = td.fullname
        writer.write("    @winrt_activatemethod\n")
        writer.write(f"    def CreateInstance(cls) -> {Package.abs_pkg(name)}: ...\n")
        return writer.getvalue()

    def winrt_constructor(self, td: TypeDefinition) -> str:
        writer = StringIO()
        methods = []
        if td.custom_attributes.has_composable():
            ca = td.custom_attributes.get_composable()
            namespace, name = ca.fixed_arguments[0].value.rsplit(".", 1)
            com = Package.current[namespace][name]
            if not isinstance(com, Com):
                raise TypeError()
            factory = com._td
            for md in factory.method_definitions:
                assert md.signature.return_type.fullname == td.fullname
                methods.append(
                    Method(
                        name=md.name_overload,
                        nargs=len(md.get_parameter_names()) - 2,
                        invoke=f"{Package.abs_pkg(td.fullname)}.{md.name_overload}(*args, None, None)",
                        declare=self.winrt_factorymethod(factory, md),
                        default_overload=False,
                    )
                )
        for ca in td.custom_attributes.get_activatable():
            if ca.fixed_arguments[0].type.kind == "Type":
                namespace, name = ca.fixed_arguments[0].value.rsplit(".", 1)
                com = Package.current[namespace][name]
                if not isinstance(com, Com):
                    raise TypeError()
                factory = com._td
                for md in factory.method_definitions:
                    assert md.signature.return_type.fullname == td.fullname
                    methods.append(
                        Method(
                            name=md.name_overload,
                            nargs=len(md.get_parameter_names()),
                            invoke=f"{Package.abs_pkg(td.fullname)}.{md.name_overload}(*args)",
                            declare=self.winrt_factorymethod(factory, md),
                            default_overload=False,
                        )
                    )
            else:
                methods.append(
                    Method(
                        name="CreateInstance",
                        nargs=0,
                        invoke=f"{Package.abs_pkg(td.fullname)}.CreateInstance(*args)",
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
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        yield from self._td.enumerate_dependencies()

    def emit(self) -> str:
        writer = StringIO()
        if self._td.is_generic:
            generic_parameters = td_format_generic_parameters(self._td)
            name = generic_strip_suffix(self._td.name)
            base = f"Generic[{generic_parameters}], MulticastDelegate"
        else:
            name = self._td.name
            base = "MulticastDelegate"
        writer.write(f"class {name}({base}):\n")
        writer.write(f"    extends: {Package.abs_pkg('Windows.Win32.System.Com.IUnknown')}\n")
        if self._td.custom_attributes.has_winrt_guid():
            guid = self._td.custom_attributes.get_winrt_guid()
            writer.write(f"    _iid_ = Guid('{guid}')\n")
        p_vtbl_index = [3]  # count of IUnknown
        for md in self._td.method_definitions:
            if md.name == ".ctor":
                continue
            # FIXME
            writer.write(Com.winrt_method(self._td, md, p_vtbl_index))
        return writer.getvalue()
