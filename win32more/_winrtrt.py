from __future__ import annotations

import logging
from ctypes import addressof, sizeof

from win32more import POINTER, Boolean, Guid, UInt32, Void, VoidPtr
from win32more._winrt import (
    FillArray,
    PassArray,
    T,
    Vtbl,
    _ro_get_parameterized_type_instance_iid,
    _windows_create_string,
    get_args,
    is_com_class,
)
from win32more.Windows.Foundation.Collections import IVector, IVectorView
from win32more.Windows.Win32.Foundation import E_NOINTERFACE, HRESULT, S_OK
from win32more.Windows.Win32.System.Com import CoTaskMemAlloc, IUnknown
from win32more.Windows.Win32.System.WinRT import HSTRING, BaseTrust, IInspectable, TrustLevel

logger = logging.getLogger(__name__)


class GenericInitialize:
    def __set__(self, instance, value):
        instance.__dict__["__orig_class__"] = value
        try:
            instance.__init_generic__()
        except Exception:
            # _BaseGenericAlias.__call__() ignore error
            logger.exception("Unhandled exception caught")
            raise


class Vector(IVector[T]):
    _keep_reference_in_python_world_ = {}

    __orig_class__ = GenericInitialize()

    def __init__(self, lst: list[T] | None = None) -> None:
        super().__init__(own=True)
        self._lst = lst

    def __init_generic__(self) -> None:
        self._type = get_args(self.__orig_class__)[0]
        self._iid_ = _ro_get_parameterized_type_instance_iid(IVector[self._type])
        self._view_iid = _ro_get_parameterized_type_instance_iid(IVectorView[self._type])

        if self._lst is None:
            self._lst = []

        self._vtbl = Vtbl(self, IVector[self._type])
        self._view_vtbl = Vtbl(self, IVectorView[self._type])

        self.value = addressof(self._vtbl)
        self._refcount = 0
        self.AddRef()

    def QueryInterface(self, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> HRESULT:
        if riid[0] == IUnknown._iid_ or riid[0] == IInspectable._iid_ or riid[0] == self._iid_:
            ppvObject[0] = addressof(self._vtbl)
            self.AddRef()
            return S_OK
        elif riid[0] == self._view_iid:
            ppvObject[0] = addressof(self._view_vtbl)
            self.AddRef()
            return S_OK
        return E_NOINTERFACE

    def AddRef(self):
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self):
        self._refcount -= 1
        if self._refcount == 0:
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount: POINTER(UInt32), iids: POINTER(POINTER(Guid))) -> HRESULT:
        iidCount[0] = 4
        iids[0] = CoTaskMemAlloc(sizeof(VoidPtr) * 4)
        iids[0][0] = IUnknown._iid_
        iids[0][1] = IInspectable._iid_
        iids[0][2] = self._iid_
        iids[0][3] = self._view_iid
        return S_OK

    def GetRuntimeClassName(self, className: POINTER(HSTRING)) -> HRESULT:
        className[0] = _windows_create_string("Vector`1")
        return S_OK

    def GetTrustLevel(self, trustLevel: POINTER(TrustLevel)) -> HRESULT:
        trustLevel[0] = BaseTrust
        return S_OK

    def GetAt(self, index: UInt32) -> T:
        r = self._lst[index]
        if is_com_class(self._type):
            r.AddRef()
        return r

    def get_Size(self) -> UInt32:
        return len(self._lst)

    def GetView(self) -> IVectorView[T]:
        return self.as_(IVector[self._type])

    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean:
        for i, v in enumerate(self._lst):
            if v == value:
                index[0] = i
                return True
        return False

    def SetAt(self, index: UInt32, value: T) -> Void:
        if is_com_class(self._type):
            value.AddRef()
        self._lst[index] = value

    def InsertAt(self, index: UInt32, value: T) -> Void:
        if is_com_class(self._type):
            value.AddRef()
        self._lst.insert(index, value)

    def RemoveAt(self, index: UInt32) -> Void:
        del self._lst[index]

    def Append(self, value: T) -> Void:
        if is_com_class(self._type):
            value.AddRef()
        self._lst.append(value)

    def RemoveAtEnd(self) -> Void:
        del self._lst[-1]

    def Clear(self) -> Void:
        self._lst[:] = []

    def GetMany(self, startIndex: UInt32, items: FillArray[T]) -> UInt32:
        numcopied = 0
        for i in range(startIndex, startIndex + len(items)):
            if i >= len(self._lst):
                break
            v = self._lst[i]
            if is_com_class(self._type):
                v.AddRef()
            items[numcopied] = v
            numcopied += 1
        return numcopied

    def ReplaceAll(self, items: PassArray[T]) -> Void:
        self._lst[:] = items
        if is_com_class(self._type):
            for v in self._lst:
                v.AddRef()
