from __future__ import annotations

import uuid
from ctypes import cast
from typing import _GenericAlias, get_args

from ._hstr import hstr
from ._win32 import (
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
    UInt32,
    UInt64,
    WinError,
    windll,
)
from ._win32api import (
    PFNGETACTIVATIONFACTORY,
    IActivationFactory,
    IInspectable,
    RoGetActivationFactory,
)


def ro_get_activation_factory(classid: str) -> IActivationFactory:
    factory = IActivationFactory(own=True)
    hr = RoGetActivationFactory(hstr(classid, own=True), IActivationFactory._iid_, factory)
    if FAILED(hr):
        return _get_runtime_activation_factory(classid)
    return factory


def ro_activate_instance(classid: str) -> IInspectable:
    factory = ro_get_activation_factory(classid)
    instance = IInspectable(own=True)
    hr = factory.ActivateInstance(instance)
    if FAILED(hr):
        raise WinError(hr)
    return instance


# cppwinrt: base.h
def _get_runtime_activation_factory(classid: str) -> IActivationFactory:
    name = classid
    while "." in name:
        name, _ = name.rsplit(".", 1)
        dllname = name + ".dll"

        try:
            DllGetActivationFactory = cast(windll[dllname].DllGetActivationFactory, PFNGETACTIVATIONFACTORY)
        except AttributeError:
            continue

        factory = IActivationFactory(own=True)
        hr = DllGetActivationFactory(hstr(classid, own=True), factory)
        if FAILED(hr):
            continue
        return factory

    raise WinError(-2147024770)  # HRESULT_FROM_WIN32(ERROR_MOD_NOT_FOUND)


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
def ro_get_parameterized_type_instance_iid(ga: _GenericAlias) -> Guid:
    wrt_pinterface_namespace = uuid.UUID("{11f47ad5-7b73-42c0-abae-878b1e16adee}")
    ptype_instance_signature = _get_type_signature(ga)
    return Guid(uuid.uuid5(wrt_pinterface_namespace, ptype_instance_signature))


# FIXME: not completed
def _get_type_signature(cls) -> str:
    if cls is IInspectable:
        return "cinterface(IInspectable)"
    elif isinstance(cls, _GenericAlias):
        piid_guid = str(cls._piid_)
        args = ";".join(_get_type_signature(arg) for arg in get_args(cls))
        return f"pinterface({piid_guid};{args})"
    elif issubclass(cls, ComPtr):
        if "_iid_" in cls.__dict__:
            return str(cls._iid_)
        elif "_default_interface_" in cls.__dict__:
            default_interface = cls._default_interface_
            args = _get_type_signature(default_interface)
            return f"rc({cls._classid_};{args})"
        else:
            raise RuntimeError("no _iid_ found")
    elif issubclass(cls, hstr):
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
