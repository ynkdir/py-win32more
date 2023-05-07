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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media
import Windows.Media.Control
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
class CurrentSessionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.ICurrentSessionChangedEventArgs
    _classid_ = 'Windows.Media.Control.CurrentSessionChangedEventArgs'
class GlobalSystemMediaTransportControlsSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSession'
    @winrt_mixinmethod
    def get_SourceAppUserModelId(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryGetMediaPropertiesAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionMediaProperties]: ...
    @winrt_mixinmethod
    def GetTimelineProperties(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionTimelineProperties: ...
    @winrt_mixinmethod
    def GetPlaybackInfo(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackInfo: ...
    @winrt_mixinmethod
    def TryPlayAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryPauseAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryStopAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRecordAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryFastForwardAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRewindAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySkipNextAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySkipPreviousAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeChannelUpAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeChannelDownAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryTogglePlayPauseAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeAutoRepeatModeAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedAutoRepeatMode: Windows.Media.MediaPlaybackAutoRepeatMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangePlaybackRateAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedPlaybackRate: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangeShuffleActiveAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedShuffleState: Boolean) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryChangePlaybackPositionAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedPlaybackPosition: Int64) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_TimelinePropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSession, Windows.Media.Control.TimelinePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TimelinePropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PlaybackInfoChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSession, Windows.Media.Control.PlaybackInfoChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlaybackInfoChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MediaPropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSession, Windows.Media.Control.MediaPropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MediaPropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SourceAppUserModelId = property(get_SourceAppUserModelId, None)
class GlobalSystemMediaTransportControlsSessionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager'
    @winrt_mixinmethod
    def GetCurrentSession(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSession: ...
    @winrt_mixinmethod
    def GetSessions(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Control.GlobalSystemMediaTransportControlsSession]: ...
    @winrt_mixinmethod
    def add_CurrentSessionChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, Windows.Media.Control.CurrentSessionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentSessionChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SessionsChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, Windows.Media.Control.SessionsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionsChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestAsync(cls: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager]: ...
class GlobalSystemMediaTransportControlsSessionMediaProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionMediaProperties'
    @winrt_mixinmethod
    def get_Title(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subtitle(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AlbumArtist(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Artist(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AlbumTitle(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackNumber(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Int32: ...
    @winrt_mixinmethod
    def get_Genres(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_AlbumTrackCount(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Int32: ...
    @winrt_mixinmethod
    def get_PlaybackType(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Windows.Foundation.IReference[Windows.Media.MediaPlaybackType]: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    Title = property(get_Title, None)
    Subtitle = property(get_Subtitle, None)
    AlbumArtist = property(get_AlbumArtist, None)
    Artist = property(get_Artist, None)
    AlbumTitle = property(get_AlbumTitle, None)
    TrackNumber = property(get_TrackNumber, None)
    Genres = property(get_Genres, None)
    AlbumTrackCount = property(get_AlbumTrackCount, None)
    PlaybackType = property(get_PlaybackType, None)
    Thumbnail = property(get_Thumbnail, None)
class GlobalSystemMediaTransportControlsSessionPlaybackControls(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackControls'
    @winrt_mixinmethod
    def get_IsPlayEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPauseEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStopEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRecordEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFastForwardEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRewindEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsNextEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPreviousEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsChannelUpEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsChannelDownEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlayPauseToggleEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsShuffleEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRepeatEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlaybackRateEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlaybackPositionEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    IsPlayEnabled = property(get_IsPlayEnabled, None)
    IsPauseEnabled = property(get_IsPauseEnabled, None)
    IsStopEnabled = property(get_IsStopEnabled, None)
    IsRecordEnabled = property(get_IsRecordEnabled, None)
    IsFastForwardEnabled = property(get_IsFastForwardEnabled, None)
    IsRewindEnabled = property(get_IsRewindEnabled, None)
    IsNextEnabled = property(get_IsNextEnabled, None)
    IsPreviousEnabled = property(get_IsPreviousEnabled, None)
    IsChannelUpEnabled = property(get_IsChannelUpEnabled, None)
    IsChannelDownEnabled = property(get_IsChannelDownEnabled, None)
    IsPlayPauseToggleEnabled = property(get_IsPlayPauseToggleEnabled, None)
    IsShuffleEnabled = property(get_IsShuffleEnabled, None)
    IsRepeatEnabled = property(get_IsRepeatEnabled, None)
    IsPlaybackRateEnabled = property(get_IsPlaybackRateEnabled, None)
    IsPlaybackPositionEnabled = property(get_IsPlaybackPositionEnabled, None)
class GlobalSystemMediaTransportControlsSessionPlaybackInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackInfo'
    @winrt_mixinmethod
    def get_Controls(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackControls: ...
    @winrt_mixinmethod
    def get_PlaybackStatus(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackStatus: ...
    @winrt_mixinmethod
    def get_PlaybackType(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Windows.Media.MediaPlaybackType]: ...
    @winrt_mixinmethod
    def get_AutoRepeatMode(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Windows.Media.MediaPlaybackAutoRepeatMode]: ...
    @winrt_mixinmethod
    def get_PlaybackRate(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_IsShuffleActive(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Boolean]: ...
    Controls = property(get_Controls, None)
    PlaybackStatus = property(get_PlaybackStatus, None)
    PlaybackType = property(get_PlaybackType, None)
    AutoRepeatMode = property(get_AutoRepeatMode, None)
    PlaybackRate = property(get_PlaybackRate, None)
    IsShuffleActive = property(get_IsShuffleActive, None)
GlobalSystemMediaTransportControlsSessionPlaybackStatus = Int32
GlobalSystemMediaTransportControlsSessionPlaybackStatus_Closed: GlobalSystemMediaTransportControlsSessionPlaybackStatus = 0
GlobalSystemMediaTransportControlsSessionPlaybackStatus_Opened: GlobalSystemMediaTransportControlsSessionPlaybackStatus = 1
GlobalSystemMediaTransportControlsSessionPlaybackStatus_Changing: GlobalSystemMediaTransportControlsSessionPlaybackStatus = 2
GlobalSystemMediaTransportControlsSessionPlaybackStatus_Stopped: GlobalSystemMediaTransportControlsSessionPlaybackStatus = 3
GlobalSystemMediaTransportControlsSessionPlaybackStatus_Playing: GlobalSystemMediaTransportControlsSessionPlaybackStatus = 4
GlobalSystemMediaTransportControlsSessionPlaybackStatus_Paused: GlobalSystemMediaTransportControlsSessionPlaybackStatus = 5
class GlobalSystemMediaTransportControlsSessionTimelineProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties
    _classid_ = 'Windows.Media.Control.GlobalSystemMediaTransportControlsSessionTimelineProperties'
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_EndTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MinSeekTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxSeekTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_LastUpdatedTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.DateTime: ...
    StartTime = property(get_StartTime, None)
    EndTime = property(get_EndTime, None)
    MinSeekTime = property(get_MinSeekTime, None)
    MaxSeekTime = property(get_MaxSeekTime, None)
    Position = property(get_Position, None)
    LastUpdatedTime = property(get_LastUpdatedTime, None)
class ICurrentSessionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.ICurrentSessionChangedEventArgs'
    _iid_ = Guid('{6969cb39-0bfa-5fe0-8d73-09cc5e5408e1}')
class IGlobalSystemMediaTransportControlsSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSession'
    _iid_ = Guid('{7148c835-9b14-5ae2-ab85-dc9b1c14e1a8}')
    @winrt_commethod(6)
    def get_SourceAppUserModelId(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> WinRT_String: ...
    @winrt_commethod(7)
    def TryGetMediaPropertiesAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionMediaProperties]: ...
    @winrt_commethod(8)
    def GetTimelineProperties(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionTimelineProperties: ...
    @winrt_commethod(9)
    def GetPlaybackInfo(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackInfo: ...
    @winrt_commethod(10)
    def TryPlayAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def TryPauseAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def TryStopAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def TryRecordAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(14)
    def TryFastForwardAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(15)
    def TryRewindAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(16)
    def TrySkipNextAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(17)
    def TrySkipPreviousAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(18)
    def TryChangeChannelUpAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(19)
    def TryChangeChannelDownAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(20)
    def TryTogglePlayPauseAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def TryChangeAutoRepeatModeAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedAutoRepeatMode: Windows.Media.MediaPlaybackAutoRepeatMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(22)
    def TryChangePlaybackRateAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedPlaybackRate: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(23)
    def TryChangeShuffleActiveAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedShuffleState: Boolean) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(24)
    def TryChangePlaybackPositionAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, requestedPlaybackPosition: Int64) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(25)
    def add_TimelinePropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSession, Windows.Media.Control.TimelinePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_TimelinePropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_PlaybackInfoChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSession, Windows.Media.Control.PlaybackInfoChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_PlaybackInfoChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_MediaPropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSession, Windows.Media.Control.MediaPropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_MediaPropertiesChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SourceAppUserModelId = property(get_SourceAppUserModelId, None)
class IGlobalSystemMediaTransportControlsSessionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager'
    _iid_ = Guid('{cace8eac-e86e-504a-ab31-5ff8ff1bce49}')
    @winrt_commethod(6)
    def GetCurrentSession(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSession: ...
    @winrt_commethod(7)
    def GetSessions(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Control.GlobalSystemMediaTransportControlsSession]: ...
    @winrt_commethod(8)
    def add_CurrentSessionChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, Windows.Media.Control.CurrentSessionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CurrentSessionChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SessionsChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager, Windows.Media.Control.SessionsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SessionsChanged(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IGlobalSystemMediaTransportControlsSessionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManagerStatics'
    _iid_ = Guid('{2050c4ee-11a0-57de-aed7-c97c70338245}')
    @winrt_commethod(6)
    def RequestAsync(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Media.Control.GlobalSystemMediaTransportControlsSessionManager]: ...
class IGlobalSystemMediaTransportControlsSessionMediaProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties'
    _iid_ = Guid('{68856cf6-adb4-54b2-ac16-05837907acb6}')
    @winrt_commethod(6)
    def get_Title(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Subtitle(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AlbumArtist(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Artist(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AlbumTitle(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_TrackNumber(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Int32: ...
    @winrt_commethod(12)
    def get_Genres(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_AlbumTrackCount(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Int32: ...
    @winrt_commethod(14)
    def get_PlaybackType(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Windows.Foundation.IReference[Windows.Media.MediaPlaybackType]: ...
    @winrt_commethod(15)
    def get_Thumbnail(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionMediaProperties) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    Title = property(get_Title, None)
    Subtitle = property(get_Subtitle, None)
    AlbumArtist = property(get_AlbumArtist, None)
    Artist = property(get_Artist, None)
    AlbumTitle = property(get_AlbumTitle, None)
    TrackNumber = property(get_TrackNumber, None)
    Genres = property(get_Genres, None)
    AlbumTrackCount = property(get_AlbumTrackCount, None)
    PlaybackType = property(get_PlaybackType, None)
    Thumbnail = property(get_Thumbnail, None)
class IGlobalSystemMediaTransportControlsSessionPlaybackControls(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls'
    _iid_ = Guid('{6501a3e6-bc7a-503a-bb1b-68f158f3fb03}')
    @winrt_commethod(6)
    def get_IsPlayEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsPauseEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsStopEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsRecordEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsFastForwardEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsRewindEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsNextEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsPreviousEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsChannelUpEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsChannelDownEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsPlayPauseToggleEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsShuffleEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(18)
    def get_IsRepeatEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsPlaybackRateEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    @winrt_commethod(20)
    def get_IsPlaybackPositionEnabled(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackControls) -> Boolean: ...
    IsPlayEnabled = property(get_IsPlayEnabled, None)
    IsPauseEnabled = property(get_IsPauseEnabled, None)
    IsStopEnabled = property(get_IsStopEnabled, None)
    IsRecordEnabled = property(get_IsRecordEnabled, None)
    IsFastForwardEnabled = property(get_IsFastForwardEnabled, None)
    IsRewindEnabled = property(get_IsRewindEnabled, None)
    IsNextEnabled = property(get_IsNextEnabled, None)
    IsPreviousEnabled = property(get_IsPreviousEnabled, None)
    IsChannelUpEnabled = property(get_IsChannelUpEnabled, None)
    IsChannelDownEnabled = property(get_IsChannelDownEnabled, None)
    IsPlayPauseToggleEnabled = property(get_IsPlayPauseToggleEnabled, None)
    IsShuffleEnabled = property(get_IsShuffleEnabled, None)
    IsRepeatEnabled = property(get_IsRepeatEnabled, None)
    IsPlaybackRateEnabled = property(get_IsPlaybackRateEnabled, None)
    IsPlaybackPositionEnabled = property(get_IsPlaybackPositionEnabled, None)
class IGlobalSystemMediaTransportControlsSessionPlaybackInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo'
    _iid_ = Guid('{94b4b6cf-e8ba-51ad-87a7-c10ade106127}')
    @winrt_commethod(6)
    def get_Controls(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackControls: ...
    @winrt_commethod(7)
    def get_PlaybackStatus(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackStatus: ...
    @winrt_commethod(8)
    def get_PlaybackType(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Windows.Media.MediaPlaybackType]: ...
    @winrt_commethod(9)
    def get_AutoRepeatMode(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Windows.Media.MediaPlaybackAutoRepeatMode]: ...
    @winrt_commethod(10)
    def get_PlaybackRate(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_IsShuffleActive(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionPlaybackInfo) -> Windows.Foundation.IReference[Boolean]: ...
    Controls = property(get_Controls, None)
    PlaybackStatus = property(get_PlaybackStatus, None)
    PlaybackType = property(get_PlaybackType, None)
    AutoRepeatMode = property(get_AutoRepeatMode, None)
    PlaybackRate = property(get_PlaybackRate, None)
    IsShuffleActive = property(get_IsShuffleActive, None)
class IGlobalSystemMediaTransportControlsSessionTimelineProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties'
    _iid_ = Guid('{ede34136-6f25-588d-8ecf-ea5b6735aaa5}')
    @winrt_commethod(6)
    def get_StartTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_EndTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_MinSeekTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MaxSeekTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Position(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def get_LastUpdatedTime(self: Windows.Media.Control.IGlobalSystemMediaTransportControlsSessionTimelineProperties) -> Windows.Foundation.DateTime: ...
    StartTime = property(get_StartTime, None)
    EndTime = property(get_EndTime, None)
    MinSeekTime = property(get_MinSeekTime, None)
    MaxSeekTime = property(get_MaxSeekTime, None)
    Position = property(get_Position, None)
    LastUpdatedTime = property(get_LastUpdatedTime, None)
class IMediaPropertiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IMediaPropertiesChangedEventArgs'
    _iid_ = Guid('{7d3741cb-adf0-5cef-91ba-cfabcdd77678}')
class IPlaybackInfoChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.IPlaybackInfoChangedEventArgs'
    _iid_ = Guid('{786756c2-bc0d-50a5-8807-054291fef139}')
class ISessionsChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.ISessionsChangedEventArgs'
    _iid_ = Guid('{bbf0cd32-42c4-5a58-b317-f34bbfbd26e0}')
class ITimelinePropertiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Control.ITimelinePropertiesChangedEventArgs'
    _iid_ = Guid('{29033a2f-c923-5a77-bcaf-055ff415ad32}')
class MediaPropertiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IMediaPropertiesChangedEventArgs
    _classid_ = 'Windows.Media.Control.MediaPropertiesChangedEventArgs'
class PlaybackInfoChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.IPlaybackInfoChangedEventArgs
    _classid_ = 'Windows.Media.Control.PlaybackInfoChangedEventArgs'
class SessionsChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.ISessionsChangedEventArgs
    _classid_ = 'Windows.Media.Control.SessionsChangedEventArgs'
class TimelinePropertiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Control.ITimelinePropertiesChangedEventArgs
    _classid_ = 'Windows.Media.Control.TimelinePropertiesChangedEventArgs'
make_head(_module, 'CurrentSessionChangedEventArgs')
make_head(_module, 'GlobalSystemMediaTransportControlsSession')
make_head(_module, 'GlobalSystemMediaTransportControlsSessionManager')
make_head(_module, 'GlobalSystemMediaTransportControlsSessionMediaProperties')
make_head(_module, 'GlobalSystemMediaTransportControlsSessionPlaybackControls')
make_head(_module, 'GlobalSystemMediaTransportControlsSessionPlaybackInfo')
make_head(_module, 'GlobalSystemMediaTransportControlsSessionTimelineProperties')
make_head(_module, 'ICurrentSessionChangedEventArgs')
make_head(_module, 'IGlobalSystemMediaTransportControlsSession')
make_head(_module, 'IGlobalSystemMediaTransportControlsSessionManager')
make_head(_module, 'IGlobalSystemMediaTransportControlsSessionManagerStatics')
make_head(_module, 'IGlobalSystemMediaTransportControlsSessionMediaProperties')
make_head(_module, 'IGlobalSystemMediaTransportControlsSessionPlaybackControls')
make_head(_module, 'IGlobalSystemMediaTransportControlsSessionPlaybackInfo')
make_head(_module, 'IGlobalSystemMediaTransportControlsSessionTimelineProperties')
make_head(_module, 'IMediaPropertiesChangedEventArgs')
make_head(_module, 'IPlaybackInfoChangedEventArgs')
make_head(_module, 'ISessionsChangedEventArgs')
make_head(_module, 'ITimelinePropertiesChangedEventArgs')
make_head(_module, 'MediaPropertiesChangedEventArgs')
make_head(_module, 'PlaybackInfoChangedEventArgs')
make_head(_module, 'SessionsChangedEventArgs')
make_head(_module, 'TimelinePropertiesChangedEventArgs')
