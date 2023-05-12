from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Phone.System.Profile
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IRetailModeStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Profile.IRetailModeStatics'
    _iid_ = Guid('{d7ded029-fdda-43e7-93fb-e53ab6e89ec3}')
    @winrt_commethod(6)
    def get_RetailModeEnabled(self) -> Boolean: ...
    RetailModeEnabled = property(get_RetailModeEnabled, None)
class _RetailMode_Meta_(ComPtr.__class__):
    pass
class RetailMode(ComPtr, metaclass=_RetailMode_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Profile.RetailMode'
    @winrt_classmethod
    def get_RetailModeEnabled(cls: Windows.Phone.System.Profile.IRetailModeStatics) -> Boolean: ...
    _RetailMode_Meta_.RetailModeEnabled = property(get_RetailModeEnabled.__wrapped__, None)
make_head(_module, 'IRetailModeStatics')
make_head(_module, 'RetailMode')
