from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Controls
import win32more.Microsoft.UI.Xaml.Controls.Primitives
import win32more.Microsoft.UI.Xaml.Media.Animation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class AddDeleteThemeTransition(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IAddDeleteThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.AddDeleteThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.AddDeleteThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.AddDeleteThemeTransition: ...
class _BackEase_Meta_(ComPtr.__class__):
    pass
class BackEase(ComPtr, metaclass=_BackEase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IBackEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.BackEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.BackEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.BackEase: ...
    @winrt_mixinmethod
    def get_Amplitude(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBackEase) -> Double: ...
    @winrt_mixinmethod
    def put_Amplitude(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBackEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_AmplitudeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IBackEaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
    _BackEase_Meta_.AmplitudeProperty = property(get_AmplitudeProperty, None)
class BasicConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfiguration
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfigurationFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration: ...
class _BeginStoryboard_Meta_(ComPtr.__class__):
    pass
class BeginStoryboard(ComPtr, metaclass=_BeginStoryboard_Meta_):
    extends: win32more.Microsoft.UI.Xaml.TriggerAction
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IBeginStoryboard
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.BeginStoryboard'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.BeginStoryboard.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.BeginStoryboard: ...
    @winrt_mixinmethod
    def get_Storyboard(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBeginStoryboard) -> win32more.Microsoft.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBeginStoryboard, value: win32more.Microsoft.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    @winrt_classmethod
    def get_StoryboardProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IBeginStoryboardStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
    _BeginStoryboard_Meta_.StoryboardProperty = property(get_StoryboardProperty, None)
class _BounceEase_Meta_(ComPtr.__class__):
    pass
class BounceEase(ComPtr, metaclass=_BounceEase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IBounceEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.BounceEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.BounceEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.BounceEase: ...
    @winrt_mixinmethod
    def get_Bounces(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBounceEase) -> Int32: ...
    @winrt_mixinmethod
    def put_Bounces(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBounceEase, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Bounciness(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBounceEase) -> Double: ...
    @winrt_mixinmethod
    def put_Bounciness(self: win32more.Microsoft.UI.Xaml.Media.Animation.IBounceEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_BouncesProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IBounceEaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BouncinessProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IBounceEaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Bounces = property(get_Bounces, put_Bounces)
    Bounciness = property(get_Bounciness, put_Bounciness)
    _BounceEase_Meta_.BouncesProperty = property(get_BouncesProperty, None)
    _BounceEase_Meta_.BouncinessProperty = property(get_BouncinessProperty, None)
class CircleEase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ICircleEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.CircleEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.CircleEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.CircleEase: ...
class ClockState(Enum, Int32):
    Active = 0
    Filling = 1
    Stopped = 2
class _ColorAnimation_Meta_(ComPtr.__class__):
    pass
class ColorAnimation(ComPtr, metaclass=_ColorAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ColorAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ColorAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorAnimation: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_By(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFramesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _ColorAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _ColorKeyFrame_Meta_(ComPtr.__class__):
    pass
class ColorKeyFrame(ComPtr, metaclass=_ColorKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrame) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrame, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IColorKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _ColorKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _ColorKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class ColorKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ColorKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame]: ...
    Size = property(get_Size, None)
class _CommonNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class CommonNavigationTransitionInfo(ComPtr, metaclass=_CommonNavigationTransitionInfo_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.CommonNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStaggerElementProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsStaggerElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsStaggerElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    _CommonNavigationTransitionInfo_Meta_.IsStaggerElementProperty = property(get_IsStaggerElementProperty, None)
    _CommonNavigationTransitionInfo_Meta_.IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class ConnectedAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ConnectedAnimation'
    @winrt_mixinmethod
    def get_IsScaleAnimationEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScaleAnimationEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration: ...
    @winrt_mixinmethod
    def put_Configuration(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation, value: win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryStart(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation, destination: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_mixinmethod
    def TryStartWithCoordinatedElements(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation, destination: win32more.Microsoft.UI.Xaml.UIElement, coordinatedElements: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]) -> Boolean: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation) -> Void: ...
    @winrt_mixinmethod
    def SetAnimationComponent(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation, component: win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationComponent, animation: win32more.Microsoft.UI.Composition.ICompositionAnimationBase) -> Void: ...
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
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationConfiguration
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration'
class ConnectedAnimationService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationService'
    @winrt_mixinmethod
    def get_DefaultDuration(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DefaultDuration(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultEasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService) -> win32more.Microsoft.UI.Composition.CompositionEasingFunction: ...
    @winrt_mixinmethod
    def put_DefaultEasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService, value: win32more.Microsoft.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_mixinmethod
    def PrepareToAnimate(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService, key: WinRT_String, source: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_mixinmethod
    def GetAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService, key: WinRT_String) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationServiceStatics) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationService: ...
    DefaultDuration = property(get_DefaultDuration, put_DefaultDuration)
    DefaultEasingFunction = property(get_DefaultEasingFunction, put_DefaultEasingFunction)
class _ContentThemeTransition_Meta_(ComPtr.__class__):
    pass
class ContentThemeTransition(ComPtr, metaclass=_ContentThemeTransition_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IContentThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ContentThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ContentThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ContentThemeTransition: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IContentThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IContentThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IContentThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IContentThemeTransition, value: Double) -> Void: ...
    @winrt_classmethod
    def get_HorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContentThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContentThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    _ContentThemeTransition_Meta_.HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    _ContentThemeTransition_Meta_.VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class _ContinuumNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class ContinuumNavigationTransitionInfo(ComPtr, metaclass=_ContinuumNavigationTransitionInfo_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ContinuumNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_ExitElement(self: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_ExitElement(self: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_ExitElementProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsEntranceElementProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsEntranceElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsEntranceElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsExitElementProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsExitElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsExitElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ExitElementContainerProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetExitElementContainer(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.Controls.ListViewBase) -> Boolean: ...
    @winrt_classmethod
    def SetExitElementContainer(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.Controls.ListViewBase, value: Boolean) -> Void: ...
    ExitElement = property(get_ExitElement, put_ExitElement)
    _ContinuumNavigationTransitionInfo_Meta_.ExitElementContainerProperty = property(get_ExitElementContainerProperty, None)
    _ContinuumNavigationTransitionInfo_Meta_.ExitElementProperty = property(get_ExitElementProperty, None)
    _ContinuumNavigationTransitionInfo_Meta_.IsEntranceElementProperty = property(get_IsEntranceElementProperty, None)
    _ContinuumNavigationTransitionInfo_Meta_.IsExitElementProperty = property(get_IsExitElementProperty, None)
class CubicEase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ICubicEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.CubicEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.CubicEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.CubicEase: ...
class DirectConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfiguration
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfigurationFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration: ...
class DiscreteColorKeyFrame(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDiscreteColorKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DiscreteColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DiscreteColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DiscreteColorKeyFrame: ...
class DiscreteDoubleKeyFrame(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDiscreteDoubleKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DiscreteDoubleKeyFrame: ...
class DiscreteObjectKeyFrame(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDiscreteObjectKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DiscreteObjectKeyFrame: ...
class DiscretePointKeyFrame(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDiscretePointKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DiscretePointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DiscretePointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DiscretePointKeyFrame: ...
class _DoubleAnimation_Meta_(ComPtr.__class__):
    pass
class DoubleAnimation(ComPtr, metaclass=_DoubleAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DoubleAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DoubleAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleAnimation: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_By(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFramesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _DoubleAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _DoubleKeyFrame_Meta_(ComPtr.__class__):
    pass
class DoubleKeyFrame(ComPtr, metaclass=_DoubleKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrame) -> Double: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrame, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _DoubleKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _DoubleKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class DoubleKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame]: ...
    Size = property(get_Size, None)
class _DragItemThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DragItemThemeAnimation(ComPtr, metaclass=_DragItemThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDragItemThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DragItemThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DragItemThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DragItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDragItemThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _DragItemThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _DragOverThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DragOverThemeAnimation(ComPtr, metaclass=_DragOverThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DragOverThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DragOverThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DragOverThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ToOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DirectionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Direction = property(get_Direction, put_Direction)
    TargetName = property(get_TargetName, put_TargetName)
    ToOffset = property(get_ToOffset, put_ToOffset)
    _DragOverThemeAnimation_Meta_.DirectionProperty = property(get_DirectionProperty, None)
    _DragOverThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
    _DragOverThemeAnimation_Meta_.ToOffsetProperty = property(get_ToOffsetProperty, None)
class DrillInNavigationTransitionInfo(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInNavigationTransitionInfo
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DrillInNavigationTransitionInfo: ...
class _DrillInThemeAnimation_Meta_(ComPtr.__class__):
    pass
class DrillInThemeAnimation(ComPtr, metaclass=_DrillInThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DrillInThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DrillInThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DrillInThemeAnimation: ...
    @winrt_mixinmethod
    def get_EntranceTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EntranceTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EntranceTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_EntranceTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ExitTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_EntranceTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EntranceTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DrillOutThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DrillOutThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DrillOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_EntranceTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EntranceTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EntranceTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_EntranceTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExitTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ExitTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_EntranceTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EntranceTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.DropTargetItemThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _DropTargetItemThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _EasingColorKeyFrame_Meta_(ComPtr.__class__):
    pass
class EasingColorKeyFrame(ComPtr, metaclass=_EasingColorKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingColorKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.EasingColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.EasingColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingColorKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingColorKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingColorKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingColorKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    _EasingColorKeyFrame_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class _EasingDoubleKeyFrame_Meta_(ComPtr.__class__):
    pass
class EasingDoubleKeyFrame(ComPtr, metaclass=_EasingDoubleKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.EasingDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.EasingDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingDoubleKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    _EasingDoubleKeyFrame_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class _EasingFunctionBase_Meta_(ComPtr.__class__):
    pass
class EasingFunctionBase(ComPtr, metaclass=_EasingFunctionBase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase'
    @winrt_mixinmethod
    def get_EasingMode(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBase) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_mixinmethod
    def put_EasingMode(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBase, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_mixinmethod
    def Ease(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBase, normalizedTime: Double) -> Double: ...
    @winrt_classmethod
    def get_EasingModeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
    _EasingFunctionBase_Meta_.EasingModeProperty = property(get_EasingModeProperty, None)
class EasingMode(Enum, Int32):
    EaseOut = 0
    EaseIn = 1
    EaseInOut = 2
class _EasingPointKeyFrame_Meta_(ComPtr.__class__):
    pass
class EasingPointKeyFrame(ComPtr, metaclass=_EasingPointKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingPointKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.EasingPointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.EasingPointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingPointKeyFrame: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingPointKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingPointKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEasingPointKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
    _EasingPointKeyFrame_Meta_.EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class _EdgeUIThemeTransition_Meta_(ComPtr.__class__):
    pass
class EdgeUIThemeTransition(ComPtr, metaclass=_EdgeUIThemeTransition_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IEdgeUIThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.EdgeUIThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.EdgeUIThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.EdgeUIThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEdgeUIThemeTransition) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEdgeUIThemeTransition, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEdgeUIThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    _EdgeUIThemeTransition_Meta_.EdgeProperty = property(get_EdgeProperty, None)
class _ElasticEase_Meta_(ComPtr.__class__):
    pass
class ElasticEase(ComPtr, metaclass=_ElasticEase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IElasticEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ElasticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ElasticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ElasticEase: ...
    @winrt_mixinmethod
    def get_Oscillations(self: win32more.Microsoft.UI.Xaml.Media.Animation.IElasticEase) -> Int32: ...
    @winrt_mixinmethod
    def put_Oscillations(self: win32more.Microsoft.UI.Xaml.Media.Animation.IElasticEase, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Springiness(self: win32more.Microsoft.UI.Xaml.Media.Animation.IElasticEase) -> Double: ...
    @winrt_mixinmethod
    def put_Springiness(self: win32more.Microsoft.UI.Xaml.Media.Animation.IElasticEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OscillationsProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IElasticEaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SpringinessProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IElasticEaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Oscillations = property(get_Oscillations, put_Oscillations)
    Springiness = property(get_Springiness, put_Springiness)
    _ElasticEase_Meta_.OscillationsProperty = property(get_OscillationsProperty, None)
    _ElasticEase_Meta_.SpringinessProperty = property(get_SpringinessProperty, None)
class _EntranceNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class EntranceNavigationTransitionInfo(ComPtr, metaclass=_EntranceNavigationTransitionInfo_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfo
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.EntranceNavigationTransitionInfo: ...
    @winrt_classmethod
    def get_IsTargetElementProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsTargetElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_classmethod
    def SetIsTargetElement(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    _EntranceNavigationTransitionInfo_Meta_.IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class _EntranceThemeTransition_Meta_(ComPtr.__class__):
    pass
class EntranceThemeTransition(ComPtr, metaclass=_EntranceThemeTransition_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.EntranceThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.EntranceThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.EntranceThemeTransition: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    _EntranceThemeTransition_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _EntranceThemeTransition_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _EntranceThemeTransition_Meta_.IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class _ExponentialEase_Meta_(ComPtr.__class__):
    pass
class ExponentialEase(ComPtr, metaclass=_ExponentialEase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IExponentialEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ExponentialEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ExponentialEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ExponentialEase: ...
    @winrt_mixinmethod
    def get_Exponent(self: win32more.Microsoft.UI.Xaml.Media.Animation.IExponentialEase) -> Double: ...
    @winrt_mixinmethod
    def put_Exponent(self: win32more.Microsoft.UI.Xaml.Media.Animation.IExponentialEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_ExponentProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IExponentialEaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Exponent = property(get_Exponent, put_Exponent)
    _ExponentialEase_Meta_.ExponentProperty = property(get_ExponentProperty, None)
class _FadeInThemeAnimation_Meta_(ComPtr.__class__):
    pass
class FadeInThemeAnimation(ComPtr, metaclass=_FadeInThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeInThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.FadeInThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.FadeInThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.FadeInThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _FadeInThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _FadeOutThemeAnimation_Meta_(ComPtr.__class__):
    pass
class FadeOutThemeAnimation(ComPtr, metaclass=_FadeOutThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeOutThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.FadeOutThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.FadeOutThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.FadeOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IFadeOutThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _FadeOutThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class FillBehavior(Enum, Int32):
    HoldEnd = 0
    Stop = 1
class GravityConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfigurationFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration: ...
    @winrt_mixinmethod
    def get_IsShadowEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsShadowEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IAddDeleteThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IAddDeleteThemeTransition'
    _iid_ = Guid('{3728595e-0ea2-524b-9348-86cfb860a0ff}')
class IBackEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBackEase'
    _iid_ = Guid('{1775bd43-1939-57cb-8c31-cd7590ec9543}')
    @winrt_commethod(6)
    def get_Amplitude(self) -> Double: ...
    @winrt_commethod(7)
    def put_Amplitude(self, value: Double) -> Void: ...
    Amplitude = property(get_Amplitude, put_Amplitude)
class IBackEaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBackEaseStatics'
    _iid_ = Guid('{1ead2ef9-7901-542d-ae08-7b5937b32ef0}')
    @winrt_commethod(6)
    def get_AmplitudeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AmplitudeProperty = property(get_AmplitudeProperty, None)
class IBasicConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfiguration'
    _iid_ = Guid('{7ff18afe-91e8-52fa-a1c1-7b2c1a140118}')
class IBasicConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBasicConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{2d156a02-0fb5-5ad1-af9b-bc9c2720fecb}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.BasicConnectedAnimationConfiguration: ...
class IBeginStoryboard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBeginStoryboard'
    _iid_ = Guid('{bb364720-ee5a-5b32-91e2-62589729fd3a}')
    @winrt_commethod(6)
    def get_Storyboard(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(7)
    def put_Storyboard(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    Storyboard = property(get_Storyboard, put_Storyboard)
class IBeginStoryboardStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBeginStoryboardStatics'
    _iid_ = Guid('{4d5fdbeb-6b0e-5a8f-a8f0-01f438df8fb2}')
    @winrt_commethod(6)
    def get_StoryboardProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    StoryboardProperty = property(get_StoryboardProperty, None)
class IBounceEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBounceEase'
    _iid_ = Guid('{c138bfff-87c8-5c60-b280-682a499c58c3}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IBounceEaseStatics'
    _iid_ = Guid('{d7716b38-c705-5093-96d6-735c13105a30}')
    @winrt_commethod(6)
    def get_BouncesProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_BouncinessProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    BouncesProperty = property(get_BouncesProperty, None)
    BouncinessProperty = property(get_BouncinessProperty, None)
class ICircleEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ICircleEase'
    _iid_ = Guid('{88209080-2929-5924-9b52-f95196568713}')
class IColorAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IColorAnimation'
    _iid_ = Guid('{6df862d2-65f2-53a8-8b1b-1b6c1763c175}')
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
    def get_EasingFunction(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IColorAnimationStatics'
    _iid_ = Guid('{99aebe0f-928e-52cb-842f-f43fe660ff06}')
    @winrt_commethod(6)
    def get_FromProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
class IColorAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFrames'
    _iid_ = Guid('{96f28c97-67eb-5393-8e37-a81d8fda18b3}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IColorAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IColorAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{5b0f4840-0ef7-5ad7-a8f2-d49424ed906f}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IColorKeyFrame'
    _iid_ = Guid('{02848c7e-c772-5f66-842b-fd494d0da669}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IColorKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IColorKeyFrameFactory'
    _iid_ = Guid('{a82cc182-9d80-508c-b962-d74225587200}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame: ...
class IColorKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IColorKeyFrameStatics'
    _iid_ = Guid('{b62fdd68-15c7-5c6c-a4fa-0cee10e04556}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class ICommonNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfo'
    _iid_ = Guid('{b21cc95f-9e3d-540a-b35a-17b99dc41b1e}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class ICommonNavigationTransitionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ICommonNavigationTransitionInfoStatics'
    _iid_ = Guid('{20020be1-c1ba-59f5-997a-c04f5e3833b0}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsStaggerElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetIsStaggerElement(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def SetIsStaggerElement(self, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsStaggerElementProperty = property(get_IsStaggerElementProperty, None)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class IConnectedAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IConnectedAnimation'
    _iid_ = Guid('{a9c1c6ad-7670-589c-a608-9b5c01cec71f}')
    @winrt_commethod(6)
    def get_IsScaleAnimationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsScaleAnimationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Configuration(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration: ...
    @winrt_commethod(9)
    def put_Configuration(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationConfiguration) -> Void: ...
    @winrt_commethod(10)
    def add_Completed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Completed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def TryStart(self, destination: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(13)
    def TryStartWithCoordinatedElements(self, destination: win32more.Microsoft.UI.Xaml.UIElement, coordinatedElements: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]) -> Boolean: ...
    @winrt_commethod(14)
    def Cancel(self) -> Void: ...
    @winrt_commethod(15)
    def SetAnimationComponent(self, component: win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationComponent, animation: win32more.Microsoft.UI.Composition.ICompositionAnimationBase) -> Void: ...
    Configuration = property(get_Configuration, put_Configuration)
    IsScaleAnimationEnabled = property(get_IsScaleAnimationEnabled, put_IsScaleAnimationEnabled)
    Completed = event()
class IConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationConfiguration'
    _iid_ = Guid('{e848379d-7e25-5976-bfb3-086bac4e8849}')
class IConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{71008845-4a12-5a1a-969c-4152b5174922}')
class IConnectedAnimationService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationService'
    _iid_ = Guid('{85f72163-c3c8-586a-91fe-3e0315a3a4fc}')
    @winrt_commethod(6)
    def get_DefaultDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DefaultDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultEasingFunction(self) -> win32more.Microsoft.UI.Composition.CompositionEasingFunction: ...
    @winrt_commethod(9)
    def put_DefaultEasingFunction(self, value: win32more.Microsoft.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_commethod(10)
    def PrepareToAnimate(self, key: WinRT_String, source: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    @winrt_commethod(11)
    def GetAnimation(self, key: WinRT_String) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimation: ...
    DefaultDuration = property(get_DefaultDuration, put_DefaultDuration)
    DefaultEasingFunction = property(get_DefaultEasingFunction, put_DefaultEasingFunction)
class IConnectedAnimationServiceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IConnectedAnimationServiceStatics'
    _iid_ = Guid('{f30ad68d-3426-5564-92c6-288b819e652a}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.ConnectedAnimationService: ...
class IContentThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IContentThemeTransition'
    _iid_ = Guid('{dff47071-cc51-556c-a3fe-8bbb4cba6195}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IContentThemeTransitionStatics'
    _iid_ = Guid('{95cda8b1-6667-56e3-be40-866eef53663c}')
    @winrt_commethod(6)
    def get_HorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class IContinuumNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfo'
    _iid_ = Guid('{c55da70f-ff2a-5fc3-81c5-9670f4d78752}')
    @winrt_commethod(6)
    def get_ExitElement(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_ExitElement(self, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    ExitElement = property(get_ExitElement, put_ExitElement)
class IContinuumNavigationTransitionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IContinuumNavigationTransitionInfoStatics'
    _iid_ = Guid('{ca9006fd-f513-5f34-ad7f-49f9d7a99432}')
    @winrt_commethod(6)
    def get_ExitElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsEntranceElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetIsEntranceElement(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(9)
    def SetIsEntranceElement(self, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsExitElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def GetIsExitElement(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(12)
    def SetIsExitElement(self, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_ExitElementContainerProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def GetExitElementContainer(self, element: win32more.Microsoft.UI.Xaml.Controls.ListViewBase) -> Boolean: ...
    @winrt_commethod(15)
    def SetExitElementContainer(self, element: win32more.Microsoft.UI.Xaml.Controls.ListViewBase, value: Boolean) -> Void: ...
    ExitElementContainerProperty = property(get_ExitElementContainerProperty, None)
    ExitElementProperty = property(get_ExitElementProperty, None)
    IsEntranceElementProperty = property(get_IsEntranceElementProperty, None)
    IsExitElementProperty = property(get_IsExitElementProperty, None)
class ICubicEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ICubicEase'
    _iid_ = Guid('{01a218b4-eb7e-54f9-bfb6-c6ee128013d2}')
class IDirectConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfiguration'
    _iid_ = Guid('{44f192eb-cc11-545e-8fa2-1f0ec9c4438a}')
class IDirectConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDirectConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{604aba9b-4eb8-5310-91dc-30962e25ab00}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.DirectConnectedAnimationConfiguration: ...
class IDiscreteColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDiscreteColorKeyFrame'
    _iid_ = Guid('{9b3d88a7-31d3-5912-8646-641a8a565ca1}')
class IDiscreteDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDiscreteDoubleKeyFrame'
    _iid_ = Guid('{ec16a555-c083-5a18-805b-a14b90bc80e2}')
class IDiscreteObjectKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDiscreteObjectKeyFrame'
    _iid_ = Guid('{542fa813-6892-559d-9f69-1f2ac666af13}')
class IDiscretePointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDiscretePointKeyFrame'
    _iid_ = Guid('{2255a291-007e-57ce-aa53-97d1e4a0d7e2}')
class IDoubleAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDoubleAnimation'
    _iid_ = Guid('{651ec97e-e483-5985-aa0b-49cfb07432dd}')
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
    def get_EasingFunction(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationStatics'
    _iid_ = Guid('{4e098387-adc6-5549-ad21-633e4fa244c2}')
    @winrt_commethod(6)
    def get_FromProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
class IDoubleAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFrames'
    _iid_ = Guid('{815437d5-63cf-54a5-aea5-24b84708d12d}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IDoubleAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDoubleAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{4c1c9bf1-3a03-5689-b18f-6c44251e13d9}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrame'
    _iid_ = Guid('{94c82ae6-ca62-5f52-934c-3e427e75d69a}')
    @winrt_commethod(6)
    def get_Value(self) -> Double: ...
    @winrt_commethod(7)
    def put_Value(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IDoubleKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrameFactory'
    _iid_ = Guid('{2d492cb3-f488-5d30-b00c-b6f2547d0efe}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame: ...
class IDoubleKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDoubleKeyFrameStatics'
    _iid_ = Guid('{0e56914c-b430-538f-bb66-0b8e83ab3db6}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IDragItemThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDragItemThemeAnimation'
    _iid_ = Guid('{648e690e-a2c0-58ca-b15d-db6fccc663f2}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDragItemThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDragItemThemeAnimationStatics'
    _iid_ = Guid('{cdbdb41a-ce84-50a1-8b96-96599cd9619d}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IDragOverThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimation'
    _iid_ = Guid('{633cd3c0-71af-52fd-993e-504e3e6f56d4}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ToOffset(self) -> Double: ...
    @winrt_commethod(9)
    def put_ToOffset(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_Direction(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(11)
    def put_Direction(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    Direction = property(get_Direction, put_Direction)
    TargetName = property(get_TargetName, put_TargetName)
    ToOffset = property(get_ToOffset, put_ToOffset)
class IDragOverThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDragOverThemeAnimationStatics'
    _iid_ = Guid('{8301afd2-68b2-5c6c-aadf-9a98d620e8d2}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_DirectionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DirectionProperty = property(get_DirectionProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToOffsetProperty = property(get_ToOffsetProperty, None)
class IDrillInNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDrillInNavigationTransitionInfo'
    _iid_ = Guid('{5d5863d6-4bbf-5b30-94fa-034531cfa2aa}')
class IDrillInThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimation'
    _iid_ = Guid('{097577e0-3027-5f24-af8c-976d9faed830}')
    @winrt_commethod(6)
    def get_EntranceTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EntranceTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_EntranceTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_EntranceTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ExitTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ExitTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ExitTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ExitTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
class IDrillInThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDrillInThemeAnimationStatics'
    _iid_ = Guid('{ba24258e-3a8e-5804-915a-7670893dbea4}')
    @winrt_commethod(6)
    def get_EntranceTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EntranceTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ExitTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ExitTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class IDrillOutThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimation'
    _iid_ = Guid('{9a93b9cc-925f-525a-9eac-55d39db3d314}')
    @winrt_commethod(6)
    def get_EntranceTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EntranceTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_EntranceTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_EntranceTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ExitTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ExitTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ExitTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ExitTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    EntranceTarget = property(get_EntranceTarget, put_EntranceTarget)
    EntranceTargetName = property(get_EntranceTargetName, put_EntranceTargetName)
    ExitTarget = property(get_ExitTarget, put_ExitTarget)
    ExitTargetName = property(get_ExitTargetName, put_ExitTargetName)
class IDrillOutThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDrillOutThemeAnimationStatics'
    _iid_ = Guid('{6eb9693b-c0d0-5bae-9cd2-10d80b8d3867}')
    @winrt_commethod(6)
    def get_EntranceTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EntranceTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ExitTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ExitTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EntranceTargetNameProperty = property(get_EntranceTargetNameProperty, None)
    EntranceTargetProperty = property(get_EntranceTargetProperty, None)
    ExitTargetNameProperty = property(get_ExitTargetNameProperty, None)
    ExitTargetProperty = property(get_ExitTargetProperty, None)
class IDropTargetItemThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimation'
    _iid_ = Guid('{b97f19c0-f1e2-5705-a252-2db05d2e5a54}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IDropTargetItemThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IDropTargetItemThemeAnimationStatics'
    _iid_ = Guid('{a0ce9e16-ae12-55fc-a9e5-29dc94a713bd}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IEasingColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingColorKeyFrame'
    _iid_ = Guid('{a137a710-da3c-5426-a1a2-3a5a672a4264}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingColorKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingColorKeyFrameStatics'
    _iid_ = Guid('{c57818c0-3361-587d-b381-620b69251bcf}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingDoubleKeyFrame'
    _iid_ = Guid('{935d9b7e-da61-5bb2-a574-7d2e53b60561}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingDoubleKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingDoubleKeyFrameStatics'
    _iid_ = Guid('{8cc08735-4221-5127-ab2f-1e7e3df95fb9}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEasingFunctionBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBase'
    _iid_ = Guid('{4fab519a-a93d-5d28-af18-84532bd32efe}')
    @winrt_commethod(6)
    def get_EasingMode(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingMode: ...
    @winrt_commethod(7)
    def put_EasingMode(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingMode) -> Void: ...
    @winrt_commethod(8)
    def Ease(self, normalizedTime: Double) -> Double: ...
    EasingMode = property(get_EasingMode, put_EasingMode)
class IEasingFunctionBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBaseFactory'
    _iid_ = Guid('{b1b92f4c-5ec7-5cda-b1d4-fd159595ca47}')
class IEasingFunctionBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingFunctionBaseStatics'
    _iid_ = Guid('{09032445-967c-52b8-b712-15f066b32821}')
    @winrt_commethod(6)
    def get_EasingModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingModeProperty = property(get_EasingModeProperty, None)
class IEasingPointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingPointKeyFrame'
    _iid_ = Guid('{9406ee8e-3641-54fe-a424-83420ea45cd3}')
    @winrt_commethod(6)
    def get_EasingFunction(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(7)
    def put_EasingFunction(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    EasingFunction = property(get_EasingFunction, put_EasingFunction)
class IEasingPointKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEasingPointKeyFrameStatics'
    _iid_ = Guid('{ac727659-92a3-52ea-8949-b609e48c233d}')
    @winrt_commethod(6)
    def get_EasingFunctionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
class IEdgeUIThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEdgeUIThemeTransition'
    _iid_ = Guid('{57089964-e358-5fe2-84e7-15e82bba9c06}')
    @winrt_commethod(6)
    def get_Edge(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IEdgeUIThemeTransitionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEdgeUIThemeTransitionStatics'
    _iid_ = Guid('{316af8d4-d2a0-5d27-9af6-747797965d46}')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IElasticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IElasticEase'
    _iid_ = Guid('{2b18d50b-4d34-509b-915c-61b1aa6f83d8}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IElasticEaseStatics'
    _iid_ = Guid('{95fd9290-d279-5857-9f50-3f299a2d02f4}')
    @winrt_commethod(6)
    def get_OscillationsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SpringinessProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    OscillationsProperty = property(get_OscillationsProperty, None)
    SpringinessProperty = property(get_SpringinessProperty, None)
class IEntranceNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfo'
    _iid_ = Guid('{dec74921-0ed7-54e1-8c1d-30b8cccc4b8d}')
class IEntranceNavigationTransitionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEntranceNavigationTransitionInfoStatics'
    _iid_ = Guid('{f1096de1-1f79-5d38-a4d6-16f3bdaab7f0}')
    @winrt_commethod(6)
    def get_IsTargetElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsTargetElement(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsTargetElement(self, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    IsTargetElementProperty = property(get_IsTargetElementProperty, None)
class IEntranceThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransition'
    _iid_ = Guid('{8eb681fa-1629-5e29-ac1e-70f3639329f8}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IEntranceThemeTransitionStatics'
    _iid_ = Guid('{c99e5435-facc-50af-b96c-63b14fe7156e}')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsStaggeringEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class IExponentialEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IExponentialEase'
    _iid_ = Guid('{4d289262-e832-5fbc-a98b-87a6ecb3b6cc}')
    @winrt_commethod(6)
    def get_Exponent(self) -> Double: ...
    @winrt_commethod(7)
    def put_Exponent(self, value: Double) -> Void: ...
    Exponent = property(get_Exponent, put_Exponent)
class IExponentialEaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IExponentialEaseStatics'
    _iid_ = Guid('{8394ab8f-ddf1-55d0-acf1-07fedd929bb5}')
    @winrt_commethod(6)
    def get_ExponentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ExponentProperty = property(get_ExponentProperty, None)
class IFadeInThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IFadeInThemeAnimation'
    _iid_ = Guid('{0dca074a-31cc-5e70-8b6b-8dbd7fff01f6}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeInThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IFadeInThemeAnimationStatics'
    _iid_ = Guid('{5d74a6a6-92c6-5e49-865f-676087247179}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IFadeOutThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IFadeOutThemeAnimation'
    _iid_ = Guid('{114024d6-5d67-5c9c-83c5-54a8bd7b671a}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IFadeOutThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IFadeOutThemeAnimationStatics'
    _iid_ = Guid('{0277bea1-a0a5-5e26-9b56-6a4208862738}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IGravityConnectedAnimationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfiguration'
    _iid_ = Guid('{04c8b276-cff3-5a55-9229-33dc66c99e20}')
    @winrt_commethod(6)
    def get_IsShadowEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsShadowEnabled(self, value: Boolean) -> Void: ...
    IsShadowEnabled = property(get_IsShadowEnabled, put_IsShadowEnabled)
class IGravityConnectedAnimationConfigurationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IGravityConnectedAnimationConfigurationFactory'
    _iid_ = Guid('{bc7a71b5-7cda-5bb7-967e-d6a031285a9c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.GravityConnectedAnimationConfiguration: ...
class IKeySpline(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IKeySpline'
    _iid_ = Guid('{130d8b2b-0b52-5253-881b-36ab48592e6b}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IKeyTimeHelper'
    _iid_ = Guid('{e354da44-1f24-59c6-bc5b-d6b1ba267e9c}')
class IKeyTimeHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IKeyTimeHelperStatics'
    _iid_ = Guid('{ae5d22c9-0fdb-5823-8846-8a4d0b9eebfa}')
    @winrt_commethod(6)
    def FromTimeSpan(self, timeSpan: win32more.Windows.Foundation.TimeSpan) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
class ILinearColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ILinearColorKeyFrame'
    _iid_ = Guid('{0bce4cd6-3a80-5f2f-932e-619a8546d0bd}')
class ILinearDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ILinearDoubleKeyFrame'
    _iid_ = Guid('{38a635b9-f613-55e0-aaec-9d4e097eff91}')
class ILinearPointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ILinearPointKeyFrame'
    _iid_ = Guid('{4ec22493-bacb-5105-ac16-8ea5418ab76e}')
class INavigationThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.INavigationThemeTransition'
    _iid_ = Guid('{d7cfbd3b-0d27-5ea1-beb7-f6b847520dc6}')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfo(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(7)
    def put_DefaultNavigationTransitionInfo(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
class INavigationThemeTransitionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.INavigationThemeTransitionStatics'
    _iid_ = Guid('{78323eff-d543-551d-b2c7-94e93a16065b}')
    @winrt_commethod(6)
    def get_DefaultNavigationTransitionInfoProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class INavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.INavigationTransitionInfo'
    _iid_ = Guid('{25bb17fb-6e15-514e-b278-197537a4d990}')
class INavigationTransitionInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.INavigationTransitionInfoFactory'
    _iid_ = Guid('{c514b6ff-f6ed-572e-8392-3ea17bc7d4c4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
class INavigationTransitionInfoOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides'
    _iid_ = Guid('{3d6af190-5a56-513d-aff9-631925d0fa43}')
    @winrt_commethod(6)
    def GetNavigationStateCore(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def SetNavigationStateCore(self, navigationState: WinRT_String) -> Void: ...
class IObjectAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames'
    _iid_ = Guid('{aa08dc4c-0b03-5c0a-b084-d95d272b2f0d}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IObjectAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{411a09b0-9ab4-54b9-99b9-54f955a6754e}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IObjectKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrame'
    _iid_ = Guid('{c5a9f65b-fc69-5a88-a797-34f46d761381}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IObjectKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrameFactory'
    _iid_ = Guid('{dc59da6e-82b9-55f7-a358-ba2a07665aa9}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
class IObjectKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrameStatics'
    _iid_ = Guid('{39e59ceb-2859-5a5f-acd8-bc491d49c4b6}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IPaneThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPaneThemeTransition'
    _iid_ = Guid('{321bcd80-157c-5e10-b0fe-6440bd92529a}')
    @winrt_commethod(6)
    def get_Edge(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_commethod(7)
    def put_Edge(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    Edge = property(get_Edge, put_Edge)
class IPaneThemeTransitionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPaneThemeTransitionStatics'
    _iid_ = Guid('{47e01752-5264-5fb1-8946-ab49fe6af8fd}')
    @winrt_commethod(6)
    def get_EdgeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EdgeProperty = property(get_EdgeProperty, None)
class IPointAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointAnimation'
    _iid_ = Guid('{a0737cc4-2eab-5c13-a5d7-78361df1000e}')
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
    def get_EasingFunction(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(13)
    def put_EasingFunction(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointAnimationStatics'
    _iid_ = Guid('{71cfb43b-bada-554b-8fca-b558d623bbc0}')
    @winrt_commethod(6)
    def get_FromProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ByProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_EasingFunctionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_EnableDependentAnimationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ByProperty = property(get_ByProperty, None)
    EasingFunctionProperty = property(get_EasingFunctionProperty, None)
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
    FromProperty = property(get_FromProperty, None)
    ToProperty = property(get_ToProperty, None)
class IPointAnimationUsingKeyFrames(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames'
    _iid_ = Guid('{bdd63992-df13-5514-8611-4952f722f6d0}')
    @winrt_commethod(6)
    def get_KeyFrames(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_commethod(7)
    def get_EnableDependentAnimation(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_EnableDependentAnimation(self, value: Boolean) -> Void: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
class IPointAnimationUsingKeyFramesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFramesStatics'
    _iid_ = Guid('{04152b3b-f0da-5b28-877d-9ac96d334a77}')
    @winrt_commethod(6)
    def get_EnableDependentAnimationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class IPointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointKeyFrame'
    _iid_ = Guid('{59d5c07d-a3a7-5450-9dfb-4b7e77d58f93}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_KeyTime(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_commethod(9)
    def put_KeyTime(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
class IPointKeyFrameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointKeyFrameFactory'
    _iid_ = Guid('{c52ee293-f10e-5252-bc08-a28659740f0e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame: ...
class IPointKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointKeyFrameStatics'
    _iid_ = Guid('{96cd72fd-d834-5b23-9a17-1548961dc348}')
    @winrt_commethod(6)
    def get_ValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTimeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTimeProperty = property(get_KeyTimeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IPointerDownThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointerDownThemeAnimation'
    _iid_ = Guid('{abdd1acc-40df-595d-be68-0362fe681b91}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerDownThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointerDownThemeAnimationStatics'
    _iid_ = Guid('{12268b39-fb7d-53da-8ccc-5967dc06bce9}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPointerUpThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointerUpThemeAnimation'
    _iid_ = Guid('{94896d1c-c938-5d68-84da-552bde815810}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPointerUpThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPointerUpThemeAnimationStatics'
    _iid_ = Guid('{51a3117e-c6fa-5dc5-8db8-73f060003ae4}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopInThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation'
    _iid_ = Guid('{20136388-b4e4-5cbb-9cb2-df2ea7e6c44b}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics'
    _iid_ = Guid('{8c9378a9-d276-5a1d-8188-f48f07840a16}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopOutThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPopOutThemeAnimation'
    _iid_ = Guid('{1bb20dd3-5648-541a-a0c9-37a955db10a6}')
    @winrt_commethod(6)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    TargetName = property(get_TargetName, put_TargetName)
class IPopOutThemeAnimationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPopOutThemeAnimationStatics'
    _iid_ = Guid('{3f569f96-367e-595c-9732-2fb919388d84}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
class IPopupThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransition'
    _iid_ = Guid('{e1fa6b8a-add3-5299-a000-121d6dbacc80}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics'
    _iid_ = Guid('{538b2114-415c-5f99-b74d-a85966dacc54}')
    @winrt_commethod(6)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromVerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class IPowerEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPowerEase'
    _iid_ = Guid('{372dfad0-5177-5df9-8e1e-920962468714}')
    @winrt_commethod(6)
    def get_Power(self) -> Double: ...
    @winrt_commethod(7)
    def put_Power(self, value: Double) -> Void: ...
    Power = property(get_Power, put_Power)
class IPowerEaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IPowerEaseStatics'
    _iid_ = Guid('{8eb72edb-3e7e-5d40-928b-4505d57c21ce}')
    @winrt_commethod(6)
    def get_PowerProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PowerProperty = property(get_PowerProperty, None)
class IQuadraticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IQuadraticEase'
    _iid_ = Guid('{db85fda1-03b7-57cd-a1ef-8855cbf62191}')
class IQuarticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IQuarticEase'
    _iid_ = Guid('{48215273-05f1-58aa-bade-0b71d7bd0484}')
class IQuinticEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IQuinticEase'
    _iid_ = Guid('{dc2f05d5-a3ac-5dce-9b85-753a0c800fc2}')
class IReorderThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IReorderThemeTransition'
    _iid_ = Guid('{0d5a0874-1df5-5379-b626-74721759438a}')
class IRepeatBehaviorHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelper'
    _iid_ = Guid('{4643f139-ffef-5c6a-8de6-142b41cd51a5}')
class IRepeatBehaviorHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics'
    _iid_ = Guid('{c66d4425-6461-5189-b17d-cca0cca34ca0}')
    @winrt_commethod(6)
    def get_Forever(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(7)
    def FromCount(self, count: Double) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(8)
    def FromDuration(self, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(9)
    def GetHasCount(self, target: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_commethod(10)
    def GetHasDuration(self, target: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_commethod(11)
    def Equals(self, target: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior, value: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    Forever = property(get_Forever, None)
class IRepositionThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation'
    _iid_ = Guid('{36f7e025-23c1-53de-8df9-7dc1e9c788fd}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics'
    _iid_ = Guid('{c04118de-aff5-5fa9-aee7-94a621c82618}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class IRepositionThemeTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IRepositionThemeTransition'
    _iid_ = Guid('{7728e3f0-24b1-5484-824a-c0b41c2745d5}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsStaggeringEnabled(self, value: Boolean) -> Void: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
class IRepositionThemeTransitionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IRepositionThemeTransitionStatics'
    _iid_ = Guid('{c70a0f9a-485e-53bb-ad3c-8b41b6788bf9}')
    @winrt_commethod(6)
    def get_IsStaggeringEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class ISineEase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISineEase'
    _iid_ = Guid('{6115539b-663d-5131-b7c2-74bb5fdc6a1d}')
class ISlideNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo'
    _iid_ = Guid('{53eade0e-6b01-511f-a563-6f5724a6c1c1}')
    @winrt_commethod(6)
    def get_Effect(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_commethod(7)
    def put_Effect(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    Effect = property(get_Effect, put_Effect)
class ISlideNavigationTransitionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfoStatics'
    _iid_ = Guid('{90ba0c6c-cd45-5a6c-bbb2-88037d43cd79}')
    @winrt_commethod(6)
    def get_EffectProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EffectProperty = property(get_EffectProperty, None)
class ISplineColorKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplineColorKeyFrame'
    _iid_ = Guid('{60c5905f-4343-504d-a2c6-64b8d924b438}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineColorKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplineColorKeyFrameStatics'
    _iid_ = Guid('{d89c7062-753d-5652-b215-c195ae2c7a18}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplineDoubleKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame'
    _iid_ = Guid('{aea80957-bb56-59b6-bb7a-6295f94bc961}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplineDoubleKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplineDoubleKeyFrameStatics'
    _iid_ = Guid('{ca88552e-7237-51f8-a8ca-79952c77883a}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplinePointKeyFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplinePointKeyFrame'
    _iid_ = Guid('{2b7eb049-708c-5220-a178-a25dbc14ffbe}')
    @winrt_commethod(6)
    def get_KeySpline(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_commethod(7)
    def put_KeySpline(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
class ISplinePointKeyFrameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplinePointKeyFrameStatics'
    _iid_ = Guid('{1e100e36-bed1-5060-8dcf-0d5b32575ed1}')
    @winrt_commethod(6)
    def get_KeySplineProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeySplineProperty = property(get_KeySplineProperty, None)
class ISplitCloseThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation'
    _iid_ = Guid('{b0dd1490-f646-5c18-b3ef-02f9b17f57df}')
    @winrt_commethod(6)
    def get_OpenedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_OpenedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_OpenedTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_OpenedTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ClosedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ClosedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ClosedTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ClosedTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_ContentTargetName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ContentTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_ContentTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(17)
    def put_ContentTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
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
    def get_ContentTranslationDirection(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(25)
    def put_ContentTranslationDirection(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics'
    _iid_ = Guid('{32345cdd-2a3c-5571-b2eb-2fcabc2e92c6}')
    @winrt_commethod(6)
    def get_OpenedTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OpenedTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ClosedTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ClosedTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ContentTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ContentTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_OpenedLengthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ClosedLengthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_OffsetFromCenterProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ContentTranslationDirectionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_ContentTranslationOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation'
    _iid_ = Guid('{79fdfaca-4245-53f0-b5c7-da1ce2b0b851}')
    @winrt_commethod(6)
    def get_OpenedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_OpenedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_OpenedTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_OpenedTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_ClosedTargetName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ClosedTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ClosedTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ClosedTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_ContentTargetName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ContentTargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_ContentTarget(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(17)
    def put_ContentTarget(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
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
    def get_ContentTranslationDirection(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(25)
    def put_ContentTranslationDirection(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics'
    _iid_ = Guid('{e5a73b84-a4ae-5c38-84da-f7ed30fc9b6e}')
    @winrt_commethod(6)
    def get_OpenedTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OpenedTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ClosedTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ClosedTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ContentTargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ContentTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_OpenedLengthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ClosedLengthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_OffsetFromCenterProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ContentTranslationDirectionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_ContentTranslationOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IStoryboard'
    _iid_ = Guid('{04d41bb3-8721-519e-8e53-fb8b34920305}')
    @winrt_commethod(6)
    def get_Children(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.TimelineCollection: ...
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
    def GetCurrentState(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.ClockState: ...
    @winrt_commethod(13)
    def GetCurrentTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def SeekAlignedToLastTick(self, offset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(15)
    def SkipToFill(self) -> Void: ...
    Children = property(get_Children, None)
class IStoryboardStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics'
    _iid_ = Guid('{dd18519b-d4e4-597d-a0b7-655ebdd35efa}')
    @winrt_commethod(6)
    def get_TargetPropertyProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetTargetProperty(self, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetTargetProperty(self, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline, path: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetTargetName(self, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetTargetName(self, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline, name: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def SetTarget(self, timeline: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline, target: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    TargetPropertyProperty = property(get_TargetPropertyProperty, None)
class ISuppressNavigationTransitionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISuppressNavigationTransitionInfo'
    _iid_ = Guid('{3ecd2bd1-9805-5f51-bb9e-051fea8dc355}')
class ISwipeBackThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation'
    _iid_ = Guid('{f095d058-bc9e-58ee-8877-e084723b4333}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics'
    _iid_ = Guid('{18a7a588-b9a2-573b-8e2b-38048c4635a7}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FromHorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FromVerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    TargetNameProperty = property(get_TargetNameProperty, None)
class ISwipeHintThemeAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation'
    _iid_ = Guid('{09de03d7-4b8a-55e1-afad-5f60598733ea}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics'
    _iid_ = Guid('{f3308304-4f09-54d7-a4d5-ca558bbfe26f}')
    @winrt_commethod(6)
    def get_TargetNameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ToHorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ToVerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetNameProperty = property(get_TargetNameProperty, None)
    ToHorizontalOffsetProperty = property(get_ToHorizontalOffsetProperty, None)
    ToVerticalOffsetProperty = property(get_ToVerticalOffsetProperty, None)
class ITimeline(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ITimeline'
    _iid_ = Guid('{d0f9b330-cc2a-5b05-9786-2da4c6584581}')
    @winrt_commethod(6)
    def get_AutoReverse(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AutoReverse(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_BeginTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def put_BeginTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(10)
    def get_Duration(self) -> win32more.Microsoft.UI.Xaml.Duration: ...
    @winrt_commethod(11)
    def put_Duration(self, value: win32more.Microsoft.UI.Xaml.Duration) -> Void: ...
    @winrt_commethod(12)
    def get_SpeedRatio(self) -> Double: ...
    @winrt_commethod(13)
    def put_SpeedRatio(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_FillBehavior(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.FillBehavior: ...
    @winrt_commethod(15)
    def put_FillBehavior(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.FillBehavior) -> Void: ...
    @winrt_commethod(16)
    def get_RepeatBehavior(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_commethod(17)
    def put_RepeatBehavior(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ITimelineFactory'
    _iid_ = Guid('{6a635732-a827-5398-9fc8-dfbc3b97e3c1}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.Timeline: ...
class ITimelineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ITimelineStatics'
    _iid_ = Guid('{778b8471-c831-503a-8748-fe6bbc7153b7}')
    @winrt_commethod(6)
    def get_AllowDependentAnimations(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowDependentAnimations(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AutoReverseProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_BeginTimeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DurationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_SpeedRatioProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_FillBehaviorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_RepeatBehaviorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AllowDependentAnimations = property(get_AllowDependentAnimations, put_AllowDependentAnimations)
    AutoReverseProperty = property(get_AutoReverseProperty, None)
    BeginTimeProperty = property(get_BeginTimeProperty, None)
    DurationProperty = property(get_DurationProperty, None)
    FillBehaviorProperty = property(get_FillBehaviorProperty, None)
    RepeatBehaviorProperty = property(get_RepeatBehaviorProperty, None)
    SpeedRatioProperty = property(get_SpeedRatioProperty, None)
class ITransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ITransition'
    _iid_ = Guid('{e5b71956-8e44-5a38-b41e-274d706102bf}')
class ITransitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ITransitionFactory'
    _iid_ = Guid('{b7023e3b-bcd3-50ec-aacf-8cfcece25f17}')
class KeySpline(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IKeySpline
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.KeySpline'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def get_ControlPoint1(self: win32more.Microsoft.UI.Xaml.Media.Animation.IKeySpline) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_ControlPoint1(self: win32more.Microsoft.UI.Xaml.Media.Animation.IKeySpline, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_ControlPoint2(self: win32more.Microsoft.UI.Xaml.Media.Animation.IKeySpline) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_ControlPoint2(self: win32more.Microsoft.UI.Xaml.Media.Animation.IKeySpline, value: win32more.Windows.Foundation.Point) -> Void: ...
    ControlPoint1 = property(get_ControlPoint1, put_ControlPoint1)
    ControlPoint2 = property(get_ControlPoint2, put_ControlPoint2)
class KeyTime(Structure):
    TimeSpan: win32more.Windows.Foundation.TimeSpan
class KeyTimeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IKeyTimeHelper
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.KeyTimeHelper'
    @winrt_classmethod
    def FromTimeSpan(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IKeyTimeHelperStatics, timeSpan: win32more.Windows.Foundation.TimeSpan) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
class LinearColorKeyFrame(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ILinearColorKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.LinearColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.LinearColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.LinearColorKeyFrame: ...
class LinearDoubleKeyFrame(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ILinearDoubleKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.LinearDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.LinearDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.LinearDoubleKeyFrame: ...
class LinearPointKeyFrame(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ILinearPointKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.LinearPointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.LinearPointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.LinearPointKeyFrame: ...
class _NavigationThemeTransition_Meta_(ComPtr.__class__):
    pass
class NavigationThemeTransition(ComPtr, metaclass=_NavigationThemeTransition_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.NavigationThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.NavigationThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationThemeTransition: ...
    @winrt_mixinmethod
    def get_DefaultNavigationTransitionInfo(self: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationThemeTransition) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def put_DefaultNavigationTransitionInfo(self: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationThemeTransition, value: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    @winrt_classmethod
    def get_DefaultNavigationTransitionInfoProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DefaultNavigationTransitionInfo = property(get_DefaultNavigationTransitionInfo, put_DefaultNavigationTransitionInfo)
    _NavigationThemeTransition_Meta_.DefaultNavigationTransitionInfoProperty = property(get_DefaultNavigationTransitionInfoProperty, None)
class NavigationTransitionInfo(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationTransitionInfo
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationTransitionInfoFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def GetNavigationStateCore(self: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetNavigationStateCore(self: win32more.Microsoft.UI.Xaml.Media.Animation.INavigationTransitionInfoOverrides, navigationState: WinRT_String) -> Void: ...
class _ObjectAnimationUsingKeyFrames_Meta_(ComPtr.__class__):
    pass
class ObjectAnimationUsingKeyFrames(ComPtr, metaclass=_ObjectAnimationUsingKeyFrames_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ObjectAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames) -> win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectAnimationUsingKeyFramesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _ObjectAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _ObjectKeyFrame_Meta_(ComPtr.__class__):
    pass
class ObjectKeyFrame(ComPtr, metaclass=_ObjectKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrame) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrame, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IObjectKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _ObjectKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _ObjectKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class ObjectKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Animation.ObjectKeyFrame]: ...
    Size = property(get_Size, None)
class _PaneThemeTransition_Meta_(ComPtr.__class__):
    pass
class PaneThemeTransition(ComPtr, metaclass=_PaneThemeTransition_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPaneThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PaneThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PaneThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PaneThemeTransition: ...
    @winrt_mixinmethod
    def get_Edge(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPaneThemeTransition) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation: ...
    @winrt_mixinmethod
    def put_Edge(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPaneThemeTransition, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.EdgeTransitionLocation) -> Void: ...
    @winrt_classmethod
    def get_EdgeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPaneThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Edge = property(get_Edge, put_Edge)
    _PaneThemeTransition_Meta_.EdgeProperty = property(get_EdgeProperty, None)
class _PointAnimation_Meta_(ComPtr.__class__):
    pass
class PointAnimation(ComPtr, metaclass=_PointAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PointAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PointAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointAnimation: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_By(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_By(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation) -> win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_EasingFunction(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation, value: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimation, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FromProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ByProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EasingFunctionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointAnimationUsingKeyFrames: ...
    @winrt_mixinmethod
    def get_KeyFrames(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_mixinmethod
    def get_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableDependentAnimation(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFrames, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_EnableDependentAnimationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointAnimationUsingKeyFramesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EnableDependentAnimation = property(get_EnableDependentAnimation, put_EnableDependentAnimation)
    KeyFrames = property(get_KeyFrames, None)
    _PointAnimationUsingKeyFrames_Meta_.EnableDependentAnimationProperty = property(get_EnableDependentAnimationProperty, None)
class _PointKeyFrame_Meta_(ComPtr.__class__):
    pass
class PointKeyFrame(ComPtr, metaclass=_PointKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrameFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrame) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrame, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime: ...
    @winrt_mixinmethod
    def put_KeyTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeyTime) -> Void: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTimeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeyTime = property(get_KeyTime, put_KeyTime)
    Value = property(get_Value, put_Value)
    _PointKeyFrame_Meta_.KeyTimeProperty = property(get_KeyTimeProperty, None)
    _PointKeyFrame_Meta_.ValueProperty = property(get_ValueProperty, None)
class PointKeyFrameCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PointKeyFrameCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrameCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrameCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], value: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame]: ...
    Size = property(get_Size, None)
class _PointerDownThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PointerDownThemeAnimation(ComPtr, metaclass=_PointerDownThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerDownThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PointerDownThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PointerDownThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointerDownThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerDownThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerDownThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerDownThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _PointerDownThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PointerUpThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PointerUpThemeAnimation(ComPtr, metaclass=_PointerUpThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerUpThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PointerUpThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PointerUpThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PointerUpThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerUpThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerUpThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPointerUpThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _PointerUpThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PopInThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PopInThemeAnimation(ComPtr, metaclass=_PopInThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PopInThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PopInThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PopInThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPopInThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
    _PopInThemeAnimation_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _PopInThemeAnimation_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _PopInThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PopOutThemeAnimation_Meta_(ComPtr.__class__):
    pass
class PopOutThemeAnimation(ComPtr, metaclass=_PopOutThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPopOutThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PopOutThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PopOutThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PopOutThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopOutThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopOutThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPopOutThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    _PopOutThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _PopupThemeTransition_Meta_(ComPtr.__class__):
    pass
class PopupThemeTransition(ComPtr, metaclass=_PopupThemeTransition_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PopupThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PopupThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PopupThemeTransition: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransition) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransition, value: Double) -> Void: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPopupThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    _PopupThemeTransition_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _PopupThemeTransition_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
class _PowerEase_Meta_(ComPtr.__class__):
    pass
class PowerEase(ComPtr, metaclass=_PowerEase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IPowerEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.PowerEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.PowerEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.PowerEase: ...
    @winrt_mixinmethod
    def get_Power(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPowerEase) -> Double: ...
    @winrt_mixinmethod
    def put_Power(self: win32more.Microsoft.UI.Xaml.Media.Animation.IPowerEase, value: Double) -> Void: ...
    @winrt_classmethod
    def get_PowerProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IPowerEaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Power = property(get_Power, put_Power)
    _PowerEase_Meta_.PowerProperty = property(get_PowerProperty, None)
class QuadraticEase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IQuadraticEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.QuadraticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.QuadraticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.QuadraticEase: ...
class QuarticEase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IQuarticEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.QuarticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.QuarticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.QuarticEase: ...
class QuinticEase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IQuinticEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.QuinticEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.QuinticEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.QuinticEase: ...
class ReorderThemeTransition(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IReorderThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.ReorderThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.ReorderThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.ReorderThemeTransition: ...
class RepeatBehavior(Structure):
    Count: Double
    Duration: win32more.Windows.Foundation.TimeSpan
    Type: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehaviorType
class _RepeatBehaviorHelper_Meta_(ComPtr.__class__):
    pass
class RepeatBehaviorHelper(ComPtr, metaclass=_RepeatBehaviorHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelper
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.RepeatBehaviorHelper'
    @winrt_classmethod
    def get_Forever(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def FromCount(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, count: Double) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def FromDuration(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_classmethod
    def GetHasCount(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_classmethod
    def GetHasDuration(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepeatBehaviorHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior, value: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Boolean: ...
    _RepeatBehaviorHelper_Meta_.Forever = property(get_Forever, None)
class RepeatBehaviorType(Enum, Int32):
    Count = 0
    Duration = 1
    Forever = 2
class _RepositionThemeAnimation_Meta_(ComPtr.__class__):
    pass
class RepositionThemeAnimation(ComPtr, metaclass=_RepositionThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.RepositionThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.RepositionThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepositionThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
    _RepositionThemeAnimation_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _RepositionThemeAnimation_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _RepositionThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _RepositionThemeTransition_Meta_(ComPtr.__class__):
    pass
class RepositionThemeTransition(ComPtr, metaclass=_RepositionThemeTransition_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Transition
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeTransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.RepositionThemeTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.RepositionThemeTransition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepositionThemeTransition: ...
    @winrt_mixinmethod
    def get_IsStaggeringEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeTransition) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStaggeringEnabled(self: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeTransition, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsStaggeringEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IRepositionThemeTransitionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsStaggeringEnabled = property(get_IsStaggeringEnabled, put_IsStaggeringEnabled)
    _RepositionThemeTransition_Meta_.IsStaggeringEnabledProperty = property(get_IsStaggeringEnabledProperty, None)
class SineEase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.EasingFunctionBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISineEase
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SineEase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SineEase.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SineEase: ...
class SlideNavigationTransitionEffect(Enum, Int32):
    FromBottom = 0
    FromLeft = 1
    FromRight = 2
class _SlideNavigationTransitionInfo_Meta_(ComPtr.__class__):
    pass
class SlideNavigationTransitionInfo(ComPtr, metaclass=_SlideNavigationTransitionInfo_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SlideNavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_Effect(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo) -> win32more.Microsoft.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect: ...
    @winrt_mixinmethod
    def put_Effect(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfo, value: win32more.Microsoft.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect) -> Void: ...
    @winrt_classmethod
    def get_EffectProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISlideNavigationTransitionInfoStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Effect = property(get_Effect, put_Effect)
    _SlideNavigationTransitionInfo_Meta_.EffectProperty = property(get_EffectProperty, None)
class _SplineColorKeyFrame_Meta_(ComPtr.__class__):
    pass
class SplineColorKeyFrame(ComPtr, metaclass=_SplineColorKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.ColorKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineColorKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SplineColorKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SplineColorKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SplineColorKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineColorKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineColorKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineColorKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    _SplineColorKeyFrame_Meta_.KeySplineProperty = property(get_KeySplineProperty, None)
class _SplineDoubleKeyFrame_Meta_(ComPtr.__class__):
    pass
class SplineDoubleKeyFrame(ComPtr, metaclass=_SplineDoubleKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.DoubleKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SplineDoubleKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SplineDoubleKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SplineDoubleKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineDoubleKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplineDoubleKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    _SplineDoubleKeyFrame_Meta_.KeySplineProperty = property(get_KeySplineProperty, None)
class _SplinePointKeyFrame_Meta_(ComPtr.__class__):
    pass
class SplinePointKeyFrame(ComPtr, metaclass=_SplinePointKeyFrame_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.PointKeyFrame
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISplinePointKeyFrame
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SplinePointKeyFrame'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SplinePointKeyFrame.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SplinePointKeyFrame: ...
    @winrt_mixinmethod
    def get_KeySpline(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplinePointKeyFrame) -> win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline: ...
    @winrt_mixinmethod
    def put_KeySpline(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplinePointKeyFrame, value: win32more.Microsoft.UI.Xaml.Media.Animation.KeySpline) -> Void: ...
    @winrt_classmethod
    def get_KeySplineProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplinePointKeyFrameStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KeySpline = property(get_KeySpline, put_KeySpline)
    _SplinePointKeyFrame_Meta_.KeySplineProperty = property(get_KeySplineProperty, None)
class _SplitCloseThemeAnimation_Meta_(ComPtr.__class__):
    pass
class SplitCloseThemeAnimation(ComPtr, metaclass=_SplitCloseThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SplitCloseThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SplitCloseThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SplitCloseThemeAnimation: ...
    @winrt_mixinmethod
    def get_OpenedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OpenedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OpenedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClosedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ClosedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ContentTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OpenedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ClosedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetFromCenter(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetFromCenter(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationDirection(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_ContentTranslationDirection(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ContentTranslationOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OpenedTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedLengthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedLengthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetFromCenterProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationDirectionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitCloseThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SplitOpenThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SplitOpenThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SplitOpenThemeAnimation: ...
    @winrt_mixinmethod
    def get_OpenedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OpenedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OpenedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClosedTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ClosedTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentTargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ContentTarget(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_OpenedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OpenedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ClosedLength(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetFromCenter(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetFromCenter(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationDirection(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def put_ContentTranslationDirection(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTranslationOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ContentTranslationOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_OpenedTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpenedLengthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClosedLengthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetFromCenterProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationDirectionProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentTranslationOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISplitOpenThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.Storyboard'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.Storyboard.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> win32more.Microsoft.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard, offset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Begin(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentState(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> win32more.Microsoft.UI.Xaml.Media.Animation.ClockState: ...
    @winrt_mixinmethod
    def GetCurrentTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SeekAlignedToLastTick(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard, offset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SkipToFill(self: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboard) -> Void: ...
    @winrt_classmethod
    def get_TargetPropertyProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_classmethod
    def SetTargetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline, path: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTargetName(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline) -> WinRT_String: ...
    @winrt_classmethod
    def SetTargetName(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics, element: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline, name: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetTarget(cls: win32more.Microsoft.UI.Xaml.Media.Animation.IStoryboardStatics, timeline: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline, target: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    Children = property(get_Children, None)
    _Storyboard_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
    _Storyboard_Meta_.TargetPropertyProperty = property(get_TargetPropertyProperty, None)
class SuppressNavigationTransitionInfo(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISuppressNavigationTransitionInfo
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SuppressNavigationTransitionInfo: ...
class _SwipeBackThemeAnimation_Meta_(ComPtr.__class__):
    pass
class SwipeBackThemeAnimation(ComPtr, metaclass=_SwipeBackThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SwipeBackThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SwipeBackThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SwipeBackThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromHorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FromVerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeBackThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, put_FromHorizontalOffset)
    FromVerticalOffset = property(get_FromVerticalOffset, put_FromVerticalOffset)
    TargetName = property(get_TargetName, put_TargetName)
    _SwipeBackThemeAnimation_Meta_.FromHorizontalOffsetProperty = property(get_FromHorizontalOffsetProperty, None)
    _SwipeBackThemeAnimation_Meta_.FromVerticalOffsetProperty = property(get_FromVerticalOffsetProperty, None)
    _SwipeBackThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
class _SwipeHintThemeAnimation_Meta_(ComPtr.__class__):
    pass
class SwipeHintThemeAnimation(ComPtr, metaclass=_SwipeHintThemeAnimation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.SwipeHintThemeAnimation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.SwipeHintThemeAnimation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.SwipeHintThemeAnimation: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ToHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ToVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation) -> Double: ...
    @winrt_mixinmethod
    def put_ToVerticalOffset(self: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimation, value: Double) -> Void: ...
    @winrt_classmethod
    def get_TargetNameProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToHorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ToVerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ISwipeHintThemeAnimationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TargetName = property(get_TargetName, put_TargetName)
    ToHorizontalOffset = property(get_ToHorizontalOffset, put_ToHorizontalOffset)
    ToVerticalOffset = property(get_ToVerticalOffset, put_ToVerticalOffset)
    _SwipeHintThemeAnimation_Meta_.TargetNameProperty = property(get_TargetNameProperty, None)
    _SwipeHintThemeAnimation_Meta_.ToHorizontalOffsetProperty = property(get_ToHorizontalOffsetProperty, None)
    _SwipeHintThemeAnimation_Meta_.ToVerticalOffsetProperty = property(get_ToVerticalOffsetProperty, None)
class _Timeline_Meta_(ComPtr.__class__):
    pass
class Timeline(ComPtr, metaclass=_Timeline_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.Timeline'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.Timeline.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Animation.Timeline: ...
    @winrt_mixinmethod
    def get_AutoReverse(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoReverse(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BeginTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_BeginTime(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline) -> win32more.Microsoft.UI.Xaml.Duration: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, value: win32more.Microsoft.UI.Xaml.Duration) -> Void: ...
    @winrt_mixinmethod
    def get_SpeedRatio(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline) -> Double: ...
    @winrt_mixinmethod
    def put_SpeedRatio(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FillBehavior(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline) -> win32more.Microsoft.UI.Xaml.Media.Animation.FillBehavior: ...
    @winrt_mixinmethod
    def put_FillBehavior(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, value: win32more.Microsoft.UI.Xaml.Media.Animation.FillBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_RepeatBehavior(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline) -> win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior: ...
    @winrt_mixinmethod
    def put_RepeatBehavior(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, value: win32more.Microsoft.UI.Xaml.Media.Animation.RepeatBehavior) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Microsoft.UI.Xaml.Media.Animation.ITimeline, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AllowDependentAnimations(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics) -> Boolean: ...
    @winrt_classmethod
    def put_AllowDependentAnimations(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_AutoReverseProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BeginTimeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DurationProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SpeedRatioProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FillBehaviorProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RepeatBehaviorProperty(cls: win32more.Microsoft.UI.Xaml.Media.Animation.ITimelineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.TimelineCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.TimelineCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.TimelineCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Animation.Timeline: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], value: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], value: win32more.Microsoft.UI.Xaml.Media.Animation.Timeline) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Animation.Timeline]: ...
    Size = property(get_Size, None)
class Transition(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Animation.ITransition
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.Transition'
class TransitionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]
    _classid_ = 'Microsoft.UI.Xaml.Media.Animation.TransitionCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Animation.TransitionCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Animation.Transition: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], value: win32more.Microsoft.UI.Xaml.Media.Animation.Transition, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], value: win32more.Microsoft.UI.Xaml.Media.Animation.Transition) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Animation.Transition], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Animation.Transition]: ...
    Size = property(get_Size, None)


make_ready(__name__)
