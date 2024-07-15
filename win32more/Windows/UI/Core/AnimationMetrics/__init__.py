from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Core.AnimationMetrics
import win32more.Windows.Win32.System.WinRT
class AnimationDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescription
    _classid_ = 'Windows.UI.Core.AnimationMetrics.AnimationDescription'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Core.AnimationMetrics.AnimationDescription.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescriptionFactory, effect: win32more.Windows.UI.Core.AnimationMetrics.AnimationEffect, target: win32more.Windows.UI.Core.AnimationMetrics.AnimationEffectTarget) -> win32more.Windows.UI.Core.AnimationMetrics.AnimationDescription: ...
    @winrt_mixinmethod
    def get_Animations(self: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescription) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation]: ...
    @winrt_mixinmethod
    def get_StaggerDelay(self: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescription) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_StaggerDelayFactor(self: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescription) -> Single: ...
    @winrt_mixinmethod
    def get_DelayLimit(self: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescription) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ZOrder(self: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescription) -> Int32: ...
    Animations = property(get_Animations, None)
    DelayLimit = property(get_DelayLimit, None)
    StaggerDelay = property(get_StaggerDelay, None)
    StaggerDelayFactor = property(get_StaggerDelayFactor, None)
    ZOrder = property(get_ZOrder, None)
class AnimationEffect(Enum, Int32):
    Expand = 0
    Collapse = 1
    Reposition = 2
    FadeIn = 3
    FadeOut = 4
    AddToList = 5
    DeleteFromList = 6
    AddToGrid = 7
    DeleteFromGrid = 8
    AddToSearchGrid = 9
    DeleteFromSearchGrid = 10
    AddToSearchList = 11
    DeleteFromSearchList = 12
    ShowEdgeUI = 13
    ShowPanel = 14
    HideEdgeUI = 15
    HidePanel = 16
    ShowPopup = 17
    HidePopup = 18
    PointerDown = 19
    PointerUp = 20
    DragSourceStart = 21
    DragSourceEnd = 22
    TransitionContent = 23
    Reveal = 24
    Hide = 25
    DragBetweenEnter = 26
    DragBetweenLeave = 27
    SwipeSelect = 28
    SwipeDeselect = 29
    SwipeReveal = 30
    EnterPage = 31
    TransitionPage = 32
    CrossFade = 33
    Peek = 34
    UpdateBadge = 35
class AnimationEffectTarget(Enum, Int32):
    Primary = 0
    Added = 1
    Affected = 2
    Background = 3
    Content = 4
    Deleted = 5
    Deselected = 6
    DragSource = 7
    Hidden = 8
    Incoming = 9
    Outgoing = 10
    Outline = 11
    Remaining = 12
    Revealed = 13
    RowIn = 14
    RowOut = 15
    Selected = 16
    Selection = 17
    Shown = 18
    Tapped = 19
AnimationMetricsContract: UInt32 = 65536
class IAnimationDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.AnimationMetrics.IAnimationDescription'
    _iid_ = Guid('{7d11a549-be3d-41de-b081-05c149962f9b}')
    @winrt_commethod(6)
    def get_Animations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation]: ...
    @winrt_commethod(7)
    def get_StaggerDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_StaggerDelayFactor(self) -> Single: ...
    @winrt_commethod(9)
    def get_DelayLimit(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_ZOrder(self) -> Int32: ...
    Animations = property(get_Animations, None)
    DelayLimit = property(get_DelayLimit, None)
    StaggerDelay = property(get_StaggerDelay, None)
    StaggerDelayFactor = property(get_StaggerDelayFactor, None)
    ZOrder = property(get_ZOrder, None)
class IAnimationDescriptionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.AnimationMetrics.IAnimationDescriptionFactory'
    _iid_ = Guid('{c6e27abe-c1fb-48b5-9271-ecc70ac86ef0}')
    @winrt_commethod(6)
    def CreateInstance(self, effect: win32more.Windows.UI.Core.AnimationMetrics.AnimationEffect, target: win32more.Windows.UI.Core.AnimationMetrics.AnimationEffectTarget) -> win32more.Windows.UI.Core.AnimationMetrics.AnimationDescription: ...
class IOpacityAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.AnimationMetrics.IOpacityAnimation'
    _iid_ = Guid('{803aabe5-ee7e-455f-84e9-2506afb8d2b4}')
    @winrt_commethod(6)
    def get_InitialOpacity(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(7)
    def get_FinalOpacity(self) -> Single: ...
    FinalOpacity = property(get_FinalOpacity, None)
    InitialOpacity = property(get_InitialOpacity, None)
class IPropertyAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.AnimationMetrics.IPropertyAnimation'
    _iid_ = Guid('{3a01b4da-4d8c-411e-b615-1ade683a9903}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.UI.Core.AnimationMetrics.PropertyAnimationType: ...
    @winrt_commethod(7)
    def get_Delay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Control1(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def get_Control2(self) -> win32more.Windows.Foundation.Point: ...
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Type = property(get_Type, None)
class IScaleAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.AnimationMetrics.IScaleAnimation'
    _iid_ = Guid('{023552c7-71ab-428c-9c9f-d31780964995}')
    @winrt_commethod(6)
    def get_InitialScaleX(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(7)
    def get_InitialScaleY(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(8)
    def get_FinalScaleX(self) -> Single: ...
    @winrt_commethod(9)
    def get_FinalScaleY(self) -> Single: ...
    @winrt_commethod(10)
    def get_NormalizedOrigin(self) -> win32more.Windows.Foundation.Point: ...
    FinalScaleX = property(get_FinalScaleX, None)
    FinalScaleY = property(get_FinalScaleY, None)
    InitialScaleX = property(get_InitialScaleX, None)
    InitialScaleY = property(get_InitialScaleY, None)
    NormalizedOrigin = property(get_NormalizedOrigin, None)
class OpacityAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.AnimationMetrics.IOpacityAnimation
    _classid_ = 'Windows.UI.Core.AnimationMetrics.OpacityAnimation'
    @winrt_mixinmethod
    def get_InitialOpacity(self: win32more.Windows.UI.Core.AnimationMetrics.IOpacityAnimation) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_FinalOpacity(self: win32more.Windows.UI.Core.AnimationMetrics.IOpacityAnimation) -> Single: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.UI.Core.AnimationMetrics.PropertyAnimationType: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Control1(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Control2(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    FinalOpacity = property(get_FinalOpacity, None)
    InitialOpacity = property(get_InitialOpacity, None)
    Type = property(get_Type, None)
class PropertyAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation
    _classid_ = 'Windows.UI.Core.AnimationMetrics.PropertyAnimation'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.UI.Core.AnimationMetrics.PropertyAnimationType: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Control1(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Control2(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Type = property(get_Type, None)
class PropertyAnimationType(Enum, Int32):
    Scale = 0
    Translation = 1
    Opacity = 2
class ScaleAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.AnimationMetrics.IScaleAnimation
    _classid_ = 'Windows.UI.Core.AnimationMetrics.ScaleAnimation'
    @winrt_mixinmethod
    def get_InitialScaleX(self: win32more.Windows.UI.Core.AnimationMetrics.IScaleAnimation) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_InitialScaleY(self: win32more.Windows.UI.Core.AnimationMetrics.IScaleAnimation) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_FinalScaleX(self: win32more.Windows.UI.Core.AnimationMetrics.IScaleAnimation) -> Single: ...
    @winrt_mixinmethod
    def get_FinalScaleY(self: win32more.Windows.UI.Core.AnimationMetrics.IScaleAnimation) -> Single: ...
    @winrt_mixinmethod
    def get_NormalizedOrigin(self: win32more.Windows.UI.Core.AnimationMetrics.IScaleAnimation) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.UI.Core.AnimationMetrics.PropertyAnimationType: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Control1(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Control2(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    FinalScaleX = property(get_FinalScaleX, None)
    FinalScaleY = property(get_FinalScaleY, None)
    InitialScaleX = property(get_InitialScaleX, None)
    InitialScaleY = property(get_InitialScaleY, None)
    NormalizedOrigin = property(get_NormalizedOrigin, None)
    Type = property(get_Type, None)
class TranslationAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation
    _classid_ = 'Windows.UI.Core.AnimationMetrics.TranslationAnimation'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.UI.Core.AnimationMetrics.PropertyAnimationType: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Control1(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Control2(self: win32more.Windows.UI.Core.AnimationMetrics.IPropertyAnimation) -> win32more.Windows.Foundation.Point: ...
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Type = property(get_Type, None)


make_ready(__name__)
