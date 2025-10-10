from __future__ import annotations

import asyncio
import inspect
import logging
import sys
import types
import uuid
from collections.abc import Iterable, MutableSequence, Sequence
from contextlib import ExitStack
from ctypes import (
    POINTER,
    Structure,
    _SimpleCData,
    addressof,
    c_void_p,
    cast,
    pointer,
    py_object,
    sizeof,
)
from functools import partial
from typing import Any, Generic, TypeVar, _GenericAlias

if sys.version_info < (3, 9):
    from typing_extensions import Annotated, Tuple, get_args, get_origin  # noqa: F401
else:
    from typing import Annotated, Tuple, get_args, get_origin  # noqa: F401

from . import asyncui
from ._boxing import box_value, unbox_value
from ._bstr import bstr
from ._comerror import ComError
from ._hstr import hstr
from ._win32 import (
    FAILED,
    WINFUNCTYPE,
    Boolean,
    Byte,
    Char,
    ComMethod,
    ComPtr,
    Double,
    Enum,
    Guid,
    Int32,
    Int64,
    Single,
    UInt32,
    UInt64,
    Void,
    VoidPtr,
    WinError,
    commethod,
    easycast,
    get_type_hints,
    windll,
)
from ._win32api import (
    E_FAIL,
    E_NOINTERFACE,
    HRESULT,
    HSTRING,
    PFNGETACTIVATIONFACTORY,
    S_OK,
    BaseTrust,
    CoTaskMemAlloc,
    CoTaskMemFree,
    CreateErrorInfo,
    IActivationFactory,
    IAgileObject,
    ICreateErrorInfo,
    IErrorInfo,
    IInspectable,
    IUnknown,
    RoGetActivationFactory,
    RoOriginateError,
    SetErrorInfo,
    TrustLevel,
)

# TODO: For backword compatibility.  Remove later.
WinRT_String = hstr

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
    hints = get_type_hints(cls)
    if hints["extends"] is None:
        return cls
    # Generic class have multiple base class (Generic[], ComPtr).
    bases = []
    for type_ in cls.__bases__:
        if type_ is ComPtr:
            type_ = hints["extends"]
        bases.append(type_)
    if "implements" in hints:
        bases.extend(get_args(hints["implements"]))
    cls.__bases__ = tuple(bases)
    if "__orig_bases__" in cls.__dict__:
        orig_bases = []
        for type_ in cls.__bases__:
            if type_ is ComPtr:
                type_ = hints["extends"]
            orig_bases.append(type_)
        cls.__orig_bases__ = tuple(orig_bases)
    if "default_interface" in hints:
        cls._default_interface_ = hints["default_interface"]
    return cls


def ComPtr_as(self, cls):
    if cls is str:
        return unbox_value(self)
    elif is_generic_alias(cls):
        iid = _ro_get_parameterized_type_instance_iid(cls)
    elif "_iid_" in cls.__dict__:
        iid = cls._iid_
    elif "_default_interface_" in cls.__dict__:
        iid = cls._default_interface_._iid_
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
    from win32more._vector import Vector
    from win32more.Windows.Foundation import IReference
    from win32more.Windows.Foundation.Collections import IVector

    if type_ is IInspectable:
        if isinstance(obj, str):
            return box_value(obj)
    elif issubclass(_get_origin_or_itself(type_), IVector):
        if isinstance(obj, list):
            return Vector[get_args(type_)[0]](obj)
    elif issubclass(_get_origin_or_itself(type_), IReference):
        # FIXME: Should I check obj is T of IReference[T]?
        if obj is None:
            return IReference(None)
        return box_value(obj).as_(type_)
    elif is_generic_alias(type_):
        # Do not propagate generic type
        return obj
    return easycast(obj, type_)


def generic_get_type_hints(prototype, cls):
    hints = get_type_hints(prototype)
    if is_generic_alias(cls):
        gs = GenericSpecializer.from_generic_alias(cls)
        hints = {key: gs.specialize_parameter(parameter) for key, parameter in hints.items()}
    return hints


class GenericSpecializer:
    def __init__(self, parameter_to_type_map: dict[TypeVar, type]) -> None:
        self._parameter_to_type_map = parameter_to_type_map

    @classmethod
    def from_generic_alias(cls, specialized_generic_alias: _GenericAlias) -> GenericSpecializer:
        parameters = get_origin(specialized_generic_alias).__parameters__
        args = get_args(specialized_generic_alias)
        return GenericSpecializer(dict(zip(parameters, args)))

    def specialize_generic_alias(self, parameterized_generic_alias: _GenericAlias) -> _GenericAlias:
        parameters = get_args(parameterized_generic_alias)
        args = self.specialize_parameters(parameters)
        return get_origin(parameterized_generic_alias)[tuple(args)]

    def specialize_parameters(self, parameters: list[_GenericAlias | TypeVar | type]) -> list[_GenericAlias | type]:
        return [self.specialize_parameter(parameter) for parameter in parameters]

    def specialize_parameter(self, parameter: _GenericAlias | TypeVar | type) -> _GenericAlias | type:
        if is_generic_alias(parameter):
            return self.specialize_generic_alias(parameter)
        elif isinstance(parameter, TypeVar):
            return self._parameter_to_type_map[parameter]
        else:
            return parameter


# types.get_original_bases
def _get_original_bases(cls):
    return cls.__dict__.get("__orig_bases__", cls.__bases__)


def _get_original_class(instance):
    return instance.__dict__.get("__orig_class__", instance.__class__)


def _get_origin_or_itself(cls):
    return get_origin(cls) or cls


def _get_specialized_bases(cls):
    if not is_generic_alias(cls):
        return _get_original_bases(cls)
    gs = GenericSpecializer.from_generic_alias(cls)
    bases = []
    for base in _get_original_bases(_get_origin_or_itself(cls)):
        if get_origin(base) is Generic:
            continue
        bases.append(gs.specialize_parameter(base))
    return bases


# Dummy type for list[T]
class PassArray(Generic[T]):
    def __init__(self, type_, seq, cargs):
        self._type = type_

        if isinstance(seq, Sequence):
            if self._type is hstr:
                self._seq = [hstr(s, own=True) for s in seq]
            else:
                self._seq = seq
            cargs.append(len(self._seq))
            cargs.append((self._type * len(self._seq))(*self._seq))
        else:
            raise TypeError(f"cannot convert {type(seq)} to PassArray[{type_.__name__}]")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class PassArrayCallback:
    def __init__(self, type_, size, ptr, pyargs):
        self._type = type_
        self._size = size
        self._ptr = ptr
        self._lst = []
        for i in range(size):
            if type_ is hstr:
                self._lst.append(str(ptr[i]))
            elif not is_simple_cdata(type_):
                self._lst.append(type_.from_buffer_copy(ptr[i]))
            else:
                self._lst.append(ptr[i])
        pyargs.append(self._lst)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


# Dummy type for list[T]
class FillArray(Generic[T]):
    def __init__(self, type_, seq, cargs):
        self._type = type_

        if isinstance(seq, MutableSequence):
            self._seq = seq
            self._ptr = (type_ * len(seq))()
            cargs.append(len(self._seq))
            cargs.append(self._ptr)
        else:
            raise TypeError(f"cannot convert {type(seq)} to FillArray[{type_.__name__}]")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return

        if self._type is hstr:
            self._seq[:] = [str(s) for s in self._ptr[:]]
            for s in self._ptr[:]:
                s.clear()
        elif is_com_class(self._type):
            self._seq[:] = self._ptr[:]
            for p in self.seq:
                p._own = True
        else:
            self._seq[:] = self._ptr[:]


class FillArrayCallback:
    def __init__(self, type_, size, ptr, pyargs):
        self._type = type_
        self._size = size
        self._ptr = ptr
        self._lst = [None] * size
        pyargs.append(self._lst)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return

        for i, v in enumerate(self._lst):
            if self._type is hstr:
                self._ptr[i] = hstr(v)
            elif is_com_class(self._type):
                if v:
                    v.AddRef()
                self._ptr[i] = v
            else:
                self._ptr[i] = v


# Dummy type for list[T]
class ReceiveArray(Generic[T]):
    def __init__(self, type_, seq, cargs):
        self._type = type_

        if isinstance(seq, MutableSequence):
            self._seq = seq
            self._size = UInt32()
            self._ptr = POINTER(type_)()
            cargs.append(pointer(self._size))
            cargs.append(pointer(self._ptr))
        else:
            raise TypeError(f"cannot convert {type(seq)} to ReceiveArray[{type_.__name__}]")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return

        if self._type is hstr:
            self._seq[:] = [str(s) for s in self._ptr[: self._size.value]]
            for s in self._ptr[: self._size.value]:
                s.clear()
        elif is_com_class(self._type):
            self._seq[:] = [self._type.from_buffer_copy(p) for p in self._ptr[: self._size.value]]
            for p in self._seq:
                p._own = True
        elif not is_simple_cdata(self._type):
            self._seq[:] = [self._type.from_buffer_copy(p) for p in self._ptr[: self._size.value]]
        else:
            self._seq[:] = self._ptr[: self._size.value]
        CoTaskMemFree(self._ptr)


class ReceiveArrayCallback:
    def __init__(self, type_, psize, pptr, pyargs):
        self._type = type_
        self._psize = psize
        self._pptr = pptr
        self._lst = []
        pyargs.append(self._lst)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return
        self.handle_result(self._type, self._psize, self._pptr, self._lst)

    @staticmethod
    def handle_result(type_, psize, pptr, seq):
        if not isinstance(seq, Sequence):
            raise ValueError(f"Sequence is expected: {seq}")

        psize[0] = len(seq)
        ptr = CoTaskMemAlloc(len(seq) * sizeof(type_))
        if not ptr:
            raise WinError()
        pptr[0] = cast(ptr, POINTER(type_))
        for i, v in enumerate(seq):
            if type_ is hstr:
                pptr[0][i] = hstr(v)
            elif is_com_class(type_):
                if v:
                    v.AddRef()
                pptr[0][i] = v
            else:
                pptr[0][i] = v


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
        cls = _get_original_class(this)
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
            self._add_parameter(argtypes, params, name, type_)
        self._add_restype(argtypes, params, restype)
        self.delegate = WINFUNCTYPE(HRESULT, *argtypes)(vtbl_index, prototype.__name__, tuple(params))
        self.restype = restype
        self._prototype = prototype
        self.hints = hints
        self._signature = inspect.signature(prototype)

    def __call__(self, this, *args, **kwargs):
        with ExitStack() as exitstack:
            cargs = []
            pargs = self._signature.bind(None, *args, **kwargs).args[1:]
            for value, type_ in zip(pargs, self.hints.values()):  # >=3.10 strict=True
                self._add_argument(cargs, value, type_, exitstack)
            result = self._add_result(cargs, self.restype, exitstack)
            hr = self.delegate(this, *cargs)
            if FAILED(hr):
                # FIXME: Is restricted error obtained here always associated with this hr?
                raise ComError(hr)
        return self._handle_result(result)

    def _add_parameter(self, argtypes: list[type], params: list[tuple[int, str]], name: str, type_: type) -> None:
        if is_passarray_class(type_):
            argtypes.append(UInt32)
            argtypes.append(POINTER(get_args(type_)[0]))
            params.append((1, f"{name}_length"))
            params.append((1, name))
        elif is_fillarray_class(type_):
            argtypes.append(UInt32)
            argtypes.append(POINTER(get_args(type_)[0]))
            params.append((1, f"{name}_length"))
            params.append((1, name))
        elif is_receivearray_class(type_):
            argtypes.append(POINTER(UInt32))
            argtypes.append(POINTER(POINTER(get_args(type_)[0])))
            params.append((1, f"{name}_length"))
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

    def _add_restype(self, argtypes: list[type], params: list[tuple[int, str]], restype: type) -> None:
        if restype is Void:
            pass
        elif is_receivearray_class(restype):
            argtypes.append(POINTER(UInt32))
            argtypes.append(POINTER(POINTER(get_args(restype)[0])))
            params.append((1, "return_length"))
            params.append((1, "return"))
        elif is_generic_alias(restype):
            argtypes.append(POINTER(get_origin(restype)))
            params.append((1, "return"))
        else:
            argtypes.append(POINTER(restype))
            params.append((1, "return"))

    def _add_argument(self, cargs: list[Any], value: Any, type_: type, exitstack: ExitStack) -> None:
        if is_passarray_class(type_):
            exitstack.enter_context(PassArray(get_args(type_)[0], value, cargs))
        elif is_fillarray_class(type_):
            exitstack.enter_context(FillArray(get_args(type_)[0], value, cargs))
        elif is_receivearray_class(type_):
            exitstack.enter_context(ReceiveArray(get_args(type_)[0], value, cargs))
        elif is_delegate_class(type_):
            cargs.append(MulticastDelegateImpl(type_, value))
        elif is_com_instance(value) and is_com_class(type_):
            cargs.append(value.as_(type_))
        else:
            cargs.append(winrt_easycast(value, type_))

    def _add_result(self, cargs: list[Any], restype: type, exitstack) -> None:
        if self.restype is Void:
            result = None
        elif is_receivearray_class(self.restype):
            result = []
            exitstack.enter_context(ReceiveArray(get_args(self.restype)[0], result, cargs))
        elif is_com_class(self.restype):
            result = self.restype(own=True)
            cargs.append(pointer(result))
        elif self.restype is hstr:
            result = self.restype(own=True)
            cargs.append(pointer(result))
        else:
            result = self.restype()
            cargs.append(pointer(result))
        return result

    def _handle_result(self, result: Any) -> Any:
        from win32more.Windows.Foundation import IReference

        if self.restype is Void:
            return None
        elif issubclass(_get_origin_or_itself(self.restype), IReference):
            if not result:
                return None
            return unbox_value(result)
        elif issubclass(_get_origin_or_itself(self.restype), Enum):
            return result.value
        elif is_com_class(self.restype):
            if not result:
                return None
            return result
        elif self.restype is hstr:
            return str(result)
        elif is_simple_cdata(_get_origin_or_itself(self.restype)):
            return result.value
        return result


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


def is_delegate_class(cls):
    return issubclass(_get_origin_or_itself(cls), MulticastDelegate)


def is_com_class(cls):
    return issubclass(_get_origin_or_itself(cls), ComPtr)


def is_com_instance(obj):
    return isinstance(obj, ComPtr)


def is_passarray_class(cls):
    return issubclass(_get_origin_or_itself(cls), PassArray)


def is_fillarray_class(cls):
    return issubclass(_get_origin_or_itself(cls), FillArray)


def is_receivearray_class(cls):
    return issubclass(_get_origin_or_itself(cls), ReceiveArray)


# check if ptr[0] returns python primitive?
def is_simple_cdata(cls):
    return cls.__base__ is _SimpleCData


class winrt_classmethod:
    def __init__(self, prototype):
        self._prototype = prototype

    def __get__(self, instance, owner=None):
        return types.MethodType(self.__call__, owner)

    def __call__(self, cls, *args, **kwargs):
        hints = get_type_hints(self._prototype)
        factory_class = hints["cls"]
        factory = _ro_get_activation_factory(cls._classid_).as_(factory_class)
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
        return _ro_activate_instance(cls._classid_).as_(cls)

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


def _ro_get_activation_factory(classid: str) -> IActivationFactory:
    factory = IActivationFactory(own=True)
    hr = RoGetActivationFactory(hstr(classid, own=True), IActivationFactory._iid_, factory)
    if FAILED(hr):
        return _get_runtime_activation_factory(classid)
    return factory


def _ro_activate_instance(classid: str) -> IInspectable:
    factory = _ro_get_activation_factory(classid)
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
        except Exception as exc:
            logger.exception(f"Unhandled exception caught: {callback}{args}")
            self._set_error_info(exc)
            return E_FAIL

    def _set_error_info(self, exc):
        info = ICreateErrorInfo(own=True)
        hr = CreateErrorInfo(info)
        if FAILED(hr):
            return
        description = bstr(f"{exc.__class__.__name__}: {exc}")
        if not description:
            return
        hr = info.SetDescription(description)
        if FAILED(hr):
            return
        SetErrorInfo(0, info.as_(IErrorInfo))

    def _winrt_callback_error_check(self, callback, restype, hints, this, *args):
        try:
            self._winrt_callback(callback, restype, hints, this, args)
            return S_OK
        except Exception as exc:
            logger.exception(f"Unhandled exception caught: {callback}{args}")
            self._originate_error(exc)
            return E_FAIL

    def _originate_error(self, exc):
        try:
            msg = hstr(f"{exc.__class__.__name__}: {exc}")
        except OSError:
            return
        RoOriginateError(E_FAIL, msg)

    def _winrt_callback(self, callback, restype, hints, this, args):
        args = list(args)
        with ExitStack() as exitstack:
            pyargs = []
            for type_ in hints.values():
                self._add_argument(type_, args, pyargs, exitstack)
            result = callback(*pyargs)
        self._handle_result(restype, args, result)

    def _add_argument(self, type_: type, args: list[Any], pyargs: list[Any], exitstack) -> None:
        if is_passarray_class(type_):
            exitstack.enter_context(PassArrayCallback(get_args(type_)[0], args.pop(0), args.pop(0), pyargs))
        elif is_fillarray_class(type_):
            exitstack.enter_context(FillArrayCallback(get_args(type_)[0], args.pop(0), args.pop(0), pyargs))
        elif is_receivearray_class(type_):
            exitstack.enter_context(ReceiveArrayCallback(get_args(type_)[0], args.pop(0), args.pop(0), pyargs))
        elif type_ is hstr:
            pyargs.append(str(args.pop(0)))
        else:
            pyargs.append(args.pop(0))

    def _handle_result(self, restype: type, args: list[Any], result: Any) -> Any:
        if restype is Void:
            pass
        elif is_receivearray_class(restype):
            return_length, return_pointer = args
            ReceiveArrayCallback.handle_result(get_args(restype)[0], return_length, return_pointer, result)
        elif restype is hstr:
            return_pointer = args[0]
            return_pointer[0] = hstr(result)
        elif is_com_class(restype):
            return_pointer = args[0]
            if result:
                result.AddRef()
            return_pointer[0] = result
        else:
            return_pointer = args[0]
            return_pointer[0] = result


class ComClass(ComPtr):
    _keep_reference_in_python_world_ = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._iid_vtbls = self._make_iid_vtbls()
        self.value = addressof(self._iid_vtbls[0][1])  # select default interface
        self._refcount = 0
        self.AddRef()
        self._inner = self._compose()

    def _make_iid_vtbls(self) -> list[tuple[Guid, Vtbl]]:
        iid_vtbls = []
        for interface in self._implemented_interfaces():
            iid = self._get_iid(interface)
            vtbl = Vtbl(self, interface)
            iid_vtbls.append((iid, vtbl))
        return iid_vtbls

    def _get_iid(self, interface):
        if is_generic_alias(interface):
            return _ro_get_parameterized_type_instance_iid(interface)
        elif "_iid_" in interface.__dict__:
            return interface.__dict__["_iid_"]
        else:
            raise ValueError("Cannot get iid")

    def _implemented_interfaces(self) -> list[_GenericAlias | type]:
        r = []
        for base in self._enumerate_specialized_bases_recursively(_get_original_class(self)):
            if is_generic_alias(base) and "_piid_" in get_origin(base).__dict__:
                r.append(base)
            elif "_iid_" in base.__dict__:
                r.append(base)
        r.append(IAgileObject)
        r.append(ISelf)
        return r

    def _enumerate_specialized_bases_recursively(self, cls: _GenericAlias | type) -> Iterable[_GenericAlias | type]:
        for base in _get_specialized_bases(cls):
            yield base
            yield from self._enumerate_specialized_bases_recursively(base)

    @classmethod
    def _runtime_class_name(cls) -> str:
        return f"{cls.__module__}.{cls.__qualname__}"

    def _compose(self) -> IInspectable:
        for base in type(self).__mro__:
            # FIXME: ComposableAttribute should be checked.
            if issubclass(base, IInspectable) and "CreateInstance" in base.__dict__:
                inner = IInspectable()
                base.CreateInstance(self, inner)
                return inner
        return None

    def QueryInterface(self, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> HRESULT:
        for iid, vtbl in self._iid_vtbls:
            if riid[0] == iid:
                ppvObject[0] = addressof(vtbl)
                self.AddRef()
                return S_OK
        if self._inner is not None:
            return self._inner.QueryInterface(riid, ppvObject)
        return E_NOINTERFACE

    def AddRef(self) -> UInt32:
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self) -> UInt32:
        self._refcount -= 1
        if self._refcount == 0:
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount: POINTER(UInt32), iids: POINTER(POINTER(Guid))) -> HRESULT:
        iidCount[0] = len(self._iid_vtbls)
        iids[0] = CoTaskMemAlloc(sizeof(VoidPtr) * len(self._iid_vtbls))
        if iids[0] is None:
            return E_FAIL
        for i, (iid, vtbl) in enumerate(self._iid_vtbls):
            iids[0][i] = iid
        return S_OK

    def GetRuntimeClassName(self, className: POINTER(HSTRING)) -> HRESULT:
        className[0] = hstr(self._runtime_class_name())
        return S_OK

    def GetTrustLevel(self, trustLevel: POINTER(TrustLevel)) -> HRESULT:
        trustLevel[0] = BaseTrust
        return S_OK

    # ISelf.GetSelf()
    def GetSelf(self) -> object:
        return self


class ISelf(IUnknown):
    _iid_ = Guid("{18320492-860a-4c7b-ad7c-6cd65c88c09e}")

    @commethod(3)
    def GetSelf(self) -> py_object: ...


class MulticastDelegate(IUnknown):
    pass


class MulticastDelegateImpl(ComClass):
    def __init__(self, interface, callback):
        if not callable(callback):
            raise TypeError(f"cannot convert {type(callback)} to MulticastDelegate")
        self._interface = interface
        self._callback = callback
        super().__init__(own=True)

    def _implemented_interfaces(self):
        return [self._interface, IUnknown, IAgileObject, ISelf]

    def Invoke(self, *args):
        if inspect.iscoroutinefunction(self._callback):
            self._addref(args)
            future = asyncui.create_task(self._callback(*args))
            future.add_done_callback(lambda _: self._release(args))
            return None
        return self._callback(*args)

    def _addref(self, args):
        for obj in args:
            if isinstance(obj, IUnknown) and obj.value:
                obj.AddRef()

    def _release(self, args):
        for obj in args:
            if isinstance(obj, IUnknown) and obj.value:
                obj.Release()


class AwaitableProtocol:
    def __await__(self):
        future = asyncio.get_running_loop().create_future()
        self.Completed = partial(self.__on_completed, future)
        return future.__await__()

    def __on_completed(self, future, asyncInfo, asyncStatus):
        from win32more.Windows.Foundation import AsyncStatus, IAsyncInfo

        if asyncStatus == AsyncStatus.Completed:
            future.get_loop().call_soon_threadsafe(future.set_result, asyncInfo.GetResults())
        elif asyncStatus == AsyncStatus.Error:
            # It seems that restricted error info is built by invoking IAsyncInfo.ErrorCode.
            error = ComError(asyncInfo.as_(IAsyncInfo).ErrorCode.Value)
            future.get_loop().call_soon_threadsafe(future.set_exception, error)
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
        gs = GenericSpecializer.from_generic_alias(_get_original_class(self))
        return gs.specialize_parameters(self.__parameters)

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
        from win32more.Windows.Foundation import IClosable

        self.as_(IClosable).Close()
