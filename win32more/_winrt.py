from __future__ import annotations

import asyncio
import inspect
import logging
import sys
import types
import uuid
from ctypes import (
    POINTER,
    WINFUNCTYPE,
    Structure,
    WinError,
    addressof,
    c_void_p,
    cast,
    pointer,
    sizeof,
    wstring_at,
)
from functools import partial
from typing import Generic, TypeVar, _GenericAlias

if sys.version_info < (3, 9):
    from typing_extensions import Annotated, Tuple, get_args, get_origin  # noqa: F401
else:
    from typing import Annotated, Tuple, get_args, get_origin  # noqa: F401

from win32more import (
    FAILED,
    Boolean,
    Byte,
    Char,
    ComMethod,
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
    easycast,
    get_type_hints,
)
from win32more.asyncui import async_callback
from win32more.Windows.Win32.Foundation import (
    E_FAIL,
    E_NOINTERFACE,
    HRESULT,
    S_OK,
)
from win32more.Windows.Win32.System.Com import CoTaskMemAlloc, CoTaskMemFree, IUnknown
from win32more.Windows.Win32.System.WinRT import (
    HSTRING,
    IInspectable,
    RoActivateInstance,
    RoGetActivationFactory,
    WindowsCreateString,
    WindowsDeleteString,
    WindowsGetStringRawBuffer,
)

K = TypeVar("K")
T = TypeVar("T")
V = TypeVar("V")
TProgress = TypeVar("TProgress")
TResult = TypeVar("TResult")
TSender = TypeVar("TSender")

logger = logging.getLogger(__name__)


class event:
    def __init__(self):
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return event_setter(instance, self._name)


class event_setter:
    def __init__(self, instance, name):
        self._instance = instance
        self._name = name

    def __iadd__(self, callback):
        getattr(self._instance, f"add_{self._name}")(callback)


def ComPtr_commit(cls):
    cls._hints_ = get_type_hints(cls)
    if cls._hints_["extends"] is None:
        return cls
    # Generic class have multiple base class (Generic[], ComPtr).
    bases = []
    for type_ in cls.__bases__:
        if type_ is ComPtr:
            type_ = cls._hints_["extends"]
        bases.append(type_)
    if "implements" in cls._hints_:
        bases.extend(get_args(cls._hints_["implements"]))
    cls.__bases__ = tuple(bases)
    return cls


def ComPtr_as(self, cls):
    if cls is str:
        return unbox_value(self)
    elif is_generic_alias(cls):
        iid = _ro_get_parameterized_type_instance_iid(cls)
    elif "_iid_" in cls.__dict__:
        iid = cls._iid_
    elif "default_interface" in cls._hints_:
        iid = cls._hints_["default_interface"]._iid_
    else:
        raise RuntimeError("no _iid_ found")
    instance = cls(own=True)
    hr = self.QueryInterface(pointer(iid), pointer(instance))
    if FAILED(hr):
        raise WinError(hr)
    return instance


ComPtr.__commit__ = classmethod(ComPtr_commit)
ComPtr.as_ = ComPtr_as


def winrt_easycast(obj, type_):
    from win32more._winrtrt import Vector
    from win32more.Windows.Foundation.Collections import IVector

    if type_ is IInspectable:
        if isinstance(obj, str):
            return box_value(obj)
    elif issubclass_generic(type_, IVector):
        if isinstance(obj, list):
            return Vector[get_args(type_)[0]](obj)
    return easycast(obj, type_)


def box_value(value: str) -> IInspectable:
    from win32more.Windows.Foundation import PropertyValue

    if isinstance(value, str):
        return PropertyValue.CreateString(value)
    raise NotImplementedError(f"box_value: {type(value)}")


def unbox_value(value: IInspectable):
    from win32more.Windows.Foundation import IPropertyValue, PropertyType

    property_value = value.as_(IPropertyValue)

    if property_value.Type == PropertyType.Empty:
        return None
    elif property_value.Type == PropertyType.UInt8:
        return property_value.GetUInt8()
    elif property_value.Type == PropertyType.Int16:
        return property_value.GetInt16()
    elif property_value.Type == PropertyType.UInt16:
        return property_value.GetUInt16()
    elif property_value.Type == PropertyType.Int32:
        return property_value.GetInt32()
    elif property_value.Type == PropertyType.UInt32:
        return property_value.GetUInt32()
    elif property_value.Type == PropertyType.Int64:
        return property_value.GetInt64()
    elif property_value.Type == PropertyType.UInt64:
        return property_value.GetUInt64()
    elif property_value.Type == PropertyType.Single:
        return property_value.GetSingle()
    elif property_value.Type == PropertyType.Double:
        return property_value.GetDouble()
    elif property_value.Type == PropertyType.Char16:
        return property_value.GetChar16()
    elif property_value.Type == PropertyType.Boolean:
        return property_value.GetBoolean()
    elif property_value.Type == PropertyType.String:
        return property_value.GetString()
    elif property_value.Type == PropertyType.Inspectable:
        return value
    elif property_value.Type == PropertyType.DateTime:
        return property_value.GetDateTime()
    elif property_value.Type == PropertyType.TimeSpan:
        return property_value.GetTimeSpan()
    elif property_value.Type == PropertyType.Guid:
        return property_value.GetGuid()
    elif property_value.Type == PropertyType.Point:
        return property_value.GetPoint()
    elif property_value.Type == PropertyType.Size:
        return property_value.GetSize()
    elif property_value.Type == PropertyType.Rect:
        return property_value.GetRect()
    elif property_value.Type == PropertyType.UInt8Array:
        r = []
        property_value.GetUInt8Array(r)
        return r
    elif property_value.Type == PropertyType.Int16Array:
        r = []
        property_value.GetInt16Array(r)
        return r
    elif property_value.Type == PropertyType.UInt16Array:
        r = []
        property_value.GetUInt16Array(r)
        return r
    elif property_value.Type == PropertyType.Int32Array:
        r = []
        property_value.GetInt32Array(r)
        return r
    elif property_value.Type == PropertyType.UInt32Array:
        r = []
        property_value.GetUInt32Array(r)
        return r
    elif property_value.Type == PropertyType.Int64Array:
        r = []
        property_value.GetInt64Array(r)
        return r
    elif property_value.Type == PropertyType.UInt64Array:
        r = []
        property_value.GetUInt64Array(r)
        return r
    elif property_value.Type == PropertyType.SingleArray:
        r = []
        property_value.GetSingleArray(r)
        return r
    elif property_value.Type == PropertyType.DoubleArray:
        r = []
        property_value.GetDoubleArray(r)
        return r
    elif property_value.Type == PropertyType.Char16Array:
        r = []
        property_value.GetChar16Array(r)
        return r
    elif property_value.Type == PropertyType.BooleanArray:
        r = []
        property_value.GetBooleanArray(r)
        return r
    elif property_value.Type == PropertyType.StringArray:
        r = []
        property_value.GetStringArray(r)
        return r
    elif property_value.Type == PropertyType.InspectableArray:
        r = []
        property_value.GetInspectableArray(r)
        return r
    elif property_value.Type == PropertyType.DateTimeArray:
        r = []
        property_value.GetDateTimeArray(r)
        return r
    elif property_value.Type == PropertyType.TimeSpanArray:
        r = []
        property_value.GetTimeSpanArray(r)
        return r
    elif property_value.Type == PropertyType.GuidArray:
        r = []
        property_value.GetGuidArray(r)
        return r
    elif property_value.Type == PropertyType.PointArray:
        r = []
        property_value.GetPointArray(r)
        return r
    elif property_value.Type == PropertyType.SizeArray:
        r = []
        property_value.GetSizeArray(r)
        return r
    elif property_value.Type == PropertyType.RectArray:
        r = []
        property_value.GetRectArray(r)
        return r
    # elif property_value.Type == PropertyType.OtherType:
    # elif property_value.Type == PropertyType.OtherTypeArray:
    else:
        raise NotImplementedError(f"unbox_value: {property_value.Type}")


def generic_get_type_hints(prototype, cls):
    hints = get_type_hints(prototype)
    if is_generic_alias(cls):
        hints = generic_solve_parameterized_hints(hints, generic_make_parameter_to_type(cls))
    return hints


def generic_make_parameter_to_type(typed_generic_alias):
    types = get_args(typed_generic_alias)
    parameters = get_origin(typed_generic_alias).__parameters__
    return dict(zip(parameters, types))


def generic_solve_parameterized_hints(parameterized_hints, parameter_to_type):
    solved_hints = {}
    for k, parameter in parameterized_hints.items():
        solved_hints[k] = generic_solve_parameter(parameter, parameter_to_type)
    return solved_hints


def generic_solve_parameterized_generic_alias(parameterized_generic_alias, parameter_to_type):
    args = []
    for parameter in get_args(parameterized_generic_alias):
        args.append(generic_solve_parameter(parameter, parameter_to_type))
    return get_origin(parameterized_generic_alias)[tuple(args)]


def generic_solve_parameter(parameter, parameter_to_type):
    if is_generic_alias(parameter):
        return generic_solve_parameterized_generic_alias(parameter, parameter_to_type)
    elif isinstance(parameter, TypeVar):
        return parameter_to_type[parameter]
    else:
        return parameter


# Dummy type for list[T]
class PassArray(Generic[T]):
    def __init__(self, type_, lst):
        self.type_ = type_
        if self.type_ is WinRT_String:
            self.lst = [WinRT_String(s, own=True) for s in lst]
        else:
            self.lst = lst
        self.length = UInt32(len(self.lst))
        self.ptr = (self.type_ * len(self.lst))(*self.lst)

    def later(self):
        # to keep self.lst instance
        pass


class PassArrayCallback:
    def __init__(self, type_, size, ptr):
        self._type = type
        self._size = size
        self._ptr = ptr
        self._lst = []
        for i in range(size):
            if type_ is WinRT_String:
                self._lst.append(_windows_create_string(ptr[i]))
            else:
                self._lst.append(ptr[i])

    def later(self):
        pass


# Dummy type for list[T]
class FillArray(Generic[T]):
    def __init__(self, type_, lst):
        self.type_ = type_
        self.lst = lst
        self.length = UInt32(len(lst))
        self.ptr = (type_ * len(lst))()

    def later(self):
        if self.type_ is WinRT_String:
            self.lst[:] = [s.strvalue for s in self.ptr[:]]
            for s in self.ptr[:]:
                s.clear()
        elif is_com_class(self.type_):
            self.lst[:] = self.ptr[:]
            for p in self.lst:
                p._own = True
        else:
            self.lst[:] = self.ptr[:]


class FillArrayCallback:
    def __init__(self, type_, size, ptr):
        self._type = type_
        self._size = size
        self._ptr = ptr
        self._lst = [None] * size

    def later(self):
        for i, v in enumerate(self._lst):
            if self._type is WinRT_String:
                self._ptr[i] = WinRT_String(v)
            else:
                self._ptr[i] = v


# Dummy type for list[T]
class ReceiveArray(Generic[T]):
    def __init__(self, type_, lst):
        self.type_ = type_
        self.lst = lst
        self.length = UInt32()
        self.ptr = POINTER(type_)()

    def later(self):
        if self.type_ is WinRT_String:
            self.lst[:] = [s.strvalue for s in self.ptr[: self.length.value]]
            for s in self.ptr[: self.length.value]:
                s.clear()
        elif is_com_class(self.type_):
            self.lst[:] = self.ptr[: self.length.value]
            for p in self.lst:
                p._own = True
        else:
            self.lst[:] = self.ptr[: self.length.value]
        CoTaskMemFree(self.ptr)


class ReceiveArrayCallback:
    def __init__(self, type_, psize, pptr):
        self._type = type
        self._psize = psize
        self._pptr = pptr
        self._lst = []

    def later(self):
        self._psize[0] = len(self._lst)
        ptr = CoTaskMemAlloc(len(self._lst) * sizeof(self._type))
        if not ptr:
            raise WinError()
        self._pptr[0] = ptr
        for i, v in enumerate(self._lst):
            if self._type is WinRT_String:
                self._pptr[0][i] = WinRT_String(v)
            else:
                self._pptr[0][i] = v


# FIXME: Not work for array and struct entry.
class WinRT_String(HSTRING):
    def __init__(self, obj=None, own=False):
        if obj is None:
            hs = HSTRING(0)
        elif isinstance(obj, HSTRING):
            hs = obj
        elif isinstance(obj, String):
            hs = _windows_create_string(obj.value)
        elif isinstance(obj, str):
            hs = _windows_create_string(obj)
        else:
            raise ValueError(obj)
        # https://github.com/python/cpython/issues/73456
        # super().__init__(hs.value)
        self.value = hs.value
        self._own = own

    def __del__(self):
        if self and getattr(self, "_own", False):
            self.clear()

    def clear(self):
        if self.value:
            hr = WindowsDeleteString(self)
            if FAILED(hr):
                raise WinError(hr)
            self.value = 0

    @classmethod
    def from_param(cls, obj):
        if isinstance(obj, String):
            return cls(obj, own=True)
        elif isinstance(obj, str):
            return cls(obj, own=True)
        else:
            return cls(obj, own=False)

    @property
    def strvalue(self):
        return _windows_get_string_raw_buffer(self)

    def __ctypes_from_outparam__(self):
        return self.strvalue


class WinrtMethod:
    def __init__(self, prototype, vtbl_index):
        self._prototype = prototype
        self._vtbl_index = vtbl_index
        self._generic_delegate = {}

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return types.MethodType(self.__call__, instance)

    def __call__(self, this, *args, **kwargs):
        cls = getattr(this, "__orig_class__", this.__class__)
        generic_args = get_args(cls)
        if generic_args not in self._generic_delegate:
            self._generic_delegate[generic_args] = WinrtMethodCall(self._prototype, self._vtbl_index, cls)
        return self._generic_delegate[generic_args](this, *args, **kwargs)


class WinrtMethodCall:
    def __init__(self, prototype, vtbl_index, cls):
        hints = generic_get_type_hints(prototype, cls)
        restype = hints.pop("return")

        argtypes = []
        params = []
        for name, type_ in hints.items():
            if is_passarray_class(type_):
                argtypes.append(UInt32)
                params.append((1, f"{name}_length"))
                argtypes.append(POINTER(get_args(type_)[0]))
                params.append((1, name))
            elif is_fillarray_class(type_):
                argtypes.append(UInt32)
                params.append((1, f"{name}_length"))
                argtypes.append(POINTER(get_args(type_)[0]))
                params.append((1, name))
            elif is_receivearray_class(type_):
                argtypes.append(POINTER(UInt32))
                params.append((1, f"{name}_length"))
                argtypes.append(POINTER(POINTER(get_args(type_)[0])))
                params.append((1, name))
            elif is_delegate_class(type_):
                argtypes.append(MulticastDelegateImpl)
                params.append((1, name))
            elif is_generic_alias(type_):
                argtypes.append(get_origin(type_))
                params.append((1, name))
            else:
                argtypes.append(type_)
                params.append((1, name))

        if restype is not Void:
            if is_receivearray_class(restype):
                argtypes.append(POINTER(UInt32))
                params.append((1, "return_length"))
                argtypes.append(POINTER(POINTER(get_args(restype)[0])))
                params.append((1, "return"))
            elif is_generic_alias(restype):
                argtypes.append(POINTER(get_origin(restype)))
                params.append((1, "return"))
            else:
                argtypes.append(POINTER(restype))
                params.append((1, "return"))

        self.delegate = WINFUNCTYPE(HRESULT, *argtypes)(vtbl_index, prototype.__name__, tuple(params))
        self.restype = restype
        self.hints = hints
        self.hints.update({i: v for i, v in enumerate(hints.values())})

    def __call__(self, this, *args, **kwargs):
        calllater = []
        cargs, ckwargs = self.make_args(args, kwargs, calllater)
        if self.restype is Void:
            result = None
        elif is_receivearray_class(self.restype):
            result = ReceiveArray(get_args(self.restype)[0], [])
            ckwargs["return_length"] = pointer(result.length)
            ckwargs["return"] = pointer(result.ptr)
        elif is_com_class(self.restype):
            result = self.restype(own=True)
            ckwargs["return"] = pointer(result)
        elif self.restype is WinRT_String:
            result = self.restype(own=True)
            ckwargs["return"] = pointer(result)
        else:
            result = self.restype()
            ckwargs["return"] = pointer(result)
        hr = self.delegate(this, *cargs, **ckwargs)
        if FAILED(hr):
            raise WinError(hr)
        for callback in calllater:
            callback()
        return self.make_result(result)

    def make_args(self, args, kwargs, calllater):
        cargs = []
        for k, v in enumerate(args):
            if k in self.hints:
                if isinstance(v, list) and is_passarray_class(self.hints[k]):
                    szarray = PassArray(get_args(self.hints[k])[0], v)
                    cargs.append(szarray.length)
                    cargs.append(szarray.ptr)
                    calllater.append(szarray.later)
                elif isinstance(v, list) and is_fillarray_class(self.hints[k]):
                    szarray = FillArray(get_args(self.hints[k])[0], v)
                    cargs.append(szarray.length)
                    cargs.append(szarray.ptr)
                    calllater.append(szarray.later)
                elif isinstance(v, list) and is_receivearray_class(self.hints[k]):
                    szarray = ReceiveArray(get_args(self.hints[k])[0], v)
                    cargs.append(pointer(szarray.length))
                    cargs.append(pointer(szarray.ptr))
                    calllater.append(szarray.later)
                elif callable(v) and is_delegate_class(self.hints[k]):
                    cargs.append(MulticastDelegateImpl(self.hints[k], v))
                elif is_com_instance(v) and is_com_class(self.hints[k]):
                    cargs.append(v.as_(self.hints[k]))
                else:
                    cargs.append(winrt_easycast(v, self.hints[k]))
            else:
                cargs.append(v)
        ckwargs = {}
        for k, v in kwargs.items():
            if k in self.hints:
                if isinstance(v, list) and is_passarray_class(self.hints[k]):
                    szarray = PassArray(get_args(self.hints[k])[0], v)
                    ckwargs[f"{k}_length"] = szarray.length
                    ckwargs[k] = szarray.ptr
                    calllater.append(szarray.later)
                elif isinstance(v, list) and is_fillarray_class(self.hints[k]):
                    szarray = FillArray(get_args(self.hints[k])[0], v)
                    ckwargs[f"{k}_length"] = szarray.length
                    ckwargs[k] = szarray.ptr
                    calllater.append(szarray.later)
                elif isinstance(v, list) and is_receivearray_class(self.hints[k]):
                    szarray = ReceiveArray(get_args(self.hints[k])[0], v)
                    ckwargs[f"{k}_length"] = pointer(szarray.length)
                    ckwargs[k] = pointer(szarray.ptr)
                    calllater.append(szarray.later)
                elif callable(v) and is_delegate_class(self.hints[k]):
                    ckwargs[k] = MulticastDelegateImpl(self.hints[k], v)
                elif is_com_instance(v) and is_com_class(self.hints[k]):
                    ckwargs[k] = v.as_(self.hints[k])
                else:
                    ckwargs[k] = winrt_easycast(v, self.hints[k])
            else:
                ckwargs[k] = v
        return cargs, ckwargs

    def make_result(self, result):
        if self.restype is Void:
            return None
        elif is_receivearray_class(self.restype):
            result.later()
            return result.lst
        return result.__ctypes_from_outparam__()


def winrt_commethod(vtbl_index):
    def decorator(prototype):
        return WinrtMethod(prototype, vtbl_index)

    return decorator


class winrt_mixinmethod:
    def __init__(self, prototype):
        self._prototype = prototype

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return types.MethodType(self.__call__, instance)

    def __call__(self, instance, *args, **kwargs):
        hints = get_type_hints(self._prototype)
        interface_instance = instance.as_(hints["self"])
        return getattr(interface_instance, self._prototype.__name__)(*args, **kwargs)

    def argcount(self):
        return len(self._prototype.__annotations__) - 2


# Cls[T]?
def is_generic_alias(cls):
    return isinstance(cls, _GenericAlias)


# Cls[T]()?
def is_generic_instance(obj):
    return isinstance(obj, Generic)


def issubclass_generic(cls, type_):
    if is_generic_alias(cls):
        return issubclass(get_origin(cls), type_)
    return issubclass(cls, type_)


def is_delegate_class(cls):
    if is_generic_alias(cls):
        cls = get_origin(cls)
    return issubclass(cls, MulticastDelegate)


def is_com_class(cls):
    if is_generic_alias(cls):
        cls = get_origin(cls)
    return issubclass(cls, ComPtr)


def is_com_instance(obj):
    return isinstance(obj, ComPtr)


def is_passarray_class(cls):
    if is_generic_alias(cls):
        cls = get_origin(cls)
    return issubclass(cls, PassArray)


def is_fillarray_class(cls):
    if is_generic_alias(cls):
        cls = get_origin(cls)
    return issubclass(cls, FillArray)


def is_receivearray_class(cls):
    if is_generic_alias(cls):
        cls = get_origin(cls)
    return issubclass(cls, ReceiveArray)


class winrt_classmethod:
    def __init__(self, prototype):
        self._prototype = prototype

    def __get__(self, instance, owner=None):
        return types.MethodType(self.__call__, owner)

    def __call__(self, cls, *args, **kwargs):
        hints = get_type_hints(self._prototype)
        factory_class = hints["cls"]
        factory = _ro_get_activation_factory(cls._classid_, factory_class)
        return getattr(factory, self._prototype.__name__)(*args, **kwargs)

    def argcount(self):
        return len(self._prototype.__annotations__) - 2


def winrt_factorymethod(prototype):
    return winrt_classmethod(prototype)


class winrt_activatemethod:
    def __init__(self, prototype):
        self._prototype = prototype

    def __get__(self, instance, owner=None):
        return types.MethodType(self.__call__, owner)

    def __call__(self, cls):
        return _ro_activate_instance(cls._classid_, cls)

    def argcount(self):
        return 0


class winrt_overload:
    def __init__(self, func: winrt_mixinmethod | winrt_classmethod | winrt_activatemethod) -> None:
        self.funcs = [func]

    def register(self, func: winrt_mixinmethod | winrt_classmethod | winrt_activatemethod):
        self.funcs.append(func)
        return self

    def __get__(self, instance, owner=None):
        if instance is None:
            return types.MethodType(self._call_classmethod, owner)
        else:
            return types.MethodType(self._call_method, instance)

    def _call_classmethod(self, cls, *args, **kwargs):
        for func in self.funcs:
            if isinstance(func, (winrt_classmethod, winrt_activatemethod)) and len(args) == func.argcount():
                return func(cls, *args, **kwargs)
        raise ValueError("no matched method")

    def _call_method(self, instance, *args, **kwargs):
        for func in self.funcs:
            if isinstance(func, winrt_mixinmethod) and len(args) == func.argcount():
                return func(instance, *args, **kwargs)
        raise ValueError("no matched method")


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
    factory = factory_class(own=True)
    hr = RoGetActivationFactory(hs, factory_class._iid_, factory)
    WindowsDeleteString(hs)
    if FAILED(hr):
        raise WinError(hr)
    return factory


def _ro_activate_instance(classid: str, cls: type[T]) -> T:
    hs = _windows_create_string(classid)
    instance = cls(own=True)
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
    if cls is IInspectable:
        return "cinterface(IInspectable)"
    elif isinstance(cls, _GenericAlias):
        piid_guid = str(cls._piid_)
        args = ";".join(_get_type_signature(arg) for arg in get_args(cls))
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


class Vtbl(Structure):
    _fields_ = [("lpvtbl", POINTER(c_void_p))]

    def __init__(self, owner, interface):
        self._owner = owner
        self._interface = interface
        self._keep_reference_in_python_world_ = []
        self.lpvtbl = self._make_lpvtbl()

    def _make_lpvtbl(self):
        methods = self._interface_methods()
        vtbl_size = max(method._vtbl_index for method in methods) + 1
        lpvtbl = (c_void_p * vtbl_size)()
        for method in methods:
            if isinstance(method, WinrtMethod):
                lpvtbl[method._vtbl_index] = self._make_thunk_winrt(method)
            else:
                lpvtbl[method._vtbl_index] = self._make_thunk_com(method)
        return lpvtbl

    def _interface_methods(self):
        if sys.version_info < (3, 10) and is_generic_alias(self._interface):
            interface = get_origin(self._interface)
        else:
            interface = self._interface
        methods = []
        for name in dir(interface):
            if isinstance(getattr(interface, name), (ComMethod, WinrtMethod)):
                methods.append(getattr(interface, name))
        return methods

    def _make_thunk_com(self, method):
        hints = generic_get_type_hints(method._prototype, self._interface)
        restype = hints.pop("return")
        argtypes = [self._make_allocator(t) for t in hints.values()]
        closure = partial(self._com_callback_error_check, getattr(self._owner, method._prototype.__name__))
        thunk = WINFUNCTYPE(restype, c_void_p, *argtypes)(closure)
        self._keep_reference_in_python_world_.append(thunk)
        return cast(thunk, c_void_p)

    def _make_thunk_winrt(self, method):
        hints = generic_get_type_hints(method._prototype, self._interface)
        restype = hints.pop("return")
        argtypes = []
        for type_ in hints.values():
            if is_passarray_class(type_):
                argtypes.append(UInt32)
                argtypes.append(POINTER(get_args(type_)[0]))
            elif is_fillarray_class(type_):
                argtypes.append(UInt32)
                argtypes.append(POINTER(get_args(type_)[0]))
            elif is_receivearray_class(type_):
                argtypes.append(POINTER(UInt32))
                argtypes.append(POINTER(POINTER(get_args(type_)[0])))
            else:
                argtypes.append(self._make_allocator(type_))
        if restype is Void:
            pass
        elif is_receivearray_class(restype):
            argtypes.append(POINTER(UInt32))
            argtypes.append(POINTER(POINTER(get_args(restype)[0])))
        elif is_generic_alias(restype):
            argtypes.append(POINTER(get_origin(restype)))
        else:
            argtypes.append(POINTER(restype))
        closure = partial(
            self._winrt_callback_error_check, getattr(self._owner, method._prototype.__name__), restype, hints
        )
        thunk = WINFUNCTYPE(HRESULT, c_void_p, *argtypes)(closure)
        self._keep_reference_in_python_world_.append(thunk)
        return cast(thunk, c_void_p)

    # allocate winrt runtime class without constructor.
    def _make_allocator(self, t):
        if is_generic_alias(t) or issubclass(t, ComPtr):
            return type(c_void_p)("Allocator", (c_void_p,), {"__new__": lambda _: t(own=False)})
        return t

    def _com_callback_error_check(self, callback, this, *args):
        try:
            return callback(*args)
        except Exception:
            logger.exception(f"Unhandled exception caught: {callback}{args}")
            # FIXME: How to return error for IUnknown.AddRef(), IUnknown.Release()
            return E_FAIL

    def _winrt_callback_error_check(self, callback, restype, hints, this, *args):
        try:
            self._winrt_callback(callback, restype, hints, this, *args)
            return S_OK
        except Exception:
            logger.exception(f"Unhandled exception caught: {callback}{args}")
            return E_FAIL

    def _winrt_callback(self, callback, restype, hints, this, *args):
        calllater = []

        if restype is Void:
            pass
        elif is_receivearray_class(restype):
            *args, return_length, return_pointer = args
        else:
            *args, return_pointer = args

        i = 0
        pyargs = []
        for type_ in hints.values():
            if is_passarray_class(type_):
                szarray = PassArrayCallback(get_args(type_)[0], args[i], args[i + 1])
                pyargs.append(szarray._lst)
                calllater.append(szarray.later)
                i += 2
            elif is_fillarray_class(type_):
                szarray = FillArrayCallback(get_args(type_)[0], args[i], args[i + 1])
                pyargs.append(szarray._lst)
                calllater.append(szarray.later)
                i += 2
            elif is_receivearray_class(type_):
                szarray = ReceiveArrayCallback(get_args(type_)[0], args[i], args[i + 1])
                pyargs.append(szarray._lst)
                calllater.append(szarray.later)
                i += 2
            elif type_ is WinRT_String:
                pyargs.append(_windows_get_string_raw_buffer(args[i]))
                i += 1
            else:
                pyargs.append(args[i])
                i += 1

        r = callback(*pyargs)

        for later in calllater:
            later()

        if restype is Void:
            if r is not None:
                raise ValueError(f"{r} cannot be treated as Void")
        elif is_receivearray_class(restype):
            if not isinstance(r, list):
                raise ValueError(f"list is expected: {r}")
            # FIXME: if len(r) == 0: p = 0 ?
            p = CoTaskMemAlloc(sizeof(c_void_p) * len(r))
            if not p:
                raise WinError()
            type_ = get_args(restype)[0]
            return_length[0] = len(r)
            return_pointer[0] = cast(p, POINTER(type_))
            if type_ is WinRT_String:
                for i, o in enumerate(r):
                    return_pointer[0][i] = WinRT_String(o, own=False)
            else:
                for i, o in enumerate(r):
                    return_pointer[0][i] = o
        elif restype is WinRT_String:
            return_pointer[0] = WinRT_String(r, own=False)
        else:
            return_pointer[0] = r


class MulticastDelegate(IUnknown):
    pass


class MulticastDelegateImpl(ComPtr):
    _keep_reference_in_python_world_ = {}

    def __init__(self, interface, callback):
        super().__init__(own=True)
        if is_generic_alias(interface):
            self._iid_ = _ro_get_parameterized_type_instance_iid(interface)
        else:
            self._iid_ = interface._iid_
        if inspect.iscoroutinefunction(callback):
            self._callback = async_callback(callback)
        else:
            self._callback = callback
        self._vtbl = Vtbl(self, interface)
        self.value = addressof(self._vtbl)
        self._refcount = 0
        self.AddRef()

    def QueryInterface(self, riid, ppvObject):
        if riid[0] == IUnknown._iid_:
            ppvObject[0] = addressof(self._vtbl)
            self.AddRef()
            return S_OK
        elif riid[0] == self._iid_:
            ppvObject[0] = addressof(self._vtbl)
            self.AddRef()
            return S_OK
        else:
            return E_NOINTERFACE

    def AddRef(self):
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self):
        self._refcount -= 1
        if self._refcount == 0:
            self._comobj.comptr = None
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def Invoke(self, *args):
        return self._callback(*args)


class AwaitableProtocol:
    def __await__(self):
        future = asyncio.get_event_loop().create_future()
        self.Completed = partial(self.__on_completed, future)
        return future.__await__()

    def __on_completed(self, future, asyncInfo, asyncStatus):
        from win32more.Windows.Foundation import AsyncStatus, IAsyncInfo

        if asyncStatus == AsyncStatus.Completed:
            future.get_loop().call_soon_threadsafe(future.set_result, asyncInfo.GetResults())
        elif asyncStatus == AsyncStatus.Error:
            future.get_loop().call_soon_threadsafe(
                future.set_exception, WinError(asyncInfo.as_(IAsyncInfo).ErrorCode.Value)
            )
        elif asyncStatus == AsyncStatus.Canceled:
            future.get_loop().call_soon_threadsafe(future.cancel)
        else:
            assert False, "unreachable"


class IterableProtocol:
    def __class_getitem__(cls, key):
        return cls

    def __iter__(self):
        iterator = self.First()
        while iterator.HasCurrent:
            yield iterator.Current
            iterator.MoveNext()


class SequenceProtocol:
    def __class_getitem__(cls, key):
        return cls

    def __len__(self):
        return self.Size

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]
        elif isinstance(index, int):
            if index < 0:
                index += len(self)
            if index < 0 or len(self) <= index:
                raise IndexError("list index out of range")
            return self.GetAt(index)
        else:
            raise TypeError(f"list indices must be integers or slices, not {type(index).__name__}")


class MappingProtocol:
    def __class_getitem__(cls, key):
        classdict = dict(cls.__dict__)
        classdict["_MappingProtocol__parameters"] = key
        return type("MappingProtocol", (), classdict)

    def __args(self):
        if not is_generic_instance(self):
            return self.__parameters
        parameter_to_type = generic_make_parameter_to_type(self.__orig_class__)
        args = []
        for parameter in self.__parameters:
            args.append(generic_solve_parameter(parameter, parameter_to_type))
        return args

    def __iterator(self):
        from win32more.Windows.Foundation.Collections import IIterable, IKeyValuePair

        args = self.__args()
        iterable = self.as_(IIterable[IKeyValuePair[args[0], args[1]]])
        for pair in iterable:
            yield pair.Key, pair.Value

    def __iter__(self):
        yield from self.keys()

    def __len__(self):
        return self.Size

    def __getitem__(self, key):
        if not self.HasKey(key):
            raise KeyError(key)
        return self.Lookup(key)

    def __contains__(self, key):
        return self.HasKey(key)

    def items(self):
        for k, v in self.__iterator():
            yield k, v

    def keys(self):
        for k, v in self.__iterator():
            yield k

    def values(self):
        for k, v in self.__iterator():
            yield v

    def get(self, key, default=None):
        if not self.HasKey(key):
            return default
        return self.Lookup(key)

    def __eq__(self, other):
        return dict(self.items()) == dict(other.items())


# IClosable
class ContextManagerProtocol:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.Close()
