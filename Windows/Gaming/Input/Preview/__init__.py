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
import Windows.Gaming.Input.Custom
import Windows.Gaming.Input.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GameControllerProviderInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.GameControllerProviderInfo'
    @winrt_classmethod
    def GetParentProviderId(cls: Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics, provider: Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
    @winrt_classmethod
    def GetProviderId(cls: Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics, provider: Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
class IGameControllerProviderInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics'
    _iid_ = Guid('{0be1e6c5-d9bd-44ee-8362-488b2e464bfb}')
    @winrt_commethod(6)
    def GetParentProviderId(self, provider: Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetProviderId(self, provider: Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
make_head(_module, 'GameControllerProviderInfo')
make_head(_module, 'IGameControllerProviderInfoStatics')
