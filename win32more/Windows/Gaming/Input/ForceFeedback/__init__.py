from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Gaming.Input.ForceFeedback
class ConditionForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.ConditionForceEffect'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Gaming.Input.ForceFeedback.ConditionForceEffect.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Gaming.Input.ForceFeedback.IConditionForceEffectFactory, effectKind: win32more.Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind) -> win32more.Windows.Gaming.Input.ForceFeedback.ConditionForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Gaming.Input.ForceFeedback.IConditionForceEffect) -> win32more.Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind: ...
    @winrt_mixinmethod
    def SetParameters(self: win32more.Windows.Gaming.Input.ForceFeedback.IConditionForceEffect, direction: win32more.Windows.Foundation.Numerics.Vector3, positiveCoefficient: Single, negativeCoefficient: Single, maxPositiveMagnitude: Single, maxNegativeMagnitude: Single, deadZone: Single, bias: Single) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
    Kind = property(get_Kind, None)
ConditionForceEffectKind = Int32
ConditionForceEffectKind_Spring: ConditionForceEffectKind = 0
ConditionForceEffectKind_Damper: ConditionForceEffectKind = 1
ConditionForceEffectKind_Inertia: ConditionForceEffectKind = 2
ConditionForceEffectKind_Friction: ConditionForceEffectKind = 3
class ConstantForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.ConstantForceEffect'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Gaming.Input.ForceFeedback.ConstantForceEffect.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Gaming.Input.ForceFeedback.ConstantForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def SetParameters(self: win32more.Windows.Gaming.Input.ForceFeedback.IConstantForceEffect, vector: win32more.Windows.Foundation.Numerics.Vector3, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SetParametersWithEnvelope(self: win32more.Windows.Gaming.Input.ForceFeedback.IConstantForceEffect, vector: win32more.Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: win32more.Windows.Foundation.TimeSpan, attackDuration: win32more.Windows.Foundation.TimeSpan, sustainDuration: win32more.Windows.Foundation.TimeSpan, releaseDuration: win32more.Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
ForceFeedbackEffectAxes = UInt32
ForceFeedbackEffectAxes_None: ForceFeedbackEffectAxes = 0
ForceFeedbackEffectAxes_X: ForceFeedbackEffectAxes = 1
ForceFeedbackEffectAxes_Y: ForceFeedbackEffectAxes = 2
ForceFeedbackEffectAxes_Z: ForceFeedbackEffectAxes = 4
ForceFeedbackEffectState = Int32
ForceFeedbackEffectState_Stopped: ForceFeedbackEffectState = 0
ForceFeedbackEffectState_Running: ForceFeedbackEffectState = 1
ForceFeedbackEffectState_Paused: ForceFeedbackEffectState = 2
ForceFeedbackEffectState_Faulted: ForceFeedbackEffectState = 3
ForceFeedbackLoadEffectResult = Int32
ForceFeedbackLoadEffectResult_Succeeded: ForceFeedbackLoadEffectResult = 0
ForceFeedbackLoadEffectResult_EffectStorageFull: ForceFeedbackLoadEffectResult = 1
ForceFeedbackLoadEffectResult_EffectNotSupported: ForceFeedbackLoadEffectResult = 2
class ForceFeedbackMotor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor'
    @winrt_mixinmethod
    def get_AreEffectsPaused(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Boolean: ...
    @winrt_mixinmethod
    def get_MasterGain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Double: ...
    @winrt_mixinmethod
    def put_MasterGain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedAxes(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectAxes: ...
    @winrt_mixinmethod
    def LoadEffectAsync(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor, effect: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackLoadEffectResult]: ...
    @winrt_mixinmethod
    def PauseAllEffects(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Void: ...
    @winrt_mixinmethod
    def ResumeAllEffects(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Void: ...
    @winrt_mixinmethod
    def StopAllEffects(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Void: ...
    @winrt_mixinmethod
    def TryDisableAsync(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryEnableAsync(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryResetAsync(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryUnloadEffectAsync(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor, effect: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    AreEffectsPaused = property(get_AreEffectsPaused, None)
    MasterGain = property(get_MasterGain, put_MasterGain)
    IsEnabled = property(get_IsEnabled, None)
    SupportedAxes = property(get_SupportedAxes, None)
class IConditionForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IConditionForceEffect'
    _iid_ = Guid('{32d1ea68-3695-4e69-85c0-cd1944189140}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind: ...
    @winrt_commethod(7)
    def SetParameters(self, direction: win32more.Windows.Foundation.Numerics.Vector3, positiveCoefficient: Single, negativeCoefficient: Single, maxPositiveMagnitude: Single, maxNegativeMagnitude: Single, deadZone: Single, bias: Single) -> Void: ...
    Kind = property(get_Kind, None)
class IConditionForceEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IConditionForceEffectFactory'
    _iid_ = Guid('{91a99264-1810-4eb6-a773-bfd3b8cddbab}')
    @winrt_commethod(6)
    def CreateInstance(self, effectKind: win32more.Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind) -> win32more.Windows.Gaming.Input.ForceFeedback.ConditionForceEffect: ...
class IConstantForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IConstantForceEffect'
    _iid_ = Guid('{9bfa0140-f3c7-415c-b068-0f068734bce0}')
    @winrt_commethod(6)
    def SetParameters(self, vector: win32more.Windows.Foundation.Numerics.Vector3, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def SetParametersWithEnvelope(self, vector: win32more.Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: win32more.Windows.Foundation.TimeSpan, attackDuration: win32more.Windows.Foundation.TimeSpan, sustainDuration: win32more.Windows.Foundation.TimeSpan, releaseDuration: win32more.Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
class IForceFeedbackEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect'
    _iid_ = Guid('{a17fba0c-2ae4-48c2-8063-eabd0777cb89}')
    @winrt_commethod(6)
    def get_Gain(self) -> Double: ...
    @winrt_commethod(7)
    def put_Gain(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
class IForceFeedbackMotor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor'
    _iid_ = Guid('{8d3d417c-a5ea-4516-8026-2b00f74ef6e5}')
    @winrt_commethod(6)
    def get_AreEffectsPaused(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MasterGain(self) -> Double: ...
    @winrt_commethod(8)
    def put_MasterGain(self, value: Double) -> Void: ...
    @winrt_commethod(9)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_SupportedAxes(self) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectAxes: ...
    @winrt_commethod(11)
    def LoadEffectAsync(self, effect: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackLoadEffectResult]: ...
    @winrt_commethod(12)
    def PauseAllEffects(self) -> Void: ...
    @winrt_commethod(13)
    def ResumeAllEffects(self) -> Void: ...
    @winrt_commethod(14)
    def StopAllEffects(self) -> Void: ...
    @winrt_commethod(15)
    def TryDisableAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(16)
    def TryEnableAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(17)
    def TryResetAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(18)
    def TryUnloadEffectAsync(self, effect: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    AreEffectsPaused = property(get_AreEffectsPaused, None)
    MasterGain = property(get_MasterGain, put_MasterGain)
    IsEnabled = property(get_IsEnabled, None)
    SupportedAxes = property(get_SupportedAxes, None)
class IPeriodicForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffect'
    _iid_ = Guid('{5c5138d7-fc75-4d52-9a0a-efe4cab5fe64}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind: ...
    @winrt_commethod(7)
    def SetParameters(self, vector: win32more.Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def SetParametersWithEnvelope(self, vector: win32more.Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: win32more.Windows.Foundation.TimeSpan, attackDuration: win32more.Windows.Foundation.TimeSpan, sustainDuration: win32more.Windows.Foundation.TimeSpan, releaseDuration: win32more.Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
    Kind = property(get_Kind, None)
class IPeriodicForceEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffectFactory'
    _iid_ = Guid('{6f62eb1a-9851-477b-b318-35ecaa15070f}')
    @winrt_commethod(6)
    def CreateInstance(self, effectKind: win32more.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind) -> win32more.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffect: ...
class IRampForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.IRampForceEffect'
    _iid_ = Guid('{f1f81259-1ca6-4080-b56d-b43f3354d052}')
    @winrt_commethod(6)
    def SetParameters(self, startVector: win32more.Windows.Foundation.Numerics.Vector3, endVector: win32more.Windows.Foundation.Numerics.Vector3, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def SetParametersWithEnvelope(self, startVector: win32more.Windows.Foundation.Numerics.Vector3, endVector: win32more.Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: win32more.Windows.Foundation.TimeSpan, attackDuration: win32more.Windows.Foundation.TimeSpan, sustainDuration: win32more.Windows.Foundation.TimeSpan, releaseDuration: win32more.Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
class PeriodicForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.PeriodicForceEffect'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffect.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffectFactory, effectKind: win32more.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind) -> win32more.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffect) -> win32more.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind: ...
    @winrt_mixinmethod
    def SetParameters(self: win32more.Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffect, vector: win32more.Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SetParametersWithEnvelope(self: win32more.Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffect, vector: win32more.Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: win32more.Windows.Foundation.TimeSpan, attackDuration: win32more.Windows.Foundation.TimeSpan, sustainDuration: win32more.Windows.Foundation.TimeSpan, releaseDuration: win32more.Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
    Kind = property(get_Kind, None)
PeriodicForceEffectKind = Int32
PeriodicForceEffectKind_SquareWave: PeriodicForceEffectKind = 0
PeriodicForceEffectKind_SineWave: PeriodicForceEffectKind = 1
PeriodicForceEffectKind_TriangleWave: PeriodicForceEffectKind = 2
PeriodicForceEffectKind_SawtoothWaveUp: PeriodicForceEffectKind = 3
PeriodicForceEffectKind_SawtoothWaveDown: PeriodicForceEffectKind = 4
class RampForceEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.RampForceEffect'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Gaming.Input.ForceFeedback.RampForceEffect.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Gaming.Input.ForceFeedback.RampForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def SetParameters(self: win32more.Windows.Gaming.Input.ForceFeedback.IRampForceEffect, startVector: win32more.Windows.Foundation.Numerics.Vector3, endVector: win32more.Windows.Foundation.Numerics.Vector3, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SetParametersWithEnvelope(self: win32more.Windows.Gaming.Input.ForceFeedback.IRampForceEffect, startVector: win32more.Windows.Foundation.Numerics.Vector3, endVector: win32more.Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: win32more.Windows.Foundation.TimeSpan, attackDuration: win32more.Windows.Foundation.TimeSpan, sustainDuration: win32more.Windows.Foundation.TimeSpan, releaseDuration: win32more.Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
make_ready(__name__)
