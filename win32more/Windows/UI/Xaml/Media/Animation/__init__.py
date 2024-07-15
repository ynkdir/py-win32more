from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Controls
import win32more.Windows.UI.Xaml.Controls.Primitives
import win32more.Windows.UI.Xaml.Media.Animation
import win32more.Windows.Win32.System.WinRT
class AddDeleteThemeTransition(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IAddDeleteThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.AddDeleteThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.AddDeleteThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.AddDeleteThemeTransition: ...
class _BackEase_Meta_(ComPtr.__class__):
    pass
class BackEase(ComPtr, metaclass=_BackEase_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IBackEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BackEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.BackEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.BackEase: ...
    @winrt_mixinmethod
    def get_Amplitude(self: win32more.Windows.UI.Xaml.Media.Animation.IBackEase) -> Double: ...
    @winrt_mixinmethod
    def put_Amplitude(self: win32more.Windows.UI.Xaml.Media.Animation.IBackEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_AmplitudeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IBackEaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
    _BackEase_Meta_.AmplitudeProperty = property(get_AmplitudeProperty, None)
class BasicConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfigurationFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration: ...
class _BeginStoryboard_Meta_(ComPtr.__class__):
    pass
class BeginStoryboard(ComPtr, metaclass=_BeginStoryboard_Meta_):
    extends: win32more.Windows.UI.Xaml.TriggerAction
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IBeginStoryboard
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BeginStoryboard'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.BeginStoryboard.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.BeginStoryboard: ...
    @winrt_mixinmethod
    def get_Storyboard(self: win32more.Windows.UI.Xaml.Media.Animation.IBeginStoryboard) -> win32more.Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: win32more.Windows.UI.Xaml.Media.Animation.IBeginStoryboard, value: win32more.Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    @winrt_classmethod
    def get_StoryboardProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IBeginStoryboardStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
    _BeginStoryboard_Meta_.StoryboardProperty = property(get_StoryboardProperty, None)
class _BounceEase_Meta_(ComPtr.__class__):
    pass
class BounceEase(ComPtr, metaclass=_BounceEase_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IBounceEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.BounceEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.BounceEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.BounceEase: ...
    @winrt_mixinmethod
    def get_Bounces(self: win32more.Windows.UI.Xaml.Media.Animation.IBounceEase) -> Int32: ...
    @winrt_mixinmethod
    def put_Bounces(self: win32more.Windows.UI.Xaml.Media.Animation.IBounceEase, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Bounciness(self: win32more.Windows.UI.Xaml.Media.Animation.IBounceEase) -> Double: ...
    @winrt_mixinmethod
    def put_Bounciness(self: win32more.Windows.UI.Xaml.Media.Animation.IBounceEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_BouncesProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IBounceEaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BouncinessProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IBounceEaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Bounces = property(get_Bounces, put_Bounces)
    Bounciness = property(get_Bounciness, put_Bounciness)
    _BounceEase_Meta_.BouncesProperty = property(get_BouncesProperty, None)
    _BounceEase_Meta_.BouncinessProperty = property(get_BouncinessProperty, None)
class CircleEase(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ICircleEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.CircleEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.CircleEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.CircleEase: ...
class ClockState(Enum, Int32):
    Active = 0
    Filling = 1
    Stopped = 2
class _ColorAnimation_Meta_(ComPtr.__class__):
    pass
class ColorAnimation(ComPtr, metaclass=_ColorAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ColorAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ColorAnimation: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_By(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    _ColorAnimation_Meta_.ByProperty = property(get_ByProperty, None)
    _ColorAnimation_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    _ColorAnimation_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    _ColorAnimation_Meta_.FromProperty = property(get_FromProperty, None)
    _ColorAnimation_Meta_.ToProperty = property(get_ToProperty, None)
class _ColorAnimationUsingKeyFrames_Meta_(ComPtr.__class__):
    pass
class ColorAnimationUsingKeyFrames(ComPtr, metaclass=_ColorAnimationUsingKeyFrames_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames) -> win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFramesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _ColorAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _ColorKeyFrame_Meta_(ComPtr.__class__):
    pass
class ColorKeyFrame(ComPtr, metaclass=_ColorKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrame) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrame, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _ColorKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _ColorKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class ColorKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame], items: PassArray[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame]: ...
    Size = property(get_Size, None)
class _CommonNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class CommonNavigationTransitionInfo(ComPtr, metaclass=_CommonNavigationTransitionInfo_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStaggerElementProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsStaggerElement(cls: win32more.Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsStaggerElement(cls: win32more.Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    _CommonNavigationTransitionInfo_Meta_.IsStaggerElementProperty = property(get_IsStaggerElementProperty, None)
    _CommonNavigationTransitionInfo_Meta_.IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class ConnectedAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimation'
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryStart(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation, destination: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation) -> Void: ...
    @winrt_mixinmethod
    def get_IsScaleAnimationEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScaleAnimationEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryStartWithCoordinatedElements(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation2, destination: win32more.Windows.UI.Xaml.UIElement, coordinatedElements: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]) -> Boolean: ...
    @winrt_mixinmethod
    def SetAnimationComponent(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation2, component: win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationComponent, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation3) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration: ...
    @winrt_mixinmethod
    def put_Configuration(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimation3, value: win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration) -> Void: ...
    Configuration = property(get_Configuration, put_Configuration)
    IsScaleAnimationEnabled = property(get_IsScaleAnimationEnabled, put_IsScaleAnimationEnabled)
    Completed = event()
class ConnectedAnimationComponent(Enum, Int32):
    OffsetX = 0
    OffsetY = 1
    CrossFade = 2
    Scale = 3
class ConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration'
class ConnectedAnimationService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationService
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ConnectedAnimationService'
    @winrt_mixinmethod
    def get_DefaultDuration(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationService) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DefaultDuration(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultEasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationService) -> win32more.Windows.UI.Composition.CompositionEasingFunction: ...
    @winrt_mixinmethod
    def put_DefaultEasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, value: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_mixinmethod
    def PrepareToAnimate(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, key: WinRT_String, source: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_mixinmethod
    def GetAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationService, key: WinRT_String) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Xaml.Media.Animation.IConnectedAnimationServiceStatics) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationService: ...
    DefaultDuration = property(get_DefaultDuration, put_DefaultDuration)
    DefaultEasingFunction = property(get_DefaultEasingFunction, put_DefaultEasingFunction)
class _ContentThemeTransition_Meta_(ComPtr.__class__):
    pass
class ContentThemeTransition(ComPtr, metaclass=_ContentThemeTransition_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IContentThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ContentThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ContentThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ContentThemeTransition: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IContentThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IContentThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IContentThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IContentThemeTransition, value: Double) -> Void: ...
    @winrt_classmethod
    def get_HorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IContentThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IContentThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    _ContentThemeTransition_Meta_.HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    _ContentThemeTransition_Meta_.VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class _ContinuumNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class ContinuumNavigationTransitionInfo(ComPtr, metaclass=_ContinuumNavigationTransitionInfo_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_ExitElement(self: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_ExitElement(self: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_ExitElementProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsEntranceElementProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsEntranceElement(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsEntranceElement(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsExitElementProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsExitElement(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsExitElement(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ExitElementContainerProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetExitElementContainer(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.Controls.ListViewBase) -> Boolean: ...
    @winrt_classmethod
    def SetExitElementContainer(cls: win32more.Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.Controls.ListViewBase, value: Boolean) -> Void: ...
    ExitElement = property(get_ExitElement, put_ExitElement)
    _ContinuumNavigationTransitionInfo_Meta_.ExitElementContainerProperty = property(get_ExitElementContainerProperty, None)
    _ContinuumNavigationTransitionInfo_Meta_.ExitElementProperty = property(get_ExitElementProperty, None)
    _ContinuumNavigationTransitionInfo_Meta_.IsEntranceElementProperty = property(get_IsEntranceElementProperty, None)
    _ContinuumNavigationTransitionInfo_Meta_.IsExitElementProperty = property(get_IsExitElementProperty, None)
class CubicEase(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ICubicEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.CubicEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.CubicEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.CubicEase: ...
class DirectConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfigurationFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration: ...
class DiscreteColorKeyFrame(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDiscreteColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscreteColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DiscreteColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DiscreteColorKeyFrame: ...
class DiscreteDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDiscreteDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame: ...
class DiscreteObjectKeyFrame(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDiscreteObjectKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame: ...
class DiscretePointKeyFrame(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDiscretePointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DiscretePointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DiscretePointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DiscretePointKeyFrame: ...
class _DoubleAnimation_Meta_(ComPtr.__class__):
    pass
class DoubleAnimation(ComPtr, metaclass=_DoubleAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DoubleAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleAnimation: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_By(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    _DoubleAnimation_Meta_.ByProperty = property(get_ByProperty, None)
    _DoubleAnimation_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    _DoubleAnimation_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    _DoubleAnimation_Meta_.FromProperty = property(get_FromProperty, None)
    _DoubleAnimation_Meta_.ToProperty = property(get_ToProperty, None)
class _DoubleAnimationUsingKeyFrames_Meta_(ComPtr.__class__):
    pass
class DoubleAnimationUsingKeyFrames(ComPtr, metaclass=_DoubleAnimationUsingKeyFrames_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFramesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _DoubleAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _DoubleKeyFrame_Meta_(ComPtr.__class__):
    pass
class DoubleKeyFrame(ComPtr, metaclass=_DoubleKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame) -> Double: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _DoubleKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _DoubleKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class DoubleKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame], items: PassArray[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame]: ...
    Size = property(get_Size, None)
class _DragItemThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DragItemThemeAnimation(ComPtr, metaclass=_DragItemThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DragItemThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DragItemThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DragItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _DragItemThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _DragOverThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DragOverThemeAnimation(ComPtr, metaclass=_DragOverThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DragOverThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DragOverThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DragOverThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ToOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DirectionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Direction = property(get_Direction, put_Direction)
    TargetName = property(get_TargetName, put_TargetName)
    ToOffset = property(get_ToOffset, put_ToOffset)
    _DragOverThemeAnimation_Meta_.DirectionProperty = property(get_DirectionProperty, None)
    _DragOverThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
    _DragOverThemeAnimation_Meta_.ToOffsetProperty = property(get_ToOffsetProperty, None)
class DrillInNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDrillInNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo: ...
class _DrillInThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DrillInThemeAnimation(ComPtr, metaclass=_DrillInThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DrillInThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DrillInThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DrillInThemeAnimation: ...
    @winrt_mixinmethod
    def get_EntranceTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EntranceTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EntranceTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_EntranceTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ExitTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_EntranceTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EntranceTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
    _DrillInThemeAnimation_Meta_.EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    _DrillInThemeAnimation_Meta_.EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    _DrillInThemeAnimation_Meta_.ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    _DrillInThemeAnimation_Meta_.ExitTargetProperty = property(get_ExitTargetProperty, None)
class _DrillOutThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DrillOutThemeAnimation(ComPtr, metaclass=_DrillOutThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DrillOutThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DrillOutThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DrillOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_EntranceTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EntranceTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EntranceTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_EntranceTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ExitTarget(self: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_EntranceTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EntranceTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
    _DrillOutThemeAnimation_Meta_.EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    _DrillOutThemeAnimation_Meta_.EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    _DrillOutThemeAnimation_Meta_.ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    _DrillOutThemeAnimation_Meta_.ExitTargetProperty = property(get_ExitTargetProperty, None)
class _DropTargetItemThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DropTargetItemThemeAnimation(ComPtr, metaclass=_DropTargetItemThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _DropTargetItemThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _EasingColorKeyFrame_Meta_(ComPtr.__class__):
    pass
class EasingColorKeyFrame(ComPtr, metaclass=_EasingColorKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.EasingColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.EasingColorKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    _EasingColorKeyFrame_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class _EasingDoubleKeyFrame_Meta_(ComPtr.__class__):
    pass
class EasingDoubleKeyFrame(ComPtr, metaclass=_EasingDoubleKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.EasingDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.EasingDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    _EasingDoubleKeyFrame_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class _EasingFunctionBase_Meta_(ComPtr.__class__):
    pass
class EasingFunctionBase(ComPtr, metaclass=_EasingFunctionBase_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IEasingFunctionBase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingFunctionBase'
    @winrt_mixinmethod
    def get_EasingMode(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingFunctionBase) -> win32more.Windows.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_mixinmethod
    def put_EasingMode(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingFunctionBase, value: win32more.Windows.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_mixinmethod
    def Ease(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingFunctionBase, normalizedTime: Double) -> Double: ...
    @winrt_classmethod
    def get_EasingModeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEasingFunctionBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
    _EasingFunctionBase_Meta_.EasingModeProperty = property(get_EasingModeProperty, None)
class EasingMode(Enum, Int32):
    EaseOut = 0
    EaseIn = 1
    EaseInOut = 2
class _EasingPointKeyFrame_Meta_(ComPtr.__class__):
    pass
class EasingPointKeyFrame(ComPtr, metaclass=_EasingPointKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EasingPointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.EasingPointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.EasingPointKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    _EasingPointKeyFrame_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class _EdgeUIThemeTransition_Meta_(ComPtr.__class__):
    pass
class EdgeUIThemeTransition(ComPtr, metaclass=_EdgeUIThemeTransition_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EdgeUIThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.EdgeUIThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.EdgeUIThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: win32more.Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition) -> win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: win32more.Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition, value: win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    _EdgeUIThemeTransition_Meta_.EdgeProperty = property(get_EdgeProperty, None)
class _ElasticEase_Meta_(ComPtr.__class__):
    pass
class ElasticEase(ComPtr, metaclass=_ElasticEase_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IElasticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ElasticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ElasticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ElasticEase: ...
    @winrt_mixinmethod
    def get_Oscillations(self: win32more.Windows.UI.Xaml.Media.Animation.IElasticEase) -> Int32: ...
    @winrt_mixinmethod
    def put_Oscillations(self: win32more.Windows.UI.Xaml.Media.Animation.IElasticEase, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Springiness(self: win32more.Windows.UI.Xaml.Media.Animation.IElasticEase) -> Double: ...
    @winrt_mixinmethod
    def put_Springiness(self: win32more.Windows.UI.Xaml.Media.Animation.IElasticEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OscillationsProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IElasticEaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SpringinessProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IElasticEaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Oscillations = property(get_Oscillations, put_Oscillations)
    Springiness = property(get_Springiness, put_Springiness)
    _ElasticEase_Meta_.OscillationsProperty = property(get_OscillationsProperty, None)
    _ElasticEase_Meta_.SpringinessProperty = property(get_SpringinessProperty, None)
class _EntranceNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class EntranceNavigationTransitionInfo(ComPtr, metaclass=_EntranceNavigationTransitionInfo_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo: ...
    @winrt_classmethod
    def get_IsTargetElementProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsTargetElement(cls: win32more.Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsTargetElement(cls: win32more.Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    _EntranceNavigationTransitionInfo_Meta_.IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class _EntranceThemeTransition_Meta_(ComPtr.__class__):
    pass
class EntranceThemeTransition(ComPtr, metaclass=_EntranceThemeTransition_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.EntranceThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.EntranceThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.EntranceThemeTransition: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    _EntranceThemeTransition_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _EntranceThemeTransition_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _EntranceThemeTransition_Meta_.IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class _ExponentialEase_Meta_(ComPtr.__class__):
    pass
class ExponentialEase(ComPtr, metaclass=_ExponentialEase_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IExponentialEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ExponentialEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ExponentialEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ExponentialEase: ...
    @winrt_mixinmethod
    def get_Exponent(self: win32more.Windows.UI.Xaml.Media.Animation.IExponentialEase) -> Double: ...
    @winrt_mixinmethod
    def put_Exponent(self: win32more.Windows.UI.Xaml.Media.Animation.IExponentialEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_ExponentProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IExponentialEaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Exponent = property(get_Exponent, put_Exponent)
    _ExponentialEase_Meta_.ExponentProperty = property(get_ExponentProperty, None)
class _FadeInThemeAnimation_Meta_(ComPtr.__class__):
    pass
class FadeInThemeAnimation(ComPtr, metaclass=_FadeInThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.FadeInThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.FadeInThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.FadeInThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _FadeInThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _FadeOutThemeAnimation_Meta_(ComPtr.__class__):
    pass
class FadeOutThemeAnimation(ComPtr, metaclass=_FadeOutThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.FadeOutThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.FadeOutThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.FadeOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _FadeOutThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class FillBehavior(Enum, Int32):
    HoldEnd = 0
    Stop = 1
class GravityConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration
    _classid_ = 'Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfigurationFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration: ...
    @winrt_mixinmethod
    def get_IsShadowEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsShadowEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration2, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IAddDeleteThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IAddDeleteThemeTransition'
    _iid_ = Guid('{adec852e-4424-4dab-99c1-3a04e36a3c48}')
class IBackEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBackEase'
    _iid_ = Guid('{e47796e7-f805-4a8f-81c9-38e6472caa94}')
    @winrt_commethod(6)
    def get_Amplitude(self) -> Double: ...
    @winrt_commethod(7)
    def put_Amplitude(self, value: Double) -> Void: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
class IBackEaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBackEaseStatics'
    _iid_ = Guid('{3c70a2ff-a0a0-4786-926c-22321f8f25b7}')
    @winrt_commethod(6)
    def get_AmplitudeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AmplitudeProperty = property(get_AmplitudeProperty, None)
class IBasicConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfiguration'
    _iid_ = Guid('{e675f9b5-a4d6-5353-83e6-c89e7cf8d456}')
class IBasicConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{95e6844a-4377-503c-bee2-11dfcd5570e6}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration: ...
class IBeginStoryboard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBeginStoryboard'
    _iid_ = Guid('{64189fcd-49ec-4e52-a6f6-55324c921053}')
    @winrt_commethod(6)
    def get_Storyboard(self) -> win32more.Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(7)
    def put_Storyboard(self, value: win32more.Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
class IBeginStoryboardStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBeginStoryboardStatics'
    _iid_ = Guid('{12cff18c-aa91-4c4a-b82f-df34fc57f94b}')
    @winrt_commethod(6)
    def get_StoryboardProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    StoryboardProperty = property(get_StoryboardProperty, None)
class IBounceEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IBounceEaseStatics'
    _iid_ = Guid('{c0701da2-4f73-41c9-b2cb-2ea3105107ff}')
    @winrt_commethod(6)
    def get_BouncesProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_BouncinessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    BouncesProperty = property(get_BouncesProperty, None)
    BouncinessProperty = property(get_BouncinessProperty, None)
class ICircleEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICircleEase'
    _iid_ = Guid('{53a3bdb2-9177-4e6e-a043-5082d889ab1f}')
class IColorAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimation'
    _iid_ = Guid('{b8ae8a15-0f63-4694-9467-bdafac1253ea}')
    @winrt_commethod(6)
    def get_From(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(7)
    def put_From(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(8)
    def get_To(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(9)
    def put_To(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(10)
    def get_By(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(11)
    def put_By(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(12)
    def get_EasingFunction(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(14)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    From = property(get_From, put_From)
    To = property(get_To, put_To)
class IColorAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimationStatics'
    _iid_ = Guid('{55eaf6e2-87e3-4f48-958f-855b2f9ea9ec}')
    @winrt_commethod(6)
    def get_FromProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
class IColorAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames'
    _iid_ = Guid('{f5c82640-13c3-42aa-9ae2-7e6b51c92f95}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IColorAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{b4723cdc-96e9-48f9-8d92-9b648b2f1cc6}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorKeyFrame'
    _iid_ = Guid('{b51d82d9-0910-4589-a284-b0c9205858e9}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IColorKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorKeyFrameFactory'
    _iid_ = Guid('{769bd88a-9cfb-4a7d-96c4-a1e7de6fdb4b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame: ...
class IColorKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IColorKeyFrameStatics'
    _iid_ = Guid('{c043ae99-210c-430f-9da5-df1082692055}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class ICommonNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo'
    _iid_ = Guid('{50345692-a555-4624-a361-0a91c1706473}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class ICommonNavigationTransitionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics'
    _iid_ = Guid('{1e3efe33-50be-4443-883c-e5627201c2e5}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsStaggerElementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetIsStaggerElement(self, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def SetIsStaggerElement(self, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsStaggerElementProperty = property(get_IsStaggerElementProperty, None)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class IConnectedAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimation'
    _iid_ = Guid('{3518628c-f387-4c25-ac98-44e86c3cadf0}')
    @winrt_commethod(6)
    def add_Completed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Completed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TryStart(self, destination: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def Cancel(self) -> Void: ...
    Completed = event()
class IConnectedAnimation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimation2'
    _iid_ = Guid('{5d2f8e5c-584b-4ddd-b668-973891431459}')
    @winrt_commethod(6)
    def get_IsScaleAnimationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsScaleAnimationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def TryStartWithCoordinatedElements(self, destination: win32more.Windows.UI.Xaml.UIElement, coordinatedElements: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]) -> Boolean: ...
    @winrt_commethod(9)
    def SetAnimationComponent(self, component: win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationComponent, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    IsScaleAnimationEnabled = property(get_IsScaleAnimationEnabled, put_IsScaleAnimationEnabled)
class IConnectedAnimation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimation3'
    _iid_ = Guid('{6e3040c6-0430-59c0-a80c-cceed2e778dd}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration: ...
    @winrt_commethod(7)
    def put_Configuration(self, value: win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration) -> Void: ...
    Configuration = property(get_Configuration, put_Configuration)
class IConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationConfiguration'
    _iid_ = Guid('{00218aae-cd8c-5651-92a0-c1db95c03998}')
class IConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{30f9b84b-dd7e-593e-bf75-e959dc0ec52a}')
class IConnectedAnimationService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationService'
    _iid_ = Guid('{1c6875c9-19bb-4d47-b9aa-66c802dcb9ff}')
    @winrt_commethod(6)
    def get_DefaultDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DefaultDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultEasingFunction(self) -> win32more.Windows.UI.Composition.CompositionEasingFunction: ...
    @winrt_commethod(9)
    def put_DefaultEasingFunction(self, value: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_commethod(10)
    def PrepareToAnimate(self, key: WinRT_String, source: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_commethod(11)
    def GetAnimation(self, key: WinRT_String) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    DefaultDuration = property(get_DefaultDuration, put_DefaultDuration)
    DefaultEasingFunction = property(get_DefaultEasingFunction, put_DefaultEasingFunction)
class IConnectedAnimationServiceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IConnectedAnimationServiceStatics'
    _iid_ = Guid('{c7078ea5-d688-40e8-8f90-96a6279273d2}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Xaml.Media.Animation.ConnectedAnimationService: ...
class IContentThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IContentThemeTransitionStatics'
    _iid_ = Guid('{0e8ee385-9a42-4459-afa9-337dc41e1587}')
    @winrt_commethod(6)
    def get_HorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class IContinuumNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo'
    _iid_ = Guid('{4be1dbad-8ba6-4004-8438-8a9017978543}')
    @winrt_commethod(6)
    def get_ExitElement(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_ExitElement(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    ExitElement = property(get_ExitElement, put_ExitElement)
class IContinuumNavigationTransitionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics'
    _iid_ = Guid('{3e25dd53-b18f-4bf1-b3bc-92f516f29903}')
    @winrt_commethod(6)
    def get_ExitElementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsEntranceElementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetIsEntranceElement(self, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def SetIsEntranceElement(self, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsExitElementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def GetIsExitElement(self, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(12)
    def SetIsExitElement(self, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_ExitElementContainerProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def GetExitElementContainer(self, element: win32more.Windows.UI.Xaml.Controls.ListViewBase) -> Boolean: ...
    @winrt_commethod(15)
    def SetExitElementContainer(self, element: win32more.Windows.UI.Xaml.Controls.ListViewBase, value: Boolean) -> Void: ...
    ExitElementContainerProperty = property(get_ExitElementContainerProperty, None)
    ExitElementProperty = property(get_ExitElementProperty, None)
    IsEntranceElementProperty = property(get_IsEntranceElementProperty, None)
    IsExitElementProperty = property(get_IsExitElementProperty, None)
class ICubicEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ICubicEase'
    _iid_ = Guid('{1b94fc76-dad7-4354-b1a2-7969fbf6a70d}')
class IDirectConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfiguration'
    _iid_ = Guid('{ee5d736f-5738-5d86-b770-151948cf365e}')
class IDirectConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{059263e9-d2b3-5a77-9cf4-e26d8b542608}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration: ...
class IDiscreteColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscreteColorKeyFrame'
    _iid_ = Guid('{230c08f4-e062-4cb1-8e2a-14093d73ed8c}')
class IDiscreteDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscreteDoubleKeyFrame'
    _iid_ = Guid('{f5f51f3a-ad11-49ce-8e1c-08fdf1447446}')
class IDiscreteObjectKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscreteObjectKeyFrame'
    _iid_ = Guid('{c7dcde89-f12d-4a9c-8199-e7a9ece3a473}')
class IDiscretePointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDiscretePointKeyFrame'
    _iid_ = Guid('{e0a9070d-4c42-4a90-983a-75f5a83a2fbe}')
class IDoubleAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimation'
    _iid_ = Guid('{7e9f3d59-0f07-4bc9-977d-03763ff8154f}')
    @winrt_commethod(6)
    def get_From(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def put_From(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(8)
    def get_To(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def put_To(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(10)
    def get_By(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def put_By(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(12)
    def get_EasingFunction(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(14)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    From = property(get_From, put_From)
    To = property(get_To, put_To)
class IDoubleAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimationStatics'
    _iid_ = Guid('{e27a935d-f111-43b7-b824-832b58d7786b}')
    @winrt_commethod(6)
    def get_FromProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
class IDoubleAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames'
    _iid_ = Guid('{4fee628f-bfee-4f75-83c2-a93b39488473}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IDoubleAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{109bf2f6-c60f-49aa-abf6-f696d492116b}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleKeyFrame'
    _iid_ = Guid('{674456fd-e81e-4f4e-b4ad-0acfed9ecd68}')
    @winrt_commethod(6)
    def get_Value(self) -> Double: ...
    @winrt_commethod(7)
    def put_Value(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IDoubleKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameFactory'
    _iid_ = Guid('{ac97dec3-7538-40b9-b152-696f7fbf4722}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
class IDoubleKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics'
    _iid_ = Guid('{324641b0-7d37-427a-adeb-43f38bb61a4d}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IDragItemThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimation'
    _iid_ = Guid('{0c7d5db5-7ed6-4949-b4e6-a78c9f4f978d}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDragItemThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDragItemThemeAnimationStatics'
    _iid_ = Guid('{6218b9f5-013a-4fb1-86fc-92bc4e8d0241}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IDragOverThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_Direction(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(11)
    def put_Direction(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    Direction = property(get_Direction, put_Direction)
    TargetName = property(get_TargetName, put_TargetName)
    ToOffset = property(get_ToOffset, put_ToOffset)
class IDragOverThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics'
    _iid_ = Guid('{146ffe57-3c9d-41d9-a5ff-8d7239516810}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_DirectionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DirectionProperty = property(get_DirectionProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToOffsetProperty = property(get_ToOffsetProperty, None)
class IDrillInNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillInNavigationTransitionInfo'
    _iid_ = Guid('{3b86201a-45d3-463b-939e-c8595f439bcc}')
class IDrillInThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimation'
    _iid_ = Guid('{b090b824-f1d2-41b8-87ba-78034126594c}')
    @winrt_commethod(6)
    def get_EntranceTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EntranceTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_EntranceTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_EntranceTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ExitTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ExitTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ExitTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ExitTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
class IDrillInThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics'
    _iid_ = Guid('{c61fe488-a17a-4b11-b53b-a4f1a07d4ba9}')
    @winrt_commethod(6)
    def get_EntranceTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EntranceTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ExitTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ExitTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class IDrillOutThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimation'
    _iid_ = Guid('{d890ccdf-06d3-4f7e-8e4a-4fb76e256139}')
    @winrt_commethod(6)
    def get_EntranceTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EntranceTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_EntranceTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_EntranceTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ExitTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ExitTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ExitTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ExitTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
class IDrillOutThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics'
    _iid_ = Guid('{beb5db9b-2617-4888-80dd-72fa7bb6fac3}')
    @winrt_commethod(6)
    def get_EntranceTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EntranceTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ExitTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ExitTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class IDropTargetItemThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation'
    _iid_ = Guid('{1881c968-1824-462b-87e8-c357212b977b}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDropTargetItemThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimationStatics'
    _iid_ = Guid('{ae80f486-2e56-4513-bf18-d77470164ae5}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IEasingColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrame'
    _iid_ = Guid('{c733d630-f4b9-4934-9bdd-27ac5ed1cfd8}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingColorKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingColorKeyFrameStatics'
    _iid_ = Guid('{6f3837fc-8e3d-4522-9b0f-003db8609851}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame'
    _iid_ = Guid('{965adb8d-9a54-4108-b4ff-b5a5212cb338}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingDoubleKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingDoubleKeyFrameStatics'
    _iid_ = Guid('{c8d3d845-dbae-4e5b-8b84-d9537398e5b1}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingFunctionBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingFunctionBase'
    _iid_ = Guid('{c108383f-2c02-4151-8ecd-68ddaa3f0d9b}')
    @winrt_commethod(6)
    def get_EasingMode(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_commethod(7)
    def put_EasingMode(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_commethod(8)
    def Ease(self, normalizedTime: Double) -> Double: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
class IEasingFunctionBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingFunctionBaseFactory'
    _iid_ = Guid('{1830fe6a-f01b-43e0-b61f-b452a1c66fd2}')
class IEasingFunctionBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingFunctionBaseStatics'
    _iid_ = Guid('{2a5031aa-2c50-4a1d-bb04-d75e07b71548}')
    @winrt_commethod(6)
    def get_EasingModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingModeProperty = property(get_EasingModeProperty, None)
class IEasingPointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrame'
    _iid_ = Guid('{b3c91380-6868-4225-a70b-3981cc0b2947}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingPointKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEasingPointKeyFrameStatics'
    _iid_ = Guid('{e22dbfc4-080c-402c-a6b5-f48d0a98116b}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEdgeUIThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransition'
    _iid_ = Guid('{5c86c19b-49d7-19ec-cf19-83a73c6de75e}')
    @winrt_commethod(6)
    def get_Edge(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IEdgeUIThemeTransitionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEdgeUIThemeTransitionStatics'
    _iid_ = Guid('{16a2b13b-4705-302b-27c6-2aac92f645ac}')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IElasticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IElasticEaseStatics'
    _iid_ = Guid('{a9f566ec-fe9c-4b2b-8e52-bb785d562185}')
    @winrt_commethod(6)
    def get_OscillationsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SpringinessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    OscillationsProperty = property(get_OscillationsProperty, None)
    SpringinessProperty = property(get_SpringinessProperty, None)
class IEntranceNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfo'
    _iid_ = Guid('{720a256b-1c8a-41ee-82ec-8a87c0cf47da}')
class IEntranceNavigationTransitionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics'
    _iid_ = Guid('{f948c27a-40c9-469f-8f33-bf45c8811f21}')
    @winrt_commethod(6)
    def get_IsTargetElementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsTargetElement(self, element: win32more.Windows.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsTargetElement(self, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class IEntranceThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics'
    _iid_ = Guid('{37cc0577-ff98-4aed-b86e-5ec23702f877}')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsStaggeringEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class IExponentialEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IExponentialEase'
    _iid_ = Guid('{7cb9e41d-f0bb-4bca-9da5-9ba3a11734c4}')
    @winrt_commethod(6)
    def get_Exponent(self) -> Double: ...
    @winrt_commethod(7)
    def put_Exponent(self, value: Double) -> Void: ...
    Exponent = property(get_Exponent, put_Exponent)
class IExponentialEaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IExponentialEaseStatics'
    _iid_ = Guid('{f37ee7e3-a761-4352-9ad6-70794567581a}')
    @winrt_commethod(6)
    def get_ExponentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ExponentProperty = property(get_ExponentProperty, None)
class IFadeInThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimation'
    _iid_ = Guid('{6d4bc8f5-a918-4477-8078-554c68812ab8}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeInThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeInThemeAnimationStatics'
    _iid_ = Guid('{7f0117e1-bea9-4923-b23a-0ddf4d7b8737}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IFadeOutThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimation'
    _iid_ = Guid('{89276ba9-ffd4-45b6-9b9a-ced48951e712}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeOutThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IFadeOutThemeAnimationStatics'
    _iid_ = Guid('{fe17a81a-4168-4f68-a28c-e5dd98cf680f}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IGravityConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration'
    _iid_ = Guid('{c751a4b7-0459-5142-b891-aeaac1d41822}')
class IGravityConnectedAnimationConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration2'
    _iid_ = Guid('{62333add-aed4-5fed-95ff-d128acce8be4}')
    @winrt_commethod(6)
    def get_IsShadowEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsShadowEnabled(self, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IGravityConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{e822c41f-3656-5090-92f5-c217eaacb682}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration: ...
class IKeySpline(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IKeySpline'
    _iid_ = Guid('{77a163bb-d5ca-4a32-ba0b-7dff988e58a0}')
    @winrt_commethod(6)
    def get_ControlPoint1(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_ControlPoint1(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_ControlPoint2(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_ControlPoint2(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    ControlPoint1 = property(get_ControlPoint1, put_ControlPoint1)
    ControlPoint2 = property(get_ControlPoint2, put_ControlPoint2)
class IKeyTimeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IKeyTimeHelper'
    _iid_ = Guid('{3643e480-4823-466a-abe5-5e79c8ed77ed}')
class IKeyTimeHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IKeyTimeHelperStatics'
    _iid_ = Guid('{7fa2612c-22a9-45e9-9af7-c7416efff7a5}')
    @winrt_commethod(6)
    def FromTimeSpan(self, timeSpan: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
class ILinearColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ILinearColorKeyFrame'
    _iid_ = Guid('{66fdb6ef-ac81-4611-b1d2-61f545983f03}')
class ILinearDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ILinearDoubleKeyFrame'
    _iid_ = Guid('{8efdf265-9a7b-431d-8f0c-14c56b5ea4d9}')
class ILinearPointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ILinearPointKeyFrame'
    _iid_ = Guid('{e7c9b8ef-af24-49ee-84f1-a86600a4e319}')
class INavigationThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationThemeTransition'
    _iid_ = Guid('{8833848c-4eb7-41f2-8799-9eef0a213b73}')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfo(self) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(7)
    def put_DefaultNavigationTransitionInfo(self, value: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
class INavigationThemeTransitionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationThemeTransitionStatics'
    _iid_ = Guid('{ea2f06e0-5e60-4f8e-bcaf-431487a294ab}')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfoProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class INavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationTransitionInfo'
    _iid_ = Guid('{a9b05091-ae4a-4372-8625-21b7a8b98ca4}')
class INavigationTransitionInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoFactory'
    _iid_ = Guid('{edf4f8d5-af63-4fab-9d4a-87927f82dd6b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
class INavigationTransitionInfoOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides'
    _iid_ = Guid('{d9517e6a-a9d0-4bf7-9db0-4633a69daff2}')
    @winrt_commethod(6)
    def GetNavigationStateCore(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def SetNavigationStateCore(self, navigationState: WinRT_String) -> Void: ...
class IObjectAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames'
    _iid_ = Guid('{334a2d92-b74a-4c64-b9a6-58bcfa314f22}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IObjectAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{eb736182-6af1-49a3-97b6-783ed97400fe}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IObjectKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectKeyFrame'
    _iid_ = Guid('{9852a851-8593-48ee-a6a4-d5d4720f029a}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IObjectKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectKeyFrameFactory'
    _iid_ = Guid('{1626143e-3e6d-44d8-9b9a-04aea70f8492}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
class IObjectKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics'
    _iid_ = Guid('{2cd6ab00-5319-4286-8eed-4e755ea0cf9c}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IPaneThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPaneThemeTransition'
    _iid_ = Guid('{4708eb8e-4bfc-ee46-d4f9-708def3fbb2b}')
    @winrt_commethod(6)
    def get_Edge(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IPaneThemeTransitionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPaneThemeTransitionStatics'
    _iid_ = Guid('{316b382f-4be4-1797-b45c-cd900bbe0caa}')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IPointAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimation'
    _iid_ = Guid('{30f04312-7726-4f88-b8e2-2fa54518963b}')
    @winrt_commethod(6)
    def get_From(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(7)
    def put_From(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(8)
    def get_To(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(9)
    def put_To(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(10)
    def get_By(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(11)
    def put_By(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(12)
    def get_EasingFunction(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(14)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    From = property(get_From, put_From)
    To = property(get_To, put_To)
class IPointAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimationStatics'
    _iid_ = Guid('{2f99b356-e737-408b-a0fd-327826d32255}')
    @winrt_commethod(6)
    def get_FromProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
class IPointAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames'
    _iid_ = Guid('{9b944f72-446a-41d0-a129-41a620f4595d}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IPointAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{5f454c87-2390-46ea-baa7-762f4bc30d04}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IPointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointKeyFrame'
    _iid_ = Guid('{fcc88d01-7f82-4dae-8026-7b7e086878b3}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IPointKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointKeyFrameFactory'
    _iid_ = Guid('{cb214bdf-426a-4392-8355-c2ae52852623}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame: ...
class IPointKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics'
    _iid_ = Guid('{95cf1b27-7965-4bec-b9fb-fbe94b65518e}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IPointerDownThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation'
    _iid_ = Guid('{b58e714e-c49d-4788-a233-0ae85d99dd5a}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerDownThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimationStatics'
    _iid_ = Guid('{63a7cb7b-6d46-4494-b94a-e72f3b492a61}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPointerUpThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation'
    _iid_ = Guid('{e9e9d07d-6340-4828-ad12-690694b9910b}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerUpThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimationStatics'
    _iid_ = Guid('{7c618f9c-7992-4139-8bfc-0883b9727a7e}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopInThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
class IPopInThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics'
    _iid_ = Guid('{efaa99d3-218a-4701-977f-f1bfae8ba649}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopOutThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation'
    _iid_ = Guid('{4786ab49-0e48-4e81-a2e5-cc5aa19e48d3}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPopOutThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimationStatics'
    _iid_ = Guid('{1d492c09-03c1-4490-99dc-909feab357fb}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopupThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics'
    _iid_ = Guid('{e5a1640e-490d-1505-9f6b-8fafc044dec5}')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IPowerEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPowerEase'
    _iid_ = Guid('{69c80579-eedf-405b-8680-d9606880c937}')
    @winrt_commethod(6)
    def get_Power(self) -> Double: ...
    @winrt_commethod(7)
    def put_Power(self, value: Double) -> Void: ...
    Power = property(get_Power, put_Power)
class IPowerEaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IPowerEaseStatics'
    _iid_ = Guid('{a5955103-91a2-460c-9c41-d28f6a939bda}')
    @winrt_commethod(6)
    def get_PowerProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PowerProperty = property(get_PowerProperty, None)
class IQuadraticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IQuadraticEase'
    _iid_ = Guid('{e1510e91-ef6d-44f0-803d-68d16de0ddfc}')
class IQuarticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IQuarticEase'
    _iid_ = Guid('{e8698814-fe42-4a05-b5b8-081f41157815}')
class IQuinticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IQuinticEase'
    _iid_ = Guid('{92ee793b-3c49-4108-aa11-ab786603da21}')
class IReorderThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IReorderThemeTransition'
    _iid_ = Guid('{f2065c6c-d052-4ad1-8362-b71b36df7497}')
class IRepeatBehaviorHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelper'
    _iid_ = Guid('{6863ab72-4997-47f9-87ad-37efb75993ea}')
class IRepeatBehaviorHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics'
    _iid_ = Guid('{7a795033-79f3-4dd9-b267-9cf50fb51f84}')
    @winrt_commethod(6)
    def get_Forever(self) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(7)
    def FromCount(self, count: Double) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(8)
    def FromDuration(self, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(9)
    def GetHasCount(self, target: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_commethod(10)
    def GetHasDuration(self, target: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_commethod(11)
    def Equals(self, target: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior, value: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    Forever = property(get_Forever, None)
class IRepositionThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
class IRepositionThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics'
    _iid_ = Guid('{4d92b1b1-860b-4bf9-a59d-1eb1ccbe8fe0}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class IRepositionThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition'
    _iid_ = Guid('{88329b82-98f3-455a-ac53-2e7083b6e22c}')
class IRepositionThemeTransition2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2'
    _iid_ = Guid('{cebfe864-dbea-4404-8e6e-de55ada75239}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class IRepositionThemeTransitionStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IRepositionThemeTransitionStatics2'
    _iid_ = Guid('{9240e930-0a19-468b-8c2a-68fab4500027}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class ISineEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISineEase'
    _iid_ = Guid('{a9382962-230b-49da-9e0d-664987892343}')
class ISlideNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo'
    _iid_ = Guid('{d6ac9d77-2e03-405f-80ed-e62beef3668f}')
class ISlideNavigationTransitionInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2'
    _iid_ = Guid('{90e2d9c0-5c81-5001-8013-4fbfea4bf139}')
    @winrt_commethod(6)
    def get_Effect(self) -> win32more.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_commethod(7)
    def put_Effect(self, value: win32more.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    Effect = property(get_Effect, put_Effect)
class ISlideNavigationTransitionInfoStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfoStatics2'
    _iid_ = Guid('{8a861baa-981a-5ace-9f85-cb7fde648a67}')
    @winrt_commethod(6)
    def get_EffectProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EffectProperty = property(get_EffectProperty, None)
class ISplineColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame'
    _iid_ = Guid('{1a4a5941-1fe0-473a-8efe-4316d8c86229}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> win32more.Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: win32more.Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineColorKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrameStatics'
    _iid_ = Guid('{61d1d997-8589-4f2f-8fbb-7d03edc98dd3}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplineDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame'
    _iid_ = Guid('{00d72d38-6b2b-4843-838e-c8b115eec801}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> win32more.Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: win32more.Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineDoubleKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrameStatics'
    _iid_ = Guid('{060a8ffc-975f-4e4e-9ec7-13c5aee02062}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplinePointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame'
    _iid_ = Guid('{0f19f306-7036-494f-bc3c-780df0cc524a}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> win32more.Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: win32more.Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplinePointKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrameStatics'
    _iid_ = Guid('{e97a32c2-0a7a-4766-95cb-0d692611cb4c}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplitCloseThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation'
    _iid_ = Guid('{4f799518-ff39-4e90-bb74-2abd56027402}')
    @winrt_commethod(6)
    def get_OpenedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_OpenedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_OpenedTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_OpenedTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ClosedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ClosedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ClosedTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ClosedTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_ContentTargetName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ContentTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_ContentTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(17)
    def put_ContentTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
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
    def get_ContentTranslationDirection(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(25)
    def put_ContentTranslationDirection(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_commethod(26)
    def get_ContentTranslationOffset(self) -> Double: ...
    @winrt_commethod(27)
    def put_ContentTranslationOffset(self, value: Double) -> Void: ...
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
class ISplitCloseThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics'
    _iid_ = Guid('{7aa94de9-cc9b-4e90-a11a-0050a2216a9e}')
    @winrt_commethod(6)
    def get_OpenedTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OpenedTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ClosedTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ClosedTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ContentTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ContentTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_OpenedLengthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ClosedLengthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_OffsetFromCenterProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ContentTranslationDirectionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_ContentTranslationOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    ContentTargetProperty = property(get_ContentTargetProperty, None)
    ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
    OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    OpenedTargetProperty = property(get_OpenedTargetProperty, None)
class ISplitOpenThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation'
    _iid_ = Guid('{785fd7aa-5456-4639-8fd2-26bae6a5ffe4}')
    @winrt_commethod(6)
    def get_OpenedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_OpenedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_OpenedTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_OpenedTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ClosedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ClosedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ClosedTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ClosedTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_ContentTargetName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ContentTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_ContentTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(17)
    def put_ContentTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
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
    def get_ContentTranslationDirection(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(25)
    def put_ContentTranslationDirection(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_commethod(26)
    def get_ContentTranslationOffset(self) -> Double: ...
    @winrt_commethod(27)
    def put_ContentTranslationOffset(self, value: Double) -> Void: ...
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
class ISplitOpenThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics'
    _iid_ = Guid('{8d4cfa89-3a91-458d-b0fb-4cad625cbf8d}')
    @winrt_commethod(6)
    def get_OpenedTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OpenedTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ClosedTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ClosedTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ContentTargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ContentTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_OpenedLengthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ClosedLengthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_OffsetFromCenterProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ContentTranslationDirectionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_ContentTranslationOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    ContentTargetProperty = property(get_ContentTargetProperty, None)
    ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
    OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    OpenedTargetProperty = property(get_OpenedTargetProperty, None)
class IStoryboard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IStoryboard'
    _iid_ = Guid('{d45c1e6e-3594-460e-981a-32271bd3aa06}')
    @winrt_commethod(6)
    def get_Children(self) -> win32more.Windows.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_commethod(7)
    def Seek(self, offset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def Begin(self) -> Void: ...
    @winrt_commethod(10)
    def Pause(self) -> Void: ...
    @winrt_commethod(11)
    def Resume(self) -> Void: ...
    @winrt_commethod(12)
    def GetCurrentState(self) -> win32more.Windows.UI.Xaml.Media.Animation.ClockState: ...
    @winrt_commethod(13)
    def GetCurrentTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def SeekAlignedToLastTick(self, offset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(15)
    def SkipToFill(self) -> Void: ...
    Children = property(get_Children, None)
class IStoryboardStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.IStoryboardStatics'
    _iid_ = Guid('{d82f07d8-73d5-4379-bd48-7e05184a8bad}')
    @winrt_commethod(6)
    def get_TargetPropertyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetTargetProperty(self, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetTargetProperty(self, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline, path: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetTargetName(self, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetTargetName(self, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline, name: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def SetTarget(self, timeline: win32more.Windows.UI.Xaml.Media.Animation.Timeline, target: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    TargetPropertyProperty = property(get_TargetPropertyProperty, None)
class ISuppressNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISuppressNavigationTransitionInfo'
    _iid_ = Guid('{244d7b0c-b1b7-4871-9d3e-d56203a3a5b4}')
class ISwipeBackThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
class ISwipeBackThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics'
    _iid_ = Guid('{693f31bf-4da6-468a-8ce0-996c9aad42e0}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class ISwipeHintThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics'
    _iid_ = Guid('{23d61a57-9115-4d63-b04a-b89f1c744dc0}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToHorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ToVerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToHorizontalOffsetProperty = property(get_ToHorizontalOffsetProperty, None)
    ToVerticalOffsetProperty = property(get_ToVerticalOffsetProperty, None)
class ITimeline(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITimeline'
    _iid_ = Guid('{0bc465dc-be4d-4d0d-9549-2208b715f40d}')
    @winrt_commethod(6)
    def get_AutoReverse(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AutoReverse(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_BeginTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def put_BeginTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(10)
    def get_Duration(self) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_commethod(11)
    def put_Duration(self, value: win32more.Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_commethod(12)
    def get_SpeedRatio(self) -> Double: ...
    @winrt_commethod(13)
    def put_SpeedRatio(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_FillBehavior(self) -> win32more.Windows.UI.Xaml.Media.Animation.FillBehavior: ...
    @winrt_commethod(15)
    def put_FillBehavior(self, value: win32more.Windows.UI.Xaml.Media.Animation.FillBehavior) -> Void: ...
    @winrt_commethod(16)
    def get_RepeatBehavior(self) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(17)
    def put_RepeatBehavior(self, value: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Void: ...
    @winrt_commethod(18)
    def add_Completed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_Completed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoReverse = property(get_AutoReverse, put_AutoReverse)
    BeginTime = property(get_BeginTime, put_BeginTime)
    Duration = property(get_Duration, put_Duration)
    FillBehavior = property(get_FillBehavior, put_FillBehavior)
    RepeatBehavior = property(get_RepeatBehavior, put_RepeatBehavior)
    SpeedRatio = property(get_SpeedRatio, put_SpeedRatio)
    Completed = event()
class ITimelineFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITimelineFactory'
    _iid_ = Guid('{1d56bb07-bda4-478b-8ada-eb04d580cd5e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.Timeline: ...
class ITimelineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITimelineStatics'
    _iid_ = Guid('{a902ed4e-ef10-4d6f-9a40-93cb8895f4e5}')
    @winrt_commethod(6)
    def get_AllowDependentAnimations(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowDependentAnimations(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AutoReverseProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_BeginTimeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DurationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_SpeedRatioProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_FillBehaviorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_RepeatBehaviorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AllowDependentAnimations = property(get_AllowDependentAnimations, put_AllowDependentAnimations)
    AutoReverseProperty = property(get_AutoReverseProperty, None)
    BeginTimeProperty = property(get_BeginTimeProperty, None)
    DurationProperty = property(get_DurationProperty, None)
    FillBehaviorProperty = property(get_FillBehaviorProperty, None)
    RepeatBehaviorProperty = property(get_RepeatBehaviorProperty, None)
    SpeedRatioProperty = property(get_SpeedRatioProperty, None)
class ITransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITransition'
    _iid_ = Guid('{3c677c7c-01d0-4dce-b333-976f93312b08}')
class ITransitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ITransitionFactory'
    _iid_ = Guid('{dc9ab2cf-3bc9-44aa-b3fc-883a83233a2c}')
class KeySpline(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IKeySpline
    _classid_ = 'Windows.UI.Xaml.Media.Animation.KeySpline'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.KeySpline.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def get_ControlPoint1(self: win32more.Windows.UI.Xaml.Media.Animation.IKeySpline) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_ControlPoint1(self: win32more.Windows.UI.Xaml.Media.Animation.IKeySpline, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_ControlPoint2(self: win32more.Windows.UI.Xaml.Media.Animation.IKeySpline) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_ControlPoint2(self: win32more.Windows.UI.Xaml.Media.Animation.IKeySpline, value: win32more.Windows.Foundation.Point) -> Void: ...
    ControlPoint1 = property(get_ControlPoint1, put_ControlPoint1)
    ControlPoint2 = property(get_ControlPoint2, put_ControlPoint2)
class KeyTime(Structure):
    TimeSpan: win32more.Windows.Foundation.TimeSpan
class KeyTimeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IKeyTimeHelper
    _classid_ = 'Windows.UI.Xaml.Media.Animation.KeyTimeHelper'
    @winrt_classmethod
    def FromTimeSpan(cls: win32more.Windows.UI.Xaml.Media.Animation.IKeyTimeHelperStatics, timeSpan: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
class LinearColorKeyFrame(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ILinearColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.LinearColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.LinearColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.LinearColorKeyFrame: ...
class LinearDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ILinearDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.LinearDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.LinearDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.LinearDoubleKeyFrame: ...
class LinearPointKeyFrame(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ILinearPointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.LinearPointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.LinearPointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.LinearPointKeyFrame: ...
class _NavigationThemeTransition_Meta_(ComPtr.__class__):
    pass
class NavigationThemeTransition(ComPtr, metaclass=_NavigationThemeTransition_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.INavigationThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.NavigationThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.NavigationThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationThemeTransition: ...
    @winrt_mixinmethod
    def get_DefaultNavigationTransitionInfo(self: win32more.Windows.UI.Xaml.Media.Animation.INavigationThemeTransition) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def put_DefaultNavigationTransitionInfo(self: win32more.Windows.UI.Xaml.Media.Animation.INavigationThemeTransition, value: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    @winrt_classmethod
    def get_DefaultNavigationTransitionInfoProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.INavigationThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
    _NavigationThemeTransition_Meta_.DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class NavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.INavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def GetNavigationStateCore(self: win32more.Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetNavigationStateCore(self: win32more.Windows.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides, navigationState: WinRT_String) -> Void: ...
class _ObjectAnimationUsingKeyFrames_Meta_(ComPtr.__class__):
    pass
class ObjectAnimationUsingKeyFrames(ComPtr, metaclass=_ObjectAnimationUsingKeyFrames_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames) -> win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFramesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _ObjectAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _ObjectKeyFrame_Meta_(ComPtr.__class__):
    pass
class ObjectKeyFrame(ComPtr, metaclass=_ObjectKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ObjectKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrame) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrame, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _ObjectKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _ObjectKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class ObjectKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame], items: PassArray[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Animation.ObjectKeyFrame]: ...
    Size = property(get_Size, None)
class _PaneThemeTransition_Meta_(ComPtr.__class__):
    pass
class PaneThemeTransition(ComPtr, metaclass=_PaneThemeTransition_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPaneThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PaneThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PaneThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PaneThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: win32more.Windows.UI.Xaml.Media.Animation.IPaneThemeTransition) -> win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: win32more.Windows.UI.Xaml.Media.Animation.IPaneThemeTransition, value: win32more.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPaneThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    _PaneThemeTransition_Meta_.EdgeProperty = property(get_EdgeProperty, None)
class _PointAnimation_Meta_(ComPtr.__class__):
    pass
class PointAnimation(ComPtr, metaclass=_PointAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PointAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PointAnimation: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_By(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    By = property(get_By, put_By)
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    From = property(get_From, put_From)
    To = property(get_To, put_To)
    _PointAnimation_Meta_.ByProperty = property(get_ByProperty, None)
    _PointAnimation_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    _PointAnimation_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    _PointAnimation_Meta_.FromProperty = property(get_FromProperty, None)
    _PointAnimation_Meta_.ToProperty = property(get_ToProperty, None)
class _PointAnimationUsingKeyFrames_Meta_(ComPtr.__class__):
    pass
class PointAnimationUsingKeyFrames(ComPtr, metaclass=_PointAnimationUsingKeyFrames_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames) -> win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFramesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _PointAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _PointKeyFrame_Meta_(ComPtr.__class__):
    pass
class PointKeyFrame(ComPtr, metaclass=_PointKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrame) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrame, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _PointKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _PointKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class PointKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], value: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame], items: PassArray[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame]: ...
    Size = property(get_Size, None)
class _PointerDownThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PointerDownThemeAnimation(ComPtr, metaclass=_PointerDownThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointerDownThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PointerDownThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PointerDownThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointerDownThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _PointerDownThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PointerUpThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PointerUpThemeAnimation(ComPtr, metaclass=_PointerUpThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PointerUpThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PointerUpThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PointerUpThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPointerUpThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _PointerUpThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PopInThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PopInThemeAnimation(ComPtr, metaclass=_PopInThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PopInThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PopInThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PopInThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
    _PopInThemeAnimation_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _PopInThemeAnimation_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _PopInThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PopOutThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PopOutThemeAnimation(ComPtr, metaclass=_PopOutThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PopOutThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PopOutThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PopOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPopOutThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _PopOutThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PopupThemeTransition_Meta_(ComPtr.__class__):
    pass
class PopupThemeTransition(ComPtr, metaclass=_PopupThemeTransition_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPopupThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PopupThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PopupThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PopupThemeTransition: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopupThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopupThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopupThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IPopupThemeTransition, value: Double) -> Void: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    _PopupThemeTransition_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _PopupThemeTransition_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class _PowerEase_Meta_(ComPtr.__class__):
    pass
class PowerEase(ComPtr, metaclass=_PowerEase_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IPowerEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.PowerEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.PowerEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.PowerEase: ...
    @winrt_mixinmethod
    def get_Power(self: win32more.Windows.UI.Xaml.Media.Animation.IPowerEase) -> Double: ...
    @winrt_mixinmethod
    def put_Power(self: win32more.Windows.UI.Xaml.Media.Animation.IPowerEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_PowerProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IPowerEaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Power = property(get_Power, put_Power)
    _PowerEase_Meta_.PowerProperty = property(get_PowerProperty, None)
class QuadraticEase(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IQuadraticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.QuadraticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.QuadraticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.QuadraticEase: ...
class QuarticEase(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IQuarticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.QuarticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.QuarticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.QuarticEase: ...
class QuinticEase(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IQuinticEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.QuinticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.QuinticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.QuinticEase: ...
class ReorderThemeTransition(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IReorderThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.ReorderThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.ReorderThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.ReorderThemeTransition: ...
class RepeatBehavior(Structure):
    Count: Double
    Duration: win32more.Windows.Foundation.TimeSpan
    Type: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehaviorType
class _RepeatBehaviorHelper_Meta_(ComPtr.__class__):
    pass
class RepeatBehaviorHelper(ComPtr, metaclass=_RepeatBehaviorHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelper
    _classid_ = 'Windows.UI.Xaml.Media.Animation.RepeatBehaviorHelper'
    @winrt_classmethod
    def get_Forever(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def FromCount(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, count: Double) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def FromDuration(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def GetHasCount(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_classmethod
    def GetHasDuration(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior, value: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    _RepeatBehaviorHelper_Meta_.Forever = property(get_Forever, None)
class RepeatBehaviorType(Enum, Int32):
    Count = 0
    Duration = 1
    Forever = 2
class _RepositionThemeAnimation_Meta_(ComPtr.__class__):
    pass
class RepositionThemeAnimation(ComPtr, metaclass=_RepositionThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.RepositionThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.RepositionThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.RepositionThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
    _RepositionThemeAnimation_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _RepositionThemeAnimation_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _RepositionThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _RepositionThemeTransition_Meta_(ComPtr.__class__):
    pass
class RepositionThemeTransition(ComPtr, metaclass=_RepositionThemeTransition_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.RepositionThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.RepositionThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.RepositionThemeTransition: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeTransition2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IRepositionThemeTransitionStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    _RepositionThemeTransition_Meta_.IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class SineEase(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISineEase
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SineEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SineEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SineEase: ...
class SlideNavigationTransitionEffect(Enum, Int32):
    FromBottom = 0
    FromLeft = 1
    FromRight = 2
class _SlideNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class SlideNavigationTransitionInfo(ComPtr, metaclass=_SlideNavigationTransitionInfo_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_Effect(self: win32more.Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2) -> win32more.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_mixinmethod
    def put_Effect(self: win32more.Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo2, value: win32more.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    @winrt_classmethod
    def get_EffectProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfoStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Effect = property(get_Effect, put_Effect)
    _SlideNavigationTransitionInfo_Meta_.EffectProperty = property(get_EffectProperty, None)
class _SplineColorKeyFrame_Meta_(ComPtr.__class__):
    pass
class SplineColorKeyFrame(ComPtr, metaclass=_SplineColorKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplineColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SplineColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SplineColorKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: win32more.Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: win32more.Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplineColorKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    _SplineColorKeyFrame_Meta_.KeySplineProperty = property(get_KeySplineProperty, None)
class _SplineDoubleKeyFrame_Meta_(ComPtr.__class__):
    pass
class SplineDoubleKeyFrame(ComPtr, metaclass=_SplineDoubleKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplineDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SplineDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SplineDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: win32more.Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: win32more.Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplineDoubleKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    _SplineDoubleKeyFrame_Meta_.KeySplineProperty = property(get_KeySplineProperty, None)
class _SplinePointKeyFrame_Meta_(ComPtr.__class__):
    pass
class SplinePointKeyFrame(ComPtr, metaclass=_SplinePointKeyFrame_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplinePointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SplinePointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SplinePointKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: win32more.Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame) -> win32more.Windows.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: win32more.Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrame, value: win32more.Windows.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplinePointKeyFrameStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    _SplinePointKeyFrame_Meta_.KeySplineProperty = property(get_KeySplineProperty, None)
class _SplitCloseThemeAnimation_Meta_(ComPtr.__class__):
    pass
class SplitCloseThemeAnimation(ComPtr, metaclass=_SplitCloseThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplitCloseThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SplitCloseThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SplitCloseThemeAnimation: ...
    @winrt_mixinmethod
    def get_OpenedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OpenedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OpenedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClosedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ClosedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ContentTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OpenedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ClosedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetFromCenter(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetFromCenter(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationDirection(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_ContentTranslationDirection(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ContentTranslationOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OpenedTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedLengthProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedLengthProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetFromCenterProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationDirectionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
    _SplitCloseThemeAnimation_Meta_.ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    _SplitCloseThemeAnimation_Meta_.ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    _SplitCloseThemeAnimation_Meta_.ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    _SplitCloseThemeAnimation_Meta_.ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    _SplitCloseThemeAnimation_Meta_.ContentTargetProperty = property(get_ContentTargetProperty, None)
    _SplitCloseThemeAnimation_Meta_.ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    _SplitCloseThemeAnimation_Meta_.ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
    _SplitCloseThemeAnimation_Meta_.OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    _SplitCloseThemeAnimation_Meta_.OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    _SplitCloseThemeAnimation_Meta_.OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    _SplitCloseThemeAnimation_Meta_.OpenedTargetProperty = property(get_OpenedTargetProperty, None)
class _SplitOpenThemeAnimation_Meta_(ComPtr.__class__):
    pass
class SplitOpenThemeAnimation(ComPtr, metaclass=_SplitOpenThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SplitOpenThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SplitOpenThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SplitOpenThemeAnimation: ...
    @winrt_mixinmethod
    def get_OpenedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OpenedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OpenedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClosedTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ClosedTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentTargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ContentTarget(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OpenedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ClosedLength(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetFromCenter(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetFromCenter(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationDirection(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_ContentTranslationDirection(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ContentTranslationOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OpenedTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedLengthProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedLengthProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetFromCenterProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationDirectionProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ClosedLength = property(get_ClosedLength, put_ClosedLength)
    ClosedTarget = property(get_ClosedTarget, put_ClosedTarget)
    ClosedTargetName = property(get_ClosedTargetName, put_ClosedTargetName)
    ContentTarget = property(get_ContentTarget, put_ContentTarget)
    ContentTargetName = property(get_ContentTargetName, put_ContentTargetName)
    ContentTranslationDirection = property(get_ContentTranslationDirection, put_ContentTranslationDirection)
    ContentTranslationOffset = property(get_ContentTranslationOffset, put_ContentTranslationOffset)
    OffsetFromCenter = property(get_OffsetFromCenter, put_OffsetFromCenter)
    OpenedLength = property(get_OpenedLength, put_OpenedLength)
    OpenedTarget = property(get_OpenedTarget, put_OpenedTarget)
    OpenedTargetName = property(get_OpenedTargetName, put_OpenedTargetName)
    _SplitOpenThemeAnimation_Meta_.ClosedLengthProperty = property(get_ClosedLengthProperty, None)
    _SplitOpenThemeAnimation_Meta_.ClosedTargetNameProperty = property(get_ClosedTargetNameProperty, None)
    _SplitOpenThemeAnimation_Meta_.ClosedTargetProperty = property(get_ClosedTargetProperty, None)
    _SplitOpenThemeAnimation_Meta_.ContentTargetNameProperty = property(get_ContentTargetNameProperty, None)
    _SplitOpenThemeAnimation_Meta_.ContentTargetProperty = property(get_ContentTargetProperty, None)
    _SplitOpenThemeAnimation_Meta_.ContentTranslationDirectionProperty = property(get_ContentTranslationDirectionProperty, None)
    _SplitOpenThemeAnimation_Meta_.ContentTranslationOffsetProperty = property(get_ContentTranslationOffsetProperty, None)
    _SplitOpenThemeAnimation_Meta_.OffsetFromCenterProperty = property(get_OffsetFromCenterProperty, None)
    _SplitOpenThemeAnimation_Meta_.OpenedLengthProperty = property(get_OpenedLengthProperty, None)
    _SplitOpenThemeAnimation_Meta_.OpenedTargetNameProperty = property(get_OpenedTargetNameProperty, None)
    _SplitOpenThemeAnimation_Meta_.OpenedTargetProperty = property(get_OpenedTargetProperty, None)
class _Storyboard_Meta_(ComPtr.__class__):
    pass
class Storyboard(ComPtr, metaclass=_Storyboard_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard
    _classid_ = 'Windows.UI.Xaml.Media.Animation.Storyboard'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.Storyboard.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> win32more.Windows.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard, offset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Begin(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentState(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> win32more.Windows.UI.Xaml.Media.Animation.ClockState: ...
    @winrt_mixinmethod
    def GetCurrentTime(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SeekAlignedToLastTick(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard, offset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SkipToFill(self: win32more.Windows.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_classmethod
    def get_TargetPropertyProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IStoryboardStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_classmethod
    def SetTargetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline, path: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.IStoryboardStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTargetName(cls: win32more.Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_classmethod
    def SetTargetName(cls: win32more.Windows.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Windows.UI.Xaml.Media.Animation.Timeline, name: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetTarget(cls: win32more.Windows.UI.Xaml.Media.Animation.IStoryboardStatics, timeline: win32more.Windows.UI.Xaml.Media.Animation.Timeline, target: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    Children = property(get_Children, None)
    _Storyboard_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
    _Storyboard_Meta_.TargetPropertyProperty = property(get_TargetPropertyProperty, None)
class SuppressNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISuppressNavigationTransitionInfo
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo: ...
class _SwipeBackThemeAnimation_Meta_(ComPtr.__class__):
    pass
class SwipeBackThemeAnimation(ComPtr, metaclass=_SwipeBackThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SwipeBackThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SwipeBackThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SwipeBackThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
    _SwipeBackThemeAnimation_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _SwipeBackThemeAnimation_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _SwipeBackThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _SwipeHintThemeAnimation_Meta_(ComPtr.__class__):
    pass
class SwipeHintThemeAnimation(ComPtr, metaclass=_SwipeHintThemeAnimation_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation
    _classid_ = 'Windows.UI.Xaml.Media.Animation.SwipeHintThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.SwipeHintThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.SwipeHintThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ToHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToHorizontalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ToVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToVerticalOffset(self: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToHorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToVerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    ToHorizontalOffset = property(get_ToHorizontalOffset, put_ToHorizontalOffset)
    ToVerticalOffset = property(get_ToVerticalOffset, put_ToVerticalOffset)
    _SwipeHintThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
    _SwipeHintThemeAnimation_Meta_.ToHorizontalOffsetProperty = property(get_ToHorizontalOffsetProperty, None)
    _SwipeHintThemeAnimation_Meta_.ToVerticalOffsetProperty = property(get_ToVerticalOffsetProperty, None)
class _Timeline_Meta_(ComPtr.__class__):
    pass
class Timeline(ComPtr, metaclass=_Timeline_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ITimeline
    _classid_ = 'Windows.UI.Xaml.Media.Animation.Timeline'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.Timeline.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Animation.Timeline: ...
    @winrt_mixinmethod
    def get_AutoReverse(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoReverse(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BeginTime(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_BeginTime(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, value: win32more.Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_mixinmethod
    def get_SpeedRatio(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline) -> Double: ...
    @winrt_mixinmethod
    def put_SpeedRatio(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FillBehavior(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline) -> win32more.Windows.UI.Xaml.Media.Animation.FillBehavior: ...
    @winrt_mixinmethod
    def put_FillBehavior(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, value: win32more.Windows.UI.Xaml.Media.Animation.FillBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_RepeatBehavior(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline) -> win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_mixinmethod
    def put_RepeatBehavior(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, value: win32more.Windows.UI.Xaml.Media.Animation.RepeatBehavior) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.UI.Xaml.Media.Animation.ITimeline, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AllowDependentAnimations(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> Boolean: ...
    @winrt_classmethod
    def put_AllowDependentAnimations(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_AutoReverseProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BeginTimeProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DurationProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SpeedRatioProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FillBehaviorProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RepeatBehaviorProperty(cls: win32more.Windows.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AutoReverse = property(get_AutoReverse, put_AutoReverse)
    BeginTime = property(get_BeginTime, put_BeginTime)
    Duration = property(get_Duration, put_Duration)
    FillBehavior = property(get_FillBehavior, put_FillBehavior)
    RepeatBehavior = property(get_RepeatBehavior, put_RepeatBehavior)
    SpeedRatio = property(get_SpeedRatio, put_SpeedRatio)
    _Timeline_Meta_.AllowDependentAnimations = property(get_AllowDependentAnimations, put_AllowDependentAnimations)
    _Timeline_Meta_.AutoReverseProperty = property(get_AutoReverseProperty, None)
    _Timeline_Meta_.BeginTimeProperty = property(get_BeginTimeProperty, None)
    _Timeline_Meta_.DurationProperty = property(get_DurationProperty, None)
    _Timeline_Meta_.FillBehaviorProperty = property(get_FillBehaviorProperty, None)
    _Timeline_Meta_.RepeatBehaviorProperty = property(get_RepeatBehaviorProperty, None)
    _Timeline_Meta_.SpeedRatioProperty = property(get_SpeedRatioProperty, None)
    Completed = event()
class TimelineCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Animation.Timeline]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.TimelineCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.TimelineCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Animation.Timeline: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Animation.Timeline]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], value: win32more.Windows.UI.Xaml.Media.Animation.Timeline, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], value: win32more.Windows.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Animation.Timeline]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Timeline], items: PassArray[win32more.Windows.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Animation.Timeline]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Animation.Timeline]: ...
    Size = property(get_Size, None)
class Transition(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Animation.ITransition
    _classid_ = 'Windows.UI.Xaml.Media.Animation.Transition'
class TransitionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Animation.Transition]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition]
    _classid_ = 'Windows.UI.Xaml.Media.Animation.TransitionCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Animation.Transition: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Animation.Transition]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], value: win32more.Windows.UI.Xaml.Media.Animation.Transition, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], value: win32more.Windows.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Animation.Transition]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Animation.Transition], items: PassArray[win32more.Windows.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Animation.Transition]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Animation.Transition]: ...
    Size = property(get_Size, None)


make_ready(__name__)
