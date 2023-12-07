from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Phone.System.Profile
class IRetailModeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Profile.IRetailModeStatics'
    _iid_ = Guid('{d7ded029-fdda-43e7-93fb-e53ab6e89ec3}')
    @winrt_commethod(6)
    def get_RetailModeEnabled(self) -> Boolean: ...
    RetailModeEnabled = property(get_RetailModeEnabled, None)
class _RetailMode_Meta_(ComPtr.__class__):
    pass
class RetailMode(ComPtr, metaclass=_RetailMode_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Profile.RetailMode'
    @winrt_classmethod
    def get_RetailModeEnabled(cls: win32more.Windows.Phone.System.Profile.IRetailModeStatics) -> Boolean: ...
    _RetailMode_Meta_.RetailModeEnabled = property(get_RetailModeEnabled.__wrapped__, None)
make_ready(__name__)
