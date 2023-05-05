from __future__ import annotations

import uuid
from ctypes import POINTER, WINFUNCTYPE, WinError, c_void_p, cast, pointer, wstring_at
from typing import Generic, TypeVar, _GenericAlias

from Windows import (
    FAILED,
    Boolean,
    Byte,
    Char,
    ComPtr,
    Double,
    Guid,
    Int32,
    Int64,
    Single,
    String,
    UInt32,
    UInt64,
    Void,
    c_char_p_no,
    c_wchar_p_no,
    easycast,
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


class WinRT_String(HSTRING):
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
        return _windows_create_string(obj)

    def __ctypes_from_outparam__(self):
        return _windows_get_string_raw_buffer(self)


class WinrtMethod:
    def __init__(self, this, prototype, factory):
        hints = get_type_hints(prototype)
        if is_generic_instance(this):
            hints = self.map_generic_types(this, hints)
        restype = hints.pop("return")
        argtypes = list(hints.values())
        types = [HRESULT] + argtypes
        params = [(1, name) for name in hints.keys()]
        if restype is not Void:
            params.append((1, "return"))
            if is_generic_class(restype):
                return_type = POINTER(restype.__origin__)
            else:
                return_type = POINTER(restype)
            types.append(return_type)
        self.hints = hints
        self.hints.update({i: v for i, v in enumerate(argtypes)})
        self.delegate = factory(prototype.__name__, types, tuple(params))
        self.restype = restype

    def map_generic_types(self, this, hints):
        generic_args = this.__orig_class__.__args__
        generic_parameters = this.__class__.__parameters__
        param_to_type = {generic_parameters[i]: t for i, t in enumerate(generic_args)}
        return {k: param_to_type[t] if isinstance(t, TypeVar) else t for k, t in hints.items()}

    def __call__(self, this, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        cargs, ckwargs = self.make_args(args, kwargs)
        if self.restype is Void:
            result = None
        else:
            result = self.restype()
            ckwargs["return"] = pointer(result)
        hr = self.delegate(this, *cargs, **ckwargs)
        if FAILED(hr):
            raise WinError(hr)
        return self.make_result(result, _as_intptr)

    def make_args(self, args, kwargs):
        cargs = [easycast(v, self.hints[i]) if i in self.hints else v for i, v in enumerate(args)]
        ckwargs = {k: easycast(v, self.hints[k]) if k in self.hints else v for k, v in kwargs.items()}
        return cargs, ckwargs

    def make_result(self, result, _as_intptr):
        if result is None:
            return None
        elif _as_intptr:
            return cast(result, c_void_p).value
        elif type(result) is c_char_p_no or type(result) is c_wchar_p_no:
            return result.value
        return result.__ctypes_from_outparam__()


def winrt_commethod(vtbl_index):
    def factory(name, types, params):
        return WINFUNCTYPE(*types)(vtbl_index, name, params)

    def decorator(prototype):
        delegate_generic = {}

        def wrapper(self, *args, **kwargs):
            if is_generic_instance(self):
                generic_args = self.__orig_class__.__args__
            else:
                generic_args = None
            if generic_args not in delegate_generic:
                delegate_generic[generic_args] = WinrtMethod(self, prototype, factory)
            return delegate_generic[generic_args](self, *args, **kwargs)

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
            iid = _ro_get_parameterized_type_instance_iid(interface_class)
        else:
            iid = interface_class._iid_
        hr = self.QueryInterface(iid, interface)
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
        factory = _ro_get_activation_factory(cls._classid_, factory_class)
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
        factory = _ro_get_activation_factory(cls._classid_, factory_class)
        try:
            return getattr(factory, prototype.__name__)(*args, **kwargs)
        finally:
            factory.Release

    return wrapper


def winrt_activatemethod(prototype):
    @classmethod
    def wrapper(cls):
        return _ro_activate_instance(cls._classid_, cls)

    return wrapper


def _windows_create_string(s: str) -> HSTRING:
    hs = HSTRING()
    hr = WindowsCreateString(s, len(s), hs)
    if FAILED(hr):
        raise WinError(hr)
    return hs


def _windows_get_string_raw_buffer(hs: HSTRING) -> str:
    length = UInt32()
    bufaddr = WindowsGetStringRawBuffer(hs, length, _as_intptr=True)
    return wstring_at(bufaddr, length.value)


def _ro_get_activation_factory(classid: str, factory_class: type[T]) -> T:
    hs = _windows_create_string(classid)
    factory = factory_class()
    hr = RoGetActivationFactory(hs, factory_class._iid_, factory)
    WindowsDeleteString(hs)
    if FAILED(hr):
        raise WinError(hr)
    return factory


def _ro_activate_instance(classid: str, cls: type[T]) -> T:
    hs = _windows_create_string(classid)
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
        piid_guid = str(cls._iid_)
        args = ";".join(_get_type_signature(arg) for arg in cls.__args__)
        return f"pinterface({piid_guid};{args})"
    elif issubclass(cls, ComPtr) and "_iid_" in cls.__dict__:
        return str(cls._iid_)
    elif issubclass(cls, ComPtr):
        default_interface = cls._hints_["default_interface"]
        args = _get_type_signature(default_interface)
        return f"rc({cls._classid_};{args})"
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
