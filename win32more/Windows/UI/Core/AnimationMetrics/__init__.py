from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Core.AnimationMetrics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AnimationDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.AnimationMetrics.IAnimationDescription
    _classid_ = 'Windows.UI.Core.AnimationMetrics.AnimationDescription'
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
    StaggerDelay = property(get_StaggerDelay, None)
    StaggerDelayFactor = property(get_StaggerDelayFactor, None)
    DelayLimit = property(get_DelayLimit, None)
    ZOrder = property(get_ZOrder, None)
AnimationEffect = Int32
AnimationEffect_Expand: AnimationEffect = 0
AnimationEffect_Collapse: AnimationEffect = 1
AnimationEffect_Reposition: AnimationEffect = 2
AnimationEffect_FadeIn: AnimationEffect = 3
AnimationEffect_FadeOut: AnimationEffect = 4
AnimationEffect_AddToList: AnimationEffect = 5
AnimationEffect_DeleteFromList: AnimationEffect = 6
AnimationEffect_AddToGrid: AnimationEffect = 7
AnimationEffect_DeleteFromGrid: AnimationEffect = 8
AnimationEffect_AddToSearchGrid: AnimationEffect = 9
AnimationEffect_DeleteFromSearchGrid: AnimationEffect = 10
AnimationEffect_AddToSearchList: AnimationEffect = 11
AnimationEffect_DeleteFromSearchList: AnimationEffect = 12
AnimationEffect_ShowEdgeUI: AnimationEffect = 13
AnimationEffect_ShowPanel: AnimationEffect = 14
AnimationEffect_HideEdgeUI: AnimationEffect = 15
AnimationEffect_HidePanel: AnimationEffect = 16
AnimationEffect_ShowPopup: AnimationEffect = 17
AnimationEffect_HidePopup: AnimationEffect = 18
AnimationEffect_PointerDown: AnimationEffect = 19
AnimationEffect_PointerUp: AnimationEffect = 20
AnimationEffect_DragSourceStart: AnimationEffect = 21
AnimationEffect_DragSourceEnd: AnimationEffect = 22
AnimationEffect_TransitionContent: AnimationEffect = 23
AnimationEffect_Reveal: AnimationEffect = 24
AnimationEffect_Hide: AnimationEffect = 25
AnimationEffect_DragBetweenEnter: AnimationEffect = 26
AnimationEffect_DragBetweenLeave: AnimationEffect = 27
AnimationEffect_SwipeSelect: AnimationEffect = 28
AnimationEffect_SwipeDeselect: AnimationEffect = 29
AnimationEffect_SwipeReveal: AnimationEffect = 30
AnimationEffect_EnterPage: AnimationEffect = 31
AnimationEffect_TransitionPage: AnimationEffect = 32
AnimationEffect_CrossFade: AnimationEffect = 33
AnimationEffect_Peek: AnimationEffect = 34
AnimationEffect_UpdateBadge: AnimationEffect = 35
AnimationEffectTarget = Int32
AnimationEffectTarget_Primary: AnimationEffectTarget = 0
AnimationEffectTarget_Added: AnimationEffectTarget = 1
AnimationEffectTarget_Affected: AnimationEffectTarget = 2
AnimationEffectTarget_Background: AnimationEffectTarget = 3
AnimationEffectTarget_Content: AnimationEffectTarget = 4
AnimationEffectTarget_Deleted: AnimationEffectTarget = 5
AnimationEffectTarget_Deselected: AnimationEffectTarget = 6
AnimationEffectTarget_DragSource: AnimationEffectTarget = 7
AnimationEffectTarget_Hidden: AnimationEffectTarget = 8
AnimationEffectTarget_Incoming: AnimationEffectTarget = 9
AnimationEffectTarget_Outgoing: AnimationEffectTarget = 10
AnimationEffectTarget_Outline: AnimationEffectTarget = 11
AnimationEffectTarget_Remaining: AnimationEffectTarget = 12
AnimationEffectTarget_Revealed: AnimationEffectTarget = 13
AnimationEffectTarget_RowIn: AnimationEffectTarget = 14
AnimationEffectTarget_RowOut: AnimationEffectTarget = 15
AnimationEffectTarget_Selected: AnimationEffectTarget = 16
AnimationEffectTarget_Selection: AnimationEffectTarget = 17
AnimationEffectTarget_Shown: AnimationEffectTarget = 18
AnimationEffectTarget_Tapped: AnimationEffectTarget = 19
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
    StaggerDelay = property(get_StaggerDelay, None)
    StaggerDelayFactor = property(get_StaggerDelayFactor, None)
    DelayLimit = property(get_DelayLimit, None)
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
    InitialOpacity = property(get_InitialOpacity, None)
    FinalOpacity = property(get_FinalOpacity, None)
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
    Type = property(get_Type, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
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
    InitialScaleX = property(get_InitialScaleX, None)
    InitialScaleY = property(get_InitialScaleY, None)
    FinalScaleX = property(get_FinalScaleX, None)
    FinalScaleY = property(get_FinalScaleY, None)
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
    InitialOpacity = property(get_InitialOpacity, None)
    FinalOpacity = property(get_FinalOpacity, None)
    Type = property(get_Type, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
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
    Type = property(get_Type, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
PropertyAnimationType = Int32
PropertyAnimationType_Scale: PropertyAnimationType = 0
PropertyAnimationType_Translation: PropertyAnimationType = 1
PropertyAnimationType_Opacity: PropertyAnimationType = 2
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
    InitialScaleX = property(get_InitialScaleX, None)
    InitialScaleY = property(get_InitialScaleY, None)
    FinalScaleX = property(get_FinalScaleX, None)
    FinalScaleY = property(get_FinalScaleY, None)
    NormalizedOrigin = property(get_NormalizedOrigin, None)
    Type = property(get_Type, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
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
    Type = property(get_Type, None)
    Delay = property(get_Delay, None)
    Duration = property(get_Duration, None)
    Control1 = property(get_Control1, None)
    Control2 = property(get_Control2, None)
make_head(_module, 'AnimationDescription')
make_head(_module, 'IAnimationDescription')
make_head(_module, 'IAnimationDescriptionFactory')
make_head(_module, 'IOpacityAnimation')
make_head(_module, 'IPropertyAnimation')
make_head(_module, 'IScaleAnimation')
make_head(_module, 'OpacityAnimation')
make_head(_module, 'PropertyAnimation')
make_head(_module, 'ScaleAnimation')
make_head(_module, 'TranslationAnimation')
