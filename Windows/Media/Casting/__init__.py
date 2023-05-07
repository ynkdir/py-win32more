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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.Casting
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
class CastingConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Casting.ICastingConnection
    _classid_ = 'Windows.Media.Casting.CastingConnection'
    @winrt_mixinmethod
    def get_State(self: Windows.Media.Casting.ICastingConnection) -> Windows.Media.Casting.CastingConnectionState: ...
    @winrt_mixinmethod
    def get_Device(self: Windows.Media.Casting.ICastingConnection) -> Windows.Media.Casting.CastingDevice: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Media.Casting.ICastingConnection) -> Windows.Media.Casting.CastingSource: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.Media.Casting.ICastingConnection, value: Windows.Media.Casting.CastingSource) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Media.Casting.ICastingConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingConnection, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Media.Casting.ICastingConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: Windows.Media.Casting.ICastingConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingConnection, Windows.Media.Casting.CastingConnectionErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: Windows.Media.Casting.ICastingConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestStartCastingAsync(self: Windows.Media.Casting.ICastingConnection, value: Windows.Media.Casting.CastingSource) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    @winrt_mixinmethod
    def DisconnectAsync(self: Windows.Media.Casting.ICastingConnection) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    State = property(get_State, None)
    Device = property(get_Device, None)
    Source = property(get_Source, put_Source)
class CastingConnectionErrorOccurredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs
    _classid_ = 'Windows.Media.Casting.CastingConnectionErrorOccurredEventArgs'
    @winrt_mixinmethod
    def get_ErrorStatus(self: Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs) -> Windows.Media.Casting.CastingConnectionErrorStatus: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs) -> WinRT_String: ...
    ErrorStatus = property(get_ErrorStatus, None)
    Message = property(get_Message, None)
CastingConnectionErrorStatus = Int32
CastingConnectionErrorStatus_Succeeded: CastingConnectionErrorStatus = 0
CastingConnectionErrorStatus_DeviceDidNotRespond: CastingConnectionErrorStatus = 1
CastingConnectionErrorStatus_DeviceError: CastingConnectionErrorStatus = 2
CastingConnectionErrorStatus_DeviceLocked: CastingConnectionErrorStatus = 3
CastingConnectionErrorStatus_ProtectedPlaybackFailed: CastingConnectionErrorStatus = 4
CastingConnectionErrorStatus_InvalidCastingSource: CastingConnectionErrorStatus = 5
CastingConnectionErrorStatus_Unknown: CastingConnectionErrorStatus = 6
CastingConnectionState = Int32
CastingConnectionState_Disconnected: CastingConnectionState = 0
CastingConnectionState_Connected: CastingConnectionState = 1
CastingConnectionState_Rendering: CastingConnectionState = 2
CastingConnectionState_Disconnecting: CastingConnectionState = 3
CastingConnectionState_Connecting: CastingConnectionState = 4
class CastingDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Casting.ICastingDevice
    _classid_ = 'Windows.Media.Casting.CastingDevice'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Casting.ICastingDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Media.Casting.ICastingDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Icon(self: Windows.Media.Casting.ICastingDevice) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def GetSupportedCastingPlaybackTypesAsync(self: Windows.Media.Casting.ICastingDevice) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingPlaybackTypes]: ...
    @winrt_mixinmethod
    def CreateCastingConnection(self: Windows.Media.Casting.ICastingDevice) -> Windows.Media.Casting.CastingConnection: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Media.Casting.ICastingDeviceStatics, type: Windows.Media.Casting.CastingPlaybackTypes) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromCastingSourceAsync(cls: Windows.Media.Casting.ICastingDeviceStatics, castingSource: Windows.Media.Casting.CastingSource) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Media.Casting.ICastingDeviceStatics, value: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingDevice]: ...
    @winrt_classmethod
    def DeviceInfoSupportsCastingAsync(cls: Windows.Media.Casting.ICastingDeviceStatics, device: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Id = property(get_Id, None)
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
class CastingDevicePicker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Casting.ICastingDevicePicker
    _classid_ = 'Windows.Media.Casting.CastingDevicePicker'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Casting.CastingDevicePicker: ...
    @winrt_mixinmethod
    def get_Filter(self: Windows.Media.Casting.ICastingDevicePicker) -> Windows.Media.Casting.CastingDevicePickerFilter: ...
    @winrt_mixinmethod
    def get_Appearance(self: Windows.Media.Casting.ICastingDevicePicker) -> Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_mixinmethod
    def add_CastingDeviceSelected(self: Windows.Media.Casting.ICastingDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingDevicePicker, Windows.Media.Casting.CastingDeviceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CastingDeviceSelected(self: Windows.Media.Casting.ICastingDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CastingDevicePickerDismissed(self: Windows.Media.Casting.ICastingDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingDevicePicker, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CastingDevicePickerDismissed(self: Windows.Media.Casting.ICastingDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Show(self: Windows.Media.Casting.ICastingDevicePicker, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPlacement(self: Windows.Media.Casting.ICastingDevicePicker, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def Hide(self: Windows.Media.Casting.ICastingDevicePicker) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class CastingDevicePickerFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Casting.ICastingDevicePickerFilter
    _classid_ = 'Windows.Media.Casting.CastingDevicePickerFilter'
    @winrt_mixinmethod
    def get_SupportsAudio(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsAudio(self: Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsVideo(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsVideo(self: Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsPictures(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsPictures(self: Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedCastingSources(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Windows.Foundation.Collections.IVector[Windows.Media.Casting.CastingSource]: ...
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    SupportsPictures = property(get_SupportsPictures, put_SupportsPictures)
    SupportedCastingSources = property(get_SupportedCastingSources, None)
class CastingDeviceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Casting.ICastingDeviceSelectedEventArgs
    _classid_ = 'Windows.Media.Casting.CastingDeviceSelectedEventArgs'
    @winrt_mixinmethod
    def get_SelectedCastingDevice(self: Windows.Media.Casting.ICastingDeviceSelectedEventArgs) -> Windows.Media.Casting.CastingDevice: ...
    SelectedCastingDevice = property(get_SelectedCastingDevice, None)
CastingPlaybackTypes = UInt32
CastingPlaybackTypes_None: CastingPlaybackTypes = 0
CastingPlaybackTypes_Audio: CastingPlaybackTypes = 1
CastingPlaybackTypes_Video: CastingPlaybackTypes = 2
CastingPlaybackTypes_Picture: CastingPlaybackTypes = 4
class CastingSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Casting.ICastingSource
    _classid_ = 'Windows.Media.Casting.CastingSource'
    @winrt_mixinmethod
    def get_PreferredSourceUri(self: Windows.Media.Casting.ICastingSource) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_PreferredSourceUri(self: Windows.Media.Casting.ICastingSource, value: Windows.Foundation.Uri) -> Void: ...
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
class ICastingConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingConnection'
    _iid_ = Guid('{cd951653-c2f1-4498-8b78-5fb4cd3640dd}')
    @winrt_commethod(6)
    def get_State(self: Windows.Media.Casting.ICastingConnection) -> Windows.Media.Casting.CastingConnectionState: ...
    @winrt_commethod(7)
    def get_Device(self: Windows.Media.Casting.ICastingConnection) -> Windows.Media.Casting.CastingDevice: ...
    @winrt_commethod(8)
    def get_Source(self: Windows.Media.Casting.ICastingConnection) -> Windows.Media.Casting.CastingSource: ...
    @winrt_commethod(9)
    def put_Source(self: Windows.Media.Casting.ICastingConnection, value: Windows.Media.Casting.CastingSource) -> Void: ...
    @winrt_commethod(10)
    def add_StateChanged(self: Windows.Media.Casting.ICastingConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingConnection, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StateChanged(self: Windows.Media.Casting.ICastingConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_ErrorOccurred(self: Windows.Media.Casting.ICastingConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingConnection, Windows.Media.Casting.CastingConnectionErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ErrorOccurred(self: Windows.Media.Casting.ICastingConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def RequestStartCastingAsync(self: Windows.Media.Casting.ICastingConnection, value: Windows.Media.Casting.CastingSource) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    @winrt_commethod(15)
    def DisconnectAsync(self: Windows.Media.Casting.ICastingConnection) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingConnectionErrorStatus]: ...
    State = property(get_State, None)
    Device = property(get_Device, None)
    Source = property(get_Source, put_Source)
class ICastingConnectionErrorOccurredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs'
    _iid_ = Guid('{a7fb3c69-8719-4f00-81fb-961863c79a32}')
    @winrt_commethod(6)
    def get_ErrorStatus(self: Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs) -> Windows.Media.Casting.CastingConnectionErrorStatus: ...
    @winrt_commethod(7)
    def get_Message(self: Windows.Media.Casting.ICastingConnectionErrorOccurredEventArgs) -> WinRT_String: ...
    ErrorStatus = property(get_ErrorStatus, None)
    Message = property(get_Message, None)
class ICastingDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDevice'
    _iid_ = Guid('{de721c83-4a43-4ad1-a6d2-2492a796c3f2}')
    @winrt_commethod(6)
    def get_Id(self: Windows.Media.Casting.ICastingDevice) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FriendlyName(self: Windows.Media.Casting.ICastingDevice) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Icon(self: Windows.Media.Casting.ICastingDevice) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(9)
    def GetSupportedCastingPlaybackTypesAsync(self: Windows.Media.Casting.ICastingDevice) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingPlaybackTypes]: ...
    @winrt_commethod(10)
    def CreateCastingConnection(self: Windows.Media.Casting.ICastingDevice) -> Windows.Media.Casting.CastingConnection: ...
    Id = property(get_Id, None)
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
class ICastingDevicePicker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDevicePicker'
    _iid_ = Guid('{dcd39924-0591-49be-aacb-4b82ee756a95}')
    @winrt_commethod(6)
    def get_Filter(self: Windows.Media.Casting.ICastingDevicePicker) -> Windows.Media.Casting.CastingDevicePickerFilter: ...
    @winrt_commethod(7)
    def get_Appearance(self: Windows.Media.Casting.ICastingDevicePicker) -> Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_commethod(8)
    def add_CastingDeviceSelected(self: Windows.Media.Casting.ICastingDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingDevicePicker, Windows.Media.Casting.CastingDeviceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CastingDeviceSelected(self: Windows.Media.Casting.ICastingDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_CastingDevicePickerDismissed(self: Windows.Media.Casting.ICastingDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Casting.CastingDevicePicker, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CastingDevicePickerDismissed(self: Windows.Media.Casting.ICastingDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def Show(self: Windows.Media.Casting.ICastingDevicePicker, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(13)
    def ShowWithPlacement(self: Windows.Media.Casting.ICastingDevicePicker, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(14)
    def Hide(self: Windows.Media.Casting.ICastingDevicePicker) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
class ICastingDevicePickerFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDevicePickerFilter'
    _iid_ = Guid('{be8c619c-b563-4354-ae33-9fdaad8c6291}')
    @winrt_commethod(6)
    def get_SupportsAudio(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_commethod(7)
    def put_SupportsAudio(self: Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SupportsVideo(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_commethod(9)
    def put_SupportsVideo(self: Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_SupportsPictures(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Boolean: ...
    @winrt_commethod(11)
    def put_SupportsPictures(self: Windows.Media.Casting.ICastingDevicePickerFilter, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedCastingSources(self: Windows.Media.Casting.ICastingDevicePickerFilter) -> Windows.Foundation.Collections.IVector[Windows.Media.Casting.CastingSource]: ...
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    SupportsPictures = property(get_SupportsPictures, put_SupportsPictures)
    SupportedCastingSources = property(get_SupportedCastingSources, None)
class ICastingDeviceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDeviceSelectedEventArgs'
    _iid_ = Guid('{dc439e86-dd57-4d0d-9400-af45e4fb3663}')
    @winrt_commethod(6)
    def get_SelectedCastingDevice(self: Windows.Media.Casting.ICastingDeviceSelectedEventArgs) -> Windows.Media.Casting.CastingDevice: ...
    SelectedCastingDevice = property(get_SelectedCastingDevice, None)
class ICastingDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingDeviceStatics'
    _iid_ = Guid('{e7d958d7-4d13-4237-a365-4c4f6a4cfd2f}')
    @winrt_commethod(6)
    def GetDeviceSelector(self: Windows.Media.Casting.ICastingDeviceStatics, type: Windows.Media.Casting.CastingPlaybackTypes) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromCastingSourceAsync(self: Windows.Media.Casting.ICastingDeviceStatics, castingSource: Windows.Media.Casting.CastingSource) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def FromIdAsync(self: Windows.Media.Casting.ICastingDeviceStatics, value: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Casting.CastingDevice]: ...
    @winrt_commethod(9)
    def DeviceInfoSupportsCastingAsync(self: Windows.Media.Casting.ICastingDeviceStatics, device: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ICastingSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Casting.ICastingSource'
    _iid_ = Guid('{f429ea72-3467-47e6-a027-522923e9d727}')
    @winrt_commethod(6)
    def get_PreferredSourceUri(self: Windows.Media.Casting.ICastingSource) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_PreferredSourceUri(self: Windows.Media.Casting.ICastingSource, value: Windows.Foundation.Uri) -> Void: ...
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
make_head(_module, 'CastingConnection')
make_head(_module, 'CastingConnectionErrorOccurredEventArgs')
make_head(_module, 'CastingDevice')
make_head(_module, 'CastingDevicePicker')
make_head(_module, 'CastingDevicePickerFilter')
make_head(_module, 'CastingDeviceSelectedEventArgs')
make_head(_module, 'CastingSource')
make_head(_module, 'ICastingConnection')
make_head(_module, 'ICastingConnectionErrorOccurredEventArgs')
make_head(_module, 'ICastingDevice')
make_head(_module, 'ICastingDevicePicker')
make_head(_module, 'ICastingDevicePickerFilter')
make_head(_module, 'ICastingDeviceSelectedEventArgs')
make_head(_module, 'ICastingDeviceStatics')
make_head(_module, 'ICastingSource')
