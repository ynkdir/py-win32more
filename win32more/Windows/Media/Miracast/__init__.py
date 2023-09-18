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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.Media.Core
import win32more.Windows.Media.Miracast
import win32more.Windows.Storage.Streams
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiver'
    _iid_ = Guid('{7a315258-e444-51b4-aff7-b88daa1229e0}')
    @winrt_commethod(6)
    def GetDefaultSettings(self) -> win32more.Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_commethod(7)
    def GetCurrentSettings(self) -> win32more.Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_commethod(8)
    def GetCurrentSettingsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverSettings]: ...
    @winrt_commethod(9)
    def DisconnectAllAndApplySettings(self, settings: win32more.Windows.Media.Miracast.MiracastReceiverSettings) -> win32more.Windows.Media.Miracast.MiracastReceiverApplySettingsResult: ...
    @winrt_commethod(10)
    def DisconnectAllAndApplySettingsAsync(self, settings: win32more.Windows.Media.Miracast.MiracastReceiverSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverApplySettingsResult]: ...
    @winrt_commethod(11)
    def GetStatus(self) -> win32more.Windows.Media.Miracast.MiracastReceiverStatus: ...
    @winrt_commethod(12)
    def GetStatusAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverStatus]: ...
    @winrt_commethod(13)
    def add_StatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiver, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def CreateSession(self, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.Media.Miracast.MiracastReceiverSession: ...
    @winrt_commethod(16)
    def CreateSessionAsync(self, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverSession]: ...
    @winrt_commethod(17)
    def ClearKnownTransmitters(self) -> Void: ...
    @winrt_commethod(18)
    def RemoveKnownTransmitter(self, transmitter: win32more.Windows.Media.Miracast.MiracastTransmitter) -> Void: ...
class IMiracastReceiverApplySettingsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverApplySettingsResult'
    _iid_ = Guid('{d0aa6272-09cd-58e1-a4f2-5d5143d312f9}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Miracast.MiracastReceiverApplySettingsStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IMiracastReceiverConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverConnection'
    _iid_ = Guid('{704b2f36-d2e5-551f-a854-f822b7917d28}')
    @winrt_commethod(6)
    def Disconnect(self, reason: win32more.Windows.Media.Miracast.MiracastReceiverDisconnectReason) -> Void: ...
    @winrt_commethod(7)
    def DisconnectWithMessage(self, reason: win32more.Windows.Media.Miracast.MiracastReceiverDisconnectReason, message: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def Pause(self) -> Void: ...
    @winrt_commethod(9)
    def PauseAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def Resume(self) -> Void: ...
    @winrt_commethod(11)
    def ResumeAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def get_Transmitter(self) -> win32more.Windows.Media.Miracast.MiracastTransmitter: ...
    @winrt_commethod(13)
    def get_InputDevices(self) -> win32more.Windows.Media.Miracast.MiracastReceiverInputDevices: ...
    @winrt_commethod(14)
    def get_CursorImageChannel(self) -> win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannel: ...
    @winrt_commethod(15)
    def get_StreamControl(self) -> win32more.Windows.Media.Miracast.MiracastReceiverStreamControl: ...
    Transmitter = property(get_Transmitter, None)
    InputDevices = property(get_InputDevices, None)
    CursorImageChannel = property(get_CursorImageChannel, None)
    StreamControl = property(get_StreamControl, None)
class IMiracastReceiverConnectionCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs'
    _iid_ = Guid('{7d8dfa39-307a-5c0f-94bd-d0c69d169982}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_commethod(7)
    def get_Pin(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    Pin = property(get_Pin, None)
class IMiracastReceiverCursorImageChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverCursorImageChannel'
    _iid_ = Guid('{d9ac332d-723a-5a9d-b90a-81153efa2a0f}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MaxImageSize(self) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_commethod(9)
    def get_ImageStream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(10)
    def add_ImageStreamChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannel, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ImageStreamChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PositionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannel, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PositionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    MaxImageSize = property(get_MaxImageSize, None)
    Position = property(get_Position, None)
    ImageStream = property(get_ImageStream, None)
class IMiracastReceiverCursorImageChannelSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings'
    _iid_ = Guid('{ccdbedff-bd00-5b9c-8e4c-00cacf86b634}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_MaxImageSize(self) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_commethod(9)
    def put_MaxImageSize(self, value: win32more.Windows.Graphics.SizeInt32) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    MaxImageSize = property(get_MaxImageSize, put_MaxImageSize)
class IMiracastReceiverDisconnectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverDisconnectedEventArgs'
    _iid_ = Guid('{d9a15e5e-5fee-57e6-b4b0-04727db93229}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.Media.Miracast.MiracastReceiverConnection: ...
    Connection = property(get_Connection, None)
class IMiracastReceiverGameControllerDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverGameControllerDevice'
    _iid_ = Guid('{2d7171e8-bed4-5118-a058-e2477eb5888d}')
    @winrt_commethod(6)
    def get_TransmitInput(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TransmitInput(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsRequestedByTransmitter(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsTransmittingInput(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Mode(self) -> win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode: ...
    @winrt_commethod(11)
    def put_Mode(self, value: win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode) -> Void: ...
    @winrt_commethod(12)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDevice, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransmitInput = property(get_TransmitInput, put_TransmitInput)
    IsRequestedByTransmitter = property(get_IsRequestedByTransmitter, None)
    IsTransmittingInput = property(get_IsTransmittingInput, None)
    Mode = property(get_Mode, put_Mode)
class IMiracastReceiverInputDevices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverInputDevices'
    _iid_ = Guid('{da35bb02-28aa-5ee8-96f5-a42901c66f00}')
    @winrt_commethod(6)
    def get_Keyboard(self) -> win32more.Windows.Media.Miracast.MiracastReceiverKeyboardDevice: ...
    @winrt_commethod(7)
    def get_GameController(self) -> win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDevice: ...
    Keyboard = property(get_Keyboard, None)
    GameController = property(get_GameController, None)
class IMiracastReceiverKeyboardDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverKeyboardDevice'
    _iid_ = Guid('{beb67272-06c0-54ff-ac96-217464ff2501}')
    @winrt_commethod(6)
    def get_TransmitInput(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TransmitInput(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsRequestedByTransmitter(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsTransmittingInput(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverKeyboardDevice, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransmitInput = property(get_TransmitInput, put_TransmitInput)
    IsRequestedByTransmitter = property(get_IsRequestedByTransmitter, None)
    IsTransmittingInput = property(get_IsTransmittingInput, None)
class IMiracastReceiverMediaSourceCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs'
    _iid_ = Guid('{17cf519e-1246-531d-945a-6b158e39c3aa}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_commethod(7)
    def get_MediaSource(self) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(8)
    def get_CursorImageChannelSettings(self) -> win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannelSettings: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    MediaSource = property(get_MediaSource, None)
    CursorImageChannelSettings = property(get_CursorImageChannelSettings, None)
class IMiracastReceiverSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverSession'
    _iid_ = Guid('{1d2bcdb4-ef8b-5209-bfc9-c32116504803}')
    @winrt_commethod(6)
    def add_ConnectionCreated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverSession, win32more.Windows.Media.Miracast.MiracastReceiverConnectionCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ConnectionCreated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_MediaSourceCreated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverSession, win32more.Windows.Media.Miracast.MiracastReceiverMediaSourceCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MediaSourceCreated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Disconnected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverSession, win32more.Windows.Media.Miracast.MiracastReceiverDisconnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Disconnected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_AllowConnectionTakeover(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_AllowConnectionTakeover(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_MaxSimultaneousConnections(self) -> Int32: ...
    @winrt_commethod(15)
    def put_MaxSimultaneousConnections(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def Start(self) -> win32more.Windows.Media.Miracast.MiracastReceiverSessionStartResult: ...
    @winrt_commethod(17)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverSessionStartResult]: ...
    AllowConnectionTakeover = property(get_AllowConnectionTakeover, put_AllowConnectionTakeover)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, put_MaxSimultaneousConnections)
class IMiracastReceiverSessionStartResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverSessionStartResult'
    _iid_ = Guid('{b7c573ee-40ca-51ff-95f2-c9de34f2e90e}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Miracast.MiracastReceiverSessionStartStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IMiracastReceiverSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverSettings'
    _iid_ = Guid('{57cd2f24-c55a-5fbe-9464-eb05307705dd}')
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
    def get_AuthorizationMethod(self) -> win32more.Windows.Media.Miracast.MiracastReceiverAuthorizationMethod: ...
    @winrt_commethod(13)
    def put_AuthorizationMethod(self, value: win32more.Windows.Media.Miracast.MiracastReceiverAuthorizationMethod) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverStatus'
    _iid_ = Guid('{c28a5591-23ab-519e-ad09-90bff6dcc87e}')
    @winrt_commethod(6)
    def get_ListeningStatus(self) -> win32more.Windows.Media.Miracast.MiracastReceiverListeningStatus: ...
    @winrt_commethod(7)
    def get_WiFiStatus(self) -> win32more.Windows.Media.Miracast.MiracastReceiverWiFiStatus: ...
    @winrt_commethod(8)
    def get_IsConnectionTakeoverSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_MaxSimultaneousConnections(self) -> Int32: ...
    @winrt_commethod(10)
    def get_KnownTransmitters(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Miracast.MiracastTransmitter]: ...
    ListeningStatus = property(get_ListeningStatus, None)
    WiFiStatus = property(get_WiFiStatus, None)
    IsConnectionTakeoverSupported = property(get_IsConnectionTakeoverSupported, None)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, None)
    KnownTransmitters = property(get_KnownTransmitters, None)
class IMiracastReceiverStreamControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverStreamControl'
    _iid_ = Guid('{38ea2d8b-2769-5ad7-8a8a-254b9df7ba82}')
    @winrt_commethod(6)
    def GetVideoStreamSettings(self) -> win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings: ...
    @winrt_commethod(7)
    def GetVideoStreamSettingsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings]: ...
    @winrt_commethod(8)
    def SuggestVideoStreamSettings(self, settings: win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> Void: ...
    @winrt_commethod(9)
    def SuggestVideoStreamSettingsAsync(self, settings: win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def get_MuteAudio(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_MuteAudio(self, value: Boolean) -> Void: ...
    MuteAudio = property(get_MuteAudio, put_MuteAudio)
class IMiracastReceiverVideoStreamSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings'
    _iid_ = Guid('{169b5e1b-149d-52d0-b126-6f89744e4f50}')
    @winrt_commethod(6)
    def get_Size(self) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_commethod(7)
    def put_Size(self, value: win32more.Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_commethod(8)
    def get_Bitrate(self) -> Int32: ...
    @winrt_commethod(9)
    def put_Bitrate(self, value: Int32) -> Void: ...
    Size = property(get_Size, put_Size)
    Bitrate = property(get_Bitrate, put_Bitrate)
class IMiracastTransmitter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Miracast.IMiracastTransmitter'
    _iid_ = Guid('{342d79fd-2e64-5508-8a30-833d1eac70d0}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AuthorizationStatus(self) -> win32more.Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus: ...
    @winrt_commethod(9)
    def put_AuthorizationStatus(self, value: win32more.Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus) -> Void: ...
    @winrt_commethod(10)
    def GetConnections(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Miracast.MiracastReceiverConnection]: ...
    @winrt_commethod(11)
    def get_MacAddress(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_LastConnectionTime(self) -> win32more.Windows.Foundation.DateTime: ...
    Name = property(get_Name, put_Name)
    AuthorizationStatus = property(get_AuthorizationStatus, put_AuthorizationStatus)
    MacAddress = property(get_MacAddress, None)
    LastConnectionTime = property(get_LastConnectionTime, None)
class MiracastReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiver
    _classid_ = 'Windows.Media.Miracast.MiracastReceiver'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Miracast.MiracastReceiver: ...
    @winrt_mixinmethod
    def GetDefaultSettings(self: win32more.Windows.Media.Miracast.IMiracastReceiver) -> win32more.Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_mixinmethod
    def GetCurrentSettings(self: win32more.Windows.Media.Miracast.IMiracastReceiver) -> win32more.Windows.Media.Miracast.MiracastReceiverSettings: ...
    @winrt_mixinmethod
    def GetCurrentSettingsAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiver) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverSettings]: ...
    @winrt_mixinmethod
    def DisconnectAllAndApplySettings(self: win32more.Windows.Media.Miracast.IMiracastReceiver, settings: win32more.Windows.Media.Miracast.MiracastReceiverSettings) -> win32more.Windows.Media.Miracast.MiracastReceiverApplySettingsResult: ...
    @winrt_mixinmethod
    def DisconnectAllAndApplySettingsAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiver, settings: win32more.Windows.Media.Miracast.MiracastReceiverSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverApplySettingsResult]: ...
    @winrt_mixinmethod
    def GetStatus(self: win32more.Windows.Media.Miracast.IMiracastReceiver) -> win32more.Windows.Media.Miracast.MiracastReceiverStatus: ...
    @winrt_mixinmethod
    def GetStatusAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiver) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverStatus]: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.Media.Miracast.IMiracastReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiver, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.Media.Miracast.IMiracastReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateSession(self: win32more.Windows.Media.Miracast.IMiracastReceiver, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.Media.Miracast.MiracastReceiverSession: ...
    @winrt_mixinmethod
    def CreateSessionAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiver, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverSession]: ...
    @winrt_mixinmethod
    def ClearKnownTransmitters(self: win32more.Windows.Media.Miracast.IMiracastReceiver) -> Void: ...
    @winrt_mixinmethod
    def RemoveKnownTransmitter(self: win32more.Windows.Media.Miracast.IMiracastReceiver, transmitter: win32more.Windows.Media.Miracast.MiracastTransmitter) -> Void: ...
class MiracastReceiverApplySettingsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverApplySettingsResult
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverApplySettingsResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Miracast.IMiracastReceiverApplySettingsResult) -> win32more.Windows.Media.Miracast.MiracastReceiverApplySettingsStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Miracast.IMiracastReceiverApplySettingsResult) -> win32more.Windows.Foundation.HResult: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverConnection
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverConnection'
    @winrt_mixinmethod
    def Disconnect(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection, reason: win32more.Windows.Media.Miracast.MiracastReceiverDisconnectReason) -> Void: ...
    @winrt_mixinmethod
    def DisconnectWithMessage(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection, reason: win32more.Windows.Media.Miracast.MiracastReceiverDisconnectReason, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> Void: ...
    @winrt_mixinmethod
    def PauseAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> Void: ...
    @winrt_mixinmethod
    def ResumeAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Transmitter(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> win32more.Windows.Media.Miracast.MiracastTransmitter: ...
    @winrt_mixinmethod
    def get_InputDevices(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> win32more.Windows.Media.Miracast.MiracastReceiverInputDevices: ...
    @winrt_mixinmethod
    def get_CursorImageChannel(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannel: ...
    @winrt_mixinmethod
    def get_StreamControl(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnection) -> win32more.Windows.Media.Miracast.MiracastReceiverStreamControl: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Transmitter = property(get_Transmitter, None)
    InputDevices = property(get_InputDevices, None)
    CursorImageChannel = property(get_CursorImageChannel, None)
    StreamControl = property(get_StreamControl, None)
class MiracastReceiverConnectionCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverConnectionCreatedEventArgs'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs) -> win32more.Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_mixinmethod
    def get_Pin(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.Miracast.IMiracastReceiverConnectionCreatedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    Pin = property(get_Pin, None)
class MiracastReceiverCursorImageChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverCursorImageChannel'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxImageSize(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_mixinmethod
    def get_ImageStream(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def add_ImageStreamChanged(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannel, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageStreamChanged(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PositionChanged(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannel, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PositionChanged(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannel, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    MaxImageSize = property(get_MaxImageSize, None)
    Position = property(get_Position, None)
    ImageStream = property(get_ImageStream, None)
class MiracastReceiverCursorImageChannelSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverCursorImageChannelSettings'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxImageSize(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def put_MaxImageSize(self: win32more.Windows.Media.Miracast.IMiracastReceiverCursorImageChannelSettings, value: win32more.Windows.Graphics.SizeInt32) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverDisconnectedEventArgs
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverDisconnectedEventArgs'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Media.Miracast.IMiracastReceiverDisconnectedEventArgs) -> win32more.Windows.Media.Miracast.MiracastReceiverConnection: ...
    Connection = property(get_Connection, None)
class MiracastReceiverGameControllerDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverGameControllerDevice'
    @winrt_mixinmethod
    def get_TransmitInput(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransmitInput(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRequestedByTransmitter(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTransmittingInput(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice) -> win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, value: win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode) -> Void: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDevice, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.Media.Miracast.IMiracastReceiverGameControllerDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransmitInput = property(get_TransmitInput, put_TransmitInput)
    IsRequestedByTransmitter = property(get_IsRequestedByTransmitter, None)
    IsTransmittingInput = property(get_IsTransmittingInput, None)
    Mode = property(get_Mode, put_Mode)
MiracastReceiverGameControllerDeviceUsageMode = Int32
MiracastReceiverGameControllerDeviceUsageMode_AsGameController: MiracastReceiverGameControllerDeviceUsageMode = 0
MiracastReceiverGameControllerDeviceUsageMode_AsMouseAndKeyboard: MiracastReceiverGameControllerDeviceUsageMode = 1
class MiracastReceiverInputDevices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverInputDevices
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverInputDevices'
    @winrt_mixinmethod
    def get_Keyboard(self: win32more.Windows.Media.Miracast.IMiracastReceiverInputDevices) -> win32more.Windows.Media.Miracast.MiracastReceiverKeyboardDevice: ...
    @winrt_mixinmethod
    def get_GameController(self: win32more.Windows.Media.Miracast.IMiracastReceiverInputDevices) -> win32more.Windows.Media.Miracast.MiracastReceiverGameControllerDevice: ...
    Keyboard = property(get_Keyboard, None)
    GameController = property(get_GameController, None)
class MiracastReceiverKeyboardDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverKeyboardDevice
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverKeyboardDevice'
    @winrt_mixinmethod
    def get_TransmitInput(self: win32more.Windows.Media.Miracast.IMiracastReceiverKeyboardDevice) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransmitInput(self: win32more.Windows.Media.Miracast.IMiracastReceiverKeyboardDevice, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRequestedByTransmitter(self: win32more.Windows.Media.Miracast.IMiracastReceiverKeyboardDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTransmittingInput(self: win32more.Windows.Media.Miracast.IMiracastReceiverKeyboardDevice) -> Boolean: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.Media.Miracast.IMiracastReceiverKeyboardDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverKeyboardDevice, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.Media.Miracast.IMiracastReceiverKeyboardDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverMediaSourceCreatedEventArgs'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> win32more.Windows.Media.Miracast.MiracastReceiverConnection: ...
    @winrt_mixinmethod
    def get_MediaSource(self: win32more.Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_mixinmethod
    def get_CursorImageChannelSettings(self: win32more.Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> win32more.Windows.Media.Miracast.MiracastReceiverCursorImageChannelSettings: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.Miracast.IMiracastReceiverMediaSourceCreatedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Connection = property(get_Connection, None)
    MediaSource = property(get_MediaSource, None)
    CursorImageChannelSettings = property(get_CursorImageChannelSettings, None)
class MiracastReceiverSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverSession
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverSession'
    @winrt_mixinmethod
    def add_ConnectionCreated(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverSession, win32more.Windows.Media.Miracast.MiracastReceiverConnectionCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionCreated(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MediaSourceCreated(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverSession, win32more.Windows.Media.Miracast.MiracastReceiverMediaSourceCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MediaSourceCreated(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Disconnected(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Miracast.MiracastReceiverSession, win32more.Windows.Media.Miracast.MiracastReceiverDisconnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Disconnected(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllowConnectionTakeover(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowConnectionTakeover(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSimultaneousConnections(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxSimultaneousConnections(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession) -> win32more.Windows.Media.Miracast.MiracastReceiverSessionStartResult: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiverSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverSessionStartResult]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    AllowConnectionTakeover = property(get_AllowConnectionTakeover, put_AllowConnectionTakeover)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, put_MaxSimultaneousConnections)
class MiracastReceiverSessionStartResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverSessionStartResult
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverSessionStartResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Miracast.IMiracastReceiverSessionStartResult) -> win32more.Windows.Media.Miracast.MiracastReceiverSessionStartStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Miracast.IMiracastReceiverSessionStartResult) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
MiracastReceiverSessionStartStatus = Int32
MiracastReceiverSessionStartStatus_Success: MiracastReceiverSessionStartStatus = 0
MiracastReceiverSessionStartStatus_UnknownFailure: MiracastReceiverSessionStartStatus = 1
MiracastReceiverSessionStartStatus_MiracastNotSupported: MiracastReceiverSessionStartStatus = 2
MiracastReceiverSessionStartStatus_AccessDenied: MiracastReceiverSessionStartStatus = 3
class MiracastReceiverSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverSettings
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverSettings'
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ModelName(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ModelName(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ModelNumber(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ModelNumber(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AuthorizationMethod(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings) -> win32more.Windows.Media.Miracast.MiracastReceiverAuthorizationMethod: ...
    @winrt_mixinmethod
    def put_AuthorizationMethod(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings, value: win32more.Windows.Media.Miracast.MiracastReceiverAuthorizationMethod) -> Void: ...
    @winrt_mixinmethod
    def get_RequireAuthorizationFromKnownTransmitters(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequireAuthorizationFromKnownTransmitters(self: win32more.Windows.Media.Miracast.IMiracastReceiverSettings, value: Boolean) -> Void: ...
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    ModelName = property(get_ModelName, put_ModelName)
    ModelNumber = property(get_ModelNumber, put_ModelNumber)
    AuthorizationMethod = property(get_AuthorizationMethod, put_AuthorizationMethod)
    RequireAuthorizationFromKnownTransmitters = property(get_RequireAuthorizationFromKnownTransmitters, put_RequireAuthorizationFromKnownTransmitters)
class MiracastReceiverStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverStatus
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverStatus'
    @winrt_mixinmethod
    def get_ListeningStatus(self: win32more.Windows.Media.Miracast.IMiracastReceiverStatus) -> win32more.Windows.Media.Miracast.MiracastReceiverListeningStatus: ...
    @winrt_mixinmethod
    def get_WiFiStatus(self: win32more.Windows.Media.Miracast.IMiracastReceiverStatus) -> win32more.Windows.Media.Miracast.MiracastReceiverWiFiStatus: ...
    @winrt_mixinmethod
    def get_IsConnectionTakeoverSupported(self: win32more.Windows.Media.Miracast.IMiracastReceiverStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxSimultaneousConnections(self: win32more.Windows.Media.Miracast.IMiracastReceiverStatus) -> Int32: ...
    @winrt_mixinmethod
    def get_KnownTransmitters(self: win32more.Windows.Media.Miracast.IMiracastReceiverStatus) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Miracast.MiracastTransmitter]: ...
    ListeningStatus = property(get_ListeningStatus, None)
    WiFiStatus = property(get_WiFiStatus, None)
    IsConnectionTakeoverSupported = property(get_IsConnectionTakeoverSupported, None)
    MaxSimultaneousConnections = property(get_MaxSimultaneousConnections, None)
    KnownTransmitters = property(get_KnownTransmitters, None)
class MiracastReceiverStreamControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverStreamControl
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverStreamControl'
    @winrt_mixinmethod
    def GetVideoStreamSettings(self: win32more.Windows.Media.Miracast.IMiracastReceiverStreamControl) -> win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings: ...
    @winrt_mixinmethod
    def GetVideoStreamSettingsAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiverStreamControl) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings]: ...
    @winrt_mixinmethod
    def SuggestVideoStreamSettings(self: win32more.Windows.Media.Miracast.IMiracastReceiverStreamControl, settings: win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> Void: ...
    @winrt_mixinmethod
    def SuggestVideoStreamSettingsAsync(self: win32more.Windows.Media.Miracast.IMiracastReceiverStreamControl, settings: win32more.Windows.Media.Miracast.MiracastReceiverVideoStreamSettings) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_MuteAudio(self: win32more.Windows.Media.Miracast.IMiracastReceiverStreamControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_MuteAudio(self: win32more.Windows.Media.Miracast.IMiracastReceiverStreamControl, value: Boolean) -> Void: ...
    MuteAudio = property(get_MuteAudio, put_MuteAudio)
class MiracastReceiverVideoStreamSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings
    _classid_ = 'Windows.Media.Miracast.MiracastReceiverVideoStreamSettings'
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings, value: win32more.Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Bitrate(self: win32more.Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_Bitrate(self: win32more.Windows.Media.Miracast.IMiracastReceiverVideoStreamSettings, value: Int32) -> Void: ...
    Size = property(get_Size, put_Size)
    Bitrate = property(get_Bitrate, put_Bitrate)
MiracastReceiverWiFiStatus = Int32
MiracastReceiverWiFiStatus_MiracastSupportUndetermined: MiracastReceiverWiFiStatus = 0
MiracastReceiverWiFiStatus_MiracastNotSupported: MiracastReceiverWiFiStatus = 1
MiracastReceiverWiFiStatus_MiracastSupportNotOptimized: MiracastReceiverWiFiStatus = 2
MiracastReceiverWiFiStatus_MiracastSupported: MiracastReceiverWiFiStatus = 3
class MiracastTransmitter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Miracast.IMiracastTransmitter
    _classid_ = 'Windows.Media.Miracast.MiracastTransmitter'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Miracast.IMiracastTransmitter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Media.Miracast.IMiracastTransmitter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AuthorizationStatus(self: win32more.Windows.Media.Miracast.IMiracastTransmitter) -> win32more.Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus: ...
    @winrt_mixinmethod
    def put_AuthorizationStatus(self: win32more.Windows.Media.Miracast.IMiracastTransmitter, value: win32more.Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus) -> Void: ...
    @winrt_mixinmethod
    def GetConnections(self: win32more.Windows.Media.Miracast.IMiracastTransmitter) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Miracast.MiracastReceiverConnection]: ...
    @winrt_mixinmethod
    def get_MacAddress(self: win32more.Windows.Media.Miracast.IMiracastTransmitter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LastConnectionTime(self: win32more.Windows.Media.Miracast.IMiracastTransmitter) -> win32more.Windows.Foundation.DateTime: ...
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
