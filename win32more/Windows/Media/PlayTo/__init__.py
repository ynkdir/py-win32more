from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.PlayTo
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class CurrentTimeChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.ICurrentTimeChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.CurrentTimeChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Time(self: win32more.Windows.Media.PlayTo.ICurrentTimeChangeRequestedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    Time = property(get_Time, None)
class ICurrentTimeChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.ICurrentTimeChangeRequestedEventArgs'
    _iid_ = Guid('{99711324-edc7-4bf5-91f6-3c8627db59e5}')
    @winrt_commethod(6)
    def get_Time(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Time = property(get_Time, None)
class IMuteChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IMuteChangeRequestedEventArgs'
    _iid_ = Guid('{e4b4f5f6-af1f-4f1e-b437-7da32400e1d4}')
    @winrt_commethod(6)
    def get_Mute(self) -> Boolean: ...
    Mute = property(get_Mute, None)
class IPlayToConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnection'
    _iid_ = Guid('{112fbfc8-f235-4fde-8d41-9bf27c9e9a40}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_commethod(7)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToConnection, win32more.Windows.Media.PlayTo.PlayToConnectionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Transferred(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToConnection, win32more.Windows.Media.PlayTo.PlayToConnectionTransferredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Transferred(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Error(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToConnection, win32more.Windows.Media.PlayTo.PlayToConnectionErrorEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Error(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
    StateChanged = event()
    Transferred = event()
    Error = event()
class IPlayToConnectionErrorEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs'
    _iid_ = Guid('{bf5eada6-88e6-445f-9d40-d9b9f8939896}')
    @winrt_commethod(6)
    def get_Code(self) -> win32more.Windows.Media.PlayTo.PlayToConnectionError: ...
    @winrt_commethod(7)
    def get_Message(self) -> WinRT_String: ...
    Code = property(get_Code, None)
    Message = property(get_Message, None)
class IPlayToConnectionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs'
    _iid_ = Guid('{68c4b50f-0c20-4980-8602-58c62238d423}')
    @winrt_commethod(6)
    def get_PreviousState(self) -> win32more.Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_commethod(7)
    def get_CurrentState(self) -> win32more.Windows.Media.PlayTo.PlayToConnectionState: ...
    CurrentState = property(get_CurrentState, None)
    PreviousState = property(get_PreviousState, None)
class IPlayToConnectionTransferredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs'
    _iid_ = Guid('{fae3193a-0683-47d9-8df0-18cbb48984d8}')
    @winrt_commethod(6)
    def get_PreviousSource(self) -> win32more.Windows.Media.PlayTo.PlayToSource: ...
    @winrt_commethod(7)
    def get_CurrentSource(self) -> win32more.Windows.Media.PlayTo.PlayToSource: ...
    CurrentSource = property(get_CurrentSource, None)
    PreviousSource = property(get_PreviousSource, None)
class IPlayToManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToManager'
    _iid_ = Guid('{f56a206e-1b77-42ef-8f0d-b949f8d9b260}')
    @winrt_commethod(6)
    def add_SourceRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToManager, win32more.Windows.Media.PlayTo.PlayToSourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceSelected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToManager, win32more.Windows.Media.PlayTo.PlayToSourceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceSelected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def put_DefaultSourceSelection(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_DefaultSourceSelection(self) -> Boolean: ...
    DefaultSourceSelection = property(get_DefaultSourceSelection, put_DefaultSourceSelection)
    SourceRequested = event()
    SourceSelected = event()
class IPlayToManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToManagerStatics'
    _iid_ = Guid('{64e6a887-3982-4f3b-ba20-6155e435325b}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Media.PlayTo.PlayToManager: ...
    @winrt_commethod(7)
    def ShowPlayToUI(self) -> Void: ...
class IPlayToReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToReceiver'
    _iid_ = Guid('{ac15cf47-a162-4aa6-af1b-3aa35f3b9069}')
    @winrt_commethod(6)
    def add_PlayRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PlayRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PauseRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PauseRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SourceChangeRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.SourceChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SourceChangeRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PlaybackRateChangeRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.PlaybackRateChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PlaybackRateChangeRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CurrentTimeChangeRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.CurrentTimeChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CurrentTimeChangeRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_MuteChangeRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.MuteChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_MuteChangeRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_VolumeChangeRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.VolumeChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_VolumeChangeRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_TimeUpdateRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_TimeUpdateRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_StopRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_StopRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def NotifyVolumeChange(self, volume: Double, mute: Boolean) -> Void: ...
    @winrt_commethod(25)
    def NotifyRateChange(self, rate: Double) -> Void: ...
    @winrt_commethod(26)
    def NotifyLoadedMetadata(self) -> Void: ...
    @winrt_commethod(27)
    def NotifyTimeUpdate(self, currentTime: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(28)
    def NotifyDurationChange(self, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(29)
    def NotifySeeking(self) -> Void: ...
    @winrt_commethod(30)
    def NotifySeeked(self) -> Void: ...
    @winrt_commethod(31)
    def NotifyPaused(self) -> Void: ...
    @winrt_commethod(32)
    def NotifyPlaying(self) -> Void: ...
    @winrt_commethod(33)
    def NotifyEnded(self) -> Void: ...
    @winrt_commethod(34)
    def NotifyError(self) -> Void: ...
    @winrt_commethod(35)
    def NotifyStopped(self) -> Void: ...
    @winrt_commethod(36)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(38)
    def put_SupportsImage(self, value: Boolean) -> Void: ...
    @winrt_commethod(39)
    def get_SupportsImage(self) -> Boolean: ...
    @winrt_commethod(40)
    def put_SupportsAudio(self, value: Boolean) -> Void: ...
    @winrt_commethod(41)
    def get_SupportsAudio(self) -> Boolean: ...
    @winrt_commethod(42)
    def put_SupportsVideo(self, value: Boolean) -> Void: ...
    @winrt_commethod(43)
    def get_SupportsVideo(self) -> Boolean: ...
    @winrt_commethod(44)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(45)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(46)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    Properties = property(get_Properties, None)
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsImage = property(get_SupportsImage, put_SupportsImage)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    PlayRequested = event()
    PauseRequested = event()
    SourceChangeRequested = event()
    PlaybackRateChangeRequested = event()
    CurrentTimeChangeRequested = event()
    MuteChangeRequested = event()
    VolumeChangeRequested = event()
    TimeUpdateRequested = event()
    StopRequested = event()
class IPlayToSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSource'
    _iid_ = Guid('{7f138a08-fbb7-4b09-8356-aa5f4e335c31}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.Media.PlayTo.PlayToConnection: ...
    @winrt_commethod(7)
    def get_Next(self) -> win32more.Windows.Media.PlayTo.PlayToSource: ...
    @winrt_commethod(8)
    def put_Next(self, value: win32more.Windows.Media.PlayTo.PlayToSource) -> Void: ...
    @winrt_commethod(9)
    def PlayNext(self) -> Void: ...
    Connection = property(get_Connection, None)
    Next = property(get_Next, put_Next)
class IPlayToSourceDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceDeferral'
    _iid_ = Guid('{4100891d-278e-4f29-859b-a9e501053e7d}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPlayToSourceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceRequest'
    _iid_ = Guid('{f8584665-64f4-44a0-ac0d-468d2b8fda83}')
    @winrt_commethod(6)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def DisplayErrorString(self, errorString: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Media.PlayTo.PlayToSourceDeferral: ...
    @winrt_commethod(9)
    def SetSource(self, value: win32more.Windows.Media.PlayTo.PlayToSource) -> Void: ...
    Deadline = property(get_Deadline, None)
class IPlayToSourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceRequestedEventArgs'
    _iid_ = Guid('{c5cdc330-29df-4ec6-9da9-9fbdfcfc1b3e}')
    @winrt_commethod(6)
    def get_SourceRequest(self) -> win32more.Windows.Media.PlayTo.PlayToSourceRequest: ...
    SourceRequest = property(get_SourceRequest, None)
class IPlayToSourceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs'
    _iid_ = Guid('{0c9d8511-5202-4dcb-8c67-abda12bb3c12}')
    @winrt_commethod(6)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Icon(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(8)
    def get_SupportsImage(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SupportsAudio(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_SupportsVideo(self) -> Boolean: ...
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
    SupportsAudio = property(get_SupportsAudio, None)
    SupportsImage = property(get_SupportsImage, None)
    SupportsVideo = property(get_SupportsVideo, None)
class IPlayToSourceWithPreferredSourceUri(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceWithPreferredSourceUri'
    _iid_ = Guid('{aab253eb-3301-4dc4-afba-b2f2ed9635a0}')
    @winrt_commethod(6)
    def get_PreferredSourceUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_PreferredSourceUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
class IPlaybackRateChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlaybackRateChangeRequestedEventArgs'
    _iid_ = Guid('{0f5661ae-2c88-4cca-8540-d586095d13a5}')
    @winrt_commethod(6)
    def get_Rate(self) -> Double: ...
    Rate = property(get_Rate, None)
class ISourceChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.ISourceChangeRequestedEventArgs'
    _iid_ = Guid('{fb3f3a96-7aa6-4a8b-86e7-54f6c6d34f64}')
    @winrt_commethod(6)
    def get_Stream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Author(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Album(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Genre(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Date(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(13)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(14)
    def get_Rating(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(15)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Album = property(get_Album, None)
    Author = property(get_Author, None)
    Date = property(get_Date, None)
    Description = property(get_Description, None)
    Genre = property(get_Genre, None)
    Properties = property(get_Properties, None)
    Rating = property(get_Rating, None)
    Stream = property(get_Stream, None)
    Thumbnail = property(get_Thumbnail, None)
    Title = property(get_Title, None)
class IVolumeChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IVolumeChangeRequestedEventArgs'
    _iid_ = Guid('{6f026d5c-cf75-4c2b-913e-6d7c6c329179}')
    @winrt_commethod(6)
    def get_Volume(self) -> Double: ...
    Volume = property(get_Volume, None)
class MuteChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IMuteChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.MuteChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Mute(self: win32more.Windows.Media.PlayTo.IMuteChangeRequestedEventArgs) -> Boolean: ...
    Mute = property(get_Mute, None)
class PlayToConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToConnection
    _classid_ = 'Windows.Media.PlayTo.PlayToConnection'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.PlayTo.IPlayToConnection) -> win32more.Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Media.PlayTo.IPlayToConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToConnection, win32more.Windows.Media.PlayTo.PlayToConnectionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Media.PlayTo.IPlayToConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Transferred(self: win32more.Windows.Media.PlayTo.IPlayToConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToConnection, win32more.Windows.Media.PlayTo.PlayToConnectionTransferredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Transferred(self: win32more.Windows.Media.PlayTo.IPlayToConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Error(self: win32more.Windows.Media.PlayTo.IPlayToConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToConnection, win32more.Windows.Media.PlayTo.PlayToConnectionErrorEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Error(self: win32more.Windows.Media.PlayTo.IPlayToConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
    StateChanged = event()
    Transferred = event()
    Error = event()
class PlayToConnectionError(Enum, Int32):
    None_ = 0
    DeviceNotResponding = 1
    DeviceError = 2
    DeviceLocked = 3
    ProtectedPlaybackFailed = 4
class PlayToConnectionErrorEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToConnectionErrorEventArgs'
    @winrt_mixinmethod
    def get_Code(self: win32more.Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs) -> win32more.Windows.Media.PlayTo.PlayToConnectionError: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs) -> WinRT_String: ...
    Code = property(get_Code, None)
    Message = property(get_Message, None)
class PlayToConnectionState(Enum, Int32):
    Disconnected = 0
    Connected = 1
    Rendering = 2
class PlayToConnectionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToConnectionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_PreviousState(self: win32more.Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs) -> win32more.Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_mixinmethod
    def get_CurrentState(self: win32more.Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs) -> win32more.Windows.Media.PlayTo.PlayToConnectionState: ...
    CurrentState = property(get_CurrentState, None)
    PreviousState = property(get_PreviousState, None)
class PlayToConnectionTransferredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToConnectionTransferredEventArgs'
    @winrt_mixinmethod
    def get_PreviousSource(self: win32more.Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs) -> win32more.Windows.Media.PlayTo.PlayToSource: ...
    @winrt_mixinmethod
    def get_CurrentSource(self: win32more.Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs) -> win32more.Windows.Media.PlayTo.PlayToSource: ...
    CurrentSource = property(get_CurrentSource, None)
    PreviousSource = property(get_PreviousSource, None)
class PlayToManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToManager
    _classid_ = 'Windows.Media.PlayTo.PlayToManager'
    @winrt_mixinmethod
    def add_SourceRequested(self: win32more.Windows.Media.PlayTo.IPlayToManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToManager, win32more.Windows.Media.PlayTo.PlayToSourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRequested(self: win32more.Windows.Media.PlayTo.IPlayToManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceSelected(self: win32more.Windows.Media.PlayTo.IPlayToManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToManager, win32more.Windows.Media.PlayTo.PlayToSourceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceSelected(self: win32more.Windows.Media.PlayTo.IPlayToManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_DefaultSourceSelection(self: win32more.Windows.Media.PlayTo.IPlayToManager, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultSourceSelection(self: win32more.Windows.Media.PlayTo.IPlayToManager) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Media.PlayTo.IPlayToManagerStatics) -> win32more.Windows.Media.PlayTo.PlayToManager: ...
    @winrt_classmethod
    def ShowPlayToUI(cls: win32more.Windows.Media.PlayTo.IPlayToManagerStatics) -> Void: ...
    DefaultSourceSelection = property(get_DefaultSourceSelection, put_DefaultSourceSelection)
    SourceRequested = event()
    SourceSelected = event()
class PlayToReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToReceiver
    _classid_ = 'Windows.Media.PlayTo.PlayToReceiver'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.PlayTo.PlayToReceiver.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.PlayTo.PlayToReceiver: ...
    @winrt_mixinmethod
    def add_PlayRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlayRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PauseRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PauseRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.SourceChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PlaybackRateChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.PlaybackRateChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlaybackRateChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CurrentTimeChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.CurrentTimeChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentTimeChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MuteChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.MuteChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MuteChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VolumeChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Media.PlayTo.VolumeChangeRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VolumeChangeRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TimeUpdateRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TimeUpdateRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StopRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.PlayTo.PlayToReceiver, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StopRequested(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyVolumeChange(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, volume: Double, mute: Boolean) -> Void: ...
    @winrt_mixinmethod
    def NotifyRateChange(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, rate: Double) -> Void: ...
    @winrt_mixinmethod
    def NotifyLoadedMetadata(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyTimeUpdate(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, currentTime: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def NotifyDurationChange(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def NotifySeeking(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifySeeked(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyPaused(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyPlaying(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyEnded(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyError(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyStopped(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def put_SupportsImage(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsImage(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsAudio(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsAudio(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsVideo(self: win32more.Windows.Media.PlayTo.IPlayToReceiver, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsVideo(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.PlayTo.IPlayToReceiver) -> win32more.Windows.Foundation.IAsyncAction: ...
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    Properties = property(get_Properties, None)
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsImage = property(get_SupportsImage, put_SupportsImage)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    PlayRequested = event()
    PauseRequested = event()
    SourceChangeRequested = event()
    PlaybackRateChangeRequested = event()
    CurrentTimeChangeRequested = event()
    MuteChangeRequested = event()
    VolumeChangeRequested = event()
    TimeUpdateRequested = event()
    StopRequested = event()
class PlayToSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToSource
    _classid_ = 'Windows.Media.PlayTo.PlayToSource'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Media.PlayTo.IPlayToSource) -> win32more.Windows.Media.PlayTo.PlayToConnection: ...
    @winrt_mixinmethod
    def get_Next(self: win32more.Windows.Media.PlayTo.IPlayToSource) -> win32more.Windows.Media.PlayTo.PlayToSource: ...
    @winrt_mixinmethod
    def put_Next(self: win32more.Windows.Media.PlayTo.IPlayToSource, value: win32more.Windows.Media.PlayTo.PlayToSource) -> Void: ...
    @winrt_mixinmethod
    def PlayNext(self: win32more.Windows.Media.PlayTo.IPlayToSource) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredSourceUri(self: win32more.Windows.Media.PlayTo.IPlayToSourceWithPreferredSourceUri) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_PreferredSourceUri(self: win32more.Windows.Media.PlayTo.IPlayToSourceWithPreferredSourceUri, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Connection = property(get_Connection, None)
    Next = property(get_Next, put_Next)
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
class PlayToSourceDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToSourceDeferral
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Media.PlayTo.IPlayToSourceDeferral) -> Void: ...
class PlayToSourceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToSourceRequest
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceRequest'
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Media.PlayTo.IPlayToSourceRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def DisplayErrorString(self: win32more.Windows.Media.PlayTo.IPlayToSourceRequest, errorString: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.PlayTo.IPlayToSourceRequest) -> win32more.Windows.Media.PlayTo.PlayToSourceDeferral: ...
    @winrt_mixinmethod
    def SetSource(self: win32more.Windows.Media.PlayTo.IPlayToSourceRequest, value: win32more.Windows.Media.PlayTo.PlayToSource) -> Void: ...
    Deadline = property(get_Deadline, None)
class PlayToSourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToSourceRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceRequestedEventArgs'
    @winrt_mixinmethod
    def get_SourceRequest(self: win32more.Windows.Media.PlayTo.IPlayToSourceRequestedEventArgs) -> win32more.Windows.Media.PlayTo.PlayToSourceRequest: ...
    SourceRequest = property(get_SourceRequest, None)
class PlayToSourceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceSelectedEventArgs'
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def get_SupportsImage(self: win32more.Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportsAudio(self: win32more.Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportsVideo(self: win32more.Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> Boolean: ...
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
    SupportsAudio = property(get_SupportsAudio, None)
    SupportsImage = property(get_SupportsImage, None)
    SupportsVideo = property(get_SupportsVideo, None)
class PlaybackRateChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IPlaybackRateChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlaybackRateChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Rate(self: win32more.Windows.Media.PlayTo.IPlaybackRateChangeRequestedEventArgs) -> Double: ...
    Rate = property(get_Rate, None)
class SourceChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.SourceChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Stream(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Author(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Album(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Genre(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Date(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_Rating(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Album = property(get_Album, None)
    Author = property(get_Author, None)
    Date = property(get_Date, None)
    Description = property(get_Description, None)
    Genre = property(get_Genre, None)
    Properties = property(get_Properties, None)
    Rating = property(get_Rating, None)
    Stream = property(get_Stream, None)
    Thumbnail = property(get_Thumbnail, None)
    Title = property(get_Title, None)
class VolumeChangeRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.PlayTo.IVolumeChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.VolumeChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Volume(self: win32more.Windows.Media.PlayTo.IVolumeChangeRequestedEventArgs) -> Double: ...
    Volume = property(get_Volume, None)


make_ready(__name__)
