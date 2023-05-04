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
import Windows.Foundation.Numerics
import Windows.Gaming.Input.ForceFeedback
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ConditionForceEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.ConditionForceEffect'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Gaming.Input.ForceFeedback.IConditionForceEffectFactory, effectKind: Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind) -> Windows.Gaming.Input.ForceFeedback.ConditionForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Gaming.Input.ForceFeedback.IConditionForceEffect) -> Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind: ...
    @winrt_mixinmethod
    def SetParameters(self: Windows.Gaming.Input.ForceFeedback.IConditionForceEffect, direction: Windows.Foundation.Numerics.Vector3, positiveCoefficient: Single, negativeCoefficient: Single, maxPositiveMagnitude: Single, maxNegativeMagnitude: Single, deadZone: Single, bias: Single) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
    Kind = property(get_Kind, None)
ConditionForceEffectKind = Int32
ConditionForceEffectKind_Spring: ConditionForceEffectKind = 0
ConditionForceEffectKind_Damper: ConditionForceEffectKind = 1
ConditionForceEffectKind_Inertia: ConditionForceEffectKind = 2
ConditionForceEffectKind_Friction: ConditionForceEffectKind = 3
class ConstantForceEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.ConstantForceEffect'
    @winrt_activatemethod
    def New(cls) -> Windows.Gaming.Input.ForceFeedback.ConstantForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def SetParameters(self: Windows.Gaming.Input.ForceFeedback.IConstantForceEffect, vector: Windows.Foundation.Numerics.Vector3, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SetParametersWithEnvelope(self: Windows.Gaming.Input.ForceFeedback.IConstantForceEffect, vector: Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: Windows.Foundation.TimeSpan, attackDuration: Windows.Foundation.TimeSpan, sustainDuration: Windows.Foundation.TimeSpan, releaseDuration: Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor'
    @winrt_mixinmethod
    def get_AreEffectsPaused(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Boolean: ...
    @winrt_mixinmethod
    def get_MasterGain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Double: ...
    @winrt_mixinmethod
    def put_MasterGain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedAxes(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectAxes: ...
    @winrt_mixinmethod
    def LoadEffectAsync(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor, effect: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.Input.ForceFeedback.ForceFeedbackLoadEffectResult]: ...
    @winrt_mixinmethod
    def PauseAllEffects(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Void: ...
    @winrt_mixinmethod
    def ResumeAllEffects(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Void: ...
    @winrt_mixinmethod
    def StopAllEffects(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Void: ...
    @winrt_mixinmethod
    def TryDisableAsync(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryEnableAsync(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryResetAsync(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryUnloadEffectAsync(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackMotor, effect: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    AreEffectsPaused = property(get_AreEffectsPaused, None)
    MasterGain = property(get_MasterGain, put_MasterGain)
    IsEnabled = property(get_IsEnabled, None)
    SupportedAxes = property(get_SupportedAxes, None)
class IConditionForceEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{32d1ea68-3695-4e69-85c0-cd1944189140}')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind: ...
    @winrt_commethod(7)
    def SetParameters(self, direction: Windows.Foundation.Numerics.Vector3, positiveCoefficient: Single, negativeCoefficient: Single, maxPositiveMagnitude: Single, maxNegativeMagnitude: Single, deadZone: Single, bias: Single) -> Void: ...
    Kind = property(get_Kind, None)
class IConditionForceEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{91a99264-1810-4eb6-a773-bfd3b8cddbab}')
    @winrt_commethod(6)
    def CreateInstance(self, effectKind: Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind) -> Windows.Gaming.Input.ForceFeedback.ConditionForceEffect: ...
class IConstantForceEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9bfa0140-f3c7-415c-b068-0f068734bce0}')
    @winrt_commethod(6)
    def SetParameters(self, vector: Windows.Foundation.Numerics.Vector3, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def SetParametersWithEnvelope(self, vector: Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: Windows.Foundation.TimeSpan, attackDuration: Windows.Foundation.TimeSpan, sustainDuration: Windows.Foundation.TimeSpan, releaseDuration: Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
class IForceFeedbackEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a17fba0c-2ae4-48c2-8063-eabd0777cb89}')
    @winrt_commethod(6)
    def get_Gain(self) -> Double: ...
    @winrt_commethod(7)
    def put_Gain(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
class IForceFeedbackMotor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_SupportedAxes(self) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectAxes: ...
    @winrt_commethod(11)
    def LoadEffectAsync(self, effect: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.Input.ForceFeedback.ForceFeedbackLoadEffectResult]: ...
    @winrt_commethod(12)
    def PauseAllEffects(self) -> Void: ...
    @winrt_commethod(13)
    def ResumeAllEffects(self) -> Void: ...
    @winrt_commethod(14)
    def StopAllEffects(self) -> Void: ...
    @winrt_commethod(15)
    def TryDisableAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(16)
    def TryEnableAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(17)
    def TryResetAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(18)
    def TryUnloadEffectAsync(self, effect: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    AreEffectsPaused = property(get_AreEffectsPaused, None)
    MasterGain = property(get_MasterGain, put_MasterGain)
    IsEnabled = property(get_IsEnabled, None)
    SupportedAxes = property(get_SupportedAxes, None)
class IPeriodicForceEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5c5138d7-fc75-4d52-9a0a-efe4cab5fe64}')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind: ...
    @winrt_commethod(7)
    def SetParameters(self, vector: Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def SetParametersWithEnvelope(self, vector: Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: Windows.Foundation.TimeSpan, attackDuration: Windows.Foundation.TimeSpan, sustainDuration: Windows.Foundation.TimeSpan, releaseDuration: Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
    Kind = property(get_Kind, None)
class IPeriodicForceEffectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6f62eb1a-9851-477b-b318-35ecaa15070f}')
    @winrt_commethod(6)
    def CreateInstance(self, effectKind: Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind) -> Windows.Gaming.Input.ForceFeedback.PeriodicForceEffect: ...
class IRampForceEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f1f81259-1ca6-4080-b56d-b43f3354d052}')
    @winrt_commethod(6)
    def SetParameters(self, startVector: Windows.Foundation.Numerics.Vector3, endVector: Windows.Foundation.Numerics.Vector3, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def SetParametersWithEnvelope(self, startVector: Windows.Foundation.Numerics.Vector3, endVector: Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: Windows.Foundation.TimeSpan, attackDuration: Windows.Foundation.TimeSpan, sustainDuration: Windows.Foundation.TimeSpan, releaseDuration: Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
class PeriodicForceEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.PeriodicForceEffect'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffectFactory, effectKind: Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind) -> Windows.Gaming.Input.ForceFeedback.PeriodicForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffect) -> Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind: ...
    @winrt_mixinmethod
    def SetParameters(self: Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffect, vector: Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SetParametersWithEnvelope(self: Windows.Gaming.Input.ForceFeedback.IPeriodicForceEffect, vector: Windows.Foundation.Numerics.Vector3, frequency: Single, phase: Single, bias: Single, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: Windows.Foundation.TimeSpan, attackDuration: Windows.Foundation.TimeSpan, sustainDuration: Windows.Foundation.TimeSpan, releaseDuration: Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect
    _classid_ = 'Windows.Gaming.Input.ForceFeedback.RampForceEffect'
    @winrt_activatemethod
    def New(cls) -> Windows.Gaming.Input.ForceFeedback.RampForceEffect: ...
    @winrt_mixinmethod
    def get_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Double: ...
    @winrt_mixinmethod
    def put_Gain(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState: ...
    @winrt_mixinmethod
    def Start(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Gaming.Input.ForceFeedback.IForceFeedbackEffect) -> Void: ...
    @winrt_mixinmethod
    def SetParameters(self: Windows.Gaming.Input.ForceFeedback.IRampForceEffect, startVector: Windows.Foundation.Numerics.Vector3, endVector: Windows.Foundation.Numerics.Vector3, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SetParametersWithEnvelope(self: Windows.Gaming.Input.ForceFeedback.IRampForceEffect, startVector: Windows.Foundation.Numerics.Vector3, endVector: Windows.Foundation.Numerics.Vector3, attackGain: Single, sustainGain: Single, releaseGain: Single, startDelay: Windows.Foundation.TimeSpan, attackDuration: Windows.Foundation.TimeSpan, sustainDuration: Windows.Foundation.TimeSpan, releaseDuration: Windows.Foundation.TimeSpan, repeatCount: UInt32) -> Void: ...
    Gain = property(get_Gain, put_Gain)
    State = property(get_State, None)
make_head(_module, 'ConditionForceEffect')
make_head(_module, 'ConstantForceEffect')
make_head(_module, 'ForceFeedbackMotor')
make_head(_module, 'IConditionForceEffect')
make_head(_module, 'IConditionForceEffectFactory')
make_head(_module, 'IConstantForceEffect')
make_head(_module, 'IForceFeedbackEffect')
make_head(_module, 'IForceFeedbackMotor')
make_head(_module, 'IPeriodicForceEffect')
make_head(_module, 'IPeriodicForceEffectFactory')
make_head(_module, 'IRampForceEffect')
make_head(_module, 'PeriodicForceEffect')
make_head(_module, 'RampForceEffect')
