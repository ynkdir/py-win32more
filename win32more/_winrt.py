from __future__ import annotations

import asyncio
import re
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
    from typing_extensions import Annotated
else:
    from typing import Annotated

if sys.version_info < (3, 8):
    from typing_extensions import get_args
else:
    from typing import get_args

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


def generic_get_type_hints(cls, prototype, include_extras=False, use_generic_alias=False):
    hints = get_type_hints(prototype, include_extras=include_extras)
    if is_generic_alias(cls):
        hints = generic_map_types(cls, hints, use_generic_alias)
    return hints


def generic_map_types(generic_alias, hints, use_generic_alias=False):
    generic_args = generic_alias.__args__
    generic_parameters = generic_alias.__origin__.__parameters__
    param_to_type = dict(zip(generic_parameters, generic_args))
    newhints = {}
    for k, t in hints.items():
        if is_generic_alias(t):
            newhints[k] = generic_map_class(t, param_to_type, use_generic_alias)
        else:
            newhints[k] = param_to_type.get(t, t)
    return newhints


def generic_map_class(generic_alias, param_to_type, use_generic_alias=False):
    args = []
    for t in generic_alias.__args__:
        if is_generic_alias(t):
            args.append(generic_map_class(t, param_to_type))
        else:
            args.append(param_to_type.get(t, t))
    if use_generic_alias:
        return generic_alias.__origin__[tuple(args)]
    else:
        return generic_alias.__origin__


class SZArray(Generic[T]):
    def __init__(self, array=None):
        if array:
            self._array = array
            self._length = UInt32(len(array))
            self._contents = cast(array, c_void_p)
        else:
            self._array = None
            self._length = UInt32(0)
            self._contents = c_void_p(0)

    @property
    def _type_(self):
        return self.__orig_class__.__args__[0]

    @property
    def length(self):
        return self._length.value

    @property
    def contents(self):
        return cast(self._contents, POINTER(self._type_))

    def __getitem__(self, i):
        return self.contents[i]

    def __setitem__(self, i, value):
        self.contents[i] = value


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
            hr = WindowsDeleteString(self)
            if FAILED(hr):
                raise WinError(hr)

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
        hints = generic_get_type_hints(cls, prototype)
        hints_extra = generic_get_type_hints(cls, prototype, include_extras=True)
        restype = hints.pop("return")

        types = [HRESULT]
        params = []
        for name, type_ in hints.items():
            if is_szarray_class(type_):
                if "Out" in get_args(hints_extra[name]):
                    types.append(POINTER(UInt32))
                    params.append((1, f"{name}_length"))
                    types.append(POINTER(c_void_p))
                    params.append((1, name))
                else:
                    types.append(UInt32)
                    params.append((1, f"{name}_length"))
                    types.append(c_void_p)
                    params.append((1, name))
            else:
                types.append(type_)
                params.append((1, name))

        if restype is not Void:
            if is_szarray_class(restype):
                types.append(POINTER(UInt32))
                params.append((1, "return_length"))
                types.append(POINTER(c_void_p))
                params.append((1, "return"))
            elif is_generic_alias(restype):
                types.append(POINTER(restype.__origin__))
                params.append((1, "return"))
            else:
                types.append(POINTER(restype))
                params.append((1, "return"))

        self.delegate = factory(prototype.__name__, types, tuple(params))
        generic_hints = generic_get_type_hints(cls, prototype, use_generic_alias=True)
        self.restype = generic_hints.pop("return")
        self.generic_hints = generic_hints
        self.generic_hints.update({i: v for i, v in enumerate(generic_hints.values())})

    def __call__(self, this, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        cargs, ckwargs = self.make_args(args, kwargs)
        if self.restype is Void:
            result = None
        elif is_szarray_class(self.restype):
            result = self.restype()
            ckwargs["return_length"] = pointer(result._length)
            ckwargs["return"] = pointer(result._contents)
        elif is_com_class(self.restype):
            result = self.restype(own=True)
            ckwargs["return"] = pointer(result)
        else:
            result = self.restype()
            ckwargs["return"] = pointer(result)
        hr = self.delegate(this, *cargs, **ckwargs)
        if FAILED(hr):
            raise WinError(hr)
        return self.make_result(result, _as_intptr)

    def make_args(self, args, kwargs):
        cargs = []
        for k, v in enumerate(args):
            if k in self.generic_hints:
                if isinstance(v, SZArray):
                    cargs.append(v._length)
                    cargs.append(v._contents)
                elif callable(v) and is_delegate_class(self.generic_hints[k]):
                    cargs.append(self.generic_hints[k](own=True).CreateInstance(v))
                elif is_com_instance(v) and is_com_class(self.generic_hints[k]):
                    cargs.append(v.as_(self.generic_hints[k]))
                else:
                    cargs.append(easycast(v, self.generic_hints[k]))
            else:
                cargs.append(v)
        ckwargs = {}
        for k, v in kwargs.items():
            if k in self.generic_hints:
                if isinstance(v, SZArray):
                    ckwargs[f"{k}_length"] = v._length
                    ckwargs[k] = v._contents
                if callable(v) and is_delegate_class(self.generic_hints[k]):
                    ckwargs[k] = self.generic_hints[k](own=True).CreateInstance(v)
                elif is_com_instance(v) and is_com_class(self.generic_hints[k]):
                    ckwargs[k] = v.as_(self.generic_hints[k])
                else:
                    ckwargs[k] = easycast(v, self.generic_hints[k])
            else:
                ckwargs[k] = v
        return cargs, ckwargs

    def make_result(self, result, _as_intptr):
        if result is None:
            return None
        elif isinstance(result, SZArray):
            return result
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
        # FIXME: Workaround for overload method.
        method_name = prototype.__name__
        m = re.match(r"^(.*)_\d$", method_name)
        if m:
            method_name = m.group(1)
        return getattr(interface, method_name)(*args, **kwargs)

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
        cls = cls.__origin__
    return issubclass(cls, MulticastDelegate)


def is_com_class(cls):
    if is_generic_alias(cls):
        cls = cls.__origin__
    return issubclass(cls, ComPtr)


def is_com_instance(obj):
    return isinstance(obj, ComPtr)


def is_szarray_class(cls):
    if is_generic_alias(cls):
        cls = cls.__origin__
    return issubclass(cls, SZArray)


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
        hints = generic_get_type_hints(cls, invoke_prototype)
        self.restype = hints.pop("return")
        argtypes = [(self._make_allocator(t) if isinstance(t, ComPtr) else t) for t in hints.values()]
        if self.restype is not Void:
            restype = self.restype
            if is_generic_alias(restype):
                restype = restype.__origin__
            argtypes.append(POINTER(restype))
        factory = WINFUNCTYPE(HRESULT, c_void_p, *argtypes)
        return factory(self.Invoke)

    # allocate winrt runtime class without constructor.
    def _make_allocator(cls):
        return type(c_void_p)("Allocator", (c_void_p,), {"__new__": lambda _: cls(own=False)})

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
    def CreateInstance(self, _callback):
        if is_generic_instance(self):
            cls = self.__orig_class__
            self._iid_ = _ro_get_parameterized_type_instance_iid(cls)
        else:
            cls = self.__class__
        self._callback = _callback
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


def IAsyncOperation___await__(self):
    event = asyncio.Event()
    # FIXME: Seems to be not required to call asyncInfo.Release().  Where is documentation.
    self.Completed = lambda asyncInfo, asyncStatus: event.set()
    yield from event.wait().__await__()
    r = self.GetResults()
    return r


def IAsyncAction___await__(self):
    event = asyncio.Event()
    self.Completed = lambda asyncInfo, asyncStatus: event.set()
    yield from event.wait().__await__()
