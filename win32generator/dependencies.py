from collections.abc import Iterator
from functools import singledispatchmethod

from .metadata import (
    CustomAttributeCollection,
    FieldDefinition,
    InterfaceImplementation,
    MethodDefinition,
    MethodSignature,
    TType,
    TypeDefinition,
)


class Dependencies:
    def __init__(self, data: TypeDefinition | FieldDefinition | MethodDefinition) -> None:
        self._entities: set[str] = set()
        self._pointers: set[str] = set()
        self._systems: set[str] = set()
        self._collect(data)

    def __iter__(self) -> Iterator[str]:
        return iter(self._entities | self._pointers)

    def exclude_pointer(self) -> Iterator[str]:
        return iter(self._entities)

    @singledispatchmethod
    def _collect(self, arg) -> None:
        raise NotImplementedError()

    @_collect.register
    def _(self, ttype: TType, pointer=False) -> None:
        if ttype.kind in ["Pointer", "Reference"]:
            self._collect(ttype.type, True)
        elif ttype.kind in ["Array", "SZArray"]:
            self._collect(ttype.type, pointer)
        elif ttype.kind == "Primitive":
            if ttype.name == "Object":
                pass  # IInspectable
        elif ttype.kind == "Type":
            if ttype.is_nested:
                pass
            elif ttype.namespace == "System":
                self._systems.add(ttype.fullname)
            else:
                self._add(ttype.fullname, pointer)
        elif ttype.kind == "Modified":
            assert ttype.modifier_type.fullname == "System.Runtime.CompilerServices.IsConst"
            self._collect(ttype.unmodified_type, pointer)
        elif ttype.kind == "Generic":
            self._add(ttype.type.fullname, pointer)
            for t in ttype.type_arguments:
                self._collect(t, pointer)
        elif ttype.kind == "GenericParameter":
            pass
        else:
            raise NotImplementedError()

    def _add(self, fullname: str, pointer: bool) -> None:
        if pointer:
            self._pointers.add(fullname)
        else:
            self._entities.add(fullname)

    @_collect.register
    def _(self, td: TypeDefinition) -> None:
        if td.is_winrt:
            if td.basetype is None:
                pass  # IInspectable
            elif td.basetype == "System.Object":
                pass  # IInspectable
            elif td.basetype == "System.MulticastDelegate":
                pass  # IUnknown
            elif td.basetype.startswith(("Windows.", "Microsoft.")):
                self._entities.add(td.basetype)
        else:  # win32
            if td.basetype is None:
                self._entities.add("Windows.Win32.System.Com.IUnknown")
        for ii in td.interface_implementations:
            self._collect(ii)
        for fd in td.fields:
            self._collect(fd)
        for md in td.methods:
            self._collect(md)
        for nested_type in td.nested_types:
            self._collect(nested_type)
        self._collect(td.custom_attributes)

    @_collect.register
    def _(self, ii: InterfaceImplementation) -> None:
        if ii.interface.kind == "TypeReference":
            self._entities.add(ii.interface.type_reference.fullname)
        elif ii.interface.kind == "TypeSpecification":
            self._collect(ii.interface.type_specification.signature)
        else:
            raise NotImplementedError()

    @_collect.register
    def _(self, fd: FieldDefinition) -> None:
        self._collect(fd.signature)

    @_collect.register
    def _(self, md: MethodDefinition) -> None:
        self._collect(md.signature)

    @_collect.register
    def _(self, ms: MethodSignature) -> None:
        self._collect(ms.return_type)
        for t in ms.parameter_types:
            self._collect(t)

    @_collect.register
    def _(self, cac: CustomAttributeCollection) -> None:
        if cac.has_activatable():
            for ca in cac.get_activatable():
                if ca.fixed_arguments[0].type.kind == "Type":
                    self._entities.add(ca.fixed_arguments[0].value)
        if cac.has_static():
            for ca in cac.get_static():
                self._entities.add(ca.fixed_arguments[0].value)
        if cac.has_composable():
            ca = cac.get_composable()
            self._entities.add(ca.fixed_arguments[0].value)
