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
import Windows.System
import Windows.UI
import Windows.UI.Composition
import Windows.UI.Core
import Windows.UI.Input
import Windows.UI.Popups
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AcceleratorKeyEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IAcceleratorKeyEventArgs
    _classid_ = 'Windows.UI.Core.AcceleratorKeyEventArgs'
    @winrt_mixinmethod
    def get_EventType(self: Windows.UI.Core.IAcceleratorKeyEventArgs) -> Windows.UI.Core.CoreAcceleratorKeyEventType: ...
    @winrt_mixinmethod
    def get_VirtualKey(self: Windows.UI.Core.IAcceleratorKeyEventArgs) -> Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: Windows.UI.Core.IAcceleratorKeyEventArgs) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.UI.Core.IAcceleratorKeyEventArgs2) -> WinRT_String: ...
    EventType = property(get_EventType, None)
    VirtualKey = property(get_VirtualKey, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
    DeviceId = property(get_DeviceId, None)
AppViewBackButtonVisibility = Int32
AppViewBackButtonVisibility_Visible: AppViewBackButtonVisibility = 0
AppViewBackButtonVisibility_Collapsed: AppViewBackButtonVisibility = 1
AppViewBackButtonVisibility_Disabled: AppViewBackButtonVisibility = 2
class AutomationProviderRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IAutomationProviderRequestedEventArgs
    _classid_ = 'Windows.UI.Core.AutomationProviderRequestedEventArgs'
    @winrt_mixinmethod
    def get_AutomationProvider(self: Windows.UI.Core.IAutomationProviderRequestedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_AutomationProvider(self: Windows.UI.Core.IAutomationProviderRequestedEventArgs, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    AutomationProvider = property(get_AutomationProvider, put_AutomationProvider)
    Handled = property(get_Handled, put_Handled)
class BackRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IBackRequestedEventArgs
    _classid_ = 'Windows.UI.Core.BackRequestedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.IBackRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.IBackRequestedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class CharacterReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICharacterReceivedEventArgs
    _classid_ = 'Windows.UI.Core.CharacterReceivedEventArgs'
    @winrt_mixinmethod
    def get_KeyCode(self: Windows.UI.Core.ICharacterReceivedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: Windows.UI.Core.ICharacterReceivedEventArgs) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    KeyCode = property(get_KeyCode, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
class ClosestInteractiveBoundsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IClosestInteractiveBoundsRequestedEventArgs
    _classid_ = 'Windows.UI.Core.ClosestInteractiveBoundsRequestedEventArgs'
    @winrt_mixinmethod
    def get_PointerPosition(self: Windows.UI.Core.IClosestInteractiveBoundsRequestedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_SearchBounds(self: Windows.UI.Core.IClosestInteractiveBoundsRequestedEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_ClosestInteractiveBounds(self: Windows.UI.Core.IClosestInteractiveBoundsRequestedEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_ClosestInteractiveBounds(self: Windows.UI.Core.IClosestInteractiveBoundsRequestedEventArgs, value: Windows.Foundation.Rect) -> Void: ...
    PointerPosition = property(get_PointerPosition, None)
    SearchBounds = property(get_SearchBounds, None)
    ClosestInteractiveBounds = property(get_ClosestInteractiveBounds, put_ClosestInteractiveBounds)
CoreAcceleratorKeyEventType = Int32
CoreAcceleratorKeyEventType_Character: CoreAcceleratorKeyEventType = 2
CoreAcceleratorKeyEventType_DeadCharacter: CoreAcceleratorKeyEventType = 3
CoreAcceleratorKeyEventType_KeyDown: CoreAcceleratorKeyEventType = 0
CoreAcceleratorKeyEventType_KeyUp: CoreAcceleratorKeyEventType = 1
CoreAcceleratorKeyEventType_SystemCharacter: CoreAcceleratorKeyEventType = 6
CoreAcceleratorKeyEventType_SystemDeadCharacter: CoreAcceleratorKeyEventType = 7
CoreAcceleratorKeyEventType_SystemKeyDown: CoreAcceleratorKeyEventType = 4
CoreAcceleratorKeyEventType_SystemKeyUp: CoreAcceleratorKeyEventType = 5
CoreAcceleratorKeyEventType_UnicodeCharacter: CoreAcceleratorKeyEventType = 8
class CoreAcceleratorKeys(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreAcceleratorKeys
    _classid_ = 'Windows.UI.Core.CoreAcceleratorKeys'
    @winrt_mixinmethod
    def add_AcceleratorKeyActivated(self: Windows.UI.Core.ICoreAcceleratorKeys, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreDispatcher, Windows.UI.Core.AcceleratorKeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AcceleratorKeyActivated(self: Windows.UI.Core.ICoreAcceleratorKeys, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class CoreComponentInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreInputSourceBase
    _classid_ = 'Windows.UI.Core.CoreComponentInputSource'
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.UI.Core.ICoreInputSourceBase) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_IsInputEnabled(self: Windows.UI.Core.ICoreInputSourceBase) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInputEnabled(self: Windows.UI.Core.ICoreInputSourceBase, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_InputEnabled(self: Windows.UI.Core.ICoreInputSourceBase, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.InputEnabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputEnabled(self: Windows.UI.Core.ICoreInputSourceBase, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ReleasePointerCapture(self: Windows.UI.Core.ICorePointerInputSource) -> Void: ...
    @winrt_mixinmethod
    def SetPointerCapture(self: Windows.UI.Core.ICorePointerInputSource) -> Void: ...
    @winrt_mixinmethod
    def get_HasCapture(self: Windows.UI.Core.ICorePointerInputSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_PointerPosition(self: Windows.UI.Core.ICorePointerInputSource) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_PointerCursor(self: Windows.UI.Core.ICorePointerInputSource) -> Windows.UI.Core.CoreCursor: ...
    @winrt_mixinmethod
    def put_PointerCursor(self: Windows.UI.Core.ICorePointerInputSource, value: Windows.UI.Core.CoreCursor) -> Void: ...
    @winrt_mixinmethod
    def add_PointerCaptureLost(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCaptureLost(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerEntered(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerWheelChanged(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerWheelChanged(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentKeyState(self: Windows.UI.Core.ICoreKeyboardInputSource, virtualKey: Windows.System.VirtualKey) -> Windows.UI.Core.CoreVirtualKeyStates: ...
    @winrt_mixinmethod
    def add_CharacterReceived(self: Windows.UI.Core.ICoreKeyboardInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.CharacterReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CharacterReceived(self: Windows.UI.Core.ICoreKeyboardInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyDown(self: Windows.UI.Core.ICoreKeyboardInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyDown(self: Windows.UI.Core.ICoreKeyboardInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyUp(self: Windows.UI.Core.ICoreKeyboardInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyUp(self: Windows.UI.Core.ICoreKeyboardInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HasFocus(self: Windows.UI.Core.ICoreComponentFocusable) -> Boolean: ...
    @winrt_mixinmethod
    def add_GotFocus(self: Windows.UI.Core.ICoreComponentFocusable, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.CoreWindowEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: Windows.UI.Core.ICoreComponentFocusable, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LostFocus(self: Windows.UI.Core.ICoreComponentFocusable, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.CoreWindowEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LostFocus(self: Windows.UI.Core.ICoreComponentFocusable, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TouchHitTesting(self: Windows.UI.Core.ICoreTouchHitTesting, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.TouchHitTestingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TouchHitTesting(self: Windows.UI.Core.ICoreTouchHitTesting, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ClosestInteractiveBoundsRequested(self: Windows.UI.Core.ICoreClosestInteractiveBoundsRequested, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreComponentInputSource, Windows.UI.Core.ClosestInteractiveBoundsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ClosestInteractiveBoundsRequested(self: Windows.UI.Core.ICoreClosestInteractiveBoundsRequested, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentKeyEventDeviceId(self: Windows.UI.Core.ICoreKeyboardInputSource2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.UI.Core.ICorePointerInputSource2) -> Windows.System.DispatcherQueue: ...
    Dispatcher = property(get_Dispatcher, None)
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    HasCapture = property(get_HasCapture, None)
    PointerPosition = property(get_PointerPosition, None)
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
    HasFocus = property(get_HasFocus, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
class CoreCursor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreCursor
    _classid_ = 'Windows.UI.Core.CoreCursor'
    @winrt_factorymethod
    def CreateCursor(cls: Windows.UI.Core.ICoreCursorFactory, type: Windows.UI.Core.CoreCursorType, id: UInt32) -> Windows.UI.Core.CoreCursor: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Core.ICoreCursor) -> UInt32: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.UI.Core.ICoreCursor) -> Windows.UI.Core.CoreCursorType: ...
    Id = property(get_Id, None)
    Type = property(get_Type, None)
CoreCursorType = Int32
CoreCursorType_Arrow: CoreCursorType = 0
CoreCursorType_Cross: CoreCursorType = 1
CoreCursorType_Custom: CoreCursorType = 2
CoreCursorType_Hand: CoreCursorType = 3
CoreCursorType_Help: CoreCursorType = 4
CoreCursorType_IBeam: CoreCursorType = 5
CoreCursorType_SizeAll: CoreCursorType = 6
CoreCursorType_SizeNortheastSouthwest: CoreCursorType = 7
CoreCursorType_SizeNorthSouth: CoreCursorType = 8
CoreCursorType_SizeNorthwestSoutheast: CoreCursorType = 9
CoreCursorType_SizeWestEast: CoreCursorType = 10
CoreCursorType_UniversalNo: CoreCursorType = 11
CoreCursorType_UpArrow: CoreCursorType = 12
CoreCursorType_Wait: CoreCursorType = 13
CoreCursorType_Pin: CoreCursorType = 14
CoreCursorType_Person: CoreCursorType = 15
class CoreDispatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreDispatcher
    _classid_ = 'Windows.UI.Core.CoreDispatcher'
    @winrt_mixinmethod
    def get_HasThreadAccess(self: Windows.UI.Core.ICoreDispatcher) -> Boolean: ...
    @winrt_mixinmethod
    def ProcessEvents(self: Windows.UI.Core.ICoreDispatcher, options: Windows.UI.Core.CoreProcessEventsOption) -> Void: ...
    @winrt_mixinmethod
    def RunAsync(self: Windows.UI.Core.ICoreDispatcher, priority: Windows.UI.Core.CoreDispatcherPriority, agileCallback: Windows.UI.Core.DispatchedHandler) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RunIdleAsync(self: Windows.UI.Core.ICoreDispatcher, agileCallback: Windows.UI.Core.IdleDispatchedHandler) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_AcceleratorKeyActivated(self: Windows.UI.Core.ICoreAcceleratorKeys, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreDispatcher, Windows.UI.Core.AcceleratorKeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AcceleratorKeyActivated(self: Windows.UI.Core.ICoreAcceleratorKeys, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentPriority(self: Windows.UI.Core.ICoreDispatcherWithTaskPriority) -> Windows.UI.Core.CoreDispatcherPriority: ...
    @winrt_mixinmethod
    def put_CurrentPriority(self: Windows.UI.Core.ICoreDispatcherWithTaskPriority, value: Windows.UI.Core.CoreDispatcherPriority) -> Void: ...
    @winrt_mixinmethod
    def ShouldYield(self: Windows.UI.Core.ICoreDispatcherWithTaskPriority) -> Boolean: ...
    @winrt_mixinmethod
    def ShouldYieldToPriority(self: Windows.UI.Core.ICoreDispatcherWithTaskPriority, priority: Windows.UI.Core.CoreDispatcherPriority) -> Boolean: ...
    @winrt_mixinmethod
    def StopProcessEvents(self: Windows.UI.Core.ICoreDispatcherWithTaskPriority) -> Void: ...
    @winrt_mixinmethod
    def TryRunAsync(self: Windows.UI.Core.ICoreDispatcher2, priority: Windows.UI.Core.CoreDispatcherPriority, agileCallback: Windows.UI.Core.DispatchedHandler) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRunIdleAsync(self: Windows.UI.Core.ICoreDispatcher2, agileCallback: Windows.UI.Core.IdleDispatchedHandler) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
    CurrentPriority = property(get_CurrentPriority, put_CurrentPriority)
CoreDispatcherPriority = Int32
CoreDispatcherPriority_Idle: CoreDispatcherPriority = -2
CoreDispatcherPriority_Low: CoreDispatcherPriority = -1
CoreDispatcherPriority_Normal: CoreDispatcherPriority = 0
CoreDispatcherPriority_High: CoreDispatcherPriority = 1
CoreIndependentInputFilters = UInt32
CoreIndependentInputFilters_None: CoreIndependentInputFilters = 0
CoreIndependentInputFilters_MouseButton: CoreIndependentInputFilters = 1
CoreIndependentInputFilters_MouseWheel: CoreIndependentInputFilters = 2
CoreIndependentInputFilters_MouseHover: CoreIndependentInputFilters = 4
CoreIndependentInputFilters_PenWithBarrel: CoreIndependentInputFilters = 8
CoreIndependentInputFilters_PenInverted: CoreIndependentInputFilters = 16
class CoreIndependentInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreInputSourceBase
    _classid_ = 'Windows.UI.Core.CoreIndependentInputSource'
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.UI.Core.ICoreInputSourceBase) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_IsInputEnabled(self: Windows.UI.Core.ICoreInputSourceBase) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInputEnabled(self: Windows.UI.Core.ICoreInputSourceBase, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_InputEnabled(self: Windows.UI.Core.ICoreInputSourceBase, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.InputEnabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputEnabled(self: Windows.UI.Core.ICoreInputSourceBase, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ReleasePointerCapture(self: Windows.UI.Core.ICorePointerInputSource) -> Void: ...
    @winrt_mixinmethod
    def SetPointerCapture(self: Windows.UI.Core.ICorePointerInputSource) -> Void: ...
    @winrt_mixinmethod
    def get_HasCapture(self: Windows.UI.Core.ICorePointerInputSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_PointerPosition(self: Windows.UI.Core.ICorePointerInputSource) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_PointerCursor(self: Windows.UI.Core.ICorePointerInputSource) -> Windows.UI.Core.CoreCursor: ...
    @winrt_mixinmethod
    def put_PointerCursor(self: Windows.UI.Core.ICorePointerInputSource, value: Windows.UI.Core.CoreCursor) -> Void: ...
    @winrt_mixinmethod
    def add_PointerCaptureLost(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCaptureLost(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerEntered(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerWheelChanged(self: Windows.UI.Core.ICorePointerInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerWheelChanged(self: Windows.UI.Core.ICorePointerInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.UI.Core.ICorePointerInputSource2) -> Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def add_PointerRoutedAway(self: Windows.UI.Core.ICorePointerRedirector, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedAway(self: Windows.UI.Core.ICorePointerRedirector, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedTo(self: Windows.UI.Core.ICorePointerRedirector, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedTo(self: Windows.UI.Core.ICorePointerRedirector, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedReleased(self: Windows.UI.Core.ICorePointerRedirector, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedReleased(self: Windows.UI.Core.ICorePointerRedirector, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Dispatcher = property(get_Dispatcher, None)
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    HasCapture = property(get_HasCapture, None)
    PointerPosition = property(get_PointerPosition, None)
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
    DispatcherQueue = property(get_DispatcherQueue, None)
class CoreIndependentInputSourceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreIndependentInputSourceController
    _classid_ = 'Windows.UI.Core.CoreIndependentInputSourceController'
    @winrt_mixinmethod
    def get_IsTransparentForUncontrolledInput(self: Windows.UI.Core.ICoreIndependentInputSourceController) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTransparentForUncontrolledInput(self: Windows.UI.Core.ICoreIndependentInputSourceController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPalmRejectionEnabled(self: Windows.UI.Core.ICoreIndependentInputSourceController) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPalmRejectionEnabled(self: Windows.UI.Core.ICoreIndependentInputSourceController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Core.ICoreIndependentInputSourceController) -> Windows.UI.Core.CoreIndependentInputSource: ...
    @winrt_mixinmethod
    def SetControlledInput(self: Windows.UI.Core.ICoreIndependentInputSourceController, inputTypes: Windows.UI.Core.CoreInputDeviceTypes) -> Void: ...
    @winrt_mixinmethod
    def SetControlledInputWithFilters(self: Windows.UI.Core.ICoreIndependentInputSourceController, inputTypes: Windows.UI.Core.CoreInputDeviceTypes, required: Windows.UI.Core.CoreIndependentInputFilters, excluded: Windows.UI.Core.CoreIndependentInputFilters) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForVisual(cls: Windows.UI.Core.ICoreIndependentInputSourceControllerStatics, visual: Windows.UI.Composition.Visual) -> Windows.UI.Core.CoreIndependentInputSourceController: ...
    @winrt_classmethod
    def CreateForIVisualElement(cls: Windows.UI.Core.ICoreIndependentInputSourceControllerStatics, visualElement: Windows.UI.Composition.IVisualElement) -> Windows.UI.Core.CoreIndependentInputSourceController: ...
    IsTransparentForUncontrolledInput = property(get_IsTransparentForUncontrolledInput, put_IsTransparentForUncontrolledInput)
    IsPalmRejectionEnabled = property(get_IsPalmRejectionEnabled, put_IsPalmRejectionEnabled)
    Source = property(get_Source, None)
CoreInputDeviceTypes = UInt32
CoreInputDeviceTypes_None: CoreInputDeviceTypes = 0
CoreInputDeviceTypes_Touch: CoreInputDeviceTypes = 1
CoreInputDeviceTypes_Pen: CoreInputDeviceTypes = 2
CoreInputDeviceTypes_Mouse: CoreInputDeviceTypes = 4
class CorePhysicalKeyStatus(EasyCastStructure):
    RepeatCount: UInt32
    ScanCode: UInt32
    IsExtendedKey: Boolean
    IsMenuKeyDown: Boolean
    WasKeyDown: Boolean
    IsKeyReleased: Boolean
CoreProcessEventsOption = Int32
CoreProcessEventsOption_ProcessOneAndAllPending: CoreProcessEventsOption = 0
CoreProcessEventsOption_ProcessOneIfPresent: CoreProcessEventsOption = 1
CoreProcessEventsOption_ProcessUntilQuit: CoreProcessEventsOption = 2
CoreProcessEventsOption_ProcessAllIfPresent: CoreProcessEventsOption = 3
class CoreProximityEvaluation(EasyCastStructure):
    Score: Int32
    AdjustedPoint: Windows.Foundation.Point
CoreProximityEvaluationScore = Int32
CoreProximityEvaluationScore_Closest: CoreProximityEvaluationScore = 0
CoreProximityEvaluationScore_Farthest: CoreProximityEvaluationScore = 2147483647
CoreVirtualKeyStates = UInt32
CoreVirtualKeyStates_None: CoreVirtualKeyStates = 0
CoreVirtualKeyStates_Down: CoreVirtualKeyStates = 1
CoreVirtualKeyStates_Locked: CoreVirtualKeyStates = 2
class CoreWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreWindow
    _classid_ = 'Windows.UI.Core.CoreWindow'
    @winrt_mixinmethod
    def get_AutomationHostProvider(self: Windows.UI.Core.ICoreWindow) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Bounds(self: Windows.UI.Core.ICoreWindow) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CustomProperties(self: Windows.UI.Core.ICoreWindow) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.UI.Core.ICoreWindow) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_FlowDirection(self: Windows.UI.Core.ICoreWindow) -> Windows.UI.Core.CoreWindowFlowDirection: ...
    @winrt_mixinmethod
    def put_FlowDirection(self: Windows.UI.Core.ICoreWindow, value: Windows.UI.Core.CoreWindowFlowDirection) -> Void: ...
    @winrt_mixinmethod
    def get_IsInputEnabled(self: Windows.UI.Core.ICoreWindow) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInputEnabled(self: Windows.UI.Core.ICoreWindow, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerCursor(self: Windows.UI.Core.ICoreWindow) -> Windows.UI.Core.CoreCursor: ...
    @winrt_mixinmethod
    def put_PointerCursor(self: Windows.UI.Core.ICoreWindow, value: Windows.UI.Core.CoreCursor) -> Void: ...
    @winrt_mixinmethod
    def get_PointerPosition(self: Windows.UI.Core.ICoreWindow) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Visible(self: Windows.UI.Core.ICoreWindow) -> Boolean: ...
    @winrt_mixinmethod
    def Activate(self: Windows.UI.Core.ICoreWindow) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.UI.Core.ICoreWindow) -> Void: ...
    @winrt_mixinmethod
    def GetAsyncKeyState(self: Windows.UI.Core.ICoreWindow, virtualKey: Windows.System.VirtualKey) -> Windows.UI.Core.CoreVirtualKeyStates: ...
    @winrt_mixinmethod
    def GetKeyState(self: Windows.UI.Core.ICoreWindow, virtualKey: Windows.System.VirtualKey) -> Windows.UI.Core.CoreVirtualKeyStates: ...
    @winrt_mixinmethod
    def ReleasePointerCapture(self: Windows.UI.Core.ICoreWindow) -> Void: ...
    @winrt_mixinmethod
    def SetPointerCapture(self: Windows.UI.Core.ICoreWindow) -> Void: ...
    @winrt_mixinmethod
    def add_Activated(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.WindowActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AutomationProviderRequested(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.AutomationProviderRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AutomationProviderRequested(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CharacterReceived(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CharacterReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CharacterReceived(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CoreWindowEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_InputEnabled(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.InputEnabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputEnabled(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyDown(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyDown(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyUp(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyUp(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerCaptureLost(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCaptureLost(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerEntered(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TouchHitTesting(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.TouchHitTestingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TouchHitTesting(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerWheelChanged(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerWheelChanged(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SizeChanged(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.WindowSizeChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SizeChanged(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VisibilityChanged(self: Windows.UI.Core.ICoreWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.VisibilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisibilityChanged(self: Windows.UI.Core.ICoreWindow, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_PointerPosition(self: Windows.UI.Core.ICoreWindow2, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedAway(self: Windows.UI.Core.ICorePointerRedirector, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedAway(self: Windows.UI.Core.ICorePointerRedirector, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedTo(self: Windows.UI.Core.ICorePointerRedirector, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedTo(self: Windows.UI.Core.ICorePointerRedirector, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedReleased(self: Windows.UI.Core.ICorePointerRedirector, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedReleased(self: Windows.UI.Core.ICorePointerRedirector, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ClosestInteractiveBoundsRequested(self: Windows.UI.Core.ICoreWindow3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.ClosestInteractiveBoundsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ClosestInteractiveBoundsRequested(self: Windows.UI.Core.ICoreWindow3, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentKeyEventDeviceId(self: Windows.UI.Core.ICoreWindow3) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_ResizeStarted(self: Windows.UI.Core.ICoreWindow4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResizeStarted(self: Windows.UI.Core.ICoreWindow4, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResizeCompleted(self: Windows.UI.Core.ICoreWindow4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResizeCompleted(self: Windows.UI.Core.ICoreWindow4, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.UI.Core.ICoreWindow5) -> Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def get_ActivationMode(self: Windows.UI.Core.ICoreWindow5) -> Windows.UI.Core.CoreWindowActivationMode: ...
    @winrt_mixinmethod
    def get_UIContext(self: Windows.UI.Core.ICoreWindowWithContext) -> Windows.UI.UIContext: ...
    @winrt_classmethod
    def GetForCurrentThread(cls: Windows.UI.Core.ICoreWindowStatic) -> Windows.UI.Core.CoreWindow: ...
    AutomationHostProvider = property(get_AutomationHostProvider, None)
    Bounds = property(get_Bounds, None)
    CustomProperties = property(get_CustomProperties, None)
    Dispatcher = property(get_Dispatcher, None)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
    PointerPosition = property(get_PointerPosition, put_PointerPosition)
    Visible = property(get_Visible, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
    ActivationMode = property(get_ActivationMode, None)
    UIContext = property(get_UIContext, None)
CoreWindowActivationMode = Int32
CoreWindowActivationMode_None: CoreWindowActivationMode = 0
CoreWindowActivationMode_Deactivated: CoreWindowActivationMode = 1
CoreWindowActivationMode_ActivatedNotForeground: CoreWindowActivationMode = 2
CoreWindowActivationMode_ActivatedInForeground: CoreWindowActivationMode = 3
CoreWindowActivationState = Int32
CoreWindowActivationState_CodeActivated: CoreWindowActivationState = 0
CoreWindowActivationState_Deactivated: CoreWindowActivationState = 1
CoreWindowActivationState_PointerActivated: CoreWindowActivationState = 2
class CoreWindowDialog(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreWindowDialog
    _classid_ = 'Windows.UI.Core.CoreWindowDialog'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Core.CoreWindowDialog: ...
    @winrt_factorymethod
    def CreateWithTitle(cls: Windows.UI.Core.ICoreWindowDialogFactory, title: WinRT_String) -> Windows.UI.Core.CoreWindowDialog: ...
    @winrt_mixinmethod
    def add_Showing(self: Windows.UI.Core.ICoreWindowDialog, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CoreWindowPopupShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Showing(self: Windows.UI.Core.ICoreWindowDialog, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSize(self: Windows.UI.Core.ICoreWindowDialog) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_MinSize(self: Windows.UI.Core.ICoreWindowDialog) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.UI.Core.ICoreWindowDialog) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.UI.Core.ICoreWindowDialog, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsInteractionDelayed(self: Windows.UI.Core.ICoreWindowDialog) -> Int32: ...
    @winrt_mixinmethod
    def put_IsInteractionDelayed(self: Windows.UI.Core.ICoreWindowDialog, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Commands(self: Windows.UI.Core.ICoreWindowDialog) -> Windows.Foundation.Collections.IVector[Windows.UI.Popups.IUICommand]: ...
    @winrt_mixinmethod
    def get_DefaultCommandIndex(self: Windows.UI.Core.ICoreWindowDialog) -> UInt32: ...
    @winrt_mixinmethod
    def put_DefaultCommandIndex(self: Windows.UI.Core.ICoreWindowDialog, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CancelCommandIndex(self: Windows.UI.Core.ICoreWindowDialog) -> UInt32: ...
    @winrt_mixinmethod
    def put_CancelCommandIndex(self: Windows.UI.Core.ICoreWindowDialog, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BackButtonCommand(self: Windows.UI.Core.ICoreWindowDialog) -> Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_BackButtonCommand(self: Windows.UI.Core.ICoreWindowDialog, value: Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def ShowAsync(self: Windows.UI.Core.ICoreWindowDialog) -> Windows.Foundation.IAsyncOperation[Windows.UI.Popups.IUICommand]: ...
    MaxSize = property(get_MaxSize, None)
    MinSize = property(get_MinSize, None)
    Title = property(get_Title, put_Title)
    IsInteractionDelayed = property(get_IsInteractionDelayed, put_IsInteractionDelayed)
    Commands = property(get_Commands, None)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    CancelCommandIndex = property(get_CancelCommandIndex, put_CancelCommandIndex)
    BackButtonCommand = property(get_BackButtonCommand, put_BackButtonCommand)
CoreWindowDialogsContract: UInt32 = 65536
class CoreWindowEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreWindowEventArgs
    _classid_ = 'Windows.UI.Core.CoreWindowEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
CoreWindowFlowDirection = Int32
CoreWindowFlowDirection_LeftToRight: CoreWindowFlowDirection = 0
CoreWindowFlowDirection_RightToLeft: CoreWindowFlowDirection = 1
class CoreWindowFlyout(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreWindowFlyout
    _classid_ = 'Windows.UI.Core.CoreWindowFlyout'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Core.ICoreWindowFlyoutFactory, position: Windows.Foundation.Point) -> Windows.UI.Core.CoreWindowFlyout: ...
    @winrt_factorymethod
    def CreateWithTitle(cls: Windows.UI.Core.ICoreWindowFlyoutFactory, position: Windows.Foundation.Point, title: WinRT_String) -> Windows.UI.Core.CoreWindowFlyout: ...
    @winrt_mixinmethod
    def add_Showing(self: Windows.UI.Core.ICoreWindowFlyout, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CoreWindowPopupShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Showing(self: Windows.UI.Core.ICoreWindowFlyout, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSize(self: Windows.UI.Core.ICoreWindowFlyout) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_MinSize(self: Windows.UI.Core.ICoreWindowFlyout) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.UI.Core.ICoreWindowFlyout) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.UI.Core.ICoreWindowFlyout, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsInteractionDelayed(self: Windows.UI.Core.ICoreWindowFlyout) -> Int32: ...
    @winrt_mixinmethod
    def put_IsInteractionDelayed(self: Windows.UI.Core.ICoreWindowFlyout, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Commands(self: Windows.UI.Core.ICoreWindowFlyout) -> Windows.Foundation.Collections.IVector[Windows.UI.Popups.IUICommand]: ...
    @winrt_mixinmethod
    def get_DefaultCommandIndex(self: Windows.UI.Core.ICoreWindowFlyout) -> UInt32: ...
    @winrt_mixinmethod
    def put_DefaultCommandIndex(self: Windows.UI.Core.ICoreWindowFlyout, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BackButtonCommand(self: Windows.UI.Core.ICoreWindowFlyout) -> Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_BackButtonCommand(self: Windows.UI.Core.ICoreWindowFlyout, value: Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def ShowAsync(self: Windows.UI.Core.ICoreWindowFlyout) -> Windows.Foundation.IAsyncOperation[Windows.UI.Popups.IUICommand]: ...
    MaxSize = property(get_MaxSize, None)
    MinSize = property(get_MinSize, None)
    Title = property(get_Title, put_Title)
    IsInteractionDelayed = property(get_IsInteractionDelayed, put_IsInteractionDelayed)
    Commands = property(get_Commands, None)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    BackButtonCommand = property(get_BackButtonCommand, put_BackButtonCommand)
class CoreWindowPopupShowingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreWindowPopupShowingEventArgs
    _classid_ = 'Windows.UI.Core.CoreWindowPopupShowingEventArgs'
    @winrt_mixinmethod
    def SetDesiredSize(self: Windows.UI.Core.ICoreWindowPopupShowingEventArgs, value: Windows.Foundation.Size) -> Void: ...
class CoreWindowResizeManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ICoreWindowResizeManager
    _classid_ = 'Windows.UI.Core.CoreWindowResizeManager'
    @winrt_mixinmethod
    def NotifyLayoutCompleted(self: Windows.UI.Core.ICoreWindowResizeManager) -> Void: ...
    @winrt_mixinmethod
    def put_ShouldWaitForLayoutCompletion(self: Windows.UI.Core.ICoreWindowResizeManagerLayoutCapability, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldWaitForLayoutCompletion(self: Windows.UI.Core.ICoreWindowResizeManagerLayoutCapability) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Core.ICoreWindowResizeManagerStatics) -> Windows.UI.Core.CoreWindowResizeManager: ...
    ShouldWaitForLayoutCompletion = property(get_ShouldWaitForLayoutCompletion, put_ShouldWaitForLayoutCompletion)
class DispatchedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Core.DispatchedHandler'
    _iid_ = Guid('{d1f276c4-98d8-4636-bf49-eb79507548e9}')
    @winrt_commethod(3)
    def Invoke(self) -> Void: ...
class IAcceleratorKeyEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IAcceleratorKeyEventArgs'
    _iid_ = Guid('{ff1c4c4a-9287-470b-836e-9086e3126ade}')
    @winrt_commethod(6)
    def get_EventType(self) -> Windows.UI.Core.CoreAcceleratorKeyEventType: ...
    @winrt_commethod(7)
    def get_VirtualKey(self) -> Windows.System.VirtualKey: ...
    @winrt_commethod(8)
    def get_KeyStatus(self) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    EventType = property(get_EventType, None)
    VirtualKey = property(get_VirtualKey, None)
    KeyStatus = property(get_KeyStatus, None)
class IAcceleratorKeyEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IAcceleratorKeyEventArgs2'
    _iid_ = Guid('{d300a9f6-2f7e-4873-a555-166e596ee1c5}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IAutomationProviderRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IAutomationProviderRequestedEventArgs'
    _iid_ = Guid('{961ff258-21bf-4b42-a298-fa479d4c52e2}')
    @winrt_commethod(6)
    def get_AutomationProvider(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def put_AutomationProvider(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    AutomationProvider = property(get_AutomationProvider, put_AutomationProvider)
class IBackRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IBackRequestedEventArgs'
    _iid_ = Guid('{d603d28a-e411-4a4e-ba41-6a327a8675bc}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class ICharacterReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICharacterReceivedEventArgs'
    _iid_ = Guid('{c584659f-99b2-4bcc-bd33-04e63f42902e}')
    @winrt_commethod(6)
    def get_KeyCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    KeyCode = property(get_KeyCode, None)
    KeyStatus = property(get_KeyStatus, None)
class IClosestInteractiveBoundsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IClosestInteractiveBoundsRequestedEventArgs'
    _iid_ = Guid('{347c11d7-f6f8-40e3-b29f-ae50d3e86486}')
    @winrt_commethod(6)
    def get_PointerPosition(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_SearchBounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_ClosestInteractiveBounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def put_ClosestInteractiveBounds(self, value: Windows.Foundation.Rect) -> Void: ...
    PointerPosition = property(get_PointerPosition, None)
    SearchBounds = property(get_SearchBounds, None)
    ClosestInteractiveBounds = property(get_ClosestInteractiveBounds, put_ClosestInteractiveBounds)
class ICoreAcceleratorKeys(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreAcceleratorKeys'
    _iid_ = Guid('{9ffdf7f5-b8c9-4ef0-b7d2-1de626561fc8}')
    @winrt_commethod(6)
    def add_AcceleratorKeyActivated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreDispatcher, Windows.UI.Core.AcceleratorKeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AcceleratorKeyActivated(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreClosestInteractiveBoundsRequested(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreClosestInteractiveBoundsRequested'
    _iid_ = Guid('{f303043a-e8bf-4e8e-ae69-c9dadd57a114}')
    @winrt_commethod(6)
    def add_ClosestInteractiveBoundsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreComponentInputSource, Windows.UI.Core.ClosestInteractiveBoundsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ClosestInteractiveBoundsRequested(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreComponentFocusable(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreComponentFocusable'
    _iid_ = Guid('{52f96fa3-8742-4411-ae69-79a85f29ac8b}')
    @winrt_commethod(6)
    def get_HasFocus(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_GotFocus(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.CoreWindowEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_GotFocus(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_LostFocus(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.CoreWindowEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_LostFocus(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    HasFocus = property(get_HasFocus, None)
class ICoreCursor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreCursor'
    _iid_ = Guid('{96893acf-111d-442c-8a77-b87992f8e2d6}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Type(self) -> Windows.UI.Core.CoreCursorType: ...
    Id = property(get_Id, None)
    Type = property(get_Type, None)
class ICoreCursorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreCursorFactory'
    _iid_ = Guid('{f6359621-a79d-4ed3-8c32-a9ef9d6b76a4}')
    @winrt_commethod(6)
    def CreateCursor(self, type: Windows.UI.Core.CoreCursorType, id: UInt32) -> Windows.UI.Core.CoreCursor: ...
class ICoreDispatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreDispatcher'
    _iid_ = Guid('{60db2fa8-b705-4fde-a7d6-ebbb1891d39e}')
    @winrt_commethod(6)
    def get_HasThreadAccess(self) -> Boolean: ...
    @winrt_commethod(7)
    def ProcessEvents(self, options: Windows.UI.Core.CoreProcessEventsOption) -> Void: ...
    @winrt_commethod(8)
    def RunAsync(self, priority: Windows.UI.Core.CoreDispatcherPriority, agileCallback: Windows.UI.Core.DispatchedHandler) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def RunIdleAsync(self, agileCallback: Windows.UI.Core.IdleDispatchedHandler) -> Windows.Foundation.IAsyncAction: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
class ICoreDispatcher2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreDispatcher2'
    _iid_ = Guid('{6f5e63c7-e3aa-4eae-b0e0-dcf321ca4b2f}')
    @winrt_commethod(6)
    def TryRunAsync(self, priority: Windows.UI.Core.CoreDispatcherPriority, agileCallback: Windows.UI.Core.DispatchedHandler) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TryRunIdleAsync(self, agileCallback: Windows.UI.Core.IdleDispatchedHandler) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ICoreDispatcherWithTaskPriority(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreDispatcherWithTaskPriority'
    _iid_ = Guid('{bafaecad-484d-41be-ba80-1d58c65263ea}')
    @winrt_commethod(6)
    def get_CurrentPriority(self) -> Windows.UI.Core.CoreDispatcherPriority: ...
    @winrt_commethod(7)
    def put_CurrentPriority(self, value: Windows.UI.Core.CoreDispatcherPriority) -> Void: ...
    @winrt_commethod(8)
    def ShouldYield(self) -> Boolean: ...
    @winrt_commethod(9)
    def ShouldYieldToPriority(self, priority: Windows.UI.Core.CoreDispatcherPriority) -> Boolean: ...
    @winrt_commethod(10)
    def StopProcessEvents(self) -> Void: ...
    CurrentPriority = property(get_CurrentPriority, put_CurrentPriority)
class ICoreIndependentInputSourceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreIndependentInputSourceController'
    _iid_ = Guid('{0963261c-84fe-578a-83ca-6425309ccde4}')
    @winrt_commethod(6)
    def get_IsTransparentForUncontrolledInput(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsTransparentForUncontrolledInput(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsPalmRejectionEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsPalmRejectionEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_Source(self) -> Windows.UI.Core.CoreIndependentInputSource: ...
    @winrt_commethod(11)
    def SetControlledInput(self, inputTypes: Windows.UI.Core.CoreInputDeviceTypes) -> Void: ...
    @winrt_commethod(12)
    def SetControlledInputWithFilters(self, inputTypes: Windows.UI.Core.CoreInputDeviceTypes, required: Windows.UI.Core.CoreIndependentInputFilters, excluded: Windows.UI.Core.CoreIndependentInputFilters) -> Void: ...
    IsTransparentForUncontrolledInput = property(get_IsTransparentForUncontrolledInput, put_IsTransparentForUncontrolledInput)
    IsPalmRejectionEnabled = property(get_IsPalmRejectionEnabled, put_IsPalmRejectionEnabled)
    Source = property(get_Source, None)
class ICoreIndependentInputSourceControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreIndependentInputSourceControllerStatics'
    _iid_ = Guid('{3edc4e20-9a8a-5691-8586-fca4cb57526d}')
    @winrt_commethod(6)
    def CreateForVisual(self, visual: Windows.UI.Composition.Visual) -> Windows.UI.Core.CoreIndependentInputSourceController: ...
    @winrt_commethod(7)
    def CreateForIVisualElement(self, visualElement: Windows.UI.Composition.IVisualElement) -> Windows.UI.Core.CoreIndependentInputSourceController: ...
class ICoreInputSourceBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreInputSourceBase'
    _iid_ = Guid('{9f488807-4580-4be8-be68-92a9311713bb}')
    @winrt_commethod(6)
    def get_Dispatcher(self) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_commethod(7)
    def get_IsInputEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsInputEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def add_InputEnabled(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.InputEnabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_InputEnabled(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Dispatcher = property(get_Dispatcher, None)
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
class ICoreKeyboardInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreKeyboardInputSource'
    _iid_ = Guid('{231c9088-e469-4df1-b208-6e490d71cb90}')
    @winrt_commethod(6)
    def GetCurrentKeyState(self, virtualKey: Windows.System.VirtualKey) -> Windows.UI.Core.CoreVirtualKeyStates: ...
    @winrt_commethod(7)
    def add_CharacterReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.CharacterReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_CharacterReceived(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_KeyDown(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_KeyDown(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_KeyUp(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_KeyUp(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreKeyboardInputSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreKeyboardInputSource2'
    _iid_ = Guid('{fa24cb94-f963-47a5-8778-207c482b0afd}')
    @winrt_commethod(6)
    def GetCurrentKeyEventDeviceId(self) -> WinRT_String: ...
class ICorePointerInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICorePointerInputSource'
    _iid_ = Guid('{bbf1bb18-e47a-48eb-8807-f8f8d3ea4551}')
    @winrt_commethod(6)
    def ReleasePointerCapture(self) -> Void: ...
    @winrt_commethod(7)
    def SetPointerCapture(self) -> Void: ...
    @winrt_commethod(8)
    def get_HasCapture(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_PointerPosition(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def get_PointerCursor(self) -> Windows.UI.Core.CoreCursor: ...
    @winrt_commethod(11)
    def put_PointerCursor(self, value: Windows.UI.Core.CoreCursor) -> Void: ...
    @winrt_commethod(12)
    def add_PointerCaptureLost(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PointerCaptureLost(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PointerEntered(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PointerEntered(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_PointerExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_PointerExited(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_PointerMoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_PointerMoved(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_PointerPressed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_PointerPressed(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_PointerReleased(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_PointerReleased(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_PointerWheelChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_PointerWheelChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    HasCapture = property(get_HasCapture, None)
    PointerPosition = property(get_PointerPosition, None)
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
class ICorePointerInputSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICorePointerInputSource2'
    _iid_ = Guid('{d703708a-4516-4786-b1e5-2751d563f997}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class ICorePointerRedirector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICorePointerRedirector'
    _iid_ = Guid('{8f9d0c94-5688-4b0c-a9f1-f931f7fa3dc3}')
    @winrt_commethod(6)
    def add_PointerRoutedAway(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PointerRoutedAway(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PointerRoutedTo(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PointerRoutedTo(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PointerRoutedReleased(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.ICorePointerRedirector, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PointerRoutedReleased(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreTouchHitTesting(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreTouchHitTesting'
    _iid_ = Guid('{b1d8a289-3acf-4124-9fa3-ea8aba353c21}')
    @winrt_commethod(6)
    def add_TouchHitTesting(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.UI.Core.TouchHitTestingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_TouchHitTesting(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindow'
    _iid_ = Guid('{79b9d5f2-879e-4b89-b798-79e47598030c}')
    @winrt_commethod(6)
    def get_AutomationHostProvider(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_Bounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_CustomProperties(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def get_Dispatcher(self) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_commethod(10)
    def get_FlowDirection(self) -> Windows.UI.Core.CoreWindowFlowDirection: ...
    @winrt_commethod(11)
    def put_FlowDirection(self, value: Windows.UI.Core.CoreWindowFlowDirection) -> Void: ...
    @winrt_commethod(12)
    def get_IsInputEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsInputEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PointerCursor(self) -> Windows.UI.Core.CoreCursor: ...
    @winrt_commethod(15)
    def put_PointerCursor(self, value: Windows.UI.Core.CoreCursor) -> Void: ...
    @winrt_commethod(16)
    def get_PointerPosition(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(17)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(18)
    def Activate(self) -> Void: ...
    @winrt_commethod(19)
    def Close(self) -> Void: ...
    @winrt_commethod(20)
    def GetAsyncKeyState(self, virtualKey: Windows.System.VirtualKey) -> Windows.UI.Core.CoreVirtualKeyStates: ...
    @winrt_commethod(21)
    def GetKeyState(self, virtualKey: Windows.System.VirtualKey) -> Windows.UI.Core.CoreVirtualKeyStates: ...
    @winrt_commethod(22)
    def ReleasePointerCapture(self) -> Void: ...
    @winrt_commethod(23)
    def SetPointerCapture(self) -> Void: ...
    @winrt_commethod(24)
    def add_Activated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.WindowActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_Activated(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_AutomationProviderRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.AutomationProviderRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_AutomationProviderRequested(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_CharacterReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CharacterReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_CharacterReceived(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CoreWindowEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_Closed(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_InputEnabled(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.InputEnabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_InputEnabled(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_KeyDown(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_KeyDown(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def add_KeyUp(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.KeyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(37)
    def remove_KeyUp(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(38)
    def add_PointerCaptureLost(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(39)
    def remove_PointerCaptureLost(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(40)
    def add_PointerEntered(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(41)
    def remove_PointerEntered(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(42)
    def add_PointerExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(43)
    def remove_PointerExited(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(44)
    def add_PointerMoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(45)
    def remove_PointerMoved(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(46)
    def add_PointerPressed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(47)
    def remove_PointerPressed(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(48)
    def add_PointerReleased(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(49)
    def remove_PointerReleased(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(50)
    def add_TouchHitTesting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.TouchHitTestingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(51)
    def remove_TouchHitTesting(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(52)
    def add_PointerWheelChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(53)
    def remove_PointerWheelChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(54)
    def add_SizeChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.WindowSizeChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(55)
    def remove_SizeChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(56)
    def add_VisibilityChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.VisibilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(57)
    def remove_VisibilityChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutomationHostProvider = property(get_AutomationHostProvider, None)
    Bounds = property(get_Bounds, None)
    CustomProperties = property(get_CustomProperties, None)
    Dispatcher = property(get_Dispatcher, None)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
    PointerPosition = property(get_PointerPosition, None)
    Visible = property(get_Visible, None)
class ICoreWindow2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindow2'
    _iid_ = Guid('{7c2b1b85-6917-4361-9c02-0d9e3a420b95}')
    @winrt_commethod(6)
    def put_PointerPosition(self, value: Windows.Foundation.Point) -> Void: ...
    PointerPosition = property(None, put_PointerPosition)
class ICoreWindow3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindow3'
    _iid_ = Guid('{32c20dd8-faef-4375-a2ab-32640e4815c7}')
    @winrt_commethod(6)
    def add_ClosestInteractiveBoundsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.ClosestInteractiveBoundsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ClosestInteractiveBoundsRequested(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetCurrentKeyEventDeviceId(self) -> WinRT_String: ...
class ICoreWindow4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindow4'
    _iid_ = Guid('{35caf0d0-47f0-436c-af97-0dd88f6f5f02}')
    @winrt_commethod(6)
    def add_ResizeStarted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ResizeStarted(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ResizeCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ResizeCompleted(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreWindow5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindow5'
    _iid_ = Guid('{4b4ae1e1-2e6d-4eaa-bda1-1c5cc1bee141}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    @winrt_commethod(7)
    def get_ActivationMode(self) -> Windows.UI.Core.CoreWindowActivationMode: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
    ActivationMode = property(get_ActivationMode, None)
class ICoreWindowDialog(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowDialog'
    _iid_ = Guid('{e7392ce0-c78d-427e-8b2c-01ff420c69d5}')
    @winrt_commethod(6)
    def add_Showing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CoreWindowPopupShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Showing(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_MaxSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def get_MinSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_IsInteractionDelayed(self) -> Int32: ...
    @winrt_commethod(13)
    def put_IsInteractionDelayed(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_Commands(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Popups.IUICommand]: ...
    @winrt_commethod(15)
    def get_DefaultCommandIndex(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_DefaultCommandIndex(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_CancelCommandIndex(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_CancelCommandIndex(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_BackButtonCommand(self) -> Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_commethod(20)
    def put_BackButtonCommand(self, value: Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_commethod(21)
    def ShowAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.Popups.IUICommand]: ...
    MaxSize = property(get_MaxSize, None)
    MinSize = property(get_MinSize, None)
    Title = property(get_Title, put_Title)
    IsInteractionDelayed = property(get_IsInteractionDelayed, put_IsInteractionDelayed)
    Commands = property(get_Commands, None)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    CancelCommandIndex = property(get_CancelCommandIndex, put_CancelCommandIndex)
    BackButtonCommand = property(get_BackButtonCommand, put_BackButtonCommand)
class ICoreWindowDialogFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowDialogFactory'
    _iid_ = Guid('{cfb2a855-1c59-4b13-b1e5-16e29805f7c4}')
    @winrt_commethod(6)
    def CreateWithTitle(self, title: WinRT_String) -> Windows.UI.Core.CoreWindowDialog: ...
class ICoreWindowEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowEventArgs'
    _iid_ = Guid('{272b1ef3-c633-4da5-a26c-c6d0f56b29da}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class ICoreWindowFlyout(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowFlyout'
    _iid_ = Guid('{e89d854d-2050-40bb-b344-f6f355eeb314}')
    @winrt_commethod(6)
    def add_Showing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Core.CoreWindow, Windows.UI.Core.CoreWindowPopupShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Showing(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_MaxSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def get_MinSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_IsInteractionDelayed(self) -> Int32: ...
    @winrt_commethod(13)
    def put_IsInteractionDelayed(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_Commands(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Popups.IUICommand]: ...
    @winrt_commethod(15)
    def get_DefaultCommandIndex(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_DefaultCommandIndex(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_BackButtonCommand(self) -> Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_commethod(18)
    def put_BackButtonCommand(self, value: Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_commethod(19)
    def ShowAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.Popups.IUICommand]: ...
    MaxSize = property(get_MaxSize, None)
    MinSize = property(get_MinSize, None)
    Title = property(get_Title, put_Title)
    IsInteractionDelayed = property(get_IsInteractionDelayed, put_IsInteractionDelayed)
    Commands = property(get_Commands, None)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    BackButtonCommand = property(get_BackButtonCommand, put_BackButtonCommand)
class ICoreWindowFlyoutFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowFlyoutFactory'
    _iid_ = Guid('{dec4c6c4-93e8-4f7c-be27-cefaa1af68a7}')
    @winrt_commethod(6)
    def Create(self, position: Windows.Foundation.Point) -> Windows.UI.Core.CoreWindowFlyout: ...
    @winrt_commethod(7)
    def CreateWithTitle(self, position: Windows.Foundation.Point, title: WinRT_String) -> Windows.UI.Core.CoreWindowFlyout: ...
class ICoreWindowPopupShowingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowPopupShowingEventArgs'
    _iid_ = Guid('{26155fa2-5ba5-4ea4-a3b4-2dc7d63c8e26}')
    @winrt_commethod(6)
    def SetDesiredSize(self, value: Windows.Foundation.Size) -> Void: ...
class ICoreWindowResizeManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowResizeManager'
    _iid_ = Guid('{b8f0b925-b350-48b3-a198-5c1a84700243}')
    @winrt_commethod(6)
    def NotifyLayoutCompleted(self) -> Void: ...
class ICoreWindowResizeManagerLayoutCapability(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowResizeManagerLayoutCapability'
    _iid_ = Guid('{bb74f27b-a544-4301-80e6-0ae033ef4536}')
    @winrt_commethod(6)
    def put_ShouldWaitForLayoutCompletion(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_ShouldWaitForLayoutCompletion(self) -> Boolean: ...
    ShouldWaitForLayoutCompletion = property(get_ShouldWaitForLayoutCompletion, put_ShouldWaitForLayoutCompletion)
class ICoreWindowResizeManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowResizeManagerStatics'
    _iid_ = Guid('{ae4a9045-6d70-49db-8e68-46ffbd17d38d}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Core.CoreWindowResizeManager: ...
class ICoreWindowStatic(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowStatic'
    _iid_ = Guid('{4d239005-3c2a-41b1-9022-536bb9cf93b1}')
    @winrt_commethod(6)
    def GetForCurrentThread(self) -> Windows.UI.Core.CoreWindow: ...
class ICoreWindowWithContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ICoreWindowWithContext'
    _iid_ = Guid('{9ac40241-3575-4c3b-af66-e8c529d4d06c}')
    @winrt_commethod(6)
    def get_UIContext(self) -> Windows.UI.UIContext: ...
    UIContext = property(get_UIContext, None)
class IIdleDispatchedHandlerArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IIdleDispatchedHandlerArgs'
    _iid_ = Guid('{98bb6a24-dc1c-43cb-b4ed-d1c0eb2391f3}')
    @winrt_commethod(6)
    def get_IsDispatcherIdle(self) -> Boolean: ...
    IsDispatcherIdle = property(get_IsDispatcherIdle, None)
class IInitializeWithCoreWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IInitializeWithCoreWindow'
    _iid_ = Guid('{188f20d6-9873-464a-ace5-57e010f465e6}')
    @winrt_commethod(6)
    def Initialize(self, window: Windows.UI.Core.CoreWindow) -> Void: ...
class IInputEnabledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IInputEnabledEventArgs'
    _iid_ = Guid('{80371d4f-2fd8-4c24-aa86-3163a87b4e5a}')
    @winrt_commethod(6)
    def get_InputEnabled(self) -> Boolean: ...
    InputEnabled = property(get_InputEnabled, None)
class IKeyEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IKeyEventArgs'
    _iid_ = Guid('{5ff5e930-2544-4a17-bd78-1f2fdebb106b}')
    @winrt_commethod(6)
    def get_VirtualKey(self) -> Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    VirtualKey = property(get_VirtualKey, None)
    KeyStatus = property(get_KeyStatus, None)
class IKeyEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IKeyEventArgs2'
    _iid_ = Guid('{583add98-0790-4571-9b12-645ef9d79e42}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IPointerEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IPointerEventArgs'
    _iid_ = Guid('{920d9cb1-a5fc-4a21-8c09-49dfe6ffe25f}')
    @winrt_commethod(6)
    def get_CurrentPoint(self) -> Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(7)
    def get_KeyModifiers(self) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(8)
    def GetIntermediatePoints(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
    CurrentPoint = property(get_CurrentPoint, None)
    KeyModifiers = property(get_KeyModifiers, None)
class ISystemNavigationManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ISystemNavigationManager'
    _iid_ = Guid('{93023118-cf50-42a6-9706-69107fa122e1}')
    @winrt_commethod(6)
    def add_BackRequested(self, handler: Windows.Foundation.EventHandler[Windows.UI.Core.BackRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BackRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISystemNavigationManager2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ISystemNavigationManager2'
    _iid_ = Guid('{8c510401-67be-49ae-9509-671c1e54a389}')
    @winrt_commethod(6)
    def get_AppViewBackButtonVisibility(self) -> Windows.UI.Core.AppViewBackButtonVisibility: ...
    @winrt_commethod(7)
    def put_AppViewBackButtonVisibility(self, value: Windows.UI.Core.AppViewBackButtonVisibility) -> Void: ...
    AppViewBackButtonVisibility = property(get_AppViewBackButtonVisibility, put_AppViewBackButtonVisibility)
class ISystemNavigationManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ISystemNavigationManagerStatics'
    _iid_ = Guid('{dc52b5ce-bee0-4305-8c54-68228ed683b5}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Core.SystemNavigationManager: ...
class ITouchHitTestingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.ITouchHitTestingEventArgs'
    _iid_ = Guid('{22f3b823-0b7c-424e-9df7-33d4f962931b}')
    @winrt_commethod(6)
    def get_ProximityEvaluation(self) -> Windows.UI.Core.CoreProximityEvaluation: ...
    @winrt_commethod(7)
    def put_ProximityEvaluation(self, value: Windows.UI.Core.CoreProximityEvaluation) -> Void: ...
    @winrt_commethod(8)
    def get_Point(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_BoundingBox(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def EvaluateProximityToRect(self, controlBoundingBox: Windows.Foundation.Rect) -> Windows.UI.Core.CoreProximityEvaluation: ...
    @winrt_commethod(11)
    def EvaluateProximityToPolygon(self, controlVertices: POINTER(Windows.Foundation.Point_head)) -> Windows.UI.Core.CoreProximityEvaluation: ...
    ProximityEvaluation = property(get_ProximityEvaluation, put_ProximityEvaluation)
    Point = property(get_Point, None)
    BoundingBox = property(get_BoundingBox, None)
class IVisibilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IVisibilityChangedEventArgs'
    _iid_ = Guid('{bf9918ea-d801-4564-a495-b1e84f8ad085}')
    @winrt_commethod(6)
    def get_Visible(self) -> Boolean: ...
    Visible = property(get_Visible, None)
class IWindowActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IWindowActivatedEventArgs'
    _iid_ = Guid('{179d65e7-4658-4cb6-aa13-41d094ea255e}')
    @winrt_commethod(6)
    def get_WindowActivationState(self) -> Windows.UI.Core.CoreWindowActivationState: ...
    WindowActivationState = property(get_WindowActivationState, None)
class IWindowSizeChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.IWindowSizeChangedEventArgs'
    _iid_ = Guid('{5a200ec7-0426-47dc-b86c-6f475915e451}')
    @winrt_commethod(6)
    def get_Size(self) -> Windows.Foundation.Size: ...
    Size = property(get_Size, None)
class IdleDispatchedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Core.IdleDispatchedHandler'
    _iid_ = Guid('{a42b0c24-7f21-4abc-99c1-8f01007f0880}')
    @winrt_commethod(3)
    def Invoke(self, e: Windows.UI.Core.IdleDispatchedHandlerArgs) -> Void: ...
class IdleDispatchedHandlerArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IIdleDispatchedHandlerArgs
    _classid_ = 'Windows.UI.Core.IdleDispatchedHandlerArgs'
    @winrt_mixinmethod
    def get_IsDispatcherIdle(self: Windows.UI.Core.IIdleDispatchedHandlerArgs) -> Boolean: ...
    IsDispatcherIdle = property(get_IsDispatcherIdle, None)
class InputEnabledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IInputEnabledEventArgs
    _classid_ = 'Windows.UI.Core.InputEnabledEventArgs'
    @winrt_mixinmethod
    def get_InputEnabled(self: Windows.UI.Core.IInputEnabledEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    InputEnabled = property(get_InputEnabled, None)
    Handled = property(get_Handled, put_Handled)
class KeyEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IKeyEventArgs
    _classid_ = 'Windows.UI.Core.KeyEventArgs'
    @winrt_mixinmethod
    def get_VirtualKey(self: Windows.UI.Core.IKeyEventArgs) -> Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: Windows.UI.Core.IKeyEventArgs) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.UI.Core.IKeyEventArgs2) -> WinRT_String: ...
    VirtualKey = property(get_VirtualKey, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
    DeviceId = property(get_DeviceId, None)
class PointerEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IPointerEventArgs
    _classid_ = 'Windows.UI.Core.PointerEventArgs'
    @winrt_mixinmethod
    def get_CurrentPoint(self: Windows.UI.Core.IPointerEventArgs) -> Windows.UI.Input.PointerPoint: ...
    @winrt_mixinmethod
    def get_KeyModifiers(self: Windows.UI.Core.IPointerEventArgs) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def GetIntermediatePoints(self: Windows.UI.Core.IPointerEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    CurrentPoint = property(get_CurrentPoint, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Handled = property(get_Handled, put_Handled)
class SystemNavigationManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ISystemNavigationManager
    _classid_ = 'Windows.UI.Core.SystemNavigationManager'
    @winrt_mixinmethod
    def add_BackRequested(self: Windows.UI.Core.ISystemNavigationManager, handler: Windows.Foundation.EventHandler[Windows.UI.Core.BackRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BackRequested(self: Windows.UI.Core.ISystemNavigationManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AppViewBackButtonVisibility(self: Windows.UI.Core.ISystemNavigationManager2) -> Windows.UI.Core.AppViewBackButtonVisibility: ...
    @winrt_mixinmethod
    def put_AppViewBackButtonVisibility(self: Windows.UI.Core.ISystemNavigationManager2, value: Windows.UI.Core.AppViewBackButtonVisibility) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Core.ISystemNavigationManagerStatics) -> Windows.UI.Core.SystemNavigationManager: ...
    AppViewBackButtonVisibility = property(get_AppViewBackButtonVisibility, put_AppViewBackButtonVisibility)
class TouchHitTestingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.ITouchHitTestingEventArgs
    _classid_ = 'Windows.UI.Core.TouchHitTestingEventArgs'
    @winrt_mixinmethod
    def get_ProximityEvaluation(self: Windows.UI.Core.ITouchHitTestingEventArgs) -> Windows.UI.Core.CoreProximityEvaluation: ...
    @winrt_mixinmethod
    def put_ProximityEvaluation(self: Windows.UI.Core.ITouchHitTestingEventArgs, value: Windows.UI.Core.CoreProximityEvaluation) -> Void: ...
    @winrt_mixinmethod
    def get_Point(self: Windows.UI.Core.ITouchHitTestingEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BoundingBox(self: Windows.UI.Core.ITouchHitTestingEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def EvaluateProximityToRect(self: Windows.UI.Core.ITouchHitTestingEventArgs, controlBoundingBox: Windows.Foundation.Rect) -> Windows.UI.Core.CoreProximityEvaluation: ...
    @winrt_mixinmethod
    def EvaluateProximityToPolygon(self: Windows.UI.Core.ITouchHitTestingEventArgs, controlVertices: POINTER(Windows.Foundation.Point_head)) -> Windows.UI.Core.CoreProximityEvaluation: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    ProximityEvaluation = property(get_ProximityEvaluation, put_ProximityEvaluation)
    Point = property(get_Point, None)
    BoundingBox = property(get_BoundingBox, None)
    Handled = property(get_Handled, put_Handled)
class VisibilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IVisibilityChangedEventArgs
    _classid_ = 'Windows.UI.Core.VisibilityChangedEventArgs'
    @winrt_mixinmethod
    def get_Visible(self: Windows.UI.Core.IVisibilityChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    Visible = property(get_Visible, None)
    Handled = property(get_Handled, put_Handled)
class WindowActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IWindowActivatedEventArgs
    _classid_ = 'Windows.UI.Core.WindowActivatedEventArgs'
    @winrt_mixinmethod
    def get_WindowActivationState(self: Windows.UI.Core.IWindowActivatedEventArgs) -> Windows.UI.Core.CoreWindowActivationState: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    WindowActivationState = property(get_WindowActivationState, None)
    Handled = property(get_Handled, put_Handled)
class WindowSizeChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.IWindowSizeChangedEventArgs
    _classid_ = 'Windows.UI.Core.WindowSizeChangedEventArgs'
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Core.IWindowSizeChangedEventArgs) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.ICoreWindowEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.ICoreWindowEventArgs, value: Boolean) -> Void: ...
    Size = property(get_Size, None)
    Handled = property(get_Handled, put_Handled)
make_head(_module, 'AcceleratorKeyEventArgs')
make_head(_module, 'AutomationProviderRequestedEventArgs')
make_head(_module, 'BackRequestedEventArgs')
make_head(_module, 'CharacterReceivedEventArgs')
make_head(_module, 'ClosestInteractiveBoundsRequestedEventArgs')
make_head(_module, 'CoreAcceleratorKeys')
make_head(_module, 'CoreComponentInputSource')
make_head(_module, 'CoreCursor')
make_head(_module, 'CoreDispatcher')
make_head(_module, 'CoreIndependentInputSource')
make_head(_module, 'CoreIndependentInputSourceController')
make_head(_module, 'CorePhysicalKeyStatus')
make_head(_module, 'CoreProximityEvaluation')
make_head(_module, 'CoreWindow')
make_head(_module, 'CoreWindowDialog')
make_head(_module, 'CoreWindowEventArgs')
make_head(_module, 'CoreWindowFlyout')
make_head(_module, 'CoreWindowPopupShowingEventArgs')
make_head(_module, 'CoreWindowResizeManager')
make_head(_module, 'DispatchedHandler')
make_head(_module, 'IAcceleratorKeyEventArgs')
make_head(_module, 'IAcceleratorKeyEventArgs2')
make_head(_module, 'IAutomationProviderRequestedEventArgs')
make_head(_module, 'IBackRequestedEventArgs')
make_head(_module, 'ICharacterReceivedEventArgs')
make_head(_module, 'IClosestInteractiveBoundsRequestedEventArgs')
make_head(_module, 'ICoreAcceleratorKeys')
make_head(_module, 'ICoreClosestInteractiveBoundsRequested')
make_head(_module, 'ICoreComponentFocusable')
make_head(_module, 'ICoreCursor')
make_head(_module, 'ICoreCursorFactory')
make_head(_module, 'ICoreDispatcher')
make_head(_module, 'ICoreDispatcher2')
make_head(_module, 'ICoreDispatcherWithTaskPriority')
make_head(_module, 'ICoreIndependentInputSourceController')
make_head(_module, 'ICoreIndependentInputSourceControllerStatics')
make_head(_module, 'ICoreInputSourceBase')
make_head(_module, 'ICoreKeyboardInputSource')
make_head(_module, 'ICoreKeyboardInputSource2')
make_head(_module, 'ICorePointerInputSource')
make_head(_module, 'ICorePointerInputSource2')
make_head(_module, 'ICorePointerRedirector')
make_head(_module, 'ICoreTouchHitTesting')
make_head(_module, 'ICoreWindow')
make_head(_module, 'ICoreWindow2')
make_head(_module, 'ICoreWindow3')
make_head(_module, 'ICoreWindow4')
make_head(_module, 'ICoreWindow5')
make_head(_module, 'ICoreWindowDialog')
make_head(_module, 'ICoreWindowDialogFactory')
make_head(_module, 'ICoreWindowEventArgs')
make_head(_module, 'ICoreWindowFlyout')
make_head(_module, 'ICoreWindowFlyoutFactory')
make_head(_module, 'ICoreWindowPopupShowingEventArgs')
make_head(_module, 'ICoreWindowResizeManager')
make_head(_module, 'ICoreWindowResizeManagerLayoutCapability')
make_head(_module, 'ICoreWindowResizeManagerStatics')
make_head(_module, 'ICoreWindowStatic')
make_head(_module, 'ICoreWindowWithContext')
make_head(_module, 'IIdleDispatchedHandlerArgs')
make_head(_module, 'IInitializeWithCoreWindow')
make_head(_module, 'IInputEnabledEventArgs')
make_head(_module, 'IKeyEventArgs')
make_head(_module, 'IKeyEventArgs2')
make_head(_module, 'IPointerEventArgs')
make_head(_module, 'ISystemNavigationManager')
make_head(_module, 'ISystemNavigationManager2')
make_head(_module, 'ISystemNavigationManagerStatics')
make_head(_module, 'ITouchHitTestingEventArgs')
make_head(_module, 'IVisibilityChangedEventArgs')
make_head(_module, 'IWindowActivatedEventArgs')
make_head(_module, 'IWindowSizeChangedEventArgs')
make_head(_module, 'IdleDispatchedHandler')
make_head(_module, 'IdleDispatchedHandlerArgs')
make_head(_module, 'InputEnabledEventArgs')
make_head(_module, 'KeyEventArgs')
make_head(_module, 'PointerEventArgs')
make_head(_module, 'SystemNavigationManager')
make_head(_module, 'TouchHitTestingEventArgs')
make_head(_module, 'VisibilityChangedEventArgs')
make_head(_module, 'WindowActivatedEventArgs')
make_head(_module, 'WindowSizeChangedEventArgs')
