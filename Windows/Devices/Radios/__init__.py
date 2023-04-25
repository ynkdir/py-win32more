from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Devices.Radios
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IRadio(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('252118df-b33e-416a-87-5f-1c-f3-8a-e2-d8-3e')
    @winrt_commethod(6)
    def SetStateAsync(self, value: Windows.Devices.Radios.RadioState) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.RadioAccessStatus]: ...
    @winrt_commethod(7)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Radios.Radio, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StateChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_State(self) -> Windows.Devices.Radios.RadioState: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Kind(self) -> Windows.Devices.Radios.RadioKind: ...
    State = property(get_State, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
class IRadioStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5fb6a12e-67cb-46ae-aa-e9-65-91-9f-86-ef-f4')
    @winrt_commethod(6)
    def GetRadiosAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Radios.Radio]]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.Radio]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.RadioAccessStatus]: ...
class Radio(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Radios.Radio'
    @winrt_mixinmethod
    def SetStateAsync(self: Windows.Devices.Radios.IRadio, value: Windows.Devices.Radios.RadioState) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.RadioAccessStatus]: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Devices.Radios.IRadio, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Radios.Radio, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Devices.Radios.IRadio, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.Radios.IRadio) -> Windows.Devices.Radios.RadioState: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Devices.Radios.IRadio) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Devices.Radios.IRadio) -> Windows.Devices.Radios.RadioKind: ...
    @winrt_classmethod
    def GetRadiosAsync(cls: Windows.Devices.Radios.IRadioStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Radios.Radio]]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Radios.IRadioStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Radios.IRadioStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.Radio]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Devices.Radios.IRadioStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.RadioAccessStatus]: ...
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
make_head(_module, 'IRadio')
make_head(_module, 'IRadioStatics')
make_head(_module, 'Radio')
