from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Haptics
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IKnownSimpleHapticsControllerWaveformsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Haptics.ISimpleHapticsController'
    _iid_ = Guid('{3d577ef9-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Haptics.ISimpleHapticsControllerFeedback'
    _iid_ = Guid('{3d577ef8-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Waveform(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Duration = property(get_Duration, None)
    Waveform = property(get_Waveform, None)
class IVibrationDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Haptics.IVibrationDevice'
    _iid_ = Guid('{40f21a3e-8844-47ff-b312-06185a3844da}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Id = property(get_Id, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IVibrationDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Haptics.IVibrationDeviceStatics'
    _iid_ = Guid('{53e2eded-2290-4ac9-8eb3-1a84122eb71c}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationAccessStatus]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_commethod(9)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_commethod(10)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.VibrationDevice]]: ...
class _KnownSimpleHapticsControllerWaveforms_Meta_(ComPtr.__class__):
    pass
class KnownSimpleHapticsControllerWaveforms(ComPtr, metaclass=_KnownSimpleHapticsControllerWaveforms_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Haptics.ISimpleHapticsController
    _classid_ = 'Windows.Devices.Haptics.SimpleHapticsController'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Haptics.ISimpleHapticsController) -> WinRT_String: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Haptics.ISimpleHapticsControllerFeedback
    _classid_ = 'Windows.Devices.Haptics.SimpleHapticsControllerFeedback'
    @winrt_mixinmethod
    def get_Waveform(self: win32more.Windows.Devices.Haptics.ISimpleHapticsControllerFeedback) -> UInt16: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Devices.Haptics.ISimpleHapticsControllerFeedback) -> win32more.Windows.Foundation.TimeSpan: ...
    Duration = property(get_Duration, None)
    Waveform = property(get_Waveform, None)
class VibrationAccessStatus(Enum, Int32):
    Allowed = 0
    DeniedByUser = 1
    DeniedBySystem = 2
    DeniedByEnergySaver = 3
class VibrationDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Haptics.IVibrationDevice
    _classid_ = 'Windows.Devices.Haptics.VibrationDevice'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Haptics.IVibrationDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.Devices.Haptics.IVibrationDevice) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationAccessStatus]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Haptics.VibrationDevice]: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Devices.Haptics.IVibrationDeviceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.VibrationDevice]]: ...
    Id = property(get_Id, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)


make_ready(__name__)
