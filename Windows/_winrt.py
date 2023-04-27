from __future__ import annotations

import uuid
from ctypes import POINTER, WINFUNCTYPE, WinError, c_void_p, wstring_at
from typing import Generic, TypeVar, _GenericAlias

from Windows import (
    FAILED,
    Boolean,
    Byte,
    Char,
    Double,
    Guid,
    Int32,
    Int64,
    IntPtr,
    Single,
    UInt32,
    UInt64,
    get_type_hints,
)
from Windows.Win32.Foundation import HRESULT
from Windows.Win32.System.WinRT import (
    HSTRING,
    RoActivateInstance,
    RoGetActivationFactory,
    WindowsCreateString,
    WindowsDeleteString,
    WindowsGetStringRawBuffer,
)

T = TypeVar("T")

class WinRT_String(IntPtr):  # HSTRING
    def __del__(self):
        if self:
            hr = WindowsDeleteString(self)
            if FAILED(hr):
                raise WinError(hr)

    @classmethod
    def from_param(cls, obj):
        if isinstance(obj, str):
            pass
        elif isinstance(obj, String):
            obj = obj.value
        else:
            raise TypeError()
        value = cls()
        hr = WindowsCreateString(obj, len(obj), value)
        if FAILED(hr):
            raise WinError(hr)
        return value

    def __ctypes_from_outparam__(self):
        length = UInt32()
        bufaddr = WindowsGetStringRawBuffer(self, length, _as_intptr=True)
        return wstring_at(bufaddr, length.value)


def errcheck_return(hr, func, args):
    if FAILED(hr):
        raise WinError(hr)
    return args


def errcheck_void(hr, func, args):
    if FAILED(hr):
        raise WinError(hr)
    return None


def winrt_commethod(vtbl_index):
    def factory(name, types, params):
        return WINFUNCTYPE(*types)(vtbl_index, name, params)

    def decorator(prototype):
        delegate_generic = {}

        def wrapper(self, *args, **kwargs):
            nonlocal delegate_generic
            if is_generic_instance(self):
                targs = self.__orig_class__.__args__
            else:
                targs = None
            if targs in delegate_generic:
                delegate = delegate_generic[targs]
            else:
                hints = get_type_hints(prototype)
                return_ = hints.pop("return")
                params = [(1, name) for name in hints.keys()]
                type_hints = list(hints.values())
                if is_generic_instance(self):
                    tparams = self.__class__.__parameters__
                    tmap = {tparams[i]: targs[i] for i in range(len(targs))}
                    if isinstance(return_, TypeVar):
                        return_ = tmap[return_]
                    for i, t in enumerate(type_hints):
                        if isinstance(t, TypeVar):
                            type_hints[i] = tmap[t]
                types = [HRESULT] + type_hints
                if return_ is None:
                    errcheck = errcheck_void
                else:
                    params.append((2, "return"))
                    if is_generic_class(return_):

                        class GenericReturnHelper(c_void_p):
                            def __ctypes_from_outparam__(self):
                                return return_(self.value)

                        types.append(POINTER(GenericReturnHelper))
                    else:
                        types.append(POINTER(return_))
                    errcheck = errcheck_return
                delegate_generic[targs] = factory(prototype.__name__, types, tuple(params))
                delegate_generic[targs].errcheck = errcheck
                delegate = delegate_generic[targs]
            return delegate(self, *args, **kwargs)

        return wrapper

    return decorator


def winrt_mixinmethod(prototype):
    interface_class = None

    def wrapper(self, *args, **kwargs):
        nonlocal interface_class
        if interface_class is None:
            hints = get_type_hints(prototype)
            interface_class = hints["self"]
        interface = interface_class()
        if is_generic_class(interface_class):
            guid = _ro_get_parameterized_type_instance_iid(interface_class)
        else:
            guid = interface_class.Guid
        hr = self.QueryInterface(guid, interface)
        if FAILED(hr):
            raise WinError(hr)
        try:
            return getattr(interface, prototype.__name__)(*args, **kwargs)
        finally:
            interface.Release()

    return wrapper


# Cls[T]?
def is_generic_class(cls):
    return isinstance(cls, _GenericAlias)


# Cls[T]()?
def is_generic_instance(obj):
    return isinstance(obj, Generic)


def winrt_classmethod(prototype):
    factory_class = None

    @classmethod
    def wrapper(cls, *args, **kwargs):
        nonlocal factory_class
        if factory_class is None:
            hints = get_type_hints(prototype)
            factory_class = hints["cls"]
        factory = _winrt_get_activation_factory(cls.ClassId, factory_class)
        try:
            return getattr(factory, prototype.__name__)(*args, **kwargs)
        finally:
            factory.Release

    return wrapper


def winrt_factorymethod(prototype):
    factory_class = None

    @classmethod
    def wrapper(cls, *args, **kwargs):
        nonlocal factory_class
        if factory_class is None:
            hints = get_type_hints(prototype)
            factory_class = hints["cls"]
        factory = _winrt_get_activation_factory(cls.ClassId, factory_class)
        try:
            return getattr(factory, prototype.__name__)(*args, **kwargs)
        finally:
            factory.Release

    return wrapper


def winrt_activatemethod(prototype):
    @classmethod
    def wrapper(cls):
        return _winrt_activate_instance(cls.ClassId, cls)

    return wrapper


def _winrt_create_string(s: str):
    hs = HSTRING()
    hr = WindowsCreateString(s, len(s), hs)
    if FAILED(hr):
        raise WinError(hr)
    return hs


def _winrt_get_activation_factory(classid: str, factory_class: type[T]) -> T:
    hs = _winrt_create_string(classid)
    factory = factory_class()
    hr = RoGetActivationFactory(hs, factory_class.Guid, factory)
    WindowsDeleteString(hs)
    if FAILED(hr):
        raise WinError(hr)
    return factory


def _winrt_activate_instance(classid: str, cls: type[T]) -> T:
    hs = _winrt_create_string(classid)
    instance = cls()
    hr = RoActivateInstance(hs, instance)
    WindowsDeleteString(hs)
    if FAILED(hr):
        raise WinError(hr)
    return instance


# https://learn.microsoft.com/en-us/uwp/winrt-cref/winrt-type-system
#
# signature_octets => guid_to_octets(wrt_pinterface_namespace) string_to_utf8_octets(ptype_instance_signature)
#         wrt_pinterface_namespace => "11f47ad5-7b73-42c0-abae-878b1e16adee"
#         ptype_instance_signature => pinterface_instance_signature | pdelegate_instance_ signature
#         pinterface_instance_signature => "pinterface(" piid_guid  ";" args ")"
#         pdelegate_instance_signature => "pinterface(" piid_guid ";" args ")"
#         piid_guid => guid
#         args => arg | arg ";" args
#         arg => type_signature
#         type_signature => base_type_identifer | com_interface_signature | interface_signature | delegate_signature  | interface_group_signature | runtime_class_signature | struct_signature | enum_signature | pinterface_instance_signature | pdelegate_instance_signature
#         com_interface_signature => "cinterface(IInspectable)"
#         base_type_identifier is defined below
#         interface_signature => guid
#         interface_group_signature => "ig(" interface_group_name ";" default_interface ")"
#         runtime_class_signature => "rc(" runtime_class_name ";" default_interface ")"
#         default_interface => type_signature
#         struct_signature => "struct(" struct_name ";" args ")"
#         enum_signature => "enum(" enum_name ";" enum_underlying_type ")"
#         enum_underlying_type => type_signature
#         delegate_signature => "delegate(" guid ")"
#         guid => "{" dashed_hex "}"
#         dashed_hex is the format that uuidgen writes in when passed no arguments.
#             dashed_hex => hex{8} "-" hex{4} "-" hex{4} "-" hex{4} "-" hex{12}
#             hex => [0-9a-f]
def _ro_get_parameterized_type_instance_iid(ga: _GenericAlias) -> Guid:
    wrt_pinterface_namespace = uuid.UUID("{11f47ad5-7b73-42c0-abae-878b1e16adee}")
    ptype_instance_signature = _get_type_signature(ga)
    return Guid(uuid.uuid5(wrt_pinterface_namespace, ptype_instance_signature))


# FIXME: not completed
def _get_type_signature(cls) -> str:
    if isinstance(cls, _GenericAlias):
        piid_guid = str(cls.Guid)
        args = ";".join(_get_type_signature(arg) for arg in cls.__args__)
        return f"pinterface({piid_guid};{args})"
    elif issubclass(cls, c_void_p):
        return str(cls.Guid)
    elif issubclass(cls, WinRT_String):
        return "string"
    elif issubclass(cls, Char):
        return "c2"
    elif issubclass(cls, Int32):
        return "i4"
    elif issubclass(cls, Int64):
        return "i8"
    elif issubclass(cls, Byte):
        return "u1"
    elif issubclass(cls, UInt32):
        return "u4"
    elif issubclass(cls, UInt64):
        return "u8"
    elif issubclass(cls, Single):
        return "f4"
    elif issubclass(cls, Double):
        return "f8"
    elif issubclass(cls, Boolean):
        return "b1"
    elif issubclass(cls, Guid):
        return "g16"
    else:
        raise NotImplementedError()

