from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Gaming.Input.Custom
import win32more.Windows.Gaming.Input.Preview
import win32more.Windows.Win32.System.WinRT
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
