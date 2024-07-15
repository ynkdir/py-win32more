from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Composition.Interactions
import win32more.Windows.UI.Input
import win32more.Windows.Win32.System.WinRT
class CompositionConditionalValue(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.Interactions.ICompositionConditionalValue
    _classid_ = 'Windows.UI.Composition.Interactions.CompositionConditionalValue'
    @winrt_mixinmethod
    def get_Condition(self: win32more.Windows.UI.Composition.Interactions.ICompositionConditionalValue) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Windows.UI.Composition.Interactions.ICompositionConditionalValue, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Composition.Interactions.ICompositionConditionalValue) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.UI.Composition.Interactions.ICompositionConditionalValue, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Interactions.ICompositionConditionalValueStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue: ...
    Condition = property(get_Condition, put_Condition)
    Value = property(get_Value, put_Value)
class CompositionInteractionSourceCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    implements: Tuple[IterableProtocol[win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSource]]
    default_interface: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection
    _classid_ = 'Windows.UI.Composition.Interactions.CompositionInteractionSourceCollection'
    @winrt_mixinmethod
    def get_Count(self: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection) -> Int32: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection, value: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection, value: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSource]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSource]: ...
    Count = property(get_Count, None)
class ICompositionConditionalValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.ICompositionConditionalValue'
    _iid_ = Guid('{43250538-eb73-4561-a71d-1a43eaeb7a9b}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_Value(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    Value = property(get_Value, put_Value)
class ICompositionConditionalValueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.ICompositionConditionalValueStatics'
    _iid_ = Guid('{090c4b72-8467-4d0a-9065-ac46b80a5522}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue: ...
class ICompositionInteractionSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.ICompositionInteractionSource'
    _iid_ = Guid('{043b2431-06e3-495a-ba54-409f0017fac0}')
class ICompositionInteractionSourceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.ICompositionInteractionSourceCollection'
    _iid_ = Guid('{1b468e4b-a5bf-47d8-a547-3894155a158c}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def Add(self, value: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_commethod(8)
    def Remove(self, value: win32more.Windows.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class IInteractionSourceConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionSourceConfiguration'
    _iid_ = Guid('{a78347e5-a9d1-4d02-985e-b930cd0b9da4}')
    @winrt_commethod(6)
    def get_PositionXSourceMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(7)
    def put_PositionXSourceMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(8)
    def get_PositionYSourceMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(9)
    def put_PositionYSourceMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(10)
    def get_ScaleSourceMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(11)
    def put_ScaleSourceMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
class IInteractionTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTracker'
    _iid_ = Guid('{2a8e8cb1-1000-4416-8363-cc27fb877308}')
    @winrt_commethod(6)
    def get_InteractionSources(self) -> win32more.Windows.UI.Composition.Interactions.CompositionInteractionSourceCollection: ...
    @winrt_commethod(7)
    def get_IsPositionRoundingSuggested(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_MaxPosition(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def put_MaxPosition(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(10)
    def get_MaxScale(self) -> Single: ...
    @winrt_commethod(11)
    def put_MaxScale(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_MinPosition(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_MinPosition(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_MinScale(self) -> Single: ...
    @winrt_commethod(15)
    def put_MinScale(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_NaturalRestingPosition(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(17)
    def get_NaturalRestingScale(self) -> Single: ...
    @winrt_commethod(18)
    def get_Owner(self) -> win32more.Windows.UI.Composition.Interactions.IInteractionTrackerOwner: ...
    @winrt_commethod(19)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(20)
    def get_PositionInertiaDecayRate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(21)
    def put_PositionInertiaDecayRate(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(22)
    def get_PositionVelocityInPixelsPerSecond(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(23)
    def get_Scale(self) -> Single: ...
    @winrt_commethod(24)
    def get_ScaleInertiaDecayRate(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(25)
    def put_ScaleInertiaDecayRate(self, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_commethod(26)
    def get_ScaleVelocityInPercentPerSecond(self) -> Single: ...
    @winrt_commethod(27)
    def AdjustPositionXIfGreaterThanThreshold(self, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_commethod(28)
    def AdjustPositionYIfGreaterThanThreshold(self, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_commethod(29)
    def ConfigurePositionXInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(30)
    def ConfigurePositionYInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(31)
    def ConfigureScaleInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(32)
    def TryUpdatePosition(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(33)
    def TryUpdatePositionBy(self, amount: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(34)
    def TryUpdatePositionWithAnimation(self, animation: win32more.Windows.UI.Composition.CompositionAnimation) -> Int32: ...
    @winrt_commethod(35)
    def TryUpdatePositionWithAdditionalVelocity(self, velocityInPixelsPerSecond: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(36)
    def TryUpdateScale(self, value: Single, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(37)
    def TryUpdateScaleWithAnimation(self, animation: win32more.Windows.UI.Composition.CompositionAnimation, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(38)
    def TryUpdateScaleWithAdditionalVelocity(self, velocityInPercentPerSecond: Single, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTracker2'
    _iid_ = Guid('{25769a3e-ce6d-448c-8386-92620d240756}')
    @winrt_commethod(6)
    def ConfigureCenterPointXInertiaModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(7)
    def ConfigureCenterPointYInertiaModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
class IInteractionTracker3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTracker3'
    _iid_ = Guid('{e6c5d7a2-5c4b-42c6-84b7-f69441b18091}')
    @winrt_commethod(6)
    def ConfigureVector2PositionInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier]) -> Void: ...
class IInteractionTracker4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTracker4'
    _iid_ = Guid('{ebd222bc-04af-4ac7-847d-06ea36e80a16}')
    @winrt_commethod(6)
    def TryUpdatePositionWithOption(self, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_commethod(7)
    def TryUpdatePositionByWithOption(self, amount: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_commethod(8)
    def get_IsInertiaFromImpulse(self) -> Boolean: ...
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
class IInteractionTracker5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTracker5'
    _iid_ = Guid('{d3ef5da2-a254-40e4-88d5-44e4e16b5809}')
    @winrt_commethod(6)
    def TryUpdatePositionWithOption(self, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Windows.UI.Composition.Interactions.InteractionTrackerClampingOption, posUpdateOption: win32more.Windows.UI.Composition.Interactions.InteractionTrackerPositionUpdateOption) -> Int32: ...
class IInteractionTrackerCustomAnimationStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs'
    _iid_ = Guid('{8d1c8cf1-d7b0-434c-a5d2-2d7611864834}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerCustomAnimationStateEnteredArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs2'
    _iid_ = Guid('{47d579b7-0985-5e99-b024-2f32c380c1a4}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerIdleStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs'
    _iid_ = Guid('{50012faa-1510-4142-a1a5-019b09f8857b}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerIdleStateEnteredArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs2'
    _iid_ = Guid('{f2e771ed-b803-5137-9435-1c96e48721e9}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerInertiaModifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaModifier'
    _iid_ = Guid('{a0e2c920-26b4-4da2-8b61-5e683979bbe2}')
class IInteractionTrackerInertiaModifierFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaModifierFactory'
    _iid_ = Guid('{993818fe-c94e-4b86-87f3-922665ba46b9}')
class IInteractionTrackerInertiaMotion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion'
    _iid_ = Guid('{04922fdc-f154-4cb8-bf33-cc1ba611e6db}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_Motion(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_Motion(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    Motion = property(get_Motion, put_Motion)
class IInteractionTrackerInertiaMotionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotionStatics'
    _iid_ = Guid('{8cc83dd6-ba7b-431a-844b-6eac9130f99a}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaMotion: ...
class IInteractionTrackerInertiaNaturalMotion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion'
    _iid_ = Guid('{70acdaae-27dc-48ed-a3c3-6d61c9a029d2}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_NaturalMotion(self) -> win32more.Windows.UI.Composition.ScalarNaturalMotionAnimation: ...
    @winrt_commethod(9)
    def put_NaturalMotion(self, value: win32more.Windows.UI.Composition.ScalarNaturalMotionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class IInteractionTrackerInertiaNaturalMotionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotionStatics'
    _iid_ = Guid('{cfda55b0-5e3e-4289-932d-ee5f50e74283}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion: ...
class IInteractionTrackerInertiaRestingValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue'
    _iid_ = Guid('{86f7ec09-5096-4170-9cc8-df2fe101bb93}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_RestingValue(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_RestingValue(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    RestingValue = property(get_RestingValue, put_RestingValue)
class IInteractionTrackerInertiaRestingValueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValueStatics'
    _iid_ = Guid('{18ed4699-0745-4096-bcab-3a4e99569bcf}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue: ...
class IInteractionTrackerInertiaStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs'
    _iid_ = Guid('{87108cf2-e7ff-4f7d-9ffd-d72f1e409b63}')
    @winrt_commethod(6)
    def get_ModifiedRestingPosition(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def get_ModifiedRestingScale(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(8)
    def get_NaturalRestingPosition(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_NaturalRestingScale(self) -> Single: ...
    @winrt_commethod(10)
    def get_PositionVelocityInPixelsPerSecond(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs2'
    _iid_ = Guid('{b1eb32f6-c26c-41f6-a189-fabc22b323cc}')
    @winrt_commethod(6)
    def get_IsInertiaFromImpulse(self) -> Boolean: ...
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
class IInteractionTrackerInertiaStateEnteredArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs3'
    _iid_ = Guid('{48ac1c2f-47bd-59af-a58c-79bd2eb9ef71}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerInteractingStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs'
    _iid_ = Guid('{a7263939-a17b-4011-99fd-b5c24f143748}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerInteractingStateEnteredArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs2'
    _iid_ = Guid('{509652d6-d488-59cd-819f-f52310295b11}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerOwner(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerOwner'
    _iid_ = Guid('{db2e8af3-4deb-4e53-b29c-b06c9f96d651}')
    @winrt_commethod(6)
    def CustomAnimationStateEntered(self, sender: win32more.Windows.UI.Composition.Interactions.InteractionTracker, args: win32more.Windows.UI.Composition.Interactions.InteractionTrackerCustomAnimationStateEnteredArgs) -> Void: ...
    @winrt_commethod(7)
    def IdleStateEntered(self, sender: win32more.Windows.UI.Composition.Interactions.InteractionTracker, args: win32more.Windows.UI.Composition.Interactions.InteractionTrackerIdleStateEnteredArgs) -> Void: ...
    @winrt_commethod(8)
    def InertiaStateEntered(self, sender: win32more.Windows.UI.Composition.Interactions.InteractionTracker, args: win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaStateEnteredArgs) -> Void: ...
    @winrt_commethod(9)
    def InteractingStateEntered(self, sender: win32more.Windows.UI.Composition.Interactions.InteractionTracker, args: win32more.Windows.UI.Composition.Interactions.InteractionTrackerInteractingStateEnteredArgs) -> Void: ...
    @winrt_commethod(10)
    def RequestIgnored(self, sender: win32more.Windows.UI.Composition.Interactions.InteractionTracker, args: win32more.Windows.UI.Composition.Interactions.InteractionTrackerRequestIgnoredArgs) -> Void: ...
    @winrt_commethod(11)
    def ValuesChanged(self, sender: win32more.Windows.UI.Composition.Interactions.InteractionTracker, args: win32more.Windows.UI.Composition.Interactions.InteractionTrackerValuesChangedArgs) -> Void: ...
class IInteractionTrackerRequestIgnoredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerRequestIgnoredArgs'
    _iid_ = Guid('{80dd82f1-ce25-488f-91dd-cb6455ccff2e}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerStatics'
    _iid_ = Guid('{bba5d7b7-6590-4498-8d6c-eb62b514c92a}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTracker: ...
    @winrt_commethod(7)
    def CreateWithOwner(self, compositor: win32more.Windows.UI.Composition.Compositor, owner: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerOwner) -> win32more.Windows.UI.Composition.Interactions.InteractionTracker: ...
class IInteractionTrackerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerStatics2'
    _iid_ = Guid('{35e53720-46b7-5cb0-b505-f3d6884a6163}')
    @winrt_commethod(6)
    def SetBindingMode(self, boundTracker1: win32more.Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Windows.UI.Composition.Interactions.InteractionTracker, axisMode: win32more.Windows.UI.Composition.Interactions.InteractionBindingAxisModes) -> Void: ...
    @winrt_commethod(7)
    def GetBindingMode(self, boundTracker1: win32more.Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Windows.UI.Composition.Interactions.InteractionTracker) -> win32more.Windows.UI.Composition.Interactions.InteractionBindingAxisModes: ...
class IInteractionTrackerValuesChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs'
    _iid_ = Guid('{cf1578ef-d3df-4501-b9e6-f02fb22f73d0}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_RequestId(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Scale(self) -> Single: ...
    Position = property(get_Position, None)
    RequestId = property(get_RequestId, None)
    Scale = property(get_Scale, None)
class IInteractionTrackerVector2InertiaModifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaModifier'
    _iid_ = Guid('{87e08ab0-3086-4853-a4b7-77882ad5d7e3}')
class IInteractionTrackerVector2InertiaModifierFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaModifierFactory'
    _iid_ = Guid('{7401d6c4-6c6d-48df-bc3e-171e227e7d7f}')
class IInteractionTrackerVector2InertiaNaturalMotion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion'
    _iid_ = Guid('{5f17695c-162d-4c07-9400-c282b28276ca}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_NaturalMotion(self) -> win32more.Windows.UI.Composition.Vector2NaturalMotionAnimation: ...
    @winrt_commethod(9)
    def put_NaturalMotion(self, value: win32more.Windows.UI.Composition.Vector2NaturalMotionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class IInteractionTrackerVector2InertiaNaturalMotionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotionStatics'
    _iid_ = Guid('{82001a48-09c0-434f-8189-141c66df362f}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion: ...
class IVisualInteractionSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IVisualInteractionSource'
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
    def get_ManipulationRedirectionMode(self) -> win32more.Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode: ...
    @winrt_commethod(11)
    def put_ManipulationRedirectionMode(self, value: win32more.Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(12)
    def get_PositionXChainingMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(13)
    def put_PositionXChainingMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(14)
    def get_PositionXSourceMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(15)
    def put_PositionXSourceMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(16)
    def get_PositionYChainingMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(17)
    def put_PositionYChainingMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(18)
    def get_PositionYSourceMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(19)
    def put_PositionYSourceMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(20)
    def get_ScaleChainingMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(21)
    def put_ScaleChainingMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(22)
    def get_ScaleSourceMode(self) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(23)
    def put_ScaleSourceMode(self, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(24)
    def get_Source(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(25)
    def TryRedirectForManipulation(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IVisualInteractionSource2'
    _iid_ = Guid('{aa914893-a73c-414d-80d0-249bad2fbd93}')
    @winrt_commethod(6)
    def get_DeltaPosition(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_DeltaScale(self) -> Single: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_PositionVelocity(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(10)
    def get_Scale(self) -> Single: ...
    @winrt_commethod(11)
    def get_ScaleVelocity(self) -> Single: ...
    @winrt_commethod(12)
    def ConfigureCenterPointXModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(13)
    def ConfigureCenterPointYModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(14)
    def ConfigureDeltaPositionXModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(15)
    def ConfigureDeltaPositionYModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(16)
    def ConfigureDeltaScaleModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    DeltaPosition = property(get_DeltaPosition, None)
    DeltaScale = property(get_DeltaScale, None)
    Position = property(get_Position, None)
    PositionVelocity = property(get_PositionVelocity, None)
    Scale = property(get_Scale, None)
    ScaleVelocity = property(get_ScaleVelocity, None)
class IVisualInteractionSource3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IVisualInteractionSource3'
    _iid_ = Guid('{d941ef2a-0d5c-4057-92d7-c9711533204f}')
    @winrt_commethod(6)
    def get_PointerWheelConfig(self) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceConfiguration: ...
    PointerWheelConfig = property(get_PointerWheelConfig, None)
class IVisualInteractionSourceObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IVisualInteractionSourceObjectFactory'
    _iid_ = Guid('{b2ca917c-e98a-41f2-b3c9-891c9266c8f6}')
class IVisualInteractionSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IVisualInteractionSourceStatics'
    _iid_ = Guid('{369965e1-8645-4f75-ba00-6479cd10c8e6}')
    @winrt_commethod(6)
    def Create(self, source: win32more.Windows.UI.Composition.Visual) -> win32more.Windows.UI.Composition.Interactions.VisualInteractionSource: ...
class IVisualInteractionSourceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Interactions.IVisualInteractionSourceStatics2'
    _iid_ = Guid('{a979c032-5764-55e0-bc1f-0778786dcfde}')
    @winrt_commethod(6)
    def CreateFromIVisualElement(self, source: win32more.Windows.UI.Composition.IVisualElement) -> win32more.Windows.UI.Composition.Interactions.VisualInteractionSource: ...
class InteractionBindingAxisModes(Enum, UInt32):
    None_ = 0
    PositionX = 1
    PositionY = 2
    Scale = 4
class InteractionChainingMode(Enum, Int32):
    Auto = 0
    Always = 1
    Never = 2
class InteractionSourceConfiguration(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionSourceConfiguration
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionSourceConfiguration'
    @winrt_mixinmethod
    def get_PositionXSourceMode(self: win32more.Windows.UI.Composition.Interactions.IInteractionSourceConfiguration) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_PositionXSourceMode(self: win32more.Windows.UI.Composition.Interactions.IInteractionSourceConfiguration, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionYSourceMode(self: win32more.Windows.UI.Composition.Interactions.IInteractionSourceConfiguration) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_PositionYSourceMode(self: win32more.Windows.UI.Composition.Interactions.IInteractionSourceConfiguration, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleSourceMode(self: win32more.Windows.UI.Composition.Interactions.IInteractionSourceConfiguration) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_ScaleSourceMode(self: win32more.Windows.UI.Composition.Interactions.IInteractionSourceConfiguration, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
class InteractionSourceMode(Enum, Int32):
    Disabled = 0
    EnabledWithInertia = 1
    EnabledWithoutInertia = 2
class InteractionSourceRedirectionMode(Enum, Int32):
    Disabled = 0
    Enabled = 1
class InteractionTracker(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTracker
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTracker'
    @winrt_mixinmethod
    def get_InteractionSources(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.UI.Composition.Interactions.CompositionInteractionSourceCollection: ...
    @winrt_mixinmethod
    def get_IsPositionRoundingSuggested(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_MaxPosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_MaxScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def put_MaxScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinPosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_MinPosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_MinScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def put_MinScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalRestingPosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_NaturalRestingScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def get_Owner(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.UI.Composition.Interactions.IInteractionTrackerOwner: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_PositionInertiaDecayRate(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def put_PositionInertiaDecayRate(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def get_PositionVelocityInPixelsPerSecond(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def get_ScaleInertiaDecayRate(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_ScaleInertiaDecayRate(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleVelocityInPercentPerSecond(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def AdjustPositionXIfGreaterThanThreshold(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_mixinmethod
    def AdjustPositionYIfGreaterThanThreshold(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_mixinmethod
    def ConfigurePositionXInertiaModifiers(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def ConfigurePositionYInertiaModifiers(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureScaleInertiaModifiers(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def TryUpdatePosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionBy(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, amount: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithAnimation(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, animation: win32more.Windows.UI.Composition.CompositionAnimation) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithAdditionalVelocity(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, velocityInPixelsPerSecond: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, value: Single, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScaleWithAnimation(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, animation: win32more.Windows.UI.Composition.CompositionAnimation, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScaleWithAdditionalVelocity(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker, velocityInPercentPerSecond: Single, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def ConfigureCenterPointXInertiaModifiers(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureCenterPointYInertiaModifiers(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureVector2PositionInertiaModifiers(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker3, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier]) -> Void: ...
    @winrt_overload
    @winrt_mixinmethod
    def TryUpdatePositionWithOption(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker4, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionByWithOption(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker4, amount: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Windows.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_mixinmethod
    def get_IsInertiaFromImpulse(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker4) -> Boolean: ...
    @TryUpdatePositionWithOption.register
    @winrt_mixinmethod
    def TryUpdatePositionWithOption(self: win32more.Windows.UI.Composition.Interactions.IInteractionTracker5, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Windows.UI.Composition.Interactions.InteractionTrackerClampingOption, posUpdateOption: win32more.Windows.UI.Composition.Interactions.InteractionTrackerPositionUpdateOption) -> Int32: ...
    @winrt_classmethod
    def SetBindingMode(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerStatics2, boundTracker1: win32more.Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Windows.UI.Composition.Interactions.InteractionTracker, axisMode: win32more.Windows.UI.Composition.Interactions.InteractionBindingAxisModes) -> Void: ...
    @winrt_classmethod
    def GetBindingMode(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerStatics2, boundTracker1: win32more.Windows.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Windows.UI.Composition.Interactions.InteractionTracker) -> win32more.Windows.UI.Composition.Interactions.InteractionBindingAxisModes: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTracker: ...
    @winrt_classmethod
    def CreateWithOwner(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerStatics, compositor: win32more.Windows.UI.Composition.Compositor, owner: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerOwner) -> win32more.Windows.UI.Composition.Interactions.InteractionTracker: ...
    InteractionSources = property(get_InteractionSources, None)
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
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
class InteractionTrackerClampingOption(Enum, Int32):
    Auto = 0
    Disabled = 1
class InteractionTrackerCustomAnimationStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerCustomAnimationStateEnteredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs2) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
    RequestId = property(get_RequestId, None)
class InteractionTrackerIdleStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerIdleStateEnteredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs2) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
    RequestId = property(get_RequestId, None)
class InteractionTrackerInertiaModifier(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaModifier
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier'
class InteractionTrackerInertiaMotion(ComPtr):
    extends: win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaMotion'
    @winrt_mixinmethod
    def get_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Motion(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Motion(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotion, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaMotionStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaMotion: ...
    Condition = property(get_Condition, put_Condition)
    Motion = property(get_Motion, put_Motion)
class InteractionTrackerInertiaNaturalMotion(ComPtr):
    extends: win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion'
    @winrt_mixinmethod
    def get_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalMotion(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion) -> win32more.Windows.UI.Composition.ScalarNaturalMotionAnimation: ...
    @winrt_mixinmethod
    def put_NaturalMotion(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion, value: win32more.Windows.UI.Composition.ScalarNaturalMotionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotionStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class InteractionTrackerInertiaRestingValue(ComPtr):
    extends: win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue'
    @winrt_mixinmethod
    def get_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_RestingValue(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_RestingValue(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValueStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue: ...
    Condition = property(get_Condition, put_Condition)
    RestingValue = property(get_RestingValue, put_RestingValue)
class InteractionTrackerInertiaStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInertiaStateEnteredArgs'
    @winrt_mixinmethod
    def get_ModifiedRestingPosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_ModifiedRestingScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_NaturalRestingPosition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_NaturalRestingScale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Single: ...
    @winrt_mixinmethod
    def get_PositionVelocityInPixelsPerSecond(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ScaleVelocityInPercentPerSecond(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Single: ...
    @winrt_mixinmethod
    def get_IsInertiaFromImpulse(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs3) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
    ModifiedRestingPosition = property(get_ModifiedRestingPosition, None)
    ModifiedRestingScale = property(get_ModifiedRestingScale, None)
    NaturalRestingPosition = property(get_NaturalRestingPosition, None)
    NaturalRestingScale = property(get_NaturalRestingScale, None)
    PositionVelocityInPixelsPerSecond = property(get_PositionVelocityInPixelsPerSecond, None)
    RequestId = property(get_RequestId, None)
    ScaleVelocityInPercentPerSecond = property(get_ScaleVelocityInPercentPerSecond, None)
class InteractionTrackerInteractingStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerInteractingStateEnteredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs2) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
    RequestId = property(get_RequestId, None)
class InteractionTrackerPositionUpdateOption(Enum, Int32):
    Default = 0
    AllowActiveCustomScaleAnimation = 1
class InteractionTrackerRequestIgnoredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerRequestIgnoredArgs
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerRequestIgnoredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerRequestIgnoredArgs) -> Int32: ...
    RequestId = property(get_RequestId, None)
class InteractionTrackerValuesChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerValuesChangedArgs'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> Single: ...
    Position = property(get_Position, None)
    RequestId = property(get_RequestId, None)
    Scale = property(get_Scale, None)
class InteractionTrackerVector2InertiaModifier(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaModifier
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier'
class InteractionTrackerVector2InertiaNaturalMotion(ComPtr):
    extends: win32more.Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier
    default_interface: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion
    _classid_ = 'Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion'
    @winrt_mixinmethod
    def get_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion, value: win32more.Windows.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalMotion(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion) -> win32more.Windows.UI.Composition.Vector2NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def put_NaturalMotion(self: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion, value: win32more.Windows.UI.Composition.Vector2NaturalMotionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotionStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class VisualInteractionSource(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource
    _classid_ = 'Windows.UI.Composition.Interactions.VisualInteractionSource'
    @winrt_mixinmethod
    def get_IsPositionXRailsEnabled(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPositionXRailsEnabled(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPositionYRailsEnabled(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPositionYRailsEnabled(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ManipulationRedirectionMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_ManipulationRedirectionMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Windows.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionXChainingMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_mixinmethod
    def put_PositionXChainingMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionXSourceMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_mixinmethod
    def put_PositionXSourceMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionYChainingMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_mixinmethod
    def put_PositionYChainingMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionYSourceMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_mixinmethod
    def put_PositionYSourceMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleChainingMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_mixinmethod
    def put_ScaleChainingMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Windows.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleSourceMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_mixinmethod
    def put_ScaleSourceMode(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Windows.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def TryRedirectForManipulation(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaPosition(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_DeltaScale(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2) -> Single: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_PositionVelocity(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2) -> Single: ...
    @winrt_mixinmethod
    def get_ScaleVelocity(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2) -> Single: ...
    @winrt_mixinmethod
    def ConfigureCenterPointXModifiers(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureCenterPointYModifiers(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureDeltaPositionXModifiers(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureDeltaPositionYModifiers(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureDeltaScaleModifiers(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def get_PointerWheelConfig(self: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSource3) -> win32more.Windows.UI.Composition.Interactions.InteractionSourceConfiguration: ...
    @winrt_classmethod
    def CreateFromIVisualElement(cls: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSourceStatics2, source: win32more.Windows.UI.Composition.IVisualElement) -> win32more.Windows.UI.Composition.Interactions.VisualInteractionSource: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Interactions.IVisualInteractionSourceStatics, source: win32more.Windows.UI.Composition.Visual) -> win32more.Windows.UI.Composition.Interactions.VisualInteractionSource: ...
    DeltaPosition = property(get_DeltaPosition, None)
    DeltaScale = property(get_DeltaScale, None)
    IsPositionXRailsEnabled = property(get_IsPositionXRailsEnabled, put_IsPositionXRailsEnabled)
    IsPositionYRailsEnabled = property(get_IsPositionYRailsEnabled, put_IsPositionYRailsEnabled)
    ManipulationRedirectionMode = property(get_ManipulationRedirectionMode, put_ManipulationRedirectionMode)
    PointerWheelConfig = property(get_PointerWheelConfig, None)
    Position = property(get_Position, None)
    PositionVelocity = property(get_PositionVelocity, None)
    PositionXChainingMode = property(get_PositionXChainingMode, put_PositionXChainingMode)
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYChainingMode = property(get_PositionYChainingMode, put_PositionYChainingMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    Scale = property(get_Scale, None)
    ScaleChainingMode = property(get_ScaleChainingMode, put_ScaleChainingMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
    ScaleVelocity = property(get_ScaleVelocity, None)
    Source = property(get_Source, None)
class VisualInteractionSourceRedirectionMode(Enum, Int32):
    Off = 0
    CapableTouchpadOnly = 1
    PointerWheelOnly = 2
    CapableTouchpadAndPointerWheel = 3


make_ready(__name__)
