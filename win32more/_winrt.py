from __future__ import annotations

import asyncio
import inspect
import sys
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
    py_object,
    wstring_at,
)
from typing import Generic, TypeVar, _GenericAlias

if sys.version_info < (3, 9):
    from typing_extensions import Annotated  # noqa: F401
else:
    from typing import Annotated  # noqa: F401

if sys.version_info < (3, 8):
    from typing_extensions import get_args, get_origin
else:
    from typing import get_args, get_origin

import win32more.Windows.Win32.System.Com
from win32more import (
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
from win32more.asyncui import async_callback
from win32more.Windows.Win32.Foundation import (
    E_NOINTERFACE,
    HRESULT,
    S_OK,
)
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
        win32more.Windows.Win32.System.Com.CoTaskMemFree(self.ptr)


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
        if self.value != 0:
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
    def __init__(self, cls, prototype, factory):
        hints = generic_get_type_hints(prototype, cls)
        restype = hints.pop("return")

        types = [HRESULT]
        params = []
        for name, type_ in hints.items():
            if is_passarray_class(type_):
                types.append(UInt32)
                params.append((1, f"{name}_length"))
                types.append(POINTER(get_args(type_)[0]))
                params.append((1, name))
            elif is_fillarray_class(type_):
                types.append(UInt32)
                params.append((1, f"{name}_length"))
                types.append(POINTER(get_args(type_)[0]))
                params.append((1, name))
            elif is_receivearray_class(type_):
                types.append(POINTER(UInt32))
                params.append((1, f"{name}_length"))
                types.append(POINTER(POINTER(get_args(type_)[0])))
                params.append((1, name))
            elif is_generic_alias(type_):
                types.append(get_origin(type_))
                params.append((1, name))
            else:
                types.append(type_)
                params.append((1, name))

        if restype is not Void:
            if is_receivearray_class(restype):
                types.append(POINTER(UInt32))
                params.append((1, "return_length"))
                types.append(POINTER(POINTER(get_args(restype)[0])))
                params.append((1, "return"))
            elif is_generic_alias(restype):
                types.append(POINTER(get_origin(restype)))
                params.append((1, "return"))
            else:
                types.append(POINTER(restype))
                params.append((1, "return"))

        self.delegate = factory(prototype.__name__, types, tuple(params))
        self.restype = restype
        self.hints = hints
        self.hints.update({i: v for i, v in enumerate(hints.values())})

    def __call__(self, this, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        calllater = []
        cargs, ckwargs = self.make_args(args, kwargs, calllater)
        if self.restype is Void:
            result = None
        elif is_receivearray_class(self.restype):
            szarray = ReceiveArray(get_args(self.restype)[0], [])
            ckwargs["return_length"] = pointer(szarray.length)
            ckwargs["return"] = pointer(szarray.ptr)
            result = szarray
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
        return self.make_result(result, _as_intptr)

    def make_args(self, args, kwargs, calllater):
        cargs = []
        for k, v in enumerate(args):
            if k in self.hints:
                if isinstance(v, list) and is_passarray_class(self.hints[k]):
                    szarray = PassArray(get_args(self.hints[k])[0], v)
                    cargs.append(szarray.length)
                    cargs.append(szarray.ptr)
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
                    cargs.append(self.hints[k](own=True).CreateInstance(v))
                elif is_com_instance(v) and is_com_class(self.hints[k]):
                    cargs.append(v.as_(self.hints[k]))
                else:
                    cargs.append(easycast(v, self.hints[k]))
            else:
                cargs.append(v)
        ckwargs = {}
        for k, v in kwargs.items():
            if k in self.hints:
                if isinstance(v, list) and is_passarray_class(self.hints[k]):
                    szarray = PassArray(get_args(self.hints[k])[0], v)
                    ckwargs[f"{k}_length"] = szarray.length
                    ckwargs[k] = szarray.ptr
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
                    ckwargs[k] = self.hints[k](own=True).CreateInstance(v)
                elif is_com_instance(v) and is_com_class(self.hints[k]):
                    ckwargs[k] = v.as_(self.hints[k])
                else:
                    ckwargs[k] = easycast(v, self.hints[k])
            else:
                ckwargs[k] = v
        return cargs, ckwargs

    def make_result(self, result, _as_intptr):
        if result is None:
            return None
        elif is_receivearray_class(self.restype):
            result.later()
            return result.lst
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
                generic_args = get_args(self.__orig_class__)
                cls = self.__orig_class__
            else:
                generic_args = None
                cls = self.__class__
            if generic_args not in delegate_generic:
                delegate_generic[generic_args] = WinrtMethod(cls, prototype, factory)
            return delegate_generic[generic_args](self, *args, **kwargs)

        wrapper.prototype = prototype

        return wrapper

    return decorator


def winrt_mixinmethod(prototype):
    def wrapper(self, *args, **kwargs):
        hints = get_type_hints(prototype)
        interface_class = hints["self"]
        interface = interface_class(own=True)
        if is_generic_alias(interface_class):
            iid = _ro_get_parameterized_type_instance_iid(interface_class)
        else:
            iid = interface_class._iid_
        hr = self.QueryInterface(iid, interface)
        if FAILED(hr):
            raise WinError(hr)
        return getattr(interface, prototype.__name__)(*args, **kwargs)

    wrapper.prototype = prototype

    return wrapper


# Cls[T]?
def is_generic_alias(cls):
    return isinstance(cls, _GenericAlias)


# Cls[T]()?
def is_generic_instance(obj):
    return isinstance(obj, Generic)


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


def _classmethod(func):
    cm = classmethod(func)
    if sys.version_info < (3, 10):
        cm.__wrapped__ = func
    return cm


def winrt_classmethod(prototype):
    @_classmethod
    def wrapper(cls, *args, **kwargs):
        hints = get_type_hints(prototype)
        factory_class = hints["cls"]
        factory = _ro_get_activation_factory(cls._classid_, factory_class)
        return getattr(factory, prototype.__name__)(*args, **kwargs)

    wrapper.prototype = prototype

    return wrapper


def winrt_factorymethod(prototype):
    return winrt_classmethod(prototype)


def winrt_activatemethod(prototype):
    @_classmethod
    def wrapper(cls):
        return _ro_activate_instance(cls._classid_, cls)

    wrapper.prototype = prototype

    return wrapper


class winrt_overload:
    def __init__(self, func):
        self.funcs = [func]

    def register(self, func):
        self.funcs.append(func)
        return self

    def __get__(self, obj, cls=None):
        def _classmethod(*args):
            for func in self.funcs:
                if isinstance(func, classmethod) and len(args) == func.prototype.__code__.co_argcount - 1:
                    return func.__get__(obj, cls)(*args)
            raise ValueError("no matched method")

        def _method(*args):
            for func in self.funcs:
                if not isinstance(func, classmethod) and len(args) == func.prototype.__code__.co_argcount - 1:
                    return func.__get__(obj, cls)(*args)
            raise ValueError("no matched method")

        if obj is None:
            return _classmethod
        else:
            return _method


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
        piid_guid = str(cls._iid_)
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


class MulticastDelegateImpl(Structure):
    _fields_ = [("lpvtbl", POINTER(c_void_p)), ("comptr", py_object), ("restype", py_object)]

    def __init__(self, comptr, cls, invoke_prototype):
        self.lpvtbl = (c_void_p * 4)()
        self.lpvtbl[0] = cast(self.QueryInterface, c_void_p)
        self.lpvtbl[1] = cast(self.AddRef, c_void_p)
        self.lpvtbl[2] = cast(self.Release, c_void_p)
        self.lpvtbl[3] = cast(self._make_trampoline(cls, invoke_prototype), c_void_p)
        self.comptr = py_object(comptr)

    def _make_trampoline(self, cls, invoke_prototype):
        hints = generic_get_type_hints(invoke_prototype, cls)
        self.restype = hints.pop("return")
        argtypes = [self._make_allocator(t) for t in hints.values()]
        if self.restype is not Void:
            restype = self.restype
            if is_generic_alias(restype):
                restype = get_origin(restype)
            argtypes.append(POINTER(restype))
        factory = WINFUNCTYPE(HRESULT, c_void_p, *argtypes)
        return factory(self.Invoke)

    # allocate winrt runtime class without constructor.
    def _make_allocator(self, t):
        if is_generic_alias(t) or issubclass(t, ComPtr):
            return type(c_void_p)("Allocator", (c_void_p,), {"__new__": lambda _: t(own=False)})
        return t

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(Guid), POINTER(c_void_p))
    def QueryInterface(this, riid, ppvObject):
        self = cast(this, POINTER(MulticastDelegateImpl)).contents
        return self.comptr.QueryInterface(riid, ppvObject)

    @WINFUNCTYPE(UInt32, c_void_p)
    def AddRef(this):
        self = cast(this, POINTER(MulticastDelegateImpl)).contents
        return self.comptr.AddRef()

    @WINFUNCTYPE(UInt32, c_void_p)
    def Release(this):
        self = cast(this, POINTER(MulticastDelegateImpl)).contents
        return self.comptr.Release()

    # @WINFUNCTYPE(...)
    @staticmethod
    def Invoke(this, *args):
        self = cast(this, POINTER(MulticastDelegateImpl)).contents
        if self.restype is not Void:
            *args, return_pointer = args
        r = self.comptr._Invoke(*args)
        if self.restype is not Void:
            return_pointer.contents = r
        else:
            if r is not None:
                raise ValueError(f"{r} cannot be treated as Void")
        return 0


class MulticastDelegate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown

    _keep_reference_in_python_world_ = {}

    # FIXME: How to get GenericClass[T].__args__ in class method?
    # @classmethod
    def CreateInstance(self, callback):
        if is_generic_instance(self):
            cls = self.__orig_class__
            self._iid_ = _ro_get_parameterized_type_instance_iid(cls)
        else:
            cls = self.__class__
        if inspect.iscoroutinefunction(callback):
            self._callback = async_callback(callback)
        else:
            self._callback = callback
        self._comobj = MulticastDelegateImpl(self, cls, self.__class__.Invoke)
        self.value = addressof(self._comobj)
        self._refcount = 0
        self.AddRef()
        return self

    def QueryInterface(self, riid, ppvObject):
        if str(riid.contents) == str(self._iid_):
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        elif str(riid.contents) == "{00000000-0000-0000-c000-000000000046}":  # IUnknown
            ppvObject.contents.value = self.value
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

    def _Invoke(self, *args):
        return self._callback(*args)


AsyncStatus_Started = 0
AsyncStatus_Completed = 1
AsyncStatus_Canceled = 2
AsyncStatus_Error = 3


class _Async__await__:
    def __init__(self, iasync):
        self._future = asyncio.get_event_loop().create_future()
        iasync.Completed = self.on_completed
        # to keep reference
        self._future.add_done_callback(lambda future: (self, iasync))

    def on_completed(self, asyncInfo, asyncStatus):
        from win32more.Windows.Foundation import IAsyncInfo

        if asyncStatus.value == AsyncStatus_Completed:
            self._future.get_loop().call_soon_threadsafe(self._future.set_result, asyncInfo.GetResults())
        elif asyncStatus.value == AsyncStatus_Error:
            self._future.get_loop().call_soon_threadsafe(
                self._future.set_exception, WinError(asyncInfo.as_(IAsyncInfo).ErrorCode.Value)
            )
        elif asyncStatus.value == AsyncStatus_Canceled:
            self._future.get_loop().call_soon_threadsafe(self._future.cancel)
        else:
            assert False, "unreachable"

    def __await__(self):
        return self._future.__await__()


def IAsyncOperation___await__(self):
    return _Async__await__(self).__await__()


def IAsyncAction___await__(self):
    return _Async__await__(self).__await__()
