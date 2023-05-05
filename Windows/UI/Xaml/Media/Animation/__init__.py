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
class AddDeleteThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IAddDeleteThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.AddDeleteThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.AddDeleteThemeTransition: ...
class BackEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IBackEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BackEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.BackEase: ...
    @winrt_mixinmethod
    def get_Amplitude(self: Windows.UI.Xaml.Media.Animation.IBackEase) -> Double: ...
    @winrt_mixinmethod
    def put_Amplitude(self: Windows.UI.Xaml.Media.Animation.IBackEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_AmplitudeProperty(cls: Windows.UI.Xaml.Media.Animation.IBackEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
    AmplitudeProperty = property(get_AmplitudeProperty, None)
class BasicConnectedAnimationConfiguration(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfigurationFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration: ...
class BeginStoryboard(ComPtr):
    extends: Windows.UI.Xaml.TriggerAction
    default_interface: Windows.UI.Xaml.Media.Animation.IBeginStoryboard
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BeginStoryboard'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.BeginStoryboard: ...
    @winrt_mixinmethod
    def get_Storyboard(self: Windows.UI.Xaml.Media.Animation.IBeginStoryboard) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: Windows.UI.Xaml.Media.Animation.IBeginStoryboard, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    @winrt_classmethod
    def get_StoryboardProperty(cls: Windows.UI.Xaml.Media.Animation.IBeginStoryboardStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
    StoryboardProperty = property(get_StoryboardProperty, None)
class BounceEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IBounceEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BounceEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.BounceEase: ...
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
class CircleEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.ICircleEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.CircleEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.CircleEase: ...
ClockState = Int32
ClockState_Active: ClockState = 0
ClockState_Filling: ClockState = 1
ClockState_Stopped: ClockState = 2
class ColorAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IColorAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ColorAnimation: ...
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
class ColorAnimationUsingKeyFrames(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames: ...
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
class ColorKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.IColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorKeyFrame'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.IColorKeyFrameFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Media.Animation.IColorKeyFrame) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.UI.Xaml.Media.Animation.IColorKeyFrame, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: Windows.UI.Xaml.Media.Animation.IColorKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: Windows.UI.Xaml.Media.Animation.IColorKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class ColorKeyFrameCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ColorKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
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
class CommonNavigationTransitionInfo(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo: ...
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
class ConnectedAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.Animation.IConnectedAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimation'
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
class ConnectedAnimationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.Animation.IConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration'
class ConnectedAnimationService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.Animation.IConnectedAnimationService
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimationService'
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
class ContentThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IContentThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ContentThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ContentThemeTransition: ...
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
class ContinuumNavigationTransitionInfo(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo: ...
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
class CubicEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.ICubicEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.CubicEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.CubicEase: ...
class DirectConnectedAnimationConfiguration(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfigurationFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration: ...
class DiscreteColorKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.IDiscreteColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscreteColorKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DiscreteColorKeyFrame: ...
class DiscreteDoubleKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.IDiscreteDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame: ...
class DiscreteObjectKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ObjectKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.IDiscreteObjectKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame: ...
class DiscretePointKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.IDiscretePointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscretePointKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DiscretePointKeyFrame: ...
class DoubleAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IDoubleAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DoubleAnimation: ...
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
class DoubleAnimationUsingKeyFrames(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames: ...
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
class DoubleKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleKeyFrame'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame) -> Double: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class DoubleKeyFrameCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
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
class DragItemThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DragItemThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DragItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class DragOverThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DragOverThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DragOverThemeAnimation: ...
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
class DrillInNavigationTransitionInfo(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: Windows.UI.Xaml.Media.Animation.IDrillInNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo: ...
class DrillInThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DrillInThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DrillInThemeAnimation: ...
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
class DrillOutThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DrillOutThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DrillOutThemeAnimation: ...
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
class DropTargetItemThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class EasingColorKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingColorKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.EasingColorKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class EasingDoubleKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingDoubleKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.EasingDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class EasingFunctionBase(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.IEasingFunctionBase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingFunctionBase'
    @winrt_mixinmethod
    def get_EasingMode(self: Windows.UI.Xaml.Media.Animation.IEasingFunctionBase) -> Windows.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_mixinmethod
    def put_EasingMode(self: Windows.UI.Xaml.Media.Animation.IEasingFunctionBase, value: Windows.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_mixinmethod
    def Ease(self: Windows.UI.Xaml.Media.Animation.IEasingFunctionBase, normalizedTime: Double) -> Double: ...
    @winrt_classmethod
    def get_EasingModeProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingFunctionBaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
    EasingModeProperty = property(get_EasingModeProperty, None)
EasingMode = Int32
EasingMode_EaseOut: EasingMode = 0
EasingMode_EaseIn: EasingMode = 1
EasingMode_EaseInOut: EasingMode = 2
class EasingPointKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingPointKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.EasingPointKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class EdgeUIThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EdgeUIThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.EdgeUIThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    EdgeProperty = property(get_EdgeProperty, None)
class ElasticEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IElasticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ElasticEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ElasticEase: ...
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
class EntranceNavigationTransitionInfo(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo: ...
    @winrt_classmethod
    def get_IsTargetElementProperty(cls: Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsTargetElement(cls: Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsTargetElement(cls: Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class EntranceThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EntranceThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.EntranceThemeTransition: ...
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
class ExponentialEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IExponentialEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ExponentialEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ExponentialEase: ...
    @winrt_mixinmethod
    def get_Exponent(self: Windows.UI.Xaml.Media.Animation.IExponentialEase) -> Double: ...
    @winrt_mixinmethod
    def put_Exponent(self: Windows.UI.Xaml.Media.Animation.IExponentialEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_ExponentProperty(cls: Windows.UI.Xaml.Media.Animation.IExponentialEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Exponent = property(get_Exponent, put_Exponent)
    ExponentProperty = property(get_ExponentProperty, None)
class FadeInThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.FadeInThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.FadeInThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class FadeOutThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.FadeOutThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.FadeOutThemeAnimation: ...
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
class GravityConnectedAnimationConfiguration(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfigurationFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration: ...
    @winrt_mixinmethod
    def get_IsShadowEnabled(self: Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsShadowEnabled(self: Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration2, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IAddDeleteThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IAddDeleteThemeTransition'
    _iid_ = Guid('{adec852e-4424-4dab-99c1-3a04e36a3c48}')
class IBackEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBackEase'
    _iid_ = Guid('{e47796e7-f805-4a8f-81c9-38e6472caa94}')
    @winrt_commethod(6)
    def get_Amplitude(self) -> Double: ...
    @winrt_commethod(7)
    def put_Amplitude(self, value: Double) -> Void: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
class IBackEaseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBackEaseStatics'
    _iid_ = Guid('{3c70a2ff-a0a0-4786-926c-22321f8f25b7}')
    @winrt_commethod(6)
    def get_AmplitudeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    AmplitudeProperty = property(get_AmplitudeProperty, None)
class IBasicConnectedAnimationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfiguration'
    _iid_ = Guid('{e675f9b5-a4d6-5353-83e6-c89e7cf8d456}')
class IBasicConnectedAnimationConfigurationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{95e6844a-4377-503c-bee2-11dfcd5570e6}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration: ...
class IBeginStoryboard(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBeginStoryboard'
    _iid_ = Guid('{64189fcd-49ec-4e52-a6f6-55324c921053}')
    @winrt_commethod(6)
    def get_Storyboard(self) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(7)
    def put_Storyboard(self, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
class IBeginStoryboardStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBeginStoryboardStatics'
    _iid_ = Guid('{12cff18c-aa91-4c4a-b82f-df34fc57f94b}')
    @winrt_commethod(6)
    def get_StoryboardProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    StoryboardProperty = property(get_StoryboardProperty, None)
class IBounceEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBounceEase'
    _iid_ = Guid('{2bf1464e-fc71-47ed-85a1-3ba9577718b4}')
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
class IBounceEaseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBounceEaseStatics'
    _iid_ = Guid('{c0701da2-4f73-41c9-b2cb-2ea3105107ff}')
    @winrt_commethod(6)
    def get_BouncesProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_BouncinessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    BouncesProperty = property(get_BouncesProperty, None)
    BouncinessProperty = property(get_BouncinessProperty, None)
class ICircleEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICircleEase'
    _iid_ = Guid('{53a3bdb2-9177-4e6e-a043-5082d889ab1f}')
class IColorAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimation'
    _iid_ = Guid('{b8ae8a15-0f63-4694-9467-bdafac1253ea}')
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
class IColorAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimationStatics'
    _iid_ = Guid('{55eaf6e2-87e3-4f48-958f-855b2f9ea9ec}')
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
class IColorAnimationUsingKeyFrames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames'
    _iid_ = Guid('{f5c82640-13c3-42aa-9ae2-7e6b51c92f95}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IColorAnimationUsingKeyFramesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{b4723cdc-96e9-48f9-8d92-9b648b2f1cc6}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IColorKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorKeyFrame'
    _iid_ = Guid('{b51d82d9-0910-4589-a284-b0c9205858e9}')
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
class IColorKeyFrameFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorKeyFrameFactory'
    _iid_ = Guid('{769bd88a-9cfb-4a7d-96c4-a1e7de6fdb4b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.ColorKeyFrame: ...
class IColorKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics'
    _iid_ = Guid('{c043ae99-210c-430f-9da5-df1082692055}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class ICommonNavigationTransitionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo'
    _iid_ = Guid('{50345692-a555-4624-a361-0a91c1706473}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class ICommonNavigationTransitionInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics'
    _iid_ = Guid('{1e3efe33-50be-4443-883c-e5627201c2e5}')
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
class IConnectedAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimation'
    _iid_ = Guid('{3518628c-f387-4c25-ac98-44e86c3cadf0}')
    @winrt_commethod(6)
    def add_Completed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Media.Animation.ConnectedAnimation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TryStart(self, destination: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def Cancel(self) -> Void: ...
class IConnectedAnimation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimation2'
    _iid_ = Guid('{5d2f8e5c-584b-4ddd-b668-973891431459}')
    @winrt_commethod(6)
    def get_IsScaleAnimationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsScaleAnimationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def TryStartWithCoordinatedElements(self, destination: Windows.UI.Xaml.UIElement, coordinatedElements: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]) -> Boolean: ...
    @winrt_commethod(9)
    def SetAnimationComponent(self, component: Windows.UI.Xaml.Media.Animation.ConnectedAnimationComponent, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    IsScaleAnimationEnabled = property(get_IsScaleAnimationEnabled, put_IsScaleAnimationEnabled)
class IConnectedAnimation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimation3'
    _iid_ = Guid('{6e3040c6-0430-59c0-a80c-cceed2e778dd}')
    @winrt_commethod(6)
    def get_Configuration(self) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration: ...
    @winrt_commethod(7)
    def put_Configuration(self, value: Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration) -> Void: ...
    Configuration = property(get_Configuration, put_Configuration)
class IConnectedAnimationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationConfiguration'
    _iid_ = Guid('{00218aae-cd8c-5651-92a0-c1db95c03998}')
class IConnectedAnimationConfigurationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{30f9b84b-dd7e-593e-bf75-e959dc0ec52a}')
class IConnectedAnimationService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationService'
    _iid_ = Guid('{1c6875c9-19bb-4d47-b9aa-66c802dcb9ff}')
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
class IConnectedAnimationServiceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationServiceStatics'
    _iid_ = Guid('{c7078ea5-d688-40e8-8f90-96a6279273d2}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Xaml.Media.Animation.ConnectedAnimationService: ...
class IContentThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IContentThemeTransition'
    _iid_ = Guid('{f66fc5c3-5915-437d-8e3b-adf8e7f0ab57}')
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
class IContentThemeTransitionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IContentThemeTransitionStatics'
    _iid_ = Guid('{0e8ee385-9a42-4459-afa9-337dc41e1587}')
    @winrt_commethod(6)
    def get_HorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class IContinuumNavigationTransitionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo'
    _iid_ = Guid('{4be1dbad-8ba6-4004-8438-8a9017978543}')
    @winrt_commethod(6)
    def get_ExitElement(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_ExitElement(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    ExitElement = property(get_ExitElement, put_ExitElement)
class IContinuumNavigationTransitionInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics'
    _iid_ = Guid('{3e25dd53-b18f-4bf1-b3bc-92f516f29903}')
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
class ICubicEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICubicEase'
    _iid_ = Guid('{1b94fc76-dad7-4354-b1a2-7969fbf6a70d}')
class IDirectConnectedAnimationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfiguration'
    _iid_ = Guid('{ee5d736f-5738-5d86-b770-151948cf365e}')
class IDirectConnectedAnimationConfigurationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{059263e9-d2b3-5a77-9cf4-e26d8b542608}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration: ...
class IDiscreteColorKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscreteColorKeyFrame'
    _iid_ = Guid('{230c08f4-e062-4cb1-8e2a-14093d73ed8c}')
class IDiscreteDoubleKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscreteDoubleKeyFrame'
    _iid_ = Guid('{f5f51f3a-ad11-49ce-8e1c-08fdf1447446}')
class IDiscreteObjectKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscreteObjectKeyFrame'
    _iid_ = Guid('{c7dcde89-f12d-4a9c-8199-e7a9ece3a473}')
class IDiscretePointKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscretePointKeyFrame'
    _iid_ = Guid('{e0a9070d-4c42-4a90-983a-75f5a83a2fbe}')
class IDoubleAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimation'
    _iid_ = Guid('{7e9f3d59-0f07-4bc9-977d-03763ff8154f}')
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
class IDoubleAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics'
    _iid_ = Guid('{e27a935d-f111-43b7-b824-832b58d7786b}')
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
class IDoubleAnimationUsingKeyFrames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames'
    _iid_ = Guid('{4fee628f-bfee-4f75-83c2-a93b39488473}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IDoubleAnimationUsingKeyFramesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{109bf2f6-c60f-49aa-abf6-f696d492116b}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IDoubleKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame'
    _iid_ = Guid('{674456fd-e81e-4f4e-b4ad-0acfed9ecd68}')
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
class IDoubleKeyFrameFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameFactory'
    _iid_ = Guid('{ac97dec3-7538-40b9-b152-696f7fbf4722}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
class IDoubleKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics'
    _iid_ = Guid('{324641b0-7d37-427a-adeb-43f38bb61a4d}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class IDragItemThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation'
    _iid_ = Guid('{0c7d5db5-7ed6-4949-b4e6-a78c9f4f978d}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDragItemThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimationStatics'
    _iid_ = Guid('{6218b9f5-013a-4fb1-86fc-92bc4e8d0241}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IDragOverThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation'
    _iid_ = Guid('{72f762f7-7e51-4a6b-b937-dc4b4c1c5458}')
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
class IDragOverThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics'
    _iid_ = Guid('{146ffe57-3c9d-41d9-a5ff-8d7239516810}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_DirectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToOffsetProperty = property(get_ToOffsetProperty, None)
    DirectionProperty = property(get_DirectionProperty, None)
class IDrillInNavigationTransitionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillInNavigationTransitionInfo'
    _iid_ = Guid('{3b86201a-45d3-463b-939e-c8595f439bcc}')
class IDrillInThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation'
    _iid_ = Guid('{b090b824-f1d2-41b8-87ba-78034126594c}')
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
class IDrillInThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics'
    _iid_ = Guid('{c61fe488-a17a-4b11-b53b-a4f1a07d4ba9}')
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
class IDrillOutThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation'
    _iid_ = Guid('{d890ccdf-06d3-4f7e-8e4a-4fb76e256139}')
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
class IDrillOutThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics'
    _iid_ = Guid('{beb5db9b-2617-4888-80dd-72fa7bb6fac3}')
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
class IDropTargetItemThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation'
    _iid_ = Guid('{1881c968-1824-462b-87e8-c357212b977b}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDropTargetItemThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimationStatics'
    _iid_ = Guid('{ae80f486-2e56-4513-bf18-d77470164ae5}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IEasingColorKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame'
    _iid_ = Guid('{c733d630-f4b9-4934-9bdd-27ac5ed1cfd8}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingColorKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrameStatics'
    _iid_ = Guid('{6f3837fc-8e3d-4522-9b0f-003db8609851}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingDoubleKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame'
    _iid_ = Guid('{965adb8d-9a54-4108-b4ff-b5a5212cb338}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingDoubleKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrameStatics'
    _iid_ = Guid('{c8d3d845-dbae-4e5b-8b84-d9537398e5b1}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingFunctionBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingFunctionBase'
    _iid_ = Guid('{c108383f-2c02-4151-8ecd-68ddaa3f0d9b}')
    @winrt_commethod(6)
    def get_EasingMode(self) -> Windows.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_commethod(7)
    def put_EasingMode(self, value: Windows.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_commethod(8)
    def Ease(self, normalizedTime: Double) -> Double: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
class IEasingFunctionBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingFunctionBaseFactory'
    _iid_ = Guid('{1830fe6a-f01b-43e0-b61f-b452a1c66fd2}')
class IEasingFunctionBaseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingFunctionBaseStatics'
    _iid_ = Guid('{2a5031aa-2c50-4a1d-bb04-d75e07b71548}')
    @winrt_commethod(6)
    def get_EasingModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingModeProperty = property(get_EasingModeProperty, None)
class IEasingPointKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame'
    _iid_ = Guid('{b3c91380-6868-4225-a70b-3981cc0b2947}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingPointKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrameStatics'
    _iid_ = Guid('{e22dbfc4-080c-402c-a6b5-f48d0a98116b}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEdgeUIThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition'
    _iid_ = Guid('{5c86c19b-49d7-19ec-cf19-83a73c6de75e}')
    @winrt_commethod(6)
    def get_Edge(self) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IEdgeUIThemeTransitionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransitionStatics'
    _iid_ = Guid('{16a2b13b-4705-302b-27c6-2aac92f645ac}')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IElasticEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IElasticEase'
    _iid_ = Guid('{ef5ba58c-b0b6-4a6c-9ca8-fb4233f12459}')
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
class IElasticEaseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IElasticEaseStatics'
    _iid_ = Guid('{a9f566ec-fe9c-4b2b-8e52-bb785d562185}')
    @winrt_commethod(6)
    def get_OscillationsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SpringinessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    OscillationsProperty = property(get_OscillationsProperty, None)
    SpringinessProperty = property(get_SpringinessProperty, None)
class IEntranceNavigationTransitionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfo'
    _iid_ = Guid('{720a256b-1c8a-41ee-82ec-8a87c0cf47da}')
class IEntranceNavigationTransitionInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics'
    _iid_ = Guid('{f948c27a-40c9-469f-8f33-bf45c8811f21}')
    @winrt_commethod(6)
    def get_IsTargetElementProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsTargetElement(self, element: Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsTargetElement(self, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class IEntranceThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition'
    _iid_ = Guid('{07698c09-a8e3-419a-a01d-7410a0ae8ec8}')
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
class IEntranceThemeTransitionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics'
    _iid_ = Guid('{37cc0577-ff98-4aed-b86e-5ec23702f877}')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsStaggeringEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class IExponentialEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IExponentialEase'
    _iid_ = Guid('{7cb9e41d-f0bb-4bca-9da5-9ba3a11734c4}')
    @winrt_commethod(6)
    def get_Exponent(self) -> Double: ...
    @winrt_commethod(7)
    def put_Exponent(self, value: Double) -> Void: ...
    Exponent = property(get_Exponent, put_Exponent)
class IExponentialEaseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IExponentialEaseStatics'
    _iid_ = Guid('{f37ee7e3-a761-4352-9ad6-70794567581a}')
    @winrt_commethod(6)
    def get_ExponentProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ExponentProperty = property(get_ExponentProperty, None)
class IFadeInThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation'
    _iid_ = Guid('{6d4bc8f5-a918-4477-8078-554c68812ab8}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeInThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimationStatics'
    _iid_ = Guid('{7f0117e1-bea9-4923-b23a-0ddf4d7b8737}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IFadeOutThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation'
    _iid_ = Guid('{89276ba9-ffd4-45b6-9b9a-ced48951e712}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeOutThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimationStatics'
    _iid_ = Guid('{fe17a81a-4168-4f68-a28c-e5dd98cf680f}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IGravityConnectedAnimationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration'
    _iid_ = Guid('{c751a4b7-0459-5142-b891-aeaac1d41822}')
class IGravityConnectedAnimationConfiguration2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration2'
    _iid_ = Guid('{62333add-aed4-5fed-95ff-d128acce8be4}')
    @winrt_commethod(6)
    def get_IsShadowEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsShadowEnabled(self, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IGravityConnectedAnimationConfigurationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{e822c41f-3656-5090-92f5-c217eaacb682}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration: ...
class IKeySpline(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IKeySpline'
    _iid_ = Guid('{77a163bb-d5ca-4a32-ba0b-7dff988e58a0}')
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
class IKeyTimeHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IKeyTimeHelper'
    _iid_ = Guid('{3643e480-4823-466a-abe5-5e79c8ed77ed}')
class IKeyTimeHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IKeyTimeHelperStatics'
    _iid_ = Guid('{7fa2612c-22a9-45e9-9af7-c7416efff7a5}')
    @winrt_commethod(6)
    def FromTimeSpan(self, timeSpan: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
class ILinearColorKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ILinearColorKeyFrame'
    _iid_ = Guid('{66fdb6ef-ac81-4611-b1d2-61f545983f03}')
class ILinearDoubleKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ILinearDoubleKeyFrame'
    _iid_ = Guid('{8efdf265-9a7b-431d-8f0c-14c56b5ea4d9}')
class ILinearPointKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ILinearPointKeyFrame'
    _iid_ = Guid('{e7c9b8ef-af24-49ee-84f1-a86600a4e319}')
class INavigationThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationThemeTransition'
    _iid_ = Guid('{8833848c-4eb7-41f2-8799-9eef0a213b73}')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfo(self) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(7)
    def put_DefaultNavigationTransitionInfo(self, value: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
class INavigationThemeTransitionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationThemeTransitionStatics'
    _iid_ = Guid('{ea2f06e0-5e60-4f8e-bcaf-431487a294ab}')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfoProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class INavigationTransitionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationTransitionInfo'
    _iid_ = Guid('{a9b05091-ae4a-4372-8625-21b7a8b98ca4}')
class INavigationTransitionInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoFactory'
    _iid_ = Guid('{edf4f8d5-af63-4fab-9d4a-87927f82dd6b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
class INavigationTransitionInfoOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides'
    _iid_ = Guid('{d9517e6a-a9d0-4bf7-9db0-4633a69daff2}')
    @winrt_commethod(6)
    def GetNavigationStateCore(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def SetNavigationStateCore(self, navigationState: WinRT_String) -> Void: ...
class IObjectAnimationUsingKeyFrames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames'
    _iid_ = Guid('{334a2d92-b74a-4c64-b9a6-58bcfa314f22}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IObjectAnimationUsingKeyFramesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{eb736182-6af1-49a3-97b6-783ed97400fe}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IObjectKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectKeyFrame'
    _iid_ = Guid('{9852a851-8593-48ee-a6a4-d5d4720f029a}')
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
class IObjectKeyFrameFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectKeyFrameFactory'
    _iid_ = Guid('{1626143e-3e6d-44d8-9b9a-04aea70f8492}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
class IObjectKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics'
    _iid_ = Guid('{2cd6ab00-5319-4286-8eed-4e755ea0cf9c}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class IPaneThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPaneThemeTransition'
    _iid_ = Guid('{4708eb8e-4bfc-ee46-d4f9-708def3fbb2b}')
    @winrt_commethod(6)
    def get_Edge(self) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IPaneThemeTransitionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPaneThemeTransitionStatics'
    _iid_ = Guid('{316b382f-4be4-1797-b45c-cd900bbe0caa}')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IPointAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimation'
    _iid_ = Guid('{30f04312-7726-4f88-b8e2-2fa54518963b}')
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
class IPointAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimationStatics'
    _iid_ = Guid('{2f99b356-e737-408b-a0fd-327826d32255}')
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
class IPointAnimationUsingKeyFrames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames'
    _iid_ = Guid('{9b944f72-446a-41d0-a129-41a620f4595d}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    KeyFrames = property(get_KeyFrames, None)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
class IPointAnimationUsingKeyFramesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{5f454c87-2390-46ea-baa7-762f4bc30d04}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IPointKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointKeyFrame'
    _iid_ = Guid('{fcc88d01-7f82-4dae-8026-7b7e086878b3}')
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
class IPointKeyFrameFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointKeyFrameFactory'
    _iid_ = Guid('{cb214bdf-426a-4392-8355-c2ae52852623}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.PointKeyFrame: ...
class IPointKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics'
    _iid_ = Guid('{95cf1b27-7965-4bec-b9fb-fbe94b65518e}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class IPointerDownThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation'
    _iid_ = Guid('{b58e714e-c49d-4788-a233-0ae85d99dd5a}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerDownThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimationStatics'
    _iid_ = Guid('{63a7cb7b-6d46-4494-b94a-e72f3b492a61}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPointerUpThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation'
    _iid_ = Guid('{e9e9d07d-6340-4828-ad12-690694b9910b}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerUpThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimationStatics'
    _iid_ = Guid('{7c618f9c-7992-4139-8bfc-0883b9727a7e}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopInThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation'
    _iid_ = Guid('{196938c1-1c07-4c28-8847-f9f055b32855}')
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
class IPopInThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics'
    _iid_ = Guid('{efaa99d3-218a-4701-977f-f1bfae8ba649}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IPopOutThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation'
    _iid_ = Guid('{4786ab49-0e48-4e81-a2e5-cc5aa19e48d3}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPopOutThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimationStatics'
    _iid_ = Guid('{1d492c09-03c1-4490-99dc-909feab357fb}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopupThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopupThemeTransition'
    _iid_ = Guid('{47843552-4283-545e-c791-268dca22ce4b}')
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
class IPopupThemeTransitionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics'
    _iid_ = Guid('{e5a1640e-490d-1505-9f6b-8fafc044dec5}')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IPowerEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPowerEase'
    _iid_ = Guid('{69c80579-eedf-405b-8680-d9606880c937}')
    @winrt_commethod(6)
    def get_Power(self) -> Double: ...
    @winrt_commethod(7)
    def put_Power(self, value: Double) -> Void: ...
    Power = property(get_Power, put_Power)
class IPowerEaseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPowerEaseStatics'
    _iid_ = Guid('{a5955103-91a2-460c-9c41-d28f6a939bda}')
    @winrt_commethod(6)
    def get_PowerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PowerProperty = property(get_PowerProperty, None)
class IQuadraticEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IQuadraticEase'
    _iid_ = Guid('{e1510e91-ef6d-44f0-803d-68d16de0ddfc}')
class IQuarticEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IQuarticEase'
    _iid_ = Guid('{e8698814-fe42-4a05-b5b8-081f41157815}')
class IQuinticEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IQuinticEase'
    _iid_ = Guid('{92ee793b-3c49-4108-aa11-ab786603da21}')
class IReorderThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IReorderThemeTransition'
    _iid_ = Guid('{f2065c6c-d052-4ad1-8362-b71b36df7497}')
class IRepeatBehaviorHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelper'
    _iid_ = Guid('{6863ab72-4997-47f9-87ad-37efb75993ea}')
class IRepeatBehaviorHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics'
    _iid_ = Guid('{7a795033-79f3-4dd9-b267-9cf50fb51f84}')
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
class IRepositionThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation'
    _iid_ = Guid('{ecda24e8-8945-4949-a1bf-62109965a7e9}')
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
class IRepositionThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics'
    _iid_ = Guid('{4d92b1b1-860b-4bf9-a59d-1eb1ccbe8fe0}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IRepositionThemeTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition'
    _iid_ = Guid('{88329b82-98f3-455a-ac53-2e7083b6e22c}')
class IRepositionThemeTransition2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2'
    _iid_ = Guid('{cebfe864-dbea-4404-8e6e-de55ada75239}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class IRepositionThemeTransitionStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeTransitionStatics2'
    _iid_ = Guid('{9240e930-0a19-468b-8c2a-68fab4500027}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class ISineEase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISineEase'
    _iid_ = Guid('{a9382962-230b-49da-9e0d-664987892343}')
class ISlideNavigationTransitionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo'
    _iid_ = Guid('{d6ac9d77-2e03-405f-80ed-e62beef3668f}')
class ISlideNavigationTransitionInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2'
    _iid_ = Guid('{90e2d9c0-5c81-5001-8013-4fbfea4bf139}')
    @winrt_commethod(6)
    def get_Effect(self) -> Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_commethod(7)
    def put_Effect(self, value: Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    Effect = property(get_Effect, put_Effect)
class ISlideNavigationTransitionInfoStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfoStatics2'
    _iid_ = Guid('{8a861baa-981a-5ace-9f85-cb7fde648a67}')
    @winrt_commethod(6)
    def get_EffectProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    EffectProperty = property(get_EffectProperty, None)
class ISplineColorKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame'
    _iid_ = Guid('{1a4a5941-1fe0-473a-8efe-4316d8c86229}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineColorKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrameStatics'
    _iid_ = Guid('{61d1d997-8589-4f2f-8fbb-7d03edc98dd3}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplineDoubleKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame'
    _iid_ = Guid('{00d72d38-6b2b-4843-838e-c8b115eec801}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineDoubleKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrameStatics'
    _iid_ = Guid('{060a8ffc-975f-4e4e-9ec7-13c5aee02062}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplinePointKeyFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame'
    _iid_ = Guid('{0f19f306-7036-494f-bc3c-780df0cc524a}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplinePointKeyFrameStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrameStatics'
    _iid_ = Guid('{e97a32c2-0a7a-4766-95cb-0d692611cb4c}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplitCloseThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation'
    _iid_ = Guid('{4f799518-ff39-4e90-bb74-2abd56027402}')
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
class ISplitCloseThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics'
    _iid_ = Guid('{7aa94de9-cc9b-4e90-a11a-0050a2216a9e}')
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
class ISplitOpenThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation'
    _iid_ = Guid('{785fd7aa-5456-4639-8fd2-26bae6a5ffe4}')
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
class ISplitOpenThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics'
    _iid_ = Guid('{8d4cfa89-3a91-458d-b0fb-4cad625cbf8d}')
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
class IStoryboard(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IStoryboard'
    _iid_ = Guid('{d45c1e6e-3594-460e-981a-32271bd3aa06}')
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
class IStoryboardStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IStoryboardStatics'
    _iid_ = Guid('{d82f07d8-73d5-4379-bd48-7e05184a8bad}')
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
class ISuppressNavigationTransitionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISuppressNavigationTransitionInfo'
    _iid_ = Guid('{244d7b0c-b1b7-4871-9d3e-d56203a3a5b4}')
class ISwipeBackThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation'
    _iid_ = Guid('{a38a4214-0bca-4d2d-95f7-ceba57fbaf60}')
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
class ISwipeBackThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics'
    _iid_ = Guid('{693f31bf-4da6-468a-8ce0-996c9aad42e0}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class ISwipeHintThemeAnimation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation'
    _iid_ = Guid('{cdd067c0-580e-4e40-be98-f202d3d84365}')
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
class ISwipeHintThemeAnimationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics'
    _iid_ = Guid('{23d61a57-9115-4d63-b04a-b89f1c744dc0}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ToVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToHorizontalOffsetProperty = property(get_ToHorizontalOffsetProperty, None)
    ToVerticalOffsetProperty = property(get_ToVerticalOffsetProperty, None)
class ITimeline(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITimeline'
    _iid_ = Guid('{0bc465dc-be4d-4d0d-9549-2208b715f40d}')
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
class ITimelineFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITimelineFactory'
    _iid_ = Guid('{1d56bb07-bda4-478b-8ada-eb04d580cd5e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.Timeline: ...
class ITimelineStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITimelineStatics'
    _iid_ = Guid('{a902ed4e-ef10-4d6f-9a40-93cb8895f4e5}')
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
class ITransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITransition'
    _iid_ = Guid('{3c677c7c-01d0-4dce-b333-976f93312b08}')
class ITransitionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITransitionFactory'
    _iid_ = Guid('{dc9ab2cf-3bc9-44aa-b3fc-883a83233a2c}')
class KeySpline(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.IKeySpline
    _classid_ = 'Windows.UI.Xaml.Media.Animation.KeySpline'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
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
class KeyTimeHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.Animation.IKeyTimeHelper
    _classid_ = 'Windows.UI.Xaml.Media.Animation.KeyTimeHelper'
    @winrt_classmethod
    def FromTimeSpan(cls: Windows.UI.Xaml.Media.Animation.IKeyTimeHelperStatics, timeSpan: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
class LinearColorKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.ILinearColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.LinearColorKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.LinearColorKeyFrame: ...
class LinearDoubleKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.ILinearDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.LinearDoubleKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.LinearDoubleKeyFrame: ...
class LinearPointKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.ILinearPointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.LinearPointKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.LinearPointKeyFrame: ...
class NavigationThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.INavigationThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.NavigationThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.NavigationThemeTransition: ...
    @winrt_mixinmethod
    def get_DefaultNavigationTransitionInfo(self: Windows.UI.Xaml.Media.Animation.INavigationThemeTransition) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def put_DefaultNavigationTransitionInfo(self: Windows.UI.Xaml.Media.Animation.INavigationThemeTransition, value: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    @winrt_classmethod
    def get_DefaultNavigationTransitionInfoProperty(cls: Windows.UI.Xaml.Media.Animation.INavigationThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
    DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class NavigationTransitionInfo(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.INavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def GetNavigationStateCore(self: Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetNavigationStateCore(self: Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides, navigationState: WinRT_String) -> Void: ...
class ObjectAnimationUsingKeyFrames(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames: ...
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
class ObjectKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.IObjectKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ObjectKeyFrame'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.IObjectKeyFrameFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Media.Animation.IObjectKeyFrame) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.UI.Xaml.Media.Animation.IObjectKeyFrame, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: Windows.UI.Xaml.Media.Animation.IObjectKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: Windows.UI.Xaml.Media.Animation.IObjectKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class ObjectKeyFrameCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
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
class PaneThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IPaneThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PaneThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PaneThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: Windows.UI.Xaml.Media.Animation.IPaneThemeTransition) -> Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: Windows.UI.Xaml.Media.Animation.IPaneThemeTransition, value: Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: Windows.UI.Xaml.Media.Animation.IPaneThemeTransitionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    EdgeProperty = property(get_EdgeProperty, None)
class PointAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IPointAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PointAnimation: ...
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
class PointAnimationUsingKeyFrames(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames: ...
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
class PointKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.IPointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointKeyFrame'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.IPointKeyFrameFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.PointKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Media.Animation.IPointKeyFrame) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.UI.Xaml.Media.Animation.IPointKeyFrame, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: Windows.UI.Xaml.Media.Animation.IPointKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: Windows.UI.Xaml.Media.Animation.IPointKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Value = property(get_Value, put_Value)
    KeyTime = property(get_KeyTime, put_KeyTime)
    ValueProperty = property(get_ValueProperty, None)
    KeyTimeProperty = property(get_KeyTimeProperty, None)
class PointKeyFrameCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.PointKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
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
class PointerDownThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointerDownThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PointerDownThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class PointerUpThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointerUpThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PointerUpThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class PopInThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PopInThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PopInThemeAnimation: ...
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
class PopOutThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PopOutThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PopOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    TargetNameProperty = property(get_TargetNameProperty, None)
class PopupThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IPopupThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PopupThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PopupThemeTransition: ...
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
class PowerEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IPowerEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PowerEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.PowerEase: ...
    @winrt_mixinmethod
    def get_Power(self: Windows.UI.Xaml.Media.Animation.IPowerEase) -> Double: ...
    @winrt_mixinmethod
    def put_Power(self: Windows.UI.Xaml.Media.Animation.IPowerEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_PowerProperty(cls: Windows.UI.Xaml.Media.Animation.IPowerEaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Power = property(get_Power, put_Power)
    PowerProperty = property(get_PowerProperty, None)
class QuadraticEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IQuadraticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.QuadraticEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.QuadraticEase: ...
class QuarticEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IQuarticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.QuarticEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.QuarticEase: ...
class QuinticEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.IQuinticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.QuinticEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.QuinticEase: ...
class ReorderThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IReorderThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ReorderThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.ReorderThemeTransition: ...
class RepeatBehavior(EasyCastStructure):
    Count: Double
    Duration: Windows.Foundation.TimeSpan
    Type: Windows.UI.Xaml.Media.Animation.RepeatBehaviorType
class RepeatBehaviorHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelper
    _classid_ = 'Windows.UI.Xaml.Media.Animation.RepeatBehaviorHelper'
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
class RepositionThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.RepositionThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.RepositionThemeAnimation: ...
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
class RepositionThemeTransition(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Transition
    default_interface: Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.RepositionThemeTransition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.RepositionThemeTransition: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: Windows.UI.Xaml.Media.Animation.IRepositionThemeTransitionStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class SineEase(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: Windows.UI.Xaml.Media.Animation.ISineEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SineEase'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SineEase: ...
SlideNavigationTransitionEffect = Int32
SlideNavigationTransitionEffect_FromBottom: SlideNavigationTransitionEffect = 0
SlideNavigationTransitionEffect_FromLeft: SlideNavigationTransitionEffect = 1
SlideNavigationTransitionEffect_FromRight: SlideNavigationTransitionEffect = 2
class SlideNavigationTransitionInfo(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_Effect(self: Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2) -> Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_mixinmethod
    def put_Effect(self: Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2, value: Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    @winrt_classmethod
    def get_EffectProperty(cls: Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfoStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    Effect = property(get_Effect, put_Effect)
    EffectProperty = property(get_EffectProperty, None)
class SplineColorKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplineColorKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SplineColorKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    KeySplineProperty = property(get_KeySplineProperty, None)
class SplineDoubleKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplineDoubleKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SplineDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    KeySplineProperty = property(get_KeySplineProperty, None)
class SplinePointKeyFrame(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplinePointKeyFrame'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SplinePointKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame) -> Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame, value: Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrameStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    KeySplineProperty = property(get_KeySplineProperty, None)
class SplitCloseThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplitCloseThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SplitCloseThemeAnimation: ...
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
class SplitOpenThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplitOpenThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SplitOpenThemeAnimation: ...
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
class Storyboard(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.IStoryboard
    _classid_ = 'Windows.UI.Xaml.Media.Animation.Storyboard'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
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
class SuppressNavigationTransitionInfo(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: Windows.UI.Xaml.Media.Animation.ISuppressNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo: ...
class SwipeBackThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SwipeBackThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SwipeBackThemeAnimation: ...
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
class SwipeHintThemeAnimation(ComPtr):
    extends: Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SwipeHintThemeAnimation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.SwipeHintThemeAnimation: ...
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
class Timeline(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.ITimeline
    _classid_ = 'Windows.UI.Xaml.Media.Animation.Timeline'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Animation.ITimelineFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Animation.Timeline: ...
    @winrt_mixinmethod
    def get_AutoReverse(self: Windows.UI.Xaml.Media.Animation.ITimeline) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoReverse(self: Windows.UI.Xaml.Media.Animation.ITimeline, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BeginTime(self: Windows.UI.Xaml.Media.Animation.ITimeline) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_BeginTime(self: Windows.UI.Xaml.Media.Animation.ITimeline, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.UI.Xaml.Media.Animation.ITimeline) -> Windows.UI.Xaml.Duration: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.UI.Xaml.Media.Animation.ITimeline, value: Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_mixinmethod
    def get_SpeedRatio(self: Windows.UI.Xaml.Media.Animation.ITimeline) -> Double: ...
    @winrt_mixinmethod
    def put_SpeedRatio(self: Windows.UI.Xaml.Media.Animation.ITimeline, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FillBehavior(self: Windows.UI.Xaml.Media.Animation.ITimeline) -> Windows.UI.Xaml.Media.Animation.FillBehavior: ...
    @winrt_mixinmethod
    def put_FillBehavior(self: Windows.UI.Xaml.Media.Animation.ITimeline, value: Windows.UI.Xaml.Media.Animation.FillBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_RepeatBehavior(self: Windows.UI.Xaml.Media.Animation.ITimeline) -> Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_mixinmethod
    def put_RepeatBehavior(self: Windows.UI.Xaml.Media.Animation.ITimeline, value: Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.UI.Xaml.Media.Animation.ITimeline, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.UI.Xaml.Media.Animation.ITimeline, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
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
class TimelineCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Timeline]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.TimelineCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.TimelineCollection: ...
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
class Transition(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Animation.ITransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.Transition'
class TransitionCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.Transition]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.TransitionCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
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
