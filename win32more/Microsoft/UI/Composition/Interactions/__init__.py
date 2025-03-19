from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Composition.Interactions
import win32more.Microsoft.UI.Input
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Win32.System.WinRT
class CompositionConditionalValue(ComPtr):
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    default_interface: win32more.Microsoft.UI.Composition.Interactions.ICompositionConditionalValue
    _classid_ = 'Microsoft.UI.Composition.Interactions.CompositionConditionalValue'
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionConditionalValue, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Condition(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionConditionalValue) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionConditionalValue) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionConditionalValue, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Interactions.ICompositionConditionalValueStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue: ...
    Condition = property(get_Condition, put_Condition)
    Value = property(get_Value, put_Value)
class CompositionInteractionSourceCollection(ComPtr):
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    implements: Tuple[IterableProtocol[win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSource]]
    default_interface: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSourceCollection
    _classid_ = 'Microsoft.UI.Composition.Interactions.CompositionInteractionSourceCollection'
    @winrt_mixinmethod
    def RemoveAll(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSourceCollection) -> Void: ...
    @winrt_mixinmethod
    def Add(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSourceCollection, value: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSourceCollection, value: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_mixinmethod
    def get_Count(self: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSourceCollection) -> Int32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSource]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSource]: ...
    Count = property(get_Count, None)
class ICompositionConditionalValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.ICompositionConditionalValue'
    _iid_ = Guid('{3743dda0-fbe2-5ecf-9e80-4638a011f707}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_Value(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    Value = property(get_Value, put_Value)
class ICompositionConditionalValueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.ICompositionConditionalValueStatics'
    _iid_ = Guid('{df133c1f-a185-536c-b54b-8f369212a581}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue: ...
class ICompositionInteractionSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.ICompositionInteractionSource'
    _iid_ = Guid('{711c72c0-c406-4a12-859b-b44f651af046}')
class ICompositionInteractionSourceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.ICompositionInteractionSourceCollection'
    _iid_ = Guid('{9aa1b86b-b002-5e2e-bb2b-0e2c547445e1}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def Add(self, value: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_commethod(8)
    def Remove(self, value: win32more.Microsoft.UI.Composition.Interactions.ICompositionInteractionSource) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class IInteractionSourceConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration'
    _iid_ = Guid('{099e0124-dadf-5bc6-a895-90387657550f}')
    @winrt_commethod(6)
    def get_PositionXSourceMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(7)
    def put_PositionXSourceMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(8)
    def get_PositionYSourceMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(9)
    def put_PositionYSourceMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(10)
    def get_ScaleSourceMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_commethod(11)
    def put_ScaleSourceMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    PositionXSourceMode = property(get_PositionXSourceMode, put_PositionXSourceMode)
    PositionYSourceMode = property(get_PositionYSourceMode, put_PositionYSourceMode)
    ScaleSourceMode = property(get_ScaleSourceMode, put_ScaleSourceMode)
class IInteractionTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTracker'
    _iid_ = Guid('{02d8ec1f-8f04-505e-bd1e-47b2a204de51}')
    @winrt_commethod(6)
    def get_InteractionSources(self) -> win32more.Microsoft.UI.Composition.Interactions.CompositionInteractionSourceCollection: ...
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
    def get_Owner(self) -> win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerOwner: ...
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
    def ConfigurePositionXInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(30)
    def ConfigurePositionYInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(31)
    def ConfigureScaleInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_commethod(32)
    def TryUpdatePosition(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(33)
    def TryUpdatePositionBy(self, amount: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(34)
    def TryUpdatePositionWithAnimation(self, animation: win32more.Microsoft.UI.Composition.CompositionAnimation) -> Int32: ...
    @winrt_commethod(35)
    def TryUpdatePositionWithAdditionalVelocity(self, velocityInPixelsPerSecond: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(36)
    def TryUpdateScale(self, value: Single, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_commethod(37)
    def TryUpdateScaleWithAnimation(self, animation: win32more.Microsoft.UI.Composition.CompositionAnimation, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
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
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTracker2'
    _iid_ = Guid('{396d7fb1-2fad-5508-8591-4ff0dc5a7484}')
    @winrt_commethod(6)
    def ConfigureCenterPointXInertiaModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(7)
    def ConfigureCenterPointYInertiaModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
class IInteractionTracker3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTracker3'
    _iid_ = Guid('{239752cf-266c-5acb-acc3-b3e3ecaf4d3f}')
    @winrt_commethod(6)
    def ConfigureVector2PositionInertiaModifiers(self, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier]) -> Void: ...
class IInteractionTracker4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTracker4'
    _iid_ = Guid('{a9a9ce02-53c9-5690-a575-f340b7c2fdf2}')
    @winrt_commethod(6)
    def TryUpdatePositionWithOption(self, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_commethod(7)
    def TryUpdatePositionByWithOption(self, amount: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_commethod(8)
    def get_IsInertiaFromImpulse(self) -> Boolean: ...
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
class IInteractionTracker5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTracker5'
    _iid_ = Guid('{dbfcd333-c3bf-5057-a45e-25edf06ebd8f}')
    @winrt_commethod(6)
    def TryUpdatePositionWithOption(self, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption, posUpdateOption: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerPositionUpdateOption) -> Int32: ...
class IInteractionTrackerCustomAnimationStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs'
    _iid_ = Guid('{7464035c-cfce-56da-9472-420f276bd0a5}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerCustomAnimationStateEnteredArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs2'
    _iid_ = Guid('{06b99fbc-d6a8-5ae3-88b8-e91621becbd6}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerIdleStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs'
    _iid_ = Guid('{199094ab-15fd-539c-97b8-964a8196f777}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerIdleStateEnteredArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs2'
    _iid_ = Guid('{4eb213c0-931c-5164-8965-11c0186d3390}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerInertiaModifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaModifier'
    _iid_ = Guid('{4d3a0c6b-c508-5029-a47a-cbf64636f010}')
class IInteractionTrackerInertiaModifierFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaModifierFactory'
    _iid_ = Guid('{6dee5b33-0b5a-57b1-8537-93d4fd038f9f}')
class IInteractionTrackerInertiaMotion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotion'
    _iid_ = Guid('{91f662c0-3141-5b5e-862f-cfc60bee8cd6}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_Motion(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_Motion(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    Motion = property(get_Motion, put_Motion)
class IInteractionTrackerInertiaMotionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotionStatics'
    _iid_ = Guid('{b0185a4f-0059-52c6-a660-9aed0c44ff7d}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaMotion: ...
class IInteractionTrackerInertiaNaturalMotion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion'
    _iid_ = Guid('{8c7482e0-185d-56b1-b67f-fca4fcd13cd2}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_NaturalMotion(self) -> win32more.Microsoft.UI.Composition.ScalarNaturalMotionAnimation: ...
    @winrt_commethod(9)
    def put_NaturalMotion(self, value: win32more.Microsoft.UI.Composition.ScalarNaturalMotionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class IInteractionTrackerInertiaNaturalMotionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotionStatics'
    _iid_ = Guid('{860ec143-f165-5298-abf2-47369dd07f10}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion: ...
class IInteractionTrackerInertiaRestingValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue'
    _iid_ = Guid('{1a2b20cd-3371-53ff-a560-f4847b467d73}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_RestingValue(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(9)
    def put_RestingValue(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    RestingValue = property(get_RestingValue, put_RestingValue)
class IInteractionTrackerInertiaRestingValueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValueStatics'
    _iid_ = Guid('{cf0f0414-7fdf-5284-aeef-28b71b62aa4f}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue: ...
class IInteractionTrackerInertiaStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs'
    _iid_ = Guid('{5b76c949-a4d0-5c9d-9292-7013ae9656c7}')
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
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs2'
    _iid_ = Guid('{c42d7e8f-7199-57a9-8aec-8727552b13e6}')
    @winrt_commethod(6)
    def get_IsInertiaFromImpulse(self) -> Boolean: ...
    IsInertiaFromImpulse = property(get_IsInertiaFromImpulse, None)
class IInteractionTrackerInertiaStateEnteredArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs3'
    _iid_ = Guid('{ce726ca0-1c04-531b-9951-4aec996952e4}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerInteractingStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs'
    _iid_ = Guid('{70d29b84-0931-5f17-a8a1-82f8f8782532}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerInteractingStateEnteredArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs2'
    _iid_ = Guid('{2f1ff38d-2f51-5ceb-8d09-bda1519f9342}')
    @winrt_commethod(6)
    def get_IsFromBinding(self) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
class IInteractionTrackerOwner(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerOwner'
    _iid_ = Guid('{8869779d-1d2a-5816-836a-68a910507d87}')
    @winrt_commethod(6)
    def CustomAnimationStateEntered(self, sender: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, args: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerCustomAnimationStateEnteredArgs) -> Void: ...
    @winrt_commethod(7)
    def IdleStateEntered(self, sender: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, args: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerIdleStateEnteredArgs) -> Void: ...
    @winrt_commethod(8)
    def InertiaStateEntered(self, sender: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, args: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaStateEnteredArgs) -> Void: ...
    @winrt_commethod(9)
    def InteractingStateEntered(self, sender: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, args: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInteractingStateEnteredArgs) -> Void: ...
    @winrt_commethod(10)
    def RequestIgnored(self, sender: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, args: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerRequestIgnoredArgs) -> Void: ...
    @winrt_commethod(11)
    def ValuesChanged(self, sender: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, args: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerValuesChangedArgs) -> Void: ...
class IInteractionTrackerRequestIgnoredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerRequestIgnoredArgs'
    _iid_ = Guid('{c276205e-f7a5-5ba2-ad45-d12c3c339149}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Int32: ...
    RequestId = property(get_RequestId, None)
class IInteractionTrackerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerStatics'
    _iid_ = Guid('{7ac9867a-e16e-56ef-9809-f6e404240f50}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTracker: ...
    @winrt_commethod(7)
    def CreateWithOwner(self, compositor: win32more.Microsoft.UI.Composition.Compositor, owner: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerOwner) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTracker: ...
class IInteractionTrackerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerStatics2'
    _iid_ = Guid('{25658e4c-b99f-5108-aab7-1cc44f11508b}')
    @winrt_commethod(6)
    def SetBindingMode(self, boundTracker1: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, axisMode: win32more.Microsoft.UI.Composition.Interactions.InteractionBindingAxisModes) -> Void: ...
    @winrt_commethod(7)
    def GetBindingMode(self, boundTracker1: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker) -> win32more.Microsoft.UI.Composition.Interactions.InteractionBindingAxisModes: ...
class IInteractionTrackerValuesChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs'
    _iid_ = Guid('{9b495bed-1cf7-55c1-82b9-8022cbf3c766}')
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
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaModifier'
    _iid_ = Guid('{4b8ed310-cb61-5f0a-b99a-940cdd2c42b1}')
class IInteractionTrackerVector2InertiaModifierFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaModifierFactory'
    _iid_ = Guid('{1b3fd240-ba66-5296-b801-62a2a3606613}')
class IInteractionTrackerVector2InertiaNaturalMotion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion'
    _iid_ = Guid('{097ba1a6-e077-52d1-86d3-38e3f6619ddf}')
    @winrt_commethod(6)
    def get_Condition(self) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(7)
    def put_Condition(self, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_commethod(8)
    def get_NaturalMotion(self) -> win32more.Microsoft.UI.Composition.Vector2NaturalMotionAnimation: ...
    @winrt_commethod(9)
    def put_NaturalMotion(self, value: win32more.Microsoft.UI.Composition.Vector2NaturalMotionAnimation) -> Void: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class IInteractionTrackerVector2InertiaNaturalMotionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotionStatics'
    _iid_ = Guid('{cc24ab87-9131-5286-b3ce-1ef97e0974e6}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion: ...
class IVisualInteractionSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IVisualInteractionSource'
    _iid_ = Guid('{ea595c95-b9cb-5cd4-bb9c-4934ff329063}')
    @winrt_commethod(6)
    def get_IsPositionXRailsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPositionXRailsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsPositionYRailsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsPositionYRailsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ManipulationRedirectionMode(self) -> win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode: ...
    @winrt_commethod(11)
    def put_ManipulationRedirectionMode(self, value: win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode) -> Void: ...
    @winrt_commethod(12)
    def get_PositionXChainingMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(13)
    def put_PositionXChainingMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(14)
    def get_PositionXSourceMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(15)
    def put_PositionXSourceMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(16)
    def get_PositionYChainingMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(17)
    def put_PositionYChainingMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(18)
    def get_PositionYSourceMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(19)
    def put_PositionYSourceMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(20)
    def get_ScaleChainingMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_commethod(21)
    def put_ScaleChainingMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_commethod(22)
    def get_ScaleSourceMode(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_commethod(23)
    def put_ScaleSourceMode(self, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_commethod(24)
    def get_Source(self) -> win32more.Microsoft.UI.Composition.Visual: ...
    @winrt_commethod(25)
    def TryRedirectForManipulation(self, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Composition.Interactions.IVisualInteractionSource2'
    _iid_ = Guid('{ff1132ba-dc0d-519e-be49-be301e52306a}')
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
    def ConfigureCenterPointXModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(13)
    def ConfigureCenterPointYModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(14)
    def ConfigureDeltaPositionXModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(15)
    def ConfigureDeltaPositionYModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_commethod(16)
    def ConfigureDeltaScaleModifiers(self, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    DeltaPosition = property(get_DeltaPosition, None)
    DeltaScale = property(get_DeltaScale, None)
    Position = property(get_Position, None)
    PositionVelocity = property(get_PositionVelocity, None)
    Scale = property(get_Scale, None)
    ScaleVelocity = property(get_ScaleVelocity, None)
class IVisualInteractionSource3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IVisualInteractionSource3'
    _iid_ = Guid('{d523bd66-a05d-5417-8e07-84ae3caf9752}')
    @winrt_commethod(6)
    def get_PointerWheelConfig(self) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceConfiguration: ...
    PointerWheelConfig = property(get_PointerWheelConfig, None)
class IVisualInteractionSourceObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IVisualInteractionSourceObjectFactory'
    _iid_ = Guid('{feb73102-238c-52aa-8e03-b68d5ecc44b3}')
class IVisualInteractionSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IVisualInteractionSourceStatics'
    _iid_ = Guid('{5fc9c763-e2e5-530e-87cd-b93118ade8a3}')
    @winrt_commethod(6)
    def Create(self, source: win32more.Microsoft.UI.Composition.Visual) -> win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSource: ...
class IVisualInteractionSourceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Interactions.IVisualInteractionSourceStatics2'
    _iid_ = Guid('{a6b494fe-12a1-5a73-b87e-4c4ef58eac6c}')
    @winrt_commethod(6)
    def CreateFromIVisualElement(self, source: win32more.Microsoft.UI.Composition.IVisualElement) -> win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSource: ...
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
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionSourceConfiguration'
    @winrt_mixinmethod
    def put_PositionXSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionXSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def get_PositionYSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_PositionYSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_ScaleSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionSourceConfiguration, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode) -> Void: ...
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
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTracker'
    @winrt_overload
    @winrt_mixinmethod
    def TryUpdatePositionWithOption(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker5, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption, posUpdateOption: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerPositionUpdateOption) -> Int32: ...
    @winrt_mixinmethod
    def get_IsInertiaFromImpulse(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker4) -> Boolean: ...
    @winrt_mixinmethod
    def get_InteractionSources(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Microsoft.UI.Composition.Interactions.CompositionInteractionSourceCollection: ...
    @winrt_mixinmethod
    def put_PositionInertiaDecayRate(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def TryUpdatePositionByWithOption(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker4, amount: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_mixinmethod
    def get_IsPositionRoundingSuggested(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_MaxPosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_MaxScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def put_MaxScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinPosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_MinPosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_MinScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def put_MinScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalRestingPosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_NaturalRestingScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def get_Owner(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerOwner: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_PositionInertiaDecayRate(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_PositionVelocityInPixelsPerSecond(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def get_ScaleInertiaDecayRate(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_ScaleInertiaDecayRate(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleVelocityInPercentPerSecond(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker) -> Single: ...
    @winrt_mixinmethod
    def AdjustPositionXIfGreaterThanThreshold(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_mixinmethod
    def AdjustPositionYIfGreaterThanThreshold(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, adjustment: Single, positionThreshold: Single) -> Void: ...
    @winrt_mixinmethod
    def ConfigurePositionXInertiaModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def ConfigurePositionYInertiaModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureScaleInertiaModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier]) -> Void: ...
    @winrt_mixinmethod
    def TryUpdatePosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionBy(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, amount: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithAnimation(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, animation: win32more.Microsoft.UI.Composition.CompositionAnimation) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdatePositionWithAdditionalVelocity(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, velocityInPixelsPerSecond: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, value: Single, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScaleWithAnimation(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, animation: win32more.Microsoft.UI.Composition.CompositionAnimation, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def TryUpdateScaleWithAdditionalVelocity(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker, velocityInPercentPerSecond: Single, centerPoint: win32more.Windows.Foundation.Numerics.Vector3) -> Int32: ...
    @winrt_mixinmethod
    def ConfigureCenterPointXInertiaModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureCenterPointYInertiaModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureVector2PositionInertiaModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker3, modifiers: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier]) -> Void: ...
    @TryUpdatePositionWithOption.register
    @winrt_mixinmethod
    def TryUpdatePositionWithOption(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTracker4, value: win32more.Windows.Foundation.Numerics.Vector3, option: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption) -> Int32: ...
    @winrt_classmethod
    def SetBindingMode(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerStatics2, boundTracker1: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, axisMode: win32more.Microsoft.UI.Composition.Interactions.InteractionBindingAxisModes) -> Void: ...
    @winrt_classmethod
    def GetBindingMode(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerStatics2, boundTracker1: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker, boundTracker2: win32more.Microsoft.UI.Composition.Interactions.InteractionTracker) -> win32more.Microsoft.UI.Composition.Interactions.InteractionBindingAxisModes: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTracker: ...
    @winrt_classmethod
    def CreateWithOwner(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerStatics, compositor: win32more.Microsoft.UI.Composition.Compositor, owner: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerOwner) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTracker: ...
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
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerCustomAnimationStateEnteredArgs'
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerCustomAnimationStateEnteredArgs) -> Int32: ...
    IsFromBinding = property(get_IsFromBinding, None)
    RequestId = property(get_RequestId, None)
class InteractionTrackerIdleStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerIdleStateEnteredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerIdleStateEnteredArgs2) -> Boolean: ...
    IsFromBinding = property(get_IsFromBinding, None)
    RequestId = property(get_RequestId, None)
class InteractionTrackerInertiaModifier(ComPtr):
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaModifier
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier'
class InteractionTrackerInertiaMotion(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotion
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaMotion'
    @winrt_mixinmethod
    def put_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotion, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotion) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def get_Motion(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotion) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Motion(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotion, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaMotionStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaMotion: ...
    Condition = property(get_Condition, put_Condition)
    Motion = property(get_Motion, put_Motion)
class InteractionTrackerInertiaNaturalMotion(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion'
    @winrt_mixinmethod
    def put_NaturalMotion(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion, value: win32more.Microsoft.UI.Composition.ScalarNaturalMotionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_NaturalMotion(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion) -> win32more.Microsoft.UI.Composition.ScalarNaturalMotionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotion) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaNaturalMotionStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaNaturalMotion: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class InteractionTrackerInertiaRestingValue(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaModifier
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue'
    @winrt_mixinmethod
    def put_RestingValue(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_RestingValue(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def get_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def put_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValue, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaRestingValueStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaRestingValue: ...
    Condition = property(get_Condition, put_Condition)
    RestingValue = property(get_RestingValue, put_RestingValue)
class InteractionTrackerInertiaStateEnteredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerInertiaStateEnteredArgs'
    @winrt_mixinmethod
    def get_ModifiedRestingScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_NaturalRestingScale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Single: ...
    @winrt_mixinmethod
    def get_PositionVelocityInPixelsPerSecond(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ModifiedRestingPosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs3) -> Boolean: ...
    @winrt_mixinmethod
    def get_NaturalRestingPosition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ScaleVelocityInPercentPerSecond(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs) -> Single: ...
    @winrt_mixinmethod
    def get_IsInertiaFromImpulse(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInertiaStateEnteredArgs2) -> Boolean: ...
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
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerInteractingStateEnteredArgs'
    @winrt_mixinmethod
    def get_IsFromBinding(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerInteractingStateEnteredArgs) -> Int32: ...
    IsFromBinding = property(get_IsFromBinding, None)
    RequestId = property(get_RequestId, None)
class InteractionTrackerPositionUpdateOption(Enum, Int32):
    Default = 0
    AllowActiveCustomScaleAnimation = 1
class InteractionTrackerRequestIgnoredArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerRequestIgnoredArgs
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerRequestIgnoredArgs'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerRequestIgnoredArgs) -> Int32: ...
    RequestId = property(get_RequestId, None)
class InteractionTrackerValuesChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerValuesChangedArgs'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> Single: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerValuesChangedArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Position = property(get_Position, None)
    RequestId = property(get_RequestId, None)
    Scale = property(get_Scale, None)
class InteractionTrackerVector2InertiaModifier(ComPtr):
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaModifier
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier'
class InteractionTrackerVector2InertiaNaturalMotion(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerVector2InertiaModifier
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion
    _classid_ = 'Microsoft.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion'
    @winrt_mixinmethod
    def put_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion, value: win32more.Microsoft.UI.Composition.ExpressionAnimation) -> Void: ...
    @winrt_mixinmethod
    def put_NaturalMotion(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion, value: win32more.Microsoft.UI.Composition.Vector2NaturalMotionAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_Condition(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion) -> win32more.Microsoft.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def get_NaturalMotion(self: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotion) -> win32more.Microsoft.UI.Composition.Vector2NaturalMotionAnimation: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Interactions.IInteractionTrackerVector2InertiaNaturalMotionStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Interactions.InteractionTrackerVector2InertiaNaturalMotion: ...
    Condition = property(get_Condition, put_Condition)
    NaturalMotion = property(get_NaturalMotion, put_NaturalMotion)
class VisualInteractionSource(ComPtr):
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    default_interface: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource
    _classid_ = 'Microsoft.UI.Composition.Interactions.VisualInteractionSource'
    @winrt_mixinmethod
    def get_ManipulationRedirectionMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode: ...
    @winrt_mixinmethod
    def put_PositionXSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionYChainingMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_mixinmethod
    def put_PositionYChainingMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionYSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_mixinmethod
    def put_PositionYSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionVelocity(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2) -> Single: ...
    @winrt_mixinmethod
    def put_IsPositionYRailsEnabled(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleChainingMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_mixinmethod
    def put_ScaleChainingMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_mixinmethod
    def put_ScaleSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def TryRedirectForManipulation(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def put_ManipulationRedirectionMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaPosition(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_DeltaScale(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2) -> Single: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ScaleVelocity(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2) -> Single: ...
    @winrt_mixinmethod
    def ConfigureCenterPointXModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureCenterPointYModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureDeltaPositionXModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureDeltaPositionYModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def ConfigureDeltaScaleModifiers(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource2, conditionalValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Interactions.CompositionConditionalValue]) -> Void: ...
    @winrt_mixinmethod
    def get_PointerWheelConfig(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource3) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceConfiguration: ...
    @winrt_mixinmethod
    def get_PositionXChainingMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode: ...
    @winrt_mixinmethod
    def put_PositionXChainingMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: win32more.Microsoft.UI.Composition.Interactions.InteractionChainingMode) -> Void: ...
    @winrt_mixinmethod
    def get_PositionXSourceMode(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> win32more.Microsoft.UI.Composition.Interactions.InteractionSourceMode: ...
    @winrt_mixinmethod
    def get_IsPositionXRailsEnabled(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPositionXRailsEnabled(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPositionYRailsEnabled(self: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSource) -> Boolean: ...
    @winrt_classmethod
    def CreateFromIVisualElement(cls: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSourceStatics2, source: win32more.Microsoft.UI.Composition.IVisualElement) -> win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSource: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Interactions.IVisualInteractionSourceStatics, source: win32more.Microsoft.UI.Composition.Visual) -> win32more.Microsoft.UI.Composition.Interactions.VisualInteractionSource: ...
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
