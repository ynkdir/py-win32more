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
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.DialProtocol
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.Popups
class DialApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialApp
    _classid_ = 'Windows.Media.DialProtocol.DialApp'
    @winrt_mixinmethod
    def get_AppName(self: win32more.Windows.Media.DialProtocol.IDialApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestLaunchAsync(self: win32more.Windows.Media.DialProtocol.IDialApp, appArgument: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialAppLaunchResult]: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.DialProtocol.IDialApp) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialAppStopResult]: ...
    @winrt_mixinmethod
    def GetAppStateAsync(self: win32more.Windows.Media.DialProtocol.IDialApp) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialAppStateDetails]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialAppStateDetails
    _classid_ = 'Windows.Media.DialProtocol.DialAppStateDetails'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.DialProtocol.IDialAppStateDetails) -> win32more.Windows.Media.DialProtocol.DialAppState: ...
    @winrt_mixinmethod
    def get_FullXml(self: win32more.Windows.Media.DialProtocol.IDialAppStateDetails) -> WinRT_String: ...
    State = property(get_State, None)
    FullXml = property(get_FullXml, None)
DialAppStopResult = Int32
DialAppStopResult_Stopped: DialAppStopResult = 0
DialAppStopResult_StopFailed: DialAppStopResult = 1
DialAppStopResult_OperationNotSupported: DialAppStopResult = 2
DialAppStopResult_NetworkFailure: DialAppStopResult = 3
class DialDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialDevice
    _classid_ = 'Windows.Media.DialProtocol.DialDevice'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.DialProtocol.IDialDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDialApp(self: win32more.Windows.Media.DialProtocol.IDialDevice, appName: WinRT_String) -> win32more.Windows.Media.DialProtocol.DialApp: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Media.DialProtocol.IDialDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.DialProtocol.IDialDevice2) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Media.DialProtocol.IDialDeviceStatics, appName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Media.DialProtocol.IDialDeviceStatics, value: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_classmethod
    def DeviceInfoSupportsDialAsync(cls: win32more.Windows.Media.DialProtocol.IDialDeviceStatics, device: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialDevicePicker
    _classid_ = 'Windows.Media.DialProtocol.DialDevicePicker'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Media.DialProtocol.DialDevicePicker.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.DialProtocol.DialDevicePicker: ...
    @winrt_mixinmethod
    def get_Filter(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker) -> win32more.Windows.Media.DialProtocol.DialDevicePickerFilter: ...
    @winrt_mixinmethod
    def get_Appearance(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker) -> win32more.Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_mixinmethod
    def add_DialDeviceSelected(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.DialProtocol.DialDevicePicker, win32more.Windows.Media.DialProtocol.DialDeviceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DialDeviceSelected(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisconnectButtonClicked(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.DialProtocol.DialDevicePicker, win32more.Windows.Media.DialProtocol.DialDisconnectButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisconnectButtonClicked(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DialDevicePickerDismissed(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.DialProtocol.DialDevicePicker, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DialDevicePickerDismissed(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Show(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPlacement(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def PickSingleDialDeviceAsync(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_mixinmethod
    def PickSingleDialDeviceAsyncWithPlacement(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_mixinmethod
    def Hide(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker) -> Void: ...
    @winrt_mixinmethod
    def SetDisplayStatus(self: win32more.Windows.Media.DialProtocol.IDialDevicePicker, device: win32more.Windows.Media.DialProtocol.DialDevice, status: win32more.Windows.Media.DialProtocol.DialDeviceDisplayStatus) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class DialDevicePickerFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialDevicePickerFilter
    _classid_ = 'Windows.Media.DialProtocol.DialDevicePickerFilter'
    @winrt_mixinmethod
    def get_SupportedAppNames(self: win32more.Windows.Media.DialProtocol.IDialDevicePickerFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedAppNames = property(get_SupportedAppNames, None)
class DialDeviceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialDeviceSelectedEventArgs
    _classid_ = 'Windows.Media.DialProtocol.DialDeviceSelectedEventArgs'
    @winrt_mixinmethod
    def get_SelectedDialDevice(self: win32more.Windows.Media.DialProtocol.IDialDeviceSelectedEventArgs) -> win32more.Windows.Media.DialProtocol.DialDevice: ...
    SelectedDialDevice = property(get_SelectedDialDevice, None)
class DialDisconnectButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialDisconnectButtonClickedEventArgs
    _classid_ = 'Windows.Media.DialProtocol.DialDisconnectButtonClickedEventArgs'
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Media.DialProtocol.IDialDisconnectButtonClickedEventArgs) -> win32more.Windows.Media.DialProtocol.DialDevice: ...
    Device = property(get_Device, None)
class _DialReceiverApp_Meta_(ComPtr.__class__):
    pass
class DialReceiverApp(ComPtr, metaclass=_DialReceiverApp_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.DialProtocol.IDialReceiverApp
    _classid_ = 'Windows.Media.DialProtocol.DialReceiverApp'
    @winrt_mixinmethod
    def GetAdditionalDataAsync(self: win32more.Windows.Media.DialProtocol.IDialReceiverApp) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]]: ...
    @winrt_mixinmethod
    def SetAdditionalDataAsync(self: win32more.Windows.Media.DialProtocol.IDialReceiverApp, additionalData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetUniqueDeviceNameAsync(self: win32more.Windows.Media.DialProtocol.IDialReceiverApp2) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.Media.DialProtocol.IDialReceiverAppStatics) -> win32more.Windows.Media.DialProtocol.DialReceiverApp: ...
    _DialReceiverApp_Meta_.Current = property(get_Current.__wrapped__, None)
class IDialApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialApp'
    _iid_ = Guid('{555ffbd3-45b7-49f3-bbd7-302db6084646}')
    @winrt_commethod(6)
    def get_AppName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def RequestLaunchAsync(self, appArgument: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialAppLaunchResult]: ...
    @winrt_commethod(8)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialAppStopResult]: ...
    @winrt_commethod(9)
    def GetAppStateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialAppStateDetails]: ...
    AppName = property(get_AppName, None)
class IDialAppStateDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialAppStateDetails'
    _iid_ = Guid('{ddc4a4a1-f5de-400d-bea4-8c8466bb2961}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.DialProtocol.DialAppState: ...
    @winrt_commethod(7)
    def get_FullXml(self) -> WinRT_String: ...
    State = property(get_State, None)
    FullXml = property(get_FullXml, None)
class IDialDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevice'
    _iid_ = Guid('{fff0edaf-759f-41d2-a20a-7f29ce0b3784}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDialApp(self, appName: WinRT_String) -> win32more.Windows.Media.DialProtocol.DialApp: ...
    Id = property(get_Id, None)
class IDialDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevice2'
    _iid_ = Guid('{bab7f3d5-5bfb-4eba-8b32-b57c5c5ee5c9}')
    @winrt_commethod(6)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    FriendlyName = property(get_FriendlyName, None)
    Thumbnail = property(get_Thumbnail, None)
class IDialDevicePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevicePicker'
    _iid_ = Guid('{ba7e520a-ff59-4f4b-bdac-d89f495ad6e1}')
    @winrt_commethod(6)
    def get_Filter(self) -> win32more.Windows.Media.DialProtocol.DialDevicePickerFilter: ...
    @winrt_commethod(7)
    def get_Appearance(self) -> win32more.Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_commethod(8)
    def add_DialDeviceSelected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.DialProtocol.DialDevicePicker, win32more.Windows.Media.DialProtocol.DialDeviceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DialDeviceSelected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_DisconnectButtonClicked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.DialProtocol.DialDevicePicker, win32more.Windows.Media.DialProtocol.DialDisconnectButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DisconnectButtonClicked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_DialDevicePickerDismissed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.DialProtocol.DialDevicePicker, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DialDevicePickerDismissed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def Show(self, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(15)
    def ShowWithPlacement(self, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(16)
    def PickSingleDialDeviceAsync(self, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_commethod(17)
    def PickSingleDialDeviceAsyncWithPlacement(self, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_commethod(18)
    def Hide(self) -> Void: ...
    @winrt_commethod(19)
    def SetDisplayStatus(self, device: win32more.Windows.Media.DialProtocol.DialDevice, status: win32more.Windows.Media.DialProtocol.DialDeviceDisplayStatus) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class IDialDevicePickerFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDevicePickerFilter'
    _iid_ = Guid('{c17c93ba-86c0-485d-b8d6-0f9a8f641590}')
    @winrt_commethod(6)
    def get_SupportedAppNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedAppNames = property(get_SupportedAppNames, None)
class IDialDeviceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDeviceSelectedEventArgs'
    _iid_ = Guid('{480b92ad-ac76-47eb-9c06-a19304da0247}')
    @winrt_commethod(6)
    def get_SelectedDialDevice(self) -> win32more.Windows.Media.DialProtocol.DialDevice: ...
    SelectedDialDevice = property(get_SelectedDialDevice, None)
class IDialDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDeviceStatics'
    _iid_ = Guid('{aa69cc95-01f8-4758-8461-2bbd1cdc3cf3}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, appName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, value: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.DialProtocol.DialDevice]: ...
    @winrt_commethod(8)
    def DeviceInfoSupportsDialAsync(self, device: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IDialDisconnectButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialDisconnectButtonClickedEventArgs'
    _iid_ = Guid('{52765152-9c81-4e55-adc2-0ebe99cde3b6}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Media.DialProtocol.DialDevice: ...
    Device = property(get_Device, None)
class IDialReceiverApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialReceiverApp'
    _iid_ = Guid('{fd3e7c57-5045-470e-b304-4dd9b13e7d11}')
    @winrt_commethod(6)
    def GetAdditionalDataAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]]: ...
    @winrt_commethod(7)
    def SetAdditionalDataAsync(self, additionalData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IDialReceiverApp2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialReceiverApp2'
    _iid_ = Guid('{530c5805-9130-42ac-a504-1977dcb2ea8a}')
    @winrt_commethod(6)
    def GetUniqueDeviceNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class IDialReceiverAppStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.DialProtocol.IDialReceiverAppStatics'
    _iid_ = Guid('{53183a3c-4c36-4d02-b28a-f2a9da38ec52}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.Media.DialProtocol.DialReceiverApp: ...
    Current = property(get_Current, None)
make_ready(__name__)
