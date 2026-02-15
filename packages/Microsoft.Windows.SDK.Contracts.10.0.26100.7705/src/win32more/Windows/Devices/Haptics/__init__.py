from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Devices.Haptics
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class HapticDeviceType(Enum, Int32):
    _name_ = 'Windows.Devices.Haptics.HapticDeviceType'
    None_ = 0
    Generic = 1
    Pen = 2
    Touchpad = 3
    Mouse = 4
class HapticsControllerOverrideToken(Structure):
    _name_ = 'Windows.Devices.Haptics.HapticsControllerOverrideToken'
    Value: Int64
class IInputHapticsManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.IInputHapticsManager'
    _iid_ = Guid('{040e91df-bb3a-507c-9e25-a2d2c685b2e5}')
    @winrt_commethod(6)
    def get_ThreadId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CurrentHapticsControllerDeviceType(self) -> win32more.Windows.Devices.Haptics.HapticDeviceType: ...
    @winrt_commethod(8)
    def get_CurrentHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_commethod(9)
    def TrySendHapticWaveform(self, waveform: UInt16, waveformFallback: UInt16) -> Boolean: ...
    @winrt_commethod(10)
    def TrySendHapticWaveformWithIntensity(self, waveform: UInt16, waveformFallback: UInt16, intensity: Double) -> Boolean: ...
    @winrt_commethod(11)
    def TrySendHapticWaveformForDuration(self, waveform: UInt16, waveformFallback: UInt16, intensity: Double, playDuration: win32more.Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_commethod(12)
    def TrySendHapticWaveformForPlayCount(self, waveform: UInt16, waveformFallback: UInt16, intensity: Double, playCount: Int32, replayPauseInterval: win32more.Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_commethod(13)
    def TryStopFeedback(self) -> Boolean: ...
    @winrt_commethod(14)
    def SetOverrideHapticsController(self, deviceType: win32more.Windows.Devices.Haptics.HapticDeviceType, controller: win32more.Windows.Devices.Haptics.SimpleHapticsController) -> win32more.Windows.Devices.Haptics.HapticsControllerOverrideToken: ...
    @winrt_commethod(15)
    def ClearOverrideHapticsController(self, token: win32more.Windows.Devices.Haptics.HapticsControllerOverrideToken) -> Void: ...
    CurrentHapticsController = property(get_CurrentHapticsController, None)
    CurrentHapticsControllerDeviceType = property(get_CurrentHapticsControllerDeviceType, None)
    ThreadId = property(get_ThreadId, None)
class IInputHapticsManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.IInputHapticsManagerStatics'
    _iid_ = Guid('{7bb40f77-e187-5322-844e-aa58223c281a}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsHapticDevicePresent(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetForCurrentThread(self) -> win32more.Windows.Devices.Haptics.InputHapticsManager: ...
    @winrt_commethod(9)
    def TryGetForThread(self, ThreadId: UInt32) -> win32more.Windows.Devices.Haptics.InputHapticsManager: ...
class IKnownSimpleHapticsControllerWaveformsStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics'
    _iid_ = Guid('{3d577ef7-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Click(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_BuzzContinuous(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_RumbleContinuous(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_Press(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_Release(self) -> UInt16: ...
    BuzzContinuous = property(get_BuzzContinuous, None)
    Click = property(get_Click, None)
    Press = property(get_Press, None)
    Release = property(get_Release, None)
    RumbleContinuous = property(get_RumbleContinuous, None)
class IKnownSimpleHapticsControllerWaveformsStatics2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2'
    _iid_ = Guid('{a7d24c27-b79d-510a-bf79-ff6d49173e1d}')
    @winrt_commethod(6)
    def get_BrushContinuous(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_ChiselMarkerContinuous(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_EraserContinuous(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_Error(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_GalaxyPenContinuous(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_Hover(self) -> UInt16: ...
    @winrt_commethod(12)
    def get_InkContinuous(self) -> UInt16: ...
    @winrt_commethod(13)
    def get_MarkerContinuous(self) -> UInt16: ...
    @winrt_commethod(14)
    def get_PencilContinuous(self) -> UInt16: ...
    @winrt_commethod(15)
    def get_Success(self) -> UInt16: ...
    BrushContinuous = property(get_BrushContinuous, None)
    ChiselMarkerContinuous = property(get_ChiselMarkerContinuous, None)
    EraserContinuous = property(get_EraserContinuous, None)
    Error = property(get_Error, None)
    GalaxyPenContinuous = property(get_GalaxyPenContinuous, None)
    Hover = property(get_Hover, None)
    InkContinuous = property(get_InkContinuous, None)
    MarkerContinuous = property(get_MarkerContinuous, None)
    PencilContinuous = property(get_PencilContinuous, None)
    Success = property(get_Success, None)
class ISimpleHapticsController(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.ISimpleHapticsController'
    _iid_ = Guid('{3d577ef9-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(7)
    def get_SupportedFeedback(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback]: ...
    @winrt_commethod(8)
    def get_IsIntensitySupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsPlayCountSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsPlayDurationSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsReplayPauseIntervalSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def StopFeedback(self) -> Void: ...
    @winrt_commethod(13)
    def SendHapticFeedback(self, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback) -> Void: ...
    @winrt_commethod(14)
    def SendHapticFeedbackWithIntensity(self, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double) -> Void: ...
    @winrt_commethod(15)
    def SendHapticFeedbackForDuration(self, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playDuration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(16)
    def SendHapticFeedbackForPlayCount(self, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playCount: Int32, replayPauseInterval: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    Id = property(get_Id, None)
    IsIntensitySupported = property(get_IsIntensitySupported, None)
    IsPlayCountSupported = property(get_IsPlayCountSupported, None)
    IsPlayDurationSupported = property(get_IsPlayDurationSupported, None)
    IsReplayPauseIntervalSupported = property(get_IsReplayPauseIntervalSupported, None)
    SupportedFeedback = property(get_SupportedFeedback, None)
class ISimpleHapticsControllerFeedback(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.ISimpleHapticsControllerFeedback'
    _iid_ = Guid('{3d577ef8-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Waveform(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Duration = property(get_Duration, None)
    Waveform = property(get_Waveform, None)
class IVibrationDevice(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.IVibrationDevice'
    _iid_ = Guid('{40f21a3e-8844-47ff-b312-06185a3844da}')
    @winrt_commethod(6)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Id = property(get_Id, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IVibrationDeviceStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.IVibrationDeviceStatics'
    _iid_ = Guid('{53e2eded-2290-4ac9-8eb3-1a84122eb71c}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationAccessStatus]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> hstr: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_commethod(9)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_commethod(10)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.VibrationDevice]]: ...
class InputHapticsManager(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Devices.Haptics.IInputHapticsManager
    _classid_ = 'Windows.Devices.Haptics.InputHapticsManager'
    @winrt_mixinmethod
    def get_ThreadId(self: win32more.Windows.Devices.Haptics.IInputHapticsManager) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentHapticsControllerDeviceType(self: win32more.Windows.Devices.Haptics.IInputHapticsManager) -> win32more.Windows.Devices.Haptics.HapticDeviceType: ...
    @winrt_mixinmethod
    def get_CurrentHapticsController(self: win32more.Windows.Devices.Haptics.IInputHapticsManager) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_mixinmethod
    def TrySendHapticWaveform(self: win32more.Windows.Devices.Haptics.IInputHapticsManager, waveform: UInt16, waveformFallback: UInt16) -> Boolean: ...
    @winrt_mixinmethod
    def TrySendHapticWaveformWithIntensity(self: win32more.Windows.Devices.Haptics.IInputHapticsManager, waveform: UInt16, waveformFallback: UInt16, intensity: Double) -> Boolean: ...
    @winrt_mixinmethod
    def TrySendHapticWaveformForDuration(self: win32more.Windows.Devices.Haptics.IInputHapticsManager, waveform: UInt16, waveformFallback: UInt16, intensity: Double, playDuration: win32more.Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_mixinmethod
    def TrySendHapticWaveformForPlayCount(self: win32more.Windows.Devices.Haptics.IInputHapticsManager, waveform: UInt16, waveformFallback: UInt16, intensity: Double, playCount: Int32, replayPauseInterval: win32more.Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_mixinmethod
    def TryStopFeedback(self: win32more.Windows.Devices.Haptics.IInputHapticsManager) -> Boolean: ...
    @winrt_mixinmethod
    def SetOverrideHapticsController(self: win32more.Windows.Devices.Haptics.IInputHapticsManager, deviceType: win32more.Windows.Devices.Haptics.HapticDeviceType, controller: win32more.Windows.Devices.Haptics.SimpleHapticsController) -> win32more.Windows.Devices.Haptics.HapticsControllerOverrideToken: ...
    @winrt_mixinmethod
    def ClearOverrideHapticsController(self: win32more.Windows.Devices.Haptics.IInputHapticsManager, token: win32more.Windows.Devices.Haptics.HapticsControllerOverrideToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Devices.Haptics.IInputHapticsManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def IsHapticDevicePresent(cls: win32more.Windows.Devices.Haptics.IInputHapticsManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentThread(cls: win32more.Windows.Devices.Haptics.IInputHapticsManagerStatics) -> win32more.Windows.Devices.Haptics.InputHapticsManager: ...
    @winrt_classmethod
    def TryGetForThread(cls: win32more.Windows.Devices.Haptics.IInputHapticsManagerStatics, ThreadId: UInt32) -> win32more.Windows.Devices.Haptics.InputHapticsManager: ...
    CurrentHapticsController = property(get_CurrentHapticsController, None)
    CurrentHapticsControllerDeviceType = property(get_CurrentHapticsControllerDeviceType, None)
    ThreadId = property(get_ThreadId, None)
class _KnownSimpleHapticsControllerWaveforms_Meta_(ComPtr.__class__):
    pass
class KnownSimpleHapticsControllerWaveforms(ComPtr, metaclass=_KnownSimpleHapticsControllerWaveforms_Meta_):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Haptics.KnownSimpleHapticsControllerWaveforms'
    @winrt_classmethod
    def get_BrushContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_ChiselMarkerContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_EraserContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Error(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_GalaxyPenContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Hover(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_InkContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_MarkerContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_PencilContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Success(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Click(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BuzzContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RumbleContinuous(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Press(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Release(cls: win32more.Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    _KnownSimpleHapticsControllerWaveforms_Meta_.BrushContinuous = property(get_BrushContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.BuzzContinuous = property(get_BuzzContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.ChiselMarkerContinuous = property(get_ChiselMarkerContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.Click = property(get_Click, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.EraserContinuous = property(get_EraserContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.Error = property(get_Error, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.GalaxyPenContinuous = property(get_GalaxyPenContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.Hover = property(get_Hover, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.InkContinuous = property(get_InkContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.MarkerContinuous = property(get_MarkerContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.PencilContinuous = property(get_PencilContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.Press = property(get_Press, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.Release = property(get_Release, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.RumbleContinuous = property(get_RumbleContinuous, None)
    _KnownSimpleHapticsControllerWaveforms_Meta_.Success = property(get_Success, None)
class SimpleHapticsController(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Devices.Haptics.ISimpleHapticsController
    _classid_ = 'Windows.Devices.Haptics.SimpleHapticsController'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> hstr: ...
    @winrt_mixinmethod
    def get_SupportedFeedback(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback]: ...
    @winrt_mixinmethod
    def get_IsIntensitySupported(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlayCountSupported(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlayDurationSupported(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReplayPauseIntervalSupported(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def StopFeedback(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedback(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedbackWithIntensity(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedbackForDuration(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playDuration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedbackForPlayCount(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController, feedback: win32more.Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playCount: Int32, replayPauseInterval: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    Id = property(get_Id, None)
    IsIntensitySupported = property(get_IsIntensitySupported, None)
    IsPlayCountSupported = property(get_IsPlayCountSupported, None)
    IsPlayDurationSupported = property(get_IsPlayDurationSupported, None)
    IsReplayPauseIntervalSupported = property(get_IsReplayPauseIntervalSupported, None)
    SupportedFeedback = property(get_SupportedFeedback, None)
class SimpleHapticsControllerFeedback(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Devices.Haptics.ISimpleHapticsControllerFeedback
    _classid_ = 'Windows.Devices.Haptics.SimpleHapticsControllerFeedback'
    @winrt_mixinmethod
    def get_Waveform(self: win32more.Windows.Devices.Haptics.ISimpleHapticsControllerFeedback) -> UInt16: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Devices.Haptics.ISimpleHapticsControllerFeedback) -> win32more.Windows.Foundation.TimeSpan: ...
    Duration = property(get_Duration, None)
    Waveform = property(get_Waveform, None)
class VibrationAccessStatus(Enum, Int32):
    _name_ = 'Windows.Devices.Haptics.VibrationAccessStatus'
    Allowed = 0
    DeniedByUser = 1
    DeniedBySystem = 2
    DeniedByEnergySaver = 3
class VibrationDevice(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Devices.Haptics.IVibrationDevice
    _classid_ = 'Windows.Devices.Haptics.VibrationDevice'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Haptics.IVibrationDevice) -> hstr: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.Devices.Haptics.IVibrationDevice) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationAccessStatus]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> hstr: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics, deviceId: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.VibrationDevice]]: ...
    Id = property(get_Id, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)


make_ready(__name__)
