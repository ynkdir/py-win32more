from __future__ import annotations

import logging
import sys
from collections.abc import Iterable
from contextlib import ExitStack
from ctypes import POINTER, Structure, addressof, c_void_p, cast, py_object, sizeof
from functools import partial
from typing import Any, _GenericAlias

if sys.version_info < (3, 9):
    from typing_extensions import get_args, get_origin
else:
    from typing import get_args, get_origin

from . import _winrt
from ._bstr import bstr
from ._hstr import hstr
from ._win32 import FAILED, WINFUNCTYPE, ComMethod, ComPtr, Guid, UInt32, Void, VoidPtr, commethod
from ._win32api import (
    E_FAIL,
    E_NOINTERFACE,
    HRESULT,
    HSTRING,
    S_OK,
    BaseTrust,
    CoTaskMemAlloc,
    CreateErrorInfo,
    IAgileObject,
    ICreateErrorInfo,
    IErrorInfo,
    IInspectable,
    IUnknown,
    RoOriginateError,
    SetErrorInfo,
    TrustLevel,
)

logger = logging.getLogger(__name__)


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
        if _winrt.is_generic_alias(interface):
            return _winrt._ro_get_parameterized_type_instance_iid(interface)
        elif "_iid_" in interface.__dict__:
            return interface.__dict__["_iid_"]
        else:
            raise ValueError("Cannot get iid")

    def _implemented_interfaces(self) -> list[_GenericAlias | type]:
        r = []
        for base in self._enumerate_specialized_bases_recursively(_winrt._get_original_class(self)):
            if _winrt.is_generic_alias(base) and "_piid_" in get_origin(base).__dict__:
                r.append(base)
            elif "_iid_" in base.__dict__:
                r.append(base)
        r.append(IAgileObject)
        r.append(ISelf)
        return r

    def _enumerate_specialized_bases_recursively(self, cls: _GenericAlias | type) -> Iterable[_GenericAlias | type]:
        for base in _winrt._get_specialized_bases(cls):
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
            if isinstance(method, _winrt.WinrtMethod):
                lpvtbl[method._vtbl_index] = self._make_thunk_winrt(method)
            else:
                lpvtbl[method._vtbl_index] = self._make_thunk_com(method)
        return lpvtbl

    def _interface_methods(self):
        if sys.version_info < (3, 10) and _winrt.is_generic_alias(self._interface):
            interface = get_origin(self._interface)
        else:
            interface = self._interface
        methods = []
        for name in dir(interface):
            if isinstance(getattr(interface, name), (ComMethod, _winrt.WinrtMethod)):
                methods.append(getattr(interface, name))
        return methods

    def _make_thunk_com(self, method):
        hints = _winrt.generic_get_type_hints(method._prototype, self._interface)
        restype = hints.pop("return")
        argtypes = [self._make_allocator(t) for t in hints.values()]
        closure = partial(self._com_callback_error_check, getattr(self._owner, method._prototype.__name__))
        thunk = WINFUNCTYPE(restype, c_void_p, *argtypes)(closure)
        self._keep_reference_in_python_world_.append(thunk)
        return cast(thunk, c_void_p)

    def _make_thunk_winrt(self, method):
        hints = _winrt.generic_get_type_hints(method._prototype, self._interface)
        restype = hints.pop("return")
        argtypes = []
        for type_ in hints.values():
            if _winrt.is_passarray_class(type_):
                argtypes.append(UInt32)
                argtypes.append(POINTER(get_args(type_)[0]))
            elif _winrt.is_fillarray_class(type_):
                argtypes.append(UInt32)
                argtypes.append(POINTER(get_args(type_)[0]))
            elif _winrt.is_receivearray_class(type_):
                argtypes.append(POINTER(UInt32))
                argtypes.append(POINTER(POINTER(get_args(type_)[0])))
            else:
                argtypes.append(self._make_allocator(type_))
        if restype is Void:
            pass
        elif _winrt.is_receivearray_class(restype):
            argtypes.append(POINTER(UInt32))
            argtypes.append(POINTER(POINTER(get_args(restype)[0])))
        elif _winrt.is_generic_alias(restype):
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
        if _winrt.is_generic_alias(t) or issubclass(t, ComPtr):
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
        if _winrt.is_passarray_class(type_):
            exitstack.enter_context(_winrt.PassArrayCallback(get_args(type_)[0], args.pop(0), args.pop(0), pyargs))
        elif _winrt.is_fillarray_class(type_):
            exitstack.enter_context(_winrt.FillArrayCallback(get_args(type_)[0], args.pop(0), args.pop(0), pyargs))
        elif _winrt.is_receivearray_class(type_):
            exitstack.enter_context(_winrt.ReceiveArrayCallback(get_args(type_)[0], args.pop(0), args.pop(0), pyargs))
        elif type_ is hstr:
            pyargs.append(str(args.pop(0)))
        else:
            pyargs.append(args.pop(0))

    def _handle_result(self, restype: type, args: list[Any], result: Any) -> Any:
        if restype is Void:
            pass
        elif _winrt.is_receivearray_class(restype):
            return_length, return_pointer = args
            _winrt.ReceiveArrayCallback.handle_result(get_args(restype)[0], return_length, return_pointer, result)
        elif restype is hstr:
            return_pointer = args[0]
            return_pointer[0] = hstr(result)
        elif _winrt.is_com_class(restype):
            return_pointer = args[0]
            if result:
                result.AddRef()
            return_pointer[0] = result
        else:
            return_pointer = args[0]
            return_pointer[0] = result


class ISelf(IUnknown):
    _iid_ = Guid("{18320492-860a-4c7b-ad7c-6cd65c88c09e}")

    @commethod(3)
    def GetSelf(self) -> py_object: ...
