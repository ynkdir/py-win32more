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
import Windows.Media.Core
import Windows.Media.Streaming.Adaptive
import Windows.Storage.Streams
import Windows.Web.Http
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AdaptiveMediaSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSource'
    @winrt_mixinmethod
    def get_IsLive(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_DesiredLiveOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DesiredLiveOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_InitialBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> UInt32: ...
    @winrt_mixinmethod
    def put_InitialBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentDownloadBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentPlaybackBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> UInt32: ...
    @winrt_mixinmethod
    def get_AvailableBitrates(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def get_DesiredMinBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_DesiredMinBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredMaxBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_DesiredMaxBitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_AudioOnlyPlayback(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_InboundBitsPerSecond(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> UInt64: ...
    @winrt_mixinmethod
    def get_InboundBitsPerSecondWindow(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_InboundBitsPerSecondWindow(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadBitrateChanged(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadBitrateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadBitrateChanged(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PlaybackBitrateChanged(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourcePlaybackBitrateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlaybackBitrateChanged(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadRequested(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadRequested(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadCompleted(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadCompleted(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadFailed(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadFailed(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AdvancedSettings(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource2) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceAdvancedSettings: ...
    @winrt_mixinmethod
    def get_MinLiveOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_MaxSeekableWindowSize(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_DesiredSeekableWindowSize(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_DesiredSeekableWindowSize(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource3, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Diagnostics(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource3) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnostics: ...
    @winrt_mixinmethod
    def GetCorrelatedTimes(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSource3) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCorrelatedTimes: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def IsContentTypeSupported(cls: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceStatics, contentType: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def CreateFromUriAsync(cls: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceStatics, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
    @winrt_classmethod
    def CreateFromUriWithDownloaderAsync(cls: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceStatics, uri: Windows.Foundation.Uri, httpClient: Windows.Web.Http.HttpClient) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
    @winrt_classmethod
    def CreateFromStreamAsync(cls: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceStatics, stream: Windows.Storage.Streams.IInputStream, uri: Windows.Foundation.Uri, contentType: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
    @winrt_classmethod
    def CreateFromStreamWithDownloaderAsync(cls: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceStatics, stream: Windows.Storage.Streams.IInputStream, uri: Windows.Foundation.Uri, contentType: WinRT_String, httpClient: Windows.Web.Http.HttpClient) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
    IsLive = property(get_IsLive, None)
    DesiredLiveOffset = property(get_DesiredLiveOffset, put_DesiredLiveOffset)
    InitialBitrate = property(get_InitialBitrate, put_InitialBitrate)
    CurrentDownloadBitrate = property(get_CurrentDownloadBitrate, None)
    CurrentPlaybackBitrate = property(get_CurrentPlaybackBitrate, None)
    AvailableBitrates = property(get_AvailableBitrates, None)
    DesiredMinBitrate = property(get_DesiredMinBitrate, put_DesiredMinBitrate)
    DesiredMaxBitrate = property(get_DesiredMaxBitrate, put_DesiredMaxBitrate)
    AudioOnlyPlayback = property(get_AudioOnlyPlayback, None)
    InboundBitsPerSecond = property(get_InboundBitsPerSecond, None)
    InboundBitsPerSecondWindow = property(get_InboundBitsPerSecondWindow, put_InboundBitsPerSecondWindow)
    AdvancedSettings = property(get_AdvancedSettings, None)
    MinLiveOffset = property(get_MinLiveOffset, None)
    MaxSeekableWindowSize = property(get_MaxSeekableWindowSize, None)
    DesiredSeekableWindowSize = property(get_DesiredSeekableWindowSize, put_DesiredSeekableWindowSize)
    Diagnostics = property(get_Diagnostics, None)
class AdaptiveMediaSourceAdvancedSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceAdvancedSettings
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceAdvancedSettings'
    @winrt_mixinmethod
    def get_AllSegmentsIndependent(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceAdvancedSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllSegmentsIndependent(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceAdvancedSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredBitrateHeadroomRatio(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceAdvancedSettings) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_DesiredBitrateHeadroomRatio(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceAdvancedSettings, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_BitrateDowngradeTriggerRatio(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceAdvancedSettings) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_BitrateDowngradeTriggerRatio(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceAdvancedSettings, value: Windows.Foundation.IReference[Double]) -> Void: ...
    AllSegmentsIndependent = property(get_AllSegmentsIndependent, put_AllSegmentsIndependent)
    DesiredBitrateHeadroomRatio = property(get_DesiredBitrateHeadroomRatio, put_DesiredBitrateHeadroomRatio)
    BitrateDowngradeTriggerRatio = property(get_BitrateDowngradeTriggerRatio, put_BitrateDowngradeTriggerRatio)
class AdaptiveMediaSourceCorrelatedTimes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCorrelatedTimes
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCorrelatedTimes'
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCorrelatedTimes) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_PresentationTimeStamp(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCorrelatedTimes) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ProgramDateTime(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCorrelatedTimes) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    Position = property(get_Position, None)
    PresentationTimeStamp = property(get_PresentationTimeStamp, None)
    ProgramDateTime = property(get_ProgramDateTime, None)
class AdaptiveMediaSourceCreationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCreationResult
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCreationResult) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationStatus: ...
    @winrt_mixinmethod
    def get_MediaSource(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCreationResult) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSource: ...
    @winrt_mixinmethod
    def get_HttpResponseMessage(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCreationResult) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceCreationResult2) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    MediaSource = property(get_MediaSource, None)
    HttpResponseMessage = property(get_HttpResponseMessage, None)
    ExtendedError = property(get_ExtendedError, None)
AdaptiveMediaSourceCreationStatus = Int32
AdaptiveMediaSourceCreationStatus_Success: AdaptiveMediaSourceCreationStatus = 0
AdaptiveMediaSourceCreationStatus_ManifestDownloadFailure: AdaptiveMediaSourceCreationStatus = 1
AdaptiveMediaSourceCreationStatus_ManifestParseFailure: AdaptiveMediaSourceCreationStatus = 2
AdaptiveMediaSourceCreationStatus_UnsupportedManifestContentType: AdaptiveMediaSourceCreationStatus = 3
AdaptiveMediaSourceCreationStatus_UnsupportedManifestVersion: AdaptiveMediaSourceCreationStatus = 4
AdaptiveMediaSourceCreationStatus_UnsupportedManifestProfile: AdaptiveMediaSourceCreationStatus = 5
AdaptiveMediaSourceCreationStatus_UnknownFailure: AdaptiveMediaSourceCreationStatus = 6
class AdaptiveMediaSourceDiagnosticAvailableEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnosticAvailableEventArgs'
    @winrt_mixinmethod
    def get_DiagnosticType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnosticType: ...
    @winrt_mixinmethod
    def get_RequestId(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_SegmentId(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_ResourceType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.IReference[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType]: ...
    @winrt_mixinmethod
    def get_ResourceUri(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeLength(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_Bitrate(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs2) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ResourceDuration(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ResourceContentType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnosticAvailableEventArgs3) -> WinRT_String: ...
    DiagnosticType = property(get_DiagnosticType, None)
    RequestId = property(get_RequestId, None)
    Position = property(get_Position, None)
    SegmentId = property(get_SegmentId, None)
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    Bitrate = property(get_Bitrate, None)
    ExtendedError = property(get_ExtendedError, None)
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
AdaptiveMediaSourceDiagnosticType = Int32
AdaptiveMediaSourceDiagnosticType_ManifestUnchangedUponReload: AdaptiveMediaSourceDiagnosticType = 0
AdaptiveMediaSourceDiagnosticType_ManifestMismatchUponReload: AdaptiveMediaSourceDiagnosticType = 1
AdaptiveMediaSourceDiagnosticType_ManifestSignaledEndOfLiveEventUponReload: AdaptiveMediaSourceDiagnosticType = 2
AdaptiveMediaSourceDiagnosticType_MediaSegmentSkipped: AdaptiveMediaSourceDiagnosticType = 3
AdaptiveMediaSourceDiagnosticType_ResourceNotFound: AdaptiveMediaSourceDiagnosticType = 4
AdaptiveMediaSourceDiagnosticType_ResourceTimedOut: AdaptiveMediaSourceDiagnosticType = 5
AdaptiveMediaSourceDiagnosticType_ResourceParsingError: AdaptiveMediaSourceDiagnosticType = 6
AdaptiveMediaSourceDiagnosticType_BitrateDisabled: AdaptiveMediaSourceDiagnosticType = 7
AdaptiveMediaSourceDiagnosticType_FatalMediaSourceError: AdaptiveMediaSourceDiagnosticType = 8
class AdaptiveMediaSourceDiagnostics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnostics
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnostics'
    @winrt_mixinmethod
    def add_DiagnosticAvailable(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnostics, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnostics, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnosticAvailableEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DiagnosticAvailable(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDiagnostics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class AdaptiveMediaSourceDownloadBitrateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadBitrateChangedEventArgs
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadBitrateChangedEventArgs'
    @winrt_mixinmethod
    def get_OldValue(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadBitrateChangedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_NewValue(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadBitrateChangedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadBitrateChangedEventArgs2) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadBitrateChangedReason: ...
    OldValue = property(get_OldValue, None)
    NewValue = property(get_NewValue, None)
    Reason = property(get_Reason, None)
AdaptiveMediaSourceDownloadBitrateChangedReason = Int32
AdaptiveMediaSourceDownloadBitrateChangedReason_SufficientInboundBitsPerSecond: AdaptiveMediaSourceDownloadBitrateChangedReason = 0
AdaptiveMediaSourceDownloadBitrateChangedReason_InsufficientInboundBitsPerSecond: AdaptiveMediaSourceDownloadBitrateChangedReason = 1
AdaptiveMediaSourceDownloadBitrateChangedReason_LowBufferLevel: AdaptiveMediaSourceDownloadBitrateChangedReason = 2
AdaptiveMediaSourceDownloadBitrateChangedReason_PositionChanged: AdaptiveMediaSourceDownloadBitrateChangedReason = 3
AdaptiveMediaSourceDownloadBitrateChangedReason_TrackSelectionChanged: AdaptiveMediaSourceDownloadBitrateChangedReason = 4
AdaptiveMediaSourceDownloadBitrateChangedReason_DesiredBitratesChanged: AdaptiveMediaSourceDownloadBitrateChangedReason = 5
AdaptiveMediaSourceDownloadBitrateChangedReason_ErrorInPreviousBitrate: AdaptiveMediaSourceDownloadBitrateChangedReason = 6
class AdaptiveMediaSourceDownloadCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadCompletedEventArgs'
    @winrt_mixinmethod
    def get_ResourceType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType: ...
    @winrt_mixinmethod
    def get_ResourceUri(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeLength(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_HttpResponseMessage(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_RequestId(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs2) -> Int32: ...
    @winrt_mixinmethod
    def get_Statistics(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs2) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadStatistics: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ResourceDuration(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ResourceContentType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadCompletedEventArgs3) -> WinRT_String: ...
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    HttpResponseMessage = property(get_HttpResponseMessage, None)
    RequestId = property(get_RequestId, None)
    Statistics = property(get_Statistics, None)
    Position = property(get_Position, None)
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
class AdaptiveMediaSourceDownloadFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadFailedEventArgs'
    @winrt_mixinmethod
    def get_ResourceType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType: ...
    @winrt_mixinmethod
    def get_ResourceUri(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeLength(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_HttpResponseMessage(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_RequestId(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs2) -> Int32: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs2) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Statistics(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs2) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadStatistics: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ResourceDuration(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ResourceContentType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadFailedEventArgs3) -> WinRT_String: ...
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    HttpResponseMessage = property(get_HttpResponseMessage, None)
    RequestId = property(get_RequestId, None)
    ExtendedError = property(get_ExtendedError, None)
    Statistics = property(get_Statistics, None)
    Position = property(get_Position, None)
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
class AdaptiveMediaSourceDownloadRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedDeferral
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadRequestedDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedDeferral) -> Void: ...
class AdaptiveMediaSourceDownloadRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadRequestedEventArgs'
    @winrt_mixinmethod
    def get_ResourceType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType: ...
    @winrt_mixinmethod
    def get_ResourceUri(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeLength(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_Result(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadResult: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadRequestedDeferral: ...
    @winrt_mixinmethod
    def get_RequestId(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs2) -> Int32: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ResourceDuration(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ResourceContentType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadRequestedEventArgs3) -> WinRT_String: ...
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    Result = property(get_Result, None)
    RequestId = property(get_RequestId, None)
    Position = property(get_Position, None)
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
class AdaptiveMediaSourceDownloadResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadResult'
    @winrt_mixinmethod
    def get_ResourceUri(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ResourceUri(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def put_InputStream(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult, value: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def get_Buffer(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Buffer(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentType(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExtendedStatus(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult) -> UInt32: ...
    @winrt_mixinmethod
    def put_ExtendedStatus(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult2) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def put_ResourceByteRangeOffset(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult2, value: Windows.Foundation.IReference[UInt64]) -> Void: ...
    @winrt_mixinmethod
    def get_ResourceByteRangeLength(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult2) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def put_ResourceByteRangeLength(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadResult2, value: Windows.Foundation.IReference[UInt64]) -> Void: ...
    ResourceUri = property(get_ResourceUri, put_ResourceUri)
    InputStream = property(get_InputStream, put_InputStream)
    Buffer = property(get_Buffer, put_Buffer)
    ContentType = property(get_ContentType, put_ContentType)
    ExtendedStatus = property(get_ExtendedStatus, put_ExtendedStatus)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, put_ResourceByteRangeOffset)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, put_ResourceByteRangeLength)
class AdaptiveMediaSourceDownloadStatistics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadStatistics
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadStatistics'
    @winrt_mixinmethod
    def get_ContentBytesReceivedCount(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadStatistics) -> UInt64: ...
    @winrt_mixinmethod
    def get_TimeToHeadersReceived(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadStatistics) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_TimeToFirstByteReceived(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadStatistics) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_TimeToLastByteReceived(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourceDownloadStatistics) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    ContentBytesReceivedCount = property(get_ContentBytesReceivedCount, None)
    TimeToHeadersReceived = property(get_TimeToHeadersReceived, None)
    TimeToFirstByteReceived = property(get_TimeToFirstByteReceived, None)
    TimeToLastByteReceived = property(get_TimeToLastByteReceived, None)
class AdaptiveMediaSourcePlaybackBitrateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs
    _classid_ = 'Windows.Media.Streaming.Adaptive.AdaptiveMediaSourcePlaybackBitrateChangedEventArgs'
    @winrt_mixinmethod
    def get_OldValue(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_NewValue(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_AudioOnly(self: Windows.Media.Streaming.Adaptive.IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs) -> Boolean: ...
    OldValue = property(get_OldValue, None)
    NewValue = property(get_NewValue, None)
    AudioOnly = property(get_AudioOnly, None)
AdaptiveMediaSourceResourceType = Int32
AdaptiveMediaSourceResourceType_Manifest: AdaptiveMediaSourceResourceType = 0
AdaptiveMediaSourceResourceType_InitializationSegment: AdaptiveMediaSourceResourceType = 1
AdaptiveMediaSourceResourceType_MediaSegment: AdaptiveMediaSourceResourceType = 2
AdaptiveMediaSourceResourceType_Key: AdaptiveMediaSourceResourceType = 3
AdaptiveMediaSourceResourceType_InitializationVector: AdaptiveMediaSourceResourceType = 4
AdaptiveMediaSourceResourceType_MediaSegmentIndex: AdaptiveMediaSourceResourceType = 5
class IAdaptiveMediaSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4c7332ef-d39f-4396-b4d9-043957a7c964}')
    @winrt_commethod(6)
    def get_IsLive(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_DesiredLiveOffset(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def put_DesiredLiveOffset(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def get_InitialBitrate(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_InitialBitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_CurrentDownloadBitrate(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_CurrentPlaybackBitrate(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_AvailableBitrates(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(14)
    def get_DesiredMinBitrate(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(15)
    def put_DesiredMinBitrate(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(16)
    def get_DesiredMaxBitrate(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(17)
    def put_DesiredMaxBitrate(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(18)
    def get_AudioOnlyPlayback(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_InboundBitsPerSecond(self) -> UInt64: ...
    @winrt_commethod(20)
    def get_InboundBitsPerSecondWindow(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(21)
    def put_InboundBitsPerSecondWindow(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(22)
    def add_DownloadBitrateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadBitrateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_DownloadBitrateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_PlaybackBitrateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourcePlaybackBitrateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_PlaybackBitrateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_DownloadRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_DownloadRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_DownloadCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_DownloadCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_DownloadFailed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSource, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_DownloadFailed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsLive = property(get_IsLive, None)
    DesiredLiveOffset = property(get_DesiredLiveOffset, put_DesiredLiveOffset)
    InitialBitrate = property(get_InitialBitrate, put_InitialBitrate)
    CurrentDownloadBitrate = property(get_CurrentDownloadBitrate, None)
    CurrentPlaybackBitrate = property(get_CurrentPlaybackBitrate, None)
    AvailableBitrates = property(get_AvailableBitrates, None)
    DesiredMinBitrate = property(get_DesiredMinBitrate, put_DesiredMinBitrate)
    DesiredMaxBitrate = property(get_DesiredMaxBitrate, put_DesiredMaxBitrate)
    AudioOnlyPlayback = property(get_AudioOnlyPlayback, None)
    InboundBitsPerSecond = property(get_InboundBitsPerSecond, None)
    InboundBitsPerSecondWindow = property(get_InboundBitsPerSecondWindow, put_InboundBitsPerSecondWindow)
class IAdaptiveMediaSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{17890342-6760-4bb9-a58a-f7aa98b08c0e}')
    @winrt_commethod(6)
    def get_AdvancedSettings(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceAdvancedSettings: ...
    AdvancedSettings = property(get_AdvancedSettings, None)
class IAdaptiveMediaSource3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ba7023fd-c334-461b-a36e-c99f54f7174a}')
    @winrt_commethod(6)
    def get_MinLiveOffset(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_MaxSeekableWindowSize(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(8)
    def get_DesiredSeekableWindowSize(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def put_DesiredSeekableWindowSize(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(10)
    def get_Diagnostics(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnostics: ...
    @winrt_commethod(11)
    def GetCorrelatedTimes(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCorrelatedTimes: ...
    MinLiveOffset = property(get_MinLiveOffset, None)
    MaxSeekableWindowSize = property(get_MaxSeekableWindowSize, None)
    DesiredSeekableWindowSize = property(get_DesiredSeekableWindowSize, put_DesiredSeekableWindowSize)
    Diagnostics = property(get_Diagnostics, None)
class IAdaptiveMediaSourceAdvancedSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{55db1680-1aeb-47dc-aa08-9a11610ba45a}')
    @winrt_commethod(6)
    def get_AllSegmentsIndependent(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllSegmentsIndependent(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredBitrateHeadroomRatio(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def put_DesiredBitrateHeadroomRatio(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(10)
    def get_BitrateDowngradeTriggerRatio(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def put_BitrateDowngradeTriggerRatio(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    AllSegmentsIndependent = property(get_AllSegmentsIndependent, put_AllSegmentsIndependent)
    DesiredBitrateHeadroomRatio = property(get_DesiredBitrateHeadroomRatio, put_DesiredBitrateHeadroomRatio)
    BitrateDowngradeTriggerRatio = property(get_BitrateDowngradeTriggerRatio, put_BitrateDowngradeTriggerRatio)
class IAdaptiveMediaSourceCorrelatedTimes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{05108787-e032-48e1-ab8d-002b0b3051df}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_PresentationTimeStamp(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(8)
    def get_ProgramDateTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    Position = property(get_Position, None)
    PresentationTimeStamp = property(get_PresentationTimeStamp, None)
    ProgramDateTime = property(get_ProgramDateTime, None)
class IAdaptiveMediaSourceCreationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4686b6b2-800f-4e31-9093-76d4782013e7}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationStatus: ...
    @winrt_commethod(7)
    def get_MediaSource(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSource: ...
    @winrt_commethod(8)
    def get_HttpResponseMessage(self) -> Windows.Web.Http.HttpResponseMessage: ...
    Status = property(get_Status, None)
    MediaSource = property(get_MediaSource, None)
    HttpResponseMessage = property(get_HttpResponseMessage, None)
class IAdaptiveMediaSourceCreationResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1c3243bf-1c44-404b-a201-df45ac7898e8}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IAdaptiveMediaSourceDiagnosticAvailableEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3af64f06-6d9c-494a-b7a9-b3a5dee6ad68}')
    @winrt_commethod(6)
    def get_DiagnosticType(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnosticType: ...
    @winrt_commethod(7)
    def get_RequestId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def get_SegmentId(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(10)
    def get_ResourceType(self) -> Windows.Foundation.IReference[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType]: ...
    @winrt_commethod(11)
    def get_ResourceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def get_ResourceByteRangeOffset(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(13)
    def get_ResourceByteRangeLength(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(14)
    def get_Bitrate(self) -> Windows.Foundation.IReference[UInt32]: ...
    DiagnosticType = property(get_DiagnosticType, None)
    RequestId = property(get_RequestId, None)
    Position = property(get_Position, None)
    SegmentId = property(get_SegmentId, None)
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    Bitrate = property(get_Bitrate, None)
class IAdaptiveMediaSourceDiagnosticAvailableEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8c6dd857-16a5-4d9f-810e-00bd901b3ef9}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IAdaptiveMediaSourceDiagnosticAvailableEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c3650cd5-daeb-4103-84da-68769ad513ff}')
    @winrt_commethod(6)
    def get_ResourceDuration(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_ResourceContentType(self) -> WinRT_String: ...
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
class IAdaptiveMediaSourceDiagnostics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9b24ee68-962e-448c-aebf-b29b56098e23}')
    @winrt_commethod(6)
    def add_DiagnosticAvailable(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnostics, Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnosticAvailableEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_DiagnosticAvailable(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IAdaptiveMediaSourceDownloadBitrateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{670c0a44-e04e-4eff-816a-17399f78f4ba}')
    @winrt_commethod(6)
    def get_OldValue(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_NewValue(self) -> UInt32: ...
    OldValue = property(get_OldValue, None)
    NewValue = property(get_NewValue, None)
class IAdaptiveMediaSourceDownloadBitrateChangedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f3f1f444-96ae-4de0-b540-2b3246e6968c}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadBitrateChangedReason: ...
    Reason = property(get_Reason, None)
class IAdaptiveMediaSourceDownloadCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{19240dc3-5b37-4a1a-8970-d621cb6ca83b}')
    @winrt_commethod(6)
    def get_ResourceType(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType: ...
    @winrt_commethod(7)
    def get_ResourceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_ResourceByteRangeOffset(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(9)
    def get_ResourceByteRangeLength(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(10)
    def get_HttpResponseMessage(self) -> Windows.Web.Http.HttpResponseMessage: ...
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    HttpResponseMessage = property(get_HttpResponseMessage, None)
class IAdaptiveMediaSourceDownloadCompletedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{704744c4-964a-40e4-af95-9177dd6dfa00}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Statistics(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadStatistics: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    RequestId = property(get_RequestId, None)
    Statistics = property(get_Statistics, None)
    Position = property(get_Position, None)
class IAdaptiveMediaSourceDownloadCompletedEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0f8a8bd1-93b2-47c6-badc-8be2c8f7f6e8}')
    @winrt_commethod(6)
    def get_ResourceDuration(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_ResourceContentType(self) -> WinRT_String: ...
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
class IAdaptiveMediaSourceDownloadFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{37739048-f4ab-40a4-b135-c6dfd8bd7ff1}')
    @winrt_commethod(6)
    def get_ResourceType(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType: ...
    @winrt_commethod(7)
    def get_ResourceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_ResourceByteRangeOffset(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(9)
    def get_ResourceByteRangeLength(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(10)
    def get_HttpResponseMessage(self) -> Windows.Web.Http.HttpResponseMessage: ...
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    HttpResponseMessage = property(get_HttpResponseMessage, None)
class IAdaptiveMediaSourceDownloadFailedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{70919568-967c-4986-90c5-c6fc4b31e2d8}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Statistics(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadStatistics: ...
    @winrt_commethod(9)
    def get_Position(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    RequestId = property(get_RequestId, None)
    ExtendedError = property(get_ExtendedError, None)
    Statistics = property(get_Statistics, None)
    Position = property(get_Position, None)
class IAdaptiveMediaSourceDownloadFailedEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d0354549-1132-4a10-915a-c2211b5b9409}')
    @winrt_commethod(6)
    def get_ResourceDuration(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_ResourceContentType(self) -> WinRT_String: ...
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
class IAdaptiveMediaSourceDownloadRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{05c68f64-fa20-4dbd-9821-4bf4c9bf77ab}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IAdaptiveMediaSourceDownloadRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c83fdffd-44a9-47a2-bf96-03398b4bfaaf}')
    @winrt_commethod(6)
    def get_ResourceType(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType: ...
    @winrt_commethod(7)
    def get_ResourceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_ResourceByteRangeOffset(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(9)
    def get_ResourceByteRangeLength(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(10)
    def get_Result(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadResult: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadRequestedDeferral: ...
    ResourceType = property(get_ResourceType, None)
    ResourceUri = property(get_ResourceUri, None)
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, None)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, None)
    Result = property(get_Result, None)
class IAdaptiveMediaSourceDownloadRequestedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b37d8bfe-aa44-4d82-825b-611de3bcfecb}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    RequestId = property(get_RequestId, None)
    Position = property(get_Position, None)
class IAdaptiveMediaSourceDownloadRequestedEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{333c50fd-4f62-4481-ab44-1e47b0574225}')
    @winrt_commethod(6)
    def get_ResourceDuration(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_ResourceContentType(self) -> WinRT_String: ...
    ResourceDuration = property(get_ResourceDuration, None)
    ResourceContentType = property(get_ResourceContentType, None)
class IAdaptiveMediaSourceDownloadResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f4afdc73-bcee-4a6a-9f0a-fec41e2339b0}')
    @winrt_commethod(6)
    def get_ResourceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_ResourceUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(9)
    def put_InputStream(self, value: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(10)
    def get_Buffer(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def put_Buffer(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(12)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_ContentType(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_ExtendedStatus(self) -> UInt32: ...
    @winrt_commethod(15)
    def put_ExtendedStatus(self, value: UInt32) -> Void: ...
    ResourceUri = property(get_ResourceUri, put_ResourceUri)
    InputStream = property(get_InputStream, put_InputStream)
    Buffer = property(get_Buffer, put_Buffer)
    ContentType = property(get_ContentType, put_ContentType)
    ExtendedStatus = property(get_ExtendedStatus, put_ExtendedStatus)
class IAdaptiveMediaSourceDownloadResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{15552cb7-7b80-4ac4-8660-a4b97f7c70f0}')
    @winrt_commethod(6)
    def get_ResourceByteRangeOffset(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(7)
    def put_ResourceByteRangeOffset(self, value: Windows.Foundation.IReference[UInt64]) -> Void: ...
    @winrt_commethod(8)
    def get_ResourceByteRangeLength(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(9)
    def put_ResourceByteRangeLength(self, value: Windows.Foundation.IReference[UInt64]) -> Void: ...
    ResourceByteRangeOffset = property(get_ResourceByteRangeOffset, put_ResourceByteRangeOffset)
    ResourceByteRangeLength = property(get_ResourceByteRangeLength, put_ResourceByteRangeLength)
class IAdaptiveMediaSourceDownloadStatistics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a306cefb-e96a-4dff-a9b8-1ae08c01ae98}')
    @winrt_commethod(6)
    def get_ContentBytesReceivedCount(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_TimeToHeadersReceived(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(8)
    def get_TimeToFirstByteReceived(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def get_TimeToLastByteReceived(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    ContentBytesReceivedCount = property(get_ContentBytesReceivedCount, None)
    TimeToHeadersReceived = property(get_TimeToHeadersReceived, None)
    TimeToFirstByteReceived = property(get_TimeToFirstByteReceived, None)
    TimeToLastByteReceived = property(get_TimeToLastByteReceived, None)
class IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{23a29f6d-7dda-4a51-87a9-6fa8c5b292be}')
    @winrt_commethod(6)
    def get_OldValue(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_NewValue(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_AudioOnly(self) -> Boolean: ...
    OldValue = property(get_OldValue, None)
    NewValue = property(get_NewValue, None)
    AudioOnly = property(get_AudioOnly, None)
class IAdaptiveMediaSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{50a6bd5d-66ef-4cd3-9579-9e660507dc3f}')
    @winrt_commethod(6)
    def IsContentTypeSupported(self, contentType: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def CreateFromUriAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
    @winrt_commethod(8)
    def CreateFromUriWithDownloaderAsync(self, uri: Windows.Foundation.Uri, httpClient: Windows.Web.Http.HttpClient) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
    @winrt_commethod(9)
    def CreateFromStreamAsync(self, stream: Windows.Storage.Streams.IInputStream, uri: Windows.Foundation.Uri, contentType: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
    @winrt_commethod(10)
    def CreateFromStreamWithDownloaderAsync(self, stream: Windows.Storage.Streams.IInputStream, uri: Windows.Foundation.Uri, contentType: WinRT_String, httpClient: Windows.Web.Http.HttpClient) -> Windows.Foundation.IAsyncOperation[Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationResult]: ...
make_head(_module, 'AdaptiveMediaSource')
make_head(_module, 'AdaptiveMediaSourceAdvancedSettings')
make_head(_module, 'AdaptiveMediaSourceCorrelatedTimes')
make_head(_module, 'AdaptiveMediaSourceCreationResult')
make_head(_module, 'AdaptiveMediaSourceDiagnosticAvailableEventArgs')
make_head(_module, 'AdaptiveMediaSourceDiagnostics')
make_head(_module, 'AdaptiveMediaSourceDownloadBitrateChangedEventArgs')
make_head(_module, 'AdaptiveMediaSourceDownloadCompletedEventArgs')
make_head(_module, 'AdaptiveMediaSourceDownloadFailedEventArgs')
make_head(_module, 'AdaptiveMediaSourceDownloadRequestedDeferral')
make_head(_module, 'AdaptiveMediaSourceDownloadRequestedEventArgs')
make_head(_module, 'AdaptiveMediaSourceDownloadResult')
make_head(_module, 'AdaptiveMediaSourceDownloadStatistics')
make_head(_module, 'AdaptiveMediaSourcePlaybackBitrateChangedEventArgs')
make_head(_module, 'IAdaptiveMediaSource')
make_head(_module, 'IAdaptiveMediaSource2')
make_head(_module, 'IAdaptiveMediaSource3')
make_head(_module, 'IAdaptiveMediaSourceAdvancedSettings')
make_head(_module, 'IAdaptiveMediaSourceCorrelatedTimes')
make_head(_module, 'IAdaptiveMediaSourceCreationResult')
make_head(_module, 'IAdaptiveMediaSourceCreationResult2')
make_head(_module, 'IAdaptiveMediaSourceDiagnosticAvailableEventArgs')
make_head(_module, 'IAdaptiveMediaSourceDiagnosticAvailableEventArgs2')
make_head(_module, 'IAdaptiveMediaSourceDiagnosticAvailableEventArgs3')
make_head(_module, 'IAdaptiveMediaSourceDiagnostics')
make_head(_module, 'IAdaptiveMediaSourceDownloadBitrateChangedEventArgs')
make_head(_module, 'IAdaptiveMediaSourceDownloadBitrateChangedEventArgs2')
make_head(_module, 'IAdaptiveMediaSourceDownloadCompletedEventArgs')
make_head(_module, 'IAdaptiveMediaSourceDownloadCompletedEventArgs2')
make_head(_module, 'IAdaptiveMediaSourceDownloadCompletedEventArgs3')
make_head(_module, 'IAdaptiveMediaSourceDownloadFailedEventArgs')
make_head(_module, 'IAdaptiveMediaSourceDownloadFailedEventArgs2')
make_head(_module, 'IAdaptiveMediaSourceDownloadFailedEventArgs3')
make_head(_module, 'IAdaptiveMediaSourceDownloadRequestedDeferral')
make_head(_module, 'IAdaptiveMediaSourceDownloadRequestedEventArgs')
make_head(_module, 'IAdaptiveMediaSourceDownloadRequestedEventArgs2')
make_head(_module, 'IAdaptiveMediaSourceDownloadRequestedEventArgs3')
make_head(_module, 'IAdaptiveMediaSourceDownloadResult')
make_head(_module, 'IAdaptiveMediaSourceDownloadResult2')
make_head(_module, 'IAdaptiveMediaSourceDownloadStatistics')
make_head(_module, 'IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs')
make_head(_module, 'IAdaptiveMediaSourceStatics')
