from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.UI
import Windows.UI.Composition
import Windows.UI.Xaml
import Windows.UI.Xaml.Controls
import Windows.UI.Xaml.Controls.Primitives
import Windows.UI.Xaml.Media.Animation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AddDeleteThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.AddDeleteThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.AddDeleteThemeTransition: ...
class BackEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.BackEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.BackEase: ...
    @winrt_mixinmethod
    def get_Amplitude(self: Windows.UI.Xaml.Media.Animation.IBackEase) -> Double: ...
    @winrt_mixinmethod
    def put_Amplitude(self: Windows.UI.Xaml.Media.Animation.IBackEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_AmplitudeProperty(cls: Windows.UI.Xaml.Media.Animation.IBackEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
    AmplitudeProperty = property(get_AmplitudeProperty, None)
class BasicConnectedAnimationConfiguration(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
class BeginStoryboard(c_void_p):
    extends: Windows.UI.Xaml.TriggerAction
    ClassId = 'Windows.UI.Xaml.Media.Animation.BeginStoryboard'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.BeginStoryboard: ...
    @winrt_mixinmethod
    def get_Storyboard(self: Windows.UI.Xaml.Media.Animation.IBeginStoryboard) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: Windows.UI.Xaml.Media.Animation.IBeginStoryboard, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    @winrt_classmethod
    def get_StoryboardProperty(cls: Windows.UI.Xaml.Media.Animation.IBeginStoryboardStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
    StoryboardProperty = property(get_StoryboardProperty, None)
class BounceEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.BounceEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.BounceEase: ...
    @winrt_mixinmethod
    def get_Bounces(self: Windows.UI.Xaml.Media.Animation.IBounceEase) -> Int32: ...
    @winrt_mixinmethod
    def put_Bounces(self: Windows.UI.Xaml.Media.Animation.IBounceEase, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Bounciness(self: Windows.UI.Xaml.Media.Animation.IBounceEase) -> Double: ...
    @winrt_mixinmethod
    def put_Bounciness(self: Windows.UI.Xaml.Media.Animation.IBounceEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_BouncesProperty(cls: Windows.UI.Xaml.Media.Animation.IBounceEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BouncinessProperty(cls: Windows.UI.Xaml.Media.Animation.IBounceEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Bounces = property(get_Bounces, put_Bounces)
    Bounciness = property(get_Bounciness, put_Bounciness)
    BouncesProperty = property(get_BouncesProperty, None)
    BouncinessProperty = property(get_BouncinessProperty, None)
class CircleEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.CircleEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.CircleEase: ...
ClockState = Int32
ClockState_Active: ClockState = 0
ClockState_Filling: ClockState = 1
ClockState_Stopped: ClockState = 2
class ColorAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.ColorAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ColorAnimation: ...
    @winrt_mixinmethod
    def get_From(self: Windows.UI.Xaml.Media.Animation.IColorAnimation) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_From(self: Windows.UI.Xaml.Media.Animation.IColorAnimation, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: Windows.UI.Xaml.Media.Animation.IColorAnimation) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_To(self: Windows.UI.Xaml.Media.Animation.IColorAnimation, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: Windows.UI.Xaml.Media.Animation.IColorAnimation) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_By(self: Windows.UI.Xaml.Media.Animation.IColorAnimation, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IColorAnimation) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IColorAnimation, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IColorAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IColorAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class ColorAnimationUsingKeyFrames(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFramesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class ColorKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(13)
    def get_Value(self) -> Windows.UI.Color: ...
    @winrt_commethod(14)
    def put_Value(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(15)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(16)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class ColorKeyFrameCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], value: Windows.UI.Xaml.Media.Animation.ColorKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], value: Windows.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Animation.ColorKeyFrame)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame], items: POINTER(Windows.UI.Xaml.Media.Animation.ColorKeyFrame)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]: ...
    Size = property(get_Size, None)
class CommonNavigationTransitionInfo(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    ClassId = 'Windows.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStaggerElementProperty(cls: Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsStaggerElement(cls: Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsStaggerElement(cls: Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
    IsStaggerElementProperty = property(get_IsStaggerElementProperty, None)
class ConnectedAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimation'
    @winrt_mixinmethod
    def add_Completed(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Media.Animation.ConnectedAnimation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryStart(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation, destination: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_IsScaleAnimationEnabled(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScaleAnimationEnabled(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryStartWithCoordinatedElements(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation2, destination: Windows.UI.Xaml.UIElement, coordinatedElements: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]) -> Boolean: ...
    @winrt_mixinmethod
    def SetAnimationComponent(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation2, component: Windows.UI.Xaml.Media.Animation.ConnectedAnimationComponent, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def get_Configuration(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation3) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration: ...
    @winrt_mixinmethod
    def put_Configuration(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimation3, value: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration) -> Void: ...
    IsScaleAnimationEnabled = property(get_IsScaleAnimationEnabled, put_IsScaleAnimationEnabled)
    Configuration = property(get_Configuration, put_Configuration)
ConnectedAnimationComponent = Int32
ConnectedAnimationComponent_OffsetX: ConnectedAnimationComponent = 0
ConnectedAnimationComponent_OffsetY: ConnectedAnimationComponent = 1
ConnectedAnimationComponent_CrossFade: ConnectedAnimationComponent = 2
ConnectedAnimationComponent_Scale: ConnectedAnimationComponent = 3
class ConnectedAnimationConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
class ConnectedAnimationService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimationService'
    @winrt_mixinmethod
    def get_DefaultDuration(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimationService) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DefaultDuration(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultEasingFunction(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimationService) -> Windows.UI.Composition.CompositionEasingFunction: ...
    @winrt_mixinmethod
    def put_DefaultEasingFunction(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, value: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_mixinmethod
    def PrepareToAnimate(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, key: WinRT_String, source: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_mixinmethod
    def GetAnimation(self: Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, key: WinRT_String) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Xaml.Media.Animation.IConnectedAnimationServiceStatics) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimationService: ...
    DefaultDuration = property(get_DefaultDuration, put_DefaultDuration)
    DefaultEasingFunction = property(get_DefaultEasingFunction, put_DefaultEasingFunction)
class ContentThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.ContentThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ContentThemeTransition: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IContentThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IContentThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: Windows.UI.Xaml.Media.Animation.IContentThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: Windows.UI.Xaml.Media.Animation.IContentThemeTransition, value: Double) -> Void: ...
    @winrt_classmethod
    def get_HorizontalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IContentThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IContentThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class ContinuumNavigationTransitionInfo(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    ClassId = 'Windows.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_ExitElement(self: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_ExitElement(self: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_ExitElementProperty(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsEntranceElementProperty(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsEntranceElement(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsEntranceElement(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsExitElementProperty(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsExitElement(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsExitElement(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ExitElementContainerProperty(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetExitElementContainer(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: Windows.UI.Xaml.Controls.ListViewBase) -> Boolean: ...
    @winrt_classmethod
    def SetExitElementContainer(cls: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: Windows.UI.Xaml.Controls.ListViewBase, value: Boolean) -> Void: ...
    ExitElement = property(get_ExitElement, put_ExitElement)
    ExitElementProperty = property(get_ExitElementProperty, None)
    IsEntranceElementProperty = property(get_IsEntranceElementProperty, None)
    IsExitElementProperty = property(get_IsExitElementProperty, None)
    ExitElementContainerProperty = property(get_ExitElementContainerProperty, None)
class CubicEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.CubicEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.CubicEase: ...
class DirectConnectedAnimationConfiguration(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
class DiscreteColorKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.DiscreteColorKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DiscreteColorKeyFrame: ...
class DiscreteDoubleKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame: ...
class DiscreteObjectKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ObjectKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame: ...
class DiscretePointKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.DiscretePointKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DiscretePointKeyFrame: ...
class DoubleAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.DoubleAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DoubleAnimation: ...
    @winrt_mixinmethod
    def get_From(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_From(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_To(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_By(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class DoubleAnimationUsingKeyFrames(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFramesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class DoubleKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(13)
    def get_Value(self) -> Double: ...
    @winrt_commethod(14)
    def put_Value(self, value: Double) -> Void: ...
    @winrt_commethod(15)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(16)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class DoubleKeyFrameCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], value: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], value: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Animation.DoubleKeyFrame)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], items: POINTER(Windows.UI.Xaml.Media.Animation.DoubleKeyFrame)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]: ...
    Size = property(get_Size, None)
class DragItemThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.DragItemThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DragItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class DragOverThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.DragOverThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DragOverThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ToOffset(self: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToOffset(self: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DirectionProperty(cls: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    ToOffset = property(get_ToOffset, put_ToOffset)
    Direction = property(get_Direction, put_Direction)
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToOffsetProperty = property(get_ToOffsetProperty, None)
    DirectionProperty = property(get_DirectionProperty, None)
class DrillInNavigationTransitionInfo(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    ClassId = 'Windows.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo: ...
class DrillInThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.DrillInThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DrillInThemeAnimation: ...
    @winrt_mixinmethod
    def get_EntranceTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EntranceTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EntranceTarget(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_EntranceTarget(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTarget(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ExitTarget(self: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_EntranceTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EntranceTargetProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class DrillOutThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.DrillOutThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DrillOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_EntranceTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EntranceTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EntranceTarget(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_EntranceTarget(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitTargetName(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTarget(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ExitTarget(self: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_EntranceTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EntranceTargetProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetProperty(cls: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class DropTargetItemThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class EasingColorKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.EasingColorKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.EasingColorKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class EasingDoubleKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.EasingDoubleKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.EasingDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class EasingFunctionBase(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(10)
    def get_EasingMode(self) -> Windows.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_commethod(11)
    def put_EasingMode(self, value: Windows.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_commethod(12)
    def Ease(self, normalizedTime: Double) -> Double: ...
    @winrt_classmethod
    def get_EasingModeProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingFunctionBaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
    EasingModeProperty = property(get_EasingModeProperty, None)
EasingMode = Int32
EasingMode_EaseOut: EasingMode = 0
EasingMode_EaseIn: EasingMode = 1
EasingMode_EaseInOut: EasingMode = 2
class EasingPointKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.EasingPointKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.EasingPointKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class EdgeUIThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.EdgeUIThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.EdgeUIThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    EdgeProperty = property(get_EdgeProperty, None)
class ElasticEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.ElasticEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ElasticEase: ...
    @winrt_mixinmethod
    def get_Oscillations(self: Windows.UI.Xaml.Media.Animation.IElasticEase) -> Int32: ...
    @winrt_mixinmethod
    def put_Oscillations(self: Windows.UI.Xaml.Media.Animation.IElasticEase, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Springiness(self: Windows.UI.Xaml.Media.Animation.IElasticEase) -> Double: ...
    @winrt_mixinmethod
    def put_Springiness(self: Windows.UI.Xaml.Media.Animation.IElasticEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OscillationsProperty(cls: Windows.UI.Xaml.Media.Animation.IElasticEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SpringinessProperty(cls: Windows.UI.Xaml.Media.Animation.IElasticEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Oscillations = property(get_Oscillations, put_Oscillations)
    Springiness = property(get_Springiness, put_Springiness)
    OscillationsProperty = property(get_OscillationsProperty, None)
    SpringinessProperty = property(get_SpringinessProperty, None)
class EntranceNavigationTransitionInfo(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    ClassId = 'Windows.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo: ...
    @winrt_classmethod
    def get_IsTargetElementProperty(cls: Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsTargetElement(cls: Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsTargetElement(cls: Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class EntranceThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.EntranceThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.EntranceThemeTransition: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class ExponentialEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.ExponentialEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ExponentialEase: ...
    @winrt_mixinmethod
    def get_Exponent(self: Windows.UI.Xaml.Media.Animation.IExponentialEase) -> Double: ...
    @winrt_mixinmethod
    def put_Exponent(self: Windows.UI.Xaml.Media.Animation.IExponentialEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_ExponentProperty(cls: Windows.UI.Xaml.Media.Animation.IExponentialEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Exponent = property(get_Exponent, put_Exponent)
    ExponentProperty = property(get_ExponentProperty, None)
class FadeInThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.FadeInThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.FadeInThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class FadeOutThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.FadeOutThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.FadeOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
FillBehavior = Int32
FillBehavior_HoldEnd: FillBehavior = 0
FillBehavior_Stop: FillBehavior = 1
class GravityConnectedAnimationConfiguration(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    @winrt_commethod(9)
    def get_IsShadowEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsShadowEnabled(self, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IAddDeleteThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('adec852e-4424-4dab-99-c1-3a-04-e3-6a-3c-48')
class IBackEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e47796e7-f805-4a8f-81-c9-38-e6-47-2c-aa-94')
    @winrt_commethod(6)
    def get_Amplitude(self) -> Double: ...
    @winrt_commethod(7)
    def put_Amplitude(self, value: Double) -> Void: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
class IBackEaseStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c70a2ff-a0a0-4786-92-6c-22-32-1f-8f-25-b7')
    @winrt_commethod(6)
    def get_AmplitudeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    AmplitudeProperty = property(get_AmplitudeProperty, None)
class IBasicConnectedAnimationConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e675f9b5-a4d6-5353-83-e6-c8-9e-7c-f8-d4-56')
class IBasicConnectedAnimationConfigurationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('95e6844a-4377-503c-be-e2-11-df-cd-55-70-e6')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration: ...
class IBeginStoryboard(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('64189fcd-49ec-4e52-a6-f6-55-32-4c-92-10-53')
    @winrt_commethod(6)
    def get_Storyboard(self) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(7)
    def put_Storyboard(self, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
class IBeginStoryboardStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('12cff18c-aa91-4c4a-b8-2f-df-34-fc-57-f9-4b')
    @winrt_commethod(6)
    def get_StoryboardProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    StoryboardProperty = property(get_StoryboardProperty, None)
class IBounceEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2bf1464e-fc71-47ed-85-a1-3b-a9-57-77-18-b4')
    @winrt_commethod(6)
    def get_Bounces(self) -> Int32: ...
    @winrt_commethod(7)
    def put_Bounces(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Bounciness(self) -> Double: ...
    @winrt_commethod(9)
    def put_Bounciness(self, value: Double) -> Void: ...
    Bounces = property(get_Bounces, put_Bounces)
    Bounciness = property(get_Bounciness, put_Bounciness)
class IBounceEaseStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c0701da2-4f73-41c9-b2-cb-2e-a3-10-51-07-ff')
    @winrt_commethod(6)
    def get_BouncesProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_BouncinessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    BouncesProperty = property(get_BouncesProperty, None)
    BouncinessProperty = property(get_BouncinessProperty, None)
class ICircleEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('53a3bdb2-9177-4e6e-a0-43-50-82-d8-89-ab-1f')
class IColorAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b8ae8a15-0f63-4694-94-67-bd-af-ac-12-53-ea')
    @winrt_commethod(6)
    def get_From(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(7)
    def put_From(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(8)
    def get_To(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(9)
    def put_To(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(10)
    def get_By(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(11)
    def put_By(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(12)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(14)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IColorAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('55eaf6e2-87e3-4f48-95-8f-85-5b-2f-9e-a9-ec')
    @winrt_commethod(6)
    def get_FromProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IColorAnimationUsingKeyFrames(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f5c82640-13c3-42aa-9a-e2-7e-6b-51-c9-2f-95')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IColorAnimationUsingKeyFramesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b4723cdc-96e9-48f9-8d-92-9b-64-8b-2f-1c-c6')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IColorKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b51d82d9-0910-4589-a2-84-b0-c9-20-58-58-e9')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Value(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
class IColorKeyFrameFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('769bd88a-9cfb-4a7d-96-c4-a1-e7-de-6f-db-4b')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrame: ...
class IColorKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c043ae99-210c-430f-9d-a5-df-10-82-69-20-55')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class ICommonNavigationTransitionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('50345692-a555-4624-a3-61-0a-91-c1-70-64-73')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class ICommonNavigationTransitionInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1e3efe33-50be-4443-88-3c-e5-62-72-01-c2-e5')
    @winrt_commethod(6)
    def get_IsStaggeringEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsStaggerElementProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetIsStaggerElement(self, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def SetIsStaggerElement(self, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
    IsStaggerElementProperty = property(get_IsStaggerElementProperty, None)
class IConnectedAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3518628c-f387-4c25-ac-98-44-e8-6c-3c-ad-f0')
    @winrt_commethod(6)
    def add_Completed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Media.Animation.ConnectedAnimation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TryStart(self, destination: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def Cancel(self) -> Void: ...
class IConnectedAnimation2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d2f8e5c-584b-4ddd-b6-68-97-38-91-43-14-59')
    @winrt_commethod(6)
    def get_IsScaleAnimationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsScaleAnimationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def TryStartWithCoordinatedElements(self, destination: Windows.UI.Xaml.UIElement, coordinatedElements: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]) -> Boolean: ...
    @winrt_commethod(9)
    def SetAnimationComponent(self, component: Windows.UI.Xaml.Media.Animation.ConnectedAnimationComponent, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    IsScaleAnimationEnabled = property(get_IsScaleAnimationEnabled, put_IsScaleAnimationEnabled)
class IConnectedAnimation3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6e3040c6-0430-59c0-a8-0c-cc-ee-d2-e7-78-dd')
    @winrt_commethod(6)
    def get_Configuration(self) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration: ...
    @winrt_commethod(7)
    def put_Configuration(self, value: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration) -> Void: ...
    Configuration = property(get_Configuration, put_Configuration)
class IConnectedAnimationConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('00218aae-cd8c-5651-92-a0-c1-db-95-c0-39-98')
class IConnectedAnimationConfigurationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('30f9b84b-dd7e-593e-bf-75-e9-59-dc-0e-c5-2a')
class IConnectedAnimationService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1c6875c9-19bb-4d47-b9-aa-66-c8-02-dc-b9-ff')
    @winrt_commethod(6)
    def get_DefaultDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DefaultDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultEasingFunction(self) -> Windows.UI.Composition.CompositionEasingFunction: ...
    @winrt_commethod(9)
    def put_DefaultEasingFunction(self, value: Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_commethod(10)
    def PrepareToAnimate(self, key: WinRT_String, source: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_commethod(11)
    def GetAnimation(self, key: WinRT_String) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    DefaultDuration = property(get_DefaultDuration, put_DefaultDuration)
    DefaultEasingFunction = property(get_DefaultEasingFunction, put_DefaultEasingFunction)
class IConnectedAnimationServiceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c7078ea5-d688-40e8-8f-90-96-a6-27-92-73-d2')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimationService: ...
class IContentThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f66fc5c3-5915-437d-8e-3b-ad-f8-e7-f0-ab-57')
    @winrt_commethod(6)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(7)
    def put_HorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_VerticalOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_VerticalOffset(self, value: Double) -> Void: ...
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
class IContentThemeTransitionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0e8ee385-9a42-4459-af-a9-33-7d-c4-1e-15-87')
    @winrt_commethod(6)
    def get_HorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class IContinuumNavigationTransitionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4be1dbad-8ba6-4004-84-38-8a-90-17-97-85-43')
    @winrt_commethod(6)
    def get_ExitElement(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_ExitElement(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    ExitElement = property(get_ExitElement, put_ExitElement)
class IContinuumNavigationTransitionInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3e25dd53-b18f-4bf1-b3-bc-92-f5-16-f2-99-03')
    @winrt_commethod(6)
    def get_ExitElementProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsEntranceElementProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetIsEntranceElement(self, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def SetIsEntranceElement(self, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsExitElementProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def GetIsExitElement(self, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(12)
    def SetIsExitElement(self, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_ExitElementContainerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def GetExitElementContainer(self, element: Windows.UI.Xaml.Controls.ListViewBase) -> Boolean: ...
    @winrt_commethod(15)
    def SetExitElementContainer(self, element: Windows.UI.Xaml.Controls.ListViewBase, value: Boolean) -> Void: ...
    ExitElementProperty = property(get_ExitElementProperty, None)
    IsEntranceElementProperty = property(get_IsEntranceElementProperty, None)
    IsExitElementProperty = property(get_IsExitElementProperty, None)
    ExitElementContainerProperty = property(get_ExitElementContainerProperty, None)
class ICubicEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1b94fc76-dad7-4354-b1-a2-79-69-fb-f6-a7-0d')
class IDirectConnectedAnimationConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ee5d736f-5738-5d86-b7-70-15-19-48-cf-36-5e')
class IDirectConnectedAnimationConfigurationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('059263e9-d2b3-5a77-9c-f4-e2-6d-8b-54-26-08')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration: ...
class IDiscreteColorKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('230c08f4-e062-4cb1-8e-2a-14-09-3d-73-ed-8c')
class IDiscreteDoubleKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f5f51f3a-ad11-49ce-8e-1c-08-fd-f1-44-74-46')
class IDiscreteObjectKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c7dcde89-f12d-4a9c-81-99-e7-a9-ec-e3-a4-73')
class IDiscretePointKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e0a9070d-4c42-4a90-98-3a-75-f5-a8-3a-2f-be')
class IDoubleAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e9f3d59-0f07-4bc9-97-7d-03-76-3f-f8-15-4f')
    @winrt_commethod(6)
    def get_From(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def put_From(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(8)
    def get_To(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def put_To(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(10)
    def get_By(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def put_By(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(12)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(14)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IDoubleAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e27a935d-f111-43b7-b8-24-83-2b-58-d7-78-6b')
    @winrt_commethod(6)
    def get_FromProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IDoubleAnimationUsingKeyFrames(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4fee628f-bfee-4f75-83-c2-a9-3b-39-48-84-73')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IDoubleAnimationUsingKeyFramesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('109bf2f6-c60f-49aa-ab-f6-f6-96-d4-92-11-6b')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IDoubleKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('674456fd-e81e-4f4e-b4-ad-0a-cf-ed-9e-cd-68')
    @winrt_commethod(6)
    def get_Value(self) -> Double: ...
    @winrt_commethod(7)
    def put_Value(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
class IDoubleKeyFrameFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ac97dec3-7538-40b9-b1-52-69-6f-7f-bf-47-22')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
class IDoubleKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('324641b0-7d37-427a-ad-eb-43-f3-8b-b6-1a-4d')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class IDragItemThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c7d5db5-7ed6-4949-b4-e6-a7-8c-9f-4f-97-8d')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDragItemThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6218b9f5-013a-4fb1-86-fc-92-bc-4e-8d-02-41')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IDragOverThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72f762f7-7e51-4a6b-b9-37-dc-4b-4c-1c-54-58')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ToOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_ToOffset(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_Direction(self) -> Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(11)
    def put_Direction(self, value: Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
    ToOffset = property(get_ToOffset, put_ToOffset)
    Direction = property(get_Direction, put_Direction)
class IDragOverThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('146ffe57-3c9d-41d9-a5-ff-8d-72-39-51-68-10')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_DirectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToOffsetProperty = property(get_ToOffsetProperty, None)
    DirectionProperty = property(get_DirectionProperty, None)
class IDrillInNavigationTransitionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3b86201a-45d3-463b-93-9e-c8-59-5f-43-9b-cc')
class IDrillInThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b090b824-f1d2-41b8-87-ba-78-03-41-26-59-4c')
    @winrt_commethod(6)
    def get_EntranceTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EntranceTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_EntranceTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_EntranceTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ExitTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ExitTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ExitTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ExitTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
class IDrillInThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c61fe488-a17a-4b11-b5-3b-a4-f1-a0-7d-4b-a9')
    @winrt_commethod(6)
    def get_EntranceTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EntranceTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ExitTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ExitTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class IDrillOutThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d890ccdf-06d3-4f7e-8e-4a-4f-b7-6e-25-61-39')
    @winrt_commethod(6)
    def get_EntranceTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EntranceTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_EntranceTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_EntranceTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ExitTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ExitTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ExitTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ExitTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
class IDrillOutThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('beb5db9b-2617-4888-80-dd-72-fa-7b-b6-fa-c3')
    @winrt_commethod(6)
    def get_EntranceTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EntranceTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ExitTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ExitTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class IDropTargetItemThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1881c968-1824-462b-87-e8-c3-57-21-2b-97-7b')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDropTargetItemThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae80f486-2e56-4513-bf-18-d7-74-70-16-4a-e5')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IEasingColorKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c733d630-f4b9-4934-9b-dd-27-ac-5e-d1-cf-d8')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingColorKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f3837fc-8e3d-4522-9b-0f-00-3d-b8-60-98-51')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingDoubleKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('965adb8d-9a54-4108-b4-ff-b5-a5-21-2c-b3-38')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingDoubleKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c8d3d845-dbae-4e5b-8b-84-d9-53-73-98-e5-b1')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingFunctionBase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c108383f-2c02-4151-8e-cd-68-dd-aa-3f-0d-9b')
    @winrt_commethod(6)
    def get_EasingMode(self) -> Windows.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_commethod(7)
    def put_EasingMode(self, value: Windows.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_commethod(8)
    def Ease(self, normalizedTime: Double) -> Double: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
class IEasingFunctionBaseFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1830fe6a-f01b-43e0-b6-1f-b4-52-a1-c6-6f-d2')
class IEasingFunctionBaseStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2a5031aa-2c50-4a1d-bb-04-d7-5e-07-b7-15-48')
    @winrt_commethod(6)
    def get_EasingModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingModeProperty = property(get_EasingModeProperty, None)
class IEasingPointKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b3c91380-6868-4225-a7-0b-39-81-cc-0b-29-47')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingPointKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e22dbfc4-080c-402c-a6-b5-f4-8d-0a-98-11-6b')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEdgeUIThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5c86c19b-49d7-19ec-cf-19-83-a7-3c-6d-e7-5e')
    @winrt_commethod(6)
    def get_Edge(self) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IEdgeUIThemeTransitionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('16a2b13b-4705-302b-27-c6-2a-ac-92-f6-45-ac')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IElasticEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef5ba58c-b0b6-4a6c-9c-a8-fb-42-33-f1-24-59')
    @winrt_commethod(6)
    def get_Oscillations(self) -> Int32: ...
    @winrt_commethod(7)
    def put_Oscillations(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Springiness(self) -> Double: ...
    @winrt_commethod(9)
    def put_Springiness(self, value: Double) -> Void: ...
    Oscillations = property(get_Oscillations, put_Oscillations)
    Springiness = property(get_Springiness, put_Springiness)
class IElasticEaseStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a9f566ec-fe9c-4b2b-8e-52-bb-78-5d-56-21-85')
    @winrt_commethod(6)
    def get_OscillationsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SpringinessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    OscillationsProperty = property(get_OscillationsProperty, None)
    SpringinessProperty = property(get_SpringinessProperty, None)
class IEntranceNavigationTransitionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('720a256b-1c8a-41ee-82-ec-8a-87-c0-cf-47-da')
class IEntranceNavigationTransitionInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f948c27a-40c9-469f-8f-33-bf-45-c8-81-1f-21')
    @winrt_commethod(6)
    def get_IsTargetElementProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsTargetElement(self, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsTargetElement(self, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class IEntranceThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('07698c09-a8e3-419a-a0-1d-74-10-a0-ae-8e-c8')
    @winrt_commethod(6)
    def get_FromHorizontalOffset(self) -> Double: ...
    @winrt_commethod(7)
    def put_FromHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_FromVerticalOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_FromVerticalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class IEntranceThemeTransitionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('37cc0577-ff98-4aed-b8-6e-5e-c2-37-02-f8-77')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsStaggeringEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class IExponentialEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7cb9e41d-f0bb-4bca-9d-a5-9b-a3-a1-17-34-c4')
    @winrt_commethod(6)
    def get_Exponent(self) -> Double: ...
    @winrt_commethod(7)
    def put_Exponent(self, value: Double) -> Void: ...
    Exponent = property(get_Exponent, put_Exponent)
class IExponentialEaseStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f37ee7e3-a761-4352-9a-d6-70-79-45-67-58-1a')
    @winrt_commethod(6)
    def get_ExponentProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ExponentProperty = property(get_ExponentProperty, None)
class IFadeInThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6d4bc8f5-a918-4477-80-78-55-4c-68-81-2a-b8')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeInThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7f0117e1-bea9-4923-b2-3a-0d-df-4d-7b-87-37')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IFadeOutThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('89276ba9-ffd4-45b6-9b-9a-ce-d4-89-51-e7-12')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeOutThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fe17a81a-4168-4f68-a2-8c-e5-dd-98-cf-68-0f')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IGravityConnectedAnimationConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c751a4b7-0459-5142-b8-91-ae-aa-c1-d4-18-22')
class IGravityConnectedAnimationConfiguration2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('62333add-aed4-5fed-95-ff-d1-28-ac-ce-8b-e4')
    @winrt_commethod(6)
    def get_IsShadowEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsShadowEnabled(self, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IGravityConnectedAnimationConfigurationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e822c41f-3656-5090-92-f5-c2-17-ea-ac-b6-82')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration: ...
class IKeySpline(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('77a163bb-d5ca-4a32-ba-0b-7d-ff-98-8e-58-a0')
    @winrt_commethod(6)
    def get_ControlPoint1(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_ControlPoint1(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_ControlPoint2(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_ControlPoint2(self, value: Windows.Foundation.Point) -> Void: ...
    ControlPoint1 = property(get_ControlPoint1, put_ControlPoint1)
    ControlPoint2 = property(get_ControlPoint2, put_ControlPoint2)
class IKeyTimeHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3643e480-4823-466a-ab-e5-5e-79-c8-ed-77-ed')
class IKeyTimeHelperStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7fa2612c-22a9-45e9-9a-f7-c7-41-6e-ff-f7-a5')
    @winrt_commethod(6)
    def FromTimeSpan(self, timeSpan: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
class ILinearColorKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('66fdb6ef-ac81-4611-b1-d2-61-f5-45-98-3f-03')
class ILinearDoubleKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8efdf265-9a7b-431d-8f-0c-14-c5-6b-5e-a4-d9')
class ILinearPointKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e7c9b8ef-af24-49ee-84-f1-a8-66-00-a4-e3-19')
class INavigationThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8833848c-4eb7-41f2-87-99-9e-ef-0a-21-3b-73')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfo(self) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(7)
    def put_DefaultNavigationTransitionInfo(self, value: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
class INavigationThemeTransitionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ea2f06e0-5e60-4f8e-bc-af-43-14-87-a2-94-ab')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfoProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class INavigationTransitionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a9b05091-ae4a-4372-86-25-21-b7-a8-b9-8c-a4')
class INavigationTransitionInfoFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('edf4f8d5-af63-4fab-9d-4a-87-92-7f-82-dd-6b')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
class INavigationTransitionInfoOverrides(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d9517e6a-a9d0-4bf7-9d-b0-46-33-a6-9d-af-f2')
    @winrt_commethod(6)
    def GetNavigationStateCore(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def SetNavigationStateCore(self, navigationState: WinRT_String) -> Void: ...
class IObjectAnimationUsingKeyFrames(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('334a2d92-b74a-4c64-b9-a6-58-bc-fa-31-4f-22')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IObjectAnimationUsingKeyFramesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb736182-6af1-49a3-97-b6-78-3e-d9-74-00-fe')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IObjectKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9852a851-8593-48ee-a6-a4-d5-d4-72-0f-02-9a')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def put_Value(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
class IObjectKeyFrameFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1626143e-3e6d-44d8-9b-9a-04-ae-a7-0f-84-92')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
class IObjectKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2cd6ab00-5319-4286-8e-ed-4e-75-5e-a0-cf-9c')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class IPaneThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4708eb8e-4bfc-ee46-d4-f9-70-8d-ef-3f-bb-2b')
    @winrt_commethod(6)
    def get_Edge(self) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IPaneThemeTransitionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('316b382f-4be4-1797-b4-5c-cd-90-0b-be-0c-aa')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IPointAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('30f04312-7726-4f88-b8-e2-2f-a5-45-18-96-3b')
    @winrt_commethod(6)
    def get_From(self) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_commethod(7)
    def put_From(self, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(8)
    def get_To(self) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_commethod(9)
    def put_To(self, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(10)
    def get_By(self) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_commethod(11)
    def put_By(self, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(12)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(14)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IPointAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f99b356-e737-408b-a0-fd-32-78-26-d3-22-55')
    @winrt_commethod(6)
    def get_FromProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IPointAnimationUsingKeyFrames(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9b944f72-446a-41d0-a1-29-41-a6-20-f4-59-5d')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IPointAnimationUsingKeyFramesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f454c87-2390-46ea-ba-a7-76-2f-4b-c3-0d-04')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IPointKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fcc88d01-7f82-4dae-80-26-7b-7e-08-68-78-b3')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Value(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
class IPointKeyFrameFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cb214bdf-426a-4392-83-55-c2-ae-52-85-26-23')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.PointKeyFrame: ...
class IPointKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('95cf1b27-7965-4bec-b9-fb-fb-e9-4b-65-51-8e')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class IPointerDownThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b58e714e-c49d-4788-a2-33-0a-e8-5d-99-dd-5a')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerDownThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63a7cb7b-6d46-4494-b9-4a-e7-2f-3b-49-2a-61')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPointerUpThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e9e9d07d-6340-4828-ad-12-69-06-94-b9-91-0b')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerUpThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7c618f9c-7992-4139-8b-fc-08-83-b9-72-7a-7e')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopInThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('196938c1-1c07-4c28-88-47-f9-f0-55-b3-28-55')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_FromHorizontalOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_FromHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_FromVerticalOffset(self) -> Double: ...
    @winrt_commethod(11)
    def put_FromVerticalOffset(self, value: Double) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
class IPopInThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('efaa99d3-218a-4701-97-7f-f1-bf-ae-8b-a6-49')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IPopOutThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4786ab49-0e48-4e81-a2-e5-cc-5a-a1-9e-48-d3')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPopOutThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1d492c09-03c1-4490-99-dc-90-9f-ea-b3-57-fb')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopupThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('47843552-4283-545e-c7-91-26-8d-ca-22-ce-4b')
    @winrt_commethod(6)
    def get_FromHorizontalOffset(self) -> Double: ...
    @winrt_commethod(7)
    def put_FromHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_FromVerticalOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_FromVerticalOffset(self, value: Double) -> Void: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
class IPopupThemeTransitionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e5a1640e-490d-1505-9f-6b-8f-af-c0-44-de-c5')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IPowerEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69c80579-eedf-405b-86-80-d9-60-68-80-c9-37')
    @winrt_commethod(6)
    def get_Power(self) -> Double: ...
    @winrt_commethod(7)
    def put_Power(self, value: Double) -> Void: ...
    Power = property(get_Power, put_Power)
class IPowerEaseStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a5955103-91a2-460c-9c-41-d2-8f-6a-93-9b-da')
    @winrt_commethod(6)
    def get_PowerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PowerProperty = property(get_PowerProperty, None)
class IQuadraticEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e1510e91-ef6d-44f0-80-3d-68-d1-6d-e0-dd-fc')
class IQuarticEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e8698814-fe42-4a05-b5-b8-08-1f-41-15-78-15')
class IQuinticEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('92ee793b-3c49-4108-aa-11-ab-78-66-03-da-21')
class IReorderThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f2065c6c-d052-4ad1-83-62-b7-1b-36-df-74-97')
class IRepeatBehaviorHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6863ab72-4997-47f9-87-ad-37-ef-b7-59-93-ea')
class IRepeatBehaviorHelperStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7a795033-79f3-4dd9-b2-67-9c-f5-0f-b5-1f-84')
    @winrt_commethod(6)
    def get_Forever(self) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(7)
    def FromCount(self, count: Double) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(8)
    def FromDuration(self, duration: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(9)
    def GetHasCount(self, target: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_commethod(10)
    def GetHasDuration(self, target: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_commethod(11)
    def Equals(self, target: Windows.UI.Xaml.Media.Animation.RepeatBehavior, value: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    Forever = property(get_Forever, None)
class IRepositionThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ecda24e8-8945-4949-a1-bf-62-10-99-65-a7-e9')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_FromHorizontalOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_FromHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_FromVerticalOffset(self) -> Double: ...
    @winrt_commethod(11)
    def put_FromVerticalOffset(self, value: Double) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
class IRepositionThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4d92b1b1-860b-4bf9-a5-9d-1e-b1-cc-be-8f-e0')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IRepositionThemeTransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('88329b82-98f3-455a-ac-53-2e-70-83-b6-e2-2c')
class IRepositionThemeTransition2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cebfe864-dbea-4404-8e-6e-de-55-ad-a7-52-39')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class IRepositionThemeTransitionStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9240e930-0a19-468b-8c-2a-68-fa-b4-50-00-27')
    @winrt_commethod(6)
    def get_IsStaggeringEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class ISineEase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a9382962-230b-49da-9e-0d-66-49-87-89-23-43')
class ISlideNavigationTransitionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d6ac9d77-2e03-405f-80-ed-e6-2b-ee-f3-66-8f')
class ISlideNavigationTransitionInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('90e2d9c0-5c81-5001-80-13-4f-bf-ea-4b-f1-39')
    @winrt_commethod(6)
    def get_Effect(self) -> Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_commethod(7)
    def put_Effect(self, value: Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    Effect = property(get_Effect, put_Effect)
class ISlideNavigationTransitionInfoStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8a861baa-981a-5ace-9f-85-cb-7f-de-64-8a-67')
    @winrt_commethod(6)
    def get_EffectProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EffectProperty = property(get_EffectProperty, None)
class ISplineColorKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1a4a5941-1fe0-473a-8e-fe-43-16-d8-c8-62-29')
    @winrt_commethod(6)
    def get_KeySpline(self) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineColorKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('61d1d997-8589-4f2f-8f-bb-7d-03-ed-c9-8d-d3')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplineDoubleKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('00d72d38-6b2b-4843-83-8e-c8-b1-15-ee-c8-01')
    @winrt_commethod(6)
    def get_KeySpline(self) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineDoubleKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('060a8ffc-975f-4e4e-9e-c7-13-c5-ae-e0-20-62')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplinePointKeyFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0f19f306-7036-494f-bc-3c-78-0d-f0-cc-52-4a')
    @winrt_commethod(6)
    def get_KeySpline(self) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplinePointKeyFrameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e97a32c2-0a7a-4766-95-cb-0d-69-26-11-cb-4c')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplitCloseThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4f799518-ff39-4e90-bb-74-2a-bd-56-02-74-02')
    @winrt_commethod(6)
    def get_OpenedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_OpenedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_OpenedTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_OpenedTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ClosedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ClosedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ClosedTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ClosedTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_ContentTargetName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ContentTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_ContentTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(17)
    def put_ContentTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(18)
    def get_OpenedLength(self) -> Double: ...
    @winrt_commethod(19)
    def put_OpenedLength(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_ClosedLength(self) -> Double: ...
    @winrt_commethod(21)
    def put_ClosedLength(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_OffsetFromCenter(self) -> Double: ...
    @winrt_commethod(23)
    def put_OffsetFromCenter(self, value: Double) -> Void: ...
    @winrt_commethod(24)
    def get_ContentTranslationDirection(self) -> Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(25)
    def put_ContentTranslationDirection(self, value: Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_commethod(26)
    def get_ContentTranslationOffset(self) -> Double: ...
    @winrt_commethod(27)
    def put_ContentTranslationOffset(self, value: Double) -> Void: ...
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
class ISplitCloseThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7aa94de9-cc9b-4e90-a1-1a-00-50-a2-21-6a-9e')
    @winrt_commethod(6)
    def get_OpenedTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OpenedTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ClosedTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ClosedTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ContentTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ContentTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_OpenedLengthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ClosedLengthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_OffsetFromCenterProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ContentTranslationDirectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_ContentTranslationOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    OpenedTargetProperty = property(get_OpenedTargetProperty, None)
    ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    ContentTargetProperty = property(get_ContentTargetProperty, None)
    OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
class ISplitOpenThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('785fd7aa-5456-4639-8f-d2-26-ba-e6-a5-ff-e4')
    @winrt_commethod(6)
    def get_OpenedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_OpenedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_OpenedTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_OpenedTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ClosedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ClosedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ClosedTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ClosedTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_ContentTargetName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ContentTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_ContentTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(17)
    def put_ContentTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(18)
    def get_OpenedLength(self) -> Double: ...
    @winrt_commethod(19)
    def put_OpenedLength(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_ClosedLength(self) -> Double: ...
    @winrt_commethod(21)
    def put_ClosedLength(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_OffsetFromCenter(self) -> Double: ...
    @winrt_commethod(23)
    def put_OffsetFromCenter(self, value: Double) -> Void: ...
    @winrt_commethod(24)
    def get_ContentTranslationDirection(self) -> Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(25)
    def put_ContentTranslationDirection(self, value: Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_commethod(26)
    def get_ContentTranslationOffset(self) -> Double: ...
    @winrt_commethod(27)
    def put_ContentTranslationOffset(self, value: Double) -> Void: ...
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
class ISplitOpenThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8d4cfa89-3a91-458d-b0-fb-4c-ad-62-5c-bf-8d')
    @winrt_commethod(6)
    def get_OpenedTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OpenedTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ClosedTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ClosedTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ContentTargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ContentTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_OpenedLengthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ClosedLengthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_OffsetFromCenterProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ContentTranslationDirectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_ContentTranslationOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    OpenedTargetProperty = property(get_OpenedTargetProperty, None)
    ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    ContentTargetProperty = property(get_ContentTargetProperty, None)
    OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
class IStoryboard(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d45c1e6e-3594-460e-98-1a-32-27-1b-d3-aa-06')
    @winrt_commethod(6)
    def get_Children(self) -> Windows.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_commethod(7)
    def Seek(self, offset: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def Begin(self) -> Void: ...
    @winrt_commethod(10)
    def Pause(self) -> Void: ...
    @winrt_commethod(11)
    def Resume(self) -> Void: ...
    @winrt_commethod(12)
    def GetCurrentState(self) -> Windows.UI.Xaml.Media.Animation.ClockState: ...
    @winrt_commethod(13)
    def GetCurrentTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def SeekAlignedToLastTick(self, offset: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(15)
    def SkipToFill(self) -> Void: ...
    Children = property(get_Children, None)
class IStoryboardStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d82f07d8-73d5-4379-bd-48-7e-05-18-4a-8b-ad')
    @winrt_commethod(6)
    def get_TargetPropertyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetTargetProperty(self, element: Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetTargetProperty(self, element: Windows.UI.Xaml.Media.Animation.Timeline, path: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetTargetName(self, element: Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetTargetName(self, element: Windows.UI.Xaml.Media.Animation.Timeline, name: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def SetTarget(self, timeline: Windows.UI.Xaml.Media.Animation.Timeline, target: Windows.UI.Xaml.DependencyObject) -> Void: ...
    TargetPropertyProperty = property(get_TargetPropertyProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class ISuppressNavigationTransitionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('244d7b0c-b1b7-4871-9d-3e-d5-62-03-a3-a5-b4')
class ISwipeBackThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a38a4214-0bca-4d2d-95-f7-ce-ba-57-fb-af-60')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_FromHorizontalOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_FromHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_FromVerticalOffset(self) -> Double: ...
    @winrt_commethod(11)
    def put_FromVerticalOffset(self, value: Double) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
class ISwipeBackThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('693f31bf-4da6-468a-8c-e0-99-6c-9a-ad-42-e0')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class ISwipeHintThemeAnimation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cdd067c0-580e-4e40-be-98-f2-02-d3-d8-43-65')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ToHorizontalOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_ToHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ToVerticalOffset(self) -> Double: ...
    @winrt_commethod(11)
    def put_ToVerticalOffset(self, value: Double) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
    ToHorizontalOffset = property(get_ToHorizontalOffset, put_ToHorizontalOffset)
    ToVerticalOffset = property(get_ToVerticalOffset, put_ToVerticalOffset)
class ISwipeHintThemeAnimationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('23d61a57-9115-4d63-b0-4a-b8-9f-1c-74-4d-c0')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ToVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToHorizontalOffsetProperty = property(get_ToHorizontalOffsetProperty, None)
    ToVerticalOffsetProperty = property(get_ToVerticalOffsetProperty, None)
class ITimeline(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0bc465dc-be4d-4d0d-95-49-22-08-b7-15-f4-0d')
    @winrt_commethod(6)
    def get_AutoReverse(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AutoReverse(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_BeginTime(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def put_BeginTime(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(10)
    def get_Duration(self) -> Windows.UI.Xaml.Duration: ...
    @winrt_commethod(11)
    def put_Duration(self, value: Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_commethod(12)
    def get_SpeedRatio(self) -> Double: ...
    @winrt_commethod(13)
    def put_SpeedRatio(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_FillBehavior(self) -> Windows.UI.Xaml.Media.Animation.FillBehavior: ...
    @winrt_commethod(15)
    def put_FillBehavior(self, value: Windows.UI.Xaml.Media.Animation.FillBehavior) -> Void: ...
    @winrt_commethod(16)
    def get_RepeatBehavior(self) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(17)
    def put_RepeatBehavior(self, value: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Void: ...
    @winrt_commethod(18)
    def add_Completed(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoReverse = property(get_AutoReverse, put_AutoReverse)
    BeginTime = property(get_BeginTime, put_BeginTime)
    Duration = property(get_Duration, put_Duration)
    SpeedRatio = property(get_SpeedRatio, put_SpeedRatio)
    FillBehavior = property(get_FillBehavior, put_FillBehavior)
    RepeatBehavior = property(get_RepeatBehavior, put_RepeatBehavior)
class ITimelineFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1d56bb07-bda4-478b-8a-da-eb-04-d5-80-cd-5e')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.Timeline: ...
class ITimelineStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a902ed4e-ef10-4d6f-9a-40-93-cb-88-95-f4-e5')
    @winrt_commethod(6)
    def get_AllowDependentAnimations(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowDependentAnimations(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AutoReverseProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_BeginTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DurationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_SpeedRatioProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_FillBehaviorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_RepeatBehaviorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    AllowDependentAnimations = property(get_AllowDependentAnimations, put_AllowDependentAnimations)
    AutoReverseProperty = property(get_AutoReverseProperty, None)
    BeginTimeProperty = property(get_BeginTimeProperty, None)
    DurationProperty = property(get_DurationProperty, None)
    SpeedRatioProperty = property(get_SpeedRatioProperty, None)
    FillBehaviorProperty = property(get_FillBehaviorProperty, None)
    RepeatBehaviorProperty = property(get_RepeatBehaviorProperty, None)
class ITransition(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c677c7c-01d0-4dce-b3-33-97-6f-93-31-2b-08')
class ITransitionFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dc9ab2cf-3bc9-44aa-b3-fc-88-3a-83-23-3a-2c')
class KeySpline(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Media.Animation.KeySpline'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def get_ControlPoint1(self: Windows.UI.Xaml.Media.Animation.IKeySpline) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_ControlPoint1(self: Windows.UI.Xaml.Media.Animation.IKeySpline, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_ControlPoint2(self: Windows.UI.Xaml.Media.Animation.IKeySpline) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_ControlPoint2(self: Windows.UI.Xaml.Media.Animation.IKeySpline, value: Windows.Foundation.Point) -> Void: ...
    ControlPoint1 = property(get_ControlPoint1, put_ControlPoint1)
    ControlPoint2 = property(get_ControlPoint2, put_ControlPoint2)
class KeyTime(EasyCastStructure):
    TimeSpan: Windows.Foundation.TimeSpan
class KeyTimeHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.KeyTimeHelper'
    @winrt_classmethod
    def FromTimeSpan(cls: Windows.UI.Xaml.Media.Animation.IKeyTimeHelperStatics, timeSpan: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
class LinearColorKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.LinearColorKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.LinearColorKeyFrame: ...
class LinearDoubleKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.LinearDoubleKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.LinearDoubleKeyFrame: ...
class LinearPointKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.LinearPointKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.LinearPointKeyFrame: ...
class NavigationThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.NavigationThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.NavigationThemeTransition: ...
    @winrt_mixinmethod
    def get_DefaultNavigationTransitionInfo(self: Windows.UI.Xaml.Media.Animation.INavigationThemeTransition) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def put_DefaultNavigationTransitionInfo(self: Windows.UI.Xaml.Media.Animation.INavigationThemeTransition, value: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    @winrt_classmethod
    def get_DefaultNavigationTransitionInfoProperty(cls: Windows.UI.Xaml.Media.Animation.INavigationThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
    DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class NavigationTransitionInfo(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(9)
    def GetNavigationStateCore(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def SetNavigationStateCore(self, navigationState: WinRT_String) -> Void: ...
class ObjectAnimationUsingKeyFrames(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFramesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class ObjectKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(13)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(14)
    def put_Value(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(15)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(16)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class ObjectKeyFrameCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], value: Windows.UI.Xaml.Media.Animation.ObjectKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], value: Windows.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Animation.ObjectKeyFrame)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], items: POINTER(Windows.UI.Xaml.Media.Animation.ObjectKeyFrame)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]: ...
    Size = property(get_Size, None)
class PaneThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.PaneThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PaneThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: Windows.UI.Xaml.Media.Animation.IPaneThemeTransition) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: Windows.UI.Xaml.Media.Animation.IPaneThemeTransition, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: Windows.UI.Xaml.Media.Animation.IPaneThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    EdgeProperty = property(get_EdgeProperty, None)
class PointAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.PointAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PointAnimation: ...
    @winrt_mixinmethod
    def get_From(self: Windows.UI.Xaml.Media.Animation.IPointAnimation) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_From(self: Windows.UI.Xaml.Media.Animation.IPointAnimation, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: Windows.UI.Xaml.Media.Animation.IPointAnimation) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_To(self: Windows.UI.Xaml.Media.Animation.IPointAnimation, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: Windows.UI.Xaml.Media.Animation.IPointAnimation) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_By(self: Windows.UI.Xaml.Media.Animation.IPointAnimation, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IPointAnimation) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IPointAnimation, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IPointAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IPointAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class PointAnimationUsingKeyFrames(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames) -> Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFramesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class PointKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(13)
    def get_Value(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(14)
    def put_Value(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(15)
    def get_KeyTime(self) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(16)
    def put_KeyTime(self, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class PointKeyFrameCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32) -> Windows.UI.Xaml.Media.Animation.PointKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Animation.PointKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], value: Windows.UI.Xaml.Media.Animation.PointKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32, value: Windows.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], value: Windows.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Animation.PointKeyFrame)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame], items: POINTER(Windows.UI.Xaml.Media.Animation.PointKeyFrame)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Animation.PointKeyFrame]: ...
    Size = property(get_Size, None)
class PointerDownThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.PointerDownThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PointerDownThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class PointerUpThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.PointerUpThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PointerUpThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class PopInThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.PopInThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PopInThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class PopOutThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.PopOutThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PopOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class PopupThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.PopupThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PopupThemeTransition: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IPopupThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IPopupThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IPopupThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IPopupThemeTransition, value: Double) -> Void: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class PowerEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.PowerEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.PowerEase: ...
    @winrt_mixinmethod
    def get_Power(self: Windows.UI.Xaml.Media.Animation.IPowerEase) -> Double: ...
    @winrt_mixinmethod
    def put_Power(self: Windows.UI.Xaml.Media.Animation.IPowerEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_PowerProperty(cls: Windows.UI.Xaml.Media.Animation.IPowerEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Power = property(get_Power, put_Power)
    PowerProperty = property(get_PowerProperty, None)
class QuadraticEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.QuadraticEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.QuadraticEase: ...
class QuarticEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.QuarticEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.QuarticEase: ...
class QuinticEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.QuinticEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.QuinticEase: ...
class ReorderThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.ReorderThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.ReorderThemeTransition: ...
class RepeatBehavior(EasyCastStructure):
    Count: Double
    Duration: Windows.Foundation.TimeSpan
    Type: Windows.UI.Xaml.Media.Animation.RepeatBehaviorType
class RepeatBehaviorHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.RepeatBehaviorHelper'
    @winrt_classmethod
    def get_Forever(cls: Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def FromCount(cls: Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, count: Double) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def FromDuration(cls: Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, duration: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def GetHasCount(cls: Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_classmethod
    def GetHasDuration(cls: Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: Windows.UI.Xaml.Media.Animation.RepeatBehavior, value: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    Forever = property(get_Forever, None)
RepeatBehaviorType = Int32
RepeatBehaviorType_Count: RepeatBehaviorType = 0
RepeatBehaviorType_Duration: RepeatBehaviorType = 1
RepeatBehaviorType_Forever: RepeatBehaviorType = 2
class RepositionThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.RepositionThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.RepositionThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class RepositionThemeTransition(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    ClassId = 'Windows.UI.Xaml.Media.Animation.RepositionThemeTransition'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.RepositionThemeTransition: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: Windows.UI.Xaml.Media.Animation.IRepositionThemeTransitionStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class SineEase(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    ClassId = 'Windows.UI.Xaml.Media.Animation.SineEase'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SineEase: ...
SlideNavigationTransitionEffect = Int32
SlideNavigationTransitionEffect_FromBottom: SlideNavigationTransitionEffect = 0
SlideNavigationTransitionEffect_FromLeft: SlideNavigationTransitionEffect = 1
SlideNavigationTransitionEffect_FromRight: SlideNavigationTransitionEffect = 2
class SlideNavigationTransitionInfo(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    ClassId = 'Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_Effect(self: Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2) -> Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_mixinmethod
    def put_Effect(self: Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2, value: Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    @winrt_classmethod
    def get_EffectProperty(cls: Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfoStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    Effect = property(get_Effect, put_Effect)
    EffectProperty = property(get_EffectProperty, None)
class SplineColorKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.SplineColorKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SplineColorKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    KeySplineProperty = property(get_KeySplineProperty, None)
class SplineDoubleKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.SplineDoubleKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SplineDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    KeySplineProperty = property(get_KeySplineProperty, None)
class SplinePointKeyFrame(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    ClassId = 'Windows.UI.Xaml.Media.Animation.SplinePointKeyFrame'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SplinePointKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    KeySplineProperty = property(get_KeySplineProperty, None)
class SplitCloseThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.SplitCloseThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SplitCloseThemeAnimation: ...
    @winrt_mixinmethod
    def get_OpenedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OpenedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OpenedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClosedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ClosedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTarget(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ContentTarget(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedLength(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OpenedLength(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedLength(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ClosedLength(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetFromCenter(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetFromCenter(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationDirection(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_ContentTranslationDirection(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationOffset(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ContentTranslationOffset(self: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OpenedTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedTargetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedLengthProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedLengthProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetFromCenterProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationDirectionProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
    OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    OpenedTargetProperty = property(get_OpenedTargetProperty, None)
    ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    ContentTargetProperty = property(get_ContentTargetProperty, None)
    OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
class SplitOpenThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.SplitOpenThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SplitOpenThemeAnimation: ...
    @winrt_mixinmethod
    def get_OpenedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OpenedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OpenedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClosedTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ClosedTarget(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentTargetName(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTarget(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ContentTarget(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedLength(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OpenedLength(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedLength(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ClosedLength(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetFromCenter(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetFromCenter(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationDirection(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_ContentTranslationDirection(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationOffset(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ContentTranslationOffset(self: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OpenedTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedTargetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedLengthProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedLengthProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetFromCenterProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationDirectionProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
    OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    OpenedTargetProperty = property(get_OpenedTargetProperty, None)
    ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    ContentTargetProperty = property(get_ContentTargetProperty, None)
    OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
class Storyboard(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.Storyboard'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Windows.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_mixinmethod
    def Seek(self: Windows.UI.Xaml.Media.Animation.IStoryboard, offset: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Begin(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentState(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Windows.UI.Xaml.Media.Animation.ClockState: ...
    @winrt_mixinmethod
    def GetCurrentTime(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SeekAlignedToLastTick(self: Windows.UI.Xaml.Media.Animation.IStoryboard, offset: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SkipToFill(self: Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_classmethod
    def get_TargetPropertyProperty(cls: Windows.UI.Xaml.Media.Animation.IStoryboardStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTargetProperty(cls: Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_classmethod
    def SetTargetProperty(cls: Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: Windows.UI.Xaml.Media.Animation.Timeline, path: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IStoryboardStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTargetName(cls: Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_classmethod
    def SetTargetName(cls: Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: Windows.UI.Xaml.Media.Animation.Timeline, name: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetTarget(cls: Windows.UI.Xaml.Media.Animation.IStoryboardStatics, timeline: Windows.UI.Xaml.Media.Animation.Timeline, target: Windows.UI.Xaml.DependencyObject) -> Void: ...
    Children = property(get_Children, None)
    TargetPropertyProperty = property(get_TargetPropertyProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class SuppressNavigationTransitionInfo(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    ClassId = 'Windows.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo: ...
class SwipeBackThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.SwipeBackThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SwipeBackThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class SwipeHintThemeAnimation(c_void_p):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    ClassId = 'Windows.UI.Xaml.Media.Animation.SwipeHintThemeAnimation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.SwipeHintThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ToHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToHorizontalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ToVerticalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToVerticalOffset(self: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToHorizontalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToVerticalOffsetProperty(cls: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    ToHorizontalOffset = property(get_ToHorizontalOffset, put_ToHorizontalOffset)
    ToVerticalOffset = property(get_ToVerticalOffset, put_ToVerticalOffset)
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToHorizontalOffsetProperty = property(get_ToHorizontalOffsetProperty, None)
    ToVerticalOffsetProperty = property(get_ToVerticalOffsetProperty, None)
class Timeline(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(29)
    def get_AutoReverse(self) -> Boolean: ...
    @winrt_commethod(30)
    def put_AutoReverse(self, value: Boolean) -> Void: ...
    @winrt_commethod(31)
    def get_BeginTime(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(32)
    def put_BeginTime(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(33)
    def get_Duration(self) -> Windows.UI.Xaml.Duration: ...
    @winrt_commethod(34)
    def put_Duration(self, value: Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_commethod(35)
    def get_SpeedRatio(self) -> Double: ...
    @winrt_commethod(36)
    def put_SpeedRatio(self, value: Double) -> Void: ...
    @winrt_commethod(37)
    def get_FillBehavior(self) -> Windows.UI.Xaml.Media.Animation.FillBehavior: ...
    @winrt_commethod(38)
    def put_FillBehavior(self, value: Windows.UI.Xaml.Media.Animation.FillBehavior) -> Void: ...
    @winrt_commethod(39)
    def get_RepeatBehavior(self) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(40)
    def put_RepeatBehavior(self, value: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Void: ...
    @winrt_commethod(41)
    def add_Completed(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(42)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AllowDependentAnimations(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Boolean: ...
    @winrt_classmethod
    def put_AllowDependentAnimations(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_AutoReverseProperty(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BeginTimeProperty(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DurationProperty(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SpeedRatioProperty(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FillBehaviorProperty(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RepeatBehaviorProperty(cls: Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    AutoReverse = property(get_AutoReverse, put_AutoReverse)
    BeginTime = property(get_BeginTime, put_BeginTime)
    Duration = property(get_Duration, put_Duration)
    SpeedRatio = property(get_SpeedRatio, put_SpeedRatio)
    FillBehavior = property(get_FillBehavior, put_FillBehavior)
    RepeatBehavior = property(get_RepeatBehavior, put_RepeatBehavior)
    AllowDependentAnimations = property(get_AllowDependentAnimations, put_AllowDependentAnimations)
    AutoReverseProperty = property(get_AutoReverseProperty, None)
    BeginTimeProperty = property(get_BeginTimeProperty, None)
    DurationProperty = property(get_DurationProperty, None)
    SpeedRatioProperty = property(get_SpeedRatioProperty, None)
    FillBehaviorProperty = property(get_FillBehaviorProperty, None)
    RepeatBehaviorProperty = property(get_RepeatBehaviorProperty, None)
class TimelineCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.TimelineCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32) -> Windows.UI.Xaml.Media.Animation.Timeline: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Animation.Timeline]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], value: Windows.UI.Xaml.Media.Animation.Timeline, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32, value: Windows.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32, value: Windows.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], value: Windows.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Animation.Timeline)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline], items: POINTER(Windows.UI.Xaml.Media.Animation.Timeline)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Animation.Timeline]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Animation.Timeline]: ...
    Size = property(get_Size, None)
class Transition(c_void_p):
    extends: Windows.UI.Xaml.DependencyObject
class TransitionCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Media.Animation.TransitionCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], index: UInt32) -> Windows.UI.Xaml.Media.Animation.Transition: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Animation.Transition]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], value: Windows.UI.Xaml.Media.Animation.Transition, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], index: UInt32, value: Windows.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], index: UInt32, value: Windows.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], value: Windows.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Animation.Transition)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition], items: POINTER(Windows.UI.Xaml.Media.Animation.Transition)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Animation.Transition]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Animation.Transition]: ...
    Size = property(get_Size, None)
make_head(_module, 'AddDeleteThemeTransition')
make_head(_module, 'BackEase')
make_head(_module, 'BasicConnectedAnimationConfiguration')
make_head(_module, 'BeginStoryboard')
make_head(_module, 'BounceEase')
make_head(_module, 'CircleEase')
make_head(_module, 'ColorAnimation')
make_head(_module, 'ColorAnimationUsingKeyFrames')
make_head(_module, 'ColorKeyFrame')
make_head(_module, 'ColorKeyFrameCollection')
make_head(_module, 'CommonNavigationTransitionInfo')
make_head(_module, 'ConnectedAnimation')
make_head(_module, 'ConnectedAnimationConfiguration')
make_head(_module, 'ConnectedAnimationService')
make_head(_module, 'ContentThemeTransition')
make_head(_module, 'ContinuumNavigationTransitionInfo')
make_head(_module, 'CubicEase')
make_head(_module, 'DirectConnectedAnimationConfiguration')
make_head(_module, 'DiscreteColorKeyFrame')
make_head(_module, 'DiscreteDoubleKeyFrame')
make_head(_module, 'DiscreteObjectKeyFrame')
make_head(_module, 'DiscretePointKeyFrame')
make_head(_module, 'DoubleAnimation')
make_head(_module, 'DoubleAnimationUsingKeyFrames')
make_head(_module, 'DoubleKeyFrame')
make_head(_module, 'DoubleKeyFrameCollection')
make_head(_module, 'DragItemThemeAnimation')
make_head(_module, 'DragOverThemeAnimation')
make_head(_module, 'DrillInNavigationTransitionInfo')
make_head(_module, 'DrillInThemeAnimation')
make_head(_module, 'DrillOutThemeAnimation')
make_head(_module, 'DropTargetItemThemeAnimation')
make_head(_module, 'EasingColorKeyFrame')
make_head(_module, 'EasingDoubleKeyFrame')
make_head(_module, 'EasingFunctionBase')
make_head(_module, 'EasingPointKeyFrame')
make_head(_module, 'EdgeUIThemeTransition')
make_head(_module, 'ElasticEase')
make_head(_module, 'EntranceNavigationTransitionInfo')
make_head(_module, 'EntranceThemeTransition')
make_head(_module, 'ExponentialEase')
make_head(_module, 'FadeInThemeAnimation')
make_head(_module, 'FadeOutThemeAnimation')
make_head(_module, 'GravityConnectedAnimationConfiguration')
make_head(_module, 'IAddDeleteThemeTransition')
make_head(_module, 'IBackEase')
make_head(_module, 'IBackEaseStatics')
make_head(_module, 'IBasicConnectedAnimationConfiguration')
make_head(_module, 'IBasicConnectedAnimationConfigurationFactory')
make_head(_module, 'IBeginStoryboard')
make_head(_module, 'IBeginStoryboardStatics')
make_head(_module, 'IBounceEase')
make_head(_module, 'IBounceEaseStatics')
make_head(_module, 'ICircleEase')
make_head(_module, 'IColorAnimation')
make_head(_module, 'IColorAnimationStatics')
make_head(_module, 'IColorAnimationUsingKeyFrames')
make_head(_module, 'IColorAnimationUsingKeyFramesStatics')
make_head(_module, 'IColorKeyFrame')
make_head(_module, 'IColorKeyFrameFactory')
make_head(_module, 'IColorKeyFrameStatics')
make_head(_module, 'ICommonNavigationTransitionInfo')
make_head(_module, 'ICommonNavigationTransitionInfoStatics')
make_head(_module, 'IConnectedAnimation')
make_head(_module, 'IConnectedAnimation2')
make_head(_module, 'IConnectedAnimation3')
make_head(_module, 'IConnectedAnimationConfiguration')
make_head(_module, 'IConnectedAnimationConfigurationFactory')
make_head(_module, 'IConnectedAnimationService')
make_head(_module, 'IConnectedAnimationServiceStatics')
make_head(_module, 'IContentThemeTransition')
make_head(_module, 'IContentThemeTransitionStatics')
make_head(_module, 'IContinuumNavigationTransitionInfo')
make_head(_module, 'IContinuumNavigationTransitionInfoStatics')
make_head(_module, 'ICubicEase')
make_head(_module, 'IDirectConnectedAnimationConfiguration')
make_head(_module, 'IDirectConnectedAnimationConfigurationFactory')
make_head(_module, 'IDiscreteColorKeyFrame')
make_head(_module, 'IDiscreteDoubleKeyFrame')
make_head(_module, 'IDiscreteObjectKeyFrame')
make_head(_module, 'IDiscretePointKeyFrame')
make_head(_module, 'IDoubleAnimation')
make_head(_module, 'IDoubleAnimationStatics')
make_head(_module, 'IDoubleAnimationUsingKeyFrames')
make_head(_module, 'IDoubleAnimationUsingKeyFramesStatics')
make_head(_module, 'IDoubleKeyFrame')
make_head(_module, 'IDoubleKeyFrameFactory')
make_head(_module, 'IDoubleKeyFrameStatics')
make_head(_module, 'IDragItemThemeAnimation')
make_head(_module, 'IDragItemThemeAnimationStatics')
make_head(_module, 'IDragOverThemeAnimation')
make_head(_module, 'IDragOverThemeAnimationStatics')
make_head(_module, 'IDrillInNavigationTransitionInfo')
make_head(_module, 'IDrillInThemeAnimation')
make_head(_module, 'IDrillInThemeAnimationStatics')
make_head(_module, 'IDrillOutThemeAnimation')
make_head(_module, 'IDrillOutThemeAnimationStatics')
make_head(_module, 'IDropTargetItemThemeAnimation')
make_head(_module, 'IDropTargetItemThemeAnimationStatics')
make_head(_module, 'IEasingColorKeyFrame')
make_head(_module, 'IEasingColorKeyFrameStatics')
make_head(_module, 'IEasingDoubleKeyFrame')
make_head(_module, 'IEasingDoubleKeyFrameStatics')
make_head(_module, 'IEasingFunctionBase')
make_head(_module, 'IEasingFunctionBaseFactory')
make_head(_module, 'IEasingFunctionBaseStatics')
make_head(_module, 'IEasingPointKeyFrame')
make_head(_module, 'IEasingPointKeyFrameStatics')
make_head(_module, 'IEdgeUIThemeTransition')
make_head(_module, 'IEdgeUIThemeTransitionStatics')
make_head(_module, 'IElasticEase')
make_head(_module, 'IElasticEaseStatics')
make_head(_module, 'IEntranceNavigationTransitionInfo')
make_head(_module, 'IEntranceNavigationTransitionInfoStatics')
make_head(_module, 'IEntranceThemeTransition')
make_head(_module, 'IEntranceThemeTransitionStatics')
make_head(_module, 'IExponentialEase')
make_head(_module, 'IExponentialEaseStatics')
make_head(_module, 'IFadeInThemeAnimation')
make_head(_module, 'IFadeInThemeAnimationStatics')
make_head(_module, 'IFadeOutThemeAnimation')
make_head(_module, 'IFadeOutThemeAnimationStatics')
make_head(_module, 'IGravityConnectedAnimationConfiguration')
make_head(_module, 'IGravityConnectedAnimationConfiguration2')
make_head(_module, 'IGravityConnectedAnimationConfigurationFactory')
make_head(_module, 'IKeySpline')
make_head(_module, 'IKeyTimeHelper')
make_head(_module, 'IKeyTimeHelperStatics')
make_head(_module, 'ILinearColorKeyFrame')
make_head(_module, 'ILinearDoubleKeyFrame')
make_head(_module, 'ILinearPointKeyFrame')
make_head(_module, 'INavigationThemeTransition')
make_head(_module, 'INavigationThemeTransitionStatics')
make_head(_module, 'INavigationTransitionInfo')
make_head(_module, 'INavigationTransitionInfoFactory')
make_head(_module, 'INavigationTransitionInfoOverrides')
make_head(_module, 'IObjectAnimationUsingKeyFrames')
make_head(_module, 'IObjectAnimationUsingKeyFramesStatics')
make_head(_module, 'IObjectKeyFrame')
make_head(_module, 'IObjectKeyFrameFactory')
make_head(_module, 'IObjectKeyFrameStatics')
make_head(_module, 'IPaneThemeTransition')
make_head(_module, 'IPaneThemeTransitionStatics')
make_head(_module, 'IPointAnimation')
make_head(_module, 'IPointAnimationStatics')
make_head(_module, 'IPointAnimationUsingKeyFrames')
make_head(_module, 'IPointAnimationUsingKeyFramesStatics')
make_head(_module, 'IPointKeyFrame')
make_head(_module, 'IPointKeyFrameFactory')
make_head(_module, 'IPointKeyFrameStatics')
make_head(_module, 'IPointerDownThemeAnimation')
make_head(_module, 'IPointerDownThemeAnimationStatics')
make_head(_module, 'IPointerUpThemeAnimation')
make_head(_module, 'IPointerUpThemeAnimationStatics')
make_head(_module, 'IPopInThemeAnimation')
make_head(_module, 'IPopInThemeAnimationStatics')
make_head(_module, 'IPopOutThemeAnimation')
make_head(_module, 'IPopOutThemeAnimationStatics')
make_head(_module, 'IPopupThemeTransition')
make_head(_module, 'IPopupThemeTransitionStatics')
make_head(_module, 'IPowerEase')
make_head(_module, 'IPowerEaseStatics')
make_head(_module, 'IQuadraticEase')
make_head(_module, 'IQuarticEase')
make_head(_module, 'IQuinticEase')
make_head(_module, 'IReorderThemeTransition')
make_head(_module, 'IRepeatBehaviorHelper')
make_head(_module, 'IRepeatBehaviorHelperStatics')
make_head(_module, 'IRepositionThemeAnimation')
make_head(_module, 'IRepositionThemeAnimationStatics')
make_head(_module, 'IRepositionThemeTransition')
make_head(_module, 'IRepositionThemeTransition2')
make_head(_module, 'IRepositionThemeTransitionStatics2')
make_head(_module, 'ISineEase')
make_head(_module, 'ISlideNavigationTransitionInfo')
make_head(_module, 'ISlideNavigationTransitionInfo2')
make_head(_module, 'ISlideNavigationTransitionInfoStatics2')
make_head(_module, 'ISplineColorKeyFrame')
make_head(_module, 'ISplineColorKeyFrameStatics')
make_head(_module, 'ISplineDoubleKeyFrame')
make_head(_module, 'ISplineDoubleKeyFrameStatics')
make_head(_module, 'ISplinePointKeyFrame')
make_head(_module, 'ISplinePointKeyFrameStatics')
make_head(_module, 'ISplitCloseThemeAnimation')
make_head(_module, 'ISplitCloseThemeAnimationStatics')
make_head(_module, 'ISplitOpenThemeAnimation')
make_head(_module, 'ISplitOpenThemeAnimationStatics')
make_head(_module, 'IStoryboard')
make_head(_module, 'IStoryboardStatics')
make_head(_module, 'ISuppressNavigationTransitionInfo')
make_head(_module, 'ISwipeBackThemeAnimation')
make_head(_module, 'ISwipeBackThemeAnimationStatics')
make_head(_module, 'ISwipeHintThemeAnimation')
make_head(_module, 'ISwipeHintThemeAnimationStatics')
make_head(_module, 'ITimeline')
make_head(_module, 'ITimelineFactory')
make_head(_module, 'ITimelineStatics')
make_head(_module, 'ITransition')
make_head(_module, 'ITransitionFactory')
make_head(_module, 'KeySpline')
make_head(_module, 'KeyTime')
make_head(_module, 'KeyTimeHelper')
make_head(_module, 'LinearColorKeyFrame')
make_head(_module, 'LinearDoubleKeyFrame')
make_head(_module, 'LinearPointKeyFrame')
make_head(_module, 'NavigationThemeTransition')
make_head(_module, 'NavigationTransitionInfo')
make_head(_module, 'ObjectAnimationUsingKeyFrames')
make_head(_module, 'ObjectKeyFrame')
make_head(_module, 'ObjectKeyFrameCollection')
make_head(_module, 'PaneThemeTransition')
make_head(_module, 'PointAnimation')
make_head(_module, 'PointAnimationUsingKeyFrames')
make_head(_module, 'PointKeyFrame')
make_head(_module, 'PointKeyFrameCollection')
make_head(_module, 'PointerDownThemeAnimation')
make_head(_module, 'PointerUpThemeAnimation')
make_head(_module, 'PopInThemeAnimation')
make_head(_module, 'PopOutThemeAnimation')
make_head(_module, 'PopupThemeTransition')
make_head(_module, 'PowerEase')
make_head(_module, 'QuadraticEase')
make_head(_module, 'QuarticEase')
make_head(_module, 'QuinticEase')
make_head(_module, 'ReorderThemeTransition')
make_head(_module, 'RepeatBehavior')
make_head(_module, 'RepeatBehaviorHelper')
make_head(_module, 'RepositionThemeAnimation')
make_head(_module, 'RepositionThemeTransition')
make_head(_module, 'SineEase')
make_head(_module, 'SlideNavigationTransitionInfo')
make_head(_module, 'SplineColorKeyFrame')
make_head(_module, 'SplineDoubleKeyFrame')
make_head(_module, 'SplinePointKeyFrame')
make_head(_module, 'SplitCloseThemeAnimation')
make_head(_module, 'SplitOpenThemeAnimation')
make_head(_module, 'Storyboard')
make_head(_module, 'SuppressNavigationTransitionInfo')
make_head(_module, 'SwipeBackThemeAnimation')
make_head(_module, 'SwipeHintThemeAnimation')
make_head(_module, 'Timeline')
make_head(_module, 'TimelineCollection')
make_head(_module, 'Transition')
make_head(_module, 'TransitionCollection')
