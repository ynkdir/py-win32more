from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Devices
import win32more.Windows.Media.Devices.Core
import win32more.Windows.Media.Effects
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AdvancedPhotoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IAdvancedPhotoCaptureSettings
    _classid_ = 'Windows.Media.Devices.AdvancedPhotoCaptureSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Devices.AdvancedPhotoCaptureSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Devices.AdvancedPhotoCaptureSettings: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IAdvancedPhotoCaptureSettings) -> win32more.Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Devices.IAdvancedPhotoCaptureSettings, value: win32more.Windows.Media.Devices.AdvancedPhotoMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class AdvancedPhotoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IAdvancedPhotoControl
    _classid_ = 'Windows.Media.Devices.AdvancedPhotoControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IAdvancedPhotoControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.IAdvancedPhotoControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AdvancedPhotoMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IAdvancedPhotoControl) -> win32more.Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_mixinmethod
    def Configure(self: win32more.Windows.Media.Devices.IAdvancedPhotoControl, settings: win32more.Windows.Media.Devices.AdvancedPhotoCaptureSettings) -> Void: ...
    Mode = property(get_Mode, None)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class AdvancedPhotoMode(Enum, Int32):
    Auto = 0
    Standard = 1
    Hdr = 2
    LowLight = 3
class AudioDeviceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IAudioDeviceController
    _classid_ = 'Windows.Media.Devices.AudioDeviceController'
    @winrt_mixinmethod
    def put_Muted(self: win32more.Windows.Media.Devices.IAudioDeviceController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Muted(self: win32more.Windows.Media.Devices.IAudioDeviceController) -> Boolean: ...
    @winrt_mixinmethod
    def put_VolumePercent(self: win32more.Windows.Media.Devices.IAudioDeviceController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_VolumePercent(self: win32more.Windows.Media.Devices.IAudioDeviceController) -> Single: ...
    @winrt_mixinmethod
    def GetAvailableMediaStreamProperties(self: win32more.Windows.Media.Devices.IMediaDeviceController, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.MediaProperties.IMediaEncodingProperties]: ...
    @winrt_mixinmethod
    def GetMediaStreamProperties(self: win32more.Windows.Media.Devices.IMediaDeviceController, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Media.MediaProperties.IMediaEncodingProperties: ...
    @winrt_mixinmethod
    def SetMediaStreamPropertiesAsync(self: win32more.Windows.Media.Devices.IMediaDeviceController, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_AudioCaptureEffectsManager(self: win32more.Windows.Media.Devices.IAudioDeviceController2) -> win32more.Windows.Media.Effects.AudioCaptureEffectsManager: ...
    AudioCaptureEffectsManager = property(get_AudioCaptureEffectsManager, None)
    Muted = property(get_Muted, put_Muted)
    VolumePercent = property(get_VolumePercent, put_VolumePercent)
class AudioDeviceModule(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IAudioDeviceModule
    _classid_ = 'Windows.Media.Devices.AudioDeviceModule'
    @winrt_mixinmethod
    def get_ClassId(self: win32more.Windows.Media.Devices.IAudioDeviceModule) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.Devices.IAudioDeviceModule) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.Media.Devices.IAudioDeviceModule) -> UInt32: ...
    @winrt_mixinmethod
    def get_MajorVersion(self: win32more.Windows.Media.Devices.IAudioDeviceModule) -> UInt32: ...
    @winrt_mixinmethod
    def get_MinorVersion(self: win32more.Windows.Media.Devices.IAudioDeviceModule) -> UInt32: ...
    @winrt_mixinmethod
    def SendCommandAsync(self: win32more.Windows.Media.Devices.IAudioDeviceModule, Command: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Devices.ModuleCommandResult]: ...
    ClassId = property(get_ClassId, None)
    DisplayName = property(get_DisplayName, None)
    InstanceId = property(get_InstanceId, None)
    MajorVersion = property(get_MajorVersion, None)
    MinorVersion = property(get_MinorVersion, None)
class AudioDeviceModuleNotificationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IAudioDeviceModuleNotificationEventArgs
    _classid_ = 'Windows.Media.Devices.AudioDeviceModuleNotificationEventArgs'
    @winrt_mixinmethod
    def get_Module(self: win32more.Windows.Media.Devices.IAudioDeviceModuleNotificationEventArgs) -> win32more.Windows.Media.Devices.AudioDeviceModule: ...
    @winrt_mixinmethod
    def get_NotificationData(self: win32more.Windows.Media.Devices.IAudioDeviceModuleNotificationEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Module = property(get_Module, None)
    NotificationData = property(get_NotificationData, None)
class AudioDeviceModulesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IAudioDeviceModulesManager
    _classid_ = 'Windows.Media.Devices.AudioDeviceModulesManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Devices.AudioDeviceModulesManager.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Devices.IAudioDeviceModulesManagerFactory, deviceId: WinRT_String) -> win32more.Windows.Media.Devices.AudioDeviceModulesManager: ...
    @winrt_mixinmethod
    def add_ModuleNotificationReceived(self: win32more.Windows.Media.Devices.IAudioDeviceModulesManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Devices.AudioDeviceModulesManager, win32more.Windows.Media.Devices.AudioDeviceModuleNotificationEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ModuleNotificationReceived(self: win32more.Windows.Media.Devices.IAudioDeviceModulesManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindAllById(self: win32more.Windows.Media.Devices.IAudioDeviceModulesManager, moduleId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AudioDeviceModule]: ...
    @winrt_mixinmethod
    def FindAll(self: win32more.Windows.Media.Devices.IAudioDeviceModulesManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AudioDeviceModule]: ...
    ModuleNotificationReceived = event()
class AudioDeviceRole(Enum, Int32):
    Default = 0
    Communications = 1
class AutoFocusRange(Enum, Int32):
    FullRange = 0
    Macro = 1
    Normal = 2
class CallControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ICallControl
    _classid_ = 'Windows.Media.Devices.CallControl'
    @winrt_mixinmethod
    def IndicateNewIncomingCall(self: win32more.Windows.Media.Devices.ICallControl, enableRinger: Boolean, callerId: WinRT_String) -> UInt64: ...
    @winrt_mixinmethod
    def IndicateNewOutgoingCall(self: win32more.Windows.Media.Devices.ICallControl) -> UInt64: ...
    @winrt_mixinmethod
    def IndicateActiveCall(self: win32more.Windows.Media.Devices.ICallControl, callToken: UInt64) -> Void: ...
    @winrt_mixinmethod
    def EndCall(self: win32more.Windows.Media.Devices.ICallControl, callToken: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_HasRinger(self: win32more.Windows.Media.Devices.ICallControl) -> Boolean: ...
    @winrt_mixinmethod
    def add_AnswerRequested(self: win32more.Windows.Media.Devices.ICallControl, handler: win32more.Windows.Media.Devices.CallControlEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AnswerRequested(self: win32more.Windows.Media.Devices.ICallControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HangUpRequested(self: win32more.Windows.Media.Devices.ICallControl, handler: win32more.Windows.Media.Devices.CallControlEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HangUpRequested(self: win32more.Windows.Media.Devices.ICallControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DialRequested(self: win32more.Windows.Media.Devices.ICallControl, handler: win32more.Windows.Media.Devices.DialRequestedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DialRequested(self: win32more.Windows.Media.Devices.ICallControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RedialRequested(self: win32more.Windows.Media.Devices.ICallControl, handler: win32more.Windows.Media.Devices.RedialRequestedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RedialRequested(self: win32more.Windows.Media.Devices.ICallControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeypadPressed(self: win32more.Windows.Media.Devices.ICallControl, handler: win32more.Windows.Media.Devices.KeypadPressedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeypadPressed(self: win32more.Windows.Media.Devices.ICallControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AudioTransferRequested(self: win32more.Windows.Media.Devices.ICallControl, handler: win32more.Windows.Media.Devices.CallControlEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioTransferRequested(self: win32more.Windows.Media.Devices.ICallControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Media.Devices.ICallControlStatics) -> win32more.Windows.Media.Devices.CallControl: ...
    @winrt_classmethod
    def FromId(cls: win32more.Windows.Media.Devices.ICallControlStatics, deviceId: WinRT_String) -> win32more.Windows.Media.Devices.CallControl: ...
    HasRinger = property(get_HasRinger, None)
    AnswerRequested = event()
    HangUpRequested = event()
    DialRequested = event()
    RedialRequested = event()
    KeypadPressed = event()
    AudioTransferRequested = event()
CallControlContract: UInt32 = 65536
class CallControlEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{596f759f-50df-4454-bc63-4d3d01b61958}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Devices.CallControl) -> Void: ...
class CameraOcclusionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ICameraOcclusionInfo
    _classid_ = 'Windows.Media.Devices.CameraOcclusionInfo'
    @winrt_mixinmethod
    def GetState(self: win32more.Windows.Media.Devices.ICameraOcclusionInfo) -> win32more.Windows.Media.Devices.CameraOcclusionState: ...
    @winrt_mixinmethod
    def IsOcclusionKindSupported(self: win32more.Windows.Media.Devices.ICameraOcclusionInfo, occlusionKind: win32more.Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Media.Devices.ICameraOcclusionInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Devices.CameraOcclusionInfo, win32more.Windows.Media.Devices.CameraOcclusionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Media.Devices.ICameraOcclusionInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    StateChanged = event()
class CameraOcclusionKind(Enum, Int32):
    Lid = 0
    CameraHardware = 1
class CameraOcclusionState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ICameraOcclusionState
    _classid_ = 'Windows.Media.Devices.CameraOcclusionState'
    @winrt_mixinmethod
    def get_IsOccluded(self: win32more.Windows.Media.Devices.ICameraOcclusionState) -> Boolean: ...
    @winrt_mixinmethod
    def IsOcclusionKind(self: win32more.Windows.Media.Devices.ICameraOcclusionState, occlusionKind: win32more.Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    IsOccluded = property(get_IsOccluded, None)
class CameraOcclusionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ICameraOcclusionStateChangedEventArgs
    _classid_ = 'Windows.Media.Devices.CameraOcclusionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Devices.ICameraOcclusionStateChangedEventArgs) -> win32more.Windows.Media.Devices.CameraOcclusionState: ...
    State = property(get_State, None)
class CameraStreamState(Enum, Int32):
    NotStreaming = 0
    Streaming = 1
    BlockedForPrivacy = 2
    Shutdown = 3
class CaptureSceneMode(Enum, Int32):
    Auto = 0
    Manual = 1
    Macro = 2
    Portrait = 3
    Sport = 4
    Snow = 5
    Night = 6
    Beach = 7
    Sunset = 8
    Candlelight = 9
    Landscape = 10
    NightPortrait = 11
    Backlit = 12
class CaptureUse(Enum, Int32):
    None_ = 0
    Photo = 1
    Video = 2
class ColorTemperaturePreset(Enum, Int32):
    Auto = 0
    Manual = 1
    Cloudy = 2
    Daylight = 3
    Flash = 4
    Fluorescent = 5
    Tungsten = 6
    Candlelight = 7
class DefaultAudioCaptureDeviceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs
    _classid_ = 'Windows.Media.Devices.DefaultAudioCaptureDeviceChangedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Role(self: win32more.Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> win32more.Windows.Media.Devices.AudioDeviceRole: ...
    Id = property(get_Id, None)
    Role = property(get_Role, None)
class DefaultAudioRenderDeviceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs
    _classid_ = 'Windows.Media.Devices.DefaultAudioRenderDeviceChangedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Role(self: win32more.Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> win32more.Windows.Media.Devices.AudioDeviceRole: ...
    Id = property(get_Id, None)
    Role = property(get_Role, None)
class DialRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IDialRequestedEventArgs
    _classid_ = 'Windows.Media.Devices.DialRequestedEventArgs'
    @winrt_mixinmethod
    def Handled(self: win32more.Windows.Media.Devices.IDialRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.Media.Devices.IDialRequestedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Contact = property(get_Contact, None)
class DialRequestedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5abbffdb-c21f-4bc4-891b-257e28c1b1a4}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Devices.CallControl, e: win32more.Windows.Media.Devices.DialRequestedEventArgs) -> Void: ...
class DigitalWindowBounds(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IDigitalWindowBounds
    _classid_ = 'Windows.Media.Devices.DigitalWindowBounds'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Devices.DigitalWindowBounds.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Devices.DigitalWindowBounds: ...
    @winrt_mixinmethod
    def get_NormalizedOriginTop(self: win32more.Windows.Media.Devices.IDigitalWindowBounds) -> Double: ...
    @winrt_mixinmethod
    def put_NormalizedOriginTop(self: win32more.Windows.Media.Devices.IDigitalWindowBounds, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_NormalizedOriginLeft(self: win32more.Windows.Media.Devices.IDigitalWindowBounds) -> Double: ...
    @winrt_mixinmethod
    def put_NormalizedOriginLeft(self: win32more.Windows.Media.Devices.IDigitalWindowBounds, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.Media.Devices.IDigitalWindowBounds) -> Double: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.Media.Devices.IDigitalWindowBounds, value: Double) -> Void: ...
    NormalizedOriginLeft = property(get_NormalizedOriginLeft, put_NormalizedOriginLeft)
    NormalizedOriginTop = property(get_NormalizedOriginTop, put_NormalizedOriginTop)
    Scale = property(get_Scale, put_Scale)
class DigitalWindowCapability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IDigitalWindowCapability
    _classid_ = 'Windows.Media.Devices.DigitalWindowCapability'
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Media.Devices.IDigitalWindowCapability) -> Int32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Media.Devices.IDigitalWindowCapability) -> Int32: ...
    @winrt_mixinmethod
    def get_MinScaleValue(self: win32more.Windows.Media.Devices.IDigitalWindowCapability) -> Double: ...
    @winrt_mixinmethod
    def get_MaxScaleValue(self: win32more.Windows.Media.Devices.IDigitalWindowCapability) -> Double: ...
    @winrt_mixinmethod
    def get_MinScaleValueWithoutUpsampling(self: win32more.Windows.Media.Devices.IDigitalWindowCapability) -> Double: ...
    @winrt_mixinmethod
    def get_NormalizedFieldOfViewLimit(self: win32more.Windows.Media.Devices.IDigitalWindowCapability) -> win32more.Windows.Foundation.Rect: ...
    Height = property(get_Height, None)
    MaxScaleValue = property(get_MaxScaleValue, None)
    MinScaleValue = property(get_MinScaleValue, None)
    MinScaleValueWithoutUpsampling = property(get_MinScaleValueWithoutUpsampling, None)
    NormalizedFieldOfViewLimit = property(get_NormalizedFieldOfViewLimit, None)
    Width = property(get_Width, None)
class DigitalWindowControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IDigitalWindowControl
    _classid_ = 'Windows.Media.Devices.DigitalWindowControl'
    @winrt_mixinmethod
    def get_IsSupported(self: win32more.Windows.Media.Devices.IDigitalWindowControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.IDigitalWindowControl) -> ReceiveArray[win32more.Windows.Media.Devices.DigitalWindowMode]: ...
    @winrt_mixinmethod
    def get_CurrentMode(self: win32more.Windows.Media.Devices.IDigitalWindowControl) -> win32more.Windows.Media.Devices.DigitalWindowMode: ...
    @winrt_mixinmethod
    def GetBounds(self: win32more.Windows.Media.Devices.IDigitalWindowControl) -> win32more.Windows.Media.Devices.DigitalWindowBounds: ...
    @winrt_mixinmethod
    def Configure(self: win32more.Windows.Media.Devices.IDigitalWindowControl, digitalWindowMode: win32more.Windows.Media.Devices.DigitalWindowMode) -> Void: ...
    @winrt_mixinmethod
    def ConfigureWithBounds(self: win32more.Windows.Media.Devices.IDigitalWindowControl, digitalWindowMode: win32more.Windows.Media.Devices.DigitalWindowMode, digitalWindowBounds: win32more.Windows.Media.Devices.DigitalWindowBounds) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedCapabilities(self: win32more.Windows.Media.Devices.IDigitalWindowControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.DigitalWindowCapability]: ...
    @winrt_mixinmethod
    def GetCapabilityForSize(self: win32more.Windows.Media.Devices.IDigitalWindowControl, width: Int32, height: Int32) -> win32more.Windows.Media.Devices.DigitalWindowCapability: ...
    CurrentMode = property(get_CurrentMode, None)
    IsSupported = property(get_IsSupported, None)
    SupportedCapabilities = property(get_SupportedCapabilities, None)
    SupportedModes = property(get_SupportedModes, None)
class DigitalWindowMode(Enum, Int32):
    Off = 0
    On = 1
    Auto = 2
class ExposureCompensationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IExposureCompensationControl
    _classid_ = 'Windows.Media.Devices.ExposureCompensationControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IExposureCompensationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def SetValueAsync(self: win32more.Windows.Media.Devices.IExposureCompensationControl, value: Single) -> win32more.Windows.Foundation.IAsyncAction: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    Value = property(get_Value, None)
class ExposureControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IExposureControl
    _classid_ = 'Windows.Media.Devices.ExposureControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IExposureControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Auto(self: win32more.Windows.Media.Devices.IExposureControl) -> Boolean: ...
    @winrt_mixinmethod
    def SetAutoAsync(self: win32more.Windows.Media.Devices.IExposureControl, value: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.IExposureControl) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.IExposureControl) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.IExposureControl) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IExposureControl) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SetValueAsync(self: win32more.Windows.Media.Devices.IExposureControl, shutterDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncAction: ...
    Auto = property(get_Auto, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    Value = property(get_Value, None)
class ExposurePriorityVideoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IExposurePriorityVideoControl
    _classid_ = 'Windows.Media.Devices.ExposurePriorityVideoControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IExposurePriorityVideoControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Media.Devices.IExposurePriorityVideoControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Media.Devices.IExposurePriorityVideoControl, value: Boolean) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    Supported = property(get_Supported, None)
class FlashControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IFlashControl
    _classid_ = 'Windows.Media.Devices.FlashControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerSupported(self: win32more.Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_RedEyeReductionSupported(self: win32more.Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Media.Devices.IFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Auto(self: win32more.Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: win32more.Windows.Media.Devices.IFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RedEyeReduction(self: win32more.Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_RedEyeReduction(self: win32more.Windows.Media.Devices.IFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PowerPercent(self: win32more.Windows.Media.Devices.IFlashControl) -> Single: ...
    @winrt_mixinmethod
    def put_PowerPercent(self: win32more.Windows.Media.Devices.IFlashControl, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AssistantLightSupported(self: win32more.Windows.Media.Devices.IFlashControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_AssistantLightEnabled(self: win32more.Windows.Media.Devices.IFlashControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AssistantLightEnabled(self: win32more.Windows.Media.Devices.IFlashControl2, value: Boolean) -> Void: ...
    AssistantLightEnabled = property(get_AssistantLightEnabled, put_AssistantLightEnabled)
    AssistantLightSupported = property(get_AssistantLightSupported, None)
    Auto = property(get_Auto, put_Auto)
    Enabled = property(get_Enabled, put_Enabled)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
    PowerSupported = property(get_PowerSupported, None)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    Supported = property(get_Supported, None)
class FocusControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IFocusControl
    _classid_ = 'Windows.Media.Devices.FocusControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IFocusControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedPresets(self: win32more.Windows.Media.Devices.IFocusControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.FocusPreset]: ...
    @winrt_mixinmethod
    def get_Preset(self: win32more.Windows.Media.Devices.IFocusControl) -> win32more.Windows.Media.Devices.FocusPreset: ...
    @winrt_mixinmethod
    def SetPresetAsync(self: win32more.Windows.Media.Devices.IFocusControl, preset: win32more.Windows.Media.Devices.FocusPreset) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetPresetWithCompletionOptionAsync(self: win32more.Windows.Media.Devices.IFocusControl, preset: win32more.Windows.Media.Devices.FocusPreset, completeBeforeFocus: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def SetValueAsync(self: win32more.Windows.Media.Devices.IFocusControl, focus: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FocusAsync(self: win32more.Windows.Media.Devices.IFocusControl) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_FocusChangedSupported(self: win32more.Windows.Media.Devices.IFocusControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_WaitForFocusSupported(self: win32more.Windows.Media.Devices.IFocusControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedFocusModes(self: win32more.Windows.Media.Devices.IFocusControl2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.FocusMode]: ...
    @winrt_mixinmethod
    def get_SupportedFocusDistances(self: win32more.Windows.Media.Devices.IFocusControl2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_mixinmethod
    def get_SupportedFocusRanges(self: win32more.Windows.Media.Devices.IFocusControl2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AutoFocusRange]: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IFocusControl2) -> win32more.Windows.Media.Devices.FocusMode: ...
    @winrt_mixinmethod
    def get_FocusState(self: win32more.Windows.Media.Devices.IFocusControl2) -> win32more.Windows.Media.Devices.MediaCaptureFocusState: ...
    @winrt_mixinmethod
    def UnlockAsync(self: win32more.Windows.Media.Devices.IFocusControl2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def LockAsync(self: win32more.Windows.Media.Devices.IFocusControl2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Configure(self: win32more.Windows.Media.Devices.IFocusControl2, settings: win32more.Windows.Media.Devices.FocusSettings) -> Void: ...
    FocusChangedSupported = property(get_FocusChangedSupported, None)
    FocusState = property(get_FocusState, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Mode = property(get_Mode, None)
    Preset = property(get_Preset, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    SupportedFocusDistances = property(get_SupportedFocusDistances, None)
    SupportedFocusModes = property(get_SupportedFocusModes, None)
    SupportedFocusRanges = property(get_SupportedFocusRanges, None)
    SupportedPresets = property(get_SupportedPresets, None)
    Value = property(get_Value, None)
    WaitForFocusSupported = property(get_WaitForFocusSupported, None)
class FocusMode(Enum, Int32):
    Auto = 0
    Single = 1
    Continuous = 2
    Manual = 3
class FocusPreset(Enum, Int32):
    Auto = 0
    Manual = 1
    AutoMacro = 2
    AutoNormal = 3
    AutoInfinity = 4
    AutoHyperfocal = 5
class FocusSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IFocusSettings
    _classid_ = 'Windows.Media.Devices.FocusSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Devices.FocusSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Devices.FocusSettings: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IFocusSettings) -> win32more.Windows.Media.Devices.FocusMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Devices.IFocusSettings, value: win32more.Windows.Media.Devices.FocusMode) -> Void: ...
    @winrt_mixinmethod
    def get_AutoFocusRange(self: win32more.Windows.Media.Devices.IFocusSettings) -> win32more.Windows.Media.Devices.AutoFocusRange: ...
    @winrt_mixinmethod
    def put_AutoFocusRange(self: win32more.Windows.Media.Devices.IFocusSettings, value: win32more.Windows.Media.Devices.AutoFocusRange) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IFocusSettings) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Media.Devices.IFocusSettings, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_Distance(self: win32more.Windows.Media.Devices.IFocusSettings) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_mixinmethod
    def put_Distance(self: win32more.Windows.Media.Devices.IFocusSettings, value: win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.ManualFocusDistance]) -> Void: ...
    @winrt_mixinmethod
    def get_WaitForFocus(self: win32more.Windows.Media.Devices.IFocusSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_WaitForFocus(self: win32more.Windows.Media.Devices.IFocusSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DisableDriverFallback(self: win32more.Windows.Media.Devices.IFocusSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisableDriverFallback(self: win32more.Windows.Media.Devices.IFocusSettings, value: Boolean) -> Void: ...
    AutoFocusRange = property(get_AutoFocusRange, put_AutoFocusRange)
    DisableDriverFallback = property(get_DisableDriverFallback, put_DisableDriverFallback)
    Distance = property(get_Distance, put_Distance)
    Mode = property(get_Mode, put_Mode)
    Value = property(get_Value, put_Value)
    WaitForFocus = property(get_WaitForFocus, put_WaitForFocus)
class HdrVideoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IHdrVideoControl
    _classid_ = 'Windows.Media.Devices.HdrVideoControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IHdrVideoControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.IHdrVideoControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.HdrVideoMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IHdrVideoControl) -> win32more.Windows.Media.Devices.HdrVideoMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Devices.IHdrVideoControl, value: win32more.Windows.Media.Devices.HdrVideoMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class HdrVideoMode(Enum, Int32):
    Off = 0
    On = 1
    Auto = 2
class IAdvancedPhotoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedPhotoCaptureSettings'
    _iid_ = Guid('{08f3863a-0018-445b-93d2-646d1c5ed05c}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.Media.Devices.AdvancedPhotoMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class IAdvancedPhotoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedPhotoControl'
    _iid_ = Guid('{c5b15486-9001-4682-9309-68eae0080eec}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AdvancedPhotoMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_commethod(9)
    def Configure(self, settings: win32more.Windows.Media.Devices.AdvancedPhotoCaptureSettings) -> Void: ...
    Mode = property(get_Mode, None)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class IAdvancedVideoCaptureDeviceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController'
    _iid_ = Guid('{de6ff4d3-2b96-4583-80ab-b5b01dc6a8d7}')
    @winrt_commethod(6)
    def SetDeviceProperty(self, propertyId: WinRT_String, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def GetDeviceProperty(self, propertyId: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IAdvancedVideoCaptureDeviceController10(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController10'
    _iid_ = Guid('{c621b82d-d6f0-5c1b-a388-a6e938407146}')
    @winrt_commethod(6)
    def get_CameraOcclusionInfo(self) -> win32more.Windows.Media.Devices.CameraOcclusionInfo: ...
    CameraOcclusionInfo = property(get_CameraOcclusionInfo, None)
class IAdvancedVideoCaptureDeviceController11(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController11'
    _iid_ = Guid('{d5b65ae2-3772-580c-a630-e75de9106904}')
    @winrt_commethod(6)
    def TryAcquireExclusiveControl(self, deviceId: WinRT_String, mode: win32more.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlReleaseMode) -> Boolean: ...
class IAdvancedVideoCaptureDeviceController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2'
    _iid_ = Guid('{8bb94f8f-f11a-43db-b402-11930b80ae56}')
    @winrt_commethod(6)
    def get_LowLagPhotoSequence(self) -> win32more.Windows.Media.Devices.LowLagPhotoSequenceControl: ...
    @winrt_commethod(7)
    def get_LowLagPhoto(self) -> win32more.Windows.Media.Devices.LowLagPhotoControl: ...
    @winrt_commethod(8)
    def get_SceneModeControl(self) -> win32more.Windows.Media.Devices.SceneModeControl: ...
    @winrt_commethod(9)
    def get_TorchControl(self) -> win32more.Windows.Media.Devices.TorchControl: ...
    @winrt_commethod(10)
    def get_FlashControl(self) -> win32more.Windows.Media.Devices.FlashControl: ...
    @winrt_commethod(11)
    def get_WhiteBalanceControl(self) -> win32more.Windows.Media.Devices.WhiteBalanceControl: ...
    @winrt_commethod(12)
    def get_ExposureControl(self) -> win32more.Windows.Media.Devices.ExposureControl: ...
    @winrt_commethod(13)
    def get_FocusControl(self) -> win32more.Windows.Media.Devices.FocusControl: ...
    @winrt_commethod(14)
    def get_ExposureCompensationControl(self) -> win32more.Windows.Media.Devices.ExposureCompensationControl: ...
    @winrt_commethod(15)
    def get_IsoSpeedControl(self) -> win32more.Windows.Media.Devices.IsoSpeedControl: ...
    @winrt_commethod(16)
    def get_RegionsOfInterestControl(self) -> win32more.Windows.Media.Devices.RegionsOfInterestControl: ...
    @winrt_commethod(17)
    def get_PrimaryUse(self) -> win32more.Windows.Media.Devices.CaptureUse: ...
    @winrt_commethod(18)
    def put_PrimaryUse(self, value: win32more.Windows.Media.Devices.CaptureUse) -> Void: ...
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    ExposureControl = property(get_ExposureControl, None)
    FlashControl = property(get_FlashControl, None)
    FocusControl = property(get_FocusControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    LowLagPhoto = property(get_LowLagPhoto, None)
    LowLagPhotoSequence = property(get_LowLagPhotoSequence, None)
    PrimaryUse = property(get_PrimaryUse, put_PrimaryUse)
    RegionsOfInterestControl = property(get_RegionsOfInterestControl, None)
    SceneModeControl = property(get_SceneModeControl, None)
    TorchControl = property(get_TorchControl, None)
    WhiteBalanceControl = property(get_WhiteBalanceControl, None)
class IAdvancedVideoCaptureDeviceController3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController3'
    _iid_ = Guid('{a98b8f34-ee0d-470c-b9f0-4229c4bbd089}')
    @winrt_commethod(6)
    def get_VariablePhotoSequenceController(self) -> win32more.Windows.Media.Devices.Core.VariablePhotoSequenceController: ...
    @winrt_commethod(7)
    def get_PhotoConfirmationControl(self) -> win32more.Windows.Media.Devices.PhotoConfirmationControl: ...
    @winrt_commethod(8)
    def get_ZoomControl(self) -> win32more.Windows.Media.Devices.ZoomControl: ...
    PhotoConfirmationControl = property(get_PhotoConfirmationControl, None)
    VariablePhotoSequenceController = property(get_VariablePhotoSequenceController, None)
    ZoomControl = property(get_ZoomControl, None)
class IAdvancedVideoCaptureDeviceController4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4'
    _iid_ = Guid('{ea9fbfaf-d371-41c3-9a17-824a87ebdfd2}')
    @winrt_commethod(6)
    def get_ExposurePriorityVideoControl(self) -> win32more.Windows.Media.Devices.ExposurePriorityVideoControl: ...
    @winrt_commethod(7)
    def get_DesiredOptimization(self) -> win32more.Windows.Media.Devices.MediaCaptureOptimization: ...
    @winrt_commethod(8)
    def put_DesiredOptimization(self, value: win32more.Windows.Media.Devices.MediaCaptureOptimization) -> Void: ...
    @winrt_commethod(9)
    def get_HdrVideoControl(self) -> win32more.Windows.Media.Devices.HdrVideoControl: ...
    @winrt_commethod(10)
    def get_OpticalImageStabilizationControl(self) -> win32more.Windows.Media.Devices.OpticalImageStabilizationControl: ...
    @winrt_commethod(11)
    def get_AdvancedPhotoControl(self) -> win32more.Windows.Media.Devices.AdvancedPhotoControl: ...
    AdvancedPhotoControl = property(get_AdvancedPhotoControl, None)
    DesiredOptimization = property(get_DesiredOptimization, put_DesiredOptimization)
    ExposurePriorityVideoControl = property(get_ExposurePriorityVideoControl, None)
    HdrVideoControl = property(get_HdrVideoControl, None)
    OpticalImageStabilizationControl = property(get_OpticalImageStabilizationControl, None)
class IAdvancedVideoCaptureDeviceController5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5'
    _iid_ = Guid('{33512b17-b9cb-4a23-b875-f9eaab535492}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDevicePropertyById(self, propertyId: WinRT_String, maxPropertyValueSize: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_commethod(8)
    def SetDevicePropertyById(self, propertyId: WinRT_String, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    @winrt_commethod(9)
    def GetDevicePropertyByExtendedId(self, extendedPropertyId: PassArray[Byte], maxPropertyValueSize: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_commethod(10)
    def SetDevicePropertyByExtendedId(self, extendedPropertyId: PassArray[Byte], propertyValue: PassArray[Byte]) -> win32more.Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    Id = property(get_Id, None)
class IAdvancedVideoCaptureDeviceController6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController6'
    _iid_ = Guid('{b6563a53-68a1-44b7-9f89-b5fa97ac0cbe}')
    @winrt_commethod(6)
    def get_VideoTemporalDenoisingControl(self) -> win32more.Windows.Media.Devices.VideoTemporalDenoisingControl: ...
    VideoTemporalDenoisingControl = property(get_VideoTemporalDenoisingControl, None)
class IAdvancedVideoCaptureDeviceController7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController7'
    _iid_ = Guid('{8d2927f0-a054-50e7-b7df-7c04234d10f0}')
    @winrt_commethod(6)
    def get_InfraredTorchControl(self) -> win32more.Windows.Media.Devices.InfraredTorchControl: ...
    InfraredTorchControl = property(get_InfraredTorchControl, None)
class IAdvancedVideoCaptureDeviceController8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController8'
    _iid_ = Guid('{d843f010-e7fb-595b-9a78-0e54c4532b43}')
    @winrt_commethod(6)
    def get_PanelBasedOptimizationControl(self) -> win32more.Windows.Media.Devices.PanelBasedOptimizationControl: ...
    PanelBasedOptimizationControl = property(get_PanelBasedOptimizationControl, None)
class IAdvancedVideoCaptureDeviceController9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAdvancedVideoCaptureDeviceController9'
    _iid_ = Guid('{8bdca95d-0255-51bc-a10d-5a169ec1625a}')
    @winrt_commethod(6)
    def get_DigitalWindowControl(self) -> win32more.Windows.Media.Devices.DigitalWindowControl: ...
    DigitalWindowControl = property(get_DigitalWindowControl, None)
class IAudioDeviceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAudioDeviceController'
    _iid_ = Guid('{edd4a388-79c7-4f7c-90e8-ef934b21580a}')
    @winrt_commethod(6)
    def put_Muted(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Muted(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_VolumePercent(self, value: Single) -> Void: ...
    @winrt_commethod(9)
    def get_VolumePercent(self) -> Single: ...
    Muted = property(get_Muted, put_Muted)
    VolumePercent = property(get_VolumePercent, put_VolumePercent)
class IAudioDeviceController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAudioDeviceController2'
    _iid_ = Guid('{85326599-4c24-48b0-81dd-0c5cc79ddf05}')
    @winrt_commethod(6)
    def get_AudioCaptureEffectsManager(self) -> win32more.Windows.Media.Effects.AudioCaptureEffectsManager: ...
    AudioCaptureEffectsManager = property(get_AudioCaptureEffectsManager, None)
class IAudioDeviceModule(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAudioDeviceModule'
    _iid_ = Guid('{86cfac36-47c1-4b33-9852-8773ec4be123}')
    @winrt_commethod(6)
    def get_ClassId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_InstanceId(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_MajorVersion(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_MinorVersion(self) -> UInt32: ...
    @winrt_commethod(11)
    def SendCommandAsync(self, Command: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Devices.ModuleCommandResult]: ...
    ClassId = property(get_ClassId, None)
    DisplayName = property(get_DisplayName, None)
    InstanceId = property(get_InstanceId, None)
    MajorVersion = property(get_MajorVersion, None)
    MinorVersion = property(get_MinorVersion, None)
class IAudioDeviceModuleNotificationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAudioDeviceModuleNotificationEventArgs'
    _iid_ = Guid('{e3e3ccaf-224c-48be-956b-9a13134e96e8}')
    @winrt_commethod(6)
    def get_Module(self) -> win32more.Windows.Media.Devices.AudioDeviceModule: ...
    @winrt_commethod(7)
    def get_NotificationData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Module = property(get_Module, None)
    NotificationData = property(get_NotificationData, None)
class IAudioDeviceModulesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAudioDeviceModulesManager'
    _iid_ = Guid('{6aa40c4d-960a-4d1c-b318-0022604547ed}')
    @winrt_commethod(6)
    def add_ModuleNotificationReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Devices.AudioDeviceModulesManager, win32more.Windows.Media.Devices.AudioDeviceModuleNotificationEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ModuleNotificationReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def FindAllById(self, moduleId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AudioDeviceModule]: ...
    @winrt_commethod(9)
    def FindAll(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AudioDeviceModule]: ...
    ModuleNotificationReceived = event()
class IAudioDeviceModulesManagerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IAudioDeviceModulesManagerFactory'
    _iid_ = Guid('{8db03670-e64d-4773-96c0-bc7ebf0e063f}')
    @winrt_commethod(6)
    def Create(self, deviceId: WinRT_String) -> win32more.Windows.Media.Devices.AudioDeviceModulesManager: ...
class ICallControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ICallControl'
    _iid_ = Guid('{a520d0d6-ae8d-45db-8011-ca49d3b3e578}')
    @winrt_commethod(6)
    def IndicateNewIncomingCall(self, enableRinger: Boolean, callerId: WinRT_String) -> UInt64: ...
    @winrt_commethod(7)
    def IndicateNewOutgoingCall(self) -> UInt64: ...
    @winrt_commethod(8)
    def IndicateActiveCall(self, callToken: UInt64) -> Void: ...
    @winrt_commethod(9)
    def EndCall(self, callToken: UInt64) -> Void: ...
    @winrt_commethod(10)
    def get_HasRinger(self) -> Boolean: ...
    @winrt_commethod(11)
    def add_AnswerRequested(self, handler: win32more.Windows.Media.Devices.CallControlEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AnswerRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_HangUpRequested(self, handler: win32more.Windows.Media.Devices.CallControlEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_HangUpRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_DialRequested(self, handler: win32more.Windows.Media.Devices.DialRequestedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_DialRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_RedialRequested(self, handler: win32more.Windows.Media.Devices.RedialRequestedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_RedialRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_KeypadPressed(self, handler: win32more.Windows.Media.Devices.KeypadPressedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_KeypadPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_AudioTransferRequested(self, handler: win32more.Windows.Media.Devices.CallControlEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_AudioTransferRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    HasRinger = property(get_HasRinger, None)
    AnswerRequested = event()
    HangUpRequested = event()
    DialRequested = event()
    RedialRequested = event()
    KeypadPressed = event()
    AudioTransferRequested = event()
class ICallControlStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ICallControlStatics'
    _iid_ = Guid('{03945ad5-85ab-40e1-af19-56c94303b019}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Media.Devices.CallControl: ...
    @winrt_commethod(7)
    def FromId(self, deviceId: WinRT_String) -> win32more.Windows.Media.Devices.CallControl: ...
class ICameraOcclusionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ICameraOcclusionInfo'
    _iid_ = Guid('{af6c4ad0-a84d-5db6-be58-a5da21cfe011}')
    @winrt_commethod(6)
    def GetState(self) -> win32more.Windows.Media.Devices.CameraOcclusionState: ...
    @winrt_commethod(7)
    def IsOcclusionKindSupported(self, occlusionKind: win32more.Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    @winrt_commethod(8)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Devices.CameraOcclusionInfo, win32more.Windows.Media.Devices.CameraOcclusionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    StateChanged = event()
class ICameraOcclusionState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ICameraOcclusionState'
    _iid_ = Guid('{430adeb8-6842-5e55-9bde-04b4ef3a8a57}')
    @winrt_commethod(6)
    def get_IsOccluded(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsOcclusionKind(self, occlusionKind: win32more.Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    IsOccluded = property(get_IsOccluded, None)
class ICameraOcclusionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ICameraOcclusionStateChangedEventArgs'
    _iid_ = Guid('{8512d848-c0de-57ca-a1ca-fb2c3d23df55}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.Devices.CameraOcclusionState: ...
    State = property(get_State, None)
class IDefaultAudioDeviceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs'
    _iid_ = Guid('{110f882f-1c05-4657-a18e-47c9b69f07ab}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Role(self) -> win32more.Windows.Media.Devices.AudioDeviceRole: ...
    Id = property(get_Id, None)
    Role = property(get_Role, None)
class IDialRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IDialRequestedEventArgs'
    _iid_ = Guid('{037b929e-953c-4286-8866-4f0f376c855a}')
    @winrt_commethod(6)
    def Handled(self) -> Void: ...
    @winrt_commethod(7)
    def get_Contact(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Contact = property(get_Contact, None)
class IDigitalWindowBounds(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IDigitalWindowBounds'
    _iid_ = Guid('{dd4f21dd-d173-5c6b-8c25-bdd26d5122b1}')
    @winrt_commethod(6)
    def get_NormalizedOriginTop(self) -> Double: ...
    @winrt_commethod(7)
    def put_NormalizedOriginTop(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_NormalizedOriginLeft(self) -> Double: ...
    @winrt_commethod(9)
    def put_NormalizedOriginLeft(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_Scale(self) -> Double: ...
    @winrt_commethod(11)
    def put_Scale(self, value: Double) -> Void: ...
    NormalizedOriginLeft = property(get_NormalizedOriginLeft, put_NormalizedOriginLeft)
    NormalizedOriginTop = property(get_NormalizedOriginTop, put_NormalizedOriginTop)
    Scale = property(get_Scale, put_Scale)
class IDigitalWindowCapability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IDigitalWindowCapability'
    _iid_ = Guid('{d78bad2c-f721-5244-a196-b56ccbec606c}')
    @winrt_commethod(6)
    def get_Width(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Height(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MinScaleValue(self) -> Double: ...
    @winrt_commethod(9)
    def get_MaxScaleValue(self) -> Double: ...
    @winrt_commethod(10)
    def get_MinScaleValueWithoutUpsampling(self) -> Double: ...
    @winrt_commethod(11)
    def get_NormalizedFieldOfViewLimit(self) -> win32more.Windows.Foundation.Rect: ...
    Height = property(get_Height, None)
    MaxScaleValue = property(get_MaxScaleValue, None)
    MinScaleValue = property(get_MinScaleValue, None)
    MinScaleValueWithoutUpsampling = property(get_MinScaleValueWithoutUpsampling, None)
    NormalizedFieldOfViewLimit = property(get_NormalizedFieldOfViewLimit, None)
    Width = property(get_Width, None)
class IDigitalWindowControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IDigitalWindowControl'
    _iid_ = Guid('{23b69eff-65d2-53ea-8780-de582b48b544}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> ReceiveArray[win32more.Windows.Media.Devices.DigitalWindowMode]: ...
    @winrt_commethod(8)
    def get_CurrentMode(self) -> win32more.Windows.Media.Devices.DigitalWindowMode: ...
    @winrt_commethod(9)
    def GetBounds(self) -> win32more.Windows.Media.Devices.DigitalWindowBounds: ...
    @winrt_commethod(10)
    def Configure(self, digitalWindowMode: win32more.Windows.Media.Devices.DigitalWindowMode) -> Void: ...
    @winrt_commethod(11)
    def ConfigureWithBounds(self, digitalWindowMode: win32more.Windows.Media.Devices.DigitalWindowMode, digitalWindowBounds: win32more.Windows.Media.Devices.DigitalWindowBounds) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedCapabilities(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.DigitalWindowCapability]: ...
    @winrt_commethod(13)
    def GetCapabilityForSize(self, width: Int32, height: Int32) -> win32more.Windows.Media.Devices.DigitalWindowCapability: ...
    CurrentMode = property(get_CurrentMode, None)
    IsSupported = property(get_IsSupported, None)
    SupportedCapabilities = property(get_SupportedCapabilities, None)
    SupportedModes = property(get_SupportedModes, None)
class IExposureCompensationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IExposureCompensationControl'
    _iid_ = Guid('{81c8e834-dcec-4011-a610-1f3847e64aca}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> Single: ...
    @winrt_commethod(8)
    def get_Max(self) -> Single: ...
    @winrt_commethod(9)
    def get_Step(self) -> Single: ...
    @winrt_commethod(10)
    def get_Value(self) -> Single: ...
    @winrt_commethod(11)
    def SetValueAsync(self, value: Single) -> win32more.Windows.Foundation.IAsyncAction: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    Value = property(get_Value, None)
class IExposureControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IExposureControl'
    _iid_ = Guid('{09e8cbe2-ad96-4f28-a0e0-96ed7e1b5fd2}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(8)
    def SetAutoAsync(self, value: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_Min(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Max(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def get_Step(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def get_Value(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def SetValueAsync(self, shutterDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncAction: ...
    Auto = property(get_Auto, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    Value = property(get_Value, None)
class IExposurePriorityVideoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IExposurePriorityVideoControl'
    _iid_ = Guid('{2cb240a3-5168-4271-9ea5-47621a98a352}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Enabled(self, value: Boolean) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    Supported = property(get_Supported, None)
class IFlashControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IFlashControl'
    _iid_ = Guid('{def41dbe-7d68-45e3-8c0f-be7bb32837d0}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_PowerSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_RedEyeReductionSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Auto(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_RedEyeReduction(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_RedEyeReduction(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_PowerPercent(self) -> Single: ...
    @winrt_commethod(16)
    def put_PowerPercent(self, value: Single) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Enabled = property(get_Enabled, put_Enabled)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
    PowerSupported = property(get_PowerSupported, None)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    Supported = property(get_Supported, None)
class IFlashControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IFlashControl2'
    _iid_ = Guid('{7d29cc9e-75e1-4af7-bd7d-4e38e1c06cd6}')
    @winrt_commethod(6)
    def get_AssistantLightSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AssistantLightEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AssistantLightEnabled(self, value: Boolean) -> Void: ...
    AssistantLightEnabled = property(get_AssistantLightEnabled, put_AssistantLightEnabled)
    AssistantLightSupported = property(get_AssistantLightSupported, None)
class IFocusControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IFocusControl'
    _iid_ = Guid('{c0d889f6-5228-4453-b153-85606592b238}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedPresets(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.FocusPreset]: ...
    @winrt_commethod(8)
    def get_Preset(self) -> win32more.Windows.Media.Devices.FocusPreset: ...
    @winrt_commethod(9)
    def SetPresetAsync(self, preset: win32more.Windows.Media.Devices.FocusPreset) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def SetPresetWithCompletionOptionAsync(self, preset: win32more.Windows.Media.Devices.FocusPreset, completeBeforeFocus: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_Step(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(15)
    def SetValueAsync(self, focus: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def FocusAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Preset = property(get_Preset, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    SupportedPresets = property(get_SupportedPresets, None)
    Value = property(get_Value, None)
class IFocusControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IFocusControl2'
    _iid_ = Guid('{3f7cff48-c534-4e9e-94c3-52ef2afd5d07}')
    @winrt_commethod(6)
    def get_FocusChangedSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_WaitForFocusSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SupportedFocusModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.FocusMode]: ...
    @winrt_commethod(9)
    def get_SupportedFocusDistances(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_commethod(10)
    def get_SupportedFocusRanges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.AutoFocusRange]: ...
    @winrt_commethod(11)
    def get_Mode(self) -> win32more.Windows.Media.Devices.FocusMode: ...
    @winrt_commethod(12)
    def get_FocusState(self) -> win32more.Windows.Media.Devices.MediaCaptureFocusState: ...
    @winrt_commethod(13)
    def UnlockAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def LockAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def Configure(self, settings: win32more.Windows.Media.Devices.FocusSettings) -> Void: ...
    FocusChangedSupported = property(get_FocusChangedSupported, None)
    FocusState = property(get_FocusState, None)
    Mode = property(get_Mode, None)
    SupportedFocusDistances = property(get_SupportedFocusDistances, None)
    SupportedFocusModes = property(get_SupportedFocusModes, None)
    SupportedFocusRanges = property(get_SupportedFocusRanges, None)
    WaitForFocusSupported = property(get_WaitForFocusSupported, None)
class IFocusSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IFocusSettings'
    _iid_ = Guid('{79958f6b-3263-4275-85d6-aeae891c96ee}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.Media.Devices.FocusMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.Media.Devices.FocusMode) -> Void: ...
    @winrt_commethod(8)
    def get_AutoFocusRange(self) -> win32more.Windows.Media.Devices.AutoFocusRange: ...
    @winrt_commethod(9)
    def put_AutoFocusRange(self, value: win32more.Windows.Media.Devices.AutoFocusRange) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(11)
    def put_Value(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(12)
    def get_Distance(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_commethod(13)
    def put_Distance(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Media.Devices.ManualFocusDistance]) -> Void: ...
    @winrt_commethod(14)
    def get_WaitForFocus(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_WaitForFocus(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_DisableDriverFallback(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_DisableDriverFallback(self, value: Boolean) -> Void: ...
    AutoFocusRange = property(get_AutoFocusRange, put_AutoFocusRange)
    DisableDriverFallback = property(get_DisableDriverFallback, put_DisableDriverFallback)
    Distance = property(get_Distance, put_Distance)
    Mode = property(get_Mode, put_Mode)
    Value = property(get_Value, put_Value)
    WaitForFocus = property(get_WaitForFocus, put_WaitForFocus)
class IHdrVideoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IHdrVideoControl'
    _iid_ = Guid('{55d8e2d0-30c0-43bf-9b9a-9799d70ced94}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.HdrVideoMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Windows.Media.Devices.HdrVideoMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: win32more.Windows.Media.Devices.HdrVideoMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class IInfraredTorchControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IInfraredTorchControl'
    _iid_ = Guid('{1cba2c83-6cb6-5a04-a6fc-3be7b33ff056}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.InfraredTorchMode]: ...
    @winrt_commethod(8)
    def get_CurrentMode(self) -> win32more.Windows.Media.Devices.InfraredTorchMode: ...
    @winrt_commethod(9)
    def put_CurrentMode(self, value: win32more.Windows.Media.Devices.InfraredTorchMode) -> Void: ...
    @winrt_commethod(10)
    def get_MinPower(self) -> Int32: ...
    @winrt_commethod(11)
    def get_MaxPower(self) -> Int32: ...
    @winrt_commethod(12)
    def get_PowerStep(self) -> Int32: ...
    @winrt_commethod(13)
    def get_Power(self) -> Int32: ...
    @winrt_commethod(14)
    def put_Power(self, value: Int32) -> Void: ...
    CurrentMode = property(get_CurrentMode, put_CurrentMode)
    IsSupported = property(get_IsSupported, None)
    MaxPower = property(get_MaxPower, None)
    MinPower = property(get_MinPower, None)
    Power = property(get_Power, put_Power)
    PowerStep = property(get_PowerStep, None)
    SupportedModes = property(get_SupportedModes, None)
class IIsoSpeedControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IIsoSpeedControl'
    _iid_ = Guid('{27b6c322-25ad-4f1b-aaab-524ab376ca33}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedPresets(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.IsoSpeedPreset]: ...
    @winrt_commethod(8)
    def get_Preset(self) -> win32more.Windows.Media.Devices.IsoSpeedPreset: ...
    @winrt_commethod(9)
    def SetPresetAsync(self, preset: win32more.Windows.Media.Devices.IsoSpeedPreset) -> win32more.Windows.Foundation.IAsyncAction: ...
    Preset = property(get_Preset, None)
    Supported = property(get_Supported, None)
    SupportedPresets = property(get_SupportedPresets, None)
class IIsoSpeedControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IIsoSpeedControl2'
    _iid_ = Guid('{6f1578f2-6d77-4f8a-8c2f-6130b6395053}')
    @winrt_commethod(6)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Step(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(10)
    def SetValueAsync(self, isoSpeed: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(12)
    def SetAutoAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Auto = property(get_Auto, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class IKeypadPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IKeypadPressedEventArgs'
    _iid_ = Guid('{d3a43900-b4fa-49cd-9442-89af6568f601}')
    @winrt_commethod(6)
    def get_TelephonyKey(self) -> win32more.Windows.Media.Devices.TelephonyKey: ...
    TelephonyKey = property(get_TelephonyKey, None)
class ILowLagPhotoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ILowLagPhotoControl'
    _iid_ = Guid('{6d5c4dd0-fadf-415d-aee6-3baa529300c9}')
    @winrt_commethod(6)
    def GetHighestConcurrentFrameRate(self, captureProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(7)
    def GetCurrentFrameRate(self) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(8)
    def get_ThumbnailEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_ThumbnailEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ThumbnailFormat(self) -> win32more.Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_commethod(11)
    def put_ThumbnailFormat(self, value: win32more.Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_commethod(12)
    def get_DesiredThumbnailSize(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_DesiredThumbnailSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_HardwareAcceleratedThumbnailSupported(self) -> UInt32: ...
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
class ILowLagPhotoSequenceControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ILowLagPhotoSequenceControl'
    _iid_ = Guid('{3dcf909d-6d16-409c-bafe-b9a594c6fde6}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MaxPastPhotos(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxPhotosPerSecond(self) -> Single: ...
    @winrt_commethod(9)
    def get_PastPhotoLimit(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_PastPhotoLimit(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_PhotosPerSecondLimit(self) -> Single: ...
    @winrt_commethod(12)
    def put_PhotosPerSecondLimit(self, value: Single) -> Void: ...
    @winrt_commethod(13)
    def GetHighestConcurrentFrameRate(self, captureProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(14)
    def GetCurrentFrameRate(self) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(15)
    def get_ThumbnailEnabled(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_ThumbnailEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_ThumbnailFormat(self) -> win32more.Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_commethod(18)
    def put_ThumbnailFormat(self, value: win32more.Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_commethod(19)
    def get_DesiredThumbnailSize(self) -> UInt32: ...
    @winrt_commethod(20)
    def put_DesiredThumbnailSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(21)
    def get_HardwareAcceleratedThumbnailSupported(self) -> UInt32: ...
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
    MaxPastPhotos = property(get_MaxPastPhotos, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PastPhotoLimit = property(get_PastPhotoLimit, put_PastPhotoLimit)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    Supported = property(get_Supported, None)
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
class IMediaDeviceControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IMediaDeviceControl'
    _iid_ = Guid('{efa8dfa9-6f75-4863-ba0b-583f3036b4de}')
    @winrt_commethod(6)
    def get_Capabilities(self) -> win32more.Windows.Media.Devices.MediaDeviceControlCapabilities: ...
    @winrt_commethod(7)
    def TryGetValue(self, value: POINTER(Double)) -> Boolean: ...
    @winrt_commethod(8)
    def TrySetValue(self, value: Double) -> Boolean: ...
    @winrt_commethod(9)
    def TryGetAuto(self, value: POINTER(Boolean)) -> Boolean: ...
    @winrt_commethod(10)
    def TrySetAuto(self, value: Boolean) -> Boolean: ...
    Capabilities = property(get_Capabilities, None)
class IMediaDeviceControlCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IMediaDeviceControlCapabilities'
    _iid_ = Guid('{23005816-eb85-43e2-b92b-8240d5ee70ec}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> Double: ...
    @winrt_commethod(8)
    def get_Max(self) -> Double: ...
    @winrt_commethod(9)
    def get_Step(self) -> Double: ...
    @winrt_commethod(10)
    def get_Default(self) -> Double: ...
    @winrt_commethod(11)
    def get_AutoModeSupported(self) -> Boolean: ...
    AutoModeSupported = property(get_AutoModeSupported, None)
    Default = property(get_Default, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class IMediaDeviceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IMediaDeviceController'
    _iid_ = Guid('{f6f8f5ce-209a-48fb-86fc-d44578f317e6}')
    @winrt_commethod(6)
    def GetAvailableMediaStreamProperties(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.MediaProperties.IMediaEncodingProperties]: ...
    @winrt_commethod(7)
    def GetMediaStreamProperties(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Media.MediaProperties.IMediaEncodingProperties: ...
    @winrt_commethod(8)
    def SetMediaStreamPropertiesAsync(self, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
class IMediaDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IMediaDeviceStatics'
    _iid_ = Guid('{aa2d9a40-909f-4bba-bf8b-0c0d296f14f0}')
    @winrt_commethod(6)
    def GetAudioCaptureSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetAudioRenderSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetVideoCaptureSelector(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDefaultAudioCaptureId(self, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDefaultAudioRenderId(self, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_commethod(11)
    def add_DefaultAudioCaptureDeviceChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Media.Devices.DefaultAudioCaptureDeviceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_DefaultAudioCaptureDeviceChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_DefaultAudioRenderDeviceChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Media.Devices.DefaultAudioRenderDeviceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_DefaultAudioRenderDeviceChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DefaultAudioCaptureDeviceChanged = event()
    DefaultAudioRenderDeviceChanged = event()
class IModuleCommandResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IModuleCommandResult'
    _iid_ = Guid('{520d1eb4-1374-4c7d-b1e4-39dcdf3eae4e}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Devices.SendCommandStatus: ...
    @winrt_commethod(7)
    def get_Result(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class IOpticalImageStabilizationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IOpticalImageStabilizationControl'
    _iid_ = Guid('{bfad9c1d-00bc-423b-8eb2-a0178ca94247}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.OpticalImageStabilizationMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Windows.Media.Devices.OpticalImageStabilizationMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: win32more.Windows.Media.Devices.OpticalImageStabilizationMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class IPanelBasedOptimizationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IPanelBasedOptimizationControl'
    _iid_ = Guid('{33323223-6247-5419-a5a4-3d808645d917}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Panel(self) -> win32more.Windows.Devices.Enumeration.Panel: ...
    @winrt_commethod(8)
    def put_Panel(self, value: win32more.Windows.Devices.Enumeration.Panel) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    Panel = property(get_Panel, put_Panel)
class IPhotoConfirmationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IPhotoConfirmationControl'
    _iid_ = Guid('{c8f3f363-ff5e-4582-a9a8-0550f85a4a76}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_PixelFormat(self) -> win32more.Windows.Media.MediaProperties.MediaPixelFormat: ...
    @winrt_commethod(10)
    def put_PixelFormat(self, format: win32more.Windows.Media.MediaProperties.MediaPixelFormat) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
    Supported = property(get_Supported, None)
class IRedialRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IRedialRequestedEventArgs'
    _iid_ = Guid('{7eb55209-76ab-4c31-b40e-4b58379d580c}')
    @winrt_commethod(6)
    def Handled(self) -> Void: ...
class IRegionOfInterest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IRegionOfInterest'
    _iid_ = Guid('{e5ecc834-ce66-4e05-a78f-cf391a5ec2d1}')
    @winrt_commethod(6)
    def get_AutoFocusEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AutoFocusEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AutoWhiteBalanceEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AutoWhiteBalanceEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_AutoExposureEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AutoExposureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_Bounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(13)
    def put_Bounds(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    AutoExposureEnabled = property(get_AutoExposureEnabled, put_AutoExposureEnabled)
    AutoFocusEnabled = property(get_AutoFocusEnabled, put_AutoFocusEnabled)
    AutoWhiteBalanceEnabled = property(get_AutoWhiteBalanceEnabled, put_AutoWhiteBalanceEnabled)
    Bounds = property(get_Bounds, put_Bounds)
class IRegionOfInterest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IRegionOfInterest2'
    _iid_ = Guid('{19fe2a91-73aa-4d51-8a9d-56ccf7db7f54}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Media.Devices.RegionOfInterestType: ...
    @winrt_commethod(7)
    def put_Type(self, value: win32more.Windows.Media.Devices.RegionOfInterestType) -> Void: ...
    @winrt_commethod(8)
    def get_BoundsNormalized(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_BoundsNormalized(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_Weight(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_Weight(self, value: UInt32) -> Void: ...
    BoundsNormalized = property(get_BoundsNormalized, put_BoundsNormalized)
    Type = property(get_Type, put_Type)
    Weight = property(get_Weight, put_Weight)
class IRegionsOfInterestControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IRegionsOfInterestControl'
    _iid_ = Guid('{c323f527-ab0b-4558-8b5b-df5693db0378}')
    @winrt_commethod(6)
    def get_MaxRegions(self) -> UInt32: ...
    @winrt_commethod(7)
    def SetRegionsAsync(self, regions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Devices.RegionOfInterest]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SetRegionsWithLockAsync(self, regions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Devices.RegionOfInterest], lockValues: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ClearRegionsAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def get_AutoFocusSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_AutoWhiteBalanceSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_AutoExposureSupported(self) -> Boolean: ...
    AutoExposureSupported = property(get_AutoExposureSupported, None)
    AutoFocusSupported = property(get_AutoFocusSupported, None)
    AutoWhiteBalanceSupported = property(get_AutoWhiteBalanceSupported, None)
    MaxRegions = property(get_MaxRegions, None)
class ISceneModeControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ISceneModeControl'
    _iid_ = Guid('{d48e5af7-8d59-4854-8c62-12c70ba89b7c}')
    @winrt_commethod(6)
    def get_SupportedModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Media.Devices.CaptureSceneMode: ...
    @winrt_commethod(8)
    def SetValueAsync(self, sceneMode: win32more.Windows.Media.Devices.CaptureSceneMode) -> win32more.Windows.Foundation.IAsyncAction: ...
    SupportedModes = property(get_SupportedModes, None)
    Value = property(get_Value, None)
class ITorchControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ITorchControl'
    _iid_ = Guid('{a6053665-8250-416c-919a-724296afa306}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_PowerSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_PowerPercent(self) -> Single: ...
    @winrt_commethod(11)
    def put_PowerPercent(self, value: Single) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
    PowerSupported = property(get_PowerSupported, None)
    Supported = property(get_Supported, None)
class IVideoDeviceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IVideoDeviceController'
    _iid_ = Guid('{99555575-2e2e-40b8-b6c7-f82d10013210}')
    @winrt_commethod(6)
    def get_Brightness(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(7)
    def get_Contrast(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(8)
    def get_Hue(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(9)
    def get_WhiteBalance(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(10)
    def get_BacklightCompensation(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(11)
    def get_Pan(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(12)
    def get_Tilt(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(13)
    def get_Zoom(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(14)
    def get_Roll(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(15)
    def get_Exposure(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(16)
    def get_Focus(self) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(17)
    def TrySetPowerlineFrequency(self, value: win32more.Windows.Media.Capture.PowerlineFrequency) -> Boolean: ...
    @winrt_commethod(18)
    def TryGetPowerlineFrequency(self, value: POINTER(win32more.Windows.Media.Capture.PowerlineFrequency)) -> Boolean: ...
    BacklightCompensation = property(get_BacklightCompensation, None)
    Brightness = property(get_Brightness, None)
    Contrast = property(get_Contrast, None)
    Exposure = property(get_Exposure, None)
    Focus = property(get_Focus, None)
    Hue = property(get_Hue, None)
    Pan = property(get_Pan, None)
    Roll = property(get_Roll, None)
    Tilt = property(get_Tilt, None)
    WhiteBalance = property(get_WhiteBalance, None)
    Zoom = property(get_Zoom, None)
class IVideoDeviceControllerGetDevicePropertyResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IVideoDeviceControllerGetDevicePropertyResult'
    _iid_ = Guid('{c5d88395-6ed5-4790-8b5d-0ef13935d0f8}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IVideoTemporalDenoisingControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IVideoTemporalDenoisingControl'
    _iid_ = Guid('{7ab34735-3e2a-4a32-baff-4358c4fbdd57}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.VideoTemporalDenoisingMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Windows.Media.Devices.VideoTemporalDenoisingMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: win32more.Windows.Media.Devices.VideoTemporalDenoisingMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class IWhiteBalanceControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IWhiteBalanceControl'
    _iid_ = Guid('{781f047e-7162-49c8-a8f9-9481c565363e}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Preset(self) -> win32more.Windows.Media.Devices.ColorTemperaturePreset: ...
    @winrt_commethod(8)
    def SetPresetAsync(self, preset: win32more.Windows.Media.Devices.ColorTemperaturePreset) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Step(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(13)
    def SetValueAsync(self, temperature: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Preset = property(get_Preset, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    Value = property(get_Value, None)
class IZoomControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IZoomControl'
    _iid_ = Guid('{3a1e0b12-32da-4c17-bfd7-8d0c73c8f5a5}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> Single: ...
    @winrt_commethod(8)
    def get_Max(self) -> Single: ...
    @winrt_commethod(9)
    def get_Step(self) -> Single: ...
    @winrt_commethod(10)
    def get_Value(self) -> Single: ...
    @winrt_commethod(11)
    def put_Value(self, value: Single) -> Void: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    Value = property(get_Value, put_Value)
class IZoomControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IZoomControl2'
    _iid_ = Guid('{69843db0-2e99-4641-8529-184f319d1671}')
    @winrt_commethod(6)
    def get_SupportedModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.ZoomTransitionMode]: ...
    @winrt_commethod(7)
    def get_Mode(self) -> win32more.Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_commethod(8)
    def Configure(self, settings: win32more.Windows.Media.Devices.ZoomSettings) -> Void: ...
    Mode = property(get_Mode, None)
    SupportedModes = property(get_SupportedModes, None)
class IZoomSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IZoomSettings'
    _iid_ = Guid('{6ad66b24-14b4-4bfd-b18f-88fe24463b52}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.Media.Devices.ZoomTransitionMode) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Single: ...
    @winrt_commethod(9)
    def put_Value(self, value: Single) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Value = property(get_Value, put_Value)
class InfraredTorchControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IInfraredTorchControl
    _classid_ = 'Windows.Media.Devices.InfraredTorchControl'
    @winrt_mixinmethod
    def get_IsSupported(self: win32more.Windows.Media.Devices.IInfraredTorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.IInfraredTorchControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.InfraredTorchMode]: ...
    @winrt_mixinmethod
    def get_CurrentMode(self: win32more.Windows.Media.Devices.IInfraredTorchControl) -> win32more.Windows.Media.Devices.InfraredTorchMode: ...
    @winrt_mixinmethod
    def put_CurrentMode(self: win32more.Windows.Media.Devices.IInfraredTorchControl, value: win32more.Windows.Media.Devices.InfraredTorchMode) -> Void: ...
    @winrt_mixinmethod
    def get_MinPower(self: win32more.Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxPower(self: win32more.Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def get_PowerStep(self: win32more.Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def get_Power(self: win32more.Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def put_Power(self: win32more.Windows.Media.Devices.IInfraredTorchControl, value: Int32) -> Void: ...
    CurrentMode = property(get_CurrentMode, put_CurrentMode)
    IsSupported = property(get_IsSupported, None)
    MaxPower = property(get_MaxPower, None)
    MinPower = property(get_MinPower, None)
    Power = property(get_Power, put_Power)
    PowerStep = property(get_PowerStep, None)
    SupportedModes = property(get_SupportedModes, None)
class InfraredTorchMode(Enum, Int32):
    Off = 0
    On = 1
    AlternatingFrameIllumination = 2
class IsoSpeedControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IIsoSpeedControl
    _classid_ = 'Windows.Media.Devices.IsoSpeedControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IIsoSpeedControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedPresets(self: win32more.Windows.Media.Devices.IIsoSpeedControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.IsoSpeedPreset]: ...
    @winrt_mixinmethod
    def get_Preset(self: win32more.Windows.Media.Devices.IIsoSpeedControl) -> win32more.Windows.Media.Devices.IsoSpeedPreset: ...
    @winrt_mixinmethod
    def SetPresetAsync(self: win32more.Windows.Media.Devices.IIsoSpeedControl, preset: win32more.Windows.Media.Devices.IsoSpeedPreset) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def SetValueAsync(self: win32more.Windows.Media.Devices.IIsoSpeedControl2, isoSpeed: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Auto(self: win32more.Windows.Media.Devices.IIsoSpeedControl2) -> Boolean: ...
    @winrt_mixinmethod
    def SetAutoAsync(self: win32more.Windows.Media.Devices.IIsoSpeedControl2) -> win32more.Windows.Foundation.IAsyncAction: ...
    Auto = property(get_Auto, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Preset = property(get_Preset, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    SupportedPresets = property(get_SupportedPresets, None)
    Value = property(get_Value, None)
class IsoSpeedPreset(Enum, Int32):
    Auto = 0
    Iso50 = 1
    Iso80 = 2
    Iso100 = 3
    Iso200 = 4
    Iso400 = 5
    Iso800 = 6
    Iso1600 = 7
    Iso3200 = 8
    Iso6400 = 9
    Iso12800 = 10
    Iso25600 = 11
class KeypadPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IKeypadPressedEventArgs
    _classid_ = 'Windows.Media.Devices.KeypadPressedEventArgs'
    @winrt_mixinmethod
    def get_TelephonyKey(self: win32more.Windows.Media.Devices.IKeypadPressedEventArgs) -> win32more.Windows.Media.Devices.TelephonyKey: ...
    TelephonyKey = property(get_TelephonyKey, None)
class KeypadPressedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e637a454-c527-422c-8926-c9af83b559a0}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Devices.CallControl, e: win32more.Windows.Media.Devices.KeypadPressedEventArgs) -> Void: ...
class LowLagPhotoControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ILowLagPhotoControl
    _classid_ = 'Windows.Media.Devices.LowLagPhotoControl'
    @winrt_mixinmethod
    def GetHighestConcurrentFrameRate(self: win32more.Windows.Media.Devices.ILowLagPhotoControl, captureProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def GetCurrentFrameRate(self: win32more.Windows.Media.Devices.ILowLagPhotoControl) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_ThumbnailEnabled(self: win32more.Windows.Media.Devices.ILowLagPhotoControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_ThumbnailEnabled(self: win32more.Windows.Media.Devices.ILowLagPhotoControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ThumbnailFormat(self: win32more.Windows.Media.Devices.ILowLagPhotoControl) -> win32more.Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_mixinmethod
    def put_ThumbnailFormat(self: win32more.Windows.Media.Devices.ILowLagPhotoControl, value: win32more.Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredThumbnailSize(self: win32more.Windows.Media.Devices.ILowLagPhotoControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_DesiredThumbnailSize(self: win32more.Windows.Media.Devices.ILowLagPhotoControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HardwareAcceleratedThumbnailSupported(self: win32more.Windows.Media.Devices.ILowLagPhotoControl) -> UInt32: ...
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
class LowLagPhotoSequenceControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl
    _classid_ = 'Windows.Media.Devices.LowLagPhotoSequenceControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPastPhotos(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxPhotosPerSecond(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Single: ...
    @winrt_mixinmethod
    def get_PastPhotoLimit(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_PastPhotoLimit(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PhotosPerSecondLimit(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Single: ...
    @winrt_mixinmethod
    def put_PhotosPerSecondLimit(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl, value: Single) -> Void: ...
    @winrt_mixinmethod
    def GetHighestConcurrentFrameRate(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl, captureProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def GetCurrentFrameRate(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_ThumbnailEnabled(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_ThumbnailEnabled(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ThumbnailFormat(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> win32more.Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_mixinmethod
    def put_ThumbnailFormat(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl, value: win32more.Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredThumbnailSize(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_DesiredThumbnailSize(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HardwareAcceleratedThumbnailSupported(self: win32more.Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
    MaxPastPhotos = property(get_MaxPastPhotos, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PastPhotoLimit = property(get_PastPhotoLimit, put_PastPhotoLimit)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    Supported = property(get_Supported, None)
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
class ManualFocusDistance(Enum, Int32):
    Infinity = 0
    Hyperfocal = 1
    Nearest = 2
class MediaCaptureFocusState(Enum, Int32):
    Uninitialized = 0
    Lost = 1
    Searching = 2
    Focused = 3
    Failed = 4
class MediaCaptureOptimization(Enum, Int32):
    Default = 0
    Quality = 1
    Latency = 2
    Power = 3
    LatencyThenQuality = 4
    LatencyThenPower = 5
    PowerAndQuality = 6
class MediaCapturePauseBehavior(Enum, Int32):
    RetainHardwareResources = 0
    ReleaseHardwareResources = 1
class MediaDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.MediaDevice'
    @winrt_classmethod
    def GetAudioCaptureSelector(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetAudioRenderSelector(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetVideoCaptureSelector(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAudioCaptureId(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAudioRenderId(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics, role: win32more.Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_classmethod
    def add_DefaultAudioCaptureDeviceChanged(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Media.Devices.DefaultAudioCaptureDeviceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DefaultAudioCaptureDeviceChanged(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_DefaultAudioRenderDeviceChanged(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Media.Devices.DefaultAudioRenderDeviceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DefaultAudioRenderDeviceChanged(cls: win32more.Windows.Media.Devices.IMediaDeviceStatics, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class MediaDeviceControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IMediaDeviceControl
    _classid_ = 'Windows.Media.Devices.MediaDeviceControl'
    @winrt_mixinmethod
    def get_Capabilities(self: win32more.Windows.Media.Devices.IMediaDeviceControl) -> win32more.Windows.Media.Devices.MediaDeviceControlCapabilities: ...
    @winrt_mixinmethod
    def TryGetValue(self: win32more.Windows.Media.Devices.IMediaDeviceControl, value: POINTER(Double)) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetValue(self: win32more.Windows.Media.Devices.IMediaDeviceControl, value: Double) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetAuto(self: win32more.Windows.Media.Devices.IMediaDeviceControl, value: POINTER(Boolean)) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetAuto(self: win32more.Windows.Media.Devices.IMediaDeviceControl, value: Boolean) -> Boolean: ...
    Capabilities = property(get_Capabilities, None)
class MediaDeviceControlCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IMediaDeviceControlCapabilities
    _classid_ = 'Windows.Media.Devices.MediaDeviceControlCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_Default(self: win32more.Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_AutoModeSupported(self: win32more.Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Boolean: ...
    AutoModeSupported = property(get_AutoModeSupported, None)
    Default = property(get_Default, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class ModuleCommandResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IModuleCommandResult
    _classid_ = 'Windows.Media.Devices.ModuleCommandResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Devices.IModuleCommandResult) -> win32more.Windows.Media.Devices.SendCommandStatus: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Media.Devices.IModuleCommandResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class OpticalImageStabilizationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IOpticalImageStabilizationControl
    _classid_ = 'Windows.Media.Devices.OpticalImageStabilizationControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IOpticalImageStabilizationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.IOpticalImageStabilizationControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.OpticalImageStabilizationMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IOpticalImageStabilizationControl) -> win32more.Windows.Media.Devices.OpticalImageStabilizationMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Devices.IOpticalImageStabilizationControl, value: win32more.Windows.Media.Devices.OpticalImageStabilizationMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class OpticalImageStabilizationMode(Enum, Int32):
    Off = 0
    On = 1
    Auto = 2
class PanelBasedOptimizationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IPanelBasedOptimizationControl
    _classid_ = 'Windows.Media.Devices.PanelBasedOptimizationControl'
    @winrt_mixinmethod
    def get_IsSupported(self: win32more.Windows.Media.Devices.IPanelBasedOptimizationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Panel(self: win32more.Windows.Media.Devices.IPanelBasedOptimizationControl) -> win32more.Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def put_Panel(self: win32more.Windows.Media.Devices.IPanelBasedOptimizationControl, value: win32more.Windows.Devices.Enumeration.Panel) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    Panel = property(get_Panel, put_Panel)
class PhotoConfirmationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IPhotoConfirmationControl
    _classid_ = 'Windows.Media.Devices.PhotoConfirmationControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IPhotoConfirmationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Media.Devices.IPhotoConfirmationControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Media.Devices.IPhotoConfirmationControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: win32more.Windows.Media.Devices.IPhotoConfirmationControl) -> win32more.Windows.Media.MediaProperties.MediaPixelFormat: ...
    @winrt_mixinmethod
    def put_PixelFormat(self: win32more.Windows.Media.Devices.IPhotoConfirmationControl, format: win32more.Windows.Media.MediaProperties.MediaPixelFormat) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
    Supported = property(get_Supported, None)
class RedialRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IRedialRequestedEventArgs
    _classid_ = 'Windows.Media.Devices.RedialRequestedEventArgs'
    @winrt_mixinmethod
    def Handled(self: win32more.Windows.Media.Devices.IRedialRequestedEventArgs) -> Void: ...
class RedialRequestedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{baf257d1-4ebd-4b84-9f47-6ec43d75d8b1}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Devices.CallControl, e: win32more.Windows.Media.Devices.RedialRequestedEventArgs) -> Void: ...
class RegionOfInterest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IRegionOfInterest
    _classid_ = 'Windows.Media.Devices.RegionOfInterest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Devices.RegionOfInterest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Devices.RegionOfInterest: ...
    @winrt_mixinmethod
    def get_AutoFocusEnabled(self: win32more.Windows.Media.Devices.IRegionOfInterest) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoFocusEnabled(self: win32more.Windows.Media.Devices.IRegionOfInterest, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutoWhiteBalanceEnabled(self: win32more.Windows.Media.Devices.IRegionOfInterest) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoWhiteBalanceEnabled(self: win32more.Windows.Media.Devices.IRegionOfInterest, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutoExposureEnabled(self: win32more.Windows.Media.Devices.IRegionOfInterest) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoExposureEnabled(self: win32more.Windows.Media.Devices.IRegionOfInterest, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.Media.Devices.IRegionOfInterest) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_Bounds(self: win32more.Windows.Media.Devices.IRegionOfInterest, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Devices.IRegionOfInterest2) -> win32more.Windows.Media.Devices.RegionOfInterestType: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Windows.Media.Devices.IRegionOfInterest2, value: win32more.Windows.Media.Devices.RegionOfInterestType) -> Void: ...
    @winrt_mixinmethod
    def get_BoundsNormalized(self: win32more.Windows.Media.Devices.IRegionOfInterest2) -> Boolean: ...
    @winrt_mixinmethod
    def put_BoundsNormalized(self: win32more.Windows.Media.Devices.IRegionOfInterest2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Weight(self: win32more.Windows.Media.Devices.IRegionOfInterest2) -> UInt32: ...
    @winrt_mixinmethod
    def put_Weight(self: win32more.Windows.Media.Devices.IRegionOfInterest2, value: UInt32) -> Void: ...
    AutoExposureEnabled = property(get_AutoExposureEnabled, put_AutoExposureEnabled)
    AutoFocusEnabled = property(get_AutoFocusEnabled, put_AutoFocusEnabled)
    AutoWhiteBalanceEnabled = property(get_AutoWhiteBalanceEnabled, put_AutoWhiteBalanceEnabled)
    Bounds = property(get_Bounds, put_Bounds)
    BoundsNormalized = property(get_BoundsNormalized, put_BoundsNormalized)
    Type = property(get_Type, put_Type)
    Weight = property(get_Weight, put_Weight)
class RegionOfInterestType(Enum, Int32):
    Unknown = 0
    Face = 1
class RegionsOfInterestControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IRegionsOfInterestControl
    _classid_ = 'Windows.Media.Devices.RegionsOfInterestControl'
    @winrt_mixinmethod
    def get_MaxRegions(self: win32more.Windows.Media.Devices.IRegionsOfInterestControl) -> UInt32: ...
    @winrt_mixinmethod
    def SetRegionsAsync(self: win32more.Windows.Media.Devices.IRegionsOfInterestControl, regions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Devices.RegionOfInterest]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRegionsWithLockAsync(self: win32more.Windows.Media.Devices.IRegionsOfInterestControl, regions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Devices.RegionOfInterest], lockValues: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearRegionsAsync(self: win32more.Windows.Media.Devices.IRegionsOfInterestControl) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_AutoFocusSupported(self: win32more.Windows.Media.Devices.IRegionsOfInterestControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutoWhiteBalanceSupported(self: win32more.Windows.Media.Devices.IRegionsOfInterestControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutoExposureSupported(self: win32more.Windows.Media.Devices.IRegionsOfInterestControl) -> Boolean: ...
    AutoExposureSupported = property(get_AutoExposureSupported, None)
    AutoFocusSupported = property(get_AutoFocusSupported, None)
    AutoWhiteBalanceSupported = property(get_AutoWhiteBalanceSupported, None)
    MaxRegions = property(get_MaxRegions, None)
class SceneModeControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ISceneModeControl
    _classid_ = 'Windows.Media.Devices.SceneModeControl'
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.ISceneModeControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.ISceneModeControl) -> win32more.Windows.Media.Devices.CaptureSceneMode: ...
    @winrt_mixinmethod
    def SetValueAsync(self: win32more.Windows.Media.Devices.ISceneModeControl, sceneMode: win32more.Windows.Media.Devices.CaptureSceneMode) -> win32more.Windows.Foundation.IAsyncAction: ...
    SupportedModes = property(get_SupportedModes, None)
    Value = property(get_Value, None)
class SendCommandStatus(Enum, Int32):
    Success = 0
    DeviceNotAvailable = 1
class TelephonyKey(Enum, Int32):
    D0 = 0
    D1 = 1
    D2 = 2
    D3 = 3
    D4 = 4
    D5 = 5
    D6 = 6
    D7 = 7
    D8 = 8
    D9 = 9
    Star = 10
    Pound = 11
    A = 12
    B = 13
    C = 14
    D = 15
class TorchControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.ITorchControl
    _classid_ = 'Windows.Media.Devices.TorchControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.ITorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerSupported(self: win32more.Windows.Media.Devices.ITorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Media.Devices.ITorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Media.Devices.ITorchControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PowerPercent(self: win32more.Windows.Media.Devices.ITorchControl) -> Single: ...
    @winrt_mixinmethod
    def put_PowerPercent(self: win32more.Windows.Media.Devices.ITorchControl, value: Single) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
    PowerSupported = property(get_PowerSupported, None)
    Supported = property(get_Supported, None)
class VideoDeviceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IVideoDeviceController
    _classid_ = 'Windows.Media.Devices.VideoDeviceController'
    @winrt_mixinmethod
    def get_Brightness(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Contrast(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Hue(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_WhiteBalance(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_BacklightCompensation(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Pan(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Tilt(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Zoom(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Roll(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Exposure(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Focus(self: win32more.Windows.Media.Devices.IVideoDeviceController) -> win32more.Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def TrySetPowerlineFrequency(self: win32more.Windows.Media.Devices.IVideoDeviceController, value: win32more.Windows.Media.Capture.PowerlineFrequency) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetPowerlineFrequency(self: win32more.Windows.Media.Devices.IVideoDeviceController, value: POINTER(win32more.Windows.Media.Capture.PowerlineFrequency)) -> Boolean: ...
    @winrt_mixinmethod
    def GetAvailableMediaStreamProperties(self: win32more.Windows.Media.Devices.IMediaDeviceController, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.MediaProperties.IMediaEncodingProperties]: ...
    @winrt_mixinmethod
    def GetMediaStreamProperties(self: win32more.Windows.Media.Devices.IMediaDeviceController, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType) -> win32more.Windows.Media.MediaProperties.IMediaEncodingProperties: ...
    @winrt_mixinmethod
    def SetMediaStreamPropertiesAsync(self: win32more.Windows.Media.Devices.IMediaDeviceController, mediaStreamType: win32more.Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetDeviceProperty(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController, propertyId: WinRT_String, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def GetDeviceProperty(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController, propertyId: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_LowLagPhotoSequence(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.LowLagPhotoSequenceControl: ...
    @winrt_mixinmethod
    def get_LowLagPhoto(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.LowLagPhotoControl: ...
    @winrt_mixinmethod
    def get_SceneModeControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.SceneModeControl: ...
    @winrt_mixinmethod
    def get_TorchControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.TorchControl: ...
    @winrt_mixinmethod
    def get_FlashControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.FlashControl: ...
    @winrt_mixinmethod
    def get_WhiteBalanceControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.WhiteBalanceControl: ...
    @winrt_mixinmethod
    def get_ExposureControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.ExposureControl: ...
    @winrt_mixinmethod
    def get_FocusControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.FocusControl: ...
    @winrt_mixinmethod
    def get_ExposureCompensationControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.ExposureCompensationControl: ...
    @winrt_mixinmethod
    def get_IsoSpeedControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.IsoSpeedControl: ...
    @winrt_mixinmethod
    def get_RegionsOfInterestControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.RegionsOfInterestControl: ...
    @winrt_mixinmethod
    def get_PrimaryUse(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> win32more.Windows.Media.Devices.CaptureUse: ...
    @winrt_mixinmethod
    def put_PrimaryUse(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2, value: win32more.Windows.Media.Devices.CaptureUse) -> Void: ...
    @winrt_mixinmethod
    def get_VariablePhotoSequenceController(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController3) -> win32more.Windows.Media.Devices.Core.VariablePhotoSequenceController: ...
    @winrt_mixinmethod
    def get_PhotoConfirmationControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController3) -> win32more.Windows.Media.Devices.PhotoConfirmationControl: ...
    @winrt_mixinmethod
    def get_ZoomControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController3) -> win32more.Windows.Media.Devices.ZoomControl: ...
    @winrt_mixinmethod
    def get_ExposurePriorityVideoControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> win32more.Windows.Media.Devices.ExposurePriorityVideoControl: ...
    @winrt_mixinmethod
    def get_DesiredOptimization(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> win32more.Windows.Media.Devices.MediaCaptureOptimization: ...
    @winrt_mixinmethod
    def put_DesiredOptimization(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4, value: win32more.Windows.Media.Devices.MediaCaptureOptimization) -> Void: ...
    @winrt_mixinmethod
    def get_HdrVideoControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> win32more.Windows.Media.Devices.HdrVideoControl: ...
    @winrt_mixinmethod
    def get_OpticalImageStabilizationControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> win32more.Windows.Media.Devices.OpticalImageStabilizationControl: ...
    @winrt_mixinmethod
    def get_AdvancedPhotoControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> win32more.Windows.Media.Devices.AdvancedPhotoControl: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDevicePropertyById(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, propertyId: WinRT_String, maxPropertyValueSize: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_mixinmethod
    def SetDevicePropertyById(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, propertyId: WinRT_String, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    @winrt_mixinmethod
    def GetDevicePropertyByExtendedId(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, extendedPropertyId: PassArray[Byte], maxPropertyValueSize: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_mixinmethod
    def SetDevicePropertyByExtendedId(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, extendedPropertyId: PassArray[Byte], propertyValue: PassArray[Byte]) -> win32more.Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    @winrt_mixinmethod
    def get_VideoTemporalDenoisingControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController6) -> win32more.Windows.Media.Devices.VideoTemporalDenoisingControl: ...
    @winrt_mixinmethod
    def get_InfraredTorchControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController7) -> win32more.Windows.Media.Devices.InfraredTorchControl: ...
    @winrt_mixinmethod
    def get_PanelBasedOptimizationControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController8) -> win32more.Windows.Media.Devices.PanelBasedOptimizationControl: ...
    @winrt_mixinmethod
    def get_DigitalWindowControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController9) -> win32more.Windows.Media.Devices.DigitalWindowControl: ...
    @winrt_mixinmethod
    def get_CameraOcclusionInfo(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController10) -> win32more.Windows.Media.Devices.CameraOcclusionInfo: ...
    @winrt_mixinmethod
    def TryAcquireExclusiveControl(self: win32more.Windows.Media.Devices.IAdvancedVideoCaptureDeviceController11, deviceId: WinRT_String, mode: win32more.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlReleaseMode) -> Boolean: ...
    AdvancedPhotoControl = property(get_AdvancedPhotoControl, None)
    BacklightCompensation = property(get_BacklightCompensation, None)
    Brightness = property(get_Brightness, None)
    CameraOcclusionInfo = property(get_CameraOcclusionInfo, None)
    Contrast = property(get_Contrast, None)
    DesiredOptimization = property(get_DesiredOptimization, put_DesiredOptimization)
    DigitalWindowControl = property(get_DigitalWindowControl, None)
    Exposure = property(get_Exposure, None)
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    ExposureControl = property(get_ExposureControl, None)
    ExposurePriorityVideoControl = property(get_ExposurePriorityVideoControl, None)
    FlashControl = property(get_FlashControl, None)
    Focus = property(get_Focus, None)
    FocusControl = property(get_FocusControl, None)
    HdrVideoControl = property(get_HdrVideoControl, None)
    Hue = property(get_Hue, None)
    Id = property(get_Id, None)
    InfraredTorchControl = property(get_InfraredTorchControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    LowLagPhoto = property(get_LowLagPhoto, None)
    LowLagPhotoSequence = property(get_LowLagPhotoSequence, None)
    OpticalImageStabilizationControl = property(get_OpticalImageStabilizationControl, None)
    Pan = property(get_Pan, None)
    PanelBasedOptimizationControl = property(get_PanelBasedOptimizationControl, None)
    PhotoConfirmationControl = property(get_PhotoConfirmationControl, None)
    PrimaryUse = property(get_PrimaryUse, put_PrimaryUse)
    RegionsOfInterestControl = property(get_RegionsOfInterestControl, None)
    Roll = property(get_Roll, None)
    SceneModeControl = property(get_SceneModeControl, None)
    Tilt = property(get_Tilt, None)
    TorchControl = property(get_TorchControl, None)
    VariablePhotoSequenceController = property(get_VariablePhotoSequenceController, None)
    VideoTemporalDenoisingControl = property(get_VideoTemporalDenoisingControl, None)
    WhiteBalance = property(get_WhiteBalance, None)
    WhiteBalanceControl = property(get_WhiteBalanceControl, None)
    Zoom = property(get_Zoom, None)
    ZoomControl = property(get_ZoomControl, None)
class VideoDeviceControllerGetDevicePropertyResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IVideoDeviceControllerGetDevicePropertyResult
    _classid_ = 'Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Devices.IVideoDeviceControllerGetDevicePropertyResult) -> win32more.Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyStatus: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IVideoDeviceControllerGetDevicePropertyResult) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class VideoDeviceControllerGetDevicePropertyStatus(Enum, Int32):
    Success = 0
    UnknownFailure = 1
    BufferTooSmall = 2
    NotSupported = 3
    DeviceNotAvailable = 4
    MaxPropertyValueSizeTooSmall = 5
    MaxPropertyValueSizeRequired = 6
class VideoDeviceControllerSetDevicePropertyStatus(Enum, Int32):
    Success = 0
    UnknownFailure = 1
    NotSupported = 2
    InvalidValue = 3
    DeviceNotAvailable = 4
    NotInControl = 5
class VideoTemporalDenoisingControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IVideoTemporalDenoisingControl
    _classid_ = 'Windows.Media.Devices.VideoTemporalDenoisingControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IVideoTemporalDenoisingControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.IVideoTemporalDenoisingControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.VideoTemporalDenoisingMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IVideoTemporalDenoisingControl) -> win32more.Windows.Media.Devices.VideoTemporalDenoisingMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Devices.IVideoTemporalDenoisingControl, value: win32more.Windows.Media.Devices.VideoTemporalDenoisingMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
class VideoTemporalDenoisingMode(Enum, Int32):
    Off = 0
    On = 1
    Auto = 2
class WhiteBalanceControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IWhiteBalanceControl
    _classid_ = 'Windows.Media.Devices.WhiteBalanceControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IWhiteBalanceControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Preset(self: win32more.Windows.Media.Devices.IWhiteBalanceControl) -> win32more.Windows.Media.Devices.ColorTemperaturePreset: ...
    @winrt_mixinmethod
    def SetPresetAsync(self: win32more.Windows.Media.Devices.IWhiteBalanceControl, preset: win32more.Windows.Media.Devices.ColorTemperaturePreset) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def SetValueAsync(self: win32more.Windows.Media.Devices.IWhiteBalanceControl, temperature: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Preset = property(get_Preset, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    Value = property(get_Value, None)
class ZoomControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IZoomControl
    _classid_ = 'Windows.Media.Devices.ZoomControl'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.IZoomControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Media.Devices.IZoomControl, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: win32more.Windows.Media.Devices.IZoomControl2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.ZoomTransitionMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IZoomControl2) -> win32more.Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_mixinmethod
    def Configure(self: win32more.Windows.Media.Devices.IZoomControl2, settings: win32more.Windows.Media.Devices.ZoomSettings) -> Void: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Mode = property(get_Mode, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Value = property(get_Value, put_Value)
class ZoomSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.IZoomSettings
    _classid_ = 'Windows.Media.Devices.ZoomSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Devices.ZoomSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Devices.ZoomSettings: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.IZoomSettings) -> win32more.Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Devices.IZoomSettings, value: win32more.Windows.Media.Devices.ZoomTransitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.IZoomSettings) -> Single: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Media.Devices.IZoomSettings, value: Single) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Value = property(get_Value, put_Value)
class ZoomTransitionMode(Enum, Int32):
    Auto = 0
    Direct = 1
    Smooth = 2


make_ready(__name__)
