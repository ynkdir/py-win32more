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
import Windows.Devices.Haptics
import Windows.Devices.Input
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import Windows.System
import Windows.UI.Core
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
class AttachableInputObject(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_commethod(6)
    def Close(self) -> Void: ...
class CrossSlideThresholds(EasyCastStructure):
    SelectionStart: Single
    SpeedBumpStart: Single
    SpeedBumpEnd: Single
    RearrangeStart: Single
class CrossSlidingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.CrossSlidingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.ICrossSlidingEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.ICrossSlidingEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_CrossSlidingState(self: Windows.UI.Input.ICrossSlidingEventArgs) -> Windows.UI.Input.CrossSlidingState: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.ICrossSlidingEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    CrossSlidingState = property(get_CrossSlidingState, None)
    ContactCount = property(get_ContactCount, None)
CrossSlidingState = Int32
CrossSlidingState_Started: CrossSlidingState = 0
CrossSlidingState_Dragging: CrossSlidingState = 1
CrossSlidingState_Selecting: CrossSlidingState = 2
CrossSlidingState_SelectSpeedBumping: CrossSlidingState = 3
CrossSlidingState_SpeedBumping: CrossSlidingState = 4
CrossSlidingState_Rearranging: CrossSlidingState = 5
CrossSlidingState_Completed: CrossSlidingState = 6
class DraggingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.DraggingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.IDraggingEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IDraggingEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_DraggingState(self: Windows.UI.Input.IDraggingEventArgs) -> Windows.UI.Input.DraggingState: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.IDraggingEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    DraggingState = property(get_DraggingState, None)
    ContactCount = property(get_ContactCount, None)
DraggingState = Int32
DraggingState_Started: DraggingState = 0
DraggingState_Continuing: DraggingState = 1
DraggingState_Completed: DraggingState = 2
class EdgeGesture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.EdgeGesture'
    @winrt_mixinmethod
    def add_Starting(self: Windows.UI.Input.IEdgeGesture, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.EdgeGesture, Windows.UI.Input.EdgeGestureEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Starting(self: Windows.UI.Input.IEdgeGesture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.UI.Input.IEdgeGesture, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.EdgeGesture, Windows.UI.Input.EdgeGestureEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.UI.Input.IEdgeGesture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Canceled(self: Windows.UI.Input.IEdgeGesture, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.EdgeGesture, Windows.UI.Input.EdgeGestureEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: Windows.UI.Input.IEdgeGesture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Input.IEdgeGestureStatics) -> Windows.UI.Input.EdgeGesture: ...
class EdgeGestureEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.EdgeGestureEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.IEdgeGestureEventArgs) -> Windows.UI.Input.EdgeGestureKind: ...
    Kind = property(get_Kind, None)
EdgeGestureKind = Int32
EdgeGestureKind_Touch: EdgeGestureKind = 0
EdgeGestureKind_Keyboard: EdgeGestureKind = 1
EdgeGestureKind_Mouse: EdgeGestureKind = 2
GazeInputAccessStatus = Int32
GazeInputAccessStatus_Unspecified: GazeInputAccessStatus = 0
GazeInputAccessStatus_Allowed: GazeInputAccessStatus = 1
GazeInputAccessStatus_DeniedByUser: GazeInputAccessStatus = 2
GazeInputAccessStatus_DeniedBySystem: GazeInputAccessStatus = 3
class GestureRecognizer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.GestureRecognizer'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Input.GestureRecognizer: ...
    @winrt_mixinmethod
    def get_GestureSettings(self: Windows.UI.Input.IGestureRecognizer) -> Windows.UI.Input.GestureSettings: ...
    @winrt_mixinmethod
    def put_GestureSettings(self: Windows.UI.Input.IGestureRecognizer, value: Windows.UI.Input.GestureSettings) -> Void: ...
    @winrt_mixinmethod
    def get_IsInertial(self: Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShowGestureFeedback(self: Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowGestureFeedback(self: Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PivotCenter(self: Windows.UI.Input.IGestureRecognizer) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PivotCenter(self: Windows.UI.Input.IGestureRecognizer, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_PivotRadius(self: Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_PivotRadius(self: Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaTranslationDeceleration(self: Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaTranslationDeceleration(self: Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaRotationDeceleration(self: Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaRotationDeceleration(self: Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaExpansionDeceleration(self: Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaExpansionDeceleration(self: Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaTranslationDisplacement(self: Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaTranslationDisplacement(self: Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaRotationAngle(self: Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaRotationAngle(self: Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaExpansion(self: Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaExpansion(self: Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ManipulationExact(self: Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_ManipulationExact(self: Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideThresholds(self: Windows.UI.Input.IGestureRecognizer) -> Windows.UI.Input.CrossSlideThresholds: ...
    @winrt_mixinmethod
    def put_CrossSlideThresholds(self: Windows.UI.Input.IGestureRecognizer, value: Windows.UI.Input.CrossSlideThresholds) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideHorizontally(self: Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_CrossSlideHorizontally(self: Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideExact(self: Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_CrossSlideExact(self: Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutoProcessInertia(self: Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoProcessInertia(self: Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MouseWheelParameters(self: Windows.UI.Input.IGestureRecognizer) -> Windows.UI.Input.MouseWheelParameters: ...
    @winrt_mixinmethod
    def CanBeDoubleTap(self: Windows.UI.Input.IGestureRecognizer, value: Windows.UI.Input.PointerPoint) -> Boolean: ...
    @winrt_mixinmethod
    def ProcessDownEvent(self: Windows.UI.Input.IGestureRecognizer, value: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessMoveEvents(self: Windows.UI.Input.IGestureRecognizer, value: Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]) -> Void: ...
    @winrt_mixinmethod
    def ProcessUpEvent(self: Windows.UI.Input.IGestureRecognizer, value: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessMouseWheelEvent(self: Windows.UI.Input.IGestureRecognizer, value: Windows.UI.Input.PointerPoint, isShiftKeyDown: Boolean, isControlKeyDown: Boolean) -> Void: ...
    @winrt_mixinmethod
    def ProcessInertia(self: Windows.UI.Input.IGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def CompleteGesture(self: Windows.UI.Input.IGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.TappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RightTapped(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.RightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RightTapped(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Holding(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.HoldingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Holding(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Dragging(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.DraggingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dragging(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationUpdated(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationUpdated(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationInertiaStarting(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationInertiaStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationInertiaStarting(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CrossSliding(self: Windows.UI.Input.IGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.CrossSlidingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CrossSliding(self: Windows.UI.Input.IGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_TapMinContactCount(self: Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TapMinContactCount(self: Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TapMaxContactCount(self: Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TapMaxContactCount(self: Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldMinContactCount(self: Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_HoldMinContactCount(self: Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldMaxContactCount(self: Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_HoldMaxContactCount(self: Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldRadius(self: Windows.UI.Input.IGestureRecognizer2) -> Single: ...
    @winrt_mixinmethod
    def put_HoldRadius(self: Windows.UI.Input.IGestureRecognizer2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_HoldStartDelay(self: Windows.UI.Input.IGestureRecognizer2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_HoldStartDelay(self: Windows.UI.Input.IGestureRecognizer2, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationMinContactCount(self: Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TranslationMinContactCount(self: Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationMaxContactCount(self: Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TranslationMaxContactCount(self: Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    IsInertial = property(get_IsInertial, None)
    IsActive = property(get_IsActive, None)
    ShowGestureFeedback = property(get_ShowGestureFeedback, put_ShowGestureFeedback)
    PivotCenter = property(get_PivotCenter, put_PivotCenter)
    PivotRadius = property(get_PivotRadius, put_PivotRadius)
    InertiaTranslationDeceleration = property(get_InertiaTranslationDeceleration, put_InertiaTranslationDeceleration)
    InertiaRotationDeceleration = property(get_InertiaRotationDeceleration, put_InertiaRotationDeceleration)
    InertiaExpansionDeceleration = property(get_InertiaExpansionDeceleration, put_InertiaExpansionDeceleration)
    InertiaTranslationDisplacement = property(get_InertiaTranslationDisplacement, put_InertiaTranslationDisplacement)
    InertiaRotationAngle = property(get_InertiaRotationAngle, put_InertiaRotationAngle)
    InertiaExpansion = property(get_InertiaExpansion, put_InertiaExpansion)
    ManipulationExact = property(get_ManipulationExact, put_ManipulationExact)
    CrossSlideThresholds = property(get_CrossSlideThresholds, put_CrossSlideThresholds)
    CrossSlideHorizontally = property(get_CrossSlideHorizontally, put_CrossSlideHorizontally)
    CrossSlideExact = property(get_CrossSlideExact, put_CrossSlideExact)
    AutoProcessInertia = property(get_AutoProcessInertia, put_AutoProcessInertia)
    MouseWheelParameters = property(get_MouseWheelParameters, None)
    TapMinContactCount = property(get_TapMinContactCount, put_TapMinContactCount)
    TapMaxContactCount = property(get_TapMaxContactCount, put_TapMaxContactCount)
    HoldMinContactCount = property(get_HoldMinContactCount, put_HoldMinContactCount)
    HoldMaxContactCount = property(get_HoldMaxContactCount, put_HoldMaxContactCount)
    HoldRadius = property(get_HoldRadius, put_HoldRadius)
    HoldStartDelay = property(get_HoldStartDelay, put_HoldStartDelay)
    TranslationMinContactCount = property(get_TranslationMinContactCount, put_TranslationMinContactCount)
    TranslationMaxContactCount = property(get_TranslationMaxContactCount, put_TranslationMaxContactCount)
GestureSettings = UInt32
GestureSettings_None: GestureSettings = 0
GestureSettings_Tap: GestureSettings = 1
GestureSettings_DoubleTap: GestureSettings = 2
GestureSettings_Hold: GestureSettings = 4
GestureSettings_HoldWithMouse: GestureSettings = 8
GestureSettings_RightTap: GestureSettings = 16
GestureSettings_Drag: GestureSettings = 32
GestureSettings_ManipulationTranslateX: GestureSettings = 64
GestureSettings_ManipulationTranslateY: GestureSettings = 128
GestureSettings_ManipulationTranslateRailsX: GestureSettings = 256
GestureSettings_ManipulationTranslateRailsY: GestureSettings = 512
GestureSettings_ManipulationRotate: GestureSettings = 1024
GestureSettings_ManipulationScale: GestureSettings = 2048
GestureSettings_ManipulationTranslateInertia: GestureSettings = 4096
GestureSettings_ManipulationRotateInertia: GestureSettings = 8192
GestureSettings_ManipulationScaleInertia: GestureSettings = 16384
GestureSettings_CrossSlide: GestureSettings = 32768
GestureSettings_ManipulationMultipleFingerPanning: GestureSettings = 65536
class HoldingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.HoldingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.IHoldingEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IHoldingEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_HoldingState(self: Windows.UI.Input.IHoldingEventArgs) -> Windows.UI.Input.HoldingState: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.IHoldingEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentContactCount(self: Windows.UI.Input.IHoldingEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    HoldingState = property(get_HoldingState, None)
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
HoldingState = Int32
HoldingState_Started: HoldingState = 0
HoldingState_Completed: HoldingState = 1
HoldingState_Canceled: HoldingState = 2
class IAttachableInputObject(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9b822734-a3c1-542a-b2-f4-0e-32-b7-73-fb-07')
class IAttachableInputObjectFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a4c54c4e-42bc-58fa-a6-40-ea-15-16-f4-c0-6b')
class ICrossSlidingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e9374738-6f88-41d9-87-20-78-e0-8e-39-83-49')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_CrossSlidingState(self) -> Windows.UI.Input.CrossSlidingState: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    CrossSlidingState = property(get_CrossSlidingState, None)
class ICrossSlidingEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eefb7d48-c070-59f3-8d-ab-bc-af-62-1d-86-87')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IDraggingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1c905384-083c-4bd3-b5-59-17-9c-dd-eb-33-ec')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_DraggingState(self) -> Windows.UI.Input.DraggingState: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    DraggingState = property(get_DraggingState, None)
class IDraggingEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('71efdbf9-382a-55ca-b4-b9-00-81-23-c1-bf-1a')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IEdgeGesture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('580d5292-2ab1-49aa-a7-f0-33-bd-3f-8d-f9-f1')
    @winrt_commethod(6)
    def add_Starting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.EdgeGesture, Windows.UI.Input.EdgeGestureEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Starting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Completed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.EdgeGesture, Windows.UI.Input.EdgeGestureEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Canceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.EdgeGesture, Windows.UI.Input.EdgeGestureEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Canceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IEdgeGestureEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('44fa4a24-2d09-42e1-8b-5e-36-82-08-79-6a-4c')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.UI.Input.EdgeGestureKind: ...
    Kind = property(get_Kind, None)
class IEdgeGestureStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bc6a8519-18ee-4043-98-39-4f-c5-84-d6-0a-14')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Input.EdgeGesture: ...
class IGestureRecognizer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b47a37bf-3d6b-4f88-83-e8-6d-cb-40-12-ff-b0')
    @winrt_commethod(6)
    def get_GestureSettings(self) -> Windows.UI.Input.GestureSettings: ...
    @winrt_commethod(7)
    def put_GestureSettings(self, value: Windows.UI.Input.GestureSettings) -> Void: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ShowGestureFeedback(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_ShowGestureFeedback(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_PivotCenter(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def put_PivotCenter(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(14)
    def get_PivotRadius(self) -> Single: ...
    @winrt_commethod(15)
    def put_PivotRadius(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_InertiaTranslationDeceleration(self) -> Single: ...
    @winrt_commethod(17)
    def put_InertiaTranslationDeceleration(self, value: Single) -> Void: ...
    @winrt_commethod(18)
    def get_InertiaRotationDeceleration(self) -> Single: ...
    @winrt_commethod(19)
    def put_InertiaRotationDeceleration(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_InertiaExpansionDeceleration(self) -> Single: ...
    @winrt_commethod(21)
    def put_InertiaExpansionDeceleration(self, value: Single) -> Void: ...
    @winrt_commethod(22)
    def get_InertiaTranslationDisplacement(self) -> Single: ...
    @winrt_commethod(23)
    def put_InertiaTranslationDisplacement(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_InertiaRotationAngle(self) -> Single: ...
    @winrt_commethod(25)
    def put_InertiaRotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def get_InertiaExpansion(self) -> Single: ...
    @winrt_commethod(27)
    def put_InertiaExpansion(self, value: Single) -> Void: ...
    @winrt_commethod(28)
    def get_ManipulationExact(self) -> Boolean: ...
    @winrt_commethod(29)
    def put_ManipulationExact(self, value: Boolean) -> Void: ...
    @winrt_commethod(30)
    def get_CrossSlideThresholds(self) -> Windows.UI.Input.CrossSlideThresholds: ...
    @winrt_commethod(31)
    def put_CrossSlideThresholds(self, value: Windows.UI.Input.CrossSlideThresholds) -> Void: ...
    @winrt_commethod(32)
    def get_CrossSlideHorizontally(self) -> Boolean: ...
    @winrt_commethod(33)
    def put_CrossSlideHorizontally(self, value: Boolean) -> Void: ...
    @winrt_commethod(34)
    def get_CrossSlideExact(self) -> Boolean: ...
    @winrt_commethod(35)
    def put_CrossSlideExact(self, value: Boolean) -> Void: ...
    @winrt_commethod(36)
    def get_AutoProcessInertia(self) -> Boolean: ...
    @winrt_commethod(37)
    def put_AutoProcessInertia(self, value: Boolean) -> Void: ...
    @winrt_commethod(38)
    def get_MouseWheelParameters(self) -> Windows.UI.Input.MouseWheelParameters: ...
    @winrt_commethod(39)
    def CanBeDoubleTap(self, value: Windows.UI.Input.PointerPoint) -> Boolean: ...
    @winrt_commethod(40)
    def ProcessDownEvent(self, value: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(41)
    def ProcessMoveEvents(self, value: Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]) -> Void: ...
    @winrt_commethod(42)
    def ProcessUpEvent(self, value: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(43)
    def ProcessMouseWheelEvent(self, value: Windows.UI.Input.PointerPoint, isShiftKeyDown: Boolean, isControlKeyDown: Boolean) -> Void: ...
    @winrt_commethod(44)
    def ProcessInertia(self) -> Void: ...
    @winrt_commethod(45)
    def CompleteGesture(self) -> Void: ...
    @winrt_commethod(46)
    def add_Tapped(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.TappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(47)
    def remove_Tapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(48)
    def add_RightTapped(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.RightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(49)
    def remove_RightTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(50)
    def add_Holding(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.HoldingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(51)
    def remove_Holding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(52)
    def add_Dragging(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.DraggingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(53)
    def remove_Dragging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(54)
    def add_ManipulationStarted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(55)
    def remove_ManipulationStarted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(56)
    def add_ManipulationUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(57)
    def remove_ManipulationUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(58)
    def add_ManipulationInertiaStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationInertiaStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(59)
    def remove_ManipulationInertiaStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(60)
    def add_ManipulationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.ManipulationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(61)
    def remove_ManipulationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(62)
    def add_CrossSliding(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.GestureRecognizer, Windows.UI.Input.CrossSlidingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(63)
    def remove_CrossSliding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    IsInertial = property(get_IsInertial, None)
    IsActive = property(get_IsActive, None)
    ShowGestureFeedback = property(get_ShowGestureFeedback, put_ShowGestureFeedback)
    PivotCenter = property(get_PivotCenter, put_PivotCenter)
    PivotRadius = property(get_PivotRadius, put_PivotRadius)
    InertiaTranslationDeceleration = property(get_InertiaTranslationDeceleration, put_InertiaTranslationDeceleration)
    InertiaRotationDeceleration = property(get_InertiaRotationDeceleration, put_InertiaRotationDeceleration)
    InertiaExpansionDeceleration = property(get_InertiaExpansionDeceleration, put_InertiaExpansionDeceleration)
    InertiaTranslationDisplacement = property(get_InertiaTranslationDisplacement, put_InertiaTranslationDisplacement)
    InertiaRotationAngle = property(get_InertiaRotationAngle, put_InertiaRotationAngle)
    InertiaExpansion = property(get_InertiaExpansion, put_InertiaExpansion)
    ManipulationExact = property(get_ManipulationExact, put_ManipulationExact)
    CrossSlideThresholds = property(get_CrossSlideThresholds, put_CrossSlideThresholds)
    CrossSlideHorizontally = property(get_CrossSlideHorizontally, put_CrossSlideHorizontally)
    CrossSlideExact = property(get_CrossSlideExact, put_CrossSlideExact)
    AutoProcessInertia = property(get_AutoProcessInertia, put_AutoProcessInertia)
    MouseWheelParameters = property(get_MouseWheelParameters, None)
class IGestureRecognizer2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d646097f-6ef7-5746-8b-a8-8f-f2-20-6e-6f-3b')
    @winrt_commethod(6)
    def get_TapMinContactCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_TapMinContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_TapMaxContactCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_TapMaxContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_HoldMinContactCount(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_HoldMinContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_HoldMaxContactCount(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_HoldMaxContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_HoldRadius(self) -> Single: ...
    @winrt_commethod(15)
    def put_HoldRadius(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_HoldStartDelay(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def put_HoldStartDelay(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(18)
    def get_TranslationMinContactCount(self) -> UInt32: ...
    @winrt_commethod(19)
    def put_TranslationMinContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(20)
    def get_TranslationMaxContactCount(self) -> UInt32: ...
    @winrt_commethod(21)
    def put_TranslationMaxContactCount(self, value: UInt32) -> Void: ...
    TapMinContactCount = property(get_TapMinContactCount, put_TapMinContactCount)
    TapMaxContactCount = property(get_TapMaxContactCount, put_TapMaxContactCount)
    HoldMinContactCount = property(get_HoldMinContactCount, put_HoldMinContactCount)
    HoldMaxContactCount = property(get_HoldMaxContactCount, put_HoldMaxContactCount)
    HoldRadius = property(get_HoldRadius, put_HoldRadius)
    HoldStartDelay = property(get_HoldStartDelay, put_HoldStartDelay)
    TranslationMinContactCount = property(get_TranslationMinContactCount, put_TranslationMinContactCount)
    TranslationMaxContactCount = property(get_TranslationMaxContactCount, put_TranslationMaxContactCount)
class IHoldingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2bf755c5-e799-41b4-bb-40-24-2f-40-95-9b-71')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_HoldingState(self) -> Windows.UI.Input.HoldingState: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    HoldingState = property(get_HoldingState, None)
class IHoldingEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('141da9ea-4c79-5674-af-ea-49-3f-de-b9-1f-19')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CurrentContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class IInputActivationListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d6d4ed2-28c7-5ae3-aa-74-c9-18-a9-f2-43-ca')
    @winrt_commethod(6)
    def get_State(self) -> Windows.UI.Input.InputActivationState: ...
    @winrt_commethod(7)
    def add_InputActivationChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.InputActivationListener, Windows.UI.Input.InputActivationListenerActivationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_InputActivationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
class IInputActivationListenerActivationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7699b465-1dcf-5791-b4-b9-6c-af-be-ed-20-56')
    @winrt_commethod(6)
    def get_State(self) -> Windows.UI.Input.InputActivationState: ...
    State = property(get_State, None)
class IKeyboardDeliveryInterceptor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b4baf068-8f49-446c-8d-b5-8c-0f-fe-85-cc-9e')
    @winrt_commethod(6)
    def get_IsInterceptionEnabledWhenInForeground(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsInterceptionEnabledWhenInForeground(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def add_KeyDown(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.KeyboardDeliveryInterceptor, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_KeyDown(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_KeyUp(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.KeyboardDeliveryInterceptor, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_KeyUp(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsInterceptionEnabledWhenInForeground = property(get_IsInterceptionEnabledWhenInForeground, put_IsInterceptionEnabledWhenInForeground)
class IKeyboardDeliveryInterceptorStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f9f63ba2-ceba-4755-8a-7e-14-c0-ff-ec-d2-39')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Input.KeyboardDeliveryInterceptor: ...
class IManipulationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b34ab22b-d19b-46ff-9f-38-de-c7-75-4b-b9-e7')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(9)
    def get_Velocities(self) -> Windows.UI.Input.ManipulationVelocities: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
class IManipulationCompletedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f0c0dce7-30a9-5b96-88-6f-65-60-a8-5e-47-57')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CurrentContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class IManipulationInertiaStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dd37a898-26bf-467a-9c-e5-cc-f3-fb-11-37-1e')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Delta(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(9)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> Windows.UI.Input.ManipulationVelocities: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
class IManipulationInertiaStartingEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c25409b8-f9fa-5a45-bd-97-dc-bb-b2-20-18-60')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IManipulationStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ddec873e-cfce-4932-8c-1d-3c-3d-01-1a-34-c0')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Cumulative = property(get_Cumulative, None)
class IManipulationStartedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2da3db4e-e583-5055-af-aa-16-fd-98-65-31-a6')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IManipulationUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cb354ce5-abb8-4f9f-b3-ce-81-81-aa-61-ad-82')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Delta(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(9)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> Windows.UI.Input.ManipulationVelocities: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
class IManipulationUpdatedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f3dfb96a-3306-5903-a1-c5-ff-97-57-a8-68-9e')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CurrentContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class IMouseWheelParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ead0ca44-9ded-4037-81-49-5e-4c-c2-56-44-68')
    @winrt_commethod(6)
    def get_CharTranslation(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_CharTranslation(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_DeltaScale(self) -> Single: ...
    @winrt_commethod(9)
    def put_DeltaScale(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_DeltaRotationAngle(self) -> Single: ...
    @winrt_commethod(11)
    def put_DeltaRotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_PageTranslation(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def put_PageTranslation(self, value: Windows.Foundation.Point) -> Void: ...
    CharTranslation = property(get_CharTranslation, put_CharTranslation)
    DeltaScale = property(get_DeltaScale, put_DeltaScale)
    DeltaRotationAngle = property(get_DeltaRotationAngle, put_DeltaRotationAngle)
    PageTranslation = property(get_PageTranslation, put_PageTranslation)
class IPointerPoint(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e995317d-7296-42d9-82-33-c5-be-73-b7-4a-4a')
    @winrt_commethod(6)
    def get_PointerDevice(self) -> Windows.Devices.Input.PointerDevice: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_RawPosition(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_FrameId(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(12)
    def get_IsInContact(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_Properties(self) -> Windows.UI.Input.PointerPointProperties: ...
    PointerDevice = property(get_PointerDevice, None)
    Position = property(get_Position, None)
    RawPosition = property(get_RawPosition, None)
    PointerId = property(get_PointerId, None)
    FrameId = property(get_FrameId, None)
    Timestamp = property(get_Timestamp, None)
    IsInContact = property(get_IsInContact, None)
    Properties = property(get_Properties, None)
class IPointerPointProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c79d8a4b-c163-4ee7-80-3f-67-ce-79-f9-97-2d')
    @winrt_commethod(6)
    def get_Pressure(self) -> Single: ...
    @winrt_commethod(7)
    def get_IsInverted(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsEraser(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Orientation(self) -> Single: ...
    @winrt_commethod(10)
    def get_XTilt(self) -> Single: ...
    @winrt_commethod(11)
    def get_YTilt(self) -> Single: ...
    @winrt_commethod(12)
    def get_Twist(self) -> Single: ...
    @winrt_commethod(13)
    def get_ContactRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(14)
    def get_ContactRectRaw(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(15)
    def get_TouchConfidence(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsLeftButtonPressed(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsRightButtonPressed(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_IsMiddleButtonPressed(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_MouseWheelDelta(self) -> Int32: ...
    @winrt_commethod(20)
    def get_IsHorizontalMouseWheel(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_IsPrimary(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_IsInRange(self) -> Boolean: ...
    @winrt_commethod(23)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(24)
    def get_IsBarrelButtonPressed(self) -> Boolean: ...
    @winrt_commethod(25)
    def get_IsXButton1Pressed(self) -> Boolean: ...
    @winrt_commethod(26)
    def get_IsXButton2Pressed(self) -> Boolean: ...
    @winrt_commethod(27)
    def get_PointerUpdateKind(self) -> Windows.UI.Input.PointerUpdateKind: ...
    @winrt_commethod(28)
    def HasUsage(self, usagePage: UInt32, usageId: UInt32) -> Boolean: ...
    @winrt_commethod(29)
    def GetUsageValue(self, usagePage: UInt32, usageId: UInt32) -> Int32: ...
    Pressure = property(get_Pressure, None)
    IsInverted = property(get_IsInverted, None)
    IsEraser = property(get_IsEraser, None)
    Orientation = property(get_Orientation, None)
    XTilt = property(get_XTilt, None)
    YTilt = property(get_YTilt, None)
    Twist = property(get_Twist, None)
    ContactRect = property(get_ContactRect, None)
    ContactRectRaw = property(get_ContactRectRaw, None)
    TouchConfidence = property(get_TouchConfidence, None)
    IsLeftButtonPressed = property(get_IsLeftButtonPressed, None)
    IsRightButtonPressed = property(get_IsRightButtonPressed, None)
    IsMiddleButtonPressed = property(get_IsMiddleButtonPressed, None)
    MouseWheelDelta = property(get_MouseWheelDelta, None)
    IsHorizontalMouseWheel = property(get_IsHorizontalMouseWheel, None)
    IsPrimary = property(get_IsPrimary, None)
    IsInRange = property(get_IsInRange, None)
    IsCanceled = property(get_IsCanceled, None)
    IsBarrelButtonPressed = property(get_IsBarrelButtonPressed, None)
    IsXButton1Pressed = property(get_IsXButton1Pressed, None)
    IsXButton2Pressed = property(get_IsXButton2Pressed, None)
    PointerUpdateKind = property(get_PointerUpdateKind, None)
class IPointerPointProperties2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('22c3433a-c83b-41c0-a2-96-5e-23-2d-64-d6-af')
    @winrt_commethod(6)
    def get_ZDistance(self) -> Windows.Foundation.IReference[Single]: ...
    ZDistance = property(get_ZDistance, None)
class IPointerPointStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a506638d-2a1a-413e-bc-75-9f-38-38-1c-c0-69')
    @winrt_commethod(6)
    def GetCurrentPoint(self, pointerId: UInt32) -> Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(7)
    def GetIntermediatePoints(self, pointerId: UInt32) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
    @winrt_commethod(8)
    def GetCurrentPointTransformed(self, pointerId: UInt32, transform: Windows.UI.Input.IPointerPointTransform) -> Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(9)
    def GetIntermediatePointsTransformed(self, pointerId: UInt32, transform: Windows.UI.Input.IPointerPointTransform) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
class IPointerPointTransform(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4d5fe14f-b87c-4028-bc-9c-59-e9-94-7f-b0-56')
    @winrt_commethod(6)
    def get_Inverse(self) -> Windows.UI.Input.IPointerPointTransform: ...
    @winrt_commethod(7)
    def TryTransform(self, inPoint: Windows.Foundation.Point, outPoint: POINTER(Windows.Foundation.Point_head)) -> Boolean: ...
    @winrt_commethod(8)
    def TransformBounds(self, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
class IPointerVisualizationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4d1e6461-84f7-499d-bd-91-2a-36-e2-b7-aa-a2')
    @winrt_commethod(6)
    def put_IsContactFeedbackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsContactFeedbackEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsBarrelButtonFeedbackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsBarrelButtonFeedbackEnabled(self) -> Boolean: ...
    IsContactFeedbackEnabled = property(get_IsContactFeedbackEnabled, put_IsContactFeedbackEnabled)
    IsBarrelButtonFeedbackEnabled = property(get_IsBarrelButtonFeedbackEnabled, put_IsBarrelButtonFeedbackEnabled)
class IPointerVisualizationSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('68870edb-165b-4214-b4-f3-58-4e-ca-8c-8a-69')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Input.PointerVisualizationSettings: ...
class IRadialController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3055d1c8-df51-43d4-b2-3b-0e-10-37-46-7a-09')
    @winrt_commethod(6)
    def get_Menu(self) -> Windows.UI.Input.RadialControllerMenu: ...
    @winrt_commethod(7)
    def get_RotationResolutionInDegrees(self) -> Double: ...
    @winrt_commethod(8)
    def put_RotationResolutionInDegrees(self, value: Double) -> Void: ...
    @winrt_commethod(9)
    def get_UseAutomaticHapticFeedback(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_UseAutomaticHapticFeedback(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def add_ScreenContactStarted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerScreenContactStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ScreenContactStarted(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_ScreenContactEnded(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_ScreenContactEnded(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_ScreenContactContinued(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerScreenContactContinuedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ScreenContactContinued(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_ControlLost(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ControlLost(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_RotationChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerRotationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_RotationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_ButtonClicked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_ButtonClicked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_ControlAcquired(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerControlAcquiredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_ControlAcquired(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Menu = property(get_Menu, None)
    RotationResolutionInDegrees = property(get_RotationResolutionInDegrees, put_RotationResolutionInDegrees)
    UseAutomaticHapticFeedback = property(get_UseAutomaticHapticFeedback, put_UseAutomaticHapticFeedback)
class IRadialController2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577eff-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def add_ButtonPressed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ButtonPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ButtonHolding(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonHoldingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ButtonHolding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ButtonReleased(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonReleasedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ButtonReleased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRadialControllerButtonClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('206aa438-e651-11e5-bf-62-2c-27-d7-40-4e-85')
    @winrt_commethod(6)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerButtonClickedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577ef3-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerButtonHoldingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577eee-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerButtonPressedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577eed-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerButtonReleasedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577eef-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a6b79ecb-6a52-4430-91-0c-56-37-0a-9d-6b-42')
    @winrt_commethod(6)
    def SetDefaultMenuItems(self, buttons: Windows.Foundation.Collections.IIterable[Windows.UI.Input.RadialControllerSystemMenuItemKind]) -> Void: ...
    @winrt_commethod(7)
    def ResetToDefaultMenuItems(self) -> Void: ...
    @winrt_commethod(8)
    def TrySelectDefaultMenuItem(self, type: Windows.UI.Input.RadialControllerSystemMenuItemKind) -> Boolean: ...
class IRadialControllerConfiguration2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577ef7-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def put_ActiveControllerWhenMenuIsSuppressed(self, value: Windows.UI.Input.RadialController) -> Void: ...
    @winrt_commethod(7)
    def get_ActiveControllerWhenMenuIsSuppressed(self) -> Windows.UI.Input.RadialController: ...
    @winrt_commethod(8)
    def put_IsMenuSuppressed(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsMenuSuppressed(self) -> Boolean: ...
    ActiveControllerWhenMenuIsSuppressed = property(get_ActiveControllerWhenMenuIsSuppressed, put_ActiveControllerWhenMenuIsSuppressed)
    IsMenuSuppressed = property(get_IsMenuSuppressed, put_IsMenuSuppressed)
class IRadialControllerConfigurationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79b6b0e5-069a-4486-a9-9d-8d-b7-72-b9-64-2f')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Input.RadialControllerConfiguration: ...
class IRadialControllerConfigurationStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('53e08b17-e205-48d3-9c-af-80-ff-47-c4-d7-c7')
    @winrt_commethod(6)
    def put_AppController(self, value: Windows.UI.Input.RadialController) -> Void: ...
    @winrt_commethod(7)
    def get_AppController(self) -> Windows.UI.Input.RadialController: ...
    @winrt_commethod(8)
    def put_IsAppControllerEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsAppControllerEnabled(self) -> Boolean: ...
    AppController = property(get_AppController, put_AppController)
    IsAppControllerEnabled = property(get_IsAppControllerEnabled, put_IsAppControllerEnabled)
class IRadialControllerControlAcquiredEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('206aa439-e651-11e5-bf-62-2c-27-d7-40-4e-85')
    @winrt_commethod(6)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerControlAcquiredEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577ef4-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerMenu(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8506b35d-f640-4412-ab-a0-ba-d0-77-e5-ea-8a')
    @winrt_commethod(6)
    def get_Items(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.RadialControllerMenuItem]: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetSelectedMenuItem(self) -> Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_commethod(10)
    def SelectMenuItem(self, menuItem: Windows.UI.Input.RadialControllerMenuItem) -> Void: ...
    @winrt_commethod(11)
    def TrySelectPreviouslySelectedMenuItem(self) -> Boolean: ...
    Items = property(get_Items, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IRadialControllerMenuItem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c80fc98d-ad0b-4c9c-8f-2f-13-6a-23-73-a6-ba')
    @winrt_commethod(6)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Tag(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def put_Tag(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(9)
    def add_Invoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialControllerMenuItem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Invoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DisplayText = property(get_DisplayText, None)
    Tag = property(get_Tag, put_Tag)
class IRadialControllerMenuItemStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('249e0887-d842-4524-9d-f8-e0-d6-47-ed-c8-87')
    @winrt_commethod(6)
    def CreateFromIcon(self, displayText: WinRT_String, icon: Windows.Storage.Streams.RandomAccessStreamReference) -> Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_commethod(7)
    def CreateFromKnownIcon(self, displayText: WinRT_String, value: Windows.UI.Input.RadialControllerMenuKnownIcon) -> Windows.UI.Input.RadialControllerMenuItem: ...
class IRadialControllerMenuItemStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0cbb70be-7e3e-48bd-be-04-2c-7f-ca-a9-c1-ff')
    @winrt_commethod(6)
    def CreateFromFontGlyph(self, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String) -> Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_commethod(7)
    def CreateFromFontGlyphWithUri(self, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String, fontUri: Windows.Foundation.Uri) -> Windows.UI.Input.RadialControllerMenuItem: ...
class IRadialControllerRotationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('206aa435-e651-11e5-bf-62-2c-27-d7-40-4e-85')
    @winrt_commethod(6)
    def get_RotationDeltaInDegrees(self) -> Double: ...
    @winrt_commethod(7)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    RotationDeltaInDegrees = property(get_RotationDeltaInDegrees, None)
    Contact = property(get_Contact, None)
class IRadialControllerRotationChangedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577eec-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerScreenContact(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('206aa434-e651-11e5-bf-62-2c-27-d7-40-4e-85')
    @winrt_commethod(6)
    def get_Bounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    Bounds = property(get_Bounds, None)
    Position = property(get_Position, None)
class IRadialControllerScreenContactContinuedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('206aa437-e651-11e5-bf-62-2c-27-d7-40-4e-85')
    @winrt_commethod(6)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerScreenContactContinuedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577ef1-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerScreenContactEndedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577ef2-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerScreenContactStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('206aa436-e651-11e5-bf-62-2c-27-d7-40-4e-85')
    @winrt_commethod(6)
    def get_Contact(self) -> Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerScreenContactStartedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d577ef0-3cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('faded0b7-b84c-4894-87-aa-8f-25-aa-5f-28-8b')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def CreateForCurrentView(self) -> Windows.UI.Input.RadialController: ...
class IRightTappedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4cbf40bd-af7a-4a36-94-76-b1-dc-e1-41-70-9a')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IRightTappedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('61c7b7bb-9f57-5857-a3-3c-c5-8c-3d-fa-95-9e')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class ISystemButtonEventController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59b893a9-73bc-52b5-ba-41-82-51-1b-2c-b4-6c')
    @winrt_commethod(6)
    def add_SystemFunctionButtonPressed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionButtonEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SystemFunctionButtonPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SystemFunctionButtonReleased(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionButtonEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SystemFunctionButtonReleased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SystemFunctionLockChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionLockChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SystemFunctionLockChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_SystemFunctionLockIndicatorChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionLockIndicatorChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SystemFunctionLockIndicatorChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISystemButtonEventControllerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('632fb07b-20bd-5e15-af-4a-00-db-f2-06-4f-fa')
    @winrt_commethod(6)
    def CreateForDispatcherQueue(self, queue: Windows.System.DispatcherQueue) -> Windows.UI.Input.SystemButtonEventController: ...
class ISystemFunctionButtonEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4833896f-80d1-5dd6-92-a7-62-a5-08-ff-ef-5a')
    @winrt_commethod(6)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    Handled = property(get_Handled, put_Handled)
class ISystemFunctionLockChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cd040608-fcf9-585c-be-ab-f1-d2-ea-f3-64-ab')
    @winrt_commethod(6)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_IsLocked(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    IsLocked = property(get_IsLocked, None)
    Handled = property(get_Handled, put_Handled)
class ISystemFunctionLockIndicatorChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b212b94e-7a6f-58ae-b3-04-ba-e6-1d-03-71-b9')
    @winrt_commethod(6)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_IsIndicatorOn(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    IsIndicatorOn = property(get_IsIndicatorOn, None)
    Handled = property(get_Handled, put_Handled)
class ITappedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cfa126e4-253a-4c3c-95-3b-39-5c-37-ae-d3-09')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_TapCount(self) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    TapCount = property(get_TapCount, None)
class ITappedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('294388f2-177e-51d5-be-56-ee-08-66-fa-96-8c')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class InputActivationListener(c_void_p):
    extends: Windows.UI.Input.AttachableInputObject
    ClassId = 'Windows.UI.Input.InputActivationListener'
    @winrt_mixinmethod
    def get_State(self: Windows.UI.Input.IInputActivationListener) -> Windows.UI.Input.InputActivationState: ...
    @winrt_mixinmethod
    def add_InputActivationChanged(self: Windows.UI.Input.IInputActivationListener, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.InputActivationListener, Windows.UI.Input.InputActivationListenerActivationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputActivationChanged(self: Windows.UI.Input.IInputActivationListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
class InputActivationListenerActivationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.InputActivationListenerActivationChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: Windows.UI.Input.IInputActivationListenerActivationChangedEventArgs) -> Windows.UI.Input.InputActivationState: ...
    State = property(get_State, None)
InputActivationState = Int32
InputActivationState_None: InputActivationState = 0
InputActivationState_Deactivated: InputActivationState = 1
InputActivationState_ActivatedNotForeground: InputActivationState = 2
InputActivationState_ActivatedInForeground: InputActivationState = 3
class KeyboardDeliveryInterceptor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.KeyboardDeliveryInterceptor'
    @winrt_mixinmethod
    def get_IsInterceptionEnabledWhenInForeground(self: Windows.UI.Input.IKeyboardDeliveryInterceptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInterceptionEnabledWhenInForeground(self: Windows.UI.Input.IKeyboardDeliveryInterceptor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_KeyDown(self: Windows.UI.Input.IKeyboardDeliveryInterceptor, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.KeyboardDeliveryInterceptor, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyDown(self: Windows.UI.Input.IKeyboardDeliveryInterceptor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyUp(self: Windows.UI.Input.IKeyboardDeliveryInterceptor, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.KeyboardDeliveryInterceptor, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyUp(self: Windows.UI.Input.IKeyboardDeliveryInterceptor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Input.IKeyboardDeliveryInterceptorStatics) -> Windows.UI.Input.KeyboardDeliveryInterceptor: ...
    IsInterceptionEnabledWhenInForeground = property(get_IsInterceptionEnabledWhenInForeground, put_IsInterceptionEnabledWhenInForeground)
class ManipulationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.ManipulationCompletedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.IManipulationCompletedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IManipulationCompletedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Cumulative(self: Windows.UI.Input.IManipulationCompletedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: Windows.UI.Input.IManipulationCompletedEventArgs) -> Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.IManipulationCompletedEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentContactCount(self: Windows.UI.Input.IManipulationCompletedEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class ManipulationDelta(EasyCastStructure):
    Translation: Windows.Foundation.Point
    Scale: Single
    Rotation: Single
    Expansion: Single
class ManipulationInertiaStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.ManipulationInertiaStartingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Delta(self: Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.IManipulationInertiaStartingEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    ContactCount = property(get_ContactCount, None)
class ManipulationStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.ManipulationStartedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.IManipulationStartedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IManipulationStartedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Cumulative(self: Windows.UI.Input.IManipulationStartedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.IManipulationStartedEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Cumulative = property(get_Cumulative, None)
    ContactCount = property(get_ContactCount, None)
class ManipulationUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.ManipulationUpdatedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.IManipulationUpdatedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IManipulationUpdatedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Delta(self: Windows.UI.Input.IManipulationUpdatedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: Windows.UI.Input.IManipulationUpdatedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: Windows.UI.Input.IManipulationUpdatedEventArgs) -> Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.IManipulationUpdatedEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentContactCount(self: Windows.UI.Input.IManipulationUpdatedEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class ManipulationVelocities(EasyCastStructure):
    Linear: Windows.Foundation.Point
    Angular: Single
    Expansion: Single
class MouseWheelParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.MouseWheelParameters'
    @winrt_mixinmethod
    def get_CharTranslation(self: Windows.UI.Input.IMouseWheelParameters) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_CharTranslation(self: Windows.UI.Input.IMouseWheelParameters, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaScale(self: Windows.UI.Input.IMouseWheelParameters) -> Single: ...
    @winrt_mixinmethod
    def put_DeltaScale(self: Windows.UI.Input.IMouseWheelParameters, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaRotationAngle(self: Windows.UI.Input.IMouseWheelParameters) -> Single: ...
    @winrt_mixinmethod
    def put_DeltaRotationAngle(self: Windows.UI.Input.IMouseWheelParameters, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_PageTranslation(self: Windows.UI.Input.IMouseWheelParameters) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PageTranslation(self: Windows.UI.Input.IMouseWheelParameters, value: Windows.Foundation.Point) -> Void: ...
    CharTranslation = property(get_CharTranslation, put_CharTranslation)
    DeltaScale = property(get_DeltaScale, put_DeltaScale)
    DeltaRotationAngle = property(get_DeltaRotationAngle, put_DeltaRotationAngle)
    PageTranslation = property(get_PageTranslation, put_PageTranslation)
class PointerPoint(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.PointerPoint'
    @winrt_mixinmethod
    def get_PointerDevice(self: Windows.UI.Input.IPointerPoint) -> Windows.Devices.Input.PointerDevice: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IPointerPoint) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_RawPosition(self: Windows.UI.Input.IPointerPoint) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_PointerId(self: Windows.UI.Input.IPointerPoint) -> UInt32: ...
    @winrt_mixinmethod
    def get_FrameId(self: Windows.UI.Input.IPointerPoint) -> UInt32: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.UI.Input.IPointerPoint) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsInContact(self: Windows.UI.Input.IPointerPoint) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.UI.Input.IPointerPoint) -> Windows.UI.Input.PointerPointProperties: ...
    @winrt_classmethod
    def GetCurrentPoint(cls: Windows.UI.Input.IPointerPointStatics, pointerId: UInt32) -> Windows.UI.Input.PointerPoint: ...
    @winrt_classmethod
    def GetIntermediatePoints(cls: Windows.UI.Input.IPointerPointStatics, pointerId: UInt32) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
    @winrt_classmethod
    def GetCurrentPointTransformed(cls: Windows.UI.Input.IPointerPointStatics, pointerId: UInt32, transform: Windows.UI.Input.IPointerPointTransform) -> Windows.UI.Input.PointerPoint: ...
    @winrt_classmethod
    def GetIntermediatePointsTransformed(cls: Windows.UI.Input.IPointerPointStatics, pointerId: UInt32, transform: Windows.UI.Input.IPointerPointTransform) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
    PointerDevice = property(get_PointerDevice, None)
    Position = property(get_Position, None)
    RawPosition = property(get_RawPosition, None)
    PointerId = property(get_PointerId, None)
    FrameId = property(get_FrameId, None)
    Timestamp = property(get_Timestamp, None)
    IsInContact = property(get_IsInContact, None)
    Properties = property(get_Properties, None)
class PointerPointProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.PointerPointProperties'
    @winrt_mixinmethod
    def get_Pressure(self: Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_IsInverted(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsEraser(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_XTilt(self: Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_YTilt(self: Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_Twist(self: Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_ContactRect(self: Windows.UI.Input.IPointerPointProperties) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_ContactRectRaw(self: Windows.UI.Input.IPointerPointProperties) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_TouchConfidence(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLeftButtonPressed(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRightButtonPressed(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMiddleButtonPressed(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_MouseWheelDelta(self: Windows.UI.Input.IPointerPointProperties) -> Int32: ...
    @winrt_mixinmethod
    def get_IsHorizontalMouseWheel(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPrimary(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInRange(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBarrelButtonPressed(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsXButton1Pressed(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsXButton2Pressed(self: Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_PointerUpdateKind(self: Windows.UI.Input.IPointerPointProperties) -> Windows.UI.Input.PointerUpdateKind: ...
    @winrt_mixinmethod
    def HasUsage(self: Windows.UI.Input.IPointerPointProperties, usagePage: UInt32, usageId: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def GetUsageValue(self: Windows.UI.Input.IPointerPointProperties, usagePage: UInt32, usageId: UInt32) -> Int32: ...
    @winrt_mixinmethod
    def get_ZDistance(self: Windows.UI.Input.IPointerPointProperties2) -> Windows.Foundation.IReference[Single]: ...
    Pressure = property(get_Pressure, None)
    IsInverted = property(get_IsInverted, None)
    IsEraser = property(get_IsEraser, None)
    Orientation = property(get_Orientation, None)
    XTilt = property(get_XTilt, None)
    YTilt = property(get_YTilt, None)
    Twist = property(get_Twist, None)
    ContactRect = property(get_ContactRect, None)
    ContactRectRaw = property(get_ContactRectRaw, None)
    TouchConfidence = property(get_TouchConfidence, None)
    IsLeftButtonPressed = property(get_IsLeftButtonPressed, None)
    IsRightButtonPressed = property(get_IsRightButtonPressed, None)
    IsMiddleButtonPressed = property(get_IsMiddleButtonPressed, None)
    MouseWheelDelta = property(get_MouseWheelDelta, None)
    IsHorizontalMouseWheel = property(get_IsHorizontalMouseWheel, None)
    IsPrimary = property(get_IsPrimary, None)
    IsInRange = property(get_IsInRange, None)
    IsCanceled = property(get_IsCanceled, None)
    IsBarrelButtonPressed = property(get_IsBarrelButtonPressed, None)
    IsXButton1Pressed = property(get_IsXButton1Pressed, None)
    IsXButton2Pressed = property(get_IsXButton2Pressed, None)
    PointerUpdateKind = property(get_PointerUpdateKind, None)
    ZDistance = property(get_ZDistance, None)
PointerUpdateKind = Int32
PointerUpdateKind_Other: PointerUpdateKind = 0
PointerUpdateKind_LeftButtonPressed: PointerUpdateKind = 1
PointerUpdateKind_LeftButtonReleased: PointerUpdateKind = 2
PointerUpdateKind_RightButtonPressed: PointerUpdateKind = 3
PointerUpdateKind_RightButtonReleased: PointerUpdateKind = 4
PointerUpdateKind_MiddleButtonPressed: PointerUpdateKind = 5
PointerUpdateKind_MiddleButtonReleased: PointerUpdateKind = 6
PointerUpdateKind_XButton1Pressed: PointerUpdateKind = 7
PointerUpdateKind_XButton1Released: PointerUpdateKind = 8
PointerUpdateKind_XButton2Pressed: PointerUpdateKind = 9
PointerUpdateKind_XButton2Released: PointerUpdateKind = 10
class PointerVisualizationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.PointerVisualizationSettings'
    @winrt_mixinmethod
    def put_IsContactFeedbackEnabled(self: Windows.UI.Input.IPointerVisualizationSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsContactFeedbackEnabled(self: Windows.UI.Input.IPointerVisualizationSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBarrelButtonFeedbackEnabled(self: Windows.UI.Input.IPointerVisualizationSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBarrelButtonFeedbackEnabled(self: Windows.UI.Input.IPointerVisualizationSettings) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Input.IPointerVisualizationSettingsStatics) -> Windows.UI.Input.PointerVisualizationSettings: ...
    IsContactFeedbackEnabled = property(get_IsContactFeedbackEnabled, put_IsContactFeedbackEnabled)
    IsBarrelButtonFeedbackEnabled = property(get_IsBarrelButtonFeedbackEnabled, put_IsBarrelButtonFeedbackEnabled)
class RadialController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialController'
    @winrt_mixinmethod
    def get_Menu(self: Windows.UI.Input.IRadialController) -> Windows.UI.Input.RadialControllerMenu: ...
    @winrt_mixinmethod
    def get_RotationResolutionInDegrees(self: Windows.UI.Input.IRadialController) -> Double: ...
    @winrt_mixinmethod
    def put_RotationResolutionInDegrees(self: Windows.UI.Input.IRadialController, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_UseAutomaticHapticFeedback(self: Windows.UI.Input.IRadialController) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseAutomaticHapticFeedback(self: Windows.UI.Input.IRadialController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_ScreenContactStarted(self: Windows.UI.Input.IRadialController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerScreenContactStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenContactStarted(self: Windows.UI.Input.IRadialController, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScreenContactEnded(self: Windows.UI.Input.IRadialController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenContactEnded(self: Windows.UI.Input.IRadialController, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScreenContactContinued(self: Windows.UI.Input.IRadialController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerScreenContactContinuedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenContactContinued(self: Windows.UI.Input.IRadialController, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ControlLost(self: Windows.UI.Input.IRadialController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ControlLost(self: Windows.UI.Input.IRadialController, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RotationChanged(self: Windows.UI.Input.IRadialController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerRotationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RotationChanged(self: Windows.UI.Input.IRadialController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonClicked(self: Windows.UI.Input.IRadialController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonClicked(self: Windows.UI.Input.IRadialController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ControlAcquired(self: Windows.UI.Input.IRadialController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerControlAcquiredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ControlAcquired(self: Windows.UI.Input.IRadialController, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonPressed(self: Windows.UI.Input.IRadialController2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonPressed(self: Windows.UI.Input.IRadialController2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonHolding(self: Windows.UI.Input.IRadialController2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonHoldingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonHolding(self: Windows.UI.Input.IRadialController2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonReleased(self: Windows.UI.Input.IRadialController2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialController, Windows.UI.Input.RadialControllerButtonReleasedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonReleased(self: Windows.UI.Input.IRadialController2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.UI.Input.IRadialControllerStatics) -> Boolean: ...
    @winrt_classmethod
    def CreateForCurrentView(cls: Windows.UI.Input.IRadialControllerStatics) -> Windows.UI.Input.RadialController: ...
    Menu = property(get_Menu, None)
    RotationResolutionInDegrees = property(get_RotationResolutionInDegrees, put_RotationResolutionInDegrees)
    UseAutomaticHapticFeedback = property(get_UseAutomaticHapticFeedback, put_UseAutomaticHapticFeedback)
class RadialControllerButtonClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerButtonClickedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerButtonClickedEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerButtonClickedEventArgs2) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerButtonHoldingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerButtonHoldingEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerButtonHoldingEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerButtonHoldingEventArgs) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerButtonPressedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerButtonPressedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerButtonPressedEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerButtonPressedEventArgs) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerButtonReleasedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerButtonReleasedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerButtonReleasedEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerButtonReleasedEventArgs) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerConfiguration'
    @winrt_mixinmethod
    def SetDefaultMenuItems(self: Windows.UI.Input.IRadialControllerConfiguration, buttons: Windows.Foundation.Collections.IIterable[Windows.UI.Input.RadialControllerSystemMenuItemKind]) -> Void: ...
    @winrt_mixinmethod
    def ResetToDefaultMenuItems(self: Windows.UI.Input.IRadialControllerConfiguration) -> Void: ...
    @winrt_mixinmethod
    def TrySelectDefaultMenuItem(self: Windows.UI.Input.IRadialControllerConfiguration, type: Windows.UI.Input.RadialControllerSystemMenuItemKind) -> Boolean: ...
    @winrt_mixinmethod
    def put_ActiveControllerWhenMenuIsSuppressed(self: Windows.UI.Input.IRadialControllerConfiguration2, value: Windows.UI.Input.RadialController) -> Void: ...
    @winrt_mixinmethod
    def get_ActiveControllerWhenMenuIsSuppressed(self: Windows.UI.Input.IRadialControllerConfiguration2) -> Windows.UI.Input.RadialController: ...
    @winrt_mixinmethod
    def put_IsMenuSuppressed(self: Windows.UI.Input.IRadialControllerConfiguration2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsMenuSuppressed(self: Windows.UI.Input.IRadialControllerConfiguration2) -> Boolean: ...
    @winrt_classmethod
    def put_AppController(cls: Windows.UI.Input.IRadialControllerConfigurationStatics2, value: Windows.UI.Input.RadialController) -> Void: ...
    @winrt_classmethod
    def get_AppController(cls: Windows.UI.Input.IRadialControllerConfigurationStatics2) -> Windows.UI.Input.RadialController: ...
    @winrt_classmethod
    def put_IsAppControllerEnabled(cls: Windows.UI.Input.IRadialControllerConfigurationStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsAppControllerEnabled(cls: Windows.UI.Input.IRadialControllerConfigurationStatics2) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Input.IRadialControllerConfigurationStatics) -> Windows.UI.Input.RadialControllerConfiguration: ...
    ActiveControllerWhenMenuIsSuppressed = property(get_ActiveControllerWhenMenuIsSuppressed, put_ActiveControllerWhenMenuIsSuppressed)
    IsMenuSuppressed = property(get_IsMenuSuppressed, put_IsMenuSuppressed)
    AppController = property(get_AppController, put_AppController)
    IsAppControllerEnabled = property(get_IsAppControllerEnabled, put_IsAppControllerEnabled)
class RadialControllerControlAcquiredEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerControlAcquiredEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerControlAcquiredEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: Windows.UI.Input.IRadialControllerControlAcquiredEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerControlAcquiredEventArgs2) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerMenu(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerMenu'
    @winrt_mixinmethod
    def get_Items(self: Windows.UI.Input.IRadialControllerMenu) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.RadialControllerMenuItem]: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.UI.Input.IRadialControllerMenu) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.UI.Input.IRadialControllerMenu, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetSelectedMenuItem(self: Windows.UI.Input.IRadialControllerMenu) -> Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_mixinmethod
    def SelectMenuItem(self: Windows.UI.Input.IRadialControllerMenu, menuItem: Windows.UI.Input.RadialControllerMenuItem) -> Void: ...
    @winrt_mixinmethod
    def TrySelectPreviouslySelectedMenuItem(self: Windows.UI.Input.IRadialControllerMenu) -> Boolean: ...
    Items = property(get_Items, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class RadialControllerMenuItem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerMenuItem'
    @winrt_mixinmethod
    def get_DisplayText(self: Windows.UI.Input.IRadialControllerMenuItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.UI.Input.IRadialControllerMenuItem) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.UI.Input.IRadialControllerMenuItem, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def add_Invoked(self: Windows.UI.Input.IRadialControllerMenuItem, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.RadialControllerMenuItem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Invoked(self: Windows.UI.Input.IRadialControllerMenuItem, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateFromFontGlyph(cls: Windows.UI.Input.IRadialControllerMenuItemStatics2, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String) -> Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_classmethod
    def CreateFromFontGlyphWithUri(cls: Windows.UI.Input.IRadialControllerMenuItemStatics2, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String, fontUri: Windows.Foundation.Uri) -> Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_classmethod
    def CreateFromIcon(cls: Windows.UI.Input.IRadialControllerMenuItemStatics, displayText: WinRT_String, icon: Windows.Storage.Streams.RandomAccessStreamReference) -> Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_classmethod
    def CreateFromKnownIcon(cls: Windows.UI.Input.IRadialControllerMenuItemStatics, displayText: WinRT_String, value: Windows.UI.Input.RadialControllerMenuKnownIcon) -> Windows.UI.Input.RadialControllerMenuItem: ...
    DisplayText = property(get_DisplayText, None)
    Tag = property(get_Tag, put_Tag)
RadialControllerMenuKnownIcon = Int32
RadialControllerMenuKnownIcon_Scroll: RadialControllerMenuKnownIcon = 0
RadialControllerMenuKnownIcon_Zoom: RadialControllerMenuKnownIcon = 1
RadialControllerMenuKnownIcon_UndoRedo: RadialControllerMenuKnownIcon = 2
RadialControllerMenuKnownIcon_Volume: RadialControllerMenuKnownIcon = 3
RadialControllerMenuKnownIcon_NextPreviousTrack: RadialControllerMenuKnownIcon = 4
RadialControllerMenuKnownIcon_Ruler: RadialControllerMenuKnownIcon = 5
RadialControllerMenuKnownIcon_InkColor: RadialControllerMenuKnownIcon = 6
RadialControllerMenuKnownIcon_InkThickness: RadialControllerMenuKnownIcon = 7
RadialControllerMenuKnownIcon_PenType: RadialControllerMenuKnownIcon = 8
class RadialControllerRotationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerRotationChangedEventArgs'
    @winrt_mixinmethod
    def get_RotationDeltaInDegrees(self: Windows.UI.Input.IRadialControllerRotationChangedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerRotationChangedEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: Windows.UI.Input.IRadialControllerRotationChangedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerRotationChangedEventArgs2) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    RotationDeltaInDegrees = property(get_RotationDeltaInDegrees, None)
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerScreenContact(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerScreenContact'
    @winrt_mixinmethod
    def get_Bounds(self: Windows.UI.Input.IRadialControllerScreenContact) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IRadialControllerScreenContact) -> Windows.Foundation.Point: ...
    Bounds = property(get_Bounds, None)
    Position = property(get_Position, None)
class RadialControllerScreenContactContinuedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerScreenContactContinuedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs2) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerScreenContactEndedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerScreenContactEndedEventArgs'
    @winrt_mixinmethod
    def get_IsButtonPressed(self: Windows.UI.Input.IRadialControllerScreenContactEndedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerScreenContactEndedEventArgs) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerScreenContactStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RadialControllerScreenContactStartedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs) -> Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs2) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
RadialControllerSystemMenuItemKind = Int32
RadialControllerSystemMenuItemKind_Scroll: RadialControllerSystemMenuItemKind = 0
RadialControllerSystemMenuItemKind_Zoom: RadialControllerSystemMenuItemKind = 1
RadialControllerSystemMenuItemKind_UndoRedo: RadialControllerSystemMenuItemKind = 2
RadialControllerSystemMenuItemKind_Volume: RadialControllerSystemMenuItemKind = 3
RadialControllerSystemMenuItemKind_NextPreviousTrack: RadialControllerSystemMenuItemKind = 4
class RightTappedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.RightTappedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.IRightTappedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.IRightTappedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.IRightTappedEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    ContactCount = property(get_ContactCount, None)
class SystemButtonEventController(c_void_p):
    extends: Windows.UI.Input.AttachableInputObject
    ClassId = 'Windows.UI.Input.SystemButtonEventController'
    @winrt_mixinmethod
    def add_SystemFunctionButtonPressed(self: Windows.UI.Input.ISystemButtonEventController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionButtonEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionButtonPressed(self: Windows.UI.Input.ISystemButtonEventController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemFunctionButtonReleased(self: Windows.UI.Input.ISystemButtonEventController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionButtonEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionButtonReleased(self: Windows.UI.Input.ISystemButtonEventController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemFunctionLockChanged(self: Windows.UI.Input.ISystemButtonEventController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionLockChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionLockChanged(self: Windows.UI.Input.ISystemButtonEventController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemFunctionLockIndicatorChanged(self: Windows.UI.Input.ISystemButtonEventController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.SystemButtonEventController, Windows.UI.Input.SystemFunctionLockIndicatorChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionLockIndicatorChanged(self: Windows.UI.Input.ISystemButtonEventController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateForDispatcherQueue(cls: Windows.UI.Input.ISystemButtonEventControllerStatics, queue: Windows.System.DispatcherQueue) -> Windows.UI.Input.SystemButtonEventController: ...
class SystemFunctionButtonEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.SystemFunctionButtonEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.UI.Input.ISystemFunctionButtonEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Input.ISystemFunctionButtonEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Input.ISystemFunctionButtonEventArgs, value: Boolean) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    Handled = property(get_Handled, put_Handled)
class SystemFunctionLockChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.SystemFunctionLockChangedEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.UI.Input.ISystemFunctionLockChangedEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsLocked(self: Windows.UI.Input.ISystemFunctionLockChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Input.ISystemFunctionLockChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Input.ISystemFunctionLockChangedEventArgs, value: Boolean) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    IsLocked = property(get_IsLocked, None)
    Handled = property(get_Handled, put_Handled)
class SystemFunctionLockIndicatorChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.SystemFunctionLockIndicatorChangedEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsIndicatorOn(self: Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs, value: Boolean) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    IsIndicatorOn = property(get_IsIndicatorOn, None)
    Handled = property(get_Handled, put_Handled)
class TappedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.TappedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Input.ITappedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.ITappedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_TapCount(self: Windows.UI.Input.ITappedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_ContactCount(self: Windows.UI.Input.ITappedEventArgs2) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    TapCount = property(get_TapCount, None)
    ContactCount = property(get_ContactCount, None)
make_head(_module, 'AttachableInputObject')
make_head(_module, 'CrossSlideThresholds')
make_head(_module, 'CrossSlidingEventArgs')
make_head(_module, 'DraggingEventArgs')
make_head(_module, 'EdgeGesture')
make_head(_module, 'EdgeGestureEventArgs')
make_head(_module, 'GestureRecognizer')
make_head(_module, 'HoldingEventArgs')
make_head(_module, 'IAttachableInputObject')
make_head(_module, 'IAttachableInputObjectFactory')
make_head(_module, 'ICrossSlidingEventArgs')
make_head(_module, 'ICrossSlidingEventArgs2')
make_head(_module, 'IDraggingEventArgs')
make_head(_module, 'IDraggingEventArgs2')
make_head(_module, 'IEdgeGesture')
make_head(_module, 'IEdgeGestureEventArgs')
make_head(_module, 'IEdgeGestureStatics')
make_head(_module, 'IGestureRecognizer')
make_head(_module, 'IGestureRecognizer2')
make_head(_module, 'IHoldingEventArgs')
make_head(_module, 'IHoldingEventArgs2')
make_head(_module, 'IInputActivationListener')
make_head(_module, 'IInputActivationListenerActivationChangedEventArgs')
make_head(_module, 'IKeyboardDeliveryInterceptor')
make_head(_module, 'IKeyboardDeliveryInterceptorStatics')
make_head(_module, 'IManipulationCompletedEventArgs')
make_head(_module, 'IManipulationCompletedEventArgs2')
make_head(_module, 'IManipulationInertiaStartingEventArgs')
make_head(_module, 'IManipulationInertiaStartingEventArgs2')
make_head(_module, 'IManipulationStartedEventArgs')
make_head(_module, 'IManipulationStartedEventArgs2')
make_head(_module, 'IManipulationUpdatedEventArgs')
make_head(_module, 'IManipulationUpdatedEventArgs2')
make_head(_module, 'IMouseWheelParameters')
make_head(_module, 'IPointerPoint')
make_head(_module, 'IPointerPointProperties')
make_head(_module, 'IPointerPointProperties2')
make_head(_module, 'IPointerPointStatics')
make_head(_module, 'IPointerPointTransform')
make_head(_module, 'IPointerVisualizationSettings')
make_head(_module, 'IPointerVisualizationSettingsStatics')
make_head(_module, 'IRadialController')
make_head(_module, 'IRadialController2')
make_head(_module, 'IRadialControllerButtonClickedEventArgs')
make_head(_module, 'IRadialControllerButtonClickedEventArgs2')
make_head(_module, 'IRadialControllerButtonHoldingEventArgs')
make_head(_module, 'IRadialControllerButtonPressedEventArgs')
make_head(_module, 'IRadialControllerButtonReleasedEventArgs')
make_head(_module, 'IRadialControllerConfiguration')
make_head(_module, 'IRadialControllerConfiguration2')
make_head(_module, 'IRadialControllerConfigurationStatics')
make_head(_module, 'IRadialControllerConfigurationStatics2')
make_head(_module, 'IRadialControllerControlAcquiredEventArgs')
make_head(_module, 'IRadialControllerControlAcquiredEventArgs2')
make_head(_module, 'IRadialControllerMenu')
make_head(_module, 'IRadialControllerMenuItem')
make_head(_module, 'IRadialControllerMenuItemStatics')
make_head(_module, 'IRadialControllerMenuItemStatics2')
make_head(_module, 'IRadialControllerRotationChangedEventArgs')
make_head(_module, 'IRadialControllerRotationChangedEventArgs2')
make_head(_module, 'IRadialControllerScreenContact')
make_head(_module, 'IRadialControllerScreenContactContinuedEventArgs')
make_head(_module, 'IRadialControllerScreenContactContinuedEventArgs2')
make_head(_module, 'IRadialControllerScreenContactEndedEventArgs')
make_head(_module, 'IRadialControllerScreenContactStartedEventArgs')
make_head(_module, 'IRadialControllerScreenContactStartedEventArgs2')
make_head(_module, 'IRadialControllerStatics')
make_head(_module, 'IRightTappedEventArgs')
make_head(_module, 'IRightTappedEventArgs2')
make_head(_module, 'ISystemButtonEventController')
make_head(_module, 'ISystemButtonEventControllerStatics')
make_head(_module, 'ISystemFunctionButtonEventArgs')
make_head(_module, 'ISystemFunctionLockChangedEventArgs')
make_head(_module, 'ISystemFunctionLockIndicatorChangedEventArgs')
make_head(_module, 'ITappedEventArgs')
make_head(_module, 'ITappedEventArgs2')
make_head(_module, 'InputActivationListener')
make_head(_module, 'InputActivationListenerActivationChangedEventArgs')
make_head(_module, 'KeyboardDeliveryInterceptor')
make_head(_module, 'ManipulationCompletedEventArgs')
make_head(_module, 'ManipulationDelta')
make_head(_module, 'ManipulationInertiaStartingEventArgs')
make_head(_module, 'ManipulationStartedEventArgs')
make_head(_module, 'ManipulationUpdatedEventArgs')
make_head(_module, 'ManipulationVelocities')
make_head(_module, 'MouseWheelParameters')
make_head(_module, 'PointerPoint')
make_head(_module, 'PointerPointProperties')
make_head(_module, 'PointerVisualizationSettings')
make_head(_module, 'RadialController')
make_head(_module, 'RadialControllerButtonClickedEventArgs')
make_head(_module, 'RadialControllerButtonHoldingEventArgs')
make_head(_module, 'RadialControllerButtonPressedEventArgs')
make_head(_module, 'RadialControllerButtonReleasedEventArgs')
make_head(_module, 'RadialControllerConfiguration')
make_head(_module, 'RadialControllerControlAcquiredEventArgs')
make_head(_module, 'RadialControllerMenu')
make_head(_module, 'RadialControllerMenuItem')
make_head(_module, 'RadialControllerRotationChangedEventArgs')
make_head(_module, 'RadialControllerScreenContact')
make_head(_module, 'RadialControllerScreenContactContinuedEventArgs')
make_head(_module, 'RadialControllerScreenContactEndedEventArgs')
make_head(_module, 'RadialControllerScreenContactStartedEventArgs')
make_head(_module, 'RightTappedEventArgs')
make_head(_module, 'SystemButtonEventController')
make_head(_module, 'SystemFunctionButtonEventArgs')
make_head(_module, 'SystemFunctionLockChangedEventArgs')
make_head(_module, 'SystemFunctionLockIndicatorChangedEventArgs')
make_head(_module, 'TappedEventArgs')
