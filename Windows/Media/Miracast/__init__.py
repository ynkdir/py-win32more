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
import Windows.ApplicationModel.Core
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics
import Windows.Media.Core
import Windows.Media.Miracast
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IMiracastReceiver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7a315258-e444-51b4-af-f7-b8-8d-aa-12-29-e0')
    @winrt_commethod(6)
    def GetDefaultSettings(self) -> Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_commethod(7)
    def GetCurrentSettings(self) -> Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_commethod(8)
    def GetCurrentSettingsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverSettings]: ...
    @winrt_commethod(9)
    def DisconnectAllAndApplySettings(self, settings: Windows.Media.Miracast.MiracastReceiverSettings) -> Windows.Media.Miracast.MiracastReceiverApplySettingsResult: ...
    @winrt_commethod(10)
    def DisconnectAllAndApplySettingsAsync(self, settings: Windows.Media.Miracast.MiracastReceiverSettings) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverApplySettingsResult]: ...
    @winrt_commethod(11)
    def GetStatus(self) -> Windows.Media.Miracast.MiracastReceiverStatus: ...
    @winrt_commethod(12)
    def GetStatusAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverStatus]: ...
    @winrt_commethod(13)
    def add_StatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def CreateSession(self, view: Windows.ApplicationModel.Core.CoreApplicationView) -> Windows.Media.Miracast.MiracastReceiverSession: ...
    @winrt_commethod(16)
    def CreateSessionAsync(self, view: Windows.ApplicationModel.Core.CoreApplicationView) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverSession]: ...
    @winrt_commethod(17)
    def ClearKnownTransmitters(self) -> Void: ...
    @winrt_commethod(18)
    def RemoveKnownTransmitter(self, transmitter: Windows.Media.Miracast.MiracastTransmitter) -> Void: ...
class IMiracastReceiverApplySettingsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d0aa6272-09cd-58e1-a4-f2-5d-51-43-d3-12-f9')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.Miracast.MiracastReceiverApplySettingsStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IMiracastReceiverConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('704b2f36-d2e5-551f-a8-54-f8-22-b7-91-7d-28')
    @winrt_commethod(6)
    def Disconnect(self, reason: Windows.Media.Miracast.MiracastReceiverDisconnectReason) -> Void: ...
    @winrt_commethod(7)
    def DisconnectWithMessage(self, reason: Windows.Media.Miracast.MiracastReceiverDisconnectReason, message: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def Pause(self) -> Void: ...
    @winrt_commethod(9)
    def PauseAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def Resume(self) -> Void: ...
    @winrt_commethod(11)
    def ResumeAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def get_Transmitter(self) -> Windows.Media.Miracast.MiracastTransmitter: ...
    @winrt_commethod(13)
    def get_InputDevices(self) -> Windows.Media.Miracast.MiracastReceiverInputDevices: ...
    @winrt_commethod(14)
    def get_CursorImageChannel(self) -> Windows.Media.Miracast.MiracastReceiverCursorImageChannel: ...
    @winrt_commethod(15)
    def get_StreamControl(self) -> Windows.Media.Miracast.MiracastReceiverStreamControl: ...
    Transmitter = property(get_Transmitter, None)
    InputDevices = property(get_InputDevices, None)
    CursorImageChannel = property(get_CursorImageChannel, None)
    StreamControl = property(get_StreamControl, None)
class IMiracastReceiverConnectionCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7d8dfa39-307a-5c0f-94-bd-d0-c6-9d-16-99-82')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_commethod(7)
    def get_Pin(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    Pin = property(get_Pin, None)
class IMiracastReceiverCursorImageChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d9ac332d-723a-5a9d-b9-0a-81-15-3e-fa-2a-0f')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MaxImageSize(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Graphics.PointInt32: ...
    @winrt_commethod(9)
    def get_ImageStream(self) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(10)
    def add_ImageStreamChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverCursorImageChannel, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ImageStreamChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PositionChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverCursorImageChannel, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PositionChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    MaxImageSize = property(get_MaxImageSize, None)
    Position = property(get_Position, None)
    ImageStream = property(get_ImageStream, None)
class IMiracastReceiverCursorImageChannelSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ccdbedff-bd00-5b9c-8e-4c-00-ca-cf-86-b6-34')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_MaxImageSize(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(9)
    def put_MaxImageSize(self, value: Windows.Graphics.SizeInt32) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    MaxImageSize = property(get_MaxImageSize, put_MaxImageSize)
class IMiracastReceiverDisconnectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d9a15e5e-5fee-57e6-b4-b0-04-72-7d-b9-32-29')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.Media.Miracast.MiracastReceiverConnection: ...
    Connection = property(get_Connection, None)
class IMiracastReceiverGameControllerDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2d7171e8-bed4-5118-a0-58-e2-47-7e-b5-88-8d')
    @winrt_commethod(6)
    def get_TransmitInput(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TransmitInput(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsRequestedByTransmitter(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsTransmittingInput(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Mode(self) -> Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode: ...
    @winrt_commethod(11)
    def put_Mode(self, value: Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode) -> Void: ...
    @winrt_commethod(12)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverGameControllerDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransmitInput = property(get_TransmitInput, put_TransmitInput)
    IsRequestedByTransmitter = property(get_IsRequestedByTransmitter, None)
    IsTransmittingInput = property(get_IsTransmittingInput, None)
    Mode = property(get_Mode, put_Mode)
class IMiracastReceiverInputDevices(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('da35bb02-28aa-5ee8-96-f5-a4-29-01-c6-6f-00')
    @winrt_commethod(6)
    def get_Keyboard(self) -> Windows.Media.Miracast.MiracastReceiverKeyboardDevice: ...
    @winrt_commethod(7)
    def get_GameController(self) -> Windows.Media.Miracast.MiracastReceiverGameControllerDevice: ...
    Keyboard = property(get_Keyboard, None)
    GameController = property(get_GameController, None)
class IMiracastReceiverKeyboardDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('beb67272-06c0-54ff-ac-96-21-74-64-ff-25-01')
    @winrt_commethod(6)
    def get_TransmitInput(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TransmitInput(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsRequestedByTransmitter(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsTransmittingInput(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverKeyboardDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransmitInput = property(get_TransmitInput, put_TransmitInput)
    IsRequestedByTransmitter = property(get_IsRequestedByTransmitter, None)
    IsTransmittingInput = property(get_IsTransmittingInput, None)
class IMiracastReceiverMediaSourceCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('17cf519e-1246-531d-94-5a-6b-15-8e-39-c3-aa')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_commethod(7)
    def get_MediaSource(self) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(8)
    def get_CursorImageChannelSettings(self) -> Windows.Media.Miracast.MiracastReceiverCursorImageChannelSettings: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    MediaSource = property(get_MediaSource, None)
    CursorImageChannelSettings = property(get_CursorImageChannelSettings, None)
class IMiracastReceiverSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1d2bcdb4-ef8b-5209-bf-c9-c3-21-16-50-48-03')
    @winrt_commethod(6)
    def add_ConnectionCreated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverSession, Windows.Media.Miracast.MiracastReceiverConnectionCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ConnectionCreated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_MediaSourceCreated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverSession, Windows.Media.Miracast.MiracastReceiverMediaSourceCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MediaSourceCreated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Disconnected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverSession, Windows.Media.Miracast.MiracastReceiverDisconnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Disconnected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_AllowConnectionTakeover(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_AllowConnectionTakeover(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_MaxSimultaneousConnections(self) -> Int32: ...
    @winrt_commethod(15)
    def put_MaxSimultaneousConnections(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def Start(self) -> Windows.Media.Miracast.MiracastReceiverSessionStartResult: ...
    @winrt_commethod(17)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverSessionStartResult]: ...
    AllowConnectionTakeover = property(get_AllowConnectionTakeover, put_AllowConnectionTakeover)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, put_MaxSimultaneousConnections)
class IMiracastReceiverSessionStartResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b7c573ee-40ca-51ff-95-f2-c9-de-34-f2-e9-0e')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.Miracast.MiracastReceiverSessionStartStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IMiracastReceiverSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('57cd2f24-c55a-5fbe-94-64-eb-05-30-77-05-dd')
    @winrt_commethod(6)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ModelName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ModelName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ModelNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ModelNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_AuthorizationMethod(self) -> Windows.Media.Miracast.MiracastReceiverAuthorizationMethod: ...
    @winrt_commethod(13)
    def put_AuthorizationMethod(self, value: Windows.Media.Miracast.MiracastReceiverAuthorizationMethod) -> Void: ...
    @winrt_commethod(14)
    def get_RequireAuthorizationFromKnownTransmitters(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_RequireAuthorizationFromKnownTransmitters(self, value: Boolean) -> Void: ...
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    ModelName = property(get_ModelName, put_ModelName)
    ModelNumber = property(get_ModelNumber, put_ModelNumber)
    AuthorizationMethod = property(get_AuthorizationMethod, put_AuthorizationMethod)
    RequireAuthorizationFromKnownTransmitters = property(get_RequireAuthorizationFromKnownTransmitters, put_RequireAuthorizationFromKnownTransmitters)
class IMiracastReceiverStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c28a5591-23ab-519e-ad-09-90-bf-f6-dc-c8-7e')
    @winrt_commethod(6)
    def get_ListeningStatus(self) -> Windows.Media.Miracast.MiracastReceiverListeningStatus: ...
    @winrt_commethod(7)
    def get_WiFiStatus(self) -> Windows.Media.Miracast.MiracastReceiverWiFiStatus: ...
    @winrt_commethod(8)
    def get_IsConnectionTakeoverSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_MaxSimultaneousConnections(self) -> Int32: ...
    @winrt_commethod(10)
    def get_KnownTransmitters(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Miracast.MiracastTransmitter]: ...
    ListeningStatus = property(get_ListeningStatus, None)
    WiFiStatus = property(get_WiFiStatus, None)
    IsConnectionTakeoverSupported = property(get_IsConnectionTakeoverSupported, None)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, None)
    KnownTransmitters = property(get_KnownTransmitters, None)
class IMiracastReceiverStreamControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('38ea2d8b-2769-5ad7-8a-8a-25-4b-9d-f7-ba-82')
    @winrt_commethod(6)
    def GetVideoStreamSettings(self) -> Windows.Media.Miracast.MiracastReceiverVideoStreamSettings: ...
    @winrt_commethod(7)
    def GetVideoStreamSettingsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverVideoStreamSettings]: ...
    @winrt_commethod(8)
    def SuggestVideoStreamSettings(self, settings: Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> Void: ...
    @winrt_commethod(9)
    def SuggestVideoStreamSettingsAsync(self, settings: Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def get_MuteAudio(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_MuteAudio(self, value: Boolean) -> Void: ...
    MuteAudio = property(get_MuteAudio, put_MuteAudio)
class IMiracastReceiverVideoStreamSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('169b5e1b-149d-52d0-b1-26-6f-89-74-4e-4f-50')
    @winrt_commethod(6)
    def get_Size(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(7)
    def put_Size(self, value: Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_commethod(8)
    def get_Bitrate(self) -> Int32: ...
    @winrt_commethod(9)
    def put_Bitrate(self, value: Int32) -> Void: ...
    Size = property(get_Size, put_Size)
    Bitrate = property(get_Bitrate, put_Bitrate)
class IMiracastTransmitter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('342d79fd-2e64-5508-8a-30-83-3d-1e-ac-70-d0')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AuthorizationStatus(self) -> Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus: ...
    @winrt_commethod(9)
    def put_AuthorizationStatus(self, value: Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus) -> Void: ...
    @winrt_commethod(10)
    def GetConnections(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Miracast.MiracastReceiverConnection]: ...
    @winrt_commethod(11)
    def get_MacAddress(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_LastConnectionTime(self) -> Windows.Foundation.DateTime: ...
    Name = property(get_Name, put_Name)
    AuthorizationStatus = property(get_AuthorizationStatus, put_AuthorizationStatus)
    MacAddress = property(get_MacAddress, None)
    LastConnectionTime = property(get_LastConnectionTime, None)
class MiracastReceiver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiver'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Miracast.MiracastReceiver: ...
    @winrt_mixinmethod
    def GetDefaultSettings(self: Windows.Media.Miracast.IMiracastReceiver) -> Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_mixinmethod
    def GetCurrentSettings(self: Windows.Media.Miracast.IMiracastReceiver) -> Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_mixinmethod
    def GetCurrentSettingsAsync(self: Windows.Media.Miracast.IMiracastReceiver) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverSettings]: ...
    @winrt_mixinmethod
    def DisconnectAllAndApplySettings(self: Windows.Media.Miracast.IMiracastReceiver, settings: Windows.Media.Miracast.MiracastReceiverSettings) -> Windows.Media.Miracast.MiracastReceiverApplySettingsResult: ...
    @winrt_mixinmethod
    def DisconnectAllAndApplySettingsAsync(self: Windows.Media.Miracast.IMiracastReceiver, settings: Windows.Media.Miracast.MiracastReceiverSettings) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverApplySettingsResult]: ...
    @winrt_mixinmethod
    def GetStatus(self: Windows.Media.Miracast.IMiracastReceiver) -> Windows.Media.Miracast.MiracastReceiverStatus: ...
    @winrt_mixinmethod
    def GetStatusAsync(self: Windows.Media.Miracast.IMiracastReceiver) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverStatus]: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Media.Miracast.IMiracastReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Media.Miracast.IMiracastReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateSession(self: Windows.Media.Miracast.IMiracastReceiver, view: Windows.ApplicationModel.Core.CoreApplicationView) -> Windows.Media.Miracast.MiracastReceiverSession: ...
    @winrt_mixinmethod
    def CreateSessionAsync(self: Windows.Media.Miracast.IMiracastReceiver, view: Windows.ApplicationModel.Core.CoreApplicationView) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverSession]: ...
    @winrt_mixinmethod
    def ClearKnownTransmitters(self: Windows.Media.Miracast.IMiracastReceiver) -> Void: ...
    @winrt_mixinmethod
    def RemoveKnownTransmitter(self: Windows.Media.Miracast.IMiracastReceiver, transmitter: Windows.Media.Miracast.MiracastTransmitter) -> Void: ...
class MiracastReceiverApplySettingsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverApplySettingsResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.Miracast.IMiracastReceiverApplySettingsResult) -> Windows.Media.Miracast.MiracastReceiverApplySettingsStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Miracast.IMiracastReceiverApplySettingsResult) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
MiracastReceiverApplySettingsStatus = Int32
MiracastReceiverApplySettingsStatus_Success: MiracastReceiverApplySettingsStatus = 0
MiracastReceiverApplySettingsStatus_UnknownFailure: MiracastReceiverApplySettingsStatus = 1
MiracastReceiverApplySettingsStatus_MiracastNotSupported: MiracastReceiverApplySettingsStatus = 2
MiracastReceiverApplySettingsStatus_AccessDenied: MiracastReceiverApplySettingsStatus = 3
MiracastReceiverApplySettingsStatus_FriendlyNameTooLong: MiracastReceiverApplySettingsStatus = 4
MiracastReceiverApplySettingsStatus_ModelNameTooLong: MiracastReceiverApplySettingsStatus = 5
MiracastReceiverApplySettingsStatus_ModelNumberTooLong: MiracastReceiverApplySettingsStatus = 6
MiracastReceiverApplySettingsStatus_InvalidSettings: MiracastReceiverApplySettingsStatus = 7
MiracastReceiverAuthorizationMethod = Int32
MiracastReceiverAuthorizationMethod_None: MiracastReceiverAuthorizationMethod = 0
MiracastReceiverAuthorizationMethod_ConfirmConnection: MiracastReceiverAuthorizationMethod = 1
MiracastReceiverAuthorizationMethod_PinDisplayIfRequested: MiracastReceiverAuthorizationMethod = 2
MiracastReceiverAuthorizationMethod_PinDisplayRequired: MiracastReceiverAuthorizationMethod = 3
class MiracastReceiverConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverConnection'
    @winrt_mixinmethod
    def Disconnect(self: Windows.Media.Miracast.IMiracastReceiverConnection, reason: Windows.Media.Miracast.MiracastReceiverDisconnectReason) -> Void: ...
    @winrt_mixinmethod
    def DisconnectWithMessage(self: Windows.Media.Miracast.IMiracastReceiverConnection, reason: Windows.Media.Miracast.MiracastReceiverDisconnectReason, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Void: ...
    @winrt_mixinmethod
    def PauseAsync(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Resume(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Void: ...
    @winrt_mixinmethod
    def ResumeAsync(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Transmitter(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Windows.Media.Miracast.MiracastTransmitter: ...
    @winrt_mixinmethod
    def get_InputDevices(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Windows.Media.Miracast.MiracastReceiverInputDevices: ...
    @winrt_mixinmethod
    def get_CursorImageChannel(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Windows.Media.Miracast.MiracastReceiverCursorImageChannel: ...
    @winrt_mixinmethod
    def get_StreamControl(self: Windows.Media.Miracast.IMiracastReceiverConnection) -> Windows.Media.Miracast.MiracastReceiverStreamControl: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Transmitter = property(get_Transmitter, None)
    InputDevices = property(get_InputDevices, None)
    CursorImageChannel = property(get_CursorImageChannel, None)
    StreamControl = property(get_StreamControl, None)
class MiracastReceiverConnectionCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverConnectionCreatedEventArgs'
    @winrt_mixinmethod
    def get_Connection(self: Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs) -> Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_mixinmethod
    def get_Pin(self: Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs) -> Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    Pin = property(get_Pin, None)
class MiracastReceiverCursorImageChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverCursorImageChannel'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxImageSize(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> Windows.Graphics.PointInt32: ...
    @winrt_mixinmethod
    def get_ImageStream(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def add_ImageStreamChanged(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverCursorImageChannel, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageStreamChanged(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PositionChanged(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverCursorImageChannel, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PositionChanged(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    MaxImageSize = property(get_MaxImageSize, None)
    Position = property(get_Position, None)
    ImageStream = property(get_ImageStream, None)
class MiracastReceiverCursorImageChannelSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverCursorImageChannelSettings'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxImageSize(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def put_MaxImageSize(self: Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings, value: Windows.Graphics.SizeInt32) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    MaxImageSize = property(get_MaxImageSize, put_MaxImageSize)
MiracastReceiverDisconnectReason = Int32
MiracastReceiverDisconnectReason_Finished: MiracastReceiverDisconnectReason = 0
MiracastReceiverDisconnectReason_AppSpecificError: MiracastReceiverDisconnectReason = 1
MiracastReceiverDisconnectReason_ConnectionNotAccepted: MiracastReceiverDisconnectReason = 2
MiracastReceiverDisconnectReason_DisconnectedByUser: MiracastReceiverDisconnectReason = 3
MiracastReceiverDisconnectReason_FailedToStartStreaming: MiracastReceiverDisconnectReason = 4
MiracastReceiverDisconnectReason_MediaDecodingError: MiracastReceiverDisconnectReason = 5
MiracastReceiverDisconnectReason_MediaStreamingError: MiracastReceiverDisconnectReason = 6
MiracastReceiverDisconnectReason_MediaDecryptionError: MiracastReceiverDisconnectReason = 7
class MiracastReceiverDisconnectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverDisconnectedEventArgs'
    @winrt_mixinmethod
    def get_Connection(self: Windows.Media.Miracast.IMiracastReceiverDisconnectedEventArgs) -> Windows.Media.Miracast.MiracastReceiverConnection: ...
    Connection = property(get_Connection, None)
class MiracastReceiverGameControllerDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverGameControllerDevice'
    @winrt_mixinmethod
    def get_TransmitInput(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransmitInput(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRequestedByTransmitter(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTransmittingInput(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, value: Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode) -> Void: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverGameControllerDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransmitInput = property(get_TransmitInput, put_TransmitInput)
    IsRequestedByTransmitter = property(get_IsRequestedByTransmitter, None)
    IsTransmittingInput = property(get_IsTransmittingInput, None)
    Mode = property(get_Mode, put_Mode)
MiracastReceiverGameControllerDeviceUsageMode = Int32
MiracastReceiverGameControllerDeviceUsageMode_AsGameController: MiracastReceiverGameControllerDeviceUsageMode = 0
MiracastReceiverGameControllerDeviceUsageMode_AsMouseAndKeyboard: MiracastReceiverGameControllerDeviceUsageMode = 1
class MiracastReceiverInputDevices(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverInputDevices'
    @winrt_mixinmethod
    def get_Keyboard(self: Windows.Media.Miracast.IMiracastReceiverInputDevices) -> Windows.Media.Miracast.MiracastReceiverKeyboardDevice: ...
    @winrt_mixinmethod
    def get_GameController(self: Windows.Media.Miracast.IMiracastReceiverInputDevices) -> Windows.Media.Miracast.MiracastReceiverGameControllerDevice: ...
    Keyboard = property(get_Keyboard, None)
    GameController = property(get_GameController, None)
class MiracastReceiverKeyboardDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverKeyboardDevice'
    @winrt_mixinmethod
    def get_TransmitInput(self: Windows.Media.Miracast.IMiracastReceiverKeyboardDevice) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransmitInput(self: Windows.Media.Miracast.IMiracastReceiverKeyboardDevice, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRequestedByTransmitter(self: Windows.Media.Miracast.IMiracastReceiverKeyboardDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTransmittingInput(self: Windows.Media.Miracast.IMiracastReceiverKeyboardDevice) -> Boolean: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.Media.Miracast.IMiracastReceiverKeyboardDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverKeyboardDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.Media.Miracast.IMiracastReceiverKeyboardDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransmitInput = property(get_TransmitInput, put_TransmitInput)
    IsRequestedByTransmitter = property(get_IsRequestedByTransmitter, None)
    IsTransmittingInput = property(get_IsTransmittingInput, None)
MiracastReceiverListeningStatus = Int32
MiracastReceiverListeningStatus_NotListening: MiracastReceiverListeningStatus = 0
MiracastReceiverListeningStatus_Listening: MiracastReceiverListeningStatus = 1
MiracastReceiverListeningStatus_ConnectionPending: MiracastReceiverListeningStatus = 2
MiracastReceiverListeningStatus_Connected: MiracastReceiverListeningStatus = 3
MiracastReceiverListeningStatus_DisabledByPolicy: MiracastReceiverListeningStatus = 4
MiracastReceiverListeningStatus_TemporarilyDisabled: MiracastReceiverListeningStatus = 5
class MiracastReceiverMediaSourceCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverMediaSourceCreatedEventArgs'
    @winrt_mixinmethod
    def get_Connection(self: Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_mixinmethod
    def get_MediaSource(self: Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> Windows.Media.Core.MediaSource: ...
    @winrt_mixinmethod
    def get_CursorImageChannelSettings(self: Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> Windows.Media.Miracast.MiracastReceiverCursorImageChannelSettings: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    MediaSource = property(get_MediaSource, None)
    CursorImageChannelSettings = property(get_CursorImageChannelSettings, None)
class MiracastReceiverSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverSession'
    @winrt_mixinmethod
    def add_ConnectionCreated(self: Windows.Media.Miracast.IMiracastReceiverSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverSession, Windows.Media.Miracast.MiracastReceiverConnectionCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionCreated(self: Windows.Media.Miracast.IMiracastReceiverSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MediaSourceCreated(self: Windows.Media.Miracast.IMiracastReceiverSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverSession, Windows.Media.Miracast.MiracastReceiverMediaSourceCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MediaSourceCreated(self: Windows.Media.Miracast.IMiracastReceiverSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Disconnected(self: Windows.Media.Miracast.IMiracastReceiverSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Miracast.MiracastReceiverSession, Windows.Media.Miracast.MiracastReceiverDisconnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Disconnected(self: Windows.Media.Miracast.IMiracastReceiverSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllowConnectionTakeover(self: Windows.Media.Miracast.IMiracastReceiverSession) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowConnectionTakeover(self: Windows.Media.Miracast.IMiracastReceiverSession, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSimultaneousConnections(self: Windows.Media.Miracast.IMiracastReceiverSession) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxSimultaneousConnections(self: Windows.Media.Miracast.IMiracastReceiverSession, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Media.Miracast.IMiracastReceiverSession) -> Windows.Media.Miracast.MiracastReceiverSessionStartResult: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.Miracast.IMiracastReceiverSession) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverSessionStartResult]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    AllowConnectionTakeover = property(get_AllowConnectionTakeover, put_AllowConnectionTakeover)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, put_MaxSimultaneousConnections)
class MiracastReceiverSessionStartResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverSessionStartResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.Miracast.IMiracastReceiverSessionStartResult) -> Windows.Media.Miracast.MiracastReceiverSessionStartStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Miracast.IMiracastReceiverSessionStartResult) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
MiracastReceiverSessionStartStatus = Int32
MiracastReceiverSessionStartStatus_Success: MiracastReceiverSessionStartStatus = 0
MiracastReceiverSessionStartStatus_UnknownFailure: MiracastReceiverSessionStartStatus = 1
MiracastReceiverSessionStartStatus_MiracastNotSupported: MiracastReceiverSessionStartStatus = 2
MiracastReceiverSessionStartStatus_AccessDenied: MiracastReceiverSessionStartStatus = 3
class MiracastReceiverSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverSettings'
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Media.Miracast.IMiracastReceiverSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: Windows.Media.Miracast.IMiracastReceiverSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ModelName(self: Windows.Media.Miracast.IMiracastReceiverSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ModelName(self: Windows.Media.Miracast.IMiracastReceiverSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ModelNumber(self: Windows.Media.Miracast.IMiracastReceiverSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ModelNumber(self: Windows.Media.Miracast.IMiracastReceiverSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AuthorizationMethod(self: Windows.Media.Miracast.IMiracastReceiverSettings) -> Windows.Media.Miracast.MiracastReceiverAuthorizationMethod: ...
    @winrt_mixinmethod
    def put_AuthorizationMethod(self: Windows.Media.Miracast.IMiracastReceiverSettings, value: Windows.Media.Miracast.MiracastReceiverAuthorizationMethod) -> Void: ...
    @winrt_mixinmethod
    def get_RequireAuthorizationFromKnownTransmitters(self: Windows.Media.Miracast.IMiracastReceiverSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequireAuthorizationFromKnownTransmitters(self: Windows.Media.Miracast.IMiracastReceiverSettings, value: Boolean) -> Void: ...
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    ModelName = property(get_ModelName, put_ModelName)
    ModelNumber = property(get_ModelNumber, put_ModelNumber)
    AuthorizationMethod = property(get_AuthorizationMethod, put_AuthorizationMethod)
    RequireAuthorizationFromKnownTransmitters = property(get_RequireAuthorizationFromKnownTransmitters, put_RequireAuthorizationFromKnownTransmitters)
class MiracastReceiverStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverStatus'
    @winrt_mixinmethod
    def get_ListeningStatus(self: Windows.Media.Miracast.IMiracastReceiverStatus) -> Windows.Media.Miracast.MiracastReceiverListeningStatus: ...
    @winrt_mixinmethod
    def get_WiFiStatus(self: Windows.Media.Miracast.IMiracastReceiverStatus) -> Windows.Media.Miracast.MiracastReceiverWiFiStatus: ...
    @winrt_mixinmethod
    def get_IsConnectionTakeoverSupported(self: Windows.Media.Miracast.IMiracastReceiverStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxSimultaneousConnections(self: Windows.Media.Miracast.IMiracastReceiverStatus) -> Int32: ...
    @winrt_mixinmethod
    def get_KnownTransmitters(self: Windows.Media.Miracast.IMiracastReceiverStatus) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Miracast.MiracastTransmitter]: ...
    ListeningStatus = property(get_ListeningStatus, None)
    WiFiStatus = property(get_WiFiStatus, None)
    IsConnectionTakeoverSupported = property(get_IsConnectionTakeoverSupported, None)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, None)
    KnownTransmitters = property(get_KnownTransmitters, None)
class MiracastReceiverStreamControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverStreamControl'
    @winrt_mixinmethod
    def GetVideoStreamSettings(self: Windows.Media.Miracast.IMiracastReceiverStreamControl) -> Windows.Media.Miracast.MiracastReceiverVideoStreamSettings: ...
    @winrt_mixinmethod
    def GetVideoStreamSettingsAsync(self: Windows.Media.Miracast.IMiracastReceiverStreamControl) -> Windows.Foundation.IAsyncOperation[Windows.Media.Miracast.MiracastReceiverVideoStreamSettings]: ...
    @winrt_mixinmethod
    def SuggestVideoStreamSettings(self: Windows.Media.Miracast.IMiracastReceiverStreamControl, settings: Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> Void: ...
    @winrt_mixinmethod
    def SuggestVideoStreamSettingsAsync(self: Windows.Media.Miracast.IMiracastReceiverStreamControl, settings: Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_MuteAudio(self: Windows.Media.Miracast.IMiracastReceiverStreamControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_MuteAudio(self: Windows.Media.Miracast.IMiracastReceiverStreamControl, value: Boolean) -> Void: ...
    MuteAudio = property(get_MuteAudio, put_MuteAudio)
class MiracastReceiverVideoStreamSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverVideoStreamSettings'
    @winrt_mixinmethod
    def get_Size(self: Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings, value: Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Bitrate(self: Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_Bitrate(self: Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings, value: Int32) -> Void: ...
    Size = property(get_Size, put_Size)
    Bitrate = property(get_Bitrate, put_Bitrate)
MiracastReceiverWiFiStatus = Int32
MiracastReceiverWiFiStatus_MiracastSupportUndetermined: MiracastReceiverWiFiStatus = 0
MiracastReceiverWiFiStatus_MiracastNotSupported: MiracastReceiverWiFiStatus = 1
MiracastReceiverWiFiStatus_MiracastSupportNotOptimized: MiracastReceiverWiFiStatus = 2
MiracastReceiverWiFiStatus_MiracastSupported: MiracastReceiverWiFiStatus = 3
class MiracastTransmitter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.MiracastTransmitter'
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Miracast.IMiracastTransmitter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Media.Miracast.IMiracastTransmitter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AuthorizationStatus(self: Windows.Media.Miracast.IMiracastTransmitter) -> Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus: ...
    @winrt_mixinmethod
    def put_AuthorizationStatus(self: Windows.Media.Miracast.IMiracastTransmitter, value: Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus) -> Void: ...
    @winrt_mixinmethod
    def GetConnections(self: Windows.Media.Miracast.IMiracastTransmitter) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Miracast.MiracastReceiverConnection]: ...
    @winrt_mixinmethod
    def get_MacAddress(self: Windows.Media.Miracast.IMiracastTransmitter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LastConnectionTime(self: Windows.Media.Miracast.IMiracastTransmitter) -> Windows.Foundation.DateTime: ...
    Name = property(get_Name, put_Name)
    AuthorizationStatus = property(get_AuthorizationStatus, put_AuthorizationStatus)
    MacAddress = property(get_MacAddress, None)
    LastConnectionTime = property(get_LastConnectionTime, None)
MiracastTransmitterAuthorizationStatus = Int32
MiracastTransmitterAuthorizationStatus_Undecided: MiracastTransmitterAuthorizationStatus = 0
MiracastTransmitterAuthorizationStatus_Allowed: MiracastTransmitterAuthorizationStatus = 1
MiracastTransmitterAuthorizationStatus_AlwaysPrompt: MiracastTransmitterAuthorizationStatus = 2
MiracastTransmitterAuthorizationStatus_Blocked: MiracastTransmitterAuthorizationStatus = 3
make_head(_module, 'IMiracastReceiver')
make_head(_module, 'IMiracastReceiverApplySettingsResult')
make_head(_module, 'IMiracastReceiverConnection')
make_head(_module, 'IMiracastReceiverConnectionCreatedEventArgs')
make_head(_module, 'IMiracastReceiverCursorImageChannel')
make_head(_module, 'IMiracastReceiverCursorImageChannelSettings')
make_head(_module, 'IMiracastReceiverDisconnectedEventArgs')
make_head(_module, 'IMiracastReceiverGameControllerDevice')
make_head(_module, 'IMiracastReceiverInputDevices')
make_head(_module, 'IMiracastReceiverKeyboardDevice')
make_head(_module, 'IMiracastReceiverMediaSourceCreatedEventArgs')
make_head(_module, 'IMiracastReceiverSession')
make_head(_module, 'IMiracastReceiverSessionStartResult')
make_head(_module, 'IMiracastReceiverSettings')
make_head(_module, 'IMiracastReceiverStatus')
make_head(_module, 'IMiracastReceiverStreamControl')
make_head(_module, 'IMiracastReceiverVideoStreamSettings')
make_head(_module, 'IMiracastTransmitter')
make_head(_module, 'MiracastReceiver')
make_head(_module, 'MiracastReceiverApplySettingsResult')
make_head(_module, 'MiracastReceiverConnection')
make_head(_module, 'MiracastReceiverConnectionCreatedEventArgs')
make_head(_module, 'MiracastReceiverCursorImageChannel')
make_head(_module, 'MiracastReceiverCursorImageChannelSettings')
make_head(_module, 'MiracastReceiverDisconnectedEventArgs')
make_head(_module, 'MiracastReceiverGameControllerDevice')
make_head(_module, 'MiracastReceiverInputDevices')
make_head(_module, 'MiracastReceiverKeyboardDevice')
make_head(_module, 'MiracastReceiverMediaSourceCreatedEventArgs')
make_head(_module, 'MiracastReceiverSession')
make_head(_module, 'MiracastReceiverSessionStartResult')
make_head(_module, 'MiracastReceiverSettings')
make_head(_module, 'MiracastReceiverStatus')
make_head(_module, 'MiracastReceiverStreamControl')
make_head(_module, 'MiracastReceiverVideoStreamSettings')
make_head(_module, 'MiracastTransmitter')
