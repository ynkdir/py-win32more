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
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.DialProtocol
import Windows.Storage.Streams
import Windows.UI.Popups
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DialApp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialApp
    _classid_ = 'Windows.Media.DialProtocol.DialApp'
    @winrt_mixinmethod
    def get_AppName(self: Windows.Media.DialProtocol.IDialApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestLaunchAsync(self: Windows.Media.DialProtocol.IDialApp, appArgument: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppLaunchResult]: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.DialProtocol.IDialApp) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppStopResult]: ...
    @winrt_mixinmethod
    def GetAppStateAsync(self: Windows.Media.DialProtocol.IDialApp) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppStateDetails]: ...
    AppName = property(get_AppName, None)
DialAppLaunchResult = Int32
DialAppLaunchResult_Launched: DialAppLaunchResult = 0
DialAppLaunchResult_FailedToLaunch: DialAppLaunchResult = 1
DialAppLaunchResult_NotFound: DialAppLaunchResult = 2
DialAppLaunchResult_NetworkFailure: DialAppLaunchResult = 3
DialAppState = Int32
DialAppState_Unknown: DialAppState = 0
DialAppState_Stopped: DialAppState = 1
DialAppState_Running: DialAppState = 2
DialAppState_NetworkFailure: DialAppState = 3
class DialAppStateDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialAppStateDetails
    _classid_ = 'Windows.Media.DialProtocol.DialAppStateDetails'
    @winrt_mixinmethod
    def get_State(self: Windows.Media.DialProtocol.IDialAppStateDetails) -> Windows.Media.DialProtocol.DialAppState: ...
    @winrt_mixinmethod
    def get_FullXml(self: Windows.Media.DialProtocol.IDialAppStateDetails) -> WinRT_String: ...
    State = property(get_State, None)
    FullXml = property(get_FullXml, None)
DialAppStopResult = Int32
DialAppStopResult_Stopped: DialAppStopResult = 0
DialAppStopResult_StopFailed: DialAppStopResult = 1
DialAppStopResult_OperationNotSupported: DialAppStopResult = 2
DialAppStopResult_NetworkFailure: DialAppStopResult = 3
class DialDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialDevice
    _classid_ = 'Windows.Media.DialProtocol.DialDevice'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.DialProtocol.IDialDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDialApp(self: Windows.Media.DialProtocol.IDialDevice, appName: WinRT_String) -> Windows.Media.DialProtocol.DialApp: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Media.DialProtocol.IDialDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.DialProtocol.IDialDevice2) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Media.DialProtocol.IDialDeviceStatics, appName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Media.DialProtocol.IDialDeviceStatics, value: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_classmethod
    def DeviceInfoSupportsDialAsync(cls: Windows.Media.DialProtocol.IDialDeviceStatics, device: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Id = property(get_Id, None)
    FriendlyName = property(get_FriendlyName, None)
    Thumbnail = property(get_Thumbnail, None)
DialDeviceDisplayStatus = Int32
DialDeviceDisplayStatus_None: DialDeviceDisplayStatus = 0
DialDeviceDisplayStatus_Connecting: DialDeviceDisplayStatus = 1
DialDeviceDisplayStatus_Connected: DialDeviceDisplayStatus = 2
DialDeviceDisplayStatus_Disconnecting: DialDeviceDisplayStatus = 3
DialDeviceDisplayStatus_Disconnected: DialDeviceDisplayStatus = 4
DialDeviceDisplayStatus_Error: DialDeviceDisplayStatus = 5
class DialDevicePicker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialDevicePicker
    _classid_ = 'Windows.Media.DialProtocol.DialDevicePicker'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.DialProtocol.DialDevicePicker: ...
    @winrt_mixinmethod
    def get_Filter(self: Windows.Media.DialProtocol.IDialDevicePicker) -> Windows.Media.DialProtocol.DialDevicePickerFilter: ...
    @winrt_mixinmethod
    def get_Appearance(self: Windows.Media.DialProtocol.IDialDevicePicker) -> Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_mixinmethod
    def add_DialDeviceSelected(self: Windows.Media.DialProtocol.IDialDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Media.DialProtocol.DialDevicePicker, Windows.Media.DialProtocol.DialDeviceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DialDeviceSelected(self: Windows.Media.DialProtocol.IDialDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisconnectButtonClicked(self: Windows.Media.DialProtocol.IDialDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Media.DialProtocol.DialDevicePicker, Windows.Media.DialProtocol.DialDisconnectButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisconnectButtonClicked(self: Windows.Media.DialProtocol.IDialDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DialDevicePickerDismissed(self: Windows.Media.DialProtocol.IDialDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Media.DialProtocol.DialDevicePicker, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DialDevicePickerDismissed(self: Windows.Media.DialProtocol.IDialDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Show(self: Windows.Media.DialProtocol.IDialDevicePicker, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPlacement(self: Windows.Media.DialProtocol.IDialDevicePicker, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def PickSingleDialDeviceAsync(self: Windows.Media.DialProtocol.IDialDevicePicker, selection: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_mixinmethod
    def PickSingleDialDeviceAsyncWithPlacement(self: Windows.Media.DialProtocol.IDialDevicePicker, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_mixinmethod
    def Hide(self: Windows.Media.DialProtocol.IDialDevicePicker) -> Void: ...
    @winrt_mixinmethod
    def SetDisplayStatus(self: Windows.Media.DialProtocol.IDialDevicePicker, device: Windows.Media.DialProtocol.DialDevice, status: Windows.Media.DialProtocol.DialDeviceDisplayStatus) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class DialDevicePickerFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialDevicePickerFilter
    _classid_ = 'Windows.Media.DialProtocol.DialDevicePickerFilter'
    @winrt_mixinmethod
    def get_SupportedAppNames(self: Windows.Media.DialProtocol.IDialDevicePickerFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedAppNames = property(get_SupportedAppNames, None)
class DialDeviceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialDeviceSelectedEventArgs
    _classid_ = 'Windows.Media.DialProtocol.DialDeviceSelectedEventArgs'
    @winrt_mixinmethod
    def get_SelectedDialDevice(self: Windows.Media.DialProtocol.IDialDeviceSelectedEventArgs) -> Windows.Media.DialProtocol.DialDevice: ...
    SelectedDialDevice = property(get_SelectedDialDevice, None)
class DialDisconnectButtonClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialDisconnectButtonClickedEventArgs
    _classid_ = 'Windows.Media.DialProtocol.DialDisconnectButtonClickedEventArgs'
    @winrt_mixinmethod
    def get_Device(self: Windows.Media.DialProtocol.IDialDisconnectButtonClickedEventArgs) -> Windows.Media.DialProtocol.DialDevice: ...
    Device = property(get_Device, None)
class _DialReceiverApp_Meta_(ComPtr.__class__):
    pass
class DialReceiverApp(ComPtr, metaclass=_DialReceiverApp_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.DialProtocol.IDialReceiverApp
    _classid_ = 'Windows.Media.DialProtocol.DialReceiverApp'
    @winrt_mixinmethod
    def GetAdditionalDataAsync(self: Windows.Media.DialProtocol.IDialReceiverApp) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]]: ...
    @winrt_mixinmethod
    def SetAdditionalDataAsync(self: Windows.Media.DialProtocol.IDialReceiverApp, additionalData: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetUniqueDeviceNameAsync(self: Windows.Media.DialProtocol.IDialReceiverApp2) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def get_Current(cls: Windows.Media.DialProtocol.IDialReceiverAppStatics) -> Windows.Media.DialProtocol.DialReceiverApp: ...
    _DialReceiverApp_Meta_.Current = property(get_Current.__wrapped__, None)
class IDialApp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialApp'
    _iid_ = Guid('{555ffbd3-45b7-49f3-bbd7-302db6084646}')
    @winrt_commethod(6)
    def get_AppName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def RequestLaunchAsync(self, appArgument: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppLaunchResult]: ...
    @winrt_commethod(8)
    def StopAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppStopResult]: ...
    @winrt_commethod(9)
    def GetAppStateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppStateDetails]: ...
    AppName = property(get_AppName, None)
class IDialAppStateDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialAppStateDetails'
    _iid_ = Guid('{ddc4a4a1-f5de-400d-bea4-8c8466bb2961}')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Media.DialProtocol.DialAppState: ...
    @winrt_commethod(7)
    def get_FullXml(self) -> WinRT_String: ...
    State = property(get_State, None)
    FullXml = property(get_FullXml, None)
class IDialDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevice'
    _iid_ = Guid('{fff0edaf-759f-41d2-a20a-7f29ce0b3784}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDialApp(self, appName: WinRT_String) -> Windows.Media.DialProtocol.DialApp: ...
    Id = property(get_Id, None)
class IDialDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevice2'
    _iid_ = Guid('{bab7f3d5-5bfb-4eba-8b32-b57c5c5ee5c9}')
    @winrt_commethod(6)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    FriendlyName = property(get_FriendlyName, None)
    Thumbnail = property(get_Thumbnail, None)
class IDialDevicePicker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevicePicker'
    _iid_ = Guid('{ba7e520a-ff59-4f4b-bdac-d89f495ad6e1}')
    @winrt_commethod(6)
    def get_Filter(self) -> Windows.Media.DialProtocol.DialDevicePickerFilter: ...
    @winrt_commethod(7)
    def get_Appearance(self) -> Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_commethod(8)
    def add_DialDeviceSelected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.DialProtocol.DialDevicePicker, Windows.Media.DialProtocol.DialDeviceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DialDeviceSelected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_DisconnectButtonClicked(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.DialProtocol.DialDevicePicker, Windows.Media.DialProtocol.DialDisconnectButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DisconnectButtonClicked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_DialDevicePickerDismissed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.DialProtocol.DialDevicePicker, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DialDevicePickerDismissed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def Show(self, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(15)
    def ShowWithPlacement(self, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(16)
    def PickSingleDialDeviceAsync(self, selection: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_commethod(17)
    def PickSingleDialDeviceAsyncWithPlacement(self, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_commethod(18)
    def Hide(self) -> Void: ...
    @winrt_commethod(19)
    def SetDisplayStatus(self, device: Windows.Media.DialProtocol.DialDevice, status: Windows.Media.DialProtocol.DialDeviceDisplayStatus) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class IDialDevicePickerFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevicePickerFilter'
    _iid_ = Guid('{c17c93ba-86c0-485d-b8d6-0f9a8f641590}')
    @winrt_commethod(6)
    def get_SupportedAppNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedAppNames = property(get_SupportedAppNames, None)
class IDialDeviceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDeviceSelectedEventArgs'
    _iid_ = Guid('{480b92ad-ac76-47eb-9c06-a19304da0247}')
    @winrt_commethod(6)
    def get_SelectedDialDevice(self) -> Windows.Media.DialProtocol.DialDevice: ...
    SelectedDialDevice = property(get_SelectedDialDevice, None)
class IDialDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDeviceStatics'
    _iid_ = Guid('{aa69cc95-01f8-4758-8461-2bbd1cdc3cf3}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, appName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, value: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_commethod(8)
    def DeviceInfoSupportsDialAsync(self, device: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IDialDisconnectButtonClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDisconnectButtonClickedEventArgs'
    _iid_ = Guid('{52765152-9c81-4e55-adc2-0ebe99cde3b6}')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Media.DialProtocol.DialDevice: ...
    Device = property(get_Device, None)
class IDialReceiverApp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialReceiverApp'
    _iid_ = Guid('{fd3e7c57-5045-470e-b304-4dd9b13e7d11}')
    @winrt_commethod(6)
    def GetAdditionalDataAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]]: ...
    @winrt_commethod(7)
    def SetAdditionalDataAsync(self, additionalData: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
class IDialReceiverApp2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialReceiverApp2'
    _iid_ = Guid('{530c5805-9130-42ac-a504-1977dcb2ea8a}')
    @winrt_commethod(6)
    def GetUniqueDeviceNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class IDialReceiverAppStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialReceiverAppStatics'
    _iid_ = Guid('{53183a3c-4c36-4d02-b28a-f2a9da38ec52}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.Media.DialProtocol.DialReceiverApp: ...
    Current = property(get_Current, None)
make_head(_module, 'DialApp')
make_head(_module, 'DialAppStateDetails')
make_head(_module, 'DialDevice')
make_head(_module, 'DialDevicePicker')
make_head(_module, 'DialDevicePickerFilter')
make_head(_module, 'DialDeviceSelectedEventArgs')
make_head(_module, 'DialDisconnectButtonClickedEventArgs')
make_head(_module, 'DialReceiverApp')
make_head(_module, 'IDialApp')
make_head(_module, 'IDialAppStateDetails')
make_head(_module, 'IDialDevice')
make_head(_module, 'IDialDevice2')
make_head(_module, 'IDialDevicePicker')
make_head(_module, 'IDialDevicePickerFilter')
make_head(_module, 'IDialDeviceSelectedEventArgs')
make_head(_module, 'IDialDeviceStatics')
make_head(_module, 'IDialDisconnectButtonClickedEventArgs')
make_head(_module, 'IDialReceiverApp')
make_head(_module, 'IDialReceiverApp2')
make_head(_module, 'IDialReceiverAppStatics')
