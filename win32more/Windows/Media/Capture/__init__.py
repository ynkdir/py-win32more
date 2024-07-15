from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Capture.Core
import win32more.Windows.Media.Capture.Frames
import win32more.Windows.Media.Core
import win32more.Windows.Media.Devices
import win32more.Windows.Media.Effects
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Security.Authentication.Web
import win32more.Windows.Security.Credentials
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI.WindowManagement
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AdvancedCapturedPhoto(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAdvancedCapturedPhoto
    _classid_ = 'Windows.Media.Capture.AdvancedCapturedPhoto'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Capture.IAdvancedCapturedPhoto) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Capture.IAdvancedCapturedPhoto) -> win32more.Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_mixinmethod
    def get_Context(self: win32more.Windows.Media.Capture.IAdvancedCapturedPhoto) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_FrameBoundsRelativeToReferencePhoto(self: win32more.Windows.Media.Capture.IAdvancedCapturedPhoto2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    Context = property(get_Context, None)
    Frame = property(get_Frame, None)
    FrameBoundsRelativeToReferencePhoto = property(get_FrameBoundsRelativeToReferencePhoto, None)
    Mode = property(get_Mode, None)
class AdvancedPhotoCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAdvancedPhotoCapture
    _classid_ = 'Windows.Media.Capture.AdvancedPhotoCapture'
    @winrt_mixinmethod
    def CaptureAsync(self: win32more.Windows.Media.Capture.IAdvancedPhotoCapture) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_mixinmethod
    def CaptureWithContextAsync(self: win32more.Windows.Media.Capture.IAdvancedPhotoCapture, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_mixinmethod
    def add_OptionalReferencePhotoCaptured(self: win32more.Windows.Media.Capture.IAdvancedPhotoCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AdvancedPhotoCapture, win32more.Windows.Media.Capture.OptionalReferencePhotoCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionalReferencePhotoCaptured(self: win32more.Windows.Media.Capture.IAdvancedPhotoCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AllPhotosCaptured(self: win32more.Windows.Media.Capture.IAdvancedPhotoCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AdvancedPhotoCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AllPhotosCaptured(self: win32more.Windows.Media.Capture.IAdvancedPhotoCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FinishAsync(self: win32more.Windows.Media.Capture.IAdvancedPhotoCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    OptionalReferencePhotoCaptured = event()
    AllPhotosCaptured = event()
class AppBroadcastBackgroundService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService
    _classid_ = 'Windows.Media.Capture.AppBroadcastBackgroundService'
    @winrt_mixinmethod
    def put_PlugInState(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService, value: win32more.Windows.Media.Capture.AppBroadcastPlugInState) -> Void: ...
    @winrt_mixinmethod
    def get_PlugInState(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService) -> win32more.Windows.Media.Capture.AppBroadcastPlugInState: ...
    @winrt_mixinmethod
    def put_SignInInfo(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService, value: win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo) -> Void: ...
    @winrt_mixinmethod
    def get_SignInInfo(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService) -> win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo: ...
    @winrt_mixinmethod
    def put_StreamInfo(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService, value: win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo) -> Void: ...
    @winrt_mixinmethod
    def get_StreamInfo(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService) -> win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BroadcastTitle(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ViewerCount(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ViewerCount(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService) -> UInt32: ...
    @winrt_mixinmethod
    def TerminateBroadcast(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService, reason: win32more.Windows.Media.Capture.AppBroadcastTerminationReason, providerSpecificReason: UInt32) -> Void: ...
    @winrt_mixinmethod
    def add_HeartbeatRequested(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Media.Capture.AppBroadcastHeartbeatRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeartbeatRequested(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_TitleId(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_BroadcastTitle(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BroadcastLanguage(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_BroadcastLanguage(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BroadcastChannel(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_BroadcastChannel(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_BroadcastTitleChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BroadcastTitleChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BroadcastLanguageChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BroadcastLanguageChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BroadcastChannelChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BroadcastChannelChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundService2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AppId = property(get_AppId, None)
    BroadcastChannel = property(get_BroadcastChannel, put_BroadcastChannel)
    BroadcastLanguage = property(get_BroadcastLanguage, put_BroadcastLanguage)
    BroadcastTitle = property(get_BroadcastTitle, put_BroadcastTitle)
    PlugInState = property(get_PlugInState, put_PlugInState)
    SignInInfo = property(get_SignInInfo, put_SignInInfo)
    StreamInfo = property(get_StreamInfo, put_StreamInfo)
    TitleId = property(get_TitleId, None)
    ViewerCount = property(get_ViewerCount, put_ViewerCount)
    HeartbeatRequested = event()
    BroadcastTitleChanged = event()
    BroadcastLanguageChanged = event()
    BroadcastChannelChanged = event()
class AppBroadcastBackgroundServiceSignInInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo
    _classid_ = 'Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo'
    @winrt_mixinmethod
    def get_SignInState(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo) -> win32more.Windows.Media.Capture.AppBroadcastSignInState: ...
    @winrt_mixinmethod
    def put_OAuthRequestUri(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_OAuthRequestUri(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_OAuthCallbackUri(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_OAuthCallbackUri(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AuthenticationResult(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def put_UserName(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_SignInStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo, win32more.Windows.Media.Capture.AppBroadcastSignInStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SignInStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserNameChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserNameChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AuthenticationResult = property(get_AuthenticationResult, None)
    OAuthCallbackUri = property(get_OAuthCallbackUri, put_OAuthCallbackUri)
    OAuthRequestUri = property(get_OAuthRequestUri, put_OAuthRequestUri)
    SignInState = property(get_SignInState, None)
    UserName = property(get_UserName, put_UserName)
    SignInStateChanged = event()
    UserNameChanged = event()
class AppBroadcastBackgroundServiceStreamInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo
    _classid_ = 'Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo'
    @winrt_mixinmethod
    def get_StreamState(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo) -> win32more.Windows.Media.Capture.AppBroadcastStreamState: ...
    @winrt_mixinmethod
    def put_DesiredVideoEncodingBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredVideoEncodingBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo) -> UInt64: ...
    @winrt_mixinmethod
    def put_BandwidthTestBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_BandwidthTestBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo) -> UInt64: ...
    @winrt_mixinmethod
    def put_AudioCodec(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AudioCodec(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BroadcastStreamReader(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo) -> win32more.Windows.Media.Capture.AppBroadcastStreamReader: ...
    @winrt_mixinmethod
    def add_StreamStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo, win32more.Windows.Media.Capture.AppBroadcastStreamStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StreamStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoEncodingResolutionChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoEncodingResolutionChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoEncodingBitrateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoEncodingBitrateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ReportProblemWithStream(self: win32more.Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo2) -> Void: ...
    AudioCodec = property(get_AudioCodec, put_AudioCodec)
    BandwidthTestBitrate = property(get_BandwidthTestBitrate, put_BandwidthTestBitrate)
    BroadcastStreamReader = property(get_BroadcastStreamReader, None)
    DesiredVideoEncodingBitrate = property(get_DesiredVideoEncodingBitrate, put_DesiredVideoEncodingBitrate)
    StreamState = property(get_StreamState, None)
    StreamStateChanged = event()
    VideoEncodingResolutionChanged = event()
    VideoEncodingBitrateChanged = event()
class AppBroadcastCameraCaptureState(Enum, Int32):
    Stopped = 0
    Started = 1
    Failed = 2
class AppBroadcastCameraCaptureStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastCameraCaptureStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastCameraCaptureStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Capture.IAppBroadcastCameraCaptureStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppBroadcastCameraCaptureState: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Capture.IAppBroadcastCameraCaptureStateChangedEventArgs) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class AppBroadcastCameraOverlayLocation(Enum, Int32):
    TopLeft = 0
    TopCenter = 1
    TopRight = 2
    MiddleLeft = 3
    MiddleCenter = 4
    MiddleRight = 5
    BottomLeft = 6
    BottomCenter = 7
    BottomRight = 8
class AppBroadcastCameraOverlaySize(Enum, Int32):
    Small = 0
    Medium = 1
    Large = 2
class AppBroadcastCaptureTargetType(Enum, Int32):
    AppView = 0
    EntireDisplay = 1
AppBroadcastContract: UInt32 = 131072
class AppBroadcastExitBroadcastModeReason(Enum, Int32):
    NormalExit = 0
    UserCanceled = 1
    AuthorizationFail = 2
    ForegroundAppActivated = 3
class AppBroadcastGlobalSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings
    _classid_ = 'Windows.Media.Capture.AppBroadcastGlobalSettings'
    @winrt_mixinmethod
    def get_IsBroadcastEnabled(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledByPolicy(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGpuConstrained(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasHardwareEncoder(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAudioCaptureEnabled(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAudioCaptureEnabled(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsMicrophoneCaptureEnabledByDefault(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsMicrophoneCaptureEnabledByDefault(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEchoCancellationEnabled(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsEchoCancellationEnabled(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_SystemAudioGain(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SystemAudioGain(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Double: ...
    @winrt_mixinmethod
    def put_MicrophoneGain(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MicrophoneGain(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Double: ...
    @winrt_mixinmethod
    def put_IsCameraCaptureEnabledByDefault(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCameraCaptureEnabledByDefault(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_SelectedCameraId(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedCameraId(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CameraOverlayLocation(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: win32more.Windows.Media.Capture.AppBroadcastCameraOverlayLocation) -> Void: ...
    @winrt_mixinmethod
    def get_CameraOverlayLocation(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> win32more.Windows.Media.Capture.AppBroadcastCameraOverlayLocation: ...
    @winrt_mixinmethod
    def put_CameraOverlaySize(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: win32more.Windows.Media.Capture.AppBroadcastCameraOverlaySize) -> Void: ...
    @winrt_mixinmethod
    def get_CameraOverlaySize(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> win32more.Windows.Media.Capture.AppBroadcastCameraOverlaySize: ...
    @winrt_mixinmethod
    def put_IsCursorImageCaptureEnabled(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCursorImageCaptureEnabled(self: win32more.Windows.Media.Capture.IAppBroadcastGlobalSettings) -> Boolean: ...
    CameraOverlayLocation = property(get_CameraOverlayLocation, put_CameraOverlayLocation)
    CameraOverlaySize = property(get_CameraOverlaySize, put_CameraOverlaySize)
    HasHardwareEncoder = property(get_HasHardwareEncoder, None)
    IsAudioCaptureEnabled = property(get_IsAudioCaptureEnabled, put_IsAudioCaptureEnabled)
    IsBroadcastEnabled = property(get_IsBroadcastEnabled, None)
    IsCameraCaptureEnabledByDefault = property(get_IsCameraCaptureEnabledByDefault, put_IsCameraCaptureEnabledByDefault)
    IsCursorImageCaptureEnabled = property(get_IsCursorImageCaptureEnabled, put_IsCursorImageCaptureEnabled)
    IsDisabledByPolicy = property(get_IsDisabledByPolicy, None)
    IsEchoCancellationEnabled = property(get_IsEchoCancellationEnabled, put_IsEchoCancellationEnabled)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsMicrophoneCaptureEnabledByDefault = property(get_IsMicrophoneCaptureEnabledByDefault, put_IsMicrophoneCaptureEnabledByDefault)
    MicrophoneGain = property(get_MicrophoneGain, put_MicrophoneGain)
    SelectedCameraId = property(get_SelectedCameraId, put_SelectedCameraId)
    SystemAudioGain = property(get_SystemAudioGain, put_SystemAudioGain)
class AppBroadcastHeartbeatRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastHeartbeatRequestedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastHeartbeatRequestedEventArgs'
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Media.Capture.IAppBroadcastHeartbeatRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Media.Capture.IAppBroadcastHeartbeatRequestedEventArgs) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class AppBroadcastManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.AppBroadcastManager'
    @winrt_classmethod
    def GetGlobalSettings(cls: win32more.Windows.Media.Capture.IAppBroadcastManagerStatics) -> win32more.Windows.Media.Capture.AppBroadcastGlobalSettings: ...
    @winrt_classmethod
    def ApplyGlobalSettings(cls: win32more.Windows.Media.Capture.IAppBroadcastManagerStatics, value: win32more.Windows.Media.Capture.AppBroadcastGlobalSettings) -> Void: ...
    @winrt_classmethod
    def GetProviderSettings(cls: win32more.Windows.Media.Capture.IAppBroadcastManagerStatics) -> win32more.Windows.Media.Capture.AppBroadcastProviderSettings: ...
    @winrt_classmethod
    def ApplyProviderSettings(cls: win32more.Windows.Media.Capture.IAppBroadcastManagerStatics, value: win32more.Windows.Media.Capture.AppBroadcastProviderSettings) -> Void: ...
class AppBroadcastMicrophoneCaptureState(Enum, Int32):
    Stopped = 0
    Started = 1
    Failed = 2
class AppBroadcastMicrophoneCaptureStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastMicrophoneCaptureStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastMicrophoneCaptureStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Capture.IAppBroadcastMicrophoneCaptureStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppBroadcastMicrophoneCaptureState: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Capture.IAppBroadcastMicrophoneCaptureStateChangedEventArgs) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class AppBroadcastPlugIn(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPlugIn
    _classid_ = 'Windows.Media.Capture.AppBroadcastPlugIn'
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Media.Capture.IAppBroadcastPlugIn) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderSettings(self: win32more.Windows.Media.Capture.IAppBroadcastPlugIn) -> win32more.Windows.Media.Capture.AppBroadcastProviderSettings: ...
    @winrt_mixinmethod
    def get_Logo(self: win32more.Windows.Media.Capture.IAppBroadcastPlugIn) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.Capture.IAppBroadcastPlugIn) -> WinRT_String: ...
    AppId = property(get_AppId, None)
    DisplayName = property(get_DisplayName, None)
    Logo = property(get_Logo, None)
    ProviderSettings = property(get_ProviderSettings, None)
class AppBroadcastPlugInManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPlugInManager
    _classid_ = 'Windows.Media.Capture.AppBroadcastPlugInManager'
    @winrt_mixinmethod
    def get_IsBroadcastProviderAvailable(self: win32more.Windows.Media.Capture.IAppBroadcastPlugInManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_PlugInList(self: win32more.Windows.Media.Capture.IAppBroadcastPlugInManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.AppBroadcastPlugIn]: ...
    @winrt_mixinmethod
    def get_DefaultPlugIn(self: win32more.Windows.Media.Capture.IAppBroadcastPlugInManager) -> win32more.Windows.Media.Capture.AppBroadcastPlugIn: ...
    @winrt_mixinmethod
    def put_DefaultPlugIn(self: win32more.Windows.Media.Capture.IAppBroadcastPlugInManager, value: win32more.Windows.Media.Capture.AppBroadcastPlugIn) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Media.Capture.IAppBroadcastPlugInManagerStatics) -> win32more.Windows.Media.Capture.AppBroadcastPlugInManager: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Media.Capture.IAppBroadcastPlugInManagerStatics, user: win32more.Windows.System.User) -> win32more.Windows.Media.Capture.AppBroadcastPlugInManager: ...
    DefaultPlugIn = property(get_DefaultPlugIn, put_DefaultPlugIn)
    IsBroadcastProviderAvailable = property(get_IsBroadcastProviderAvailable, None)
    PlugInList = property(get_PlugInList, None)
class AppBroadcastPlugInState(Enum, Int32):
    Unknown = 0
    Initialized = 1
    MicrosoftSignInRequired = 2
    OAuthSignInRequired = 3
    ProviderSignInRequired = 4
    InBandwidthTest = 5
    ReadyToBroadcast = 6
class AppBroadcastPlugInStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPlugInStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastPlugInStateChangedEventArgs'
    @winrt_mixinmethod
    def get_PlugInState(self: win32more.Windows.Media.Capture.IAppBroadcastPlugInStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppBroadcastPlugInState: ...
    PlugInState = property(get_PlugInState, None)
class AppBroadcastPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPreview
    _classid_ = 'Windows.Media.Capture.AppBroadcastPreview'
    @winrt_mixinmethod
    def StopPreview(self: win32more.Windows.Media.Capture.IAppBroadcastPreview) -> Void: ...
    @winrt_mixinmethod
    def get_PreviewState(self: win32more.Windows.Media.Capture.IAppBroadcastPreview) -> win32more.Windows.Media.Capture.AppBroadcastPreviewState: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Capture.IAppBroadcastPreview) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def add_PreviewStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastPreview, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastPreview, win32more.Windows.Media.Capture.AppBroadcastPreviewStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PreviewStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_PreviewStreamReader(self: win32more.Windows.Media.Capture.IAppBroadcastPreview) -> win32more.Windows.Media.Capture.AppBroadcastPreviewStreamReader: ...
    ErrorCode = property(get_ErrorCode, None)
    PreviewState = property(get_PreviewState, None)
    PreviewStreamReader = property(get_PreviewStreamReader, None)
    PreviewStateChanged = event()
class AppBroadcastPreviewState(Enum, Int32):
    Started = 0
    Stopped = 1
    Failed = 2
class AppBroadcastPreviewStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPreviewStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastPreviewStateChangedEventArgs'
    @winrt_mixinmethod
    def get_PreviewState(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppBroadcastPreviewState: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStateChangedEventArgs) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    PreviewState = property(get_PreviewState, None)
class AppBroadcastPreviewStreamReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader
    _classid_ = 'Windows.Media.Capture.AppBroadcastPreviewStreamReader'
    @winrt_mixinmethod
    def get_VideoWidth(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideoHeight(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideoStride(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideoBitmapPixelFormat(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_VideoBitmapAlphaMode(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def TryGetNextVideoFrame(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader) -> win32more.Windows.Media.Capture.AppBroadcastPreviewStreamVideoFrame: ...
    @winrt_mixinmethod
    def add_VideoFrameArrived(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastPreviewStreamReader, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoFrameArrived(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    VideoBitmapAlphaMode = property(get_VideoBitmapAlphaMode, None)
    VideoBitmapPixelFormat = property(get_VideoBitmapPixelFormat, None)
    VideoHeight = property(get_VideoHeight, None)
    VideoStride = property(get_VideoStride, None)
    VideoWidth = property(get_VideoWidth, None)
    VideoFrameArrived = event()
class AppBroadcastPreviewStreamVideoFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoFrame
    _classid_ = 'Windows.Media.Capture.AppBroadcastPreviewStreamVideoFrame'
    @winrt_mixinmethod
    def get_VideoHeader(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoFrame) -> win32more.Windows.Media.Capture.AppBroadcastPreviewStreamVideoHeader: ...
    @winrt_mixinmethod
    def get_VideoBuffer(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoFrame) -> win32more.Windows.Storage.Streams.IBuffer: ...
    VideoBuffer = property(get_VideoBuffer, None)
    VideoHeader = property(get_VideoHeader, None)
class AppBroadcastPreviewStreamVideoHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoHeader
    _classid_ = 'Windows.Media.Capture.AppBroadcastPreviewStreamVideoHeader'
    @winrt_mixinmethod
    def get_AbsoluteTimestamp(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoHeader) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_RelativeTimestamp(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoHeader) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoHeader) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Windows.Media.Capture.IAppBroadcastPreviewStreamVideoHeader) -> UInt64: ...
    AbsoluteTimestamp = property(get_AbsoluteTimestamp, None)
    Duration = property(get_Duration, None)
    FrameId = property(get_FrameId, None)
    RelativeTimestamp = property(get_RelativeTimestamp, None)
class AppBroadcastProviderSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings
    _classid_ = 'Windows.Media.Capture.AppBroadcastProviderSettings'
    @winrt_mixinmethod
    def put_DefaultBroadcastTitle(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultBroadcastTitle(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AudioEncodingBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_AudioEncodingBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_CustomVideoEncodingBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CustomVideoEncodingBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_CustomVideoEncodingHeight(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CustomVideoEncodingHeight(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_CustomVideoEncodingWidth(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CustomVideoEncodingWidth(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_VideoEncodingBitrateMode(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings, value: win32more.Windows.Media.Capture.AppBroadcastVideoEncodingBitrateMode) -> Void: ...
    @winrt_mixinmethod
    def get_VideoEncodingBitrateMode(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings) -> win32more.Windows.Media.Capture.AppBroadcastVideoEncodingBitrateMode: ...
    @winrt_mixinmethod
    def put_VideoEncodingResolutionMode(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings, value: win32more.Windows.Media.Capture.AppBroadcastVideoEncodingResolutionMode) -> Void: ...
    @winrt_mixinmethod
    def get_VideoEncodingResolutionMode(self: win32more.Windows.Media.Capture.IAppBroadcastProviderSettings) -> win32more.Windows.Media.Capture.AppBroadcastVideoEncodingResolutionMode: ...
    AudioEncodingBitrate = property(get_AudioEncodingBitrate, put_AudioEncodingBitrate)
    CustomVideoEncodingBitrate = property(get_CustomVideoEncodingBitrate, put_CustomVideoEncodingBitrate)
    CustomVideoEncodingHeight = property(get_CustomVideoEncodingHeight, put_CustomVideoEncodingHeight)
    CustomVideoEncodingWidth = property(get_CustomVideoEncodingWidth, put_CustomVideoEncodingWidth)
    DefaultBroadcastTitle = property(get_DefaultBroadcastTitle, put_DefaultBroadcastTitle)
    VideoEncodingBitrateMode = property(get_VideoEncodingBitrateMode, put_VideoEncodingBitrateMode)
    VideoEncodingResolutionMode = property(get_VideoEncodingResolutionMode, put_VideoEncodingResolutionMode)
class AppBroadcastServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastServices
    _classid_ = 'Windows.Media.Capture.AppBroadcastServices'
    @winrt_mixinmethod
    def get_CaptureTargetType(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> win32more.Windows.Media.Capture.AppBroadcastCaptureTargetType: ...
    @winrt_mixinmethod
    def put_CaptureTargetType(self: win32more.Windows.Media.Capture.IAppBroadcastServices, value: win32more.Windows.Media.Capture.AppBroadcastCaptureTargetType) -> Void: ...
    @winrt_mixinmethod
    def get_BroadcastTitle(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_BroadcastTitle(self: win32more.Windows.Media.Capture.IAppBroadcastServices, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BroadcastLanguage(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_BroadcastLanguage(self: win32more.Windows.Media.Capture.IAppBroadcastServices, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanCapture(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> Boolean: ...
    @winrt_mixinmethod
    def EnterBroadcastModeAsync(self: win32more.Windows.Media.Capture.IAppBroadcastServices, plugIn: win32more.Windows.Media.Capture.AppBroadcastPlugIn) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def ExitBroadcastMode(self: win32more.Windows.Media.Capture.IAppBroadcastServices, reason: win32more.Windows.Media.Capture.AppBroadcastExitBroadcastModeReason) -> Void: ...
    @winrt_mixinmethod
    def StartBroadcast(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> Void: ...
    @winrt_mixinmethod
    def PauseBroadcast(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> Void: ...
    @winrt_mixinmethod
    def ResumeBroadcast(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> Void: ...
    @winrt_mixinmethod
    def StartPreview(self: win32more.Windows.Media.Capture.IAppBroadcastServices, desiredSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Media.Capture.AppBroadcastPreview: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Capture.IAppBroadcastServices) -> win32more.Windows.Media.Capture.AppBroadcastState: ...
    BroadcastLanguage = property(get_BroadcastLanguage, put_BroadcastLanguage)
    BroadcastTitle = property(get_BroadcastTitle, put_BroadcastTitle)
    CanCapture = property(get_CanCapture, None)
    CaptureTargetType = property(get_CaptureTargetType, put_CaptureTargetType)
    State = property(get_State, None)
    UserName = property(get_UserName, None)
class AppBroadcastSignInResult(Enum, Int32):
    Success = 0
    AuthenticationFailed = 1
    Unauthorized = 2
    ServiceUnavailable = 3
    Unknown = 4
class AppBroadcastSignInState(Enum, Int32):
    NotSignedIn = 0
    MicrosoftSignInInProgress = 1
    MicrosoftSignInComplete = 2
    OAuthSignInInProgress = 3
    OAuthSignInComplete = 4
class AppBroadcastSignInStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastSignInStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastSignInStateChangedEventArgs'
    @winrt_mixinmethod
    def get_SignInState(self: win32more.Windows.Media.Capture.IAppBroadcastSignInStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppBroadcastSignInState: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Media.Capture.IAppBroadcastSignInStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppBroadcastSignInResult: ...
    Result = property(get_Result, None)
    SignInState = property(get_SignInState, None)
class AppBroadcastState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastState
    _classid_ = 'Windows.Media.Capture.AppBroadcastState'
    @winrt_mixinmethod
    def get_IsCaptureTargetRunning(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> Boolean: ...
    @winrt_mixinmethod
    def get_ViewerCount(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> UInt32: ...
    @winrt_mixinmethod
    def get_ShouldCaptureMicrophone(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldCaptureMicrophone(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RestartMicrophoneCapture(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldCaptureCamera(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldCaptureCamera(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RestartCameraCapture(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> Void: ...
    @winrt_mixinmethod
    def get_EncodedVideoSize(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_MicrophoneCaptureState(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Media.Capture.AppBroadcastMicrophoneCaptureState: ...
    @winrt_mixinmethod
    def get_MicrophoneCaptureError(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> UInt32: ...
    @winrt_mixinmethod
    def get_CameraCaptureState(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Media.Capture.AppBroadcastCameraCaptureState: ...
    @winrt_mixinmethod
    def get_CameraCaptureError(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> UInt32: ...
    @winrt_mixinmethod
    def get_StreamState(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Media.Capture.AppBroadcastStreamState: ...
    @winrt_mixinmethod
    def get_PlugInState(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Media.Capture.AppBroadcastPlugInState: ...
    @winrt_mixinmethod
    def get_OAuthRequestUri(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_OAuthCallbackUri(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AuthenticationResult(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def put_AuthenticationResult(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: win32more.Windows.Security.Authentication.Web.WebAuthenticationResult) -> Void: ...
    @winrt_mixinmethod
    def put_SignInState(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: win32more.Windows.Media.Capture.AppBroadcastSignInState) -> Void: ...
    @winrt_mixinmethod
    def get_SignInState(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Media.Capture.AppBroadcastSignInState: ...
    @winrt_mixinmethod
    def get_TerminationReason(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> win32more.Windows.Media.Capture.AppBroadcastTerminationReason: ...
    @winrt_mixinmethod
    def get_TerminationReasonPlugInSpecific(self: win32more.Windows.Media.Capture.IAppBroadcastState) -> UInt32: ...
    @winrt_mixinmethod
    def add_ViewerCountChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastViewerCountChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ViewerCountChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MicrophoneCaptureStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastMicrophoneCaptureStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MicrophoneCaptureStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraCaptureStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastCameraCaptureStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraCaptureStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PlugInStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastPlugInStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlugInStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StreamStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastStreamStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StreamStateChanged(self: win32more.Windows.Media.Capture.IAppBroadcastState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CaptureTargetClosed(self: win32more.Windows.Media.Capture.IAppBroadcastState, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CaptureTargetClosed(self: win32more.Windows.Media.Capture.IAppBroadcastState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AuthenticationResult = property(get_AuthenticationResult, put_AuthenticationResult)
    CameraCaptureError = property(get_CameraCaptureError, None)
    CameraCaptureState = property(get_CameraCaptureState, None)
    EncodedVideoSize = property(get_EncodedVideoSize, None)
    IsCaptureTargetRunning = property(get_IsCaptureTargetRunning, None)
    MicrophoneCaptureError = property(get_MicrophoneCaptureError, None)
    MicrophoneCaptureState = property(get_MicrophoneCaptureState, None)
    OAuthCallbackUri = property(get_OAuthCallbackUri, None)
    OAuthRequestUri = property(get_OAuthRequestUri, None)
    PlugInState = property(get_PlugInState, None)
    ShouldCaptureCamera = property(get_ShouldCaptureCamera, put_ShouldCaptureCamera)
    ShouldCaptureMicrophone = property(get_ShouldCaptureMicrophone, put_ShouldCaptureMicrophone)
    SignInState = property(get_SignInState, put_SignInState)
    StreamState = property(get_StreamState, None)
    TerminationReason = property(get_TerminationReason, None)
    TerminationReasonPlugInSpecific = property(get_TerminationReasonPlugInSpecific, None)
    ViewerCount = property(get_ViewerCount, None)
    ViewerCountChanged = event()
    MicrophoneCaptureStateChanged = event()
    CameraCaptureStateChanged = event()
    PlugInStateChanged = event()
    StreamStateChanged = event()
    CaptureTargetClosed = event()
class AppBroadcastStreamAudioFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioFrame
    _classid_ = 'Windows.Media.Capture.AppBroadcastStreamAudioFrame'
    @winrt_mixinmethod
    def get_AudioHeader(self: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioFrame) -> win32more.Windows.Media.Capture.AppBroadcastStreamAudioHeader: ...
    @winrt_mixinmethod
    def get_AudioBuffer(self: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioFrame) -> win32more.Windows.Storage.Streams.IBuffer: ...
    AudioBuffer = property(get_AudioBuffer, None)
    AudioHeader = property(get_AudioHeader, None)
class AppBroadcastStreamAudioHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioHeader
    _classid_ = 'Windows.Media.Capture.AppBroadcastStreamAudioHeader'
    @winrt_mixinmethod
    def get_AbsoluteTimestamp(self: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioHeader) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_RelativeTimestamp(self: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioHeader) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioHeader) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_HasDiscontinuity(self: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioHeader) -> Boolean: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Windows.Media.Capture.IAppBroadcastStreamAudioHeader) -> UInt64: ...
    AbsoluteTimestamp = property(get_AbsoluteTimestamp, None)
    Duration = property(get_Duration, None)
    FrameId = property(get_FrameId, None)
    HasDiscontinuity = property(get_HasDiscontinuity, None)
    RelativeTimestamp = property(get_RelativeTimestamp, None)
class AppBroadcastStreamReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastStreamReader
    _classid_ = 'Windows.Media.Capture.AppBroadcastStreamReader'
    @winrt_mixinmethod
    def get_AudioChannels(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def get_AudioSampleRate(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def get_AudioAacSequence(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AudioBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def TryGetNextAudioFrame(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> win32more.Windows.Media.Capture.AppBroadcastStreamAudioFrame: ...
    @winrt_mixinmethod
    def get_VideoWidth(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideoHeight(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideoBitrate(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> UInt32: ...
    @winrt_mixinmethod
    def TryGetNextVideoFrame(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader) -> win32more.Windows.Media.Capture.AppBroadcastStreamVideoFrame: ...
    @winrt_mixinmethod
    def add_AudioFrameArrived(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastStreamReader, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioFrameArrived(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoFrameArrived(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastStreamReader, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoFrameArrived(self: win32more.Windows.Media.Capture.IAppBroadcastStreamReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AudioAacSequence = property(get_AudioAacSequence, None)
    AudioBitrate = property(get_AudioBitrate, None)
    AudioChannels = property(get_AudioChannels, None)
    AudioSampleRate = property(get_AudioSampleRate, None)
    VideoBitrate = property(get_VideoBitrate, None)
    VideoHeight = property(get_VideoHeight, None)
    VideoWidth = property(get_VideoWidth, None)
    AudioFrameArrived = event()
    VideoFrameArrived = event()
class AppBroadcastStreamState(Enum, Int32):
    Initializing = 0
    StreamReady = 1
    Started = 2
    Paused = 3
    Terminated = 4
class AppBroadcastStreamStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastStreamStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastStreamStateChangedEventArgs'
    @winrt_mixinmethod
    def get_StreamState(self: win32more.Windows.Media.Capture.IAppBroadcastStreamStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppBroadcastStreamState: ...
    StreamState = property(get_StreamState, None)
class AppBroadcastStreamVideoFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoFrame
    _classid_ = 'Windows.Media.Capture.AppBroadcastStreamVideoFrame'
    @winrt_mixinmethod
    def get_VideoHeader(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoFrame) -> win32more.Windows.Media.Capture.AppBroadcastStreamVideoHeader: ...
    @winrt_mixinmethod
    def get_VideoBuffer(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoFrame) -> win32more.Windows.Storage.Streams.IBuffer: ...
    VideoBuffer = property(get_VideoBuffer, None)
    VideoHeader = property(get_VideoHeader, None)
class AppBroadcastStreamVideoHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoHeader
    _classid_ = 'Windows.Media.Capture.AppBroadcastStreamVideoHeader'
    @winrt_mixinmethod
    def get_AbsoluteTimestamp(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoHeader) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_RelativeTimestamp(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoHeader) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoHeader) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IsKeyFrame(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoHeader) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasDiscontinuity(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoHeader) -> Boolean: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Windows.Media.Capture.IAppBroadcastStreamVideoHeader) -> UInt64: ...
    AbsoluteTimestamp = property(get_AbsoluteTimestamp, None)
    Duration = property(get_Duration, None)
    FrameId = property(get_FrameId, None)
    HasDiscontinuity = property(get_HasDiscontinuity, None)
    IsKeyFrame = property(get_IsKeyFrame, None)
    RelativeTimestamp = property(get_RelativeTimestamp, None)
class AppBroadcastTerminationReason(Enum, Int32):
    NormalTermination = 0
    LostConnectionToService = 1
    NoNetworkConnectivity = 2
    ServiceAbort = 3
    ServiceError = 4
    ServiceUnavailable = 5
    InternalError = 6
    UnsupportedFormat = 7
    BackgroundTaskTerminated = 8
    BackgroundTaskUnresponsive = 9
class AppBroadcastTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastTriggerDetails
    _classid_ = 'Windows.Media.Capture.AppBroadcastTriggerDetails'
    @winrt_mixinmethod
    def get_BackgroundService(self: win32more.Windows.Media.Capture.IAppBroadcastTriggerDetails) -> win32more.Windows.Media.Capture.AppBroadcastBackgroundService: ...
    BackgroundService = property(get_BackgroundService, None)
class AppBroadcastVideoEncodingBitrateMode(Enum, Int32):
    Custom = 0
    Auto = 1
class AppBroadcastVideoEncodingResolutionMode(Enum, Int32):
    Custom = 0
    Auto = 1
class AppBroadcastViewerCountChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppBroadcastViewerCountChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppBroadcastViewerCountChangedEventArgs'
    @winrt_mixinmethod
    def get_ViewerCount(self: win32more.Windows.Media.Capture.IAppBroadcastViewerCountChangedEventArgs) -> UInt32: ...
    ViewerCount = property(get_ViewerCount, None)
class AppCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCapture
    _classid_ = 'Windows.Media.Capture.AppCapture'
    @winrt_mixinmethod
    def get_IsCapturingAudio(self: win32more.Windows.Media.Capture.IAppCapture) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCapturingVideo(self: win32more.Windows.Media.Capture.IAppCapture) -> Boolean: ...
    @winrt_mixinmethod
    def add_CapturingChanged(self: win32more.Windows.Media.Capture.IAppCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CapturingChanged(self: win32more.Windows.Media.Capture.IAppCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def SetAllowedAsync(cls: win32more.Windows.Media.Capture.IAppCaptureStatics2, allowed: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Media.Capture.IAppCaptureStatics) -> win32more.Windows.Media.Capture.AppCapture: ...
    IsCapturingAudio = property(get_IsCapturingAudio, None)
    IsCapturingVideo = property(get_IsCapturingVideo, None)
    CapturingChanged = event()
class AppCaptureAlternateShortcutKeys(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys
    _classid_ = 'Windows.Media.Capture.AppCaptureAlternateShortcutKeys'
    @winrt_mixinmethod
    def put_ToggleGameBarKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleGameBarKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_ToggleGameBarKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleGameBarKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_SaveHistoricalVideoKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_SaveHistoricalVideoKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_SaveHistoricalVideoKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_SaveHistoricalVideoKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_ToggleRecordingKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleRecordingKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_ToggleRecordingKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleRecordingKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_TakeScreenshotKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_TakeScreenshotKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_TakeScreenshotKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_TakeScreenshotKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_ToggleRecordingIndicatorKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleRecordingIndicatorKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_ToggleRecordingIndicatorKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleRecordingIndicatorKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_ToggleMicrophoneCaptureKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys2, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleMicrophoneCaptureKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys2) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_ToggleMicrophoneCaptureKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys2, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleMicrophoneCaptureKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys2) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_ToggleCameraCaptureKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleCameraCaptureKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_ToggleCameraCaptureKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleCameraCaptureKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_ToggleBroadcastKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleBroadcastKey(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_ToggleBroadcastKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleBroadcastKeyModifiers(self: win32more.Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3) -> win32more.Windows.System.VirtualKeyModifiers: ...
    SaveHistoricalVideoKey = property(get_SaveHistoricalVideoKey, put_SaveHistoricalVideoKey)
    SaveHistoricalVideoKeyModifiers = property(get_SaveHistoricalVideoKeyModifiers, put_SaveHistoricalVideoKeyModifiers)
    TakeScreenshotKey = property(get_TakeScreenshotKey, put_TakeScreenshotKey)
    TakeScreenshotKeyModifiers = property(get_TakeScreenshotKeyModifiers, put_TakeScreenshotKeyModifiers)
    ToggleBroadcastKey = property(get_ToggleBroadcastKey, put_ToggleBroadcastKey)
    ToggleBroadcastKeyModifiers = property(get_ToggleBroadcastKeyModifiers, put_ToggleBroadcastKeyModifiers)
    ToggleCameraCaptureKey = property(get_ToggleCameraCaptureKey, put_ToggleCameraCaptureKey)
    ToggleCameraCaptureKeyModifiers = property(get_ToggleCameraCaptureKeyModifiers, put_ToggleCameraCaptureKeyModifiers)
    ToggleGameBarKey = property(get_ToggleGameBarKey, put_ToggleGameBarKey)
    ToggleGameBarKeyModifiers = property(get_ToggleGameBarKeyModifiers, put_ToggleGameBarKeyModifiers)
    ToggleMicrophoneCaptureKey = property(get_ToggleMicrophoneCaptureKey, put_ToggleMicrophoneCaptureKey)
    ToggleMicrophoneCaptureKeyModifiers = property(get_ToggleMicrophoneCaptureKeyModifiers, put_ToggleMicrophoneCaptureKeyModifiers)
    ToggleRecordingIndicatorKey = property(get_ToggleRecordingIndicatorKey, put_ToggleRecordingIndicatorKey)
    ToggleRecordingIndicatorKeyModifiers = property(get_ToggleRecordingIndicatorKeyModifiers, put_ToggleRecordingIndicatorKeyModifiers)
    ToggleRecordingKey = property(get_ToggleRecordingKey, put_ToggleRecordingKey)
    ToggleRecordingKeyModifiers = property(get_ToggleRecordingKeyModifiers, put_ToggleRecordingKeyModifiers)
AppCaptureContract: UInt32 = 262144
class AppCaptureDurationGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureDurationGeneratedEventArgs
    _classid_ = 'Windows.Media.Capture.AppCaptureDurationGeneratedEventArgs'
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Capture.IAppCaptureDurationGeneratedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    Duration = property(get_Duration, None)
class AppCaptureFileGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureFileGeneratedEventArgs
    _classid_ = 'Windows.Media.Capture.AppCaptureFileGeneratedEventArgs'
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Media.Capture.IAppCaptureFileGeneratedEventArgs) -> win32more.Windows.Storage.StorageFile: ...
    File = property(get_File, None)
class AppCaptureHistoricalBufferLengthUnit(Enum, Int32):
    Megabytes = 0
    Seconds = 1
class AppCaptureManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.AppCaptureManager'
    @winrt_classmethod
    def GetCurrentSettings(cls: win32more.Windows.Media.Capture.IAppCaptureManagerStatics) -> win32more.Windows.Media.Capture.AppCaptureSettings: ...
    @winrt_classmethod
    def ApplySettings(cls: win32more.Windows.Media.Capture.IAppCaptureManagerStatics, appCaptureSettings: win32more.Windows.Media.Capture.AppCaptureSettings) -> Void: ...
AppCaptureMetadataContract: UInt32 = 65536
class AppCaptureMetadataPriority(Enum, Int32):
    Informational = 0
    Important = 1
class AppCaptureMetadataWriter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter
    _classid_ = 'Windows.Media.Capture.AppCaptureMetadataWriter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Capture.AppCaptureMetadataWriter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Capture.AppCaptureMetadataWriter: ...
    @winrt_mixinmethod
    def AddStringEvent(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, name: WinRT_String, value: WinRT_String, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_mixinmethod
    def AddInt32Event(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, name: WinRT_String, value: Int32, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_mixinmethod
    def AddDoubleEvent(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, name: WinRT_String, value: Double, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_mixinmethod
    def StartStringState(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, name: WinRT_String, value: WinRT_String, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_mixinmethod
    def StartInt32State(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, name: WinRT_String, value: Int32, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_mixinmethod
    def StartDoubleState(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, name: WinRT_String, value: Double, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_mixinmethod
    def StopState(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def StopAllStates(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter) -> Void: ...
    @winrt_mixinmethod
    def get_RemainingStorageBytesAvailable(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter) -> UInt64: ...
    @winrt_mixinmethod
    def add_MetadataPurged(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureMetadataWriter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MetadataPurged(self: win32more.Windows.Media.Capture.IAppCaptureMetadataWriter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    RemainingStorageBytesAvailable = property(get_RemainingStorageBytesAvailable, None)
    MetadataPurged = event()
class AppCaptureMicrophoneCaptureState(Enum, Int32):
    Stopped = 0
    Started = 1
    Failed = 2
class AppCaptureMicrophoneCaptureStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureMicrophoneCaptureStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppCaptureMicrophoneCaptureStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Capture.IAppCaptureMicrophoneCaptureStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppCaptureMicrophoneCaptureState: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Capture.IAppCaptureMicrophoneCaptureStateChangedEventArgs) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class AppCaptureRecordOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureRecordOperation
    _classid_ = 'Windows.Media.Capture.AppCaptureRecordOperation'
    @winrt_mixinmethod
    def StopRecording(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation) -> win32more.Windows.Media.Capture.AppCaptureRecordingState: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_IsFileTruncated(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureRecordOperation, win32more.Windows.Media.Capture.AppCaptureRecordingStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DurationGenerated(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureRecordOperation, win32more.Windows.Media.Capture.AppCaptureDurationGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DurationGenerated(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FileGenerated(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureRecordOperation, win32more.Windows.Media.Capture.AppCaptureFileGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileGenerated(self: win32more.Windows.Media.Capture.IAppCaptureRecordOperation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Duration = property(get_Duration, None)
    ErrorCode = property(get_ErrorCode, None)
    File = property(get_File, None)
    IsFileTruncated = property(get_IsFileTruncated, None)
    State = property(get_State, None)
    StateChanged = event()
    DurationGenerated = event()
    FileGenerated = event()
class AppCaptureRecordingState(Enum, Int32):
    InProgress = 0
    Completed = 1
    Failed = 2
class AppCaptureRecordingStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureRecordingStateChangedEventArgs
    _classid_ = 'Windows.Media.Capture.AppCaptureRecordingStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Capture.IAppCaptureRecordingStateChangedEventArgs) -> win32more.Windows.Media.Capture.AppCaptureRecordingState: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Capture.IAppCaptureRecordingStateChangedEventArgs) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class AppCaptureServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureServices
    _classid_ = 'Windows.Media.Capture.AppCaptureServices'
    @winrt_mixinmethod
    def Record(self: win32more.Windows.Media.Capture.IAppCaptureServices) -> win32more.Windows.Media.Capture.AppCaptureRecordOperation: ...
    @winrt_mixinmethod
    def RecordTimeSpan(self: win32more.Windows.Media.Capture.IAppCaptureServices, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Capture.AppCaptureRecordOperation: ...
    @winrt_mixinmethod
    def get_CanCapture(self: win32more.Windows.Media.Capture.IAppCaptureServices) -> Boolean: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Capture.IAppCaptureServices) -> win32more.Windows.Media.Capture.AppCaptureState: ...
    CanCapture = property(get_CanCapture, None)
    State = property(get_State, None)
class AppCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureSettings
    _classid_ = 'Windows.Media.Capture.AppCaptureSettings'
    @winrt_mixinmethod
    def put_AppCaptureDestinationFolder(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: win32more.Windows.Storage.StorageFolder) -> Void: ...
    @winrt_mixinmethod
    def get_AppCaptureDestinationFolder(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def put_AudioEncodingBitrate(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_AudioEncodingBitrate(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_IsAudioCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAudioCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_CustomVideoEncodingBitrate(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CustomVideoEncodingBitrate(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_CustomVideoEncodingHeight(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CustomVideoEncodingHeight(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_CustomVideoEncodingWidth(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CustomVideoEncodingWidth(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_HistoricalBufferLength(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HistoricalBufferLength(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_HistoricalBufferLengthUnit(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: win32more.Windows.Media.Capture.AppCaptureHistoricalBufferLengthUnit) -> Void: ...
    @winrt_mixinmethod
    def get_HistoricalBufferLengthUnit(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> win32more.Windows.Media.Capture.AppCaptureHistoricalBufferLengthUnit: ...
    @winrt_mixinmethod
    def put_IsHistoricalCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsHistoricalCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHistoricalCaptureOnBatteryAllowed(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsHistoricalCaptureOnBatteryAllowed(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHistoricalCaptureOnWirelessDisplayAllowed(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsHistoricalCaptureOnWirelessDisplayAllowed(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_MaximumRecordLength(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_MaximumRecordLength(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_ScreenshotDestinationFolder(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: win32more.Windows.Storage.StorageFolder) -> Void: ...
    @winrt_mixinmethod
    def get_ScreenshotDestinationFolder(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def put_VideoEncodingBitrateMode(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: win32more.Windows.Media.Capture.AppCaptureVideoEncodingBitrateMode) -> Void: ...
    @winrt_mixinmethod
    def get_VideoEncodingBitrateMode(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> win32more.Windows.Media.Capture.AppCaptureVideoEncodingBitrateMode: ...
    @winrt_mixinmethod
    def put_VideoEncodingResolutionMode(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: win32more.Windows.Media.Capture.AppCaptureVideoEncodingResolutionMode) -> Void: ...
    @winrt_mixinmethod
    def get_VideoEncodingResolutionMode(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> win32more.Windows.Media.Capture.AppCaptureVideoEncodingResolutionMode: ...
    @winrt_mixinmethod
    def put_IsAppCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAppCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCpuConstrained(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledByPolicy(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMemoryConstrained(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasHardwareEncoder(self: win32more.Windows.Media.Capture.IAppCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGpuConstrained(self: win32more.Windows.Media.Capture.IAppCaptureSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def get_AlternateShortcutKeys(self: win32more.Windows.Media.Capture.IAppCaptureSettings2) -> win32more.Windows.Media.Capture.AppCaptureAlternateShortcutKeys: ...
    @winrt_mixinmethod
    def put_IsMicrophoneCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsMicrophoneCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsMicrophoneCaptureEnabledByDefault(self: win32more.Windows.Media.Capture.IAppCaptureSettings4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsMicrophoneCaptureEnabledByDefault(self: win32more.Windows.Media.Capture.IAppCaptureSettings4) -> Boolean: ...
    @winrt_mixinmethod
    def put_SystemAudioGain(self: win32more.Windows.Media.Capture.IAppCaptureSettings4, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SystemAudioGain(self: win32more.Windows.Media.Capture.IAppCaptureSettings4) -> Double: ...
    @winrt_mixinmethod
    def put_MicrophoneGain(self: win32more.Windows.Media.Capture.IAppCaptureSettings4, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MicrophoneGain(self: win32more.Windows.Media.Capture.IAppCaptureSettings4) -> Double: ...
    @winrt_mixinmethod
    def put_VideoEncodingFrameRateMode(self: win32more.Windows.Media.Capture.IAppCaptureSettings4, value: win32more.Windows.Media.Capture.AppCaptureVideoEncodingFrameRateMode) -> Void: ...
    @winrt_mixinmethod
    def get_VideoEncodingFrameRateMode(self: win32more.Windows.Media.Capture.IAppCaptureSettings4) -> win32more.Windows.Media.Capture.AppCaptureVideoEncodingFrameRateMode: ...
    @winrt_mixinmethod
    def put_IsEchoCancellationEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings5, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsEchoCancellationEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings5) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCursorImageCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings5, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCursorImageCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureSettings5) -> Boolean: ...
    AlternateShortcutKeys = property(get_AlternateShortcutKeys, None)
    AppCaptureDestinationFolder = property(get_AppCaptureDestinationFolder, put_AppCaptureDestinationFolder)
    AudioEncodingBitrate = property(get_AudioEncodingBitrate, put_AudioEncodingBitrate)
    CustomVideoEncodingBitrate = property(get_CustomVideoEncodingBitrate, put_CustomVideoEncodingBitrate)
    CustomVideoEncodingHeight = property(get_CustomVideoEncodingHeight, put_CustomVideoEncodingHeight)
    CustomVideoEncodingWidth = property(get_CustomVideoEncodingWidth, put_CustomVideoEncodingWidth)
    HasHardwareEncoder = property(get_HasHardwareEncoder, None)
    HistoricalBufferLength = property(get_HistoricalBufferLength, put_HistoricalBufferLength)
    HistoricalBufferLengthUnit = property(get_HistoricalBufferLengthUnit, put_HistoricalBufferLengthUnit)
    IsAppCaptureEnabled = property(get_IsAppCaptureEnabled, put_IsAppCaptureEnabled)
    IsAudioCaptureEnabled = property(get_IsAudioCaptureEnabled, put_IsAudioCaptureEnabled)
    IsCpuConstrained = property(get_IsCpuConstrained, None)
    IsCursorImageCaptureEnabled = property(get_IsCursorImageCaptureEnabled, put_IsCursorImageCaptureEnabled)
    IsDisabledByPolicy = property(get_IsDisabledByPolicy, None)
    IsEchoCancellationEnabled = property(get_IsEchoCancellationEnabled, put_IsEchoCancellationEnabled)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsHistoricalCaptureEnabled = property(get_IsHistoricalCaptureEnabled, put_IsHistoricalCaptureEnabled)
    IsHistoricalCaptureOnBatteryAllowed = property(get_IsHistoricalCaptureOnBatteryAllowed, put_IsHistoricalCaptureOnBatteryAllowed)
    IsHistoricalCaptureOnWirelessDisplayAllowed = property(get_IsHistoricalCaptureOnWirelessDisplayAllowed, put_IsHistoricalCaptureOnWirelessDisplayAllowed)
    IsMemoryConstrained = property(get_IsMemoryConstrained, None)
    IsMicrophoneCaptureEnabled = property(get_IsMicrophoneCaptureEnabled, put_IsMicrophoneCaptureEnabled)
    IsMicrophoneCaptureEnabledByDefault = property(get_IsMicrophoneCaptureEnabledByDefault, put_IsMicrophoneCaptureEnabledByDefault)
    MaximumRecordLength = property(get_MaximumRecordLength, put_MaximumRecordLength)
    MicrophoneGain = property(get_MicrophoneGain, put_MicrophoneGain)
    ScreenshotDestinationFolder = property(get_ScreenshotDestinationFolder, put_ScreenshotDestinationFolder)
    SystemAudioGain = property(get_SystemAudioGain, put_SystemAudioGain)
    VideoEncodingBitrateMode = property(get_VideoEncodingBitrateMode, put_VideoEncodingBitrateMode)
    VideoEncodingFrameRateMode = property(get_VideoEncodingFrameRateMode, put_VideoEncodingFrameRateMode)
    VideoEncodingResolutionMode = property(get_VideoEncodingResolutionMode, put_VideoEncodingResolutionMode)
class AppCaptureState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IAppCaptureState
    _classid_ = 'Windows.Media.Capture.AppCaptureState'
    @winrt_mixinmethod
    def get_IsTargetRunning(self: win32more.Windows.Media.Capture.IAppCaptureState) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHistoricalCaptureEnabled(self: win32more.Windows.Media.Capture.IAppCaptureState) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldCaptureMicrophone(self: win32more.Windows.Media.Capture.IAppCaptureState) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldCaptureMicrophone(self: win32more.Windows.Media.Capture.IAppCaptureState, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RestartMicrophoneCapture(self: win32more.Windows.Media.Capture.IAppCaptureState) -> Void: ...
    @winrt_mixinmethod
    def get_MicrophoneCaptureState(self: win32more.Windows.Media.Capture.IAppCaptureState) -> win32more.Windows.Media.Capture.AppCaptureMicrophoneCaptureState: ...
    @winrt_mixinmethod
    def get_MicrophoneCaptureError(self: win32more.Windows.Media.Capture.IAppCaptureState) -> UInt32: ...
    @winrt_mixinmethod
    def add_MicrophoneCaptureStateChanged(self: win32more.Windows.Media.Capture.IAppCaptureState, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureState, win32more.Windows.Media.Capture.AppCaptureMicrophoneCaptureStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MicrophoneCaptureStateChanged(self: win32more.Windows.Media.Capture.IAppCaptureState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CaptureTargetClosed(self: win32more.Windows.Media.Capture.IAppCaptureState, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureState, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CaptureTargetClosed(self: win32more.Windows.Media.Capture.IAppCaptureState, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsHistoricalCaptureEnabled = property(get_IsHistoricalCaptureEnabled, None)
    IsTargetRunning = property(get_IsTargetRunning, None)
    MicrophoneCaptureError = property(get_MicrophoneCaptureError, None)
    MicrophoneCaptureState = property(get_MicrophoneCaptureState, None)
    ShouldCaptureMicrophone = property(get_ShouldCaptureMicrophone, put_ShouldCaptureMicrophone)
    MicrophoneCaptureStateChanged = event()
    CaptureTargetClosed = event()
class AppCaptureVideoEncodingBitrateMode(Enum, Int32):
    Custom = 0
    High = 1
    Standard = 2
class AppCaptureVideoEncodingFrameRateMode(Enum, Int32):
    Standard = 0
    High = 1
class AppCaptureVideoEncodingResolutionMode(Enum, Int32):
    Custom = 0
    High = 1
    Standard = 2
class CameraCaptureUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ICameraCaptureUI
    _classid_ = 'Windows.Media.Capture.CameraCaptureUI'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Capture.CameraCaptureUI.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Capture.CameraCaptureUI: ...
    @winrt_mixinmethod
    def get_PhotoSettings(self: win32more.Windows.Media.Capture.ICameraCaptureUI) -> win32more.Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings: ...
    @winrt_mixinmethod
    def get_VideoSettings(self: win32more.Windows.Media.Capture.ICameraCaptureUI) -> win32more.Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings: ...
    @winrt_mixinmethod
    def CaptureFileAsync(self: win32more.Windows.Media.Capture.ICameraCaptureUI, mode: win32more.Windows.Media.Capture.CameraCaptureUIMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    PhotoSettings = property(get_PhotoSettings, None)
    VideoSettings = property(get_VideoSettings, None)
CameraCaptureUIContract: UInt32 = 65536
class CameraCaptureUIMaxPhotoResolution(Enum, Int32):
    HighestAvailable = 0
    VerySmallQvga = 1
    SmallVga = 2
    MediumXga = 3
    Large3M = 4
    VeryLarge5M = 5
class CameraCaptureUIMaxVideoResolution(Enum, Int32):
    HighestAvailable = 0
    LowDefinition = 1
    StandardDefinition = 2
    HighDefinition = 3
class CameraCaptureUIMode(Enum, Int32):
    PhotoOrVideo = 0
    Photo = 1
    Video = 2
class CameraCaptureUIPhotoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings
    _classid_ = 'Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings'
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Windows.Media.Capture.CameraCaptureUIPhotoFormat: ...
    @winrt_mixinmethod
    def put_Format(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Windows.Media.Capture.CameraCaptureUIPhotoFormat) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution: ...
    @winrt_mixinmethod
    def put_MaxResolution(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution) -> Void: ...
    @winrt_mixinmethod
    def get_CroppedSizeInPixels(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CroppedSizeInPixels(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_CroppedAspectRatio(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CroppedAspectRatio(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_AllowCropping(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCropping(self: win32more.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: Boolean) -> Void: ...
    AllowCropping = property(get_AllowCropping, put_AllowCropping)
    CroppedAspectRatio = property(get_CroppedAspectRatio, put_CroppedAspectRatio)
    CroppedSizeInPixels = property(get_CroppedSizeInPixels, put_CroppedSizeInPixels)
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
class CameraCaptureUIPhotoFormat(Enum, Int32):
    Jpeg = 0
    Png = 1
    JpegXR = 2
class CameraCaptureUIVideoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings
    _classid_ = 'Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings'
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> win32more.Windows.Media.Capture.CameraCaptureUIVideoFormat: ...
    @winrt_mixinmethod
    def put_Format(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: win32more.Windows.Media.Capture.CameraCaptureUIVideoFormat) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> win32more.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution: ...
    @winrt_mixinmethod
    def put_MaxResolution(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: win32more.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution) -> Void: ...
    @winrt_mixinmethod
    def get_MaxDurationInSeconds(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Single: ...
    @winrt_mixinmethod
    def put_MaxDurationInSeconds(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AllowTrimming(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowTrimming(self: win32more.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Boolean) -> Void: ...
    AllowTrimming = property(get_AllowTrimming, put_AllowTrimming)
    Format = property(get_Format, put_Format)
    MaxDurationInSeconds = property(get_MaxDurationInSeconds, put_MaxDurationInSeconds)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
class CameraCaptureUIVideoFormat(Enum, Int32):
    Mp4 = 0
    Wmv = 1
class CameraOptionsUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.CameraOptionsUI'
    @winrt_classmethod
    def Show(cls: win32more.Windows.Media.Capture.ICameraOptionsUIStatics, mediaCapture: win32more.Windows.Media.Capture.MediaCapture) -> Void: ...
class CapturedFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Capture.ICapturedFrame
    _classid_ = 'Windows.Media.Capture.CapturedFrame'
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Media.Capture.ICapturedFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Media.Capture.ICapturedFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: win32more.Windows.Storage.Streams.IInputStream, buffer: win32more.Windows.Storage.Streams.IBuffer, count: UInt32, options: win32more.Windows.Storage.Streams.InputStreamOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: win32more.Windows.Storage.Streams.IOutputStream, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SoftwareBitmap(self: win32more.Windows.Media.Capture.ICapturedFrameWithSoftwareBitmap) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def get_ControlValues(self: win32more.Windows.Media.Capture.ICapturedFrame2) -> win32more.Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: win32more.Windows.Media.Capture.ICapturedFrame2) -> win32more.Windows.Graphics.Imaging.BitmapPropertySet: ...
    BitmapProperties = property(get_BitmapProperties, None)
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
    ControlValues = property(get_ControlValues, None)
    Height = property(get_Height, None)
    Position = property(get_Position, None)
    Size = property(get_Size, put_Size)
    SoftwareBitmap = property(get_SoftwareBitmap, None)
    Width = property(get_Width, None)
class CapturedFrameControlValues(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ICapturedFrameControlValues
    _classid_ = 'Windows.Media.Capture.CapturedFrameControlValues'
    @winrt_mixinmethod
    def get_Exposure(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ExposureCompensation(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_IsoSpeed(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_Focus(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_SceneMode(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_mixinmethod
    def get_Flashed(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def get_FlashPowerPercent(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_WhiteBalance(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_ZoomFactor(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_FocusState(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.MediaCaptureFocusState]: ...
    @winrt_mixinmethod
    def get_IsoDigitalGain(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues2) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_IsoAnalogGain(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues2) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SensorFrameRate(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues2) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_WhiteBalanceGain(self: win32more.Windows.Media.Capture.ICapturedFrameControlValues2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Capture.WhiteBalanceGain]: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    FlashPowerPercent = property(get_FlashPowerPercent, None)
    Flashed = property(get_Flashed, None)
    Focus = property(get_Focus, None)
    FocusState = property(get_FocusState, None)
    IsoAnalogGain = property(get_IsoAnalogGain, None)
    IsoDigitalGain = property(get_IsoDigitalGain, None)
    IsoSpeed = property(get_IsoSpeed, None)
    SceneMode = property(get_SceneMode, None)
    SensorFrameRate = property(get_SensorFrameRate, None)
    WhiteBalance = property(get_WhiteBalance, None)
    WhiteBalanceGain = property(get_WhiteBalanceGain, None)
    ZoomFactor = property(get_ZoomFactor, None)
class CapturedPhoto(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ICapturedPhoto
    _classid_ = 'Windows.Media.Capture.CapturedPhoto'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Capture.ICapturedPhoto) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Capture.ICapturedPhoto) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
class ForegroundActivationArgument(Enum, Int32):
    SignInRequired = 0
    MoreSettings = 1
class GameBarCommand(Enum, Int32):
    OpenGameBar = 0
    RecordHistoricalBuffer = 1
    ToggleStartStopRecord = 2
    StartRecord = 3
    StopRecord = 4
    TakeScreenshot = 5
    StartBroadcast = 6
    StopBroadcast = 7
    PauseBroadcast = 8
    ResumeBroadcast = 9
    ToggleStartStopBroadcast = 10
    ToggleMicrophoneCapture = 11
    ToggleCameraCapture = 12
    ToggleRecordingIndicator = 13
class GameBarCommandOrigin(Enum, Int32):
    ShortcutKey = 0
    Cortana = 1
    AppCommand = 2
GameBarContract: UInt32 = 65536
class GameBarServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IGameBarServices
    _classid_ = 'Windows.Media.Capture.GameBarServices'
    @winrt_mixinmethod
    def get_TargetCapturePolicy(self: win32more.Windows.Media.Capture.IGameBarServices) -> win32more.Windows.Media.Capture.GameBarTargetCapturePolicy: ...
    @winrt_mixinmethod
    def EnableCapture(self: win32more.Windows.Media.Capture.IGameBarServices) -> Void: ...
    @winrt_mixinmethod
    def DisableCapture(self: win32more.Windows.Media.Capture.IGameBarServices) -> Void: ...
    @winrt_mixinmethod
    def get_TargetInfo(self: win32more.Windows.Media.Capture.IGameBarServices) -> win32more.Windows.Media.Capture.GameBarServicesTargetInfo: ...
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Media.Capture.IGameBarServices) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppBroadcastServices(self: win32more.Windows.Media.Capture.IGameBarServices) -> win32more.Windows.Media.Capture.AppBroadcastServices: ...
    @winrt_mixinmethod
    def get_AppCaptureServices(self: win32more.Windows.Media.Capture.IGameBarServices) -> win32more.Windows.Media.Capture.AppCaptureServices: ...
    @winrt_mixinmethod
    def add_CommandReceived(self: win32more.Windows.Media.Capture.IGameBarServices, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.GameBarServices, win32more.Windows.Media.Capture.GameBarServicesCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommandReceived(self: win32more.Windows.Media.Capture.IGameBarServices, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AppBroadcastServices = property(get_AppBroadcastServices, None)
    AppCaptureServices = property(get_AppCaptureServices, None)
    SessionId = property(get_SessionId, None)
    TargetCapturePolicy = property(get_TargetCapturePolicy, None)
    TargetInfo = property(get_TargetInfo, None)
    CommandReceived = event()
class GameBarServicesCommandEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IGameBarServicesCommandEventArgs
    _classid_ = 'Windows.Media.Capture.GameBarServicesCommandEventArgs'
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.Media.Capture.IGameBarServicesCommandEventArgs) -> win32more.Windows.Media.Capture.GameBarCommand: ...
    @winrt_mixinmethod
    def get_Origin(self: win32more.Windows.Media.Capture.IGameBarServicesCommandEventArgs) -> win32more.Windows.Media.Capture.GameBarCommandOrigin: ...
    Command = property(get_Command, None)
    Origin = property(get_Origin, None)
class GameBarServicesDisplayMode(Enum, Int32):
    Windowed = 0
    FullScreenExclusive = 1
class GameBarServicesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IGameBarServicesManager
    _classid_ = 'Windows.Media.Capture.GameBarServicesManager'
    @winrt_mixinmethod
    def add_GameBarServicesCreated(self: win32more.Windows.Media.Capture.IGameBarServicesManager, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.GameBarServicesManager, win32more.Windows.Media.Capture.GameBarServicesManagerGameBarServicesCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GameBarServicesCreated(self: win32more.Windows.Media.Capture.IGameBarServicesManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Media.Capture.IGameBarServicesManagerStatics) -> win32more.Windows.Media.Capture.GameBarServicesManager: ...
    GameBarServicesCreated = event()
class GameBarServicesManagerGameBarServicesCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IGameBarServicesManagerGameBarServicesCreatedEventArgs
    _classid_ = 'Windows.Media.Capture.GameBarServicesManagerGameBarServicesCreatedEventArgs'
    @winrt_mixinmethod
    def get_GameBarServices(self: win32more.Windows.Media.Capture.IGameBarServicesManagerGameBarServicesCreatedEventArgs) -> win32more.Windows.Media.Capture.GameBarServices: ...
    GameBarServices = property(get_GameBarServices, None)
class GameBarServicesTargetInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IGameBarServicesTargetInfo
    _classid_ = 'Windows.Media.Capture.GameBarServicesTargetInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.Capture.IGameBarServicesTargetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Media.Capture.IGameBarServicesTargetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TitleId(self: win32more.Windows.Media.Capture.IGameBarServicesTargetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayMode(self: win32more.Windows.Media.Capture.IGameBarServicesTargetInfo) -> win32more.Windows.Media.Capture.GameBarServicesDisplayMode: ...
    AppId = property(get_AppId, None)
    DisplayMode = property(get_DisplayMode, None)
    DisplayName = property(get_DisplayName, None)
    TitleId = property(get_TitleId, None)
class GameBarTargetCapturePolicy(Enum, Int32):
    EnabledBySystem = 0
    EnabledByUser = 1
    NotEnabled = 2
    ProhibitedBySystem = 3
    ProhibitedByPublisher = 4
class IAdvancedCapturedPhoto(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAdvancedCapturedPhoto'
    _iid_ = Guid('{f072728b-b292-4491-9d41-99807a550bbf}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Mode(self) -> win32more.Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_commethod(8)
    def get_Context(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Context = property(get_Context, None)
    Frame = property(get_Frame, None)
    Mode = property(get_Mode, None)
class IAdvancedCapturedPhoto2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAdvancedCapturedPhoto2'
    _iid_ = Guid('{18cf6cd8-cffe-42d8-8104-017bb318f4a1}')
    @winrt_commethod(6)
    def get_FrameBoundsRelativeToReferencePhoto(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    FrameBoundsRelativeToReferencePhoto = property(get_FrameBoundsRelativeToReferencePhoto, None)
class IAdvancedPhotoCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAdvancedPhotoCapture'
    _iid_ = Guid('{83ffaafa-6667-44dc-973c-a6bce596aa0f}')
    @winrt_commethod(6)
    def CaptureAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_commethod(7)
    def CaptureWithContextAsync(self, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_commethod(8)
    def add_OptionalReferencePhotoCaptured(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AdvancedPhotoCapture, win32more.Windows.Media.Capture.OptionalReferencePhotoCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_OptionalReferencePhotoCaptured(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_AllPhotosCaptured(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AdvancedPhotoCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AllPhotosCaptured(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def FinishAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    OptionalReferencePhotoCaptured = event()
    AllPhotosCaptured = event()
class IAppBroadcastBackgroundService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastBackgroundService'
    _iid_ = Guid('{bad1e72a-fa94-46f9-95fc-d71511cda70b}')
    @winrt_commethod(6)
    def put_PlugInState(self, value: win32more.Windows.Media.Capture.AppBroadcastPlugInState) -> Void: ...
    @winrt_commethod(7)
    def get_PlugInState(self) -> win32more.Windows.Media.Capture.AppBroadcastPlugInState: ...
    @winrt_commethod(8)
    def put_SignInInfo(self, value: win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo) -> Void: ...
    @winrt_commethod(9)
    def get_SignInInfo(self) -> win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo: ...
    @winrt_commethod(10)
    def put_StreamInfo(self, value: win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo) -> Void: ...
    @winrt_commethod(11)
    def get_StreamInfo(self) -> win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo: ...
    @winrt_commethod(12)
    def get_AppId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_BroadcastTitle(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_ViewerCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(15)
    def get_ViewerCount(self) -> UInt32: ...
    @winrt_commethod(16)
    def TerminateBroadcast(self, reason: win32more.Windows.Media.Capture.AppBroadcastTerminationReason, providerSpecificReason: UInt32) -> Void: ...
    @winrt_commethod(17)
    def add_HeartbeatRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Media.Capture.AppBroadcastHeartbeatRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_HeartbeatRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def get_TitleId(self) -> WinRT_String: ...
    AppId = property(get_AppId, None)
    BroadcastTitle = property(get_BroadcastTitle, None)
    PlugInState = property(get_PlugInState, put_PlugInState)
    SignInInfo = property(get_SignInInfo, put_SignInInfo)
    StreamInfo = property(get_StreamInfo, put_StreamInfo)
    TitleId = property(get_TitleId, None)
    ViewerCount = property(get_ViewerCount, put_ViewerCount)
    HeartbeatRequested = event()
class IAppBroadcastBackgroundService2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastBackgroundService2'
    _iid_ = Guid('{fc8ccbbf-5549-4b87-959f-23ca401fd473}')
    @winrt_commethod(6)
    def put_BroadcastTitle(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_BroadcastLanguage(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_BroadcastLanguage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_BroadcastChannel(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_BroadcastChannel(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def add_BroadcastTitleChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_BroadcastTitleChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_BroadcastLanguageChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_BroadcastLanguageChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_BroadcastChannelChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundService, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_BroadcastChannelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BroadcastChannel = property(get_BroadcastChannel, put_BroadcastChannel)
    BroadcastLanguage = property(get_BroadcastLanguage, put_BroadcastLanguage)
    BroadcastTitle = property(None, put_BroadcastTitle)
    BroadcastTitleChanged = event()
    BroadcastLanguageChanged = event()
    BroadcastChannelChanged = event()
class IAppBroadcastBackgroundServiceSignInInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo'
    _iid_ = Guid('{5e735275-88c8-4eca-89ba-4825985db880}')
    @winrt_commethod(6)
    def get_SignInState(self) -> win32more.Windows.Media.Capture.AppBroadcastSignInState: ...
    @winrt_commethod(7)
    def put_OAuthRequestUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_OAuthRequestUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_OAuthCallbackUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(10)
    def get_OAuthCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def get_AuthenticationResult(self) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_commethod(12)
    def put_UserName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_UserName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def add_SignInStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo, win32more.Windows.Media.Capture.AppBroadcastSignInStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SignInStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AuthenticationResult = property(get_AuthenticationResult, None)
    OAuthCallbackUri = property(get_OAuthCallbackUri, put_OAuthCallbackUri)
    OAuthRequestUri = property(get_OAuthRequestUri, put_OAuthRequestUri)
    SignInState = property(get_SignInState, None)
    UserName = property(get_UserName, put_UserName)
    SignInStateChanged = event()
class IAppBroadcastBackgroundServiceSignInInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastBackgroundServiceSignInInfo2'
    _iid_ = Guid('{9104285c-62cf-4a3c-a7ee-aeb507404645}')
    @winrt_commethod(6)
    def add_UserNameChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceSignInInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UserNameChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    UserNameChanged = event()
class IAppBroadcastBackgroundServiceStreamInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo'
    _iid_ = Guid('{31dc02bc-990a-4904-aa96-fe364381f136}')
    @winrt_commethod(6)
    def get_StreamState(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamState: ...
    @winrt_commethod(7)
    def put_DesiredVideoEncodingBitrate(self, value: UInt64) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredVideoEncodingBitrate(self) -> UInt64: ...
    @winrt_commethod(9)
    def put_BandwidthTestBitrate(self, value: UInt64) -> Void: ...
    @winrt_commethod(10)
    def get_BandwidthTestBitrate(self) -> UInt64: ...
    @winrt_commethod(11)
    def put_AudioCodec(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_AudioCodec(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_BroadcastStreamReader(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamReader: ...
    @winrt_commethod(14)
    def add_StreamStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo, win32more.Windows.Media.Capture.AppBroadcastStreamStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_StreamStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_VideoEncodingResolutionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_VideoEncodingResolutionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_VideoEncodingBitrateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastBackgroundServiceStreamInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_VideoEncodingBitrateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AudioCodec = property(get_AudioCodec, put_AudioCodec)
    BandwidthTestBitrate = property(get_BandwidthTestBitrate, put_BandwidthTestBitrate)
    BroadcastStreamReader = property(get_BroadcastStreamReader, None)
    DesiredVideoEncodingBitrate = property(get_DesiredVideoEncodingBitrate, put_DesiredVideoEncodingBitrate)
    StreamState = property(get_StreamState, None)
    StreamStateChanged = event()
    VideoEncodingResolutionChanged = event()
    VideoEncodingBitrateChanged = event()
class IAppBroadcastBackgroundServiceStreamInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastBackgroundServiceStreamInfo2'
    _iid_ = Guid('{bd1e9f6d-94dc-4fce-9541-a9f129596334}')
    @winrt_commethod(6)
    def ReportProblemWithStream(self) -> Void: ...
class IAppBroadcastCameraCaptureStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastCameraCaptureStateChangedEventArgs'
    _iid_ = Guid('{1e334cd0-b882-4b88-8692-05999aceb70f}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.Capture.AppBroadcastCameraCaptureState: ...
    @winrt_commethod(7)
    def get_ErrorCode(self) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class IAppBroadcastGlobalSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastGlobalSettings'
    _iid_ = Guid('{b2cb27a5-70fc-4e17-80bd-6ba0fd3ff3a0}')
    @winrt_commethod(6)
    def get_IsBroadcastEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsDisabledByPolicy(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGpuConstrained(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_HasHardwareEncoder(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsAudioCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsAudioCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_IsMicrophoneCaptureEnabledByDefault(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_IsMicrophoneCaptureEnabledByDefault(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_IsEchoCancellationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_IsEchoCancellationEnabled(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_SystemAudioGain(self, value: Double) -> Void: ...
    @winrt_commethod(17)
    def get_SystemAudioGain(self) -> Double: ...
    @winrt_commethod(18)
    def put_MicrophoneGain(self, value: Double) -> Void: ...
    @winrt_commethod(19)
    def get_MicrophoneGain(self) -> Double: ...
    @winrt_commethod(20)
    def put_IsCameraCaptureEnabledByDefault(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_IsCameraCaptureEnabledByDefault(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_SelectedCameraId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(23)
    def get_SelectedCameraId(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def put_CameraOverlayLocation(self, value: win32more.Windows.Media.Capture.AppBroadcastCameraOverlayLocation) -> Void: ...
    @winrt_commethod(25)
    def get_CameraOverlayLocation(self) -> win32more.Windows.Media.Capture.AppBroadcastCameraOverlayLocation: ...
    @winrt_commethod(26)
    def put_CameraOverlaySize(self, value: win32more.Windows.Media.Capture.AppBroadcastCameraOverlaySize) -> Void: ...
    @winrt_commethod(27)
    def get_CameraOverlaySize(self) -> win32more.Windows.Media.Capture.AppBroadcastCameraOverlaySize: ...
    @winrt_commethod(28)
    def put_IsCursorImageCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(29)
    def get_IsCursorImageCaptureEnabled(self) -> Boolean: ...
    CameraOverlayLocation = property(get_CameraOverlayLocation, put_CameraOverlayLocation)
    CameraOverlaySize = property(get_CameraOverlaySize, put_CameraOverlaySize)
    HasHardwareEncoder = property(get_HasHardwareEncoder, None)
    IsAudioCaptureEnabled = property(get_IsAudioCaptureEnabled, put_IsAudioCaptureEnabled)
    IsBroadcastEnabled = property(get_IsBroadcastEnabled, None)
    IsCameraCaptureEnabledByDefault = property(get_IsCameraCaptureEnabledByDefault, put_IsCameraCaptureEnabledByDefault)
    IsCursorImageCaptureEnabled = property(get_IsCursorImageCaptureEnabled, put_IsCursorImageCaptureEnabled)
    IsDisabledByPolicy = property(get_IsDisabledByPolicy, None)
    IsEchoCancellationEnabled = property(get_IsEchoCancellationEnabled, put_IsEchoCancellationEnabled)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsMicrophoneCaptureEnabledByDefault = property(get_IsMicrophoneCaptureEnabledByDefault, put_IsMicrophoneCaptureEnabledByDefault)
    MicrophoneGain = property(get_MicrophoneGain, put_MicrophoneGain)
    SelectedCameraId = property(get_SelectedCameraId, put_SelectedCameraId)
    SystemAudioGain = property(get_SystemAudioGain, put_SystemAudioGain)
class IAppBroadcastHeartbeatRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastHeartbeatRequestedEventArgs'
    _iid_ = Guid('{cea54283-ee51-4dbf-9472-79a9ed4e2165}')
    @winrt_commethod(6)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class IAppBroadcastManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastManagerStatics'
    _iid_ = Guid('{364e018b-1e4e-411f-ab3e-92959844c156}')
    @winrt_commethod(6)
    def GetGlobalSettings(self) -> win32more.Windows.Media.Capture.AppBroadcastGlobalSettings: ...
    @winrt_commethod(7)
    def ApplyGlobalSettings(self, value: win32more.Windows.Media.Capture.AppBroadcastGlobalSettings) -> Void: ...
    @winrt_commethod(8)
    def GetProviderSettings(self) -> win32more.Windows.Media.Capture.AppBroadcastProviderSettings: ...
    @winrt_commethod(9)
    def ApplyProviderSettings(self, value: win32more.Windows.Media.Capture.AppBroadcastProviderSettings) -> Void: ...
class IAppBroadcastMicrophoneCaptureStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastMicrophoneCaptureStateChangedEventArgs'
    _iid_ = Guid('{a86ad5e9-9440-4908-9d09-65b7e315d795}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.Capture.AppBroadcastMicrophoneCaptureState: ...
    @winrt_commethod(7)
    def get_ErrorCode(self) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class IAppBroadcastPlugIn(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPlugIn'
    _iid_ = Guid('{520c1e66-6513-4574-ac54-23b79729615b}')
    @winrt_commethod(6)
    def get_AppId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProviderSettings(self) -> win32more.Windows.Media.Capture.AppBroadcastProviderSettings: ...
    @winrt_commethod(8)
    def get_Logo(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    AppId = property(get_AppId, None)
    DisplayName = property(get_DisplayName, None)
    Logo = property(get_Logo, None)
    ProviderSettings = property(get_ProviderSettings, None)
class IAppBroadcastPlugInManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPlugInManager'
    _iid_ = Guid('{e550d979-27a1-49a7-bbf4-d7a9e9d07668}')
    @winrt_commethod(6)
    def get_IsBroadcastProviderAvailable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_PlugInList(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.AppBroadcastPlugIn]: ...
    @winrt_commethod(8)
    def get_DefaultPlugIn(self) -> win32more.Windows.Media.Capture.AppBroadcastPlugIn: ...
    @winrt_commethod(9)
    def put_DefaultPlugIn(self, value: win32more.Windows.Media.Capture.AppBroadcastPlugIn) -> Void: ...
    DefaultPlugIn = property(get_DefaultPlugIn, put_DefaultPlugIn)
    IsBroadcastProviderAvailable = property(get_IsBroadcastProviderAvailable, None)
    PlugInList = property(get_PlugInList, None)
class IAppBroadcastPlugInManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPlugInManagerStatics'
    _iid_ = Guid('{f2645c20-5c76-4cdc-9364-82fe9eb6534d}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Media.Capture.AppBroadcastPlugInManager: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Media.Capture.AppBroadcastPlugInManager: ...
class IAppBroadcastPlugInStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPlugInStateChangedEventArgs'
    _iid_ = Guid('{4881d0f2-abc5-4fc6-84b0-89370bb47212}')
    @winrt_commethod(6)
    def get_PlugInState(self) -> win32more.Windows.Media.Capture.AppBroadcastPlugInState: ...
    PlugInState = property(get_PlugInState, None)
class IAppBroadcastPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPreview'
    _iid_ = Guid('{14b60f5a-6e4a-4b80-a14f-67ee77d153e7}')
    @winrt_commethod(6)
    def StopPreview(self) -> Void: ...
    @winrt_commethod(7)
    def get_PreviewState(self) -> win32more.Windows.Media.Capture.AppBroadcastPreviewState: ...
    @winrt_commethod(8)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def add_PreviewStateChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastPreview, win32more.Windows.Media.Capture.AppBroadcastPreviewStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PreviewStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_PreviewStreamReader(self) -> win32more.Windows.Media.Capture.AppBroadcastPreviewStreamReader: ...
    ErrorCode = property(get_ErrorCode, None)
    PreviewState = property(get_PreviewState, None)
    PreviewStreamReader = property(get_PreviewStreamReader, None)
    PreviewStateChanged = event()
class IAppBroadcastPreviewStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPreviewStateChangedEventArgs'
    _iid_ = Guid('{5a57f2de-8dea-4e86-90ad-03fc26b9653c}')
    @winrt_commethod(6)
    def get_PreviewState(self) -> win32more.Windows.Media.Capture.AppBroadcastPreviewState: ...
    @winrt_commethod(7)
    def get_ErrorCode(self) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    PreviewState = property(get_PreviewState, None)
class IAppBroadcastPreviewStreamReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPreviewStreamReader'
    _iid_ = Guid('{92228d50-db3f-40a8-8cd4-f4e371ddab37}')
    @winrt_commethod(6)
    def get_VideoWidth(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_VideoHeight(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_VideoStride(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_VideoBitmapPixelFormat(self) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(10)
    def get_VideoBitmapAlphaMode(self) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_commethod(11)
    def TryGetNextVideoFrame(self) -> win32more.Windows.Media.Capture.AppBroadcastPreviewStreamVideoFrame: ...
    @winrt_commethod(12)
    def add_VideoFrameArrived(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastPreviewStreamReader, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_VideoFrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    VideoBitmapAlphaMode = property(get_VideoBitmapAlphaMode, None)
    VideoBitmapPixelFormat = property(get_VideoBitmapPixelFormat, None)
    VideoHeight = property(get_VideoHeight, None)
    VideoStride = property(get_VideoStride, None)
    VideoWidth = property(get_VideoWidth, None)
    VideoFrameArrived = event()
class IAppBroadcastPreviewStreamVideoFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPreviewStreamVideoFrame'
    _iid_ = Guid('{010fbea1-94fe-4499-b8c0-8d244279fb12}')
    @winrt_commethod(6)
    def get_VideoHeader(self) -> win32more.Windows.Media.Capture.AppBroadcastPreviewStreamVideoHeader: ...
    @winrt_commethod(7)
    def get_VideoBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    VideoBuffer = property(get_VideoBuffer, None)
    VideoHeader = property(get_VideoHeader, None)
class IAppBroadcastPreviewStreamVideoHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastPreviewStreamVideoHeader'
    _iid_ = Guid('{8bef6113-da84-4499-a7ab-87118cb4a157}')
    @winrt_commethod(6)
    def get_AbsoluteTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_RelativeTimestamp(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_FrameId(self) -> UInt64: ...
    AbsoluteTimestamp = property(get_AbsoluteTimestamp, None)
    Duration = property(get_Duration, None)
    FrameId = property(get_FrameId, None)
    RelativeTimestamp = property(get_RelativeTimestamp, None)
class IAppBroadcastProviderSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastProviderSettings'
    _iid_ = Guid('{c30bdf62-9948-458f-ad50-aa06ec03da08}')
    @winrt_commethod(6)
    def put_DefaultBroadcastTitle(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DefaultBroadcastTitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_AudioEncodingBitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_AudioEncodingBitrate(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_CustomVideoEncodingBitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_CustomVideoEncodingBitrate(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_CustomVideoEncodingHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_CustomVideoEncodingHeight(self) -> UInt32: ...
    @winrt_commethod(14)
    def put_CustomVideoEncodingWidth(self, value: UInt32) -> Void: ...
    @winrt_commethod(15)
    def get_CustomVideoEncodingWidth(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_VideoEncodingBitrateMode(self, value: win32more.Windows.Media.Capture.AppBroadcastVideoEncodingBitrateMode) -> Void: ...
    @winrt_commethod(17)
    def get_VideoEncodingBitrateMode(self) -> win32more.Windows.Media.Capture.AppBroadcastVideoEncodingBitrateMode: ...
    @winrt_commethod(18)
    def put_VideoEncodingResolutionMode(self, value: win32more.Windows.Media.Capture.AppBroadcastVideoEncodingResolutionMode) -> Void: ...
    @winrt_commethod(19)
    def get_VideoEncodingResolutionMode(self) -> win32more.Windows.Media.Capture.AppBroadcastVideoEncodingResolutionMode: ...
    AudioEncodingBitrate = property(get_AudioEncodingBitrate, put_AudioEncodingBitrate)
    CustomVideoEncodingBitrate = property(get_CustomVideoEncodingBitrate, put_CustomVideoEncodingBitrate)
    CustomVideoEncodingHeight = property(get_CustomVideoEncodingHeight, put_CustomVideoEncodingHeight)
    CustomVideoEncodingWidth = property(get_CustomVideoEncodingWidth, put_CustomVideoEncodingWidth)
    DefaultBroadcastTitle = property(get_DefaultBroadcastTitle, put_DefaultBroadcastTitle)
    VideoEncodingBitrateMode = property(get_VideoEncodingBitrateMode, put_VideoEncodingBitrateMode)
    VideoEncodingResolutionMode = property(get_VideoEncodingResolutionMode, put_VideoEncodingResolutionMode)
class IAppBroadcastServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastServices'
    _iid_ = Guid('{8660b4d6-969b-4e3c-ac3a-8b042ee4ee63}')
    @winrt_commethod(6)
    def get_CaptureTargetType(self) -> win32more.Windows.Media.Capture.AppBroadcastCaptureTargetType: ...
    @winrt_commethod(7)
    def put_CaptureTargetType(self, value: win32more.Windows.Media.Capture.AppBroadcastCaptureTargetType) -> Void: ...
    @winrt_commethod(8)
    def get_BroadcastTitle(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_BroadcastTitle(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_BroadcastLanguage(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_BroadcastLanguage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_UserName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_CanCapture(self) -> Boolean: ...
    @winrt_commethod(14)
    def EnterBroadcastModeAsync(self, plugIn: win32more.Windows.Media.Capture.AppBroadcastPlugIn) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(15)
    def ExitBroadcastMode(self, reason: win32more.Windows.Media.Capture.AppBroadcastExitBroadcastModeReason) -> Void: ...
    @winrt_commethod(16)
    def StartBroadcast(self) -> Void: ...
    @winrt_commethod(17)
    def PauseBroadcast(self) -> Void: ...
    @winrt_commethod(18)
    def ResumeBroadcast(self) -> Void: ...
    @winrt_commethod(19)
    def StartPreview(self, desiredSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Media.Capture.AppBroadcastPreview: ...
    @winrt_commethod(20)
    def get_State(self) -> win32more.Windows.Media.Capture.AppBroadcastState: ...
    BroadcastLanguage = property(get_BroadcastLanguage, put_BroadcastLanguage)
    BroadcastTitle = property(get_BroadcastTitle, put_BroadcastTitle)
    CanCapture = property(get_CanCapture, None)
    CaptureTargetType = property(get_CaptureTargetType, put_CaptureTargetType)
    State = property(get_State, None)
    UserName = property(get_UserName, None)
class IAppBroadcastSignInStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastSignInStateChangedEventArgs'
    _iid_ = Guid('{02b692a4-5919-4a9e-8d5e-c9bb0dd3377a}')
    @winrt_commethod(6)
    def get_SignInState(self) -> win32more.Windows.Media.Capture.AppBroadcastSignInState: ...
    @winrt_commethod(7)
    def get_Result(self) -> win32more.Windows.Media.Capture.AppBroadcastSignInResult: ...
    Result = property(get_Result, None)
    SignInState = property(get_SignInState, None)
class IAppBroadcastState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastState'
    _iid_ = Guid('{ee08056d-8099-4ddd-922e-c56dac58abfb}')
    @winrt_commethod(6)
    def get_IsCaptureTargetRunning(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ViewerCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ShouldCaptureMicrophone(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_ShouldCaptureMicrophone(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def RestartMicrophoneCapture(self) -> Void: ...
    @winrt_commethod(11)
    def get_ShouldCaptureCamera(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_ShouldCaptureCamera(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def RestartCameraCapture(self) -> Void: ...
    @winrt_commethod(14)
    def get_EncodedVideoSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(15)
    def get_MicrophoneCaptureState(self) -> win32more.Windows.Media.Capture.AppBroadcastMicrophoneCaptureState: ...
    @winrt_commethod(16)
    def get_MicrophoneCaptureError(self) -> UInt32: ...
    @winrt_commethod(17)
    def get_CameraCaptureState(self) -> win32more.Windows.Media.Capture.AppBroadcastCameraCaptureState: ...
    @winrt_commethod(18)
    def get_CameraCaptureError(self) -> UInt32: ...
    @winrt_commethod(19)
    def get_StreamState(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamState: ...
    @winrt_commethod(20)
    def get_PlugInState(self) -> win32more.Windows.Media.Capture.AppBroadcastPlugInState: ...
    @winrt_commethod(21)
    def get_OAuthRequestUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(22)
    def get_OAuthCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(23)
    def get_AuthenticationResult(self) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_commethod(24)
    def put_AuthenticationResult(self, value: win32more.Windows.Security.Authentication.Web.WebAuthenticationResult) -> Void: ...
    @winrt_commethod(25)
    def put_SignInState(self, value: win32more.Windows.Media.Capture.AppBroadcastSignInState) -> Void: ...
    @winrt_commethod(26)
    def get_SignInState(self) -> win32more.Windows.Media.Capture.AppBroadcastSignInState: ...
    @winrt_commethod(27)
    def get_TerminationReason(self) -> win32more.Windows.Media.Capture.AppBroadcastTerminationReason: ...
    @winrt_commethod(28)
    def get_TerminationReasonPlugInSpecific(self) -> UInt32: ...
    @winrt_commethod(29)
    def add_ViewerCountChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastViewerCountChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_ViewerCountChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_MicrophoneCaptureStateChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastMicrophoneCaptureStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_MicrophoneCaptureStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def add_CameraCaptureStateChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastCameraCaptureStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(34)
    def remove_CameraCaptureStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(35)
    def add_PlugInStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastPlugInStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(36)
    def remove_PlugInStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(37)
    def add_StreamStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Media.Capture.AppBroadcastStreamStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_StreamStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(39)
    def add_CaptureTargetClosed(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastState, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(40)
    def remove_CaptureTargetClosed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AuthenticationResult = property(get_AuthenticationResult, put_AuthenticationResult)
    CameraCaptureError = property(get_CameraCaptureError, None)
    CameraCaptureState = property(get_CameraCaptureState, None)
    EncodedVideoSize = property(get_EncodedVideoSize, None)
    IsCaptureTargetRunning = property(get_IsCaptureTargetRunning, None)
    MicrophoneCaptureError = property(get_MicrophoneCaptureError, None)
    MicrophoneCaptureState = property(get_MicrophoneCaptureState, None)
    OAuthCallbackUri = property(get_OAuthCallbackUri, None)
    OAuthRequestUri = property(get_OAuthRequestUri, None)
    PlugInState = property(get_PlugInState, None)
    ShouldCaptureCamera = property(get_ShouldCaptureCamera, put_ShouldCaptureCamera)
    ShouldCaptureMicrophone = property(get_ShouldCaptureMicrophone, put_ShouldCaptureMicrophone)
    SignInState = property(get_SignInState, put_SignInState)
    StreamState = property(get_StreamState, None)
    TerminationReason = property(get_TerminationReason, None)
    TerminationReasonPlugInSpecific = property(get_TerminationReasonPlugInSpecific, None)
    ViewerCount = property(get_ViewerCount, None)
    ViewerCountChanged = event()
    MicrophoneCaptureStateChanged = event()
    CameraCaptureStateChanged = event()
    PlugInStateChanged = event()
    StreamStateChanged = event()
    CaptureTargetClosed = event()
class IAppBroadcastStreamAudioFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastStreamAudioFrame'
    _iid_ = Guid('{efab4ac8-21ba-453f-8bb7-5e938a2e9a74}')
    @winrt_commethod(6)
    def get_AudioHeader(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamAudioHeader: ...
    @winrt_commethod(7)
    def get_AudioBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    AudioBuffer = property(get_AudioBuffer, None)
    AudioHeader = property(get_AudioHeader, None)
class IAppBroadcastStreamAudioHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastStreamAudioHeader'
    _iid_ = Guid('{bf21a570-6b78-4216-9f07-5aff5256f1b7}')
    @winrt_commethod(6)
    def get_AbsoluteTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_RelativeTimestamp(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_HasDiscontinuity(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_FrameId(self) -> UInt64: ...
    AbsoluteTimestamp = property(get_AbsoluteTimestamp, None)
    Duration = property(get_Duration, None)
    FrameId = property(get_FrameId, None)
    HasDiscontinuity = property(get_HasDiscontinuity, None)
    RelativeTimestamp = property(get_RelativeTimestamp, None)
class IAppBroadcastStreamReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastStreamReader'
    _iid_ = Guid('{b338bcf9-3364-4460-b5f1-3cc2796a8aa2}')
    @winrt_commethod(6)
    def get_AudioChannels(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_AudioSampleRate(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_AudioAacSequence(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def get_AudioBitrate(self) -> UInt32: ...
    @winrt_commethod(10)
    def TryGetNextAudioFrame(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamAudioFrame: ...
    @winrt_commethod(11)
    def get_VideoWidth(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_VideoHeight(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_VideoBitrate(self) -> UInt32: ...
    @winrt_commethod(14)
    def TryGetNextVideoFrame(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamVideoFrame: ...
    @winrt_commethod(15)
    def add_AudioFrameArrived(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastStreamReader, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_AudioFrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_VideoFrameArrived(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppBroadcastStreamReader, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_VideoFrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AudioAacSequence = property(get_AudioAacSequence, None)
    AudioBitrate = property(get_AudioBitrate, None)
    AudioChannels = property(get_AudioChannels, None)
    AudioSampleRate = property(get_AudioSampleRate, None)
    VideoBitrate = property(get_VideoBitrate, None)
    VideoHeight = property(get_VideoHeight, None)
    VideoWidth = property(get_VideoWidth, None)
    AudioFrameArrived = event()
    VideoFrameArrived = event()
class IAppBroadcastStreamStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastStreamStateChangedEventArgs'
    _iid_ = Guid('{5108a733-d008-4a89-93be-58aed961374e}')
    @winrt_commethod(6)
    def get_StreamState(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamState: ...
    StreamState = property(get_StreamState, None)
class IAppBroadcastStreamVideoFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastStreamVideoFrame'
    _iid_ = Guid('{0f97cf2b-c9e4-4e88-8194-d814cbd585d8}')
    @winrt_commethod(6)
    def get_VideoHeader(self) -> win32more.Windows.Media.Capture.AppBroadcastStreamVideoHeader: ...
    @winrt_commethod(7)
    def get_VideoBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    VideoBuffer = property(get_VideoBuffer, None)
    VideoHeader = property(get_VideoHeader, None)
class IAppBroadcastStreamVideoHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastStreamVideoHeader'
    _iid_ = Guid('{0b9ebece-7e32-432d-8ca2-36bf10b9f462}')
    @winrt_commethod(6)
    def get_AbsoluteTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_RelativeTimestamp(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_IsKeyFrame(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_HasDiscontinuity(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_FrameId(self) -> UInt64: ...
    AbsoluteTimestamp = property(get_AbsoluteTimestamp, None)
    Duration = property(get_Duration, None)
    FrameId = property(get_FrameId, None)
    HasDiscontinuity = property(get_HasDiscontinuity, None)
    IsKeyFrame = property(get_IsKeyFrame, None)
    RelativeTimestamp = property(get_RelativeTimestamp, None)
class IAppBroadcastTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastTriggerDetails'
    _iid_ = Guid('{deebab35-ec5e-4d8f-b1c0-5da6e8c75638}')
    @winrt_commethod(6)
    def get_BackgroundService(self) -> win32more.Windows.Media.Capture.AppBroadcastBackgroundService: ...
    BackgroundService = property(get_BackgroundService, None)
class IAppBroadcastViewerCountChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppBroadcastViewerCountChangedEventArgs'
    _iid_ = Guid('{e6e11825-5401-4ade-8bd2-c14ecee6807d}')
    @winrt_commethod(6)
    def get_ViewerCount(self) -> UInt32: ...
    ViewerCount = property(get_ViewerCount, None)
class IAppCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCapture'
    _iid_ = Guid('{9749d453-a29a-45ed-8f29-22d09942cff7}')
    @winrt_commethod(6)
    def get_IsCapturingAudio(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsCapturingVideo(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_CapturingChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CapturingChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsCapturingAudio = property(get_IsCapturingAudio, None)
    IsCapturingVideo = property(get_IsCapturingVideo, None)
    CapturingChanged = event()
class IAppCaptureAlternateShortcutKeys(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureAlternateShortcutKeys'
    _iid_ = Guid('{19e8e0ef-236c-40f9-b38f-9b7dd65d1ccc}')
    @winrt_commethod(6)
    def put_ToggleGameBarKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(7)
    def get_ToggleGameBarKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(8)
    def put_ToggleGameBarKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(9)
    def get_ToggleGameBarKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(10)
    def put_SaveHistoricalVideoKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(11)
    def get_SaveHistoricalVideoKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(12)
    def put_SaveHistoricalVideoKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(13)
    def get_SaveHistoricalVideoKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(14)
    def put_ToggleRecordingKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(15)
    def get_ToggleRecordingKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(16)
    def put_ToggleRecordingKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(17)
    def get_ToggleRecordingKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(18)
    def put_TakeScreenshotKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(19)
    def get_TakeScreenshotKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(20)
    def put_TakeScreenshotKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(21)
    def get_TakeScreenshotKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(22)
    def put_ToggleRecordingIndicatorKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(23)
    def get_ToggleRecordingIndicatorKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(24)
    def put_ToggleRecordingIndicatorKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(25)
    def get_ToggleRecordingIndicatorKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    SaveHistoricalVideoKey = property(get_SaveHistoricalVideoKey, put_SaveHistoricalVideoKey)
    SaveHistoricalVideoKeyModifiers = property(get_SaveHistoricalVideoKeyModifiers, put_SaveHistoricalVideoKeyModifiers)
    TakeScreenshotKey = property(get_TakeScreenshotKey, put_TakeScreenshotKey)
    TakeScreenshotKeyModifiers = property(get_TakeScreenshotKeyModifiers, put_TakeScreenshotKeyModifiers)
    ToggleGameBarKey = property(get_ToggleGameBarKey, put_ToggleGameBarKey)
    ToggleGameBarKeyModifiers = property(get_ToggleGameBarKeyModifiers, put_ToggleGameBarKeyModifiers)
    ToggleRecordingIndicatorKey = property(get_ToggleRecordingIndicatorKey, put_ToggleRecordingIndicatorKey)
    ToggleRecordingIndicatorKeyModifiers = property(get_ToggleRecordingIndicatorKeyModifiers, put_ToggleRecordingIndicatorKeyModifiers)
    ToggleRecordingKey = property(get_ToggleRecordingKey, put_ToggleRecordingKey)
    ToggleRecordingKeyModifiers = property(get_ToggleRecordingKeyModifiers, put_ToggleRecordingKeyModifiers)
class IAppCaptureAlternateShortcutKeys2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureAlternateShortcutKeys2'
    _iid_ = Guid('{c3669090-dd17-47f0-95e5-ce42286cf338}')
    @winrt_commethod(6)
    def put_ToggleMicrophoneCaptureKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(7)
    def get_ToggleMicrophoneCaptureKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(8)
    def put_ToggleMicrophoneCaptureKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(9)
    def get_ToggleMicrophoneCaptureKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    ToggleMicrophoneCaptureKey = property(get_ToggleMicrophoneCaptureKey, put_ToggleMicrophoneCaptureKey)
    ToggleMicrophoneCaptureKeyModifiers = property(get_ToggleMicrophoneCaptureKeyModifiers, put_ToggleMicrophoneCaptureKeyModifiers)
class IAppCaptureAlternateShortcutKeys3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureAlternateShortcutKeys3'
    _iid_ = Guid('{7b81448c-418e-469c-a49a-45b597c826b6}')
    @winrt_commethod(6)
    def put_ToggleCameraCaptureKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(7)
    def get_ToggleCameraCaptureKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(8)
    def put_ToggleCameraCaptureKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(9)
    def get_ToggleCameraCaptureKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(10)
    def put_ToggleBroadcastKey(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(11)
    def get_ToggleBroadcastKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(12)
    def put_ToggleBroadcastKeyModifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(13)
    def get_ToggleBroadcastKeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    ToggleBroadcastKey = property(get_ToggleBroadcastKey, put_ToggleBroadcastKey)
    ToggleBroadcastKeyModifiers = property(get_ToggleBroadcastKeyModifiers, put_ToggleBroadcastKeyModifiers)
    ToggleCameraCaptureKey = property(get_ToggleCameraCaptureKey, put_ToggleCameraCaptureKey)
    ToggleCameraCaptureKeyModifiers = property(get_ToggleCameraCaptureKeyModifiers, put_ToggleCameraCaptureKeyModifiers)
class IAppCaptureDurationGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureDurationGeneratedEventArgs'
    _iid_ = Guid('{c1f5563b-ffa1-44c9-975f-27fbeb553b35}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Duration = property(get_Duration, None)
class IAppCaptureFileGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureFileGeneratedEventArgs'
    _iid_ = Guid('{4189fbf4-465e-45bf-907f-165b3fb23758}')
    @winrt_commethod(6)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    File = property(get_File, None)
class IAppCaptureManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureManagerStatics'
    _iid_ = Guid('{7d9e3ea7-6282-4735-8d4e-aa45f90f6723}')
    @winrt_commethod(6)
    def GetCurrentSettings(self) -> win32more.Windows.Media.Capture.AppCaptureSettings: ...
    @winrt_commethod(7)
    def ApplySettings(self, appCaptureSettings: win32more.Windows.Media.Capture.AppCaptureSettings) -> Void: ...
class IAppCaptureMetadataWriter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureMetadataWriter'
    _iid_ = Guid('{e0ce4877-9aaf-46b4-ad31-6a60b441c780}')
    @winrt_commethod(6)
    def AddStringEvent(self, name: WinRT_String, value: WinRT_String, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_commethod(7)
    def AddInt32Event(self, name: WinRT_String, value: Int32, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_commethod(8)
    def AddDoubleEvent(self, name: WinRT_String, value: Double, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_commethod(9)
    def StartStringState(self, name: WinRT_String, value: WinRT_String, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_commethod(10)
    def StartInt32State(self, name: WinRT_String, value: Int32, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_commethod(11)
    def StartDoubleState(self, name: WinRT_String, value: Double, priority: win32more.Windows.Media.Capture.AppCaptureMetadataPriority) -> Void: ...
    @winrt_commethod(12)
    def StopState(self, name: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def StopAllStates(self) -> Void: ...
    @winrt_commethod(14)
    def get_RemainingStorageBytesAvailable(self) -> UInt64: ...
    @winrt_commethod(15)
    def add_MetadataPurged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureMetadataWriter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_MetadataPurged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    RemainingStorageBytesAvailable = property(get_RemainingStorageBytesAvailable, None)
    MetadataPurged = event()
class IAppCaptureMicrophoneCaptureStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureMicrophoneCaptureStateChangedEventArgs'
    _iid_ = Guid('{324d249e-45bc-4c35-bc35-e469fc7a69e0}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.Capture.AppCaptureMicrophoneCaptureState: ...
    @winrt_commethod(7)
    def get_ErrorCode(self) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class IAppCaptureRecordOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureRecordOperation'
    _iid_ = Guid('{c66020a9-1538-495c-9bbb-2ba870ec5861}')
    @winrt_commethod(6)
    def StopRecording(self) -> Void: ...
    @winrt_commethod(7)
    def get_State(self) -> win32more.Windows.Media.Capture.AppCaptureRecordingState: ...
    @winrt_commethod(8)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_Duration(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(10)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_commethod(11)
    def get_IsFileTruncated(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(12)
    def add_StateChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureRecordOperation, win32more.Windows.Media.Capture.AppCaptureRecordingStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_DurationGenerated(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureRecordOperation, win32more.Windows.Media.Capture.AppCaptureDurationGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DurationGenerated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_FileGenerated(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureRecordOperation, win32more.Windows.Media.Capture.AppCaptureFileGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_FileGenerated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Duration = property(get_Duration, None)
    ErrorCode = property(get_ErrorCode, None)
    File = property(get_File, None)
    IsFileTruncated = property(get_IsFileTruncated, None)
    State = property(get_State, None)
    StateChanged = event()
    DurationGenerated = event()
    FileGenerated = event()
class IAppCaptureRecordingStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureRecordingStateChangedEventArgs'
    _iid_ = Guid('{24fc8712-e305-490d-b415-6b1c9049736b}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.Capture.AppCaptureRecordingState: ...
    @winrt_commethod(7)
    def get_ErrorCode(self) -> UInt32: ...
    ErrorCode = property(get_ErrorCode, None)
    State = property(get_State, None)
class IAppCaptureServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureServices'
    _iid_ = Guid('{44fec0b5-34f5-4f18-ae8c-b9123abbfc0d}')
    @winrt_commethod(6)
    def Record(self) -> win32more.Windows.Media.Capture.AppCaptureRecordOperation: ...
    @winrt_commethod(7)
    def RecordTimeSpan(self, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Capture.AppCaptureRecordOperation: ...
    @winrt_commethod(8)
    def get_CanCapture(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Media.Capture.AppCaptureState: ...
    CanCapture = property(get_CanCapture, None)
    State = property(get_State, None)
class IAppCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureSettings'
    _iid_ = Guid('{14683a86-8807-48d3-883a-970ee4532a39}')
    @winrt_commethod(6)
    def put_AppCaptureDestinationFolder(self, value: win32more.Windows.Storage.StorageFolder) -> Void: ...
    @winrt_commethod(7)
    def get_AppCaptureDestinationFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def put_AudioEncodingBitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_AudioEncodingBitrate(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_IsAudioCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsAudioCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_CustomVideoEncodingBitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_CustomVideoEncodingBitrate(self) -> UInt32: ...
    @winrt_commethod(14)
    def put_CustomVideoEncodingHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(15)
    def get_CustomVideoEncodingHeight(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_CustomVideoEncodingWidth(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_CustomVideoEncodingWidth(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_HistoricalBufferLength(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_HistoricalBufferLength(self) -> UInt32: ...
    @winrt_commethod(20)
    def put_HistoricalBufferLengthUnit(self, value: win32more.Windows.Media.Capture.AppCaptureHistoricalBufferLengthUnit) -> Void: ...
    @winrt_commethod(21)
    def get_HistoricalBufferLengthUnit(self) -> win32more.Windows.Media.Capture.AppCaptureHistoricalBufferLengthUnit: ...
    @winrt_commethod(22)
    def put_IsHistoricalCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_IsHistoricalCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_IsHistoricalCaptureOnBatteryAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(25)
    def get_IsHistoricalCaptureOnBatteryAllowed(self) -> Boolean: ...
    @winrt_commethod(26)
    def put_IsHistoricalCaptureOnWirelessDisplayAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(27)
    def get_IsHistoricalCaptureOnWirelessDisplayAllowed(self) -> Boolean: ...
    @winrt_commethod(28)
    def put_MaximumRecordLength(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(29)
    def get_MaximumRecordLength(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(30)
    def put_ScreenshotDestinationFolder(self, value: win32more.Windows.Storage.StorageFolder) -> Void: ...
    @winrt_commethod(31)
    def get_ScreenshotDestinationFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(32)
    def put_VideoEncodingBitrateMode(self, value: win32more.Windows.Media.Capture.AppCaptureVideoEncodingBitrateMode) -> Void: ...
    @winrt_commethod(33)
    def get_VideoEncodingBitrateMode(self) -> win32more.Windows.Media.Capture.AppCaptureVideoEncodingBitrateMode: ...
    @winrt_commethod(34)
    def put_VideoEncodingResolutionMode(self, value: win32more.Windows.Media.Capture.AppCaptureVideoEncodingResolutionMode) -> Void: ...
    @winrt_commethod(35)
    def get_VideoEncodingResolutionMode(self) -> win32more.Windows.Media.Capture.AppCaptureVideoEncodingResolutionMode: ...
    @winrt_commethod(36)
    def put_IsAppCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(37)
    def get_IsAppCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(38)
    def get_IsCpuConstrained(self) -> Boolean: ...
    @winrt_commethod(39)
    def get_IsDisabledByPolicy(self) -> Boolean: ...
    @winrt_commethod(40)
    def get_IsMemoryConstrained(self) -> Boolean: ...
    @winrt_commethod(41)
    def get_HasHardwareEncoder(self) -> Boolean: ...
    AppCaptureDestinationFolder = property(get_AppCaptureDestinationFolder, put_AppCaptureDestinationFolder)
    AudioEncodingBitrate = property(get_AudioEncodingBitrate, put_AudioEncodingBitrate)
    CustomVideoEncodingBitrate = property(get_CustomVideoEncodingBitrate, put_CustomVideoEncodingBitrate)
    CustomVideoEncodingHeight = property(get_CustomVideoEncodingHeight, put_CustomVideoEncodingHeight)
    CustomVideoEncodingWidth = property(get_CustomVideoEncodingWidth, put_CustomVideoEncodingWidth)
    HasHardwareEncoder = property(get_HasHardwareEncoder, None)
    HistoricalBufferLength = property(get_HistoricalBufferLength, put_HistoricalBufferLength)
    HistoricalBufferLengthUnit = property(get_HistoricalBufferLengthUnit, put_HistoricalBufferLengthUnit)
    IsAppCaptureEnabled = property(get_IsAppCaptureEnabled, put_IsAppCaptureEnabled)
    IsAudioCaptureEnabled = property(get_IsAudioCaptureEnabled, put_IsAudioCaptureEnabled)
    IsCpuConstrained = property(get_IsCpuConstrained, None)
    IsDisabledByPolicy = property(get_IsDisabledByPolicy, None)
    IsHistoricalCaptureEnabled = property(get_IsHistoricalCaptureEnabled, put_IsHistoricalCaptureEnabled)
    IsHistoricalCaptureOnBatteryAllowed = property(get_IsHistoricalCaptureOnBatteryAllowed, put_IsHistoricalCaptureOnBatteryAllowed)
    IsHistoricalCaptureOnWirelessDisplayAllowed = property(get_IsHistoricalCaptureOnWirelessDisplayAllowed, put_IsHistoricalCaptureOnWirelessDisplayAllowed)
    IsMemoryConstrained = property(get_IsMemoryConstrained, None)
    MaximumRecordLength = property(get_MaximumRecordLength, put_MaximumRecordLength)
    ScreenshotDestinationFolder = property(get_ScreenshotDestinationFolder, put_ScreenshotDestinationFolder)
    VideoEncodingBitrateMode = property(get_VideoEncodingBitrateMode, put_VideoEncodingBitrateMode)
    VideoEncodingResolutionMode = property(get_VideoEncodingResolutionMode, put_VideoEncodingResolutionMode)
class IAppCaptureSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureSettings2'
    _iid_ = Guid('{fcb8cee7-e26b-476f-9b1a-ec342d2a8fde}')
    @winrt_commethod(6)
    def get_IsGpuConstrained(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AlternateShortcutKeys(self) -> win32more.Windows.Media.Capture.AppCaptureAlternateShortcutKeys: ...
    AlternateShortcutKeys = property(get_AlternateShortcutKeys, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
class IAppCaptureSettings3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureSettings3'
    _iid_ = Guid('{a93502fe-88c2-42d6-aaaa-40feffd75aec}')
    @winrt_commethod(6)
    def put_IsMicrophoneCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsMicrophoneCaptureEnabled(self) -> Boolean: ...
    IsMicrophoneCaptureEnabled = property(get_IsMicrophoneCaptureEnabled, put_IsMicrophoneCaptureEnabled)
class IAppCaptureSettings4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureSettings4'
    _iid_ = Guid('{07c2774c-1a81-482f-a244-049d95f25b0b}')
    @winrt_commethod(6)
    def put_IsMicrophoneCaptureEnabledByDefault(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsMicrophoneCaptureEnabledByDefault(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_SystemAudioGain(self, value: Double) -> Void: ...
    @winrt_commethod(9)
    def get_SystemAudioGain(self) -> Double: ...
    @winrt_commethod(10)
    def put_MicrophoneGain(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def get_MicrophoneGain(self) -> Double: ...
    @winrt_commethod(12)
    def put_VideoEncodingFrameRateMode(self, value: win32more.Windows.Media.Capture.AppCaptureVideoEncodingFrameRateMode) -> Void: ...
    @winrt_commethod(13)
    def get_VideoEncodingFrameRateMode(self) -> win32more.Windows.Media.Capture.AppCaptureVideoEncodingFrameRateMode: ...
    IsMicrophoneCaptureEnabledByDefault = property(get_IsMicrophoneCaptureEnabledByDefault, put_IsMicrophoneCaptureEnabledByDefault)
    MicrophoneGain = property(get_MicrophoneGain, put_MicrophoneGain)
    SystemAudioGain = property(get_SystemAudioGain, put_SystemAudioGain)
    VideoEncodingFrameRateMode = property(get_VideoEncodingFrameRateMode, put_VideoEncodingFrameRateMode)
class IAppCaptureSettings5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureSettings5'
    _iid_ = Guid('{18894522-b0e8-4ba0-8f13-3eaa5fa4013b}')
    @winrt_commethod(6)
    def put_IsEchoCancellationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsEchoCancellationEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsCursorImageCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsCursorImageCaptureEnabled(self) -> Boolean: ...
    IsCursorImageCaptureEnabled = property(get_IsCursorImageCaptureEnabled, put_IsCursorImageCaptureEnabled)
    IsEchoCancellationEnabled = property(get_IsEchoCancellationEnabled, put_IsEchoCancellationEnabled)
class IAppCaptureState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureState'
    _iid_ = Guid('{73134372-d4eb-44ce-9538-465f506ac4ea}')
    @winrt_commethod(6)
    def get_IsTargetRunning(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsHistoricalCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ShouldCaptureMicrophone(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_ShouldCaptureMicrophone(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def RestartMicrophoneCapture(self) -> Void: ...
    @winrt_commethod(11)
    def get_MicrophoneCaptureState(self) -> win32more.Windows.Media.Capture.AppCaptureMicrophoneCaptureState: ...
    @winrt_commethod(12)
    def get_MicrophoneCaptureError(self) -> UInt32: ...
    @winrt_commethod(13)
    def add_MicrophoneCaptureStateChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureState, win32more.Windows.Media.Capture.AppCaptureMicrophoneCaptureStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_MicrophoneCaptureStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_CaptureTargetClosed(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.AppCaptureState, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_CaptureTargetClosed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsHistoricalCaptureEnabled = property(get_IsHistoricalCaptureEnabled, None)
    IsTargetRunning = property(get_IsTargetRunning, None)
    MicrophoneCaptureError = property(get_MicrophoneCaptureError, None)
    MicrophoneCaptureState = property(get_MicrophoneCaptureState, None)
    ShouldCaptureMicrophone = property(get_ShouldCaptureMicrophone, put_ShouldCaptureMicrophone)
    MicrophoneCaptureStateChanged = event()
    CaptureTargetClosed = event()
class IAppCaptureStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureStatics'
    _iid_ = Guid('{f922dd6c-0a7e-4e74-8b20-9c1f902d08a1}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Media.Capture.AppCapture: ...
class IAppCaptureStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IAppCaptureStatics2'
    _iid_ = Guid('{b2d881d4-836c-4da4-afd7-facc041e1cf3}')
    @winrt_commethod(6)
    def SetAllowedAsync(self, allowed: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICameraCaptureUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICameraCaptureUI'
    _iid_ = Guid('{48587540-6f93-4bb4-b8f3-e89e48948c91}')
    @winrt_commethod(6)
    def get_PhotoSettings(self) -> win32more.Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings: ...
    @winrt_commethod(7)
    def get_VideoSettings(self) -> win32more.Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings: ...
    @winrt_commethod(8)
    def CaptureFileAsync(self, mode: win32more.Windows.Media.Capture.CameraCaptureUIMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    PhotoSettings = property(get_PhotoSettings, None)
    VideoSettings = property(get_VideoSettings, None)
class ICameraCaptureUIPhotoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings'
    _iid_ = Guid('{b9f5be97-3472-46a8-8a9e-04ce42ccc97d}')
    @winrt_commethod(6)
    def get_Format(self) -> win32more.Windows.Media.Capture.CameraCaptureUIPhotoFormat: ...
    @winrt_commethod(7)
    def put_Format(self, value: win32more.Windows.Media.Capture.CameraCaptureUIPhotoFormat) -> Void: ...
    @winrt_commethod(8)
    def get_MaxResolution(self) -> win32more.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution: ...
    @winrt_commethod(9)
    def put_MaxResolution(self, value: win32more.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution) -> Void: ...
    @winrt_commethod(10)
    def get_CroppedSizeInPixels(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def put_CroppedSizeInPixels(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(12)
    def get_CroppedAspectRatio(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(13)
    def put_CroppedAspectRatio(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(14)
    def get_AllowCropping(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AllowCropping(self, value: Boolean) -> Void: ...
    AllowCropping = property(get_AllowCropping, put_AllowCropping)
    CroppedAspectRatio = property(get_CroppedAspectRatio, put_CroppedAspectRatio)
    CroppedSizeInPixels = property(get_CroppedSizeInPixels, put_CroppedSizeInPixels)
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
class ICameraCaptureUIVideoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings'
    _iid_ = Guid('{64e92d1f-a28d-425a-b84f-e568335ff24e}')
    @winrt_commethod(6)
    def get_Format(self) -> win32more.Windows.Media.Capture.CameraCaptureUIVideoFormat: ...
    @winrt_commethod(7)
    def put_Format(self, value: win32more.Windows.Media.Capture.CameraCaptureUIVideoFormat) -> Void: ...
    @winrt_commethod(8)
    def get_MaxResolution(self) -> win32more.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution: ...
    @winrt_commethod(9)
    def put_MaxResolution(self, value: win32more.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution) -> Void: ...
    @winrt_commethod(10)
    def get_MaxDurationInSeconds(self) -> Single: ...
    @winrt_commethod(11)
    def put_MaxDurationInSeconds(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_AllowTrimming(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_AllowTrimming(self, value: Boolean) -> Void: ...
    AllowTrimming = property(get_AllowTrimming, put_AllowTrimming)
    Format = property(get_Format, put_Format)
    MaxDurationInSeconds = property(get_MaxDurationInSeconds, put_MaxDurationInSeconds)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
class ICameraOptionsUIStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICameraOptionsUIStatics'
    _iid_ = Guid('{3b0d5e34-3906-4b7d-946c-7bde844499ae}')
    @winrt_commethod(6)
    def Show(self, mediaCapture: win32more.Windows.Media.Capture.MediaCapture) -> Void: ...
class ICapturedFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Capture.ICapturedFrame'
    _iid_ = Guid('{1dd2de1f-571b-44d8-8e80-a08a1578766e}')
    @winrt_commethod(6)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Height(self) -> UInt32: ...
    Height = property(get_Height, None)
    Width = property(get_Width, None)
class ICapturedFrame2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICapturedFrame2'
    _iid_ = Guid('{543fa6d1-bd78-4866-adda-24314bc65dea}')
    @winrt_commethod(6)
    def get_ControlValues(self) -> win32more.Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_commethod(7)
    def get_BitmapProperties(self) -> win32more.Windows.Graphics.Imaging.BitmapPropertySet: ...
    BitmapProperties = property(get_BitmapProperties, None)
    ControlValues = property(get_ControlValues, None)
class ICapturedFrameControlValues(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICapturedFrameControlValues'
    _iid_ = Guid('{90c65b7f-4e0d-4ca4-882d-7a144fed0a90}')
    @winrt_commethod(6)
    def get_Exposure(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_ExposureCompensation(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(8)
    def get_IsoSpeed(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_Focus(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(10)
    def get_SceneMode(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_commethod(11)
    def get_Flashed(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(12)
    def get_FlashPowerPercent(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(13)
    def get_WhiteBalance(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(14)
    def get_ZoomFactor(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    FlashPowerPercent = property(get_FlashPowerPercent, None)
    Flashed = property(get_Flashed, None)
    Focus = property(get_Focus, None)
    IsoSpeed = property(get_IsoSpeed, None)
    SceneMode = property(get_SceneMode, None)
    WhiteBalance = property(get_WhiteBalance, None)
    ZoomFactor = property(get_ZoomFactor, None)
class ICapturedFrameControlValues2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICapturedFrameControlValues2'
    _iid_ = Guid('{500b2b88-06d2-4aa7-a7db-d37af73321d8}')
    @winrt_commethod(6)
    def get_FocusState(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.MediaCaptureFocusState]: ...
    @winrt_commethod(7)
    def get_IsoDigitalGain(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(8)
    def get_IsoAnalogGain(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def get_SensorFrameRate(self) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(10)
    def get_WhiteBalanceGain(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Capture.WhiteBalanceGain]: ...
    FocusState = property(get_FocusState, None)
    IsoAnalogGain = property(get_IsoAnalogGain, None)
    IsoDigitalGain = property(get_IsoDigitalGain, None)
    SensorFrameRate = property(get_SensorFrameRate, None)
    WhiteBalanceGain = property(get_WhiteBalanceGain, None)
class ICapturedFrameWithSoftwareBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICapturedFrameWithSoftwareBitmap'
    _iid_ = Guid('{b58e8b6e-8503-49b5-9e86-897d26a3ff3d}')
    @winrt_commethod(6)
    def get_SoftwareBitmap(self) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    SoftwareBitmap = property(get_SoftwareBitmap, None)
class ICapturedPhoto(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ICapturedPhoto'
    _iid_ = Guid('{b0ce7e5a-cfcc-4d6c-8ad1-0869208aca16}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Thumbnail(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
class IGameBarServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IGameBarServices'
    _iid_ = Guid('{2dbead57-50a6-499e-8c6c-d330a7311796}')
    @winrt_commethod(6)
    def get_TargetCapturePolicy(self) -> win32more.Windows.Media.Capture.GameBarTargetCapturePolicy: ...
    @winrt_commethod(7)
    def EnableCapture(self) -> Void: ...
    @winrt_commethod(8)
    def DisableCapture(self) -> Void: ...
    @winrt_commethod(9)
    def get_TargetInfo(self) -> win32more.Windows.Media.Capture.GameBarServicesTargetInfo: ...
    @winrt_commethod(10)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AppBroadcastServices(self) -> win32more.Windows.Media.Capture.AppBroadcastServices: ...
    @winrt_commethod(12)
    def get_AppCaptureServices(self) -> win32more.Windows.Media.Capture.AppCaptureServices: ...
    @winrt_commethod(13)
    def add_CommandReceived(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.GameBarServices, win32more.Windows.Media.Capture.GameBarServicesCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_CommandReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AppBroadcastServices = property(get_AppBroadcastServices, None)
    AppCaptureServices = property(get_AppCaptureServices, None)
    SessionId = property(get_SessionId, None)
    TargetCapturePolicy = property(get_TargetCapturePolicy, None)
    TargetInfo = property(get_TargetInfo, None)
    CommandReceived = event()
class IGameBarServicesCommandEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IGameBarServicesCommandEventArgs'
    _iid_ = Guid('{a74226b2-f176-4fcf-8fbb-cf698b2eb8e0}')
    @winrt_commethod(6)
    def get_Command(self) -> win32more.Windows.Media.Capture.GameBarCommand: ...
    @winrt_commethod(7)
    def get_Origin(self) -> win32more.Windows.Media.Capture.GameBarCommandOrigin: ...
    Command = property(get_Command, None)
    Origin = property(get_Origin, None)
class IGameBarServicesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IGameBarServicesManager'
    _iid_ = Guid('{3a4b9cfa-7f8b-4c60-9dbb-0bcd262dffc6}')
    @winrt_commethod(6)
    def add_GameBarServicesCreated(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.GameBarServicesManager, win32more.Windows.Media.Capture.GameBarServicesManagerGameBarServicesCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GameBarServicesCreated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    GameBarServicesCreated = event()
class IGameBarServicesManagerGameBarServicesCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IGameBarServicesManagerGameBarServicesCreatedEventArgs'
    _iid_ = Guid('{ededbd9c-143e-49a3-a5ea-0b1995c8d46e}')
    @winrt_commethod(6)
    def get_GameBarServices(self) -> win32more.Windows.Media.Capture.GameBarServices: ...
    GameBarServices = property(get_GameBarServices, None)
class IGameBarServicesManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IGameBarServicesManagerStatics'
    _iid_ = Guid('{34c1b616-ff25-4792-98f2-d3753f15ac13}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Media.Capture.GameBarServicesManager: ...
class IGameBarServicesTargetInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IGameBarServicesTargetInfo'
    _iid_ = Guid('{b4202f92-1611-4e05-b6ef-dfd737ae33b0}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_TitleId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayMode(self) -> win32more.Windows.Media.Capture.GameBarServicesDisplayMode: ...
    AppId = property(get_AppId, None)
    DisplayMode = property(get_DisplayMode, None)
    DisplayName = property(get_DisplayName, None)
    TitleId = property(get_TitleId, None)
class ILowLagMediaRecording(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ILowLagMediaRecording'
    _iid_ = Guid('{41c8baf7-ff3f-49f0-a477-f195e3ce5108}')
    @winrt_commethod(6)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def FinishAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class ILowLagMediaRecording2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ILowLagMediaRecording2'
    _iid_ = Guid('{6369c758-5644-41e2-97af-8ef56a25e225}')
    @winrt_commethod(6)
    def PauseAsync(self, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ResumeAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class ILowLagMediaRecording3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ILowLagMediaRecording3'
    _iid_ = Guid('{5c33ab12-48f7-47da-b41e-90880a5fe0ec}')
    @winrt_commethod(6)
    def PauseWithResultAsync(self, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_commethod(7)
    def StopWithResultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCaptureStopResult]: ...
class ILowLagPhotoCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ILowLagPhotoCapture'
    _iid_ = Guid('{a37251b7-6b44-473d-8f24-f703d6c0ec44}')
    @winrt_commethod(6)
    def CaptureAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.CapturedPhoto]: ...
    @winrt_commethod(7)
    def FinishAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class ILowLagPhotoSequenceCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ILowLagPhotoSequenceCapture'
    _iid_ = Guid('{7cc346bb-b9a9-4c91-8ffa-287e9c668669}')
    @winrt_commethod(6)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def FinishAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_PhotoCaptured(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.LowLagPhotoSequenceCapture, win32more.Windows.Media.Capture.PhotoCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PhotoCaptured(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PhotoCaptured = event()
class IMediaCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapture'
    _iid_ = Guid('{c61afbb4-fb10-4a34-ac18-ca80d9c8e7ee}')
    @winrt_commethod(6)
    def InitializeAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def InitializeWithSettingsAsync(self, mediaCaptureInitializationSettings: win32more.Windows.Media.Capture.MediaCaptureInitializationSettings) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def StartRecordToStorageFileAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def StartRecordToStreamAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def StartRecordToCustomSinkAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def StartRecordToCustomSinkIdAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def StopRecordAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def CapturePhotoToStorageFileAsync(self, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def CapturePhotoToStreamAsync(self, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def AddEffectAsync(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, effectActivationID: WinRT_String, effectSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def ClearEffectsAsync(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def SetEncoderProperty(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, propertyId: Guid, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(18)
    def GetEncoderProperty(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, propertyId: Guid) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(19)
    def add_Failed(self, errorEventHandler: win32more.Windows.Media.Capture.MediaCaptureFailedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_Failed(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_RecordLimitationExceeded(self, recordLimitationExceededEventHandler: win32more.Windows.Media.Capture.RecordLimitationExceededEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_RecordLimitationExceeded(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def get_MediaCaptureSettings(self) -> win32more.Windows.Media.Capture.MediaCaptureSettings: ...
    @winrt_commethod(24)
    def get_AudioDeviceController(self) -> win32more.Windows.Media.Devices.AudioDeviceController: ...
    @winrt_commethod(25)
    def get_VideoDeviceController(self) -> win32more.Windows.Media.Devices.VideoDeviceController: ...
    @winrt_commethod(26)
    def SetPreviewMirroring(self, value: Boolean) -> Void: ...
    @winrt_commethod(27)
    def GetPreviewMirroring(self) -> Boolean: ...
    @winrt_commethod(28)
    def SetPreviewRotation(self, value: win32more.Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_commethod(29)
    def GetPreviewRotation(self) -> win32more.Windows.Media.Capture.VideoRotation: ...
    @winrt_commethod(30)
    def SetRecordRotation(self, value: win32more.Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_commethod(31)
    def GetRecordRotation(self) -> win32more.Windows.Media.Capture.VideoRotation: ...
    AudioDeviceController = property(get_AudioDeviceController, None)
    MediaCaptureSettings = property(get_MediaCaptureSettings, None)
    VideoDeviceController = property(get_VideoDeviceController, None)
    Failed = event()
    RecordLimitationExceeded = event()
class IMediaCapture2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapture2'
    _iid_ = Guid('{9cc68260-7da1-4043-b652-21b8878daff9}')
    @winrt_commethod(6)
    def PrepareLowLagRecordToStorageFileAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(7)
    def PrepareLowLagRecordToStreamAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(8)
    def PrepareLowLagRecordToCustomSinkAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(9)
    def PrepareLowLagRecordToCustomSinkIdAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(10)
    def PrepareLowLagPhotoCaptureAsync(self, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagPhotoCapture]: ...
    @winrt_commethod(11)
    def PrepareLowLagPhotoSequenceCaptureAsync(self, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagPhotoSequenceCapture]: ...
    @winrt_commethod(12)
    def SetEncodingPropertiesAsync(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties, encoderProperties: win32more.Windows.Media.MediaProperties.MediaPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
class IMediaCapture3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapture3'
    _iid_ = Guid('{d4136f30-1564-466e-bc0a-af94e02ab016}')
    @winrt_commethod(6)
    def PrepareVariablePhotoSequenceCaptureAsync(self, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture]: ...
    @winrt_commethod(7)
    def add_FocusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Media.Capture.MediaCaptureFocusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_FocusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PhotoConfirmationCaptured(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Media.Capture.PhotoConfirmationCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PhotoConfirmationCaptured(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    FocusChanged = event()
    PhotoConfirmationCaptured = event()
class IMediaCapture4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapture4'
    _iid_ = Guid('{bacd6fd6-fb08-4947-aea2-ce14eff0ce13}')
    @winrt_commethod(6)
    def AddAudioEffectAsync(self, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.IMediaExtension]: ...
    @winrt_commethod(7)
    def AddVideoEffectAsync(self, definition: win32more.Windows.Media.Effects.IVideoEffectDefinition, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.IMediaExtension]: ...
    @winrt_commethod(8)
    def PauseRecordAsync(self, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ResumeRecordAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def add_CameraStreamStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CameraStreamStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_CameraStreamState(self) -> win32more.Windows.Media.Devices.CameraStreamState: ...
    @winrt_commethod(13)
    def GetPreviewFrameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.VideoFrame]: ...
    @winrt_commethod(14)
    def GetPreviewFrameCopyAsync(self, destination: win32more.Windows.Media.VideoFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.VideoFrame]: ...
    @winrt_commethod(15)
    def add_ThermalStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ThermalStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def get_ThermalStatus(self) -> win32more.Windows.Media.Capture.MediaCaptureThermalStatus: ...
    @winrt_commethod(18)
    def PrepareAdvancedPhotoCaptureAsync(self, encodingProperties: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.AdvancedPhotoCapture]: ...
    CameraStreamState = property(get_CameraStreamState, None)
    ThermalStatus = property(get_ThermalStatus, None)
    CameraStreamStateChanged = event()
    ThermalStatusChanged = event()
class IMediaCapture5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapture5'
    _iid_ = Guid('{da787c22-3a9b-4720-a71e-97900a316e5a}')
    @winrt_commethod(6)
    def RemoveEffectAsync(self, effect: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def PauseRecordWithResultAsync(self, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_commethod(8)
    def StopRecordWithResultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCaptureStopResult]: ...
    @winrt_commethod(9)
    def get_FrameSources(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Media.Capture.Frames.MediaFrameSource]: ...
    @winrt_commethod(10)
    def CreateFrameReaderAsync(self, inputSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_commethod(11)
    def CreateFrameReaderWithSubtypeAsync(self, inputSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_commethod(12)
    def CreateFrameReaderWithSubtypeAndSizeAsync(self, inputSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String, outputSize: win32more.Windows.Graphics.Imaging.BitmapSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReader]: ...
    FrameSources = property(get_FrameSources, None)
class IMediaCapture6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapture6'
    _iid_ = Guid('{228948bd-4b20-4bb1-9fd6-a583212a1012}')
    @winrt_commethod(6)
    def add_CaptureDeviceExclusiveControlStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CaptureDeviceExclusiveControlStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def CreateMultiSourceFrameReaderAsync(self, inputSources: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Capture.Frames.MediaFrameSource]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReader]: ...
    CaptureDeviceExclusiveControlStatusChanged = event()
class IMediaCapture7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapture7'
    _iid_ = Guid('{9169f102-8888-541a-95bc-24e4d462542a}')
    @winrt_commethod(6)
    def CreateRelativePanelWatcher(self, captureMode: win32more.Windows.Media.Capture.StreamingCaptureMode, displayRegion: win32more.Windows.UI.WindowManagement.DisplayRegion) -> win32more.Windows.Media.Capture.MediaCaptureRelativePanelWatcher: ...
class IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs'
    _iid_ = Guid('{9d2f920d-a588-43c6-89d6-5ad322af006a}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatus: ...
    DeviceId = property(get_DeviceId, None)
    Status = property(get_Status, None)
class IMediaCaptureFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureFailedEventArgs'
    _iid_ = Guid('{80fde3f4-54c4-42c0-8d19-cea1a87ca18b}')
    @winrt_commethod(6)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Code(self) -> UInt32: ...
    Code = property(get_Code, None)
    Message = property(get_Message, None)
class IMediaCaptureFocusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureFocusChangedEventArgs'
    _iid_ = Guid('{81e1bc7f-2277-493e-abee-d3f44ff98c04}')
    @winrt_commethod(6)
    def get_FocusState(self) -> win32more.Windows.Media.Devices.MediaCaptureFocusState: ...
    FocusState = property(get_FocusState, None)
class IMediaCaptureInitializationSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureInitializationSettings'
    _iid_ = Guid('{9782ba70-ea65-4900-9356-8ca887726884}')
    @winrt_commethod(6)
    def put_AudioDeviceId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_AudioDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_VideoDeviceId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_StreamingCaptureMode(self, value: win32more.Windows.Media.Capture.StreamingCaptureMode) -> Void: ...
    @winrt_commethod(11)
    def get_StreamingCaptureMode(self) -> win32more.Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_commethod(12)
    def put_PhotoCaptureSource(self, value: win32more.Windows.Media.Capture.PhotoCaptureSource) -> Void: ...
    @winrt_commethod(13)
    def get_PhotoCaptureSource(self) -> win32more.Windows.Media.Capture.PhotoCaptureSource: ...
    AudioDeviceId = property(get_AudioDeviceId, put_AudioDeviceId)
    PhotoCaptureSource = property(get_PhotoCaptureSource, put_PhotoCaptureSource)
    StreamingCaptureMode = property(get_StreamingCaptureMode, put_StreamingCaptureMode)
    VideoDeviceId = property(get_VideoDeviceId, put_VideoDeviceId)
class IMediaCaptureInitializationSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureInitializationSettings2'
    _iid_ = Guid('{404e0626-c9dc-43e9-aee4-e6bf1b57b44c}')
    @winrt_commethod(6)
    def put_MediaCategory(self, value: win32more.Windows.Media.Capture.MediaCategory) -> Void: ...
    @winrt_commethod(7)
    def get_MediaCategory(self) -> win32more.Windows.Media.Capture.MediaCategory: ...
    @winrt_commethod(8)
    def put_AudioProcessing(self, value: win32more.Windows.Media.AudioProcessing) -> Void: ...
    @winrt_commethod(9)
    def get_AudioProcessing(self) -> win32more.Windows.Media.AudioProcessing: ...
    AudioProcessing = property(get_AudioProcessing, put_AudioProcessing)
    MediaCategory = property(get_MediaCategory, put_MediaCategory)
class IMediaCaptureInitializationSettings3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureInitializationSettings3'
    _iid_ = Guid('{4160519d-be48-4730-8104-0cf6e9e97948}')
    @winrt_commethod(6)
    def put_AudioSource(self, value: win32more.Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_commethod(7)
    def get_AudioSource(self) -> win32more.Windows.Media.Core.IMediaSource: ...
    @winrt_commethod(8)
    def put_VideoSource(self, value: win32more.Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_commethod(9)
    def get_VideoSource(self) -> win32more.Windows.Media.Core.IMediaSource: ...
    AudioSource = property(get_AudioSource, put_AudioSource)
    VideoSource = property(get_VideoSource, put_VideoSource)
class IMediaCaptureInitializationSettings4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureInitializationSettings4'
    _iid_ = Guid('{f502a537-4cb7-4d28-95ed-4f9f012e0518}')
    @winrt_commethod(6)
    def get_VideoProfile(self) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfile: ...
    @winrt_commethod(7)
    def put_VideoProfile(self, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfile) -> Void: ...
    @winrt_commethod(8)
    def get_PreviewMediaDescription(self) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_commethod(9)
    def put_PreviewMediaDescription(self, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_commethod(10)
    def get_RecordMediaDescription(self) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_commethod(11)
    def put_RecordMediaDescription(self, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_commethod(12)
    def get_PhotoMediaDescription(self) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_commethod(13)
    def put_PhotoMediaDescription(self, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    PhotoMediaDescription = property(get_PhotoMediaDescription, put_PhotoMediaDescription)
    PreviewMediaDescription = property(get_PreviewMediaDescription, put_PreviewMediaDescription)
    RecordMediaDescription = property(get_RecordMediaDescription, put_RecordMediaDescription)
    VideoProfile = property(get_VideoProfile, put_VideoProfile)
class IMediaCaptureInitializationSettings5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureInitializationSettings5'
    _iid_ = Guid('{d5a2e3b8-2626-4e94-b7b3-5308a0f64b1a}')
    @winrt_commethod(6)
    def get_SourceGroup(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_commethod(7)
    def put_SourceGroup(self, value: win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup) -> Void: ...
    @winrt_commethod(8)
    def get_SharingMode(self) -> win32more.Windows.Media.Capture.MediaCaptureSharingMode: ...
    @winrt_commethod(9)
    def put_SharingMode(self, value: win32more.Windows.Media.Capture.MediaCaptureSharingMode) -> Void: ...
    @winrt_commethod(10)
    def get_MemoryPreference(self) -> win32more.Windows.Media.Capture.MediaCaptureMemoryPreference: ...
    @winrt_commethod(11)
    def put_MemoryPreference(self, value: win32more.Windows.Media.Capture.MediaCaptureMemoryPreference) -> Void: ...
    MemoryPreference = property(get_MemoryPreference, put_MemoryPreference)
    SharingMode = property(get_SharingMode, put_SharingMode)
    SourceGroup = property(get_SourceGroup, put_SourceGroup)
class IMediaCaptureInitializationSettings6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureInitializationSettings6'
    _iid_ = Guid('{b2e26b47-3db1-4d33-ab63-0ffa09056585}')
    @winrt_commethod(6)
    def get_AlwaysPlaySystemShutterSound(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AlwaysPlaySystemShutterSound(self, value: Boolean) -> Void: ...
    AlwaysPlaySystemShutterSound = property(get_AlwaysPlaySystemShutterSound, put_AlwaysPlaySystemShutterSound)
class IMediaCaptureInitializationSettings7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureInitializationSettings7'
    _iid_ = Guid('{41546967-f58a-5d82-9ef4-ed572fb5e34e}')
    @winrt_commethod(6)
    def get_DeviceUriPasswordCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def put_DeviceUriPasswordCredential(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_DeviceUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    DeviceUri = property(get_DeviceUri, put_DeviceUri)
    DeviceUriPasswordCredential = property(get_DeviceUriPasswordCredential, put_DeviceUriPasswordCredential)
class IMediaCapturePauseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCapturePauseResult'
    _iid_ = Guid('{aec47ca3-4477-4b04-a06f-2c1c5182fe9d}')
    @winrt_commethod(6)
    def get_LastFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_commethod(7)
    def get_RecordDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
class IMediaCaptureRelativePanelWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureRelativePanelWatcher'
    _iid_ = Guid('{7d896566-04be-5b89-b30e-bd34a9f12db0}')
    @winrt_commethod(6)
    def get_RelativePanel(self) -> win32more.Windows.Devices.Enumeration.Panel: ...
    @winrt_commethod(7)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCaptureRelativePanelWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    RelativePanel = property(get_RelativePanel, None)
    Changed = event()
class IMediaCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureSettings'
    _iid_ = Guid('{1d83aafe-6d45-4477-8dc4-ac5bc01c4091}')
    @winrt_commethod(6)
    def get_AudioDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_StreamingCaptureMode(self) -> win32more.Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_commethod(9)
    def get_PhotoCaptureSource(self) -> win32more.Windows.Media.Capture.PhotoCaptureSource: ...
    @winrt_commethod(10)
    def get_VideoDeviceCharacteristic(self) -> win32more.Windows.Media.Capture.VideoDeviceCharacteristic: ...
    AudioDeviceId = property(get_AudioDeviceId, None)
    PhotoCaptureSource = property(get_PhotoCaptureSource, None)
    StreamingCaptureMode = property(get_StreamingCaptureMode, None)
    VideoDeviceCharacteristic = property(get_VideoDeviceCharacteristic, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
class IMediaCaptureSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureSettings2'
    _iid_ = Guid('{6f9e7cfb-fa9f-4b13-9cbe-5ab94f1f3493}')
    @winrt_commethod(6)
    def get_ConcurrentRecordAndPhotoSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ConcurrentRecordAndPhotoSequenceSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CameraSoundRequiredForRegion(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Horizontal35mmEquivalentFocalLength(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(10)
    def get_PitchOffsetDegrees(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def get_Vertical35mmEquivalentFocalLength(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(12)
    def get_MediaCategory(self) -> win32more.Windows.Media.Capture.MediaCategory: ...
    @winrt_commethod(13)
    def get_AudioProcessing(self) -> win32more.Windows.Media.AudioProcessing: ...
    AudioProcessing = property(get_AudioProcessing, None)
    CameraSoundRequiredForRegion = property(get_CameraSoundRequiredForRegion, None)
    ConcurrentRecordAndPhotoSequenceSupported = property(get_ConcurrentRecordAndPhotoSequenceSupported, None)
    ConcurrentRecordAndPhotoSupported = property(get_ConcurrentRecordAndPhotoSupported, None)
    Horizontal35mmEquivalentFocalLength = property(get_Horizontal35mmEquivalentFocalLength, None)
    MediaCategory = property(get_MediaCategory, None)
    PitchOffsetDegrees = property(get_PitchOffsetDegrees, None)
    Vertical35mmEquivalentFocalLength = property(get_Vertical35mmEquivalentFocalLength, None)
class IMediaCaptureSettings3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureSettings3'
    _iid_ = Guid('{303c67c2-8058-4b1b-b877-8c2ef3528440}')
    @winrt_commethod(6)
    def get_Direct3D11Device(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    Direct3D11Device = property(get_Direct3D11Device, None)
class IMediaCaptureStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureStatics'
    _iid_ = Guid('{acef81ff-99ed-4645-965e-1925cfc63834}')
    @winrt_commethod(6)
    def IsVideoProfileSupported(self, videoDeviceId: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def FindAllVideoProfiles(self, videoDeviceId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_commethod(8)
    def FindConcurrentProfiles(self, videoDeviceId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_commethod(9)
    def FindKnownVideoProfiles(self, videoDeviceId: WinRT_String, name: win32more.Windows.Media.Capture.KnownVideoProfile) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
class IMediaCaptureStopResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureStopResult'
    _iid_ = Guid('{f9db6a2a-a092-4ad1-97d4-f201f9d082db}')
    @winrt_commethod(6)
    def get_LastFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_commethod(7)
    def get_RecordDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
class IMediaCaptureVideoPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureVideoPreview'
    _iid_ = Guid('{27727073-549e-447f-a20a-4f03c479d8c0}')
    @winrt_commethod(6)
    def StartPreviewAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StartPreviewToCustomSinkAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def StartPreviewToCustomSinkIdAsync(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def StopPreviewAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IMediaCaptureVideoProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureVideoProfile'
    _iid_ = Guid('{21a073bf-a3ee-4ecf-9ef6-50b0bc4e1305}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SupportedPreviewMediaDescription(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_commethod(9)
    def get_SupportedRecordMediaDescription(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_commethod(10)
    def get_SupportedPhotoMediaDescription(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_commethod(11)
    def GetConcurrency(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    Id = property(get_Id, None)
    SupportedPhotoMediaDescription = property(get_SupportedPhotoMediaDescription, None)
    SupportedPreviewMediaDescription = property(get_SupportedPreviewMediaDescription, None)
    SupportedRecordMediaDescription = property(get_SupportedRecordMediaDescription, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
class IMediaCaptureVideoProfile2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureVideoProfile2'
    _iid_ = Guid('{97ddc95f-94ce-468f-9316-fc5bc2638f6b}')
    @winrt_commethod(6)
    def get_FrameSourceInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    FrameSourceInfos = property(get_FrameSourceInfos, None)
    Properties = property(get_Properties, None)
class IMediaCaptureVideoProfileMediaDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription'
    _iid_ = Guid('{8012afef-b691-49ff-83f2-c1e76eaaea1b}')
    @winrt_commethod(6)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_FrameRate(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsVariablePhotoSequenceSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsHdrVideoSupported(self) -> Boolean: ...
    FrameRate = property(get_FrameRate, None)
    Height = property(get_Height, None)
    IsHdrVideoSupported = property(get_IsHdrVideoSupported, None)
    IsVariablePhotoSequenceSupported = property(get_IsVariablePhotoSequenceSupported, None)
    Width = property(get_Width, None)
class IMediaCaptureVideoProfileMediaDescription2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription2'
    _iid_ = Guid('{c6a6ef13-322d-413a-b85a-68a88e02f4e9}')
    @winrt_commethod(6)
    def get_Subtype(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Properties = property(get_Properties, None)
    Subtype = property(get_Subtype, None)
class IOptionalReferencePhotoCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IOptionalReferencePhotoCapturedEventArgs'
    _iid_ = Guid('{470f88b3-1e6d-4051-9c8b-f1d85af047b7}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Context(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Context = property(get_Context, None)
    Frame = property(get_Frame, None)
class IPhotoCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IPhotoCapturedEventArgs'
    _iid_ = Guid('{373bfbc1-984e-4ff0-bf85-1c00aabc5a45}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Thumbnail(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(8)
    def get_CaptureTimeOffset(self) -> win32more.Windows.Foundation.TimeSpan: ...
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
class IPhotoConfirmationCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IPhotoConfirmationCapturedEventArgs'
    _iid_ = Guid('{ab473672-c28a-4827-8f8d-3636d3beb51e}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_CaptureTimeOffset(self) -> win32more.Windows.Foundation.TimeSpan: ...
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    Frame = property(get_Frame, None)
class IScreenCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IScreenCapture'
    _iid_ = Guid('{89179ef7-cd12-4e0e-a6d4-5b3de98b2e9b}')
    @winrt_commethod(6)
    def get_AudioSource(self) -> win32more.Windows.Media.Core.IMediaSource: ...
    @winrt_commethod(7)
    def get_VideoSource(self) -> win32more.Windows.Media.Core.IMediaSource: ...
    @winrt_commethod(8)
    def get_IsAudioSuspended(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsVideoSuspended(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_SourceSuspensionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.ScreenCapture, win32more.Windows.Media.Capture.SourceSuspensionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SourceSuspensionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AudioSource = property(get_AudioSource, None)
    IsAudioSuspended = property(get_IsAudioSuspended, None)
    IsVideoSuspended = property(get_IsVideoSuspended, None)
    VideoSource = property(get_VideoSource, None)
    SourceSuspensionChanged = event()
class IScreenCaptureStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IScreenCaptureStatics'
    _iid_ = Guid('{c898c3b0-c8a5-11e2-8b8b-0800200c9a66}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Media.Capture.ScreenCapture: ...
class ISourceSuspensionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.ISourceSuspensionChangedEventArgs'
    _iid_ = Guid('{2ece7b5e-d49b-4394-bc32-f97d6cedec1c}')
    @winrt_commethod(6)
    def get_IsAudioSuspended(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsVideoSuspended(self) -> Boolean: ...
    IsAudioSuspended = property(get_IsAudioSuspended, None)
    IsVideoSuspended = property(get_IsVideoSuspended, None)
class IVideoStreamConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.IVideoStreamConfiguration'
    _iid_ = Guid('{d8770a6f-4390-4b5e-ad3e-0f8af0963490}')
    @winrt_commethod(6)
    def get_InputProperties(self) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(7)
    def get_OutputProperties(self) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    InputProperties = property(get_InputProperties, None)
    OutputProperties = property(get_OutputProperties, None)
class KnownVideoProfile(Enum, Int32):
    VideoRecording = 0
    HighQualityPhoto = 1
    BalancedVideoAndPhoto = 2
    VideoConferencing = 3
    PhotoSequence = 4
    HighFrameRate = 5
    VariablePhotoSequence = 6
    HdrWithWcgVideo = 7
    HdrWithWcgPhoto = 8
    VideoHdr8 = 9
    CompressedCamera = 10
class LowLagMediaRecording(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ILowLagMediaRecording
    _classid_ = 'Windows.Media.Capture.LowLagMediaRecording'
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Capture.ILowLagMediaRecording) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.Capture.ILowLagMediaRecording) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FinishAsync(self: win32more.Windows.Media.Capture.ILowLagMediaRecording) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseAsync(self: win32more.Windows.Media.Capture.ILowLagMediaRecording2, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResumeAsync(self: win32more.Windows.Media.Capture.ILowLagMediaRecording2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseWithResultAsync(self: win32more.Windows.Media.Capture.ILowLagMediaRecording3, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_mixinmethod
    def StopWithResultAsync(self: win32more.Windows.Media.Capture.ILowLagMediaRecording3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCaptureStopResult]: ...
class LowLagPhotoCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ILowLagPhotoCapture
    _classid_ = 'Windows.Media.Capture.LowLagPhotoCapture'
    @winrt_mixinmethod
    def CaptureAsync(self: win32more.Windows.Media.Capture.ILowLagPhotoCapture) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.CapturedPhoto]: ...
    @winrt_mixinmethod
    def FinishAsync(self: win32more.Windows.Media.Capture.ILowLagPhotoCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
class LowLagPhotoSequenceCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ILowLagPhotoSequenceCapture
    _classid_ = 'Windows.Media.Capture.LowLagPhotoSequenceCapture'
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Capture.ILowLagPhotoSequenceCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.Capture.ILowLagPhotoSequenceCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FinishAsync(self: win32more.Windows.Media.Capture.ILowLagPhotoSequenceCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_PhotoCaptured(self: win32more.Windows.Media.Capture.ILowLagPhotoSequenceCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.LowLagPhotoSequenceCapture, win32more.Windows.Media.Capture.PhotoCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PhotoCaptured(self: win32more.Windows.Media.Capture.ILowLagPhotoSequenceCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PhotoCaptured = event()
class MediaCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Capture.IMediaCapture
    _classid_ = 'Windows.Media.Capture.MediaCapture'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Capture.MediaCapture.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Capture.MediaCapture: ...
    @winrt_mixinmethod
    def InitializeAsync(self: win32more.Windows.Media.Capture.IMediaCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def InitializeWithSettingsAsync(self: win32more.Windows.Media.Capture.IMediaCapture, mediaCaptureInitializationSettings: win32more.Windows.Media.Capture.MediaCaptureInitializationSettings) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToStorageFileAsync(self: win32more.Windows.Media.Capture.IMediaCapture, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToStreamAsync(self: win32more.Windows.Media.Capture.IMediaCapture, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToCustomSinkAsync(self: win32more.Windows.Media.Capture.IMediaCapture, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToCustomSinkIdAsync(self: win32more.Windows.Media.Capture.IMediaCapture, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopRecordAsync(self: win32more.Windows.Media.Capture.IMediaCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CapturePhotoToStorageFileAsync(self: win32more.Windows.Media.Capture.IMediaCapture, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CapturePhotoToStreamAsync(self: win32more.Windows.Media.Capture.IMediaCapture, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def AddEffectAsync(self: win32more.Windows.Media.Capture.IMediaCapture, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, effectActivationID: WinRT_String, effectSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearEffectsAsync(self: win32more.Windows.Media.Capture.IMediaCapture, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetEncoderProperty(self: win32more.Windows.Media.Capture.IMediaCapture, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, propertyId: Guid, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def GetEncoderProperty(self: win32more.Windows.Media.Capture.IMediaCapture, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, propertyId: Guid) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def add_Failed(self: win32more.Windows.Media.Capture.IMediaCapture, errorEventHandler: win32more.Windows.Media.Capture.MediaCaptureFailedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Failed(self: win32more.Windows.Media.Capture.IMediaCapture, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RecordLimitationExceeded(self: win32more.Windows.Media.Capture.IMediaCapture, recordLimitationExceededEventHandler: win32more.Windows.Media.Capture.RecordLimitationExceededEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecordLimitationExceeded(self: win32more.Windows.Media.Capture.IMediaCapture, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MediaCaptureSettings(self: win32more.Windows.Media.Capture.IMediaCapture) -> win32more.Windows.Media.Capture.MediaCaptureSettings: ...
    @winrt_mixinmethod
    def get_AudioDeviceController(self: win32more.Windows.Media.Capture.IMediaCapture) -> win32more.Windows.Media.Devices.AudioDeviceController: ...
    @winrt_mixinmethod
    def get_VideoDeviceController(self: win32more.Windows.Media.Capture.IMediaCapture) -> win32more.Windows.Media.Devices.VideoDeviceController: ...
    @winrt_mixinmethod
    def SetPreviewMirroring(self: win32more.Windows.Media.Capture.IMediaCapture, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPreviewMirroring(self: win32more.Windows.Media.Capture.IMediaCapture) -> Boolean: ...
    @winrt_mixinmethod
    def SetPreviewRotation(self: win32more.Windows.Media.Capture.IMediaCapture, value: win32more.Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_mixinmethod
    def GetPreviewRotation(self: win32more.Windows.Media.Capture.IMediaCapture) -> win32more.Windows.Media.Capture.VideoRotation: ...
    @winrt_mixinmethod
    def SetRecordRotation(self: win32more.Windows.Media.Capture.IMediaCapture, value: win32more.Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_mixinmethod
    def GetRecordRotation(self: win32more.Windows.Media.Capture.IMediaCapture) -> win32more.Windows.Media.Capture.VideoRotation: ...
    @winrt_mixinmethod
    def StartPreviewAsync(self: win32more.Windows.Media.Capture.IMediaCaptureVideoPreview) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartPreviewToCustomSinkAsync(self: win32more.Windows.Media.Capture.IMediaCaptureVideoPreview, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartPreviewToCustomSinkIdAsync(self: win32more.Windows.Media.Capture.IMediaCaptureVideoPreview, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopPreviewAsync(self: win32more.Windows.Media.Capture.IMediaCaptureVideoPreview) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToStorageFileAsync(self: win32more.Windows.Media.Capture.IMediaCapture2, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToStreamAsync(self: win32more.Windows.Media.Capture.IMediaCapture2, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToCustomSinkAsync(self: win32more.Windows.Media.Capture.IMediaCapture2, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToCustomSinkIdAsync(self: win32more.Windows.Media.Capture.IMediaCapture2, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagPhotoCaptureAsync(self: win32more.Windows.Media.Capture.IMediaCapture2, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagPhotoCapture]: ...
    @winrt_mixinmethod
    def PrepareLowLagPhotoSequenceCaptureAsync(self: win32more.Windows.Media.Capture.IMediaCapture2, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.LowLagPhotoSequenceCapture]: ...
    @winrt_mixinmethod
    def SetEncodingPropertiesAsync(self: win32more.Windows.Media.Capture.IMediaCapture2, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties, encoderProperties: win32more.Windows.Media.MediaProperties.MediaPropertySet) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def PrepareVariablePhotoSequenceCaptureAsync(self: win32more.Windows.Media.Capture.IMediaCapture3, type: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture]: ...
    @winrt_mixinmethod
    def add_FocusChanged(self: win32more.Windows.Media.Capture.IMediaCapture3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Media.Capture.MediaCaptureFocusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FocusChanged(self: win32more.Windows.Media.Capture.IMediaCapture3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PhotoConfirmationCaptured(self: win32more.Windows.Media.Capture.IMediaCapture3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Media.Capture.PhotoConfirmationCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PhotoConfirmationCaptured(self: win32more.Windows.Media.Capture.IMediaCapture3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddAudioEffectAsync(self: win32more.Windows.Media.Capture.IMediaCapture4, definition: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.IMediaExtension]: ...
    @winrt_mixinmethod
    def AddVideoEffectAsync(self: win32more.Windows.Media.Capture.IMediaCapture4, definition: win32more.Windows.Media.Effects.IVideoEffectDefinition, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.IMediaExtension]: ...
    @winrt_mixinmethod
    def PauseRecordAsync(self: win32more.Windows.Media.Capture.IMediaCapture4, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResumeRecordAsync(self: win32more.Windows.Media.Capture.IMediaCapture4) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_CameraStreamStateChanged(self: win32more.Windows.Media.Capture.IMediaCapture4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraStreamStateChanged(self: win32more.Windows.Media.Capture.IMediaCapture4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CameraStreamState(self: win32more.Windows.Media.Capture.IMediaCapture4) -> win32more.Windows.Media.Devices.CameraStreamState: ...
    @winrt_mixinmethod
    def GetPreviewFrameAsync(self: win32more.Windows.Media.Capture.IMediaCapture4) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.VideoFrame]: ...
    @winrt_mixinmethod
    def GetPreviewFrameCopyAsync(self: win32more.Windows.Media.Capture.IMediaCapture4, destination: win32more.Windows.Media.VideoFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.VideoFrame]: ...
    @winrt_mixinmethod
    def add_ThermalStatusChanged(self: win32more.Windows.Media.Capture.IMediaCapture4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ThermalStatusChanged(self: win32more.Windows.Media.Capture.IMediaCapture4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ThermalStatus(self: win32more.Windows.Media.Capture.IMediaCapture4) -> win32more.Windows.Media.Capture.MediaCaptureThermalStatus: ...
    @winrt_mixinmethod
    def PrepareAdvancedPhotoCaptureAsync(self: win32more.Windows.Media.Capture.IMediaCapture4, encodingProperties: win32more.Windows.Media.MediaProperties.ImageEncodingProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.AdvancedPhotoCapture]: ...
    @winrt_mixinmethod
    def RemoveEffectAsync(self: win32more.Windows.Media.Capture.IMediaCapture5, effect: win32more.Windows.Media.IMediaExtension) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseRecordWithResultAsync(self: win32more.Windows.Media.Capture.IMediaCapture5, behavior: win32more.Windows.Media.Devices.MediaCapturePauseBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_mixinmethod
    def StopRecordWithResultAsync(self: win32more.Windows.Media.Capture.IMediaCapture5) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.MediaCaptureStopResult]: ...
    @winrt_mixinmethod
    def get_FrameSources(self: win32more.Windows.Media.Capture.IMediaCapture5) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Media.Capture.Frames.MediaFrameSource]: ...
    @winrt_mixinmethod
    def CreateFrameReaderAsync(self: win32more.Windows.Media.Capture.IMediaCapture5, inputSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithSubtypeAsync(self: win32more.Windows.Media.Capture.IMediaCapture5, inputSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithSubtypeAndSizeAsync(self: win32more.Windows.Media.Capture.IMediaCapture5, inputSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String, outputSize: win32more.Windows.Graphics.Imaging.BitmapSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_mixinmethod
    def add_CaptureDeviceExclusiveControlStatusChanged(self: win32more.Windows.Media.Capture.IMediaCapture6, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCapture, win32more.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CaptureDeviceExclusiveControlStatusChanged(self: win32more.Windows.Media.Capture.IMediaCapture6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateMultiSourceFrameReaderAsync(self: win32more.Windows.Media.Capture.IMediaCapture6, inputSources: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Capture.Frames.MediaFrameSource]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReader]: ...
    @winrt_mixinmethod
    def CreateRelativePanelWatcher(self: win32more.Windows.Media.Capture.IMediaCapture7, captureMode: win32more.Windows.Media.Capture.StreamingCaptureMode, displayRegion: win32more.Windows.UI.WindowManagement.DisplayRegion) -> win32more.Windows.Media.Capture.MediaCaptureRelativePanelWatcher: ...
    @winrt_classmethod
    def IsVideoProfileSupported(cls: win32more.Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def FindAllVideoProfiles(cls: win32more.Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_classmethod
    def FindConcurrentProfiles(cls: win32more.Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_classmethod
    def FindKnownVideoProfiles(cls: win32more.Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String, name: win32more.Windows.Media.Capture.KnownVideoProfile) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    AudioDeviceController = property(get_AudioDeviceController, None)
    CameraStreamState = property(get_CameraStreamState, None)
    FrameSources = property(get_FrameSources, None)
    MediaCaptureSettings = property(get_MediaCaptureSettings, None)
    ThermalStatus = property(get_ThermalStatus, None)
    VideoDeviceController = property(get_VideoDeviceController, None)
    Failed = event()
    RecordLimitationExceeded = event()
    FocusChanged = event()
    PhotoConfirmationCaptured = event()
    CameraStreamStateChanged = event()
    ThermalStatusChanged = event()
    CaptureDeviceExclusiveControlStatusChanged = event()
class MediaCaptureDeviceExclusiveControlReleaseMode(Enum, Int32):
    OnDispose = 0
    OnAllStreamsStopped = 1
class MediaCaptureDeviceExclusiveControlStatus(Enum, Int32):
    ExclusiveControlAvailable = 0
    SharedReadOnlyAvailable = 1
class MediaCaptureDeviceExclusiveControlStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs
    _classid_ = 'Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Capture.IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs) -> win32more.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatus: ...
    DeviceId = property(get_DeviceId, None)
    Status = property(get_Status, None)
class MediaCaptureFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureFailedEventArgs
    _classid_ = 'Windows.Media.Capture.MediaCaptureFailedEventArgs'
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Media.Capture.IMediaCaptureFailedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Code(self: win32more.Windows.Media.Capture.IMediaCaptureFailedEventArgs) -> UInt32: ...
    Code = property(get_Code, None)
    Message = property(get_Message, None)
class MediaCaptureFailedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2014effb-5cd8-4f08-a314-0d360da59f14}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Capture.MediaCapture, errorEventArgs: win32more.Windows.Media.Capture.MediaCaptureFailedEventArgs) -> Void: ...
class MediaCaptureFocusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureFocusChangedEventArgs
    _classid_ = 'Windows.Media.Capture.MediaCaptureFocusChangedEventArgs'
    @winrt_mixinmethod
    def get_FocusState(self: win32more.Windows.Media.Capture.IMediaCaptureFocusChangedEventArgs) -> win32more.Windows.Media.Devices.MediaCaptureFocusState: ...
    FocusState = property(get_FocusState, None)
class MediaCaptureInitializationSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings
    _classid_ = 'Windows.Media.Capture.MediaCaptureInitializationSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Capture.MediaCaptureInitializationSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Capture.MediaCaptureInitializationSettings: ...
    @winrt_mixinmethod
    def put_AudioDeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AudioDeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_VideoDeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StreamingCaptureMode(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings, value: win32more.Windows.Media.Capture.StreamingCaptureMode) -> Void: ...
    @winrt_mixinmethod
    def get_StreamingCaptureMode(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings) -> win32more.Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_mixinmethod
    def put_PhotoCaptureSource(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings, value: win32more.Windows.Media.Capture.PhotoCaptureSource) -> Void: ...
    @winrt_mixinmethod
    def get_PhotoCaptureSource(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings) -> win32more.Windows.Media.Capture.PhotoCaptureSource: ...
    @winrt_mixinmethod
    def put_MediaCategory(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings2, value: win32more.Windows.Media.Capture.MediaCategory) -> Void: ...
    @winrt_mixinmethod
    def get_MediaCategory(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings2) -> win32more.Windows.Media.Capture.MediaCategory: ...
    @winrt_mixinmethod
    def put_AudioProcessing(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings2, value: win32more.Windows.Media.AudioProcessing) -> Void: ...
    @winrt_mixinmethod
    def get_AudioProcessing(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings2) -> win32more.Windows.Media.AudioProcessing: ...
    @winrt_mixinmethod
    def put_AudioSource(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings3, value: win32more.Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_mixinmethod
    def get_AudioSource(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings3) -> win32more.Windows.Media.Core.IMediaSource: ...
    @winrt_mixinmethod
    def put_VideoSource(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings3, value: win32more.Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_mixinmethod
    def get_VideoSource(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings3) -> win32more.Windows.Media.Core.IMediaSource: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfile: ...
    @winrt_mixinmethod
    def put_VideoProfile(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfile) -> Void: ...
    @winrt_mixinmethod
    def get_PreviewMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_mixinmethod
    def put_PreviewMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_mixinmethod
    def get_RecordMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_mixinmethod
    def put_RecordMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_mixinmethod
    def get_PhotoMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_mixinmethod
    def put_PhotoMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_mixinmethod
    def get_SourceGroup(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings5) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_mixinmethod
    def put_SourceGroup(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings5, value: win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings5) -> win32more.Windows.Media.Capture.MediaCaptureSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings5, value: win32more.Windows.Media.Capture.MediaCaptureSharingMode) -> Void: ...
    @winrt_mixinmethod
    def get_MemoryPreference(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings5) -> win32more.Windows.Media.Capture.MediaCaptureMemoryPreference: ...
    @winrt_mixinmethod
    def put_MemoryPreference(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings5, value: win32more.Windows.Media.Capture.MediaCaptureMemoryPreference) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysPlaySystemShutterSound(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings6) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysPlaySystemShutterSound(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceUriPasswordCredential(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings7) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_DeviceUriPasswordCredential(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings7, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceUri(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings7) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_DeviceUri(self: win32more.Windows.Media.Capture.IMediaCaptureInitializationSettings7, value: win32more.Windows.Foundation.Uri) -> Void: ...
    AlwaysPlaySystemShutterSound = property(get_AlwaysPlaySystemShutterSound, put_AlwaysPlaySystemShutterSound)
    AudioDeviceId = property(get_AudioDeviceId, put_AudioDeviceId)
    AudioProcessing = property(get_AudioProcessing, put_AudioProcessing)
    AudioSource = property(get_AudioSource, put_AudioSource)
    DeviceUri = property(get_DeviceUri, put_DeviceUri)
    DeviceUriPasswordCredential = property(get_DeviceUriPasswordCredential, put_DeviceUriPasswordCredential)
    MediaCategory = property(get_MediaCategory, put_MediaCategory)
    MemoryPreference = property(get_MemoryPreference, put_MemoryPreference)
    PhotoCaptureSource = property(get_PhotoCaptureSource, put_PhotoCaptureSource)
    PhotoMediaDescription = property(get_PhotoMediaDescription, put_PhotoMediaDescription)
    PreviewMediaDescription = property(get_PreviewMediaDescription, put_PreviewMediaDescription)
    RecordMediaDescription = property(get_RecordMediaDescription, put_RecordMediaDescription)
    SharingMode = property(get_SharingMode, put_SharingMode)
    SourceGroup = property(get_SourceGroup, put_SourceGroup)
    StreamingCaptureMode = property(get_StreamingCaptureMode, put_StreamingCaptureMode)
    VideoDeviceId = property(get_VideoDeviceId, put_VideoDeviceId)
    VideoProfile = property(get_VideoProfile, put_VideoProfile)
    VideoSource = property(get_VideoSource, put_VideoSource)
class MediaCaptureMemoryPreference(Enum, Int32):
    Auto = 0
    Cpu = 1
class MediaCapturePauseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Capture.IMediaCapturePauseResult
    _classid_ = 'Windows.Media.Capture.MediaCapturePauseResult'
    @winrt_mixinmethod
    def get_LastFrame(self: win32more.Windows.Media.Capture.IMediaCapturePauseResult) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_RecordDuration(self: win32more.Windows.Media.Capture.IMediaCapturePauseResult) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
class MediaCaptureRelativePanelWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureRelativePanelWatcher
    _classid_ = 'Windows.Media.Capture.MediaCaptureRelativePanelWatcher'
    @winrt_mixinmethod
    def get_RelativePanel(self: win32more.Windows.Media.Capture.IMediaCaptureRelativePanelWatcher) -> win32more.Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.Media.Capture.IMediaCaptureRelativePanelWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.MediaCaptureRelativePanelWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.Media.Capture.IMediaCaptureRelativePanelWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Capture.IMediaCaptureRelativePanelWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Media.Capture.IMediaCaptureRelativePanelWatcher) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    RelativePanel = property(get_RelativePanel, None)
    Changed = event()
class MediaCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureSettings
    _classid_ = 'Windows.Media.Capture.MediaCaptureSettings'
    @winrt_mixinmethod
    def get_AudioDeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StreamingCaptureMode(self: win32more.Windows.Media.Capture.IMediaCaptureSettings) -> win32more.Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_mixinmethod
    def get_PhotoCaptureSource(self: win32more.Windows.Media.Capture.IMediaCaptureSettings) -> win32more.Windows.Media.Capture.PhotoCaptureSource: ...
    @winrt_mixinmethod
    def get_VideoDeviceCharacteristic(self: win32more.Windows.Media.Capture.IMediaCaptureSettings) -> win32more.Windows.Media.Capture.VideoDeviceCharacteristic: ...
    @winrt_mixinmethod
    def get_ConcurrentRecordAndPhotoSupported(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ConcurrentRecordAndPhotoSequenceSupported(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CameraSoundRequiredForRegion(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Horizontal35mmEquivalentFocalLength(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_PitchOffsetDegrees(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_Vertical35mmEquivalentFocalLength(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_MediaCategory(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> win32more.Windows.Media.Capture.MediaCategory: ...
    @winrt_mixinmethod
    def get_AudioProcessing(self: win32more.Windows.Media.Capture.IMediaCaptureSettings2) -> win32more.Windows.Media.AudioProcessing: ...
    @winrt_mixinmethod
    def get_Direct3D11Device(self: win32more.Windows.Media.Capture.IMediaCaptureSettings3) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    AudioDeviceId = property(get_AudioDeviceId, None)
    AudioProcessing = property(get_AudioProcessing, None)
    CameraSoundRequiredForRegion = property(get_CameraSoundRequiredForRegion, None)
    ConcurrentRecordAndPhotoSequenceSupported = property(get_ConcurrentRecordAndPhotoSequenceSupported, None)
    ConcurrentRecordAndPhotoSupported = property(get_ConcurrentRecordAndPhotoSupported, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
    Horizontal35mmEquivalentFocalLength = property(get_Horizontal35mmEquivalentFocalLength, None)
    MediaCategory = property(get_MediaCategory, None)
    PhotoCaptureSource = property(get_PhotoCaptureSource, None)
    PitchOffsetDegrees = property(get_PitchOffsetDegrees, None)
    StreamingCaptureMode = property(get_StreamingCaptureMode, None)
    Vertical35mmEquivalentFocalLength = property(get_Vertical35mmEquivalentFocalLength, None)
    VideoDeviceCharacteristic = property(get_VideoDeviceCharacteristic, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
class MediaCaptureSharingMode(Enum, Int32):
    ExclusiveControl = 0
    SharedReadOnly = 1
class MediaCaptureStopResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureStopResult
    _classid_ = 'Windows.Media.Capture.MediaCaptureStopResult'
    @winrt_mixinmethod
    def get_LastFrame(self: win32more.Windows.Media.Capture.IMediaCaptureStopResult) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_RecordDuration(self: win32more.Windows.Media.Capture.IMediaCaptureStopResult) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
class MediaCaptureThermalStatus(Enum, Int32):
    Normal = 0
    Overheated = 1
class MediaCaptureVideoProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile
    _classid_ = 'Windows.Media.Capture.MediaCaptureVideoProfile'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedPreviewMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def get_SupportedRecordMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def get_SupportedPhotoMediaDescription(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def GetConcurrency(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_mixinmethod
    def get_FrameSourceInfos(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfile2) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    FrameSourceInfos = property(get_FrameSourceInfos, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
    SupportedPhotoMediaDescription = property(get_SupportedPhotoMediaDescription, None)
    SupportedPreviewMediaDescription = property(get_SupportedPreviewMediaDescription, None)
    SupportedRecordMediaDescription = property(get_SupportedRecordMediaDescription, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
class MediaCaptureVideoProfileMediaDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription
    _classid_ = 'Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription'
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_FrameRate(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> Double: ...
    @winrt_mixinmethod
    def get_IsVariablePhotoSequenceSupported(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHdrVideoSupported(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_Subtype(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription2) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    FrameRate = property(get_FrameRate, None)
    Height = property(get_Height, None)
    IsHdrVideoSupported = property(get_IsHdrVideoSupported, None)
    IsVariablePhotoSequenceSupported = property(get_IsVariablePhotoSequenceSupported, None)
    Properties = property(get_Properties, None)
    Subtype = property(get_Subtype, None)
    Width = property(get_Width, None)
class MediaCategory(Enum, Int32):
    Other = 0
    Communications = 1
    Media = 2
    GameChat = 3
    Speech = 4
    FarFieldSpeech = 5
    UniformSpeech = 6
    VoiceTyping = 7
class MediaStreamType(Enum, Int32):
    VideoPreview = 0
    VideoRecord = 1
    Audio = 2
    Photo = 3
    Metadata = 4
class OptionalReferencePhotoCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IOptionalReferencePhotoCapturedEventArgs
    _classid_ = 'Windows.Media.Capture.OptionalReferencePhotoCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Capture.IOptionalReferencePhotoCapturedEventArgs) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Context(self: win32more.Windows.Media.Capture.IOptionalReferencePhotoCapturedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Context = property(get_Context, None)
    Frame = property(get_Frame, None)
class PhotoCaptureSource(Enum, Int32):
    Auto = 0
    VideoPreview = 1
    Photo = 2
class PhotoCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IPhotoCapturedEventArgs
    _classid_ = 'Windows.Media.Capture.PhotoCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Capture.IPhotoCapturedEventArgs) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Capture.IPhotoCapturedEventArgs) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_CaptureTimeOffset(self: win32more.Windows.Media.Capture.IPhotoCapturedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
class PhotoConfirmationCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IPhotoConfirmationCapturedEventArgs
    _classid_ = 'Windows.Media.Capture.PhotoConfirmationCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Capture.IPhotoConfirmationCapturedEventArgs) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_CaptureTimeOffset(self: win32more.Windows.Media.Capture.IPhotoConfirmationCapturedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    Frame = property(get_Frame, None)
class PowerlineFrequency(Enum, Int32):
    Disabled = 0
    FiftyHertz = 1
    SixtyHertz = 2
    Auto = 3
class RecordLimitationExceededEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3fae8f2e-4fe1-4ffd-aaba-e1f1337d4e53}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Capture.MediaCapture) -> Void: ...
class ScreenCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IScreenCapture
    _classid_ = 'Windows.Media.Capture.ScreenCapture'
    @winrt_mixinmethod
    def get_AudioSource(self: win32more.Windows.Media.Capture.IScreenCapture) -> win32more.Windows.Media.Core.IMediaSource: ...
    @winrt_mixinmethod
    def get_VideoSource(self: win32more.Windows.Media.Capture.IScreenCapture) -> win32more.Windows.Media.Core.IMediaSource: ...
    @winrt_mixinmethod
    def get_IsAudioSuspended(self: win32more.Windows.Media.Capture.IScreenCapture) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVideoSuspended(self: win32more.Windows.Media.Capture.IScreenCapture) -> Boolean: ...
    @winrt_mixinmethod
    def add_SourceSuspensionChanged(self: win32more.Windows.Media.Capture.IScreenCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.ScreenCapture, win32more.Windows.Media.Capture.SourceSuspensionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceSuspensionChanged(self: win32more.Windows.Media.Capture.IScreenCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Media.Capture.IScreenCaptureStatics) -> win32more.Windows.Media.Capture.ScreenCapture: ...
    AudioSource = property(get_AudioSource, None)
    IsAudioSuspended = property(get_IsAudioSuspended, None)
    IsVideoSuspended = property(get_IsVideoSuspended, None)
    VideoSource = property(get_VideoSource, None)
    SourceSuspensionChanged = event()
class SourceSuspensionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.ISourceSuspensionChangedEventArgs
    _classid_ = 'Windows.Media.Capture.SourceSuspensionChangedEventArgs'
    @winrt_mixinmethod
    def get_IsAudioSuspended(self: win32more.Windows.Media.Capture.ISourceSuspensionChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVideoSuspended(self: win32more.Windows.Media.Capture.ISourceSuspensionChangedEventArgs) -> Boolean: ...
    IsAudioSuspended = property(get_IsAudioSuspended, None)
    IsVideoSuspended = property(get_IsVideoSuspended, None)
class StreamingCaptureMode(Enum, Int32):
    AudioAndVideo = 0
    Audio = 1
    Video = 2
class VideoDeviceCharacteristic(Enum, Int32):
    AllStreamsIndependent = 0
    PreviewRecordStreamsIdentical = 1
    PreviewPhotoStreamsIdentical = 2
    RecordPhotoStreamsIdentical = 3
    AllStreamsIdentical = 4
class VideoRotation(Enum, Int32):
    None_ = 0
    Clockwise90Degrees = 1
    Clockwise180Degrees = 2
    Clockwise270Degrees = 3
class VideoStreamConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.IVideoStreamConfiguration
    _classid_ = 'Windows.Media.Capture.VideoStreamConfiguration'
    @winrt_mixinmethod
    def get_InputProperties(self: win32more.Windows.Media.Capture.IVideoStreamConfiguration) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def get_OutputProperties(self: win32more.Windows.Media.Capture.IVideoStreamConfiguration) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    InputProperties = property(get_InputProperties, None)
    OutputProperties = property(get_OutputProperties, None)
class WhiteBalanceGain(Structure):
    R: Double
    G: Double
    B: Double


make_ready(__name__)
