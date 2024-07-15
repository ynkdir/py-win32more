from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media
import win32more.Windows.Media.Control
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class CurrentSessionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.ICurrentSessionChangedEventArgs
    _classid_ = 'Windows.Media.Control.CurrentSessionChangedEventArgs'
class GlobalSystemMediaTransportControlsSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSession'
    @winrt_mixinmethod
    def get_SourceAppUserModelId(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryGetMediaPropertiesAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionMediaProperties]: ...
    @winrt_mixinmethod
    def GetTimelineProperties(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionTimelineProperties: ...
    @winrt_mixinmethod
    def GetPlaybackInfo(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackInfo: ...
    @winrt_mixinmethod
    def TryPlayAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryPauseAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryStopAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRecordAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryFastForwardAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRewindAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySkipNextAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySkipPreviousAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeChannelUpAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeChannelDownAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryTogglePlayPauseAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeAutoRepeatModeAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedAutoRepeatMode: win32more.Windows.Media.MediaPlaybackAutoRepeatMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangePlaybackRateAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedPlaybackRate: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeShuffleActiveAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedShuffleState: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangePlaybackPositionAsync(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedPlaybackPosition: Int64) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_TimelinePropertiesChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession, win32more.Windows.Media.Control.TimelinePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TimelinePropertiesChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PlaybackInfoChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession, win32more.Windows.Media.Control.PlaybackInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlaybackInfoChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MediaPropertiesChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession, win32more.Windows.Media.Control.MediaPropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MediaPropertiesChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SourceAppUserModelId = property(get_SourceAppUserModelId, None)
    TimelinePropertiesChanged = event()
    PlaybackInfoChanged = event()
    MediaPropertiesChanged = event()
class GlobalSystemMediaTransportControlsSessionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager'
    @winrt_mixinmethod
    def GetCurrentSession(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession: ...
    @winrt_mixinmethod
    def GetSessions(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession]: ...
    @winrt_mixinmethod
    def add_CurrentSessionChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, win32more.Windows.Media.Control.CurrentSessionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentSessionChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SessionsChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, win32more.Windows.Media.Control.SessionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionsChanged(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestAsync(cls: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager]: ...
    CurrentSessionChanged = event()
    SessionsChanged = event()
class GlobalSystemMediaTransportControlsSessionMediaProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionMediaProperties'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subtitle(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AlbumArtist(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Artist(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AlbumTitle(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackNumber(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Int32: ...
    @winrt_mixinmethod
    def get_Genres(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_AlbumTrackCount(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Int32: ...
    @winrt_mixinmethod
    def get_PlaybackType(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.MediaPlaybackType]: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    AlbumArtist = property(get_AlbumArtist, None)
    AlbumTitle = property(get_AlbumTitle, None)
    AlbumTrackCount = property(get_AlbumTrackCount, None)
    Artist = property(get_Artist, None)
    Genres = property(get_Genres, None)
    PlaybackType = property(get_PlaybackType, None)
    Subtitle = property(get_Subtitle, None)
    Thumbnail = property(get_Thumbnail, None)
    Title = property(get_Title, None)
    TrackNumber = property(get_TrackNumber, None)
class GlobalSystemMediaTransportControlsSessionPlaybackControls(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackControls'
    @winrt_mixinmethod
    def get_IsPlayEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPauseEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStopEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRecordEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFastForwardEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRewindEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsNextEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPreviousEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsChannelUpEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsChannelDownEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlayPauseToggleEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsShuffleEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRepeatEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlaybackRateEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlaybackPositionEnabled(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    IsChannelDownEnabled = property(get_IsChannelDownEnabled, None)
    IsChannelUpEnabled = property(get_IsChannelUpEnabled, None)
    IsFastForwardEnabled = property(get_IsFastForwardEnabled, None)
    IsNextEnabled = property(get_IsNextEnabled, None)
    IsPauseEnabled = property(get_IsPauseEnabled, None)
    IsPlayEnabled = property(get_IsPlayEnabled, None)
    IsPlayPauseToggleEnabled = property(get_IsPlayPauseToggleEnabled, None)
    IsPlaybackPositionEnabled = property(get_IsPlaybackPositionEnabled, None)
    IsPlaybackRateEnabled = property(get_IsPlaybackRateEnabled, None)
    IsPreviousEnabled = property(get_IsPreviousEnabled, None)
    IsRecordEnabled = property(get_IsRecordEnabled, None)
    IsRepeatEnabled = property(get_IsRepeatEnabled, None)
    IsRewindEnabled = property(get_IsRewindEnabled, None)
    IsShuffleEnabled = property(get_IsShuffleEnabled, None)
    IsStopEnabled = property(get_IsStopEnabled, None)
class GlobalSystemMediaTransportControlsSessionPlaybackInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackInfo'
    @winrt_mixinmethod
    def get_Controls(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackControls: ...
    @winrt_mixinmethod
    def get_PlaybackStatus(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackStatus: ...
    @winrt_mixinmethod
    def get_PlaybackType(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.MediaPlaybackType]: ...
    @winrt_mixinmethod
    def get_AutoRepeatMode(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.MediaPlaybackAutoRepeatMode]: ...
    @winrt_mixinmethod
    def get_PlaybackRate(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_IsShuffleActive(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    AutoRepeatMode = property(get_AutoRepeatMode, None)
    Controls = property(get_Controls, None)
    IsShuffleActive = property(get_IsShuffleActive, None)
    PlaybackRate = property(get_PlaybackRate, None)
    PlaybackStatus = property(get_PlaybackStatus, None)
    PlaybackType = property(get_PlaybackType, None)
class GlobalSystemMediaTransportControlsSessionPlaybackStatus(Enum, Int32):
    Closed = 0
    Opened = 1
    Changing = 2
    Stopped = 3
    Playing = 4
    Paused = 5
class GlobalSystemMediaTransportControlsSessionTimelineProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionTimelineProperties'
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MinSeekTime(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxSeekTime(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_LastUpdatedTime(self: win32more.Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> win32more.Windows.Foundation.DateTime: ...
    EndTime = property(get_EndTime, None)
    LastUpdatedTime = property(get_LastUpdatedTime, None)
    MaxSeekTime = property(get_MaxSeekTime, None)
    MinSeekTime = property(get_MinSeekTime, None)
    Position = property(get_Position, None)
    StartTime = property(get_StartTime, None)
class ICurrentSessionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.ICurrentSessionChangedEventArgs'
    _iid_ = Guid('{6969cb39-0bfa-5fe0-8d73-09cc5e5408e1}')
class IGlobalSystemMediaTransportControlsSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSession'
    _iid_ = Guid('{7148c835-9b14-5ae2-ab85-dc9b1c14e1a8}')
    @winrt_commethod(6)
    def get_SourceAppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def TryGetMediaPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionMediaProperties]: ...
    @winrt_commethod(8)
    def GetTimelineProperties(self) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionTimelineProperties: ...
    @winrt_commethod(9)
    def GetPlaybackInfo(self) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackInfo: ...
    @winrt_commethod(10)
    def TryPlayAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def TryPauseAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def TryStopAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def TryRecordAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(14)
    def TryFastForwardAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(15)
    def TryRewindAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(16)
    def TrySkipNextAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(17)
    def TrySkipPreviousAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(18)
    def TryChangeChannelUpAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(19)
    def TryChangeChannelDownAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(20)
    def TryTogglePlayPauseAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def TryChangeAutoRepeatModeAsync(self, requestedAutoRepeatMode: win32more.Windows.Media.MediaPlaybackAutoRepeatMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(22)
    def TryChangePlaybackRateAsync(self, requestedPlaybackRate: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(23)
    def TryChangeShuffleActiveAsync(self, requestedShuffleState: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(24)
    def TryChangePlaybackPositionAsync(self, requestedPlaybackPosition: Int64) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(25)
    def add_TimelinePropertiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession, win32more.Windows.Media.Control.TimelinePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_TimelinePropertiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_PlaybackInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession, win32more.Windows.Media.Control.PlaybackInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_PlaybackInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_MediaPropertiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession, win32more.Windows.Media.Control.MediaPropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_MediaPropertiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SourceAppUserModelId = property(get_SourceAppUserModelId, None)
    TimelinePropertiesChanged = event()
    PlaybackInfoChanged = event()
    MediaPropertiesChanged = event()
class IGlobalSystemMediaTransportControlsSessionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager'
    _iid_ = Guid('{cace8eac-e86e-504a-ab31-5ff8ff1bce49}')
    @winrt_commethod(6)
    def GetCurrentSession(self) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession: ...
    @winrt_commethod(7)
    def GetSessions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSession]: ...
    @winrt_commethod(8)
    def add_CurrentSessionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, win32more.Windows.Media.Control.CurrentSessionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CurrentSessionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SessionsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, win32more.Windows.Media.Control.SessionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SessionsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentSessionChanged = event()
    SessionsChanged = event()
class IGlobalSystemMediaTransportControlsSessionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManagerStatics'
    _iid_ = Guid('{2050c4ee-11a0-57de-aed7-c97c70338245}')
    @winrt_commethod(6)
    def RequestAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager]: ...
class IGlobalSystemMediaTransportControlsSessionMediaProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties'
    _iid_ = Guid('{68856cf6-adb4-54b2-ac16-05837907acb6}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Subtitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AlbumArtist(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Artist(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AlbumTitle(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_TrackNumber(self) -> Int32: ...
    @winrt_commethod(12)
    def get_Genres(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_AlbumTrackCount(self) -> Int32: ...
    @winrt_commethod(14)
    def get_PlaybackType(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.MediaPlaybackType]: ...
    @winrt_commethod(15)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    AlbumArtist = property(get_AlbumArtist, None)
    AlbumTitle = property(get_AlbumTitle, None)
    AlbumTrackCount = property(get_AlbumTrackCount, None)
    Artist = property(get_Artist, None)
    Genres = property(get_Genres, None)
    PlaybackType = property(get_PlaybackType, None)
    Subtitle = property(get_Subtitle, None)
    Thumbnail = property(get_Thumbnail, None)
    Title = property(get_Title, None)
    TrackNumber = property(get_TrackNumber, None)
class IGlobalSystemMediaTransportControlsSessionPlaybackControls(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls'
    _iid_ = Guid('{6501a3e6-bc7a-503a-bb1b-68f158f3fb03}')
    @winrt_commethod(6)
    def get_IsPlayEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsPauseEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsStopEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsRecordEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsFastForwardEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsRewindEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsNextEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsPreviousEnabled(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsChannelUpEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsChannelDownEnabled(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsPlayPauseToggleEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsShuffleEnabled(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_IsRepeatEnabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsPlaybackRateEnabled(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_IsPlaybackPositionEnabled(self) -> Boolean: ...
    IsChannelDownEnabled = property(get_IsChannelDownEnabled, None)
    IsChannelUpEnabled = property(get_IsChannelUpEnabled, None)
    IsFastForwardEnabled = property(get_IsFastForwardEnabled, None)
    IsNextEnabled = property(get_IsNextEnabled, None)
    IsPauseEnabled = property(get_IsPauseEnabled, None)
    IsPlayEnabled = property(get_IsPlayEnabled, None)
    IsPlayPauseToggleEnabled = property(get_IsPlayPauseToggleEnabled, None)
    IsPlaybackPositionEnabled = property(get_IsPlaybackPositionEnabled, None)
    IsPlaybackRateEnabled = property(get_IsPlaybackRateEnabled, None)
    IsPreviousEnabled = property(get_IsPreviousEnabled, None)
    IsRecordEnabled = property(get_IsRecordEnabled, None)
    IsRepeatEnabled = property(get_IsRepeatEnabled, None)
    IsRewindEnabled = property(get_IsRewindEnabled, None)
    IsShuffleEnabled = property(get_IsShuffleEnabled, None)
    IsStopEnabled = property(get_IsStopEnabled, None)
class IGlobalSystemMediaTransportControlsSessionPlaybackInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo'
    _iid_ = Guid('{94b4b6cf-e8ba-51ad-87a7-c10ade106127}')
    @winrt_commethod(6)
    def get_Controls(self) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackControls: ...
    @winrt_commethod(7)
    def get_PlaybackStatus(self) -> win32more.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackStatus: ...
    @winrt_commethod(8)
    def get_PlaybackType(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.MediaPlaybackType]: ...
    @winrt_commethod(9)
    def get_AutoRepeatMode(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.MediaPlaybackAutoRepeatMode]: ...
    @winrt_commethod(10)
    def get_PlaybackRate(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_IsShuffleActive(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    AutoRepeatMode = property(get_AutoRepeatMode, None)
    Controls = property(get_Controls, None)
    IsShuffleActive = property(get_IsShuffleActive, None)
    PlaybackRate = property(get_PlaybackRate, None)
    PlaybackStatus = property(get_PlaybackStatus, None)
    PlaybackType = property(get_PlaybackType, None)
class IGlobalSystemMediaTransportControlsSessionTimelineProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties'
    _iid_ = Guid('{ede34136-6f25-588d-8ecf-ea5b6735aaa5}')
    @winrt_commethod(6)
    def get_StartTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_EndTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_MinSeekTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MaxSeekTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Position(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def get_LastUpdatedTime(self) -> win32more.Windows.Foundation.DateTime: ...
    EndTime = property(get_EndTime, None)
    LastUpdatedTime = property(get_LastUpdatedTime, None)
    MaxSeekTime = property(get_MaxSeekTime, None)
    MinSeekTime = property(get_MinSeekTime, None)
    Position = property(get_Position, None)
    StartTime = property(get_StartTime, None)
class IMediaPropertiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IMediaPropertiesChangedEventArgs'
    _iid_ = Guid('{7d3741cb-adf0-5cef-91ba-cfabcdd77678}')
class IPlaybackInfoChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IPlaybackInfoChangedEventArgs'
    _iid_ = Guid('{786756c2-bc0d-50a5-8807-054291fef139}')
class ISessionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.ISessionsChangedEventArgs'
    _iid_ = Guid('{bbf0cd32-42c4-5a58-b317-f34bbfbd26e0}')
class ITimelinePropertiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.ITimelinePropertiesChangedEventArgs'
    _iid_ = Guid('{29033a2f-c923-5a77-bcaf-055ff415ad32}')
class MediaPropertiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IMediaPropertiesChangedEventArgs
    _classid_ = 'Windows.Media.Control.MediaPropertiesChangedEventArgs'
class PlaybackInfoChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.IPlaybackInfoChangedEventArgs
    _classid_ = 'Windows.Media.Control.PlaybackInfoChangedEventArgs'
class SessionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.ISessionsChangedEventArgs
    _classid_ = 'Windows.Media.Control.SessionsChangedEventArgs'
class TimelinePropertiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Control.ITimelinePropertiesChangedEventArgs
    _classid_ = 'Windows.Media.Control.TimelinePropertiesChangedEventArgs'


make_ready(__name__)
