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
import Windows.Media.Capture
import Windows.Media.Devices
import Windows.Media.Devices.Core
import Windows.Media.MediaProperties
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
class AdvancedPhotoCaptureSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.AdvancedPhotoCaptureSettings'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Devices.AdvancedPhotoCaptureSettings: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IAdvancedPhotoCaptureSettings) -> Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Devices.IAdvancedPhotoCaptureSettings, value: Windows.Media.Devices.AdvancedPhotoMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class AdvancedPhotoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.AdvancedPhotoControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IAdvancedPhotoControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.IAdvancedPhotoControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AdvancedPhotoMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IAdvancedPhotoControl) -> Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_mixinmethod
    def Configure(self: Windows.Media.Devices.IAdvancedPhotoControl, settings: Windows.Media.Devices.AdvancedPhotoCaptureSettings) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, None)
AdvancedPhotoMode = Int32
AdvancedPhotoMode_Auto: AdvancedPhotoMode = 0
AdvancedPhotoMode_Standard: AdvancedPhotoMode = 1
AdvancedPhotoMode_Hdr: AdvancedPhotoMode = 2
AdvancedPhotoMode_LowLight: AdvancedPhotoMode = 3
class AudioDeviceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.AudioDeviceController'
    @winrt_mixinmethod
    def put_Muted(self: Windows.Media.Devices.IAudioDeviceController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Muted(self: Windows.Media.Devices.IAudioDeviceController) -> Boolean: ...
    @winrt_mixinmethod
    def put_VolumePercent(self: Windows.Media.Devices.IAudioDeviceController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_VolumePercent(self: Windows.Media.Devices.IAudioDeviceController) -> Single: ...
    @winrt_mixinmethod
    def GetAvailableMediaStreamProperties(self: Windows.Media.Devices.IMediaDeviceController, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Foundation.Collections.IVectorView[Windows.Media.MediaProperties.IMediaEncodingProperties]: ...
    @winrt_mixinmethod
    def GetMediaStreamProperties(self: Windows.Media.Devices.IMediaDeviceController, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Media.MediaProperties.IMediaEncodingProperties: ...
    @winrt_mixinmethod
    def SetMediaStreamPropertiesAsync(self: Windows.Media.Devices.IMediaDeviceController, mediaStreamType: Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Foundation.IAsyncAction: ...
    Muted = property(get_Muted, put_Muted)
    VolumePercent = property(get_VolumePercent, put_VolumePercent)
class AudioDeviceModule(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.AudioDeviceModule'
    @winrt_mixinmethod
    def get_ClassId(self: Windows.Media.Devices.IAudioDeviceModule) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Media.Devices.IAudioDeviceModule) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstanceId(self: Windows.Media.Devices.IAudioDeviceModule) -> UInt32: ...
    @winrt_mixinmethod
    def get_MajorVersion(self: Windows.Media.Devices.IAudioDeviceModule) -> UInt32: ...
    @winrt_mixinmethod
    def get_MinorVersion(self: Windows.Media.Devices.IAudioDeviceModule) -> UInt32: ...
    @winrt_mixinmethod
    def SendCommandAsync(self: Windows.Media.Devices.IAudioDeviceModule, Command: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Media.Devices.ModuleCommandResult]: ...
    ClassId = property(get_ClassId, None)
    DisplayName = property(get_DisplayName, None)
    InstanceId = property(get_InstanceId, None)
    MajorVersion = property(get_MajorVersion, None)
    MinorVersion = property(get_MinorVersion, None)
class AudioDeviceModuleNotificationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.AudioDeviceModuleNotificationEventArgs'
    @winrt_mixinmethod
    def get_Module(self: Windows.Media.Devices.IAudioDeviceModuleNotificationEventArgs) -> Windows.Media.Devices.AudioDeviceModule: ...
    @winrt_mixinmethod
    def get_NotificationData(self: Windows.Media.Devices.IAudioDeviceModuleNotificationEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    Module = property(get_Module, None)
    NotificationData = property(get_NotificationData, None)
class AudioDeviceModulesManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.AudioDeviceModulesManager'
    @winrt_factorymethod
    def Create(cls: Windows.Media.Devices.IAudioDeviceModulesManagerFactory, deviceId: WinRT_String) -> Windows.Media.Devices.AudioDeviceModulesManager: ...
    @winrt_mixinmethod
    def add_ModuleNotificationReceived(self: Windows.Media.Devices.IAudioDeviceModulesManager, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Devices.AudioDeviceModulesManager, Windows.Media.Devices.AudioDeviceModuleNotificationEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ModuleNotificationReceived(self: Windows.Media.Devices.IAudioDeviceModulesManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindAllById(self: Windows.Media.Devices.IAudioDeviceModulesManager, moduleId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AudioDeviceModule]: ...
    @winrt_mixinmethod
    def FindAll(self: Windows.Media.Devices.IAudioDeviceModulesManager) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AudioDeviceModule]: ...
AudioDeviceRole = Int32
AudioDeviceRole_Default: AudioDeviceRole = 0
AudioDeviceRole_Communications: AudioDeviceRole = 1
AutoFocusRange = Int32
AutoFocusRange_FullRange: AutoFocusRange = 0
AutoFocusRange_Macro: AutoFocusRange = 1
AutoFocusRange_Normal: AutoFocusRange = 2
class CameraOcclusionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.CameraOcclusionInfo'
    @winrt_mixinmethod
    def GetState(self: Windows.Media.Devices.ICameraOcclusionInfo) -> Windows.Media.Devices.CameraOcclusionState: ...
    @winrt_mixinmethod
    def IsOcclusionKindSupported(self: Windows.Media.Devices.ICameraOcclusionInfo, occlusionKind: Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Media.Devices.ICameraOcclusionInfo, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Devices.CameraOcclusionInfo, Windows.Media.Devices.CameraOcclusionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Media.Devices.ICameraOcclusionInfo, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
CameraOcclusionKind = Int32
CameraOcclusionKind_Lid: CameraOcclusionKind = 0
CameraOcclusionKind_CameraHardware: CameraOcclusionKind = 1
class CameraOcclusionState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.CameraOcclusionState'
    @winrt_mixinmethod
    def get_IsOccluded(self: Windows.Media.Devices.ICameraOcclusionState) -> Boolean: ...
    @winrt_mixinmethod
    def IsOcclusionKind(self: Windows.Media.Devices.ICameraOcclusionState, occlusionKind: Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    IsOccluded = property(get_IsOccluded, None)
class CameraOcclusionStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.CameraOcclusionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: Windows.Media.Devices.ICameraOcclusionStateChangedEventArgs) -> Windows.Media.Devices.CameraOcclusionState: ...
    State = property(get_State, None)
CameraStreamState = Int32
CameraStreamState_NotStreaming: CameraStreamState = 0
CameraStreamState_Streaming: CameraStreamState = 1
CameraStreamState_BlockedForPrivacy: CameraStreamState = 2
CameraStreamState_Shutdown: CameraStreamState = 3
CaptureSceneMode = Int32
CaptureSceneMode_Auto: CaptureSceneMode = 0
CaptureSceneMode_Manual: CaptureSceneMode = 1
CaptureSceneMode_Macro: CaptureSceneMode = 2
CaptureSceneMode_Portrait: CaptureSceneMode = 3
CaptureSceneMode_Sport: CaptureSceneMode = 4
CaptureSceneMode_Snow: CaptureSceneMode = 5
CaptureSceneMode_Night: CaptureSceneMode = 6
CaptureSceneMode_Beach: CaptureSceneMode = 7
CaptureSceneMode_Sunset: CaptureSceneMode = 8
CaptureSceneMode_Candlelight: CaptureSceneMode = 9
CaptureSceneMode_Landscape: CaptureSceneMode = 10
CaptureSceneMode_NightPortrait: CaptureSceneMode = 11
CaptureSceneMode_Backlit: CaptureSceneMode = 12
CaptureUse = Int32
CaptureUse_None: CaptureUse = 0
CaptureUse_Photo: CaptureUse = 1
CaptureUse_Video: CaptureUse = 2
ColorTemperaturePreset = Int32
ColorTemperaturePreset_Auto: ColorTemperaturePreset = 0
ColorTemperaturePreset_Manual: ColorTemperaturePreset = 1
ColorTemperaturePreset_Cloudy: ColorTemperaturePreset = 2
ColorTemperaturePreset_Daylight: ColorTemperaturePreset = 3
ColorTemperaturePreset_Flash: ColorTemperaturePreset = 4
ColorTemperaturePreset_Fluorescent: ColorTemperaturePreset = 5
ColorTemperaturePreset_Tungsten: ColorTemperaturePreset = 6
ColorTemperaturePreset_Candlelight: ColorTemperaturePreset = 7
class DefaultAudioCaptureDeviceChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.DefaultAudioCaptureDeviceChangedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Role(self: Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> Windows.Media.Devices.AudioDeviceRole: ...
    Id = property(get_Id, None)
    Role = property(get_Role, None)
class DefaultAudioRenderDeviceChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.DefaultAudioRenderDeviceChangedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Role(self: Windows.Media.Devices.IDefaultAudioDeviceChangedEventArgs) -> Windows.Media.Devices.AudioDeviceRole: ...
    Id = property(get_Id, None)
    Role = property(get_Role, None)
class DigitalWindowBounds(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.DigitalWindowBounds'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Devices.DigitalWindowBounds: ...
    @winrt_mixinmethod
    def get_NormalizedOriginTop(self: Windows.Media.Devices.IDigitalWindowBounds) -> Double: ...
    @winrt_mixinmethod
    def put_NormalizedOriginTop(self: Windows.Media.Devices.IDigitalWindowBounds, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_NormalizedOriginLeft(self: Windows.Media.Devices.IDigitalWindowBounds) -> Double: ...
    @winrt_mixinmethod
    def put_NormalizedOriginLeft(self: Windows.Media.Devices.IDigitalWindowBounds, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.Media.Devices.IDigitalWindowBounds) -> Double: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.Media.Devices.IDigitalWindowBounds, value: Double) -> Void: ...
    NormalizedOriginTop = property(get_NormalizedOriginTop, put_NormalizedOriginTop)
    NormalizedOriginLeft = property(get_NormalizedOriginLeft, put_NormalizedOriginLeft)
    Scale = property(get_Scale, put_Scale)
class DigitalWindowCapability(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.DigitalWindowCapability'
    @winrt_mixinmethod
    def get_Width(self: Windows.Media.Devices.IDigitalWindowCapability) -> Int32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Media.Devices.IDigitalWindowCapability) -> Int32: ...
    @winrt_mixinmethod
    def get_MinScaleValue(self: Windows.Media.Devices.IDigitalWindowCapability) -> Double: ...
    @winrt_mixinmethod
    def get_MaxScaleValue(self: Windows.Media.Devices.IDigitalWindowCapability) -> Double: ...
    @winrt_mixinmethod
    def get_MinScaleValueWithoutUpsampling(self: Windows.Media.Devices.IDigitalWindowCapability) -> Double: ...
    @winrt_mixinmethod
    def get_NormalizedFieldOfViewLimit(self: Windows.Media.Devices.IDigitalWindowCapability) -> Windows.Foundation.Rect: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    MinScaleValue = property(get_MinScaleValue, None)
    MaxScaleValue = property(get_MaxScaleValue, None)
    MinScaleValueWithoutUpsampling = property(get_MinScaleValueWithoutUpsampling, None)
    NormalizedFieldOfViewLimit = property(get_NormalizedFieldOfViewLimit, None)
class DigitalWindowControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.DigitalWindowControl'
    @winrt_mixinmethod
    def get_IsSupported(self: Windows.Media.Devices.IDigitalWindowControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.IDigitalWindowControl) -> POINTER(Windows.Media.Devices.DigitalWindowMode): ...
    @winrt_mixinmethod
    def get_CurrentMode(self: Windows.Media.Devices.IDigitalWindowControl) -> Windows.Media.Devices.DigitalWindowMode: ...
    @winrt_mixinmethod
    def GetBounds(self: Windows.Media.Devices.IDigitalWindowControl) -> Windows.Media.Devices.DigitalWindowBounds: ...
    @winrt_mixinmethod
    def Configure(self: Windows.Media.Devices.IDigitalWindowControl, digitalWindowMode: Windows.Media.Devices.DigitalWindowMode) -> Void: ...
    @winrt_mixinmethod
    def ConfigureWithBounds(self: Windows.Media.Devices.IDigitalWindowControl, digitalWindowMode: Windows.Media.Devices.DigitalWindowMode, digitalWindowBounds: Windows.Media.Devices.DigitalWindowBounds) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedCapabilities(self: Windows.Media.Devices.IDigitalWindowControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.DigitalWindowCapability]: ...
    @winrt_mixinmethod
    def GetCapabilityForSize(self: Windows.Media.Devices.IDigitalWindowControl, width: Int32, height: Int32) -> Windows.Media.Devices.DigitalWindowCapability: ...
    IsSupported = property(get_IsSupported, None)
    SupportedModes = property(get_SupportedModes, None)
    CurrentMode = property(get_CurrentMode, None)
    SupportedCapabilities = property(get_SupportedCapabilities, None)
DigitalWindowMode = Int32
DigitalWindowMode_Off: DigitalWindowMode = 0
DigitalWindowMode_On: DigitalWindowMode = 1
DigitalWindowMode_Auto: DigitalWindowMode = 2
class ExposureCompensationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ExposureCompensationControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IExposureCompensationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IExposureCompensationControl) -> Single: ...
    @winrt_mixinmethod
    def SetValueAsync(self: Windows.Media.Devices.IExposureCompensationControl, value: Single) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class ExposureControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ExposureControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IExposureControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Auto(self: Windows.Media.Devices.IExposureControl) -> Boolean: ...
    @winrt_mixinmethod
    def SetAutoAsync(self: Windows.Media.Devices.IExposureControl, value: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.IExposureControl) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.IExposureControl) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.IExposureControl) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IExposureControl) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SetValueAsync(self: Windows.Media.Devices.IExposureControl, shutterDuration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    Auto = property(get_Auto, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class ExposurePriorityVideoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ExposurePriorityVideoControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IExposurePriorityVideoControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Media.Devices.IExposurePriorityVideoControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: Windows.Media.Devices.IExposurePriorityVideoControl, value: Boolean) -> Void: ...
    Supported = property(get_Supported, None)
    Enabled = property(get_Enabled, put_Enabled)
class FlashControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.FlashControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerSupported(self: Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_RedEyeReductionSupported(self: Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: Windows.Media.Devices.IFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Auto(self: Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: Windows.Media.Devices.IFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RedEyeReduction(self: Windows.Media.Devices.IFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_RedEyeReduction(self: Windows.Media.Devices.IFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PowerPercent(self: Windows.Media.Devices.IFlashControl) -> Single: ...
    @winrt_mixinmethod
    def put_PowerPercent(self: Windows.Media.Devices.IFlashControl, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AssistantLightSupported(self: Windows.Media.Devices.IFlashControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_AssistantLightEnabled(self: Windows.Media.Devices.IFlashControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AssistantLightEnabled(self: Windows.Media.Devices.IFlashControl2, value: Boolean) -> Void: ...
    Supported = property(get_Supported, None)
    PowerSupported = property(get_PowerSupported, None)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    Enabled = property(get_Enabled, put_Enabled)
    Auto = property(get_Auto, put_Auto)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
    AssistantLightSupported = property(get_AssistantLightSupported, None)
    AssistantLightEnabled = property(get_AssistantLightEnabled, put_AssistantLightEnabled)
class FocusControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.FocusControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IFocusControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedPresets(self: Windows.Media.Devices.IFocusControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.FocusPreset]: ...
    @winrt_mixinmethod
    def get_Preset(self: Windows.Media.Devices.IFocusControl) -> Windows.Media.Devices.FocusPreset: ...
    @winrt_mixinmethod
    def SetPresetAsync(self: Windows.Media.Devices.IFocusControl, preset: Windows.Media.Devices.FocusPreset) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetPresetWithCompletionOptionAsync(self: Windows.Media.Devices.IFocusControl, preset: Windows.Media.Devices.FocusPreset, completeBeforeFocus: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IFocusControl) -> UInt32: ...
    @winrt_mixinmethod
    def SetValueAsync(self: Windows.Media.Devices.IFocusControl, focus: UInt32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FocusAsync(self: Windows.Media.Devices.IFocusControl) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_FocusChangedSupported(self: Windows.Media.Devices.IFocusControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_WaitForFocusSupported(self: Windows.Media.Devices.IFocusControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedFocusModes(self: Windows.Media.Devices.IFocusControl2) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.FocusMode]: ...
    @winrt_mixinmethod
    def get_SupportedFocusDistances(self: Windows.Media.Devices.IFocusControl2) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_mixinmethod
    def get_SupportedFocusRanges(self: Windows.Media.Devices.IFocusControl2) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AutoFocusRange]: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IFocusControl2) -> Windows.Media.Devices.FocusMode: ...
    @winrt_mixinmethod
    def get_FocusState(self: Windows.Media.Devices.IFocusControl2) -> Windows.Media.Devices.MediaCaptureFocusState: ...
    @winrt_mixinmethod
    def UnlockAsync(self: Windows.Media.Devices.IFocusControl2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def LockAsync(self: Windows.Media.Devices.IFocusControl2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Configure(self: Windows.Media.Devices.IFocusControl2, settings: Windows.Media.Devices.FocusSettings) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedPresets = property(get_SupportedPresets, None)
    Preset = property(get_Preset, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
    FocusChangedSupported = property(get_FocusChangedSupported, None)
    WaitForFocusSupported = property(get_WaitForFocusSupported, None)
    SupportedFocusModes = property(get_SupportedFocusModes, None)
    SupportedFocusDistances = property(get_SupportedFocusDistances, None)
    SupportedFocusRanges = property(get_SupportedFocusRanges, None)
    Mode = property(get_Mode, None)
    FocusState = property(get_FocusState, None)
FocusMode = Int32
FocusMode_Auto: FocusMode = 0
FocusMode_Single: FocusMode = 1
FocusMode_Continuous: FocusMode = 2
FocusMode_Manual: FocusMode = 3
FocusPreset = Int32
FocusPreset_Auto: FocusPreset = 0
FocusPreset_Manual: FocusPreset = 1
FocusPreset_AutoMacro: FocusPreset = 2
FocusPreset_AutoNormal: FocusPreset = 3
FocusPreset_AutoInfinity: FocusPreset = 4
FocusPreset_AutoHyperfocal: FocusPreset = 5
class FocusSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.FocusSettings'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Devices.FocusSettings: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IFocusSettings) -> Windows.Media.Devices.FocusMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Devices.IFocusSettings, value: Windows.Media.Devices.FocusMode) -> Void: ...
    @winrt_mixinmethod
    def get_AutoFocusRange(self: Windows.Media.Devices.IFocusSettings) -> Windows.Media.Devices.AutoFocusRange: ...
    @winrt_mixinmethod
    def put_AutoFocusRange(self: Windows.Media.Devices.IFocusSettings, value: Windows.Media.Devices.AutoFocusRange) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IFocusSettings) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Media.Devices.IFocusSettings, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_Distance(self: Windows.Media.Devices.IFocusSettings) -> Windows.Foundation.IReference[Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_mixinmethod
    def put_Distance(self: Windows.Media.Devices.IFocusSettings, value: Windows.Foundation.IReference[Windows.Media.Devices.ManualFocusDistance]) -> Void: ...
    @winrt_mixinmethod
    def get_WaitForFocus(self: Windows.Media.Devices.IFocusSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_WaitForFocus(self: Windows.Media.Devices.IFocusSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DisableDriverFallback(self: Windows.Media.Devices.IFocusSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisableDriverFallback(self: Windows.Media.Devices.IFocusSettings, value: Boolean) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    AutoFocusRange = property(get_AutoFocusRange, put_AutoFocusRange)
    Value = property(get_Value, put_Value)
    Distance = property(get_Distance, put_Distance)
    WaitForFocus = property(get_WaitForFocus, put_WaitForFocus)
    DisableDriverFallback = property(get_DisableDriverFallback, put_DisableDriverFallback)
class HdrVideoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.HdrVideoControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IHdrVideoControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.IHdrVideoControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.HdrVideoMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IHdrVideoControl) -> Windows.Media.Devices.HdrVideoMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Devices.IHdrVideoControl, value: Windows.Media.Devices.HdrVideoMode) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, put_Mode)
HdrVideoMode = Int32
HdrVideoMode_Off: HdrVideoMode = 0
HdrVideoMode_On: HdrVideoMode = 1
HdrVideoMode_Auto: HdrVideoMode = 2
class IAdvancedPhotoCaptureSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('08f3863a-0018-445b-93-d2-64-6d-1c-5e-d0-5c')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: Windows.Media.Devices.AdvancedPhotoMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class IAdvancedPhotoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c5b15486-9001-4682-93-09-68-ea-e0-08-0e-ec')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AdvancedPhotoMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_commethod(9)
    def Configure(self, settings: Windows.Media.Devices.AdvancedPhotoCaptureSettings) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, None)
class IAdvancedVideoCaptureDeviceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('de6ff4d3-2b96-4583-80-ab-b5-b0-1d-c6-a8-d7')
    @winrt_commethod(6)
    def SetDeviceProperty(self, propertyId: WinRT_String, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(7)
    def GetDeviceProperty(self, propertyId: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IAdvancedVideoCaptureDeviceController10(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c621b82d-d6f0-5c1b-a3-88-a6-e9-38-40-71-46')
    @winrt_commethod(6)
    def get_CameraOcclusionInfo(self) -> Windows.Media.Devices.CameraOcclusionInfo: ...
    CameraOcclusionInfo = property(get_CameraOcclusionInfo, None)
class IAdvancedVideoCaptureDeviceController11(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d5b65ae2-3772-580c-a6-30-e7-5d-e9-10-69-04')
    @winrt_commethod(6)
    def TryAcquireExclusiveControl(self, deviceId: WinRT_String, mode: Windows.Media.Capture.MediaCaptureDeviceExclusiveControlReleaseMode) -> Boolean: ...
class IAdvancedVideoCaptureDeviceController2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8bb94f8f-f11a-43db-b4-02-11-93-0b-80-ae-56')
    @winrt_commethod(6)
    def get_LowLagPhotoSequence(self) -> Windows.Media.Devices.LowLagPhotoSequenceControl: ...
    @winrt_commethod(7)
    def get_LowLagPhoto(self) -> Windows.Media.Devices.LowLagPhotoControl: ...
    @winrt_commethod(8)
    def get_SceneModeControl(self) -> Windows.Media.Devices.SceneModeControl: ...
    @winrt_commethod(9)
    def get_TorchControl(self) -> Windows.Media.Devices.TorchControl: ...
    @winrt_commethod(10)
    def get_FlashControl(self) -> Windows.Media.Devices.FlashControl: ...
    @winrt_commethod(11)
    def get_WhiteBalanceControl(self) -> Windows.Media.Devices.WhiteBalanceControl: ...
    @winrt_commethod(12)
    def get_ExposureControl(self) -> Windows.Media.Devices.ExposureControl: ...
    @winrt_commethod(13)
    def get_FocusControl(self) -> Windows.Media.Devices.FocusControl: ...
    @winrt_commethod(14)
    def get_ExposureCompensationControl(self) -> Windows.Media.Devices.ExposureCompensationControl: ...
    @winrt_commethod(15)
    def get_IsoSpeedControl(self) -> Windows.Media.Devices.IsoSpeedControl: ...
    @winrt_commethod(16)
    def get_RegionsOfInterestControl(self) -> Windows.Media.Devices.RegionsOfInterestControl: ...
    @winrt_commethod(17)
    def get_PrimaryUse(self) -> Windows.Media.Devices.CaptureUse: ...
    @winrt_commethod(18)
    def put_PrimaryUse(self, value: Windows.Media.Devices.CaptureUse) -> Void: ...
    LowLagPhotoSequence = property(get_LowLagPhotoSequence, None)
    LowLagPhoto = property(get_LowLagPhoto, None)
    SceneModeControl = property(get_SceneModeControl, None)
    TorchControl = property(get_TorchControl, None)
    FlashControl = property(get_FlashControl, None)
    WhiteBalanceControl = property(get_WhiteBalanceControl, None)
    ExposureControl = property(get_ExposureControl, None)
    FocusControl = property(get_FocusControl, None)
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    RegionsOfInterestControl = property(get_RegionsOfInterestControl, None)
    PrimaryUse = property(get_PrimaryUse, put_PrimaryUse)
class IAdvancedVideoCaptureDeviceController3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a98b8f34-ee0d-470c-b9-f0-42-29-c4-bb-d0-89')
    @winrt_commethod(6)
    def get_VariablePhotoSequenceController(self) -> Windows.Media.Devices.Core.VariablePhotoSequenceController: ...
    @winrt_commethod(7)
    def get_PhotoConfirmationControl(self) -> Windows.Media.Devices.PhotoConfirmationControl: ...
    @winrt_commethod(8)
    def get_ZoomControl(self) -> Windows.Media.Devices.ZoomControl: ...
    VariablePhotoSequenceController = property(get_VariablePhotoSequenceController, None)
    PhotoConfirmationControl = property(get_PhotoConfirmationControl, None)
    ZoomControl = property(get_ZoomControl, None)
class IAdvancedVideoCaptureDeviceController4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ea9fbfaf-d371-41c3-9a-17-82-4a-87-eb-df-d2')
    @winrt_commethod(6)
    def get_ExposurePriorityVideoControl(self) -> Windows.Media.Devices.ExposurePriorityVideoControl: ...
    @winrt_commethod(7)
    def get_DesiredOptimization(self) -> Windows.Media.Devices.MediaCaptureOptimization: ...
    @winrt_commethod(8)
    def put_DesiredOptimization(self, value: Windows.Media.Devices.MediaCaptureOptimization) -> Void: ...
    @winrt_commethod(9)
    def get_HdrVideoControl(self) -> Windows.Media.Devices.HdrVideoControl: ...
    @winrt_commethod(10)
    def get_OpticalImageStabilizationControl(self) -> Windows.Media.Devices.OpticalImageStabilizationControl: ...
    @winrt_commethod(11)
    def get_AdvancedPhotoControl(self) -> Windows.Media.Devices.AdvancedPhotoControl: ...
    ExposurePriorityVideoControl = property(get_ExposurePriorityVideoControl, None)
    DesiredOptimization = property(get_DesiredOptimization, put_DesiredOptimization)
    HdrVideoControl = property(get_HdrVideoControl, None)
    OpticalImageStabilizationControl = property(get_OpticalImageStabilizationControl, None)
    AdvancedPhotoControl = property(get_AdvancedPhotoControl, None)
class IAdvancedVideoCaptureDeviceController5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('33512b17-b9cb-4a23-b8-75-f9-ea-ab-53-54-92')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDevicePropertyById(self, propertyId: WinRT_String, maxPropertyValueSize: Windows.Foundation.IReference[UInt32]) -> Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_commethod(8)
    def SetDevicePropertyById(self, propertyId: WinRT_String, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    @winrt_commethod(9)
    def GetDevicePropertyByExtendedId(self, extendedPropertyId: c_char_p_no, maxPropertyValueSize: Windows.Foundation.IReference[UInt32]) -> Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_commethod(10)
    def SetDevicePropertyByExtendedId(self, extendedPropertyId: c_char_p_no, propertyValue: c_char_p_no) -> Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    Id = property(get_Id, None)
class IAdvancedVideoCaptureDeviceController6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b6563a53-68a1-44b7-9f-89-b5-fa-97-ac-0c-be')
    @winrt_commethod(6)
    def get_VideoTemporalDenoisingControl(self) -> Windows.Media.Devices.VideoTemporalDenoisingControl: ...
    VideoTemporalDenoisingControl = property(get_VideoTemporalDenoisingControl, None)
class IAdvancedVideoCaptureDeviceController7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8d2927f0-a054-50e7-b7-df-7c-04-23-4d-10-f0')
    @winrt_commethod(6)
    def get_InfraredTorchControl(self) -> Windows.Media.Devices.InfraredTorchControl: ...
    InfraredTorchControl = property(get_InfraredTorchControl, None)
class IAdvancedVideoCaptureDeviceController8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d843f010-e7fb-595b-9a-78-0e-54-c4-53-2b-43')
    @winrt_commethod(6)
    def get_PanelBasedOptimizationControl(self) -> Windows.Media.Devices.PanelBasedOptimizationControl: ...
    PanelBasedOptimizationControl = property(get_PanelBasedOptimizationControl, None)
class IAdvancedVideoCaptureDeviceController9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8bdca95d-0255-51bc-a1-0d-5a-16-9e-c1-62-5a')
    @winrt_commethod(6)
    def get_DigitalWindowControl(self) -> Windows.Media.Devices.DigitalWindowControl: ...
    DigitalWindowControl = property(get_DigitalWindowControl, None)
class IAudioDeviceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('edd4a388-79c7-4f7c-90-e8-ef-93-4b-21-58-0a')
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
class IAudioDeviceModule(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('86cfac36-47c1-4b33-98-52-87-73-ec-4b-e1-23')
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
    def SendCommandAsync(self, Command: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Media.Devices.ModuleCommandResult]: ...
    ClassId = property(get_ClassId, None)
    DisplayName = property(get_DisplayName, None)
    InstanceId = property(get_InstanceId, None)
    MajorVersion = property(get_MajorVersion, None)
    MinorVersion = property(get_MinorVersion, None)
class IAudioDeviceModuleNotificationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e3e3ccaf-224c-48be-95-6b-9a-13-13-4e-96-e8')
    @winrt_commethod(6)
    def get_Module(self) -> Windows.Media.Devices.AudioDeviceModule: ...
    @winrt_commethod(7)
    def get_NotificationData(self) -> Windows.Storage.Streams.IBuffer: ...
    Module = property(get_Module, None)
    NotificationData = property(get_NotificationData, None)
class IAudioDeviceModulesManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6aa40c4d-960a-4d1c-b3-18-00-22-60-45-47-ed')
    @winrt_commethod(6)
    def add_ModuleNotificationReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Devices.AudioDeviceModulesManager, Windows.Media.Devices.AudioDeviceModuleNotificationEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ModuleNotificationReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def FindAllById(self, moduleId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AudioDeviceModule]: ...
    @winrt_commethod(9)
    def FindAll(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AudioDeviceModule]: ...
class IAudioDeviceModulesManagerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8db03670-e64d-4773-96-c0-bc-7e-bf-0e-06-3f')
    @winrt_commethod(6)
    def Create(self, deviceId: WinRT_String) -> Windows.Media.Devices.AudioDeviceModulesManager: ...
class ICameraOcclusionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('af6c4ad0-a84d-5db6-be-58-a5-da-21-cf-e0-11')
    @winrt_commethod(6)
    def GetState(self) -> Windows.Media.Devices.CameraOcclusionState: ...
    @winrt_commethod(7)
    def IsOcclusionKindSupported(self, occlusionKind: Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    @winrt_commethod(8)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Devices.CameraOcclusionInfo, Windows.Media.Devices.CameraOcclusionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICameraOcclusionState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('430adeb8-6842-5e55-9b-de-04-b4-ef-3a-8a-57')
    @winrt_commethod(6)
    def get_IsOccluded(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsOcclusionKind(self, occlusionKind: Windows.Media.Devices.CameraOcclusionKind) -> Boolean: ...
    IsOccluded = property(get_IsOccluded, None)
class ICameraOcclusionStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8512d848-c0de-57ca-a1-ca-fb-2c-3d-23-df-55')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Media.Devices.CameraOcclusionState: ...
    State = property(get_State, None)
class IDefaultAudioDeviceChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('110f882f-1c05-4657-a1-8e-47-c9-b6-9f-07-ab')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Role(self) -> Windows.Media.Devices.AudioDeviceRole: ...
    Id = property(get_Id, None)
    Role = property(get_Role, None)
class IDigitalWindowBounds(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dd4f21dd-d173-5c6b-8c-25-bd-d2-6d-51-22-b1')
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
    NormalizedOriginTop = property(get_NormalizedOriginTop, put_NormalizedOriginTop)
    NormalizedOriginLeft = property(get_NormalizedOriginLeft, put_NormalizedOriginLeft)
    Scale = property(get_Scale, put_Scale)
class IDigitalWindowCapability(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d78bad2c-f721-5244-a1-96-b5-6c-cb-ec-60-6c')
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
    def get_NormalizedFieldOfViewLimit(self) -> Windows.Foundation.Rect: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    MinScaleValue = property(get_MinScaleValue, None)
    MaxScaleValue = property(get_MaxScaleValue, None)
    MinScaleValueWithoutUpsampling = property(get_MinScaleValueWithoutUpsampling, None)
    NormalizedFieldOfViewLimit = property(get_NormalizedFieldOfViewLimit, None)
class IDigitalWindowControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('23b69eff-65d2-53ea-87-80-de-58-2b-48-b5-44')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> POINTER(Windows.Media.Devices.DigitalWindowMode): ...
    @winrt_commethod(8)
    def get_CurrentMode(self) -> Windows.Media.Devices.DigitalWindowMode: ...
    @winrt_commethod(9)
    def GetBounds(self) -> Windows.Media.Devices.DigitalWindowBounds: ...
    @winrt_commethod(10)
    def Configure(self, digitalWindowMode: Windows.Media.Devices.DigitalWindowMode) -> Void: ...
    @winrt_commethod(11)
    def ConfigureWithBounds(self, digitalWindowMode: Windows.Media.Devices.DigitalWindowMode, digitalWindowBounds: Windows.Media.Devices.DigitalWindowBounds) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedCapabilities(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.DigitalWindowCapability]: ...
    @winrt_commethod(13)
    def GetCapabilityForSize(self, width: Int32, height: Int32) -> Windows.Media.Devices.DigitalWindowCapability: ...
    IsSupported = property(get_IsSupported, None)
    SupportedModes = property(get_SupportedModes, None)
    CurrentMode = property(get_CurrentMode, None)
    SupportedCapabilities = property(get_SupportedCapabilities, None)
class IExposureCompensationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('81c8e834-dcec-4011-a6-10-1f-38-47-e6-4a-ca')
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
    def SetValueAsync(self, value: Single) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class IExposureControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('09e8cbe2-ad96-4f28-a0-e0-96-ed-7e-1b-5f-d2')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(8)
    def SetAutoAsync(self, value: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_Min(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Max(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def get_Step(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def get_Value(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def SetValueAsync(self, shutterDuration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    Auto = property(get_Auto, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class IExposurePriorityVideoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2cb240a3-5168-4271-9e-a5-47-62-1a-98-a3-52')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Enabled(self, value: Boolean) -> Void: ...
    Supported = property(get_Supported, None)
    Enabled = property(get_Enabled, put_Enabled)
class IFlashControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('def41dbe-7d68-45e3-8c-0f-be-7b-b3-28-37-d0')
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
    Supported = property(get_Supported, None)
    PowerSupported = property(get_PowerSupported, None)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    Enabled = property(get_Enabled, put_Enabled)
    Auto = property(get_Auto, put_Auto)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
class IFlashControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7d29cc9e-75e1-4af7-bd-7d-4e-38-e1-c0-6c-d6')
    @winrt_commethod(6)
    def get_AssistantLightSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AssistantLightEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AssistantLightEnabled(self, value: Boolean) -> Void: ...
    AssistantLightSupported = property(get_AssistantLightSupported, None)
    AssistantLightEnabled = property(get_AssistantLightEnabled, put_AssistantLightEnabled)
class IFocusControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c0d889f6-5228-4453-b1-53-85-60-65-92-b2-38')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedPresets(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.FocusPreset]: ...
    @winrt_commethod(8)
    def get_Preset(self) -> Windows.Media.Devices.FocusPreset: ...
    @winrt_commethod(9)
    def SetPresetAsync(self, preset: Windows.Media.Devices.FocusPreset) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def SetPresetWithCompletionOptionAsync(self, preset: Windows.Media.Devices.FocusPreset, completeBeforeFocus: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_Step(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(15)
    def SetValueAsync(self, focus: UInt32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def FocusAsync(self) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    SupportedPresets = property(get_SupportedPresets, None)
    Preset = property(get_Preset, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class IFocusControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3f7cff48-c534-4e9e-94-c3-52-ef-2a-fd-5d-07')
    @winrt_commethod(6)
    def get_FocusChangedSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_WaitForFocusSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SupportedFocusModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.FocusMode]: ...
    @winrt_commethod(9)
    def get_SupportedFocusDistances(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_commethod(10)
    def get_SupportedFocusRanges(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.AutoFocusRange]: ...
    @winrt_commethod(11)
    def get_Mode(self) -> Windows.Media.Devices.FocusMode: ...
    @winrt_commethod(12)
    def get_FocusState(self) -> Windows.Media.Devices.MediaCaptureFocusState: ...
    @winrt_commethod(13)
    def UnlockAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def LockAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def Configure(self, settings: Windows.Media.Devices.FocusSettings) -> Void: ...
    FocusChangedSupported = property(get_FocusChangedSupported, None)
    WaitForFocusSupported = property(get_WaitForFocusSupported, None)
    SupportedFocusModes = property(get_SupportedFocusModes, None)
    SupportedFocusDistances = property(get_SupportedFocusDistances, None)
    SupportedFocusRanges = property(get_SupportedFocusRanges, None)
    Mode = property(get_Mode, None)
    FocusState = property(get_FocusState, None)
class IFocusSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('79958f6b-3263-4275-85-d6-ae-ae-89-1c-96-ee')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.Media.Devices.FocusMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: Windows.Media.Devices.FocusMode) -> Void: ...
    @winrt_commethod(8)
    def get_AutoFocusRange(self) -> Windows.Media.Devices.AutoFocusRange: ...
    @winrt_commethod(9)
    def put_AutoFocusRange(self, value: Windows.Media.Devices.AutoFocusRange) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(11)
    def put_Value(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(12)
    def get_Distance(self) -> Windows.Foundation.IReference[Windows.Media.Devices.ManualFocusDistance]: ...
    @winrt_commethod(13)
    def put_Distance(self, value: Windows.Foundation.IReference[Windows.Media.Devices.ManualFocusDistance]) -> Void: ...
    @winrt_commethod(14)
    def get_WaitForFocus(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_WaitForFocus(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_DisableDriverFallback(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_DisableDriverFallback(self, value: Boolean) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    AutoFocusRange = property(get_AutoFocusRange, put_AutoFocusRange)
    Value = property(get_Value, put_Value)
    Distance = property(get_Distance, put_Distance)
    WaitForFocus = property(get_WaitForFocus, put_WaitForFocus)
    DisableDriverFallback = property(get_DisableDriverFallback, put_DisableDriverFallback)
class IHdrVideoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('55d8e2d0-30c0-43bf-9b-9a-97-99-d7-0c-ed-94')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.HdrVideoMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> Windows.Media.Devices.HdrVideoMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: Windows.Media.Devices.HdrVideoMode) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, put_Mode)
class IInfraredTorchControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1cba2c83-6cb6-5a04-a6-fc-3b-e7-b3-3f-f0-56')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.InfraredTorchMode]: ...
    @winrt_commethod(8)
    def get_CurrentMode(self) -> Windows.Media.Devices.InfraredTorchMode: ...
    @winrt_commethod(9)
    def put_CurrentMode(self, value: Windows.Media.Devices.InfraredTorchMode) -> Void: ...
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
    IsSupported = property(get_IsSupported, None)
    SupportedModes = property(get_SupportedModes, None)
    CurrentMode = property(get_CurrentMode, put_CurrentMode)
    MinPower = property(get_MinPower, None)
    MaxPower = property(get_MaxPower, None)
    PowerStep = property(get_PowerStep, None)
    Power = property(get_Power, put_Power)
class IIsoSpeedControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('27b6c322-25ad-4f1b-aa-ab-52-4a-b3-76-ca-33')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedPresets(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.IsoSpeedPreset]: ...
    @winrt_commethod(8)
    def get_Preset(self) -> Windows.Media.Devices.IsoSpeedPreset: ...
    @winrt_commethod(9)
    def SetPresetAsync(self, preset: Windows.Media.Devices.IsoSpeedPreset) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    SupportedPresets = property(get_SupportedPresets, None)
    Preset = property(get_Preset, None)
class IIsoSpeedControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6f1578f2-6d77-4f8a-8c-2f-61-30-b6-39-50-53')
    @winrt_commethod(6)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Step(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(10)
    def SetValueAsync(self, isoSpeed: UInt32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(12)
    def SetAutoAsync(self) -> Windows.Foundation.IAsyncAction: ...
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
    Auto = property(get_Auto, None)
class ILowLagPhotoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6d5c4dd0-fadf-415d-ae-e6-3b-aa-52-93-00-c9')
    @winrt_commethod(6)
    def GetHighestConcurrentFrameRate(self, captureProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(7)
    def GetCurrentFrameRate(self) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(8)
    def get_ThumbnailEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_ThumbnailEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ThumbnailFormat(self) -> Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_commethod(11)
    def put_ThumbnailFormat(self, value: Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_commethod(12)
    def get_DesiredThumbnailSize(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_DesiredThumbnailSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_HardwareAcceleratedThumbnailSupported(self) -> UInt32: ...
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
class ILowLagPhotoSequenceControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3dcf909d-6d16-409c-ba-fe-b9-a5-94-c6-fd-e6')
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
    def GetHighestConcurrentFrameRate(self, captureProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(14)
    def GetCurrentFrameRate(self) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(15)
    def get_ThumbnailEnabled(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_ThumbnailEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_ThumbnailFormat(self) -> Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_commethod(18)
    def put_ThumbnailFormat(self, value: Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_commethod(19)
    def get_DesiredThumbnailSize(self) -> UInt32: ...
    @winrt_commethod(20)
    def put_DesiredThumbnailSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(21)
    def get_HardwareAcceleratedThumbnailSupported(self) -> UInt32: ...
    Supported = property(get_Supported, None)
    MaxPastPhotos = property(get_MaxPastPhotos, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PastPhotoLimit = property(get_PastPhotoLimit, put_PastPhotoLimit)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
class IMediaDeviceControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('efa8dfa9-6f75-4863-ba-0b-58-3f-30-36-b4-de')
    @winrt_commethod(6)
    def get_Capabilities(self) -> Windows.Media.Devices.MediaDeviceControlCapabilities: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('23005816-eb85-43e2-b9-2b-82-40-d5-ee-70-ec')
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
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Default = property(get_Default, None)
    AutoModeSupported = property(get_AutoModeSupported, None)
class IMediaDeviceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f6f8f5ce-209a-48fb-86-fc-d4-45-78-f3-17-e6')
    @winrt_commethod(6)
    def GetAvailableMediaStreamProperties(self, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Foundation.Collections.IVectorView[Windows.Media.MediaProperties.IMediaEncodingProperties]: ...
    @winrt_commethod(7)
    def GetMediaStreamProperties(self, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Media.MediaProperties.IMediaEncodingProperties: ...
    @winrt_commethod(8)
    def SetMediaStreamPropertiesAsync(self, mediaStreamType: Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Foundation.IAsyncAction: ...
class IMediaDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('aa2d9a40-909f-4bba-bf-8b-0c-0d-29-6f-14-f0')
    @winrt_commethod(6)
    def GetAudioCaptureSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetAudioRenderSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetVideoCaptureSelector(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDefaultAudioCaptureId(self, role: Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDefaultAudioRenderId(self, role: Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_commethod(11)
    def add_DefaultAudioCaptureDeviceChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Media.Devices.DefaultAudioCaptureDeviceChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_DefaultAudioCaptureDeviceChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_DefaultAudioRenderDeviceChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Media.Devices.DefaultAudioRenderDeviceChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_DefaultAudioRenderDeviceChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IModuleCommandResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('520d1eb4-1374-4c7d-b1-e4-39-dc-df-3e-ae-4e')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.Devices.SendCommandStatus: ...
    @winrt_commethod(7)
    def get_Result(self) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Result = property(get_Result, None)
class IOpticalImageStabilizationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bfad9c1d-00bc-423b-8e-b2-a0-17-8c-a9-42-47')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.OpticalImageStabilizationMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> Windows.Media.Devices.OpticalImageStabilizationMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: Windows.Media.Devices.OpticalImageStabilizationMode) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, put_Mode)
class IPanelBasedOptimizationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('33323223-6247-5419-a5-a4-3d-80-86-45-d9-17')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Panel(self) -> Windows.Devices.Enumeration.Panel: ...
    @winrt_commethod(8)
    def put_Panel(self, value: Windows.Devices.Enumeration.Panel) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    Panel = property(get_Panel, put_Panel)
class IPhotoConfirmationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c8f3f363-ff5e-4582-a9-a8-05-50-f8-5a-4a-76')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_PixelFormat(self) -> Windows.Media.MediaProperties.MediaPixelFormat: ...
    @winrt_commethod(10)
    def put_PixelFormat(self, format: Windows.Media.MediaProperties.MediaPixelFormat) -> Void: ...
    Supported = property(get_Supported, None)
    Enabled = property(get_Enabled, put_Enabled)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
class IRegionOfInterest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e5ecc834-ce66-4e05-a7-8f-cf-39-1a-5e-c2-d1')
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
    def get_Bounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(13)
    def put_Bounds(self, value: Windows.Foundation.Rect) -> Void: ...
    AutoFocusEnabled = property(get_AutoFocusEnabled, put_AutoFocusEnabled)
    AutoWhiteBalanceEnabled = property(get_AutoWhiteBalanceEnabled, put_AutoWhiteBalanceEnabled)
    AutoExposureEnabled = property(get_AutoExposureEnabled, put_AutoExposureEnabled)
    Bounds = property(get_Bounds, put_Bounds)
class IRegionOfInterest2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('19fe2a91-73aa-4d51-8a-9d-56-cc-f7-db-7f-54')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.Media.Devices.RegionOfInterestType: ...
    @winrt_commethod(7)
    def put_Type(self, value: Windows.Media.Devices.RegionOfInterestType) -> Void: ...
    @winrt_commethod(8)
    def get_BoundsNormalized(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_BoundsNormalized(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_Weight(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_Weight(self, value: UInt32) -> Void: ...
    Type = property(get_Type, put_Type)
    BoundsNormalized = property(get_BoundsNormalized, put_BoundsNormalized)
    Weight = property(get_Weight, put_Weight)
class IRegionsOfInterestControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c323f527-ab0b-4558-8b-5b-df-56-93-db-03-78')
    @winrt_commethod(6)
    def get_MaxRegions(self) -> UInt32: ...
    @winrt_commethod(7)
    def SetRegionsAsync(self, regions: Windows.Foundation.Collections.IIterable[Windows.Media.Devices.RegionOfInterest]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SetRegionsWithLockAsync(self, regions: Windows.Foundation.Collections.IIterable[Windows.Media.Devices.RegionOfInterest], lockValues: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ClearRegionsAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def get_AutoFocusSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_AutoWhiteBalanceSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_AutoExposureSupported(self) -> Boolean: ...
    MaxRegions = property(get_MaxRegions, None)
    AutoFocusSupported = property(get_AutoFocusSupported, None)
    AutoWhiteBalanceSupported = property(get_AutoWhiteBalanceSupported, None)
    AutoExposureSupported = property(get_AutoExposureSupported, None)
class ISceneModeControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d48e5af7-8d59-4854-8c-62-12-c7-0b-a8-9b-7c')
    @winrt_commethod(6)
    def get_SupportedModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Media.Devices.CaptureSceneMode: ...
    @winrt_commethod(8)
    def SetValueAsync(self, sceneMode: Windows.Media.Devices.CaptureSceneMode) -> Windows.Foundation.IAsyncAction: ...
    SupportedModes = property(get_SupportedModes, None)
    Value = property(get_Value, None)
class ITorchControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a6053665-8250-416c-91-9a-72-42-96-af-a3-06')
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
    Supported = property(get_Supported, None)
    PowerSupported = property(get_PowerSupported, None)
    Enabled = property(get_Enabled, put_Enabled)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
class IVideoDeviceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('99555575-2e2e-40b8-b6-c7-f8-2d-10-01-32-10')
    @winrt_commethod(6)
    def get_Brightness(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(7)
    def get_Contrast(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(8)
    def get_Hue(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(9)
    def get_WhiteBalance(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(10)
    def get_BacklightCompensation(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(11)
    def get_Pan(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(12)
    def get_Tilt(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(13)
    def get_Zoom(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(14)
    def get_Roll(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(15)
    def get_Exposure(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(16)
    def get_Focus(self) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_commethod(17)
    def TrySetPowerlineFrequency(self, value: Windows.Media.Capture.PowerlineFrequency) -> Boolean: ...
    @winrt_commethod(18)
    def TryGetPowerlineFrequency(self, value: POINTER(Windows.Media.Capture.PowerlineFrequency)) -> Boolean: ...
    Brightness = property(get_Brightness, None)
    Contrast = property(get_Contrast, None)
    Hue = property(get_Hue, None)
    WhiteBalance = property(get_WhiteBalance, None)
    BacklightCompensation = property(get_BacklightCompensation, None)
    Pan = property(get_Pan, None)
    Tilt = property(get_Tilt, None)
    Zoom = property(get_Zoom, None)
    Roll = property(get_Roll, None)
    Exposure = property(get_Exposure, None)
    Focus = property(get_Focus, None)
class IVideoDeviceControllerGetDevicePropertyResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c5d88395-6ed5-4790-8b-5d-0e-f1-39-35-d0-f8')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IVideoTemporalDenoisingControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7ab34735-3e2a-4a32-ba-ff-43-58-c4-fb-dd-57')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.VideoTemporalDenoisingMode]: ...
    @winrt_commethod(8)
    def get_Mode(self) -> Windows.Media.Devices.VideoTemporalDenoisingMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: Windows.Media.Devices.VideoTemporalDenoisingMode) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, put_Mode)
class IWhiteBalanceControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('781f047e-7162-49c8-a8-f9-94-81-c5-65-36-3e')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Preset(self) -> Windows.Media.Devices.ColorTemperaturePreset: ...
    @winrt_commethod(8)
    def SetPresetAsync(self, preset: Windows.Media.Devices.ColorTemperaturePreset) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Step(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(13)
    def SetValueAsync(self, temperature: UInt32) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    Preset = property(get_Preset, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class IZoomControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3a1e0b12-32da-4c17-bf-d7-8d-0c-73-c8-f5-a5')
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
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, put_Value)
class IZoomControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('69843db0-2e99-4641-85-29-18-4f-31-9d-16-71')
    @winrt_commethod(6)
    def get_SupportedModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.ZoomTransitionMode]: ...
    @winrt_commethod(7)
    def get_Mode(self) -> Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_commethod(8)
    def Configure(self, settings: Windows.Media.Devices.ZoomSettings) -> Void: ...
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, None)
class IZoomSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6ad66b24-14b4-4bfd-b1-8f-88-fe-24-46-3b-52')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: Windows.Media.Devices.ZoomTransitionMode) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Single: ...
    @winrt_commethod(9)
    def put_Value(self, value: Single) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Value = property(get_Value, put_Value)
class InfraredTorchControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.InfraredTorchControl'
    @winrt_mixinmethod
    def get_IsSupported(self: Windows.Media.Devices.IInfraredTorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.IInfraredTorchControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.InfraredTorchMode]: ...
    @winrt_mixinmethod
    def get_CurrentMode(self: Windows.Media.Devices.IInfraredTorchControl) -> Windows.Media.Devices.InfraredTorchMode: ...
    @winrt_mixinmethod
    def put_CurrentMode(self: Windows.Media.Devices.IInfraredTorchControl, value: Windows.Media.Devices.InfraredTorchMode) -> Void: ...
    @winrt_mixinmethod
    def get_MinPower(self: Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxPower(self: Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def get_PowerStep(self: Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def get_Power(self: Windows.Media.Devices.IInfraredTorchControl) -> Int32: ...
    @winrt_mixinmethod
    def put_Power(self: Windows.Media.Devices.IInfraredTorchControl, value: Int32) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    SupportedModes = property(get_SupportedModes, None)
    CurrentMode = property(get_CurrentMode, put_CurrentMode)
    MinPower = property(get_MinPower, None)
    MaxPower = property(get_MaxPower, None)
    PowerStep = property(get_PowerStep, None)
    Power = property(get_Power, put_Power)
InfraredTorchMode = Int32
InfraredTorchMode_Off: InfraredTorchMode = 0
InfraredTorchMode_On: InfraredTorchMode = 1
InfraredTorchMode_AlternatingFrameIllumination: InfraredTorchMode = 2
class IsoSpeedControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.IsoSpeedControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IIsoSpeedControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedPresets(self: Windows.Media.Devices.IIsoSpeedControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.IsoSpeedPreset]: ...
    @winrt_mixinmethod
    def get_Preset(self: Windows.Media.Devices.IIsoSpeedControl) -> Windows.Media.Devices.IsoSpeedPreset: ...
    @winrt_mixinmethod
    def SetPresetAsync(self: Windows.Media.Devices.IIsoSpeedControl, preset: Windows.Media.Devices.IsoSpeedPreset) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IIsoSpeedControl2) -> UInt32: ...
    @winrt_mixinmethod
    def SetValueAsync(self: Windows.Media.Devices.IIsoSpeedControl2, isoSpeed: UInt32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Auto(self: Windows.Media.Devices.IIsoSpeedControl2) -> Boolean: ...
    @winrt_mixinmethod
    def SetAutoAsync(self: Windows.Media.Devices.IIsoSpeedControl2) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    SupportedPresets = property(get_SupportedPresets, None)
    Preset = property(get_Preset, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
    Auto = property(get_Auto, None)
IsoSpeedPreset = Int32
IsoSpeedPreset_Auto: IsoSpeedPreset = 0
IsoSpeedPreset_Iso50: IsoSpeedPreset = 1
IsoSpeedPreset_Iso80: IsoSpeedPreset = 2
IsoSpeedPreset_Iso100: IsoSpeedPreset = 3
IsoSpeedPreset_Iso200: IsoSpeedPreset = 4
IsoSpeedPreset_Iso400: IsoSpeedPreset = 5
IsoSpeedPreset_Iso800: IsoSpeedPreset = 6
IsoSpeedPreset_Iso1600: IsoSpeedPreset = 7
IsoSpeedPreset_Iso3200: IsoSpeedPreset = 8
IsoSpeedPreset_Iso6400: IsoSpeedPreset = 9
IsoSpeedPreset_Iso12800: IsoSpeedPreset = 10
IsoSpeedPreset_Iso25600: IsoSpeedPreset = 11
class LowLagPhotoControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.LowLagPhotoControl'
    @winrt_mixinmethod
    def GetHighestConcurrentFrameRate(self: Windows.Media.Devices.ILowLagPhotoControl, captureProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def GetCurrentFrameRate(self: Windows.Media.Devices.ILowLagPhotoControl) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_ThumbnailEnabled(self: Windows.Media.Devices.ILowLagPhotoControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_ThumbnailEnabled(self: Windows.Media.Devices.ILowLagPhotoControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ThumbnailFormat(self: Windows.Media.Devices.ILowLagPhotoControl) -> Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_mixinmethod
    def put_ThumbnailFormat(self: Windows.Media.Devices.ILowLagPhotoControl, value: Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredThumbnailSize(self: Windows.Media.Devices.ILowLagPhotoControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_DesiredThumbnailSize(self: Windows.Media.Devices.ILowLagPhotoControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HardwareAcceleratedThumbnailSupported(self: Windows.Media.Devices.ILowLagPhotoControl) -> UInt32: ...
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
class LowLagPhotoSequenceControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.LowLagPhotoSequenceControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPastPhotos(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxPhotosPerSecond(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Single: ...
    @winrt_mixinmethod
    def get_PastPhotoLimit(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_PastPhotoLimit(self: Windows.Media.Devices.ILowLagPhotoSequenceControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PhotosPerSecondLimit(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Single: ...
    @winrt_mixinmethod
    def put_PhotosPerSecondLimit(self: Windows.Media.Devices.ILowLagPhotoSequenceControl, value: Single) -> Void: ...
    @winrt_mixinmethod
    def GetHighestConcurrentFrameRate(self: Windows.Media.Devices.ILowLagPhotoSequenceControl, captureProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def GetCurrentFrameRate(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_ThumbnailEnabled(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_ThumbnailEnabled(self: Windows.Media.Devices.ILowLagPhotoSequenceControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ThumbnailFormat(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> Windows.Media.MediaProperties.MediaThumbnailFormat: ...
    @winrt_mixinmethod
    def put_ThumbnailFormat(self: Windows.Media.Devices.ILowLagPhotoSequenceControl, value: Windows.Media.MediaProperties.MediaThumbnailFormat) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredThumbnailSize(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_DesiredThumbnailSize(self: Windows.Media.Devices.ILowLagPhotoSequenceControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HardwareAcceleratedThumbnailSupported(self: Windows.Media.Devices.ILowLagPhotoSequenceControl) -> UInt32: ...
    Supported = property(get_Supported, None)
    MaxPastPhotos = property(get_MaxPastPhotos, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PastPhotoLimit = property(get_PastPhotoLimit, put_PastPhotoLimit)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    ThumbnailEnabled = property(get_ThumbnailEnabled, put_ThumbnailEnabled)
    ThumbnailFormat = property(get_ThumbnailFormat, put_ThumbnailFormat)
    DesiredThumbnailSize = property(get_DesiredThumbnailSize, put_DesiredThumbnailSize)
    HardwareAcceleratedThumbnailSupported = property(get_HardwareAcceleratedThumbnailSupported, None)
ManualFocusDistance = Int32
ManualFocusDistance_Infinity: ManualFocusDistance = 0
ManualFocusDistance_Hyperfocal: ManualFocusDistance = 1
ManualFocusDistance_Nearest: ManualFocusDistance = 2
MediaCaptureFocusState = Int32
MediaCaptureFocusState_Uninitialized: MediaCaptureFocusState = 0
MediaCaptureFocusState_Lost: MediaCaptureFocusState = 1
MediaCaptureFocusState_Searching: MediaCaptureFocusState = 2
MediaCaptureFocusState_Focused: MediaCaptureFocusState = 3
MediaCaptureFocusState_Failed: MediaCaptureFocusState = 4
MediaCaptureOptimization = Int32
MediaCaptureOptimization_Default: MediaCaptureOptimization = 0
MediaCaptureOptimization_Quality: MediaCaptureOptimization = 1
MediaCaptureOptimization_Latency: MediaCaptureOptimization = 2
MediaCaptureOptimization_Power: MediaCaptureOptimization = 3
MediaCaptureOptimization_LatencyThenQuality: MediaCaptureOptimization = 4
MediaCaptureOptimization_LatencyThenPower: MediaCaptureOptimization = 5
MediaCaptureOptimization_PowerAndQuality: MediaCaptureOptimization = 6
MediaCapturePauseBehavior = Int32
MediaCapturePauseBehavior_RetainHardwareResources: MediaCapturePauseBehavior = 0
MediaCapturePauseBehavior_ReleaseHardwareResources: MediaCapturePauseBehavior = 1
class MediaDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.MediaDevice'
    @winrt_classmethod
    def GetAudioCaptureSelector(cls: Windows.Media.Devices.IMediaDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetAudioRenderSelector(cls: Windows.Media.Devices.IMediaDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetVideoCaptureSelector(cls: Windows.Media.Devices.IMediaDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAudioCaptureId(cls: Windows.Media.Devices.IMediaDeviceStatics, role: Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAudioRenderId(cls: Windows.Media.Devices.IMediaDeviceStatics, role: Windows.Media.Devices.AudioDeviceRole) -> WinRT_String: ...
    @winrt_classmethod
    def add_DefaultAudioCaptureDeviceChanged(cls: Windows.Media.Devices.IMediaDeviceStatics, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Media.Devices.DefaultAudioCaptureDeviceChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DefaultAudioCaptureDeviceChanged(cls: Windows.Media.Devices.IMediaDeviceStatics, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_DefaultAudioRenderDeviceChanged(cls: Windows.Media.Devices.IMediaDeviceStatics, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Media.Devices.DefaultAudioRenderDeviceChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DefaultAudioRenderDeviceChanged(cls: Windows.Media.Devices.IMediaDeviceStatics, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class MediaDeviceControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.MediaDeviceControl'
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Media.Devices.IMediaDeviceControl) -> Windows.Media.Devices.MediaDeviceControlCapabilities: ...
    @winrt_mixinmethod
    def TryGetValue(self: Windows.Media.Devices.IMediaDeviceControl, value: POINTER(Double)) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Media.Devices.IMediaDeviceControl, value: Double) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetAuto(self: Windows.Media.Devices.IMediaDeviceControl, value: POINTER(Boolean)) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetAuto(self: Windows.Media.Devices.IMediaDeviceControl, value: Boolean) -> Boolean: ...
    Capabilities = property(get_Capabilities, None)
class MediaDeviceControlCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.MediaDeviceControlCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_Default(self: Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Double: ...
    @winrt_mixinmethod
    def get_AutoModeSupported(self: Windows.Media.Devices.IMediaDeviceControlCapabilities) -> Boolean: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Default = property(get_Default, None)
    AutoModeSupported = property(get_AutoModeSupported, None)
class ModuleCommandResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ModuleCommandResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.Devices.IModuleCommandResult) -> Windows.Media.Devices.SendCommandStatus: ...
    @winrt_mixinmethod
    def get_Result(self: Windows.Media.Devices.IModuleCommandResult) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Result = property(get_Result, None)
class OpticalImageStabilizationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.OpticalImageStabilizationControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IOpticalImageStabilizationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.IOpticalImageStabilizationControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.OpticalImageStabilizationMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IOpticalImageStabilizationControl) -> Windows.Media.Devices.OpticalImageStabilizationMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Devices.IOpticalImageStabilizationControl, value: Windows.Media.Devices.OpticalImageStabilizationMode) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, put_Mode)
OpticalImageStabilizationMode = Int32
OpticalImageStabilizationMode_Off: OpticalImageStabilizationMode = 0
OpticalImageStabilizationMode_On: OpticalImageStabilizationMode = 1
OpticalImageStabilizationMode_Auto: OpticalImageStabilizationMode = 2
class PanelBasedOptimizationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.PanelBasedOptimizationControl'
    @winrt_mixinmethod
    def get_IsSupported(self: Windows.Media.Devices.IPanelBasedOptimizationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Panel(self: Windows.Media.Devices.IPanelBasedOptimizationControl) -> Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def put_Panel(self: Windows.Media.Devices.IPanelBasedOptimizationControl, value: Windows.Devices.Enumeration.Panel) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    Panel = property(get_Panel, put_Panel)
class PhotoConfirmationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.PhotoConfirmationControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IPhotoConfirmationControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Media.Devices.IPhotoConfirmationControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: Windows.Media.Devices.IPhotoConfirmationControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: Windows.Media.Devices.IPhotoConfirmationControl) -> Windows.Media.MediaProperties.MediaPixelFormat: ...
    @winrt_mixinmethod
    def put_PixelFormat(self: Windows.Media.Devices.IPhotoConfirmationControl, format: Windows.Media.MediaProperties.MediaPixelFormat) -> Void: ...
    Supported = property(get_Supported, None)
    Enabled = property(get_Enabled, put_Enabled)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
class RegionOfInterest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.RegionOfInterest'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Devices.RegionOfInterest: ...
    @winrt_mixinmethod
    def get_AutoFocusEnabled(self: Windows.Media.Devices.IRegionOfInterest) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoFocusEnabled(self: Windows.Media.Devices.IRegionOfInterest, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutoWhiteBalanceEnabled(self: Windows.Media.Devices.IRegionOfInterest) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoWhiteBalanceEnabled(self: Windows.Media.Devices.IRegionOfInterest, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutoExposureEnabled(self: Windows.Media.Devices.IRegionOfInterest) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoExposureEnabled(self: Windows.Media.Devices.IRegionOfInterest, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: Windows.Media.Devices.IRegionOfInterest) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_Bounds(self: Windows.Media.Devices.IRegionOfInterest, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Devices.IRegionOfInterest2) -> Windows.Media.Devices.RegionOfInterestType: ...
    @winrt_mixinmethod
    def put_Type(self: Windows.Media.Devices.IRegionOfInterest2, value: Windows.Media.Devices.RegionOfInterestType) -> Void: ...
    @winrt_mixinmethod
    def get_BoundsNormalized(self: Windows.Media.Devices.IRegionOfInterest2) -> Boolean: ...
    @winrt_mixinmethod
    def put_BoundsNormalized(self: Windows.Media.Devices.IRegionOfInterest2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Weight(self: Windows.Media.Devices.IRegionOfInterest2) -> UInt32: ...
    @winrt_mixinmethod
    def put_Weight(self: Windows.Media.Devices.IRegionOfInterest2, value: UInt32) -> Void: ...
    AutoFocusEnabled = property(get_AutoFocusEnabled, put_AutoFocusEnabled)
    AutoWhiteBalanceEnabled = property(get_AutoWhiteBalanceEnabled, put_AutoWhiteBalanceEnabled)
    AutoExposureEnabled = property(get_AutoExposureEnabled, put_AutoExposureEnabled)
    Bounds = property(get_Bounds, put_Bounds)
    Type = property(get_Type, put_Type)
    BoundsNormalized = property(get_BoundsNormalized, put_BoundsNormalized)
    Weight = property(get_Weight, put_Weight)
RegionOfInterestType = Int32
RegionOfInterestType_Unknown: RegionOfInterestType = 0
RegionOfInterestType_Face: RegionOfInterestType = 1
class RegionsOfInterestControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.RegionsOfInterestControl'
    @winrt_mixinmethod
    def get_MaxRegions(self: Windows.Media.Devices.IRegionsOfInterestControl) -> UInt32: ...
    @winrt_mixinmethod
    def SetRegionsAsync(self: Windows.Media.Devices.IRegionsOfInterestControl, regions: Windows.Foundation.Collections.IIterable[Windows.Media.Devices.RegionOfInterest]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRegionsWithLockAsync(self: Windows.Media.Devices.IRegionsOfInterestControl, regions: Windows.Foundation.Collections.IIterable[Windows.Media.Devices.RegionOfInterest], lockValues: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearRegionsAsync(self: Windows.Media.Devices.IRegionsOfInterestControl) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_AutoFocusSupported(self: Windows.Media.Devices.IRegionsOfInterestControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutoWhiteBalanceSupported(self: Windows.Media.Devices.IRegionsOfInterestControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutoExposureSupported(self: Windows.Media.Devices.IRegionsOfInterestControl) -> Boolean: ...
    MaxRegions = property(get_MaxRegions, None)
    AutoFocusSupported = property(get_AutoFocusSupported, None)
    AutoWhiteBalanceSupported = property(get_AutoWhiteBalanceSupported, None)
    AutoExposureSupported = property(get_AutoExposureSupported, None)
class SceneModeControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.SceneModeControl'
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.ISceneModeControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.ISceneModeControl) -> Windows.Media.Devices.CaptureSceneMode: ...
    @winrt_mixinmethod
    def SetValueAsync(self: Windows.Media.Devices.ISceneModeControl, sceneMode: Windows.Media.Devices.CaptureSceneMode) -> Windows.Foundation.IAsyncAction: ...
    SupportedModes = property(get_SupportedModes, None)
    Value = property(get_Value, None)
SendCommandStatus = Int32
SendCommandStatus_Success: SendCommandStatus = 0
SendCommandStatus_DeviceNotAvailable: SendCommandStatus = 1
class TorchControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.TorchControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.ITorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerSupported(self: Windows.Media.Devices.ITorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Media.Devices.ITorchControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: Windows.Media.Devices.ITorchControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PowerPercent(self: Windows.Media.Devices.ITorchControl) -> Single: ...
    @winrt_mixinmethod
    def put_PowerPercent(self: Windows.Media.Devices.ITorchControl, value: Single) -> Void: ...
    Supported = property(get_Supported, None)
    PowerSupported = property(get_PowerSupported, None)
    Enabled = property(get_Enabled, put_Enabled)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
class VideoDeviceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.VideoDeviceController'
    @winrt_mixinmethod
    def get_Brightness(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Contrast(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Hue(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_WhiteBalance(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_BacklightCompensation(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Pan(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Tilt(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Zoom(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Roll(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Exposure(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def get_Focus(self: Windows.Media.Devices.IVideoDeviceController) -> Windows.Media.Devices.MediaDeviceControl: ...
    @winrt_mixinmethod
    def TrySetPowerlineFrequency(self: Windows.Media.Devices.IVideoDeviceController, value: Windows.Media.Capture.PowerlineFrequency) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetPowerlineFrequency(self: Windows.Media.Devices.IVideoDeviceController, value: POINTER(Windows.Media.Capture.PowerlineFrequency)) -> Boolean: ...
    @winrt_mixinmethod
    def GetAvailableMediaStreamProperties(self: Windows.Media.Devices.IMediaDeviceController, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Foundation.Collections.IVectorView[Windows.Media.MediaProperties.IMediaEncodingProperties]: ...
    @winrt_mixinmethod
    def GetMediaStreamProperties(self: Windows.Media.Devices.IMediaDeviceController, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Media.MediaProperties.IMediaEncodingProperties: ...
    @winrt_mixinmethod
    def SetMediaStreamPropertiesAsync(self: Windows.Media.Devices.IMediaDeviceController, mediaStreamType: Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetDeviceProperty(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController, propertyId: WinRT_String, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def GetDeviceProperty(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController, propertyId: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_LowLagPhotoSequence(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.LowLagPhotoSequenceControl: ...
    @winrt_mixinmethod
    def get_LowLagPhoto(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.LowLagPhotoControl: ...
    @winrt_mixinmethod
    def get_SceneModeControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.SceneModeControl: ...
    @winrt_mixinmethod
    def get_TorchControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.TorchControl: ...
    @winrt_mixinmethod
    def get_FlashControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.FlashControl: ...
    @winrt_mixinmethod
    def get_WhiteBalanceControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.WhiteBalanceControl: ...
    @winrt_mixinmethod
    def get_ExposureControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.ExposureControl: ...
    @winrt_mixinmethod
    def get_FocusControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.FocusControl: ...
    @winrt_mixinmethod
    def get_ExposureCompensationControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.ExposureCompensationControl: ...
    @winrt_mixinmethod
    def get_IsoSpeedControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.IsoSpeedControl: ...
    @winrt_mixinmethod
    def get_RegionsOfInterestControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.RegionsOfInterestControl: ...
    @winrt_mixinmethod
    def get_PrimaryUse(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2) -> Windows.Media.Devices.CaptureUse: ...
    @winrt_mixinmethod
    def put_PrimaryUse(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController2, value: Windows.Media.Devices.CaptureUse) -> Void: ...
    @winrt_mixinmethod
    def get_VariablePhotoSequenceController(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController3) -> Windows.Media.Devices.Core.VariablePhotoSequenceController: ...
    @winrt_mixinmethod
    def get_PhotoConfirmationControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController3) -> Windows.Media.Devices.PhotoConfirmationControl: ...
    @winrt_mixinmethod
    def get_ZoomControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController3) -> Windows.Media.Devices.ZoomControl: ...
    @winrt_mixinmethod
    def get_ExposurePriorityVideoControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> Windows.Media.Devices.ExposurePriorityVideoControl: ...
    @winrt_mixinmethod
    def get_DesiredOptimization(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> Windows.Media.Devices.MediaCaptureOptimization: ...
    @winrt_mixinmethod
    def put_DesiredOptimization(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4, value: Windows.Media.Devices.MediaCaptureOptimization) -> Void: ...
    @winrt_mixinmethod
    def get_HdrVideoControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> Windows.Media.Devices.HdrVideoControl: ...
    @winrt_mixinmethod
    def get_OpticalImageStabilizationControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> Windows.Media.Devices.OpticalImageStabilizationControl: ...
    @winrt_mixinmethod
    def get_AdvancedPhotoControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController4) -> Windows.Media.Devices.AdvancedPhotoControl: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDevicePropertyById(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, propertyId: WinRT_String, maxPropertyValueSize: Windows.Foundation.IReference[UInt32]) -> Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_mixinmethod
    def SetDevicePropertyById(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, propertyId: WinRT_String, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    @winrt_mixinmethod
    def GetDevicePropertyByExtendedId(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, extendedPropertyId: c_char_p_no, maxPropertyValueSize: Windows.Foundation.IReference[UInt32]) -> Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult: ...
    @winrt_mixinmethod
    def SetDevicePropertyByExtendedId(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController5, extendedPropertyId: c_char_p_no, propertyValue: c_char_p_no) -> Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus: ...
    @winrt_mixinmethod
    def get_VideoTemporalDenoisingControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController6) -> Windows.Media.Devices.VideoTemporalDenoisingControl: ...
    @winrt_mixinmethod
    def get_InfraredTorchControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController7) -> Windows.Media.Devices.InfraredTorchControl: ...
    @winrt_mixinmethod
    def get_PanelBasedOptimizationControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController8) -> Windows.Media.Devices.PanelBasedOptimizationControl: ...
    @winrt_mixinmethod
    def get_DigitalWindowControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController9) -> Windows.Media.Devices.DigitalWindowControl: ...
    @winrt_mixinmethod
    def get_CameraOcclusionInfo(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController10) -> Windows.Media.Devices.CameraOcclusionInfo: ...
    @winrt_mixinmethod
    def TryAcquireExclusiveControl(self: Windows.Media.Devices.IAdvancedVideoCaptureDeviceController11, deviceId: WinRT_String, mode: Windows.Media.Capture.MediaCaptureDeviceExclusiveControlReleaseMode) -> Boolean: ...
    Brightness = property(get_Brightness, None)
    Contrast = property(get_Contrast, None)
    Hue = property(get_Hue, None)
    WhiteBalance = property(get_WhiteBalance, None)
    BacklightCompensation = property(get_BacklightCompensation, None)
    Pan = property(get_Pan, None)
    Tilt = property(get_Tilt, None)
    Zoom = property(get_Zoom, None)
    Roll = property(get_Roll, None)
    Exposure = property(get_Exposure, None)
    Focus = property(get_Focus, None)
    LowLagPhotoSequence = property(get_LowLagPhotoSequence, None)
    LowLagPhoto = property(get_LowLagPhoto, None)
    SceneModeControl = property(get_SceneModeControl, None)
    TorchControl = property(get_TorchControl, None)
    FlashControl = property(get_FlashControl, None)
    WhiteBalanceControl = property(get_WhiteBalanceControl, None)
    ExposureControl = property(get_ExposureControl, None)
    FocusControl = property(get_FocusControl, None)
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    RegionsOfInterestControl = property(get_RegionsOfInterestControl, None)
    PrimaryUse = property(get_PrimaryUse, put_PrimaryUse)
    VariablePhotoSequenceController = property(get_VariablePhotoSequenceController, None)
    PhotoConfirmationControl = property(get_PhotoConfirmationControl, None)
    ZoomControl = property(get_ZoomControl, None)
    ExposurePriorityVideoControl = property(get_ExposurePriorityVideoControl, None)
    DesiredOptimization = property(get_DesiredOptimization, put_DesiredOptimization)
    HdrVideoControl = property(get_HdrVideoControl, None)
    OpticalImageStabilizationControl = property(get_OpticalImageStabilizationControl, None)
    AdvancedPhotoControl = property(get_AdvancedPhotoControl, None)
    Id = property(get_Id, None)
    VideoTemporalDenoisingControl = property(get_VideoTemporalDenoisingControl, None)
    InfraredTorchControl = property(get_InfraredTorchControl, None)
    PanelBasedOptimizationControl = property(get_PanelBasedOptimizationControl, None)
    DigitalWindowControl = property(get_DigitalWindowControl, None)
    CameraOcclusionInfo = property(get_CameraOcclusionInfo, None)
class VideoDeviceControllerGetDevicePropertyResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.Devices.IVideoDeviceControllerGetDevicePropertyResult) -> Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyStatus: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IVideoDeviceControllerGetDevicePropertyResult) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
VideoDeviceControllerGetDevicePropertyStatus = Int32
VideoDeviceControllerGetDevicePropertyStatus_Success: VideoDeviceControllerGetDevicePropertyStatus = 0
VideoDeviceControllerGetDevicePropertyStatus_UnknownFailure: VideoDeviceControllerGetDevicePropertyStatus = 1
VideoDeviceControllerGetDevicePropertyStatus_BufferTooSmall: VideoDeviceControllerGetDevicePropertyStatus = 2
VideoDeviceControllerGetDevicePropertyStatus_NotSupported: VideoDeviceControllerGetDevicePropertyStatus = 3
VideoDeviceControllerGetDevicePropertyStatus_DeviceNotAvailable: VideoDeviceControllerGetDevicePropertyStatus = 4
VideoDeviceControllerGetDevicePropertyStatus_MaxPropertyValueSizeTooSmall: VideoDeviceControllerGetDevicePropertyStatus = 5
VideoDeviceControllerGetDevicePropertyStatus_MaxPropertyValueSizeRequired: VideoDeviceControllerGetDevicePropertyStatus = 6
VideoDeviceControllerSetDevicePropertyStatus = Int32
VideoDeviceControllerSetDevicePropertyStatus_Success: VideoDeviceControllerSetDevicePropertyStatus = 0
VideoDeviceControllerSetDevicePropertyStatus_UnknownFailure: VideoDeviceControllerSetDevicePropertyStatus = 1
VideoDeviceControllerSetDevicePropertyStatus_NotSupported: VideoDeviceControllerSetDevicePropertyStatus = 2
VideoDeviceControllerSetDevicePropertyStatus_InvalidValue: VideoDeviceControllerSetDevicePropertyStatus = 3
VideoDeviceControllerSetDevicePropertyStatus_DeviceNotAvailable: VideoDeviceControllerSetDevicePropertyStatus = 4
VideoDeviceControllerSetDevicePropertyStatus_NotInControl: VideoDeviceControllerSetDevicePropertyStatus = 5
class VideoTemporalDenoisingControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.VideoTemporalDenoisingControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IVideoTemporalDenoisingControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.IVideoTemporalDenoisingControl) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.VideoTemporalDenoisingMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IVideoTemporalDenoisingControl) -> Windows.Media.Devices.VideoTemporalDenoisingMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Devices.IVideoTemporalDenoisingControl, value: Windows.Media.Devices.VideoTemporalDenoisingMode) -> Void: ...
    Supported = property(get_Supported, None)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, put_Mode)
VideoTemporalDenoisingMode = Int32
VideoTemporalDenoisingMode_Off: VideoTemporalDenoisingMode = 0
VideoTemporalDenoisingMode_On: VideoTemporalDenoisingMode = 1
VideoTemporalDenoisingMode_Auto: VideoTemporalDenoisingMode = 2
class WhiteBalanceControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.WhiteBalanceControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IWhiteBalanceControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Preset(self: Windows.Media.Devices.IWhiteBalanceControl) -> Windows.Media.Devices.ColorTemperaturePreset: ...
    @winrt_mixinmethod
    def SetPresetAsync(self: Windows.Media.Devices.IWhiteBalanceControl, preset: Windows.Media.Devices.ColorTemperaturePreset) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IWhiteBalanceControl) -> UInt32: ...
    @winrt_mixinmethod
    def SetValueAsync(self: Windows.Media.Devices.IWhiteBalanceControl, temperature: UInt32) -> Windows.Foundation.IAsyncAction: ...
    Supported = property(get_Supported, None)
    Preset = property(get_Preset, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, None)
class ZoomControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ZoomControl'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.IZoomControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IZoomControl) -> Single: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Media.Devices.IZoomControl, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedModes(self: Windows.Media.Devices.IZoomControl2) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.ZoomTransitionMode]: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IZoomControl2) -> Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_mixinmethod
    def Configure(self: Windows.Media.Devices.IZoomControl2, settings: Windows.Media.Devices.ZoomSettings) -> Void: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
    Value = property(get_Value, put_Value)
    SupportedModes = property(get_SupportedModes, None)
    Mode = property(get_Mode, None)
class ZoomSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.ZoomSettings'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Devices.ZoomSettings: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.IZoomSettings) -> Windows.Media.Devices.ZoomTransitionMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Devices.IZoomSettings, value: Windows.Media.Devices.ZoomTransitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.IZoomSettings) -> Single: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Media.Devices.IZoomSettings, value: Single) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Value = property(get_Value, put_Value)
ZoomTransitionMode = Int32
ZoomTransitionMode_Auto: ZoomTransitionMode = 0
ZoomTransitionMode_Direct: ZoomTransitionMode = 1
ZoomTransitionMode_Smooth: ZoomTransitionMode = 2
make_head(_module, 'AdvancedPhotoCaptureSettings')
make_head(_module, 'AdvancedPhotoControl')
make_head(_module, 'AudioDeviceController')
make_head(_module, 'AudioDeviceModule')
make_head(_module, 'AudioDeviceModuleNotificationEventArgs')
make_head(_module, 'AudioDeviceModulesManager')
make_head(_module, 'CameraOcclusionInfo')
make_head(_module, 'CameraOcclusionState')
make_head(_module, 'CameraOcclusionStateChangedEventArgs')
make_head(_module, 'DefaultAudioCaptureDeviceChangedEventArgs')
make_head(_module, 'DefaultAudioRenderDeviceChangedEventArgs')
make_head(_module, 'DigitalWindowBounds')
make_head(_module, 'DigitalWindowCapability')
make_head(_module, 'DigitalWindowControl')
make_head(_module, 'ExposureCompensationControl')
make_head(_module, 'ExposureControl')
make_head(_module, 'ExposurePriorityVideoControl')
make_head(_module, 'FlashControl')
make_head(_module, 'FocusControl')
make_head(_module, 'FocusSettings')
make_head(_module, 'HdrVideoControl')
make_head(_module, 'IAdvancedPhotoCaptureSettings')
make_head(_module, 'IAdvancedPhotoControl')
make_head(_module, 'IAdvancedVideoCaptureDeviceController')
make_head(_module, 'IAdvancedVideoCaptureDeviceController10')
make_head(_module, 'IAdvancedVideoCaptureDeviceController11')
make_head(_module, 'IAdvancedVideoCaptureDeviceController2')
make_head(_module, 'IAdvancedVideoCaptureDeviceController3')
make_head(_module, 'IAdvancedVideoCaptureDeviceController4')
make_head(_module, 'IAdvancedVideoCaptureDeviceController5')
make_head(_module, 'IAdvancedVideoCaptureDeviceController6')
make_head(_module, 'IAdvancedVideoCaptureDeviceController7')
make_head(_module, 'IAdvancedVideoCaptureDeviceController8')
make_head(_module, 'IAdvancedVideoCaptureDeviceController9')
make_head(_module, 'IAudioDeviceController')
make_head(_module, 'IAudioDeviceModule')
make_head(_module, 'IAudioDeviceModuleNotificationEventArgs')
make_head(_module, 'IAudioDeviceModulesManager')
make_head(_module, 'IAudioDeviceModulesManagerFactory')
make_head(_module, 'ICameraOcclusionInfo')
make_head(_module, 'ICameraOcclusionState')
make_head(_module, 'ICameraOcclusionStateChangedEventArgs')
make_head(_module, 'IDefaultAudioDeviceChangedEventArgs')
make_head(_module, 'IDigitalWindowBounds')
make_head(_module, 'IDigitalWindowCapability')
make_head(_module, 'IDigitalWindowControl')
make_head(_module, 'IExposureCompensationControl')
make_head(_module, 'IExposureControl')
make_head(_module, 'IExposurePriorityVideoControl')
make_head(_module, 'IFlashControl')
make_head(_module, 'IFlashControl2')
make_head(_module, 'IFocusControl')
make_head(_module, 'IFocusControl2')
make_head(_module, 'IFocusSettings')
make_head(_module, 'IHdrVideoControl')
make_head(_module, 'IInfraredTorchControl')
make_head(_module, 'IIsoSpeedControl')
make_head(_module, 'IIsoSpeedControl2')
make_head(_module, 'ILowLagPhotoControl')
make_head(_module, 'ILowLagPhotoSequenceControl')
make_head(_module, 'IMediaDeviceControl')
make_head(_module, 'IMediaDeviceControlCapabilities')
make_head(_module, 'IMediaDeviceController')
make_head(_module, 'IMediaDeviceStatics')
make_head(_module, 'IModuleCommandResult')
make_head(_module, 'IOpticalImageStabilizationControl')
make_head(_module, 'IPanelBasedOptimizationControl')
make_head(_module, 'IPhotoConfirmationControl')
make_head(_module, 'IRegionOfInterest')
make_head(_module, 'IRegionOfInterest2')
make_head(_module, 'IRegionsOfInterestControl')
make_head(_module, 'ISceneModeControl')
make_head(_module, 'ITorchControl')
make_head(_module, 'IVideoDeviceController')
make_head(_module, 'IVideoDeviceControllerGetDevicePropertyResult')
make_head(_module, 'IVideoTemporalDenoisingControl')
make_head(_module, 'IWhiteBalanceControl')
make_head(_module, 'IZoomControl')
make_head(_module, 'IZoomControl2')
make_head(_module, 'IZoomSettings')
make_head(_module, 'InfraredTorchControl')
make_head(_module, 'IsoSpeedControl')
make_head(_module, 'LowLagPhotoControl')
make_head(_module, 'LowLagPhotoSequenceControl')
make_head(_module, 'MediaDevice')
make_head(_module, 'MediaDeviceControl')
make_head(_module, 'MediaDeviceControlCapabilities')
make_head(_module, 'ModuleCommandResult')
make_head(_module, 'OpticalImageStabilizationControl')
make_head(_module, 'PanelBasedOptimizationControl')
make_head(_module, 'PhotoConfirmationControl')
make_head(_module, 'RegionOfInterest')
make_head(_module, 'RegionsOfInterestControl')
make_head(_module, 'SceneModeControl')
make_head(_module, 'TorchControl')
make_head(_module, 'VideoDeviceController')
make_head(_module, 'VideoDeviceControllerGetDevicePropertyResult')
make_head(_module, 'VideoTemporalDenoisingControl')
make_head(_module, 'WhiteBalanceControl')
make_head(_module, 'ZoomControl')
make_head(_module, 'ZoomSettings')
