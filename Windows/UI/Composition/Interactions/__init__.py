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
import Windows.Foundation.Numerics
import Windows.UI.Composition
import Windows.UI.Composition.Interactions
import Windows.UI.Input
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CompositionConditionalValue(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    _classid_ = 'Windows.UI.Composition.Interactions.CompositionConditionalValue'
    @winrt_mixinmethod
    def get_Condition(self: Windows.UI.Composition.Interactions.ICompositionConditionalValue) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: Windows.UI.Composition.Interactions.ICompositionConditionalValue, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Composition.Interactions.ICompositionConditionalValue) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.UI.Composition.Interactions.ICompositionConditionalValue, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Interactions.ICompositionConditionalValueStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.CompositionConditionalValue: ...
    Condition = property(get_Condition, put_Condition)
    Value = property(get_Value, put_Value)
class CompositionInteractionSourceCollection(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    _classid_ = 'Windows.UI.Composition.Interactions.CompositionInteractionSourceCollection'
    @winrt_mixinmethod
    def get_Count(self: Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection) -> Int32: ...
    @winrt_mixinmethod
    def Add(self: Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection, value: Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection, value: Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.ICompositionInteractionSource]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.Interactions.ICompositionInteractionSource]: ...
    Count = property(get_Count, None)
class ICompositionConditionalValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{43250538-eb73-4561-a71d-1a43eaeb7a9b}')
    @winrt_commethod(6)
    def get_Condition(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_Value(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    Value = property(get_Value, put_Value)
class ICompositionConditionalValueStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{090c4b72-8467-4d0a-9065-ac46b80a5522}')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.CompositionConditionalValue: ...
class ICompositionInteractionSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{043b2431-06e3-495a-ba54-409f0017fac0}')
class ICompositionInteractionSourceCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1b468e4b-a5bf-47d8-a547-3894155a158c}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def Add(self, value: Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_commethod(8)
    def Remove(self, value: Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class IInteractionSourceConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a78347e5-a9d1-4d02-985e-b930cd0b9da4}')
    @winrt_commethod(6)
    def get_PositionXSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(7)
    def put_PositionXSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(8)
    def get_PositionYSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(9)
    def put_PositionYSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(10)
    def get_ScaleSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(11)
    def put_ScaleSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
class IInteractionTracker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2a8e8cb1-1000-4416-8363-cc27fb877308}')
    @winrt_commethod(6)
    def get_InteractionSources(self) -> Windows.UI.Composition.Interactions.CompositionInteractionSourceCollection: ...
    @winrt_commethod(7)
    def get_IsPositionRoundingSuggested(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_MaxPosition(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def put_MaxPosition(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(10)
    def get_MaxScale(self) -> Single: ...
    @winrt_commethod(11)
    def put_MaxScale(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_MinPosition(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_MinPosition(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_MinScale(self) -> Single: ...
    @winrt_commethod(15)
    def put_MinScale(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_NaturalRestingPosition(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(17)
    def get_NaturalRestingScale(self) -> Single: ...
    @winrt_commethod(18)
    def get_Owner(self) -> Windows.UI.Composition.Interactions.IInteractionTrackerOwner: ...
    @winrt_commethod(19)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(20)
    def get_PositionInertiaDecayRate(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(21)
    def put_PositionInertiaDecayRate(self, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(22)
    def get_PositionVelocityInPixelsPerSecond(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(23)
    def get_Scale(self) -> Single: ...
    @winrt_commethod(24)
    def get_ScaleInertiaDecayRate(self) -> Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(25)
    def put_ScaleInertiaDecayRate(self, value: Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_commethod(26)
    def get_ScaleVelocityInPercentPerSecond(self) -> Single: ...
    @winrt_commethod(27)
    def AdjustPositionXIfGreaterThanThreshold(self, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_commethod(28)
    def AdjustPositionYIfGreaterThanThreshold(self, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_commethod(29)
    def ConfigurePositionXInertiaModifiers(self, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(30)
    def ConfigurePositionYInertiaModifiers(self, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(31)
    def ConfigureScaleInertiaModifiers(self, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(32)
    def TryUpdatePosition(self, value: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(33)
    def TryUpdatePositionBy(self, amount: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(34)
    def TryUpdatePositionWithAnimation(self, animation: Windows.UI.Composition.CompositionAnimation) -> Int32: ...
    @winrt_commethod(35)
    def TryUpdatePositionWithAdditionalVelocity(self, velocityInPixelsPerSecond: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(36)
    def TryUpdateScale(self, value: Single, centerPoint: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(37)
    def TryUpdateScaleWithAnimation(self, animation: Windows.UI.Composition.CompositionAnimation, centerPoint: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(38)
    def TryUpdateScaleWithAdditionalVelocity(self, velocityInPercentPerSecond: Single, centerPoint: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    InteractionSources = property(get_InteractionSources, None)
    IsPositionRoundingSuggested = property(get_IsPositionRoundingSuggested, None)
    MaxPosition = property(get_MaxPosition, put_MaxPosition)
    MaxScale = property(get_MaxScale, put_MaxScale)
    MinPosition = property(get_MinPosition, put_MinPosition)
    MinScale = property(get_MinScale, put_MinScale)
    NaturalRestingPosition = property(get_NaturalRestingPosition, None)
    NaturalRestingScale = property(get_NaturalRestingScale, None)
    Owner = property(get_Owner, None)
    Position = property(get_Position, None)
    PositionInertiaDecayRate = property(get_PositionInertiaDecayRate, put_PositionInertiaDecayRate)
    PositionVelocityInPixelsPerSecond = property(get_PositionVelocityInPixelsPerSecond, None)
    Scale = property(get_Scale, None)
    ScaleInertiaDecayRate = property(get_ScaleInertiaDecayRate, put_ScaleInertiaDecayRate)
    ScaleVelocityInPercentPerSecond = property(get_ScaleVelocityInPercentPerSecond, None)
class IInteractionTracker2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{25769a3e-ce6d-448c-8386-92620d240756}')
    @winrt_commethod(6)
    def ConfigureCenterPointXInertiaModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(7)
    def ConfigureCenterPointYInertiaModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
class IInteractionTracker3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e6c5d7a2-5c4b-42c6-84b7-f69441b18091}')
    @winrt_commethod(6)
    def ConfigureVector2PositionInertiaModifiers(self, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier]) -> Void: ...
class IInteractionTracker4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ebd222bc-04af-4ac7-847d-06ea36e80a16}')
    @winrt_commethod(6)
    def TryUpdatePositionWithOption(self, value: Windows.Foundation.Numerics.Vector3, option: Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_commethod(7)
    def TryUpdatePositionByWithOption(self, amount: Windows.Foundation.Numerics.Vector3, option: Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_commethod(8)
    def get_IsInertiaFromImpulse(self) -> Boolean: ...
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
class IInteractionTracker5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d3ef5da2-a254-40e4-88d5-44e4e16b5809}')
    @winrt_commethod(6)
    def TryUpdatePositionWithOption(self, value: Windows.Foundation.Numerics.Vector3, option: Windows.UI.Composition.Interactions.InteractionTrackerClampingOption, posUpdateOption: Windows.UI.Composition.Interactions.InteractionTrackerPositionUpdateOption) -> Int32: ...
class IInteractionTrackerCustomAnimationStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8d1c8cf1-d7b0-434c-a5d2-2d7611864834}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerCustomAnimationStateEnteredArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{47d579b7-0985-5e99-b024-2f32c380c1a4}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerIdleStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{50012faa-1510-4142-a1a5-019b09f8857b}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerIdleStateEnteredArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f2e771ed-b803-5137-9435-1c96e48721e9}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerInertiaModifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a0e2c920-26b4-4da2-8b61-5e683979bbe2}')
class IInteractionTrackerInertiaModifierFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{993818fe-c94e-4b86-87f3-922665ba46b9}')
class IInteractionTrackerInertiaMotion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{04922fdc-f154-4cb8-bf33-cc1ba611e6db}')
    @winrt_commethod(6)
    def get_Condition(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_Motion(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_Motion(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    Motion = property(get_Motion, put_Motion)
class IInteractionTrackerInertiaMotionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8cc83dd6-ba7b-431a-844b-6eac9130f99a}')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerInertiaMotion: ...
class IInteractionTrackerInertiaNaturalMotion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{70acdaae-27dc-48ed-a3c3-6d61c9a029d2}')
    @winrt_commethod(6)
    def get_Condition(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_NaturalMotion(self) -> Windows.UI.Composition.ScalarNaturalMotionAnimation: ...
    @winrt_commethod(9)
    def put_NaturalMotion(self, value: Windows.UI.Composition.ScalarNaturalMotionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class IInteractionTrackerInertiaNaturalMotionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cfda55b0-5e3e-4289-932d-ee5f50e74283}')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion: ...
class IInteractionTrackerInertiaRestingValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{86f7ec09-5096-4170-9cc8-df2fe101bb93}')
    @winrt_commethod(6)
    def get_Condition(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_RestingValue(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_RestingValue(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    RestingValue = property(get_RestingValue, put_RestingValue)
class IInteractionTrackerInertiaRestingValueStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{18ed4699-0745-4096-bcab-3a4e99569bcf}')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue: ...
class IInteractionTrackerInertiaStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{87108cf2-e7ff-4f7d-9ffd-d72f1e409b63}')
    @winrt_commethod(6)
    def get_ModifiedRestingPosition(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def get_ModifiedRestingScale(self) -> Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(8)
    def get_NaturalRestingPosition(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_NaturalRestingScale(self) -> Single: ...
    @winrt_commethod(10)
    def get_PositionVelocityInPixelsPerSecond(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def get_RequestId(self) -> Int32: ...
    @winrt_commethod(12)
    def get_ScaleVelocityInPercentPerSecond(self) -> Single: ...
    ModifiedRestingPosition = property(get_ModifiedRestingPosition, None)
    ModifiedRestingScale = property(get_ModifiedRestingScale, None)
    NaturalRestingPosition = property(get_NaturalRestingPosition, None)
    NaturalRestingScale = property(get_NaturalRestingScale, None)
    PositionVelocityInPixelsPerSecond = property(get_PositionVelocityInPixelsPerSecond, None)
    RequestId = property(get_RequestId, None)
    ScaleVelocityInPercentPerSecond = property(get_ScaleVelocityInPercentPerSecond, None)
class IInteractionTrackerInertiaStateEnteredArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b1eb32f6-c26c-41f6-a189-fabc22b323cc}')
    @winrt_commethod(6)
    def get_IsInertiaFromImpulse(self) -> Boolean: ...
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
class IInteractionTrackerInertiaStateEnteredArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{48ac1c2f-47bd-59af-a58c-79bd2eb9ef71}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerInteractingStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a7263939-a17b-4011-99fd-b5c24f143748}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerInteractingStateEnteredArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{509652d6-d488-59cd-819f-f52310295b11}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerOwner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{db2e8af3-4deb-4e53-b29c-b06c9f96d651}')
    @winrt_commethod(6)
    def CustomAnimationStateEntered(self, sender: Windows.UI.Composition.Interactions.InteractionTracker, args: Windows.UI.Composition.Interactions.InteractionTrackerCustomAnimationStateEnteredArgs) -> Void: ...
    @winrt_commethod(7)
    def IdleStateEntered(self, sender: Windows.UI.Composition.Interactions.InteractionTracker, args: Windows.UI.Composition.Interactions.InteractionTrackerIdleStateEnteredArgs) -> Void: ...
    @winrt_commethod(8)
    def InertiaStateEntered(self, sender: Windows.UI.Composition.Interactions.InteractionTracker, args: Windows.UI.Composition.Interactions.InteractionTrackerInertiaStateEnteredArgs) -> Void: ...
    @winrt_commethod(9)
    def InteractingStateEntered(self, sender: Windows.UI.Composition.Interactions.InteractionTracker, args: Windows.UI.Composition.Interactions.InteractionTrackerInteractingStateEnteredArgs) -> Void: ...
    @winrt_commethod(10)
    def RequestIgnored(self, sender: Windows.UI.Composition.Interactions.InteractionTracker, args: Windows.UI.Composition.Interactions.InteractionTrackerRequestIgnoredArgs) -> Void: ...
    @winrt_commethod(11)
    def ValuesChanged(self, sender: Windows.UI.Composition.Interactions.InteractionTracker, args: Windows.UI.Composition.Interactions.InteractionTrackerValuesChangedArgs) -> Void: ...
class IInteractionTrackerRequestIgnoredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{80dd82f1-ce25-488f-91dd-cb6455ccff2e}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bba5d7b7-6590-4498-8d6c-eb62b514c92a}')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTracker: ...
    @winrt_commethod(7)
    def CreateWithOwner(self, compositor: Windows.UI.Composition.Compositor, owner: Windows.UI.Composition.Interactions.IInteractionTrackerOwner) -> Windows.UI.Composition.Interactions.InteractionTracker: ...
class IInteractionTrackerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{35e53720-46b7-5cb0-b505-f3d6884a6163}')
    @winrt_commethod(6)
    def SetBindingMode(self, boundTracker1: Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: Windows.UI.Composition.Interactions.InteractionTracker, axisMode: Windows.UI.Composition.Interactions.InteractionBindingAxisModes) -> Void: ...
    @winrt_commethod(7)
    def GetBindingMode(self, boundTracker1: Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: Windows.UI.Composition.Interactions.InteractionTracker) -> Windows.UI.Composition.Interactions.InteractionBindingAxisModes: ...
class IInteractionTrackerValuesChangedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cf1578ef-d3df-4501-b9e6-f02fb22f73d0}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_RequestId(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Scale(self) -> Single: ...
    Position = property(get_Position, None)
    RequestId = property(get_RequestId, None)
    Scale = property(get_Scale, None)
class IInteractionTrackerVector2InertiaModifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{87e08ab0-3086-4853-a4b7-77882ad5d7e3}')
class IInteractionTrackerVector2InertiaModifierFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7401d6c4-6c6d-48df-bc3e-171e227e7d7f}')
class IInteractionTrackerVector2InertiaNaturalMotion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5f17695c-162d-4c07-9400-c282b28276ca}')
    @winrt_commethod(6)
    def get_Condition(self) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_NaturalMotion(self) -> Windows.UI.Composition.Vector2NaturalMotionAnimation: ...
    @winrt_commethod(9)
    def put_NaturalMotion(self, value: Windows.UI.Composition.Vector2NaturalMotionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class IInteractionTrackerVector2InertiaNaturalMotionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{82001a48-09c0-434f-8189-141c66df362f}')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion: ...
class IVisualInteractionSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ca0e8a86-d8d6-4111-b088-70347bd2b0ed}')
    @winrt_commethod(6)
    def get_IsPositionXRailsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPositionXRailsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsPositionYRailsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsPositionYRailsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ManipulationRedirectionMode(self) -> Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode: ...
    @winrt_commethod(11)
    def put_ManipulationRedirectionMode(self, value: Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(12)
    def get_PositionXChainingMode(self) -> Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(13)
    def put_PositionXChainingMode(self, value: Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(14)
    def get_PositionXSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(15)
    def put_PositionXSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(16)
    def get_PositionYChainingMode(self) -> Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(17)
    def put_PositionYChainingMode(self, value: Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(18)
    def get_PositionYSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(19)
    def put_PositionYSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(20)
    def get_ScaleChainingMode(self) -> Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(21)
    def put_ScaleChainingMode(self, value: Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(22)
    def get_ScaleSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(23)
    def put_ScaleSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(24)
    def get_Source(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(25)
    def TryRedirectForManipulation(self, pointerPoint: Windows.UI.Input.PointerPoint) -> Void: ...
    IsPositionXRailsEnabled = property(get_IsPositionXRailsEnabled, put_IsPositionXRailsEnabled)
    IsPositionYRailsEnabled = property(get_IsPositionYRailsEnabled, put_IsPositionYRailsEnabled)
    ManipulationRedirectionMode = property(get_ManipulationRedirectionMode, put_ManipulationRedirectionMode)
    PositionXChainingMode = property(get_PositionXChainingMode, put_PositionXChainingMode)
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYChainingMode = property(get_PositionYChainingMode, put_PositionYChainingMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    ScaleChainingMode = property(get_ScaleChainingMode, put_ScaleChainingMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
    Source = property(get_Source, None)
class IVisualInteractionSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{aa914893-a73c-414d-80d0-249bad2fbd93}')
    @winrt_commethod(6)
    def get_DeltaPosition(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_DeltaScale(self) -> Single: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_PositionVelocity(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(10)
    def get_Scale(self) -> Single: ...
    @winrt_commethod(11)
    def get_ScaleVelocity(self) -> Single: ...
    @winrt_commethod(12)
    def ConfigureCenterPointXModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(13)
    def ConfigureCenterPointYModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(14)
    def ConfigureDeltaPositionXModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(15)
    def ConfigureDeltaPositionYModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(16)
    def ConfigureDeltaScaleModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    DeltaPosition = property(get_DeltaPosition, None)
    DeltaScale = property(get_DeltaScale, None)
    Position = property(get_Position, None)
    PositionVelocity = property(get_PositionVelocity, None)
    Scale = property(get_Scale, None)
    ScaleVelocity = property(get_ScaleVelocity, None)
class IVisualInteractionSource3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d941ef2a-0d5c-4057-92d7-c9711533204f}')
    @winrt_commethod(6)
    def get_PointerWheelConfig(self) -> Windows.UI.Composition.Interactions.InteractionSourceConfiguration: ...
    PointerWheelConfig = property(get_PointerWheelConfig, None)
class IVisualInteractionSourceObjectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b2ca917c-e98a-41f2-b3c9-891c9266c8f6}')
class IVisualInteractionSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{369965e1-8645-4f75-ba00-6479cd10c8e6}')
    @winrt_commethod(6)
    def Create(self, source: Windows.UI.Composition.Visual) -> Windows.UI.Composition.Interactions.VisualInteractionSource: ...
class IVisualInteractionSourceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a979c032-5764-55e0-bc1f-0778786dcfde}')
    @winrt_commethod(6)
    def CreateFromIVisualElement(self, source: Windows.UI.Composition.IVisualElement) -> Windows.UI.Composition.Interactions.VisualInteractionSource: ...
InteractionBindingAxisModes = UInt32
InteractionBindingAxisModes_None: InteractionBindingAxisModes = 0
InteractionBindingAxisModes_PositionX: InteractionBindingAxisModes = 1
InteractionBindingAxisModes_PositionY: InteractionBindingAxisModes = 2
InteractionBindingAxisModes_Scale: InteractionBindingAxisModes = 4
InteractionChainingMode = Int32
InteractionChainingMode_Auto: InteractionChainingMode = 0
InteractionChainingMode_Always: InteractionChainingMode = 1
InteractionChainingMode_Never: InteractionChainingMode = 2
class InteractionSourceConfiguration(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionSourceConfiguration'
    @winrt_mixinmethod
    def get_PositionXSourceMode(self: Windows.UI.Composition.Interactions.IInteractionSourceConfiguration) -> Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_PositionXSourceMode(self: Windows.UI.Composition.Interactions.IInteractionSourceConfiguration, value: Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionYSourceMode(self: Windows.UI.Composition.Interactions.IInteractionSourceConfiguration) -> Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_PositionYSourceMode(self: Windows.UI.Composition.Interactions.IInteractionSourceConfiguration, value: Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleSourceMode(self: Windows.UI.Composition.Interactions.IInteractionSourceConfiguration) -> Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_ScaleSourceMode(self: Windows.UI.Composition.Interactions.IInteractionSourceConfiguration, value: Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
InteractionSourceMode = Int32
InteractionSourceMode_Disabled: InteractionSourceMode = 0
InteractionSourceMode_EnabledWithInertia: InteractionSourceMode = 1
InteractionSourceMode_EnabledWithoutInertia: InteractionSourceMode = 2
InteractionSourceRedirectionMode = Int32
InteractionSourceRedirectionMode_Disabled: InteractionSourceRedirectionMode = 0
InteractionSourceRedirectionMode_Enabled: InteractionSourceRedirectionMode = 1
class InteractionTracker(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTracker'
    @winrt_mixinmethod
    def get_InteractionSources(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.UI.Composition.Interactions.CompositionInteractionSourceCollection: ...
    @winrt_mixinmethod
    def get_IsPositionRoundingSuggested(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPosition(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_MaxPosition(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_MaxScale(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def put_MaxScale(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinPosition(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_MinPosition(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_MinScale(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def put_MinScale(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalRestingPosition(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_NaturalRestingScale(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def get_Owner(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.UI.Composition.Interactions.IInteractionTrackerOwner: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_PositionInertiaDecayRate(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def put_PositionInertiaDecayRate(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def get_PositionVelocityInPixelsPerSecond(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def get_ScaleInertiaDecayRate(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_ScaleInertiaDecayRate(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleVelocityInPercentPerSecond(self: Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def AdjustPositionXIfGreaterThanThreshold(self: Windows.UI.Composition.Interactions.IInteractionTracker, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_mixinmethod
    def AdjustPositionYIfGreaterThanThreshold(self: Windows.UI.Composition.Interactions.IInteractionTracker, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_mixinmethod
    def ConfigurePositionXInertiaModifiers(self: Windows.UI.Composition.Interactions.IInteractionTracker, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def ConfigurePositionYInertiaModifiers(self: Windows.UI.Composition.Interactions.IInteractionTracker, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureScaleInertiaModifiers(self: Windows.UI.Composition.Interactions.IInteractionTracker, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def TryUpdatePosition(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionBy(self: Windows.UI.Composition.Interactions.IInteractionTracker, amount: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithAnimation(self: Windows.UI.Composition.Interactions.IInteractionTracker, animation: Windows.UI.Composition.CompositionAnimation) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithAdditionalVelocity(self: Windows.UI.Composition.Interactions.IInteractionTracker, velocityInPixelsPerSecond: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScale(self: Windows.UI.Composition.Interactions.IInteractionTracker, value: Single, centerPoint: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScaleWithAnimation(self: Windows.UI.Composition.Interactions.IInteractionTracker, animation: Windows.UI.Composition.CompositionAnimation, centerPoint: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScaleWithAdditionalVelocity(self: Windows.UI.Composition.Interactions.IInteractionTracker, velocityInPercentPerSecond: Single, centerPoint: Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def ConfigureCenterPointXInertiaModifiers(self: Windows.UI.Composition.Interactions.IInteractionTracker2, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureCenterPointYInertiaModifiers(self: Windows.UI.Composition.Interactions.IInteractionTracker2, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureVector2PositionInertiaModifiers(self: Windows.UI.Composition.Interactions.IInteractionTracker3, modifiers: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithOption(self: Windows.UI.Composition.Interactions.IInteractionTracker4, value: Windows.Foundation.Numerics.Vector3, option: Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionByWithOption(self: Windows.UI.Composition.Interactions.IInteractionTracker4, amount: Windows.Foundation.Numerics.Vector3, option: Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_mixinmethod
    def get_IsInertiaFromImpulse(self: Windows.UI.Composition.Interactions.IInteractionTracker4) -> Boolean: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithOption(self: Windows.UI.Composition.Interactions.IInteractionTracker4, value: Windows.Foundation.Numerics.Vector3, option: Windows.UI.Composition.Interactions.InteractionTrackerClampingOption, posUpdateOption: Windows.UI.Composition.Interactions.InteractionTrackerPositionUpdateOption) -> Int32: ...
    @winrt_classmethod
    def SetBindingMode(cls: Windows.UI.Composition.Interactions.IInteractionTrackerStatics2, boundTracker1: Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: Windows.UI.Composition.Interactions.InteractionTracker, axisMode: Windows.UI.Composition.Interactions.InteractionBindingAxisModes) -> Void: ...
    @winrt_classmethod
    def GetBindingMode(cls: Windows.UI.Composition.Interactions.IInteractionTrackerStatics2, boundTracker1: Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: Windows.UI.Composition.Interactions.InteractionTracker) -> Windows.UI.Composition.Interactions.InteractionBindingAxisModes: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Interactions.IInteractionTrackerStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTracker: ...
    @winrt_classmethod
    def CreateWithOwner(cls: Windows.UI.Composition.Interactions.IInteractionTrackerStatics, compositor: Windows.UI.Composition.Compositor, owner: Windows.UI.Composition.Interactions.IInteractionTrackerOwner) -> Windows.UI.Composition.Interactions.InteractionTracker: ...
    InteractionSources = property(get_InteractionSources, None)
    IsPositionRoundingSuggested = property(get_IsPositionRoundingSuggested, None)
    MaxPosition = property(get_MaxPosition, put_MaxPosition)
    MaxScale = property(get_MaxScale, put_MaxScale)
    MinPosition = property(get_MinPosition, put_MinPosition)
    MinScale = property(get_MinScale, put_MinScale)
    NaturalRestingPosition = property(get_NaturalRestingPosition, None)
    NaturalRestingScale = property(get_NaturalRestingScale, None)
    Owner = property(get_Owner, None)
    Position = property(get_Position, None)
    PositionInertiaDecayRate = property(get_PositionInertiaDecayRate, put_PositionInertiaDecayRate)
    PositionVelocityInPixelsPerSecond = property(get_PositionVelocityInPixelsPerSecond, None)
    Scale = property(get_Scale, None)
    ScaleInertiaDecayRate = property(get_ScaleInertiaDecayRate, put_ScaleInertiaDecayRate)
    ScaleVelocityInPercentPerSecond = property(get_ScaleVelocityInPercentPerSecond, None)
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
InteractionTrackerClampingOption = Int32
InteractionTrackerClampingOption_Auto: InteractionTrackerClampingOption = 0
InteractionTrackerClampingOption_Disabled: InteractionTrackerClampingOption = 1
class InteractionTrackerCustomAnimationStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerCustomAnimationStateEnteredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: Windows.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: Windows.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs2) -> Boolean: ...
    RequestId = property(get_RequestId, None)
    IsFromBinding = property(get_IsFromBinding, None)
class InteractionTrackerIdleStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerIdleStateEnteredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: Windows.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: Windows.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs2) -> Boolean: ...
    RequestId = property(get_RequestId, None)
    IsFromBinding = property(get_IsFromBinding, None)
class InteractionTrackerInertiaModifier(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
class InteractionTrackerInertiaMotion(ComPtr):
    extends: Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaMotion'
    @winrt_mixinmethod
    def get_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Motion(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Motion(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotionStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerInertiaMotion: ...
    Condition = property(get_Condition, put_Condition)
    Motion = property(get_Motion, put_Motion)
class InteractionTrackerInertiaNaturalMotion(ComPtr):
    extends: Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion'
    @winrt_mixinmethod
    def get_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalMotion(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion) -> Windows.UI.Composition.ScalarNaturalMotionAnimation: ...
    @winrt_mixinmethod
    def put_NaturalMotion(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion, value: Windows.UI.Composition.ScalarNaturalMotionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotionStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class InteractionTrackerInertiaRestingValue(ComPtr):
    extends: Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue'
    @winrt_mixinmethod
    def get_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_RestingValue(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_RestingValue(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValueStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue: ...
    Condition = property(get_Condition, put_Condition)
    RestingValue = property(get_RestingValue, put_RestingValue)
class InteractionTrackerInertiaStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaStateEnteredArgs'
    @winrt_mixinmethod
    def get_ModifiedRestingPosition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_ModifiedRestingScale(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_NaturalRestingPosition(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_NaturalRestingScale(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Single: ...
    @winrt_mixinmethod
    def get_PositionVelocityInPixelsPerSecond(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RequestId(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ScaleVelocityInPercentPerSecond(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Single: ...
    @winrt_mixinmethod
    def get_IsInertiaFromImpulse(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs3) -> Boolean: ...
    ModifiedRestingPosition = property(get_ModifiedRestingPosition, None)
    ModifiedRestingScale = property(get_ModifiedRestingScale, None)
    NaturalRestingPosition = property(get_NaturalRestingPosition, None)
    NaturalRestingScale = property(get_NaturalRestingScale, None)
    PositionVelocityInPixelsPerSecond = property(get_PositionVelocityInPixelsPerSecond, None)
    RequestId = property(get_RequestId, None)
    ScaleVelocityInPercentPerSecond = property(get_ScaleVelocityInPercentPerSecond, None)
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
    IsFromBinding = property(get_IsFromBinding, None)
class InteractionTrackerInteractingStateEnteredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInteractingStateEnteredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: Windows.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: Windows.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs2) -> Boolean: ...
    RequestId = property(get_RequestId, None)
    IsFromBinding = property(get_IsFromBinding, None)
InteractionTrackerPositionUpdateOption = Int32
InteractionTrackerPositionUpdateOption_Default: InteractionTrackerPositionUpdateOption = 0
InteractionTrackerPositionUpdateOption_AllowActiveCustomScaleAnimation: InteractionTrackerPositionUpdateOption = 1
class InteractionTrackerRequestIgnoredArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerRequestIgnoredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: Windows.UI.Composition.Interactions.IInteractionTrackerRequestIgnoredArgs) -> Int32: ...
    RequestId = property(get_RequestId, None)
class InteractionTrackerValuesChangedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerValuesChangedArgs'
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RequestId(self: Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> Single: ...
    Position = property(get_Position, None)
    RequestId = property(get_RequestId, None)
    Scale = property(get_Scale, None)
class InteractionTrackerVector2InertiaModifier(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
class InteractionTrackerVector2InertiaNaturalMotion(ComPtr):
    extends: Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion'
    @winrt_mixinmethod
    def get_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion) -> Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion, value: Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalMotion(self: Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion) -> Windows.UI.Composition.Vector2NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def put_NaturalMotion(self: Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion, value: Windows.UI.Composition.Vector2NaturalMotionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotionStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class VisualInteractionSource(ComPtr):
    extends: Windows.UI.Composition.CompositionObject
    @winrt_commethod(40)
    def get_IsPositionXRailsEnabled(self) -> Boolean: ...
    @winrt_commethod(41)
    def put_IsPositionXRailsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(42)
    def get_IsPositionYRailsEnabled(self) -> Boolean: ...
    @winrt_commethod(43)
    def put_IsPositionYRailsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(44)
    def get_ManipulationRedirectionMode(self) -> Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode: ...
    @winrt_commethod(45)
    def put_ManipulationRedirectionMode(self, value: Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(46)
    def get_PositionXChainingMode(self) -> Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(47)
    def put_PositionXChainingMode(self, value: Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(48)
    def get_PositionXSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(49)
    def put_PositionXSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(50)
    def get_PositionYChainingMode(self) -> Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(51)
    def put_PositionYChainingMode(self, value: Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(52)
    def get_PositionYSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(53)
    def put_PositionYSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(54)
    def get_ScaleChainingMode(self) -> Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(55)
    def put_ScaleChainingMode(self, value: Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(56)
    def get_ScaleSourceMode(self) -> Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(57)
    def put_ScaleSourceMode(self, value: Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(58)
    def get_Source(self) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(59)
    def TryRedirectForManipulation(self, pointerPoint: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(60)
    def get_DeltaPosition(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(61)
    def get_DeltaScale(self) -> Single: ...
    @winrt_commethod(62)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(63)
    def get_PositionVelocity(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(64)
    def get_Scale(self) -> Single: ...
    @winrt_commethod(65)
    def get_ScaleVelocity(self) -> Single: ...
    @winrt_commethod(66)
    def ConfigureCenterPointXModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(67)
    def ConfigureCenterPointYModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(68)
    def ConfigureDeltaPositionXModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(69)
    def ConfigureDeltaPositionYModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(70)
    def ConfigureDeltaScaleModifiers(self, conditionalValues: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(71)
    def get_PointerWheelConfig(self) -> Windows.UI.Composition.Interactions.InteractionSourceConfiguration: ...
    @winrt_classmethod
    def CreateFromIVisualElement(cls: Windows.UI.Composition.Interactions.IVisualInteractionSourceStatics2, source: Windows.UI.Composition.IVisualElement) -> Windows.UI.Composition.Interactions.VisualInteractionSource: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Interactions.IVisualInteractionSourceStatics, source: Windows.UI.Composition.Visual) -> Windows.UI.Composition.Interactions.VisualInteractionSource: ...
    IsPositionXRailsEnabled = property(get_IsPositionXRailsEnabled, put_IsPositionXRailsEnabled)
    IsPositionYRailsEnabled = property(get_IsPositionYRailsEnabled, put_IsPositionYRailsEnabled)
    ManipulationRedirectionMode = property(get_ManipulationRedirectionMode, put_ManipulationRedirectionMode)
    PositionXChainingMode = property(get_PositionXChainingMode, put_PositionXChainingMode)
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYChainingMode = property(get_PositionYChainingMode, put_PositionYChainingMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    ScaleChainingMode = property(get_ScaleChainingMode, put_ScaleChainingMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
    Source = property(get_Source, None)
    DeltaPosition = property(get_DeltaPosition, None)
    DeltaScale = property(get_DeltaScale, None)
    Position = property(get_Position, None)
    PositionVelocity = property(get_PositionVelocity, None)
    Scale = property(get_Scale, None)
    ScaleVelocity = property(get_ScaleVelocity, None)
    PointerWheelConfig = property(get_PointerWheelConfig, None)
VisualInteractionSourceRedirectionMode = Int32
VisualInteractionSourceRedirectionMode_Off: VisualInteractionSourceRedirectionMode = 0
VisualInteractionSourceRedirectionMode_CapableTouchpadOnly: VisualInteractionSourceRedirectionMode = 1
VisualInteractionSourceRedirectionMode_PointerWheelOnly: VisualInteractionSourceRedirectionMode = 2
VisualInteractionSourceRedirectionMode_CapableTouchpadAndPointerWheel: VisualInteractionSourceRedirectionMode = 3
make_head(_module, 'CompositionConditionalValue')
make_head(_module, 'CompositionInteractionSourceCollection')
make_head(_module, 'ICompositionConditionalValue')
make_head(_module, 'ICompositionConditionalValueStatics')
make_head(_module, 'ICompositionInteractionSource')
make_head(_module, 'ICompositionInteractionSourceCollection')
make_head(_module, 'IInteractionSourceConfiguration')
make_head(_module, 'IInteractionTracker')
make_head(_module, 'IInteractionTracker2')
make_head(_module, 'IInteractionTracker3')
make_head(_module, 'IInteractionTracker4')
make_head(_module, 'IInteractionTracker5')
make_head(_module, 'IInteractionTrackerCustomAnimationStateEnteredArgs')
make_head(_module, 'IInteractionTrackerCustomAnimationStateEnteredArgs2')
make_head(_module, 'IInteractionTrackerIdleStateEnteredArgs')
make_head(_module, 'IInteractionTrackerIdleStateEnteredArgs2')
make_head(_module, 'IInteractionTrackerInertiaModifier')
make_head(_module, 'IInteractionTrackerInertiaModifierFactory')
make_head(_module, 'IInteractionTrackerInertiaMotion')
make_head(_module, 'IInteractionTrackerInertiaMotionStatics')
make_head(_module, 'IInteractionTrackerInertiaNaturalMotion')
make_head(_module, 'IInteractionTrackerInertiaNaturalMotionStatics')
make_head(_module, 'IInteractionTrackerInertiaRestingValue')
make_head(_module, 'IInteractionTrackerInertiaRestingValueStatics')
make_head(_module, 'IInteractionTrackerInertiaStateEnteredArgs')
make_head(_module, 'IInteractionTrackerInertiaStateEnteredArgs2')
make_head(_module, 'IInteractionTrackerInertiaStateEnteredArgs3')
make_head(_module, 'IInteractionTrackerInteractingStateEnteredArgs')
make_head(_module, 'IInteractionTrackerInteractingStateEnteredArgs2')
make_head(_module, 'IInteractionTrackerOwner')
make_head(_module, 'IInteractionTrackerRequestIgnoredArgs')
make_head(_module, 'IInteractionTrackerStatics')
make_head(_module, 'IInteractionTrackerStatics2')
make_head(_module, 'IInteractionTrackerValuesChangedArgs')
make_head(_module, 'IInteractionTrackerVector2InertiaModifier')
make_head(_module, 'IInteractionTrackerVector2InertiaModifierFactory')
make_head(_module, 'IInteractionTrackerVector2InertiaNaturalMotion')
make_head(_module, 'IInteractionTrackerVector2InertiaNaturalMotionStatics')
make_head(_module, 'IVisualInteractionSource')
make_head(_module, 'IVisualInteractionSource2')
make_head(_module, 'IVisualInteractionSource3')
make_head(_module, 'IVisualInteractionSourceObjectFactory')
make_head(_module, 'IVisualInteractionSourceStatics')
make_head(_module, 'IVisualInteractionSourceStatics2')
make_head(_module, 'InteractionSourceConfiguration')
make_head(_module, 'InteractionTracker')
make_head(_module, 'InteractionTrackerCustomAnimationStateEnteredArgs')
make_head(_module, 'InteractionTrackerIdleStateEnteredArgs')
make_head(_module, 'InteractionTrackerInertiaModifier')
make_head(_module, 'InteractionTrackerInertiaMotion')
make_head(_module, 'InteractionTrackerInertiaNaturalMotion')
make_head(_module, 'InteractionTrackerInertiaRestingValue')
make_head(_module, 'InteractionTrackerInertiaStateEnteredArgs')
make_head(_module, 'InteractionTrackerInteractingStateEnteredArgs')
make_head(_module, 'InteractionTrackerRequestIgnoredArgs')
make_head(_module, 'InteractionTrackerValuesChangedArgs')
make_head(_module, 'InteractionTrackerVector2InertiaModifier')
make_head(_module, 'InteractionTrackerVector2InertiaNaturalMotion')
make_head(_module, 'VisualInteractionSource')
