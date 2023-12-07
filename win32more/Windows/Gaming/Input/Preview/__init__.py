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
import win32more.Windows.Gaming.Input.Custom
import win32more.Windows.Gaming.Input.Preview
class GameControllerProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.GameControllerProviderInfo'
    @winrt_classmethod
    def GetParentProviderId(cls: win32more.Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
    @winrt_classmethod
    def GetProviderId(cls: win32more.Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
class IGameControllerProviderInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics'
    _iid_ = Guid('{0be1e6c5-d9bd-44ee-8362-488b2e464bfb}')
    @winrt_commethod(6)
    def GetParentProviderId(self, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetProviderId(self, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
make_ready(__name__)
