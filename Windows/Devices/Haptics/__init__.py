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
import Windows.Devices.Haptics
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IKnownSimpleHapticsControllerWaveformsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3d577ef7-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
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
    Click = property(get_Click, None)
    BuzzContinuous = property(get_BuzzContinuous, None)
    RumbleContinuous = property(get_RumbleContinuous, None)
    Press = property(get_Press, None)
    Release = property(get_Release, None)
class IKnownSimpleHapticsControllerWaveformsStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a7d24c27-b79d-510a-bf-79-ff-6d-49-17-3e-1d')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3d577ef9-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedFeedback(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Haptics.SimpleHapticsControllerFeedback]: ...
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
    def SendHapticFeedback(self, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback) -> Void: ...
    @winrt_commethod(14)
    def SendHapticFeedbackWithIntensity(self, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double) -> Void: ...
    @winrt_commethod(15)
    def SendHapticFeedbackForDuration(self, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playDuration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(16)
    def SendHapticFeedbackForPlayCount(self, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playCount: Int32, replayPauseInterval: Windows.Foundation.TimeSpan) -> Void: ...
    Id = property(get_Id, None)
    SupportedFeedback = property(get_SupportedFeedback, None)
    IsIntensitySupported = property(get_IsIntensitySupported, None)
    IsPlayCountSupported = property(get_IsPlayCountSupported, None)
    IsPlayDurationSupported = property(get_IsPlayDurationSupported, None)
    IsReplayPauseIntervalSupported = property(get_IsReplayPauseIntervalSupported, None)
class ISimpleHapticsControllerFeedback(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3d577ef8-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_Waveform(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    Waveform = property(get_Waveform, None)
    Duration = property(get_Duration, None)
class IVibrationDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('40f21a3e-8844-47ff-b3-12-06-18-5a-38-44-da')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Id = property(get_Id, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IVibrationDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('53e2eded-2290-4ac9-8e-b3-1a-84-12-2e-b7-1c')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Haptics.VibrationAccessStatus]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_commethod(9)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_commethod(10)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Haptics.VibrationDevice]]: ...
class KnownSimpleHapticsControllerWaveforms(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Haptics.KnownSimpleHapticsControllerWaveforms'
    @winrt_classmethod
    def get_BrushContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_ChiselMarkerContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_EraserContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Error(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_GalaxyPenContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Hover(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_InkContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_MarkerContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_PencilContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Success(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics2) -> UInt16: ...
    @winrt_classmethod
    def get_Click(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BuzzContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RumbleContinuous(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Press(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Release(cls: Windows.Devices.Haptics.IKnownSimpleHapticsControllerWaveformsStatics) -> UInt16: ...
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
    Click = property(get_Click, None)
    BuzzContinuous = property(get_BuzzContinuous, None)
    RumbleContinuous = property(get_RumbleContinuous, None)
    Press = property(get_Press, None)
    Release = property(get_Release, None)
class SimpleHapticsController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Haptics.SimpleHapticsController'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Haptics.ISimpleHapticsController) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedFeedback(self: Windows.Devices.Haptics.ISimpleHapticsController) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Haptics.SimpleHapticsControllerFeedback]: ...
    @winrt_mixinmethod
    def get_IsIntensitySupported(self: Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlayCountSupported(self: Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlayDurationSupported(self: Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReplayPauseIntervalSupported(self: Windows.Devices.Haptics.ISimpleHapticsController) -> Boolean: ...
    @winrt_mixinmethod
    def StopFeedback(self: Windows.Devices.Haptics.ISimpleHapticsController) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedback(self: Windows.Devices.Haptics.ISimpleHapticsController, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedbackWithIntensity(self: Windows.Devices.Haptics.ISimpleHapticsController, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedbackForDuration(self: Windows.Devices.Haptics.ISimpleHapticsController, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playDuration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SendHapticFeedbackForPlayCount(self: Windows.Devices.Haptics.ISimpleHapticsController, feedback: Windows.Devices.Haptics.SimpleHapticsControllerFeedback, intensity: Double, playCount: Int32, replayPauseInterval: Windows.Foundation.TimeSpan) -> Void: ...
    Id = property(get_Id, None)
    SupportedFeedback = property(get_SupportedFeedback, None)
    IsIntensitySupported = property(get_IsIntensitySupported, None)
    IsPlayCountSupported = property(get_IsPlayCountSupported, None)
    IsPlayDurationSupported = property(get_IsPlayDurationSupported, None)
    IsReplayPauseIntervalSupported = property(get_IsReplayPauseIntervalSupported, None)
class SimpleHapticsControllerFeedback(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Haptics.SimpleHapticsControllerFeedback'
    @winrt_mixinmethod
    def get_Waveform(self: Windows.Devices.Haptics.ISimpleHapticsControllerFeedback) -> UInt16: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Devices.Haptics.ISimpleHapticsControllerFeedback) -> Windows.Foundation.TimeSpan: ...
    Waveform = property(get_Waveform, None)
    Duration = property(get_Duration, None)
VibrationAccessStatus = Int32
VibrationAccessStatus_Allowed: VibrationAccessStatus = 0
VibrationAccessStatus_DeniedByUser: VibrationAccessStatus = 1
VibrationAccessStatus_DeniedBySystem: VibrationAccessStatus = 2
VibrationAccessStatus_DeniedByEnergySaver: VibrationAccessStatus = 3
class VibrationDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Haptics.VibrationDevice'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Haptics.IVibrationDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.Devices.Haptics.IVibrationDevice) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Devices.Haptics.IVibrationDeviceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Haptics.VibrationAccessStatus]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Haptics.IVibrationDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Haptics.IVibrationDeviceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Haptics.IVibrationDeviceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Devices.Haptics.IVibrationDeviceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Haptics.VibrationDevice]]: ...
    Id = property(get_Id, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
make_head(_module, 'IKnownSimpleHapticsControllerWaveformsStatics')
make_head(_module, 'IKnownSimpleHapticsControllerWaveformsStatics2')
make_head(_module, 'ISimpleHapticsController')
make_head(_module, 'ISimpleHapticsControllerFeedback')
make_head(_module, 'IVibrationDevice')
make_head(_module, 'IVibrationDeviceStatics')
make_head(_module, 'KnownSimpleHapticsControllerWaveforms')
make_head(_module, 'SimpleHapticsController')
make_head(_module, 'SimpleHapticsControllerFeedback')
make_head(_module, 'VibrationDevice')
