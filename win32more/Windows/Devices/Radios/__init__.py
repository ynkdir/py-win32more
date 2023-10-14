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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Radios
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class IRadio(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Radios.IRadio'
    _iid_ = Guid('{252118df-b33e-416a-875f-1cf38ae2d83e}')
    @winrt_commethod(6)
    def SetStateAsync(self, value: win32more.Windows.Devices.Radios.RadioState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.RadioAccessStatus]: ...
    @winrt_commethod(7)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Radios.Radio, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StateChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Devices.Radios.RadioState: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Kind(self) -> win32more.Windows.Devices.Radios.RadioKind: ...
    State = property(get_State, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
class IRadioStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Radios.IRadioStatics'
    _iid_ = Guid('{5fb6a12e-67cb-46ae-aae9-65919f86eff4}')
    @winrt_commethod(6)
    def GetRadiosAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Radios.Radio]]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.Radio]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.RadioAccessStatus]: ...
class Radio(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Radios.IRadio
    _classid_ = 'Windows.Devices.Radios.Radio'
    @winrt_mixinmethod
    def SetStateAsync(self: win32more.Windows.Devices.Radios.IRadio, value: win32more.Windows.Devices.Radios.RadioState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.RadioAccessStatus]: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Devices.Radios.IRadio, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Radios.Radio, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Devices.Radios.IRadio, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.Radios.IRadio) -> win32more.Windows.Devices.Radios.RadioState: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Devices.Radios.IRadio) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Devices.Radios.IRadio) -> win32more.Windows.Devices.Radios.RadioKind: ...
    @winrt_classmethod
    def GetRadiosAsync(cls: win32more.Windows.Devices.Radios.IRadioStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Radios.Radio]]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Radios.IRadioStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Radios.IRadioStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.Radio]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.Radios.IRadioStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.RadioAccessStatus]: ...
    State = property(get_State, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
RadioAccessStatus = Int32
RadioAccessStatus_Unspecified: RadioAccessStatus = 0
RadioAccessStatus_Allowed: RadioAccessStatus = 1
RadioAccessStatus_DeniedByUser: RadioAccessStatus = 2
RadioAccessStatus_DeniedBySystem: RadioAccessStatus = 3
RadioKind = Int32
RadioKind_Other: RadioKind = 0
RadioKind_WiFi: RadioKind = 1
RadioKind_MobileBroadband: RadioKind = 2
RadioKind_Bluetooth: RadioKind = 3
RadioKind_FM: RadioKind = 4
RadioState = Int32
RadioState_Unknown: RadioState = 0
RadioState_On: RadioState = 1
RadioState_Off: RadioState = 2
RadioState_Disabled: RadioState = 3
make_ready(__name__)
