from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Haptics
import win32more.Windows.Devices.Input
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input
import win32more.Windows.Win32.System.WinRT
class AttachableInputObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Input.IAttachableInputObject
    _classid_ = 'Windows.UI.Input.AttachableInputObject'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class CrossSlideThresholds(Structure):
    SelectionStart: Single
    SpeedBumpStart: Single
    SpeedBumpEnd: Single
    RearrangeStart: Single
class CrossSlidingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.ICrossSlidingEventArgs
    _classid_ = 'Windows.UI.Input.CrossSlidingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.ICrossSlidingEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.ICrossSlidingEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_CrossSlidingState(self: win32more.Windows.UI.Input.ICrossSlidingEventArgs) -> win32more.Windows.UI.Input.CrossSlidingState: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.ICrossSlidingEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CrossSlidingState = property(get_CrossSlidingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class CrossSlidingState(Enum, Int32):
    Started = 0
    Dragging = 1
    Selecting = 2
    SelectSpeedBumping = 3
    SpeedBumping = 4
    Rearranging = 5
    Completed = 6
class DraggingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IDraggingEventArgs
    _classid_ = 'Windows.UI.Input.DraggingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.IDraggingEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IDraggingEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_DraggingState(self: win32more.Windows.UI.Input.IDraggingEventArgs) -> win32more.Windows.UI.Input.DraggingState: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.IDraggingEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    DraggingState = property(get_DraggingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class DraggingState(Enum, Int32):
    Started = 0
    Continuing = 1
    Completed = 2
class EdgeGesture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IEdgeGesture
    _classid_ = 'Windows.UI.Input.EdgeGesture'
    @winrt_mixinmethod
    def add_Starting(self: win32more.Windows.UI.Input.IEdgeGesture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.EdgeGesture, win32more.Windows.UI.Input.EdgeGestureEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Starting(self: win32more.Windows.UI.Input.IEdgeGesture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.UI.Input.IEdgeGesture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.EdgeGesture, win32more.Windows.UI.Input.EdgeGestureEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.UI.Input.IEdgeGesture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Canceled(self: win32more.Windows.UI.Input.IEdgeGesture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.EdgeGesture, win32more.Windows.UI.Input.EdgeGestureEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: win32more.Windows.UI.Input.IEdgeGesture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Input.IEdgeGestureStatics) -> win32more.Windows.UI.Input.EdgeGesture: ...
    Starting = event()
    Completed = event()
    Canceled = event()
class EdgeGestureEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IEdgeGestureEventArgs
    _classid_ = 'Windows.UI.Input.EdgeGestureEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.IEdgeGestureEventArgs) -> win32more.Windows.UI.Input.EdgeGestureKind: ...
    Kind = property(get_Kind, None)
class EdgeGestureKind(Enum, Int32):
    Touch = 0
    Keyboard = 1
    Mouse = 2
class GazeInputAccessStatus(Enum, Int32):
    Unspecified = 0
    Allowed = 1
    DeniedByUser = 2
    DeniedBySystem = 3
class GestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IGestureRecognizer
    _classid_ = 'Windows.UI.Input.GestureRecognizer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.GestureRecognizer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.GestureRecognizer: ...
    @winrt_mixinmethod
    def get_GestureSettings(self: win32more.Windows.UI.Input.IGestureRecognizer) -> win32more.Windows.UI.Input.GestureSettings: ...
    @winrt_mixinmethod
    def put_GestureSettings(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.UI.Input.GestureSettings) -> Void: ...
    @winrt_mixinmethod
    def get_IsInertial(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShowGestureFeedback(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowGestureFeedback(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PivotCenter(self: win32more.Windows.UI.Input.IGestureRecognizer) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PivotCenter(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_PivotRadius(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_PivotRadius(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaTranslationDeceleration(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaTranslationDeceleration(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaRotationDeceleration(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaRotationDeceleration(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaExpansionDeceleration(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaExpansionDeceleration(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaTranslationDisplacement(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaTranslationDisplacement(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaRotationAngle(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaRotationAngle(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaExpansion(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaExpansion(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ManipulationExact(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_ManipulationExact(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideThresholds(self: win32more.Windows.UI.Input.IGestureRecognizer) -> win32more.Windows.UI.Input.CrossSlideThresholds: ...
    @winrt_mixinmethod
    def put_CrossSlideThresholds(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.UI.Input.CrossSlideThresholds) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideHorizontally(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_CrossSlideHorizontally(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideExact(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_CrossSlideExact(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutoProcessInertia(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoProcessInertia(self: win32more.Windows.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MouseWheelParameters(self: win32more.Windows.UI.Input.IGestureRecognizer) -> win32more.Windows.UI.Input.MouseWheelParameters: ...
    @winrt_mixinmethod
    def CanBeDoubleTap(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.UI.Input.PointerPoint) -> Boolean: ...
    @winrt_mixinmethod
    def ProcessDownEvent(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessMoveEvents(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]) -> Void: ...
    @winrt_mixinmethod
    def ProcessUpEvent(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessMouseWheelEvent(self: win32more.Windows.UI.Input.IGestureRecognizer, value: win32more.Windows.UI.Input.PointerPoint, isShiftKeyDown: Boolean, isControlKeyDown: Boolean) -> Void: ...
    @winrt_mixinmethod
    def ProcessInertia(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def CompleteGesture(self: win32more.Windows.UI.Input.IGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.TappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RightTapped(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.RightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RightTapped(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Holding(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.HoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Holding(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Dragging(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.DraggingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dragging(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationUpdated(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationUpdated(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationInertiaStarting(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationInertiaStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationInertiaStarting(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CrossSliding(self: win32more.Windows.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.CrossSlidingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CrossSliding(self: win32more.Windows.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_TapMinContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TapMinContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TapMaxContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TapMaxContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldMinContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_HoldMinContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldMaxContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_HoldMaxContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldRadius(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> Single: ...
    @winrt_mixinmethod
    def put_HoldRadius(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_HoldStartDelay(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_HoldStartDelay(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationMinContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TranslationMinContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationMaxContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2) -> UInt32: ...
    @winrt_mixinmethod
    def put_TranslationMaxContactCount(self: win32more.Windows.UI.Input.IGestureRecognizer2, value: UInt32) -> Void: ...
    AutoProcessInertia = property(get_AutoProcessInertia, put_AutoProcessInertia)
    CrossSlideExact = property(get_CrossSlideExact, put_CrossSlideExact)
    CrossSlideHorizontally = property(get_CrossSlideHorizontally, put_CrossSlideHorizontally)
    CrossSlideThresholds = property(get_CrossSlideThresholds, put_CrossSlideThresholds)
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    HoldMaxContactCount = property(get_HoldMaxContactCount, put_HoldMaxContactCount)
    HoldMinContactCount = property(get_HoldMinContactCount, put_HoldMinContactCount)
    HoldRadius = property(get_HoldRadius, put_HoldRadius)
    HoldStartDelay = property(get_HoldStartDelay, put_HoldStartDelay)
    InertiaExpansion = property(get_InertiaExpansion, put_InertiaExpansion)
    InertiaExpansionDeceleration = property(get_InertiaExpansionDeceleration, put_InertiaExpansionDeceleration)
    InertiaRotationAngle = property(get_InertiaRotationAngle, put_InertiaRotationAngle)
    InertiaRotationDeceleration = property(get_InertiaRotationDeceleration, put_InertiaRotationDeceleration)
    InertiaTranslationDeceleration = property(get_InertiaTranslationDeceleration, put_InertiaTranslationDeceleration)
    InertiaTranslationDisplacement = property(get_InertiaTranslationDisplacement, put_InertiaTranslationDisplacement)
    IsActive = property(get_IsActive, None)
    IsInertial = property(get_IsInertial, None)
    ManipulationExact = property(get_ManipulationExact, put_ManipulationExact)
    MouseWheelParameters = property(get_MouseWheelParameters, None)
    PivotCenter = property(get_PivotCenter, put_PivotCenter)
    PivotRadius = property(get_PivotRadius, put_PivotRadius)
    ShowGestureFeedback = property(get_ShowGestureFeedback, put_ShowGestureFeedback)
    TapMaxContactCount = property(get_TapMaxContactCount, put_TapMaxContactCount)
    TapMinContactCount = property(get_TapMinContactCount, put_TapMinContactCount)
    TranslationMaxContactCount = property(get_TranslationMaxContactCount, put_TranslationMaxContactCount)
    TranslationMinContactCount = property(get_TranslationMinContactCount, put_TranslationMinContactCount)
    Tapped = event()
    RightTapped = event()
    Holding = event()
    Dragging = event()
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationInertiaStarting = event()
    ManipulationCompleted = event()
    CrossSliding = event()
class GestureSettings(Enum, UInt32):
    None_ = 0
    Tap = 1
    DoubleTap = 2
    Hold = 4
    HoldWithMouse = 8
    RightTap = 16
    Drag = 32
    ManipulationTranslateX = 64
    ManipulationTranslateY = 128
    ManipulationTranslateRailsX = 256
    ManipulationTranslateRailsY = 512
    ManipulationRotate = 1024
    ManipulationScale = 2048
    ManipulationTranslateInertia = 4096
    ManipulationRotateInertia = 8192
    ManipulationScaleInertia = 16384
    CrossSlide = 32768
    ManipulationMultipleFingerPanning = 65536
class HoldingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IHoldingEventArgs
    _classid_ = 'Windows.UI.Input.HoldingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.IHoldingEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IHoldingEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_HoldingState(self: win32more.Windows.UI.Input.IHoldingEventArgs) -> win32more.Windows.UI.Input.HoldingState: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.IHoldingEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentContactCount(self: win32more.Windows.UI.Input.IHoldingEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class HoldingState(Enum, Int32):
    Started = 0
    Completed = 1
    Canceled = 2
class IAttachableInputObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IAttachableInputObject'
    _iid_ = Guid('{9b822734-a3c1-542a-b2f4-0e32b773fb07}')
class IAttachableInputObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IAttachableInputObjectFactory'
    _iid_ = Guid('{a4c54c4e-42bc-58fa-a640-ea1516f4c06b}')
class ICrossSlidingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ICrossSlidingEventArgs'
    _iid_ = Guid('{e9374738-6f88-41d9-8720-78e08e398349}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_CrossSlidingState(self) -> win32more.Windows.UI.Input.CrossSlidingState: ...
    CrossSlidingState = property(get_CrossSlidingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class ICrossSlidingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ICrossSlidingEventArgs2'
    _iid_ = Guid('{eefb7d48-c070-59f3-8dab-bcaf621d8687}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IDraggingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IDraggingEventArgs'
    _iid_ = Guid('{1c905384-083c-4bd3-b559-179cddeb33ec}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_DraggingState(self) -> win32more.Windows.UI.Input.DraggingState: ...
    DraggingState = property(get_DraggingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IDraggingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IDraggingEventArgs2'
    _iid_ = Guid('{71efdbf9-382a-55ca-b4b9-008123c1bf1a}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IEdgeGesture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IEdgeGesture'
    _iid_ = Guid('{580d5292-2ab1-49aa-a7f0-33bd3f8df9f1}')
    @winrt_commethod(6)
    def add_Starting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.EdgeGesture, win32more.Windows.UI.Input.EdgeGestureEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Starting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Completed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.EdgeGesture, win32more.Windows.UI.Input.EdgeGestureEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Completed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Canceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.EdgeGesture, win32more.Windows.UI.Input.EdgeGestureEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Canceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Starting = event()
    Completed = event()
    Canceled = event()
class IEdgeGestureEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IEdgeGestureEventArgs'
    _iid_ = Guid('{44fa4a24-2d09-42e1-8b5e-368208796a4c}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.UI.Input.EdgeGestureKind: ...
    Kind = property(get_Kind, None)
class IEdgeGestureStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IEdgeGestureStatics'
    _iid_ = Guid('{bc6a8519-18ee-4043-9839-4fc584d60a14}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Input.EdgeGesture: ...
class IGestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IGestureRecognizer'
    _iid_ = Guid('{b47a37bf-3d6b-4f88-83e8-6dcb4012ffb0}')
    @winrt_commethod(6)
    def get_GestureSettings(self) -> win32more.Windows.UI.Input.GestureSettings: ...
    @winrt_commethod(7)
    def put_GestureSettings(self, value: win32more.Windows.UI.Input.GestureSettings) -> Void: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ShowGestureFeedback(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_ShowGestureFeedback(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_PivotCenter(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def put_PivotCenter(self, value: win32more.Windows.Foundation.Point) -> Void: ...
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
    def get_CrossSlideThresholds(self) -> win32more.Windows.UI.Input.CrossSlideThresholds: ...
    @winrt_commethod(31)
    def put_CrossSlideThresholds(self, value: win32more.Windows.UI.Input.CrossSlideThresholds) -> Void: ...
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
    def get_MouseWheelParameters(self) -> win32more.Windows.UI.Input.MouseWheelParameters: ...
    @winrt_commethod(39)
    def CanBeDoubleTap(self, value: win32more.Windows.UI.Input.PointerPoint) -> Boolean: ...
    @winrt_commethod(40)
    def ProcessDownEvent(self, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(41)
    def ProcessMoveEvents(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]) -> Void: ...
    @winrt_commethod(42)
    def ProcessUpEvent(self, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(43)
    def ProcessMouseWheelEvent(self, value: win32more.Windows.UI.Input.PointerPoint, isShiftKeyDown: Boolean, isControlKeyDown: Boolean) -> Void: ...
    @winrt_commethod(44)
    def ProcessInertia(self) -> Void: ...
    @winrt_commethod(45)
    def CompleteGesture(self) -> Void: ...
    @winrt_commethod(46)
    def add_Tapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.TappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(47)
    def remove_Tapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(48)
    def add_RightTapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.RightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(49)
    def remove_RightTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(50)
    def add_Holding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.HoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(51)
    def remove_Holding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(52)
    def add_Dragging(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.DraggingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(53)
    def remove_Dragging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(54)
    def add_ManipulationStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(55)
    def remove_ManipulationStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(56)
    def add_ManipulationUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(57)
    def remove_ManipulationUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(58)
    def add_ManipulationInertiaStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationInertiaStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(59)
    def remove_ManipulationInertiaStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(60)
    def add_ManipulationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.ManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(61)
    def remove_ManipulationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(62)
    def add_CrossSliding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.GestureRecognizer, win32more.Windows.UI.Input.CrossSlidingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(63)
    def remove_CrossSliding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoProcessInertia = property(get_AutoProcessInertia, put_AutoProcessInertia)
    CrossSlideExact = property(get_CrossSlideExact, put_CrossSlideExact)
    CrossSlideHorizontally = property(get_CrossSlideHorizontally, put_CrossSlideHorizontally)
    CrossSlideThresholds = property(get_CrossSlideThresholds, put_CrossSlideThresholds)
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    InertiaExpansion = property(get_InertiaExpansion, put_InertiaExpansion)
    InertiaExpansionDeceleration = property(get_InertiaExpansionDeceleration, put_InertiaExpansionDeceleration)
    InertiaRotationAngle = property(get_InertiaRotationAngle, put_InertiaRotationAngle)
    InertiaRotationDeceleration = property(get_InertiaRotationDeceleration, put_InertiaRotationDeceleration)
    InertiaTranslationDeceleration = property(get_InertiaTranslationDeceleration, put_InertiaTranslationDeceleration)
    InertiaTranslationDisplacement = property(get_InertiaTranslationDisplacement, put_InertiaTranslationDisplacement)
    IsActive = property(get_IsActive, None)
    IsInertial = property(get_IsInertial, None)
    ManipulationExact = property(get_ManipulationExact, put_ManipulationExact)
    MouseWheelParameters = property(get_MouseWheelParameters, None)
    PivotCenter = property(get_PivotCenter, put_PivotCenter)
    PivotRadius = property(get_PivotRadius, put_PivotRadius)
    ShowGestureFeedback = property(get_ShowGestureFeedback, put_ShowGestureFeedback)
    Tapped = event()
    RightTapped = event()
    Holding = event()
    Dragging = event()
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationInertiaStarting = event()
    ManipulationCompleted = event()
    CrossSliding = event()
class IGestureRecognizer2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IGestureRecognizer2'
    _iid_ = Guid('{d646097f-6ef7-5746-8ba8-8ff2206e6f3b}')
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
    def get_HoldStartDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def put_HoldStartDelay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(18)
    def get_TranslationMinContactCount(self) -> UInt32: ...
    @winrt_commethod(19)
    def put_TranslationMinContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(20)
    def get_TranslationMaxContactCount(self) -> UInt32: ...
    @winrt_commethod(21)
    def put_TranslationMaxContactCount(self, value: UInt32) -> Void: ...
    HoldMaxContactCount = property(get_HoldMaxContactCount, put_HoldMaxContactCount)
    HoldMinContactCount = property(get_HoldMinContactCount, put_HoldMinContactCount)
    HoldRadius = property(get_HoldRadius, put_HoldRadius)
    HoldStartDelay = property(get_HoldStartDelay, put_HoldStartDelay)
    TapMaxContactCount = property(get_TapMaxContactCount, put_TapMaxContactCount)
    TapMinContactCount = property(get_TapMinContactCount, put_TapMinContactCount)
    TranslationMaxContactCount = property(get_TranslationMaxContactCount, put_TranslationMaxContactCount)
    TranslationMinContactCount = property(get_TranslationMinContactCount, put_TranslationMinContactCount)
class IHoldingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IHoldingEventArgs'
    _iid_ = Guid('{2bf755c5-e799-41b4-bb40-242f40959b71}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_HoldingState(self) -> win32more.Windows.UI.Input.HoldingState: ...
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IHoldingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IHoldingEventArgs2'
    _iid_ = Guid('{141da9ea-4c79-5674-afea-493fdeb91f19}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CurrentContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class IInputActivationListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IInputActivationListener'
    _iid_ = Guid('{5d6d4ed2-28c7-5ae3-aa74-c918a9f243ca}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.UI.Input.InputActivationState: ...
    @winrt_commethod(7)
    def add_InputActivationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.InputActivationListener, win32more.Windows.UI.Input.InputActivationListenerActivationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_InputActivationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
    InputActivationChanged = event()
class IInputActivationListenerActivationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IInputActivationListenerActivationChangedEventArgs'
    _iid_ = Guid('{7699b465-1dcf-5791-b4b9-6cafbeed2056}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.UI.Input.InputActivationState: ...
    State = property(get_State, None)
class IKeyboardDeliveryInterceptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IKeyboardDeliveryInterceptor'
    _iid_ = Guid('{b4baf068-8f49-446c-8db5-8c0ffe85cc9e}')
    @winrt_commethod(6)
    def get_IsInterceptionEnabledWhenInForeground(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsInterceptionEnabledWhenInForeground(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def add_KeyDown(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.KeyboardDeliveryInterceptor, win32more.Windows.UI.Core.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_KeyDown(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_KeyUp(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.KeyboardDeliveryInterceptor, win32more.Windows.UI.Core.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_KeyUp(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsInterceptionEnabledWhenInForeground = property(get_IsInterceptionEnabledWhenInForeground, put_IsInterceptionEnabledWhenInForeground)
    KeyDown = event()
    KeyUp = event()
class IKeyboardDeliveryInterceptorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IKeyboardDeliveryInterceptorStatics'
    _iid_ = Guid('{f9f63ba2-ceba-4755-8a7e-14c0ffecd239}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Input.KeyboardDeliveryInterceptor: ...
class IManipulationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationCompletedEventArgs'
    _iid_ = Guid('{b34ab22b-d19b-46ff-9f38-dec7754bb9e7}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(9)
    def get_Velocities(self) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class IManipulationCompletedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationCompletedEventArgs2'
    _iid_ = Guid('{f0c0dce7-30a9-5b96-886f-6560a85e4757}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CurrentContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class IManipulationInertiaStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationInertiaStartingEventArgs'
    _iid_ = Guid('{dd37a898-26bf-467a-9ce5-ccf3fb11371e}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Delta(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(9)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class IManipulationInertiaStartingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationInertiaStartingEventArgs2'
    _iid_ = Guid('{c25409b8-f9fa-5a45-bd97-dcbbb2201860}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IManipulationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationStartedEventArgs'
    _iid_ = Guid('{ddec873e-cfce-4932-8c1d-3c3d011a34c0}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    Cumulative = property(get_Cumulative, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IManipulationStartedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationStartedEventArgs2'
    _iid_ = Guid('{2da3db4e-e583-5055-afaa-16fd986531a6}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class IManipulationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationUpdatedEventArgs'
    _iid_ = Guid('{cb354ce5-abb8-4f9f-b3ce-8181aa61ad82}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Delta(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(9)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class IManipulationUpdatedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IManipulationUpdatedEventArgs2'
    _iid_ = Guid('{f3dfb96a-3306-5903-a1c5-ff9757a8689e}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CurrentContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
class IMouseWheelParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IMouseWheelParameters'
    _iid_ = Guid('{ead0ca44-9ded-4037-8149-5e4cc2564468}')
    @winrt_commethod(6)
    def get_CharTranslation(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_CharTranslation(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_DeltaScale(self) -> Single: ...
    @winrt_commethod(9)
    def put_DeltaScale(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_DeltaRotationAngle(self) -> Single: ...
    @winrt_commethod(11)
    def put_DeltaRotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_PageTranslation(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def put_PageTranslation(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    CharTranslation = property(get_CharTranslation, put_CharTranslation)
    DeltaRotationAngle = property(get_DeltaRotationAngle, put_DeltaRotationAngle)
    DeltaScale = property(get_DeltaScale, put_DeltaScale)
    PageTranslation = property(get_PageTranslation, put_PageTranslation)
class IPhysicalGestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPhysicalGestureRecognizer'
    _iid_ = Guid('{a3bb83e5-6937-5f29-8707-ae4875f8fda3}')
    @winrt_commethod(6)
    def get_GestureSettings(self) -> win32more.Windows.UI.Input.GestureSettings: ...
    @winrt_commethod(7)
    def put_GestureSettings(self, value: win32more.Windows.UI.Input.GestureSettings) -> Void: ...
    @winrt_commethod(8)
    def get_TapMinContactCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_TapMinContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_TapMaxContactCount(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_TapMaxContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_HoldMinContactCount(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_HoldMinContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_HoldMaxContactCount(self) -> UInt32: ...
    @winrt_commethod(15)
    def put_HoldMaxContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(16)
    def get_HoldRadius(self) -> Single: ...
    @winrt_commethod(17)
    def put_HoldRadius(self, value: Single) -> Void: ...
    @winrt_commethod(18)
    def get_HoldStartDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(19)
    def put_HoldStartDelay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(20)
    def get_TranslationMinContactCount(self) -> UInt32: ...
    @winrt_commethod(21)
    def put_TranslationMinContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(22)
    def get_TranslationMaxContactCount(self) -> UInt32: ...
    @winrt_commethod(23)
    def put_TranslationMaxContactCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(24)
    def ProcessDownEvent(self, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(25)
    def ProcessMoveEvents(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]) -> Void: ...
    @winrt_commethod(26)
    def ProcessUpEvent(self, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(27)
    def CompleteGesture(self) -> Void: ...
    @winrt_commethod(28)
    def add_ManipulationStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.ManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_ManipulationStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_ManipulationUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.ManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_ManipulationUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_ManipulationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.ManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_ManipulationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_Tapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.TappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_Tapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def add_Holding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.HoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(37)
    def remove_Holding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    HoldMaxContactCount = property(get_HoldMaxContactCount, put_HoldMaxContactCount)
    HoldMinContactCount = property(get_HoldMinContactCount, put_HoldMinContactCount)
    HoldRadius = property(get_HoldRadius, put_HoldRadius)
    HoldStartDelay = property(get_HoldStartDelay, put_HoldStartDelay)
    TapMaxContactCount = property(get_TapMaxContactCount, put_TapMaxContactCount)
    TapMinContactCount = property(get_TapMinContactCount, put_TapMinContactCount)
    TranslationMaxContactCount = property(get_TranslationMaxContactCount, put_TranslationMaxContactCount)
    TranslationMinContactCount = property(get_TranslationMinContactCount, put_TranslationMinContactCount)
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationCompleted = event()
    Tapped = event()
    Holding = event()
class IPointerPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerPoint'
    _iid_ = Guid('{e995317d-7296-42d9-8233-c5be73b74a4a}')
    @winrt_commethod(6)
    def get_PointerDevice(self) -> win32more.Windows.Devices.Input.PointerDevice: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_RawPosition(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_FrameId(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(12)
    def get_IsInContact(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_Properties(self) -> win32more.Windows.UI.Input.PointerPointProperties: ...
    FrameId = property(get_FrameId, None)
    IsInContact = property(get_IsInContact, None)
    PointerDevice = property(get_PointerDevice, None)
    PointerId = property(get_PointerId, None)
    Position = property(get_Position, None)
    Properties = property(get_Properties, None)
    RawPosition = property(get_RawPosition, None)
    Timestamp = property(get_Timestamp, None)
class IPointerPointPhysicalPosition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerPointPhysicalPosition'
    _iid_ = Guid('{003185a3-a5e7-4859-9c0b-89340204806c}')
    @winrt_commethod(6)
    def get_IsPhysicalPositionSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_PhysicalPosition(self) -> win32more.Windows.Foundation.Point: ...
    IsPhysicalPositionSupported = property(get_IsPhysicalPositionSupported, None)
    PhysicalPosition = property(get_PhysicalPosition, None)
class IPointerPointProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerPointProperties'
    _iid_ = Guid('{c79d8a4b-c163-4ee7-803f-67ce79f9972d}')
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
    def get_ContactRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(14)
    def get_ContactRectRaw(self) -> win32more.Windows.Foundation.Rect: ...
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
    def get_PointerUpdateKind(self) -> win32more.Windows.UI.Input.PointerUpdateKind: ...
    @winrt_commethod(28)
    def HasUsage(self, usagePage: UInt32, usageId: UInt32) -> Boolean: ...
    @winrt_commethod(29)
    def GetUsageValue(self, usagePage: UInt32, usageId: UInt32) -> Int32: ...
    ContactRect = property(get_ContactRect, None)
    ContactRectRaw = property(get_ContactRectRaw, None)
    IsBarrelButtonPressed = property(get_IsBarrelButtonPressed, None)
    IsCanceled = property(get_IsCanceled, None)
    IsEraser = property(get_IsEraser, None)
    IsHorizontalMouseWheel = property(get_IsHorizontalMouseWheel, None)
    IsInRange = property(get_IsInRange, None)
    IsInverted = property(get_IsInverted, None)
    IsLeftButtonPressed = property(get_IsLeftButtonPressed, None)
    IsMiddleButtonPressed = property(get_IsMiddleButtonPressed, None)
    IsPrimary = property(get_IsPrimary, None)
    IsRightButtonPressed = property(get_IsRightButtonPressed, None)
    IsXButton1Pressed = property(get_IsXButton1Pressed, None)
    IsXButton2Pressed = property(get_IsXButton2Pressed, None)
    MouseWheelDelta = property(get_MouseWheelDelta, None)
    Orientation = property(get_Orientation, None)
    PointerUpdateKind = property(get_PointerUpdateKind, None)
    Pressure = property(get_Pressure, None)
    TouchConfidence = property(get_TouchConfidence, None)
    Twist = property(get_Twist, None)
    XTilt = property(get_XTilt, None)
    YTilt = property(get_YTilt, None)
class IPointerPointProperties2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerPointProperties2'
    _iid_ = Guid('{22c3433a-c83b-41c0-a296-5e232d64d6af}')
    @winrt_commethod(6)
    def get_ZDistance(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    ZDistance = property(get_ZDistance, None)
class IPointerPointStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerPointStatics'
    _iid_ = Guid('{a506638d-2a1a-413e-bc75-9f38381cc069}')
    @winrt_commethod(6)
    def GetCurrentPoint(self, pointerId: UInt32) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(7)
    def GetIntermediatePoints(self, pointerId: UInt32) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]: ...
    @winrt_commethod(8)
    def GetCurrentPointTransformed(self, pointerId: UInt32, transform: win32more.Windows.UI.Input.IPointerPointTransform) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(9)
    def GetIntermediatePointsTransformed(self, pointerId: UInt32, transform: win32more.Windows.UI.Input.IPointerPointTransform) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]: ...
class IPointerPointTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerPointTransform'
    _iid_ = Guid('{4d5fe14f-b87c-4028-bc9c-59e9947fb056}')
    @winrt_commethod(6)
    def get_Inverse(self) -> win32more.Windows.UI.Input.IPointerPointTransform: ...
    @winrt_commethod(7)
    def TryTransform(self, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_commethod(8)
    def TransformBounds(self, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
class IPointerVisualizationSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerVisualizationSettings'
    _iid_ = Guid('{4d1e6461-84f7-499d-bd91-2a36e2b7aaa2}')
    @winrt_commethod(6)
    def put_IsContactFeedbackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsContactFeedbackEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsBarrelButtonFeedbackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsBarrelButtonFeedbackEnabled(self) -> Boolean: ...
    IsBarrelButtonFeedbackEnabled = property(get_IsBarrelButtonFeedbackEnabled, put_IsBarrelButtonFeedbackEnabled)
    IsContactFeedbackEnabled = property(get_IsContactFeedbackEnabled, put_IsContactFeedbackEnabled)
class IPointerVisualizationSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IPointerVisualizationSettingsStatics'
    _iid_ = Guid('{68870edb-165b-4214-b4f3-584eca8c8a69}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Input.PointerVisualizationSettings: ...
class IRadialController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialController'
    _iid_ = Guid('{3055d1c8-df51-43d4-b23b-0e1037467a09}')
    @winrt_commethod(6)
    def get_Menu(self) -> win32more.Windows.UI.Input.RadialControllerMenu: ...
    @winrt_commethod(7)
    def get_RotationResolutionInDegrees(self) -> Double: ...
    @winrt_commethod(8)
    def put_RotationResolutionInDegrees(self, value: Double) -> Void: ...
    @winrt_commethod(9)
    def get_UseAutomaticHapticFeedback(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_UseAutomaticHapticFeedback(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def add_ScreenContactStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerScreenContactStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ScreenContactStarted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_ScreenContactEnded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_ScreenContactEnded(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_ScreenContactContinued(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerScreenContactContinuedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ScreenContactContinued(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_ControlLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ControlLost(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_RotationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerRotationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_RotationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_ButtonClicked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_ButtonClicked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_ControlAcquired(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerControlAcquiredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_ControlAcquired(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Menu = property(get_Menu, None)
    RotationResolutionInDegrees = property(get_RotationResolutionInDegrees, put_RotationResolutionInDegrees)
    UseAutomaticHapticFeedback = property(get_UseAutomaticHapticFeedback, put_UseAutomaticHapticFeedback)
    ScreenContactStarted = event()
    ScreenContactEnded = event()
    ScreenContactContinued = event()
    ControlLost = event()
    RotationChanged = event()
    ButtonClicked = event()
    ControlAcquired = event()
class IRadialController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialController2'
    _iid_ = Guid('{3d577eff-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def add_ButtonPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ButtonPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ButtonHolding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonHoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ButtonHolding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ButtonReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonReleasedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ButtonReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ButtonPressed = event()
    ButtonHolding = event()
    ButtonReleased = event()
class IRadialControllerButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerButtonClickedEventArgs'
    _iid_ = Guid('{206aa438-e651-11e5-bf62-2c27d7404e85}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerButtonClickedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerButtonClickedEventArgs2'
    _iid_ = Guid('{3d577ef3-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerButtonHoldingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerButtonHoldingEventArgs'
    _iid_ = Guid('{3d577eee-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerButtonPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerButtonPressedEventArgs'
    _iid_ = Guid('{3d577eed-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerButtonReleasedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerButtonReleasedEventArgs'
    _iid_ = Guid('{3d577eef-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerConfiguration'
    _iid_ = Guid('{a6b79ecb-6a52-4430-910c-56370a9d6b42}')
    @winrt_commethod(6)
    def SetDefaultMenuItems(self, buttons: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.RadialControllerSystemMenuItemKind]) -> Void: ...
    @winrt_commethod(7)
    def ResetToDefaultMenuItems(self) -> Void: ...
    @winrt_commethod(8)
    def TrySelectDefaultMenuItem(self, type: win32more.Windows.UI.Input.RadialControllerSystemMenuItemKind) -> Boolean: ...
class IRadialControllerConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerConfiguration2'
    _iid_ = Guid('{3d577ef7-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def put_ActiveControllerWhenMenuIsSuppressed(self, value: win32more.Windows.UI.Input.RadialController) -> Void: ...
    @winrt_commethod(7)
    def get_ActiveControllerWhenMenuIsSuppressed(self) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_commethod(8)
    def put_IsMenuSuppressed(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsMenuSuppressed(self) -> Boolean: ...
    ActiveControllerWhenMenuIsSuppressed = property(get_ActiveControllerWhenMenuIsSuppressed, put_ActiveControllerWhenMenuIsSuppressed)
    IsMenuSuppressed = property(get_IsMenuSuppressed, put_IsMenuSuppressed)
class IRadialControllerConfigurationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerConfigurationStatics'
    _iid_ = Guid('{79b6b0e5-069a-4486-a99d-8db772b9642f}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Input.RadialControllerConfiguration: ...
class IRadialControllerConfigurationStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerConfigurationStatics2'
    _iid_ = Guid('{53e08b17-e205-48d3-9caf-80ff47c4d7c7}')
    @winrt_commethod(6)
    def put_AppController(self, value: win32more.Windows.UI.Input.RadialController) -> Void: ...
    @winrt_commethod(7)
    def get_AppController(self) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_commethod(8)
    def put_IsAppControllerEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsAppControllerEnabled(self) -> Boolean: ...
    AppController = property(get_AppController, put_AppController)
    IsAppControllerEnabled = property(get_IsAppControllerEnabled, put_IsAppControllerEnabled)
class IRadialControllerControlAcquiredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerControlAcquiredEventArgs'
    _iid_ = Guid('{206aa439-e651-11e5-bf62-2c27d7404e85}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerControlAcquiredEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerControlAcquiredEventArgs2'
    _iid_ = Guid('{3d577ef4-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerMenu(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerMenu'
    _iid_ = Guid('{8506b35d-f640-4412-aba0-bad077e5ea8a}')
    @winrt_commethod(6)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.RadialControllerMenuItem]: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetSelectedMenuItem(self) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_commethod(10)
    def SelectMenuItem(self, menuItem: win32more.Windows.UI.Input.RadialControllerMenuItem) -> Void: ...
    @winrt_commethod(11)
    def TrySelectPreviouslySelectedMenuItem(self) -> Boolean: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Items = property(get_Items, None)
class IRadialControllerMenuItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerMenuItem'
    _iid_ = Guid('{c80fc98d-ad0b-4c9c-8f2f-136a2373a6ba}')
    @winrt_commethod(6)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Tag(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def put_Tag(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(9)
    def add_Invoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialControllerMenuItem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Invoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DisplayText = property(get_DisplayText, None)
    Tag = property(get_Tag, put_Tag)
    Invoked = event()
class IRadialControllerMenuItemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerMenuItemStatics'
    _iid_ = Guid('{249e0887-d842-4524-9df8-e0d647edc887}')
    @winrt_commethod(6)
    def CreateFromIcon(self, displayText: WinRT_String, icon: win32more.Windows.Storage.Streams.RandomAccessStreamReference) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_commethod(7)
    def CreateFromKnownIcon(self, displayText: WinRT_String, value: win32more.Windows.UI.Input.RadialControllerMenuKnownIcon) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
class IRadialControllerMenuItemStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerMenuItemStatics2'
    _iid_ = Guid('{0cbb70be-7e3e-48bd-be04-2c7fcaa9c1ff}')
    @winrt_commethod(6)
    def CreateFromFontGlyph(self, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_commethod(7)
    def CreateFromFontGlyphWithUri(self, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String, fontUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
class IRadialControllerRotationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerRotationChangedEventArgs'
    _iid_ = Guid('{206aa435-e651-11e5-bf62-2c27d7404e85}')
    @winrt_commethod(6)
    def get_RotationDeltaInDegrees(self) -> Double: ...
    @winrt_commethod(7)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
    RotationDeltaInDegrees = property(get_RotationDeltaInDegrees, None)
class IRadialControllerRotationChangedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerRotationChangedEventArgs2'
    _iid_ = Guid('{3d577eec-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerScreenContact(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerScreenContact'
    _iid_ = Guid('{206aa434-e651-11e5-bf62-2c27d7404e85}')
    @winrt_commethod(6)
    def get_Bounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    Bounds = property(get_Bounds, None)
    Position = property(get_Position, None)
class IRadialControllerScreenContactContinuedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs'
    _iid_ = Guid('{206aa437-e651-11e5-bf62-2c27d7404e85}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerScreenContactContinuedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs2'
    _iid_ = Guid('{3d577ef1-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerScreenContactEndedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerScreenContactEndedEventArgs'
    _iid_ = Guid('{3d577ef2-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerScreenContactStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs'
    _iid_ = Guid('{206aa436-e651-11e5-bf62-2c27d7404e85}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    Contact = property(get_Contact, None)
class IRadialControllerScreenContactStartedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs2'
    _iid_ = Guid('{3d577ef0-3cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_IsButtonPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IRadialControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRadialControllerStatics'
    _iid_ = Guid('{faded0b7-b84c-4894-87aa-8f25aa5f288b}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def CreateForCurrentView(self) -> win32more.Windows.UI.Input.RadialController: ...
class IRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRightTappedEventArgs'
    _iid_ = Guid('{4cbf40bd-af7a-4a36-9476-b1dce141709a}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IRightTappedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.IRightTappedEventArgs2'
    _iid_ = Guid('{61c7b7bb-9f57-5857-a33c-c58c3dfa959e}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class ISystemButtonEventController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ISystemButtonEventController'
    _iid_ = Guid('{59b893a9-73bc-52b5-ba41-82511b2cb46c}')
    @winrt_commethod(6)
    def add_SystemFunctionButtonPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionButtonEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SystemFunctionButtonPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SystemFunctionButtonReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionButtonEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SystemFunctionButtonReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SystemFunctionLockChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionLockChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SystemFunctionLockChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_SystemFunctionLockIndicatorChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionLockIndicatorChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SystemFunctionLockIndicatorChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SystemFunctionButtonPressed = event()
    SystemFunctionButtonReleased = event()
    SystemFunctionLockChanged = event()
    SystemFunctionLockIndicatorChanged = event()
class ISystemButtonEventControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ISystemButtonEventControllerStatics'
    _iid_ = Guid('{632fb07b-20bd-5e15-af4a-00dbf2064ffa}')
    @winrt_commethod(6)
    def CreateForDispatcherQueue(self, queue: win32more.Windows.System.DispatcherQueue) -> win32more.Windows.UI.Input.SystemButtonEventController: ...
class ISystemFunctionButtonEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ISystemFunctionButtonEventArgs'
    _iid_ = Guid('{4833896f-80d1-5dd6-92a7-62a508ffef5a}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Timestamp = property(get_Timestamp, None)
class ISystemFunctionLockChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ISystemFunctionLockChangedEventArgs'
    _iid_ = Guid('{cd040608-fcf9-585c-beab-f1d2eaf364ab}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_IsLocked(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    IsLocked = property(get_IsLocked, None)
    Timestamp = property(get_Timestamp, None)
class ISystemFunctionLockIndicatorChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs'
    _iid_ = Guid('{b212b94e-7a6f-58ae-b304-bae61d0371b9}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_IsIndicatorOn(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    IsIndicatorOn = property(get_IsIndicatorOn, None)
    Timestamp = property(get_Timestamp, None)
class ITappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ITappedEventArgs'
    _iid_ = Guid('{cfa126e4-253a-4c3c-953b-395c37aed309}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_TapCount(self) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    TapCount = property(get_TapCount, None)
class ITappedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ITappedEventArgs2'
    _iid_ = Guid('{294388f2-177e-51d5-be56-ee0866fa968c}')
    @winrt_commethod(6)
    def get_ContactCount(self) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
class ITouchpadGesturesController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ITouchpadGesturesController'
    _iid_ = Guid('{b58f88d0-58ea-51b5-b5bf-61cc081bf21d}')
    @winrt_commethod(6)
    def get_GesturesEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_GesturesEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SupportedGestures(self) -> win32more.Windows.UI.Input.TouchpadGlobalGestureKinds: ...
    @winrt_commethod(9)
    def put_SupportedGestures(self, value: win32more.Windows.UI.Input.TouchpadGlobalGestureKinds) -> Void: ...
    @winrt_commethod(10)
    def add_PointerPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PointerPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PointerMoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PointerMoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PointerReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PointerReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_TouchpadGlobalActionPerformed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Input.TouchpadGlobalActionEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_TouchpadGlobalActionPerformed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    GesturesEnabled = property(get_GesturesEnabled, put_GesturesEnabled)
    SupportedGestures = property(get_SupportedGestures, put_SupportedGestures)
    PointerPressed = event()
    PointerMoved = event()
    PointerReleased = event()
    TouchpadGlobalActionPerformed = event()
class ITouchpadGesturesControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ITouchpadGesturesControllerStatics'
    _iid_ = Guid('{207ef171-1a73-51cd-a694-8840e09dbafa}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def CreateForProcess(self) -> win32more.Windows.UI.Input.TouchpadGesturesController: ...
class ITouchpadGlobalActionEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.ITouchpadGlobalActionEventArgs'
    _iid_ = Guid('{08103525-dbb6-5f7f-9ffe-98c84bb49591}')
    @winrt_commethod(6)
    def get_Action(self) -> win32more.Windows.UI.Input.TouchpadGlobalAction: ...
    Action = property(get_Action, None)
class InputActivationListener(ComPtr):
    extends: win32more.Windows.UI.Input.AttachableInputObject
    default_interface: win32more.Windows.UI.Input.IInputActivationListener
    _classid_ = 'Windows.UI.Input.InputActivationListener'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.UI.Input.IInputActivationListener) -> win32more.Windows.UI.Input.InputActivationState: ...
    @winrt_mixinmethod
    def add_InputActivationChanged(self: win32more.Windows.UI.Input.IInputActivationListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.InputActivationListener, win32more.Windows.UI.Input.InputActivationListenerActivationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputActivationChanged(self: win32more.Windows.UI.Input.IInputActivationListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
    InputActivationChanged = event()
class InputActivationListenerActivationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IInputActivationListenerActivationChangedEventArgs
    _classid_ = 'Windows.UI.Input.InputActivationListenerActivationChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.UI.Input.IInputActivationListenerActivationChangedEventArgs) -> win32more.Windows.UI.Input.InputActivationState: ...
    State = property(get_State, None)
class InputActivationState(Enum, Int32):
    None_ = 0
    Deactivated = 1
    ActivatedNotForeground = 2
    ActivatedInForeground = 3
class KeyboardDeliveryInterceptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptor
    _classid_ = 'Windows.UI.Input.KeyboardDeliveryInterceptor'
    @winrt_mixinmethod
    def get_IsInterceptionEnabledWhenInForeground(self: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInterceptionEnabledWhenInForeground(self: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_KeyDown(self: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.KeyboardDeliveryInterceptor, win32more.Windows.UI.Core.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyDown(self: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyUp(self: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.KeyboardDeliveryInterceptor, win32more.Windows.UI.Core.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyUp(self: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Input.IKeyboardDeliveryInterceptorStatics) -> win32more.Windows.UI.Input.KeyboardDeliveryInterceptor: ...
    IsInterceptionEnabledWhenInForeground = property(get_IsInterceptionEnabledWhenInForeground, put_IsInterceptionEnabledWhenInForeground)
    KeyDown = event()
    KeyUp = event()
class ManipulationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IManipulationCompletedEventArgs
    _classid_ = 'Windows.UI.Input.ManipulationCompletedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.IManipulationCompletedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IManipulationCompletedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Input.IManipulationCompletedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Windows.UI.Input.IManipulationCompletedEventArgs) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.IManipulationCompletedEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentContactCount(self: win32more.Windows.UI.Input.IManipulationCompletedEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    Cumulative = property(get_Cumulative, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationDelta(Structure):
    Translation: win32more.Windows.Foundation.Point
    Scale: Single
    Rotation: Single
    Expansion: Single
class ManipulationInertiaStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IManipulationInertiaStartingEventArgs
    _classid_ = 'Windows.UI.Input.ManipulationInertiaStartingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Delta(self: win32more.Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Windows.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.IManipulationInertiaStartingEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IManipulationStartedEventArgs
    _classid_ = 'Windows.UI.Input.ManipulationStartedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.IManipulationStartedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IManipulationStartedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Input.IManipulationStartedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.IManipulationStartedEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    Cumulative = property(get_Cumulative, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class ManipulationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs
    _classid_ = 'Windows.UI.Input.ManipulationUpdatedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Delta(self: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def get_CurrentContactCount(self: win32more.Windows.UI.Input.IManipulationUpdatedEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    Cumulative = property(get_Cumulative, None)
    CurrentContactCount = property(get_CurrentContactCount, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationVelocities(Structure):
    Linear: win32more.Windows.Foundation.Point
    Angular: Single
    Expansion: Single
class MouseWheelParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IMouseWheelParameters
    _classid_ = 'Windows.UI.Input.MouseWheelParameters'
    @winrt_mixinmethod
    def get_CharTranslation(self: win32more.Windows.UI.Input.IMouseWheelParameters) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_CharTranslation(self: win32more.Windows.UI.Input.IMouseWheelParameters, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaScale(self: win32more.Windows.UI.Input.IMouseWheelParameters) -> Single: ...
    @winrt_mixinmethod
    def put_DeltaScale(self: win32more.Windows.UI.Input.IMouseWheelParameters, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaRotationAngle(self: win32more.Windows.UI.Input.IMouseWheelParameters) -> Single: ...
    @winrt_mixinmethod
    def put_DeltaRotationAngle(self: win32more.Windows.UI.Input.IMouseWheelParameters, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_PageTranslation(self: win32more.Windows.UI.Input.IMouseWheelParameters) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PageTranslation(self: win32more.Windows.UI.Input.IMouseWheelParameters, value: win32more.Windows.Foundation.Point) -> Void: ...
    CharTranslation = property(get_CharTranslation, put_CharTranslation)
    DeltaRotationAngle = property(get_DeltaRotationAngle, put_DeltaRotationAngle)
    DeltaScale = property(get_DeltaScale, put_DeltaScale)
    PageTranslation = property(get_PageTranslation, put_PageTranslation)
class PhysicalGestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IPhysicalGestureRecognizer
    _classid_ = 'Windows.UI.Input.PhysicalGestureRecognizer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.PhysicalGestureRecognizer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.PhysicalGestureRecognizer: ...
    @winrt_mixinmethod
    def get_GestureSettings(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> win32more.Windows.UI.Input.GestureSettings: ...
    @winrt_mixinmethod
    def put_GestureSettings(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: win32more.Windows.UI.Input.GestureSettings) -> Void: ...
    @winrt_mixinmethod
    def get_TapMinContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> UInt32: ...
    @winrt_mixinmethod
    def put_TapMinContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TapMaxContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> UInt32: ...
    @winrt_mixinmethod
    def put_TapMaxContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldMinContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> UInt32: ...
    @winrt_mixinmethod
    def put_HoldMinContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldMaxContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> UInt32: ...
    @winrt_mixinmethod
    def put_HoldMaxContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HoldRadius(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_HoldRadius(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_HoldStartDelay(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_HoldStartDelay(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationMinContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> UInt32: ...
    @winrt_mixinmethod
    def put_TranslationMinContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationMaxContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> UInt32: ...
    @winrt_mixinmethod
    def put_TranslationMaxContactCount(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def ProcessDownEvent(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessMoveEvents(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]) -> Void: ...
    @winrt_mixinmethod
    def ProcessUpEvent(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, value: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def CompleteGesture(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.ManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationUpdated(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.ManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationUpdated(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.ManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.TappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Holding(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.PhysicalGestureRecognizer, win32more.Windows.UI.Input.HoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Holding(self: win32more.Windows.UI.Input.IPhysicalGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    HoldMaxContactCount = property(get_HoldMaxContactCount, put_HoldMaxContactCount)
    HoldMinContactCount = property(get_HoldMinContactCount, put_HoldMinContactCount)
    HoldRadius = property(get_HoldRadius, put_HoldRadius)
    HoldStartDelay = property(get_HoldStartDelay, put_HoldStartDelay)
    TapMaxContactCount = property(get_TapMaxContactCount, put_TapMaxContactCount)
    TapMinContactCount = property(get_TapMinContactCount, put_TapMinContactCount)
    TranslationMaxContactCount = property(get_TranslationMaxContactCount, put_TranslationMaxContactCount)
    TranslationMinContactCount = property(get_TranslationMinContactCount, put_TranslationMinContactCount)
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationCompleted = event()
    Tapped = event()
    Holding = event()
class PointerPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IPointerPoint
    _classid_ = 'Windows.UI.Input.PointerPoint'
    @winrt_mixinmethod
    def get_PointerDevice(self: win32more.Windows.UI.Input.IPointerPoint) -> win32more.Windows.Devices.Input.PointerDevice: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IPointerPoint) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_RawPosition(self: win32more.Windows.UI.Input.IPointerPoint) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_PointerId(self: win32more.Windows.UI.Input.IPointerPoint) -> UInt32: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Windows.UI.Input.IPointerPoint) -> UInt32: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.UI.Input.IPointerPoint) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsInContact(self: win32more.Windows.UI.Input.IPointerPoint) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.UI.Input.IPointerPoint) -> win32more.Windows.UI.Input.PointerPointProperties: ...
    @winrt_mixinmethod
    def get_IsPhysicalPositionSupported(self: win32more.Windows.UI.Input.IPointerPointPhysicalPosition) -> Boolean: ...
    @winrt_mixinmethod
    def get_PhysicalPosition(self: win32more.Windows.UI.Input.IPointerPointPhysicalPosition) -> win32more.Windows.Foundation.Point: ...
    @winrt_classmethod
    def GetCurrentPoint(cls: win32more.Windows.UI.Input.IPointerPointStatics, pointerId: UInt32) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_classmethod
    def GetIntermediatePoints(cls: win32more.Windows.UI.Input.IPointerPointStatics, pointerId: UInt32) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]: ...
    @winrt_classmethod
    def GetCurrentPointTransformed(cls: win32more.Windows.UI.Input.IPointerPointStatics, pointerId: UInt32, transform: win32more.Windows.UI.Input.IPointerPointTransform) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_classmethod
    def GetIntermediatePointsTransformed(cls: win32more.Windows.UI.Input.IPointerPointStatics, pointerId: UInt32, transform: win32more.Windows.UI.Input.IPointerPointTransform) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]: ...
    FrameId = property(get_FrameId, None)
    IsInContact = property(get_IsInContact, None)
    IsPhysicalPositionSupported = property(get_IsPhysicalPositionSupported, None)
    PhysicalPosition = property(get_PhysicalPosition, None)
    PointerDevice = property(get_PointerDevice, None)
    PointerId = property(get_PointerId, None)
    Position = property(get_Position, None)
    Properties = property(get_Properties, None)
    RawPosition = property(get_RawPosition, None)
    Timestamp = property(get_Timestamp, None)
class PointerPointProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IPointerPointProperties
    _classid_ = 'Windows.UI.Input.PointerPointProperties'
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_IsInverted(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsEraser(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_XTilt(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_YTilt(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_Twist(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_ContactRect(self: win32more.Windows.UI.Input.IPointerPointProperties) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_ContactRectRaw(self: win32more.Windows.UI.Input.IPointerPointProperties) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_TouchConfidence(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLeftButtonPressed(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRightButtonPressed(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMiddleButtonPressed(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_MouseWheelDelta(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Int32: ...
    @winrt_mixinmethod
    def get_IsHorizontalMouseWheel(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPrimary(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInRange(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBarrelButtonPressed(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsXButton1Pressed(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsXButton2Pressed(self: win32more.Windows.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_PointerUpdateKind(self: win32more.Windows.UI.Input.IPointerPointProperties) -> win32more.Windows.UI.Input.PointerUpdateKind: ...
    @winrt_mixinmethod
    def HasUsage(self: win32more.Windows.UI.Input.IPointerPointProperties, usagePage: UInt32, usageId: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def GetUsageValue(self: win32more.Windows.UI.Input.IPointerPointProperties, usagePage: UInt32, usageId: UInt32) -> Int32: ...
    @winrt_mixinmethod
    def get_ZDistance(self: win32more.Windows.UI.Input.IPointerPointProperties2) -> win32more.Windows.Foundation.IReference[Single]: ...
    ContactRect = property(get_ContactRect, None)
    ContactRectRaw = property(get_ContactRectRaw, None)
    IsBarrelButtonPressed = property(get_IsBarrelButtonPressed, None)
    IsCanceled = property(get_IsCanceled, None)
    IsEraser = property(get_IsEraser, None)
    IsHorizontalMouseWheel = property(get_IsHorizontalMouseWheel, None)
    IsInRange = property(get_IsInRange, None)
    IsInverted = property(get_IsInverted, None)
    IsLeftButtonPressed = property(get_IsLeftButtonPressed, None)
    IsMiddleButtonPressed = property(get_IsMiddleButtonPressed, None)
    IsPrimary = property(get_IsPrimary, None)
    IsRightButtonPressed = property(get_IsRightButtonPressed, None)
    IsXButton1Pressed = property(get_IsXButton1Pressed, None)
    IsXButton2Pressed = property(get_IsXButton2Pressed, None)
    MouseWheelDelta = property(get_MouseWheelDelta, None)
    Orientation = property(get_Orientation, None)
    PointerUpdateKind = property(get_PointerUpdateKind, None)
    Pressure = property(get_Pressure, None)
    TouchConfidence = property(get_TouchConfidence, None)
    Twist = property(get_Twist, None)
    XTilt = property(get_XTilt, None)
    YTilt = property(get_YTilt, None)
    ZDistance = property(get_ZDistance, None)
class PointerUpdateKind(Enum, Int32):
    Other = 0
    LeftButtonPressed = 1
    LeftButtonReleased = 2
    RightButtonPressed = 3
    RightButtonReleased = 4
    MiddleButtonPressed = 5
    MiddleButtonReleased = 6
    XButton1Pressed = 7
    XButton1Released = 8
    XButton2Pressed = 9
    XButton2Released = 10
class PointerVisualizationSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IPointerVisualizationSettings
    _classid_ = 'Windows.UI.Input.PointerVisualizationSettings'
    @winrt_mixinmethod
    def put_IsContactFeedbackEnabled(self: win32more.Windows.UI.Input.IPointerVisualizationSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsContactFeedbackEnabled(self: win32more.Windows.UI.Input.IPointerVisualizationSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBarrelButtonFeedbackEnabled(self: win32more.Windows.UI.Input.IPointerVisualizationSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBarrelButtonFeedbackEnabled(self: win32more.Windows.UI.Input.IPointerVisualizationSettings) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Input.IPointerVisualizationSettingsStatics) -> win32more.Windows.UI.Input.PointerVisualizationSettings: ...
    IsBarrelButtonFeedbackEnabled = property(get_IsBarrelButtonFeedbackEnabled, put_IsBarrelButtonFeedbackEnabled)
    IsContactFeedbackEnabled = property(get_IsContactFeedbackEnabled, put_IsContactFeedbackEnabled)
class RadialController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialController
    _classid_ = 'Windows.UI.Input.RadialController'
    @winrt_mixinmethod
    def get_Menu(self: win32more.Windows.UI.Input.IRadialController) -> win32more.Windows.UI.Input.RadialControllerMenu: ...
    @winrt_mixinmethod
    def get_RotationResolutionInDegrees(self: win32more.Windows.UI.Input.IRadialController) -> Double: ...
    @winrt_mixinmethod
    def put_RotationResolutionInDegrees(self: win32more.Windows.UI.Input.IRadialController, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_UseAutomaticHapticFeedback(self: win32more.Windows.UI.Input.IRadialController) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseAutomaticHapticFeedback(self: win32more.Windows.UI.Input.IRadialController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_ScreenContactStarted(self: win32more.Windows.UI.Input.IRadialController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerScreenContactStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenContactStarted(self: win32more.Windows.UI.Input.IRadialController, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScreenContactEnded(self: win32more.Windows.UI.Input.IRadialController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenContactEnded(self: win32more.Windows.UI.Input.IRadialController, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScreenContactContinued(self: win32more.Windows.UI.Input.IRadialController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerScreenContactContinuedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenContactContinued(self: win32more.Windows.UI.Input.IRadialController, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ControlLost(self: win32more.Windows.UI.Input.IRadialController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ControlLost(self: win32more.Windows.UI.Input.IRadialController, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RotationChanged(self: win32more.Windows.UI.Input.IRadialController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerRotationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RotationChanged(self: win32more.Windows.UI.Input.IRadialController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonClicked(self: win32more.Windows.UI.Input.IRadialController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonClicked(self: win32more.Windows.UI.Input.IRadialController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ControlAcquired(self: win32more.Windows.UI.Input.IRadialController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerControlAcquiredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ControlAcquired(self: win32more.Windows.UI.Input.IRadialController, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonPressed(self: win32more.Windows.UI.Input.IRadialController2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonPressed(self: win32more.Windows.UI.Input.IRadialController2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonHolding(self: win32more.Windows.UI.Input.IRadialController2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonHoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonHolding(self: win32more.Windows.UI.Input.IRadialController2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ButtonReleased(self: win32more.Windows.UI.Input.IRadialController2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialController, win32more.Windows.UI.Input.RadialControllerButtonReleasedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ButtonReleased(self: win32more.Windows.UI.Input.IRadialController2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.UI.Input.IRadialControllerStatics) -> Boolean: ...
    @winrt_classmethod
    def CreateForCurrentView(cls: win32more.Windows.UI.Input.IRadialControllerStatics) -> win32more.Windows.UI.Input.RadialController: ...
    Menu = property(get_Menu, None)
    RotationResolutionInDegrees = property(get_RotationResolutionInDegrees, put_RotationResolutionInDegrees)
    UseAutomaticHapticFeedback = property(get_UseAutomaticHapticFeedback, put_UseAutomaticHapticFeedback)
    ScreenContactStarted = event()
    ScreenContactEnded = event()
    ScreenContactContinued = event()
    ControlLost = event()
    RotationChanged = event()
    ButtonClicked = event()
    ControlAcquired = event()
    ButtonPressed = event()
    ButtonHolding = event()
    ButtonReleased = event()
class RadialControllerButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerButtonClickedEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerButtonClickedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerButtonClickedEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerButtonClickedEventArgs2) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerButtonHoldingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerButtonHoldingEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerButtonHoldingEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerButtonHoldingEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerButtonHoldingEventArgs) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerButtonPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerButtonPressedEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerButtonPressedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerButtonPressedEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerButtonPressedEventArgs) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerButtonReleasedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerButtonReleasedEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerButtonReleasedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerButtonReleasedEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerButtonReleasedEventArgs) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class _RadialControllerConfiguration_Meta_(ComPtr.__class__):
    pass
class RadialControllerConfiguration(ComPtr, metaclass=_RadialControllerConfiguration_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerConfiguration
    _classid_ = 'Windows.UI.Input.RadialControllerConfiguration'
    @winrt_mixinmethod
    def SetDefaultMenuItems(self: win32more.Windows.UI.Input.IRadialControllerConfiguration, buttons: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.RadialControllerSystemMenuItemKind]) -> Void: ...
    @winrt_mixinmethod
    def ResetToDefaultMenuItems(self: win32more.Windows.UI.Input.IRadialControllerConfiguration) -> Void: ...
    @winrt_mixinmethod
    def TrySelectDefaultMenuItem(self: win32more.Windows.UI.Input.IRadialControllerConfiguration, type: win32more.Windows.UI.Input.RadialControllerSystemMenuItemKind) -> Boolean: ...
    @winrt_mixinmethod
    def put_ActiveControllerWhenMenuIsSuppressed(self: win32more.Windows.UI.Input.IRadialControllerConfiguration2, value: win32more.Windows.UI.Input.RadialController) -> Void: ...
    @winrt_mixinmethod
    def get_ActiveControllerWhenMenuIsSuppressed(self: win32more.Windows.UI.Input.IRadialControllerConfiguration2) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_mixinmethod
    def put_IsMenuSuppressed(self: win32more.Windows.UI.Input.IRadialControllerConfiguration2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsMenuSuppressed(self: win32more.Windows.UI.Input.IRadialControllerConfiguration2) -> Boolean: ...
    @winrt_classmethod
    def put_AppController(cls: win32more.Windows.UI.Input.IRadialControllerConfigurationStatics2, value: win32more.Windows.UI.Input.RadialController) -> Void: ...
    @winrt_classmethod
    def get_AppController(cls: win32more.Windows.UI.Input.IRadialControllerConfigurationStatics2) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_classmethod
    def put_IsAppControllerEnabled(cls: win32more.Windows.UI.Input.IRadialControllerConfigurationStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsAppControllerEnabled(cls: win32more.Windows.UI.Input.IRadialControllerConfigurationStatics2) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Input.IRadialControllerConfigurationStatics) -> win32more.Windows.UI.Input.RadialControllerConfiguration: ...
    ActiveControllerWhenMenuIsSuppressed = property(get_ActiveControllerWhenMenuIsSuppressed, put_ActiveControllerWhenMenuIsSuppressed)
    IsMenuSuppressed = property(get_IsMenuSuppressed, put_IsMenuSuppressed)
    _RadialControllerConfiguration_Meta_.AppController = property(get_AppController, put_AppController)
    _RadialControllerConfiguration_Meta_.IsAppControllerEnabled = property(get_IsAppControllerEnabled, put_IsAppControllerEnabled)
class RadialControllerControlAcquiredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerControlAcquiredEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerControlAcquiredEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerControlAcquiredEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: win32more.Windows.UI.Input.IRadialControllerControlAcquiredEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerControlAcquiredEventArgs2) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerMenu(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerMenu
    _classid_ = 'Windows.UI.Input.RadialControllerMenu'
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.UI.Input.IRadialControllerMenu) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.RadialControllerMenuItem]: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.UI.Input.IRadialControllerMenu) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.UI.Input.IRadialControllerMenu, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetSelectedMenuItem(self: win32more.Windows.UI.Input.IRadialControllerMenu) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_mixinmethod
    def SelectMenuItem(self: win32more.Windows.UI.Input.IRadialControllerMenu, menuItem: win32more.Windows.UI.Input.RadialControllerMenuItem) -> Void: ...
    @winrt_mixinmethod
    def TrySelectPreviouslySelectedMenuItem(self: win32more.Windows.UI.Input.IRadialControllerMenu) -> Boolean: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Items = property(get_Items, None)
class RadialControllerMenuItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerMenuItem
    _classid_ = 'Windows.UI.Input.RadialControllerMenuItem'
    @winrt_mixinmethod
    def get_DisplayText(self: win32more.Windows.UI.Input.IRadialControllerMenuItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Input.IRadialControllerMenuItem) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Input.IRadialControllerMenuItem, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def add_Invoked(self: win32more.Windows.UI.Input.IRadialControllerMenuItem, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.RadialControllerMenuItem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Invoked(self: win32more.Windows.UI.Input.IRadialControllerMenuItem, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateFromFontGlyph(cls: win32more.Windows.UI.Input.IRadialControllerMenuItemStatics2, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_classmethod
    def CreateFromFontGlyphWithUri(cls: win32more.Windows.UI.Input.IRadialControllerMenuItemStatics2, displayText: WinRT_String, glyph: WinRT_String, fontFamily: WinRT_String, fontUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_classmethod
    def CreateFromIcon(cls: win32more.Windows.UI.Input.IRadialControllerMenuItemStatics, displayText: WinRT_String, icon: win32more.Windows.Storage.Streams.RandomAccessStreamReference) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    @winrt_classmethod
    def CreateFromKnownIcon(cls: win32more.Windows.UI.Input.IRadialControllerMenuItemStatics, displayText: WinRT_String, value: win32more.Windows.UI.Input.RadialControllerMenuKnownIcon) -> win32more.Windows.UI.Input.RadialControllerMenuItem: ...
    DisplayText = property(get_DisplayText, None)
    Tag = property(get_Tag, put_Tag)
    Invoked = event()
class RadialControllerMenuKnownIcon(Enum, Int32):
    Scroll = 0
    Zoom = 1
    UndoRedo = 2
    Volume = 3
    NextPreviousTrack = 4
    Ruler = 5
    InkColor = 6
    InkThickness = 7
    PenType = 8
class RadialControllerRotationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerRotationChangedEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerRotationChangedEventArgs'
    @winrt_mixinmethod
    def get_RotationDeltaInDegrees(self: win32more.Windows.UI.Input.IRadialControllerRotationChangedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerRotationChangedEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: win32more.Windows.UI.Input.IRadialControllerRotationChangedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerRotationChangedEventArgs2) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    RotationDeltaInDegrees = property(get_RotationDeltaInDegrees, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerScreenContact(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerScreenContact
    _classid_ = 'Windows.UI.Input.RadialControllerScreenContact'
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.UI.Input.IRadialControllerScreenContact) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IRadialControllerScreenContact) -> win32more.Windows.Foundation.Point: ...
    Bounds = property(get_Bounds, None)
    Position = property(get_Position, None)
class RadialControllerScreenContactContinuedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerScreenContactContinuedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: win32more.Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerScreenContactContinuedEventArgs2) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerScreenContactEndedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerScreenContactEndedEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerScreenContactEndedEventArgs'
    @winrt_mixinmethod
    def get_IsButtonPressed(self: win32more.Windows.UI.Input.IRadialControllerScreenContactEndedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerScreenContactEndedEventArgs) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerScreenContactStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs
    _classid_ = 'Windows.UI.Input.RadialControllerScreenContactStartedEventArgs'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs) -> win32more.Windows.UI.Input.RadialControllerScreenContact: ...
    @winrt_mixinmethod
    def get_IsButtonPressed(self: win32more.Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.IRadialControllerScreenContactStartedEventArgs2) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    Contact = property(get_Contact, None)
    IsButtonPressed = property(get_IsButtonPressed, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class RadialControllerSystemMenuItemKind(Enum, Int32):
    Scroll = 0
    Zoom = 1
    UndoRedo = 2
    Volume = 3
    NextPreviousTrack = 4
class RightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.IRightTappedEventArgs
    _classid_ = 'Windows.UI.Input.RightTappedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.IRightTappedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.IRightTappedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.IRightTappedEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class SystemButtonEventController(ComPtr):
    extends: win32more.Windows.UI.Input.AttachableInputObject
    default_interface: win32more.Windows.UI.Input.ISystemButtonEventController
    _classid_ = 'Windows.UI.Input.SystemButtonEventController'
    @winrt_mixinmethod
    def add_SystemFunctionButtonPressed(self: win32more.Windows.UI.Input.ISystemButtonEventController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionButtonEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionButtonPressed(self: win32more.Windows.UI.Input.ISystemButtonEventController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemFunctionButtonReleased(self: win32more.Windows.UI.Input.ISystemButtonEventController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionButtonEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionButtonReleased(self: win32more.Windows.UI.Input.ISystemButtonEventController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemFunctionLockChanged(self: win32more.Windows.UI.Input.ISystemButtonEventController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionLockChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionLockChanged(self: win32more.Windows.UI.Input.ISystemButtonEventController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemFunctionLockIndicatorChanged(self: win32more.Windows.UI.Input.ISystemButtonEventController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.SystemButtonEventController, win32more.Windows.UI.Input.SystemFunctionLockIndicatorChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemFunctionLockIndicatorChanged(self: win32more.Windows.UI.Input.ISystemButtonEventController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateForDispatcherQueue(cls: win32more.Windows.UI.Input.ISystemButtonEventControllerStatics, queue: win32more.Windows.System.DispatcherQueue) -> win32more.Windows.UI.Input.SystemButtonEventController: ...
    SystemFunctionButtonPressed = event()
    SystemFunctionButtonReleased = event()
    SystemFunctionLockChanged = event()
    SystemFunctionLockIndicatorChanged = event()
class SystemFunctionButtonEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.ISystemFunctionButtonEventArgs
    _classid_ = 'Windows.UI.Input.SystemFunctionButtonEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.UI.Input.ISystemFunctionButtonEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Input.ISystemFunctionButtonEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Input.ISystemFunctionButtonEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Timestamp = property(get_Timestamp, None)
class SystemFunctionLockChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.ISystemFunctionLockChangedEventArgs
    _classid_ = 'Windows.UI.Input.SystemFunctionLockChangedEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.UI.Input.ISystemFunctionLockChangedEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsLocked(self: win32more.Windows.UI.Input.ISystemFunctionLockChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Input.ISystemFunctionLockChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Input.ISystemFunctionLockChangedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    IsLocked = property(get_IsLocked, None)
    Timestamp = property(get_Timestamp, None)
class SystemFunctionLockIndicatorChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs
    _classid_ = 'Windows.UI.Input.SystemFunctionLockIndicatorChangedEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsIndicatorOn(self: win32more.Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Input.ISystemFunctionLockIndicatorChangedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    IsIndicatorOn = property(get_IsIndicatorOn, None)
    Timestamp = property(get_Timestamp, None)
class TappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.ITappedEventArgs
    _classid_ = 'Windows.UI.Input.TappedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Input.ITappedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.ITappedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_TapCount(self: win32more.Windows.UI.Input.ITappedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_ContactCount(self: win32more.Windows.UI.Input.ITappedEventArgs2) -> UInt32: ...
    ContactCount = property(get_ContactCount, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    TapCount = property(get_TapCount, None)
class TouchpadGesturesController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.ITouchpadGesturesController
    _classid_ = 'Windows.UI.Input.TouchpadGesturesController'
    @winrt_mixinmethod
    def get_GesturesEnabled(self: win32more.Windows.UI.Input.ITouchpadGesturesController) -> Boolean: ...
    @winrt_mixinmethod
    def put_GesturesEnabled(self: win32more.Windows.UI.Input.ITouchpadGesturesController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedGestures(self: win32more.Windows.UI.Input.ITouchpadGesturesController) -> win32more.Windows.UI.Input.TouchpadGlobalGestureKinds: ...
    @winrt_mixinmethod
    def put_SupportedGestures(self: win32more.Windows.UI.Input.ITouchpadGesturesController, value: win32more.Windows.UI.Input.TouchpadGlobalGestureKinds) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: win32more.Windows.UI.Input.ITouchpadGesturesController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: win32more.Windows.UI.Input.ITouchpadGesturesController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: win32more.Windows.UI.Input.ITouchpadGesturesController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: win32more.Windows.UI.Input.ITouchpadGesturesController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: win32more.Windows.UI.Input.ITouchpadGesturesController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: win32more.Windows.UI.Input.ITouchpadGesturesController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TouchpadGlobalActionPerformed(self: win32more.Windows.UI.Input.ITouchpadGesturesController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.TouchpadGesturesController, win32more.Windows.UI.Input.TouchpadGlobalActionEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TouchpadGlobalActionPerformed(self: win32more.Windows.UI.Input.ITouchpadGesturesController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.UI.Input.ITouchpadGesturesControllerStatics) -> Boolean: ...
    @winrt_classmethod
    def CreateForProcess(cls: win32more.Windows.UI.Input.ITouchpadGesturesControllerStatics) -> win32more.Windows.UI.Input.TouchpadGesturesController: ...
    GesturesEnabled = property(get_GesturesEnabled, put_GesturesEnabled)
    SupportedGestures = property(get_SupportedGestures, put_SupportedGestures)
    PointerPressed = event()
    PointerMoved = event()
    PointerReleased = event()
    TouchpadGlobalActionPerformed = event()
class TouchpadGlobalAction(Enum, Int32):
    ThreeFingerTap = 0
    FourFingerTap = 1
    FiveFingerTap = 2
    ThreeFingerPressDown = 3
    FourFingerPressDown = 4
    FiveFingerPressDown = 5
    ThreeFingerPressUp = 6
    FourFingerPressUp = 7
    FiveFingerPressUp = 8
class TouchpadGlobalActionEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.ITouchpadGlobalActionEventArgs
    _classid_ = 'Windows.UI.Input.TouchpadGlobalActionEventArgs'
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.UI.Input.ITouchpadGlobalActionEventArgs) -> win32more.Windows.UI.Input.TouchpadGlobalAction: ...
    Action = property(get_Action, None)
class TouchpadGlobalGestureKinds(Enum, UInt32):
    None_ = 0
    ThreeFingerManipulations = 1
    FourFingerManipulations = 2
    FiveFingerManipulations = 4
    ThreeFingerActions = 8
    FourFingerActions = 16
    FiveFingerActions = 32


make_ready(__name__)
