from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Radios
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
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
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
    State = property(get_State, None)
    StateChanged = event()
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
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
    State = property(get_State, None)
    StateChanged = event()
class RadioAccessStatus(Enum, Int32):
    Unspecified = 0
    Allowed = 1
    DeniedByUser = 2
    DeniedBySystem = 3
class RadioKind(Enum, Int32):
    Other = 0
    WiFi = 1
    MobileBroadband = 2
    Bluetooth = 3
    FM = 4
class RadioState(Enum, Int32):
    Unknown = 0
    On = 1
    Off = 2
    Disabled = 3


make_ready(__name__)
