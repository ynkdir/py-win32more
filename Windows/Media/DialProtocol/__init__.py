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
class DialApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialApp'
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
class DialAppStateDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialAppStateDetails'
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
class DialDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialDevice'
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
class DialDevicePicker(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialDevicePicker'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.DialProtocol.DialDevicePicker: ...
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
class DialDevicePickerFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialDevicePickerFilter'
    @winrt_mixinmethod
    def get_SupportedAppNames(self: Windows.Media.DialProtocol.IDialDevicePickerFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedAppNames = property(get_SupportedAppNames, None)
class DialDeviceSelectedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialDeviceSelectedEventArgs'
    @winrt_mixinmethod
    def get_SelectedDialDevice(self: Windows.Media.DialProtocol.IDialDeviceSelectedEventArgs) -> Windows.Media.DialProtocol.DialDevice: ...
    SelectedDialDevice = property(get_SelectedDialDevice, None)
class DialDisconnectButtonClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialDisconnectButtonClickedEventArgs'
    @winrt_mixinmethod
    def get_Device(self: Windows.Media.DialProtocol.IDialDisconnectButtonClickedEventArgs) -> Windows.Media.DialProtocol.DialDevice: ...
    Device = property(get_Device, None)
class DialReceiverApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.DialProtocol.DialReceiverApp'
    @winrt_mixinmethod
    def GetAdditionalDataAsync(self: Windows.Media.DialProtocol.IDialReceiverApp) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]]: ...
    @winrt_mixinmethod
    def SetAdditionalDataAsync(self: Windows.Media.DialProtocol.IDialReceiverApp, additionalData: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetUniqueDeviceNameAsync(self: Windows.Media.DialProtocol.IDialReceiverApp2) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def get_Current(cls: Windows.Media.DialProtocol.IDialReceiverAppStatics) -> Windows.Media.DialProtocol.DialReceiverApp: ...
    Current = property(get_Current, None)
class IDialApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('555ffbd3-45b7-49f3-bb-d7-30-2d-b6-08-46-46')
    @winrt_commethod(6)
    def get_AppName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def RequestLaunchAsync(self, appArgument: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppLaunchResult]: ...
    @winrt_commethod(8)
    def StopAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppStopResult]: ...
    @winrt_commethod(9)
    def GetAppStateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialAppStateDetails]: ...
    AppName = property(get_AppName, None)
class IDialAppStateDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ddc4a4a1-f5de-400d-be-a4-8c-84-66-bb-29-61')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Media.DialProtocol.DialAppState: ...
    @winrt_commethod(7)
    def get_FullXml(self) -> WinRT_String: ...
    State = property(get_State, None)
    FullXml = property(get_FullXml, None)
class IDialDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fff0edaf-759f-41d2-a2-0a-7f-29-ce-0b-37-84')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDialApp(self, appName: WinRT_String) -> Windows.Media.DialProtocol.DialApp: ...
    Id = property(get_Id, None)
class IDialDevice2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bab7f3d5-5bfb-4eba-8b-32-b5-7c-5c-5e-e5-c9')
    @winrt_commethod(6)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    FriendlyName = property(get_FriendlyName, None)
    Thumbnail = property(get_Thumbnail, None)
class IDialDevicePicker(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ba7e520a-ff59-4f4b-bd-ac-d8-9f-49-5a-d6-e1')
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
class IDialDevicePickerFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c17c93ba-86c0-485d-b8-d6-0f-9a-8f-64-15-90')
    @winrt_commethod(6)
    def get_SupportedAppNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedAppNames = property(get_SupportedAppNames, None)
class IDialDeviceSelectedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('480b92ad-ac76-47eb-9c-06-a1-93-04-da-02-47')
    @winrt_commethod(6)
    def get_SelectedDialDevice(self) -> Windows.Media.DialProtocol.DialDevice: ...
    SelectedDialDevice = property(get_SelectedDialDevice, None)
class IDialDeviceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aa69cc95-01f8-4758-84-61-2b-bd-1c-dc-3c-f3')
    @winrt_commethod(6)
    def GetDeviceSelector(self, appName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, value: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_commethod(8)
    def DeviceInfoSupportsDialAsync(self, device: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IDialDisconnectButtonClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('52765152-9c81-4e55-ad-c2-0e-be-99-cd-e3-b6')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Media.DialProtocol.DialDevice: ...
    Device = property(get_Device, None)
class IDialReceiverApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fd3e7c57-5045-470e-b3-04-4d-d9-b1-3e-7d-11')
    @winrt_commethod(6)
    def GetAdditionalDataAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]]: ...
    @winrt_commethod(7)
    def SetAdditionalDataAsync(self, additionalData: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
class IDialReceiverApp2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('530c5805-9130-42ac-a5-04-19-77-dc-b2-ea-8a')
    @winrt_commethod(6)
    def GetUniqueDeviceNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class IDialReceiverAppStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('53183a3c-4c36-4d02-b2-8a-f2-a9-da-38-ec-52')
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
