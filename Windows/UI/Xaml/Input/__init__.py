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
import Windows.Devices.Input
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.System
import Windows.UI.Core
import Windows.UI.Input
import Windows.UI.Xaml
import Windows.UI.Xaml.Controls
import Windows.UI.Xaml.Input
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AccessKeyDisplayDismissedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs: ...
class AccessKeyDisplayRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_PressedKeys(self: Windows.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs) -> WinRT_String: ...
    PressedKeys = property(get_PressedKeys, None)
class AccessKeyInvokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IAccessKeyInvokedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IAccessKeyInvokedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class AccessKeyManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.AccessKeyManager'
    @winrt_classmethod
    def get_AreKeyTipsEnabled(cls: Windows.UI.Xaml.Input.IAccessKeyManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def put_AreKeyTipsEnabled(cls: Windows.UI.Xaml.Input.IAccessKeyManagerStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsDisplayModeEnabled(cls: Windows.UI.Xaml.Input.IAccessKeyManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def add_IsDisplayModeEnabledChanged(cls: Windows.UI.Xaml.Input.IAccessKeyManagerStatics, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_IsDisplayModeEnabledChanged(cls: Windows.UI.Xaml.Input.IAccessKeyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def ExitDisplayMode(cls: Windows.UI.Xaml.Input.IAccessKeyManagerStatics) -> Void: ...
    AreKeyTipsEnabled = property(get_AreKeyTipsEnabled, put_AreKeyTipsEnabled)
    IsDisplayModeEnabled = property(get_IsDisplayModeEnabled, None)
class CanExecuteRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.CanExecuteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Parameter(self: Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_CanExecute(self: Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanExecute(self: Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs, value: Boolean) -> Void: ...
    Parameter = property(get_Parameter, None)
    CanExecute = property(get_CanExecute, put_CanExecute)
class CharacterReceivedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.CharacterReceivedRoutedEventArgs'
    @winrt_mixinmethod
    def get_Character(self: Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> Char: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs, value: Boolean) -> Void: ...
    Character = property(get_Character, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
class ContextRequestedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.ContextRequestedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.ContextRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IContextRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IContextRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryGetPosition(self: Windows.UI.Xaml.Input.IContextRequestedEventArgs, relativeTo: Windows.UI.Xaml.UIElement, point: POINTER(Windows.Foundation.Point_head)) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class DoubleTappedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('3124d025-04a7-4d45-82-5e-82-04-a6-24-db-f4')
    ClassId = 'Windows.UI.Xaml.Input.DoubleTappedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs) -> Void: ...
class DoubleTappedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class ExecuteRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.ExecuteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Parameter(self: Windows.UI.Xaml.Input.IExecuteRequestedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Parameter = property(get_Parameter, None)
class FindNextElementOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.FindNextElementOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.FindNextElementOptions: ...
    @winrt_mixinmethod
    def get_SearchRoot(self: Windows.UI.Xaml.Input.IFindNextElementOptions) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_SearchRoot(self: Windows.UI.Xaml.Input.IFindNextElementOptions, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExclusionRect(self: Windows.UI.Xaml.Input.IFindNextElementOptions) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_ExclusionRect(self: Windows.UI.Xaml.Input.IFindNextElementOptions, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_HintRect(self: Windows.UI.Xaml.Input.IFindNextElementOptions) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_HintRect(self: Windows.UI.Xaml.Input.IFindNextElementOptions, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusNavigationStrategyOverride(self: Windows.UI.Xaml.Input.IFindNextElementOptions) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride: ...
    @winrt_mixinmethod
    def put_XYFocusNavigationStrategyOverride(self: Windows.UI.Xaml.Input.IFindNextElementOptions, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride) -> Void: ...
    SearchRoot = property(get_SearchRoot, put_SearchRoot)
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    HintRect = property(get_HintRect, put_HintRect)
    XYFocusNavigationStrategyOverride = property(get_XYFocusNavigationStrategyOverride, put_XYFocusNavigationStrategyOverride)
FocusInputDeviceKind = Int32
FocusInputDeviceKind_None: FocusInputDeviceKind = 0
FocusInputDeviceKind_Mouse: FocusInputDeviceKind = 1
FocusInputDeviceKind_Touch: FocusInputDeviceKind = 2
FocusInputDeviceKind_Pen: FocusInputDeviceKind = 3
FocusInputDeviceKind_Keyboard: FocusInputDeviceKind = 4
FocusInputDeviceKind_GameController: FocusInputDeviceKind = 5
class FocusManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.FocusManager'
    @winrt_classmethod
    def GetFocusedElement(cls: Windows.UI.Xaml.Input.IFocusManagerStatics7, xamlRoot: Windows.UI.Xaml.XamlRoot) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def add_GotFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.FocusManagerGotFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GotFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LostFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.FocusManagerLostFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LostFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GettingFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GettingFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LosingFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LosingFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryFocusAsync(cls: Windows.UI.Xaml.Input.IFocusManagerStatics5, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.FocusState) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusAsync(cls: Windows.UI.Xaml.Input.IFocusManagerStatics5, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusWithOptionsAsync(cls: Windows.UI.Xaml.Input.IFocusManagerStatics5, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: Windows.UI.Xaml.Input.FindNextElementOptions) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusWithOptions(cls: Windows.UI.Xaml.Input.IFocusManagerStatics4, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: Windows.UI.Xaml.Input.FindNextElementOptions) -> Boolean: ...
    @winrt_classmethod
    def FindNextElement(cls: Windows.UI.Xaml.Input.IFocusManagerStatics4, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindFirstFocusableElement(cls: Windows.UI.Xaml.Input.IFocusManagerStatics4, searchScope: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindLastFocusableElement(cls: Windows.UI.Xaml.Input.IFocusManagerStatics4, searchScope: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindNextElementWithOptions(cls: Windows.UI.Xaml.Input.IFocusManagerStatics4, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: Windows.UI.Xaml.Input.FindNextElementOptions) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindNextFocusableElement(cls: Windows.UI.Xaml.Input.IFocusManagerStatics3, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def FindNextFocusableElementWithHint(cls: Windows.UI.Xaml.Input.IFocusManagerStatics3, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, hintRect: Windows.Foundation.Rect) -> Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def TryMoveFocus(cls: Windows.UI.Xaml.Input.IFocusManagerStatics2, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Boolean: ...
    @winrt_classmethod
    def GetFocusedElement(cls: Windows.UI.Xaml.Input.IFocusManagerStatics7) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class FocusManagerGotFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.FocusManagerGotFocusEventArgs'
    @winrt_mixinmethod
    def get_NewFocusedElement(self: Windows.UI.Xaml.Input.IFocusManagerGotFocusEventArgs) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.UI.Xaml.Input.IFocusManagerGotFocusEventArgs) -> Guid: ...
    NewFocusedElement = property(get_NewFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class FocusManagerLostFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.FocusManagerLostFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class FocusMovementResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.FocusMovementResult'
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.UI.Xaml.Input.IFocusMovementResult) -> Boolean: ...
    Succeeded = property(get_Succeeded, None)
FocusNavigationDirection = Int32
FocusNavigationDirection_Next: FocusNavigationDirection = 0
FocusNavigationDirection_Previous: FocusNavigationDirection = 1
FocusNavigationDirection_Up: FocusNavigationDirection = 2
FocusNavigationDirection_Down: FocusNavigationDirection = 3
FocusNavigationDirection_Left: FocusNavigationDirection = 4
FocusNavigationDirection_Right: FocusNavigationDirection = 5
FocusNavigationDirection_None: FocusNavigationDirection = 6
class GettingFocusEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.GettingFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_NewFocusedElement(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_NewFocusedElement(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_FocusState(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Windows.UI.Xaml.FocusState: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_mixinmethod
    def get_Cancel(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryCancel(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetNewFocusedElement(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs2, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.UI.Xaml.Input.IGettingFocusEventArgs3) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    FocusState = property(get_FocusState, None)
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
class HoldingEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('ecae8ccd-8e5e-4fbe-98-46-30-a6-37-0a-fc-df')
    ClassId = 'Windows.UI.Xaml.Input.HoldingEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.HoldingRoutedEventArgs) -> Void: ...
class HoldingRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.HoldingRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.HoldingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.IHoldingRoutedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_HoldingState(self: Windows.UI.Xaml.Input.IHoldingRoutedEventArgs) -> Windows.UI.Input.HoldingState: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IHoldingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IHoldingRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: Windows.UI.Xaml.Input.IHoldingRoutedEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    HoldingState = property(get_HoldingState, None)
    Handled = property(get_Handled, put_Handled)
class IAccessKeyDisplayDismissedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8a610dc6-d72d-4ca8-9f-66-55-6f-35-b5-13-da')
class IAccessKeyDisplayRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0c079e55-13fe-4d03-a6-1d-e1-2f-06-56-72-86')
    @winrt_commethod(6)
    def get_PressedKeys(self) -> WinRT_String: ...
    PressedKeys = property(get_PressedKeys, None)
class IAccessKeyInvokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cfe9cd97-c718-4091-b7-dd-ad-f1-c0-72-b1-e1')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class IAccessKeyManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ecc973b0-2ee9-4b1c-98-d7-6e-0e-81-6d-33-4b')
class IAccessKeyManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4ca0efe6-d9c8-4ebc-b4-c7-30-d1-83-8a-81-f1')
    @winrt_commethod(6)
    def get_IsDisplayModeEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsDisplayModeEnabledChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsDisplayModeEnabledChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def ExitDisplayMode(self) -> Void: ...
    IsDisplayModeEnabled = property(get_IsDisplayModeEnabled, None)
class IAccessKeyManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('962bb594-2ab3-47c5-95-4b-70-92-f3-55-f7-97')
    @winrt_commethod(6)
    def get_AreKeyTipsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreKeyTipsEnabled(self, value: Boolean) -> Void: ...
    AreKeyTipsEnabled = property(get_AreKeyTipsEnabled, put_AreKeyTipsEnabled)
class ICanExecuteRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c8e75256-1950-505d-99-3b-75-90-7e-f9-68-30')
    @winrt_commethod(6)
    def get_Parameter(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_CanExecute(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_CanExecute(self, value: Boolean) -> Void: ...
    Parameter = property(get_Parameter, None)
    CanExecute = property(get_CanExecute, put_CanExecute)
class ICharacterReceivedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7849fd82-48e4-444d-94-19-93-ab-88-92-c1-07')
    @winrt_commethod(6)
    def get_Character(self) -> Char: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Character = property(get_Character, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
class ICommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e5af3542-ca67-4081-99-5b-70-9d-d1-37-92-df')
    @winrt_commethod(6)
    def add_CanExecuteChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CanExecuteChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def CanExecute(self, parameter: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_commethod(9)
    def Execute(self, parameter: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class IContextRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('42618e0a-1cb6-46fb-83-74-0a-ec-68-aa-5e-51')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def TryGetPosition(self, relativeTo: Windows.UI.Xaml.UIElement, point: POINTER(Windows.Foundation.Point_head)) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class IDoubleTappedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('af404424-26df-44f4-87-14-93-59-24-9b-62-d3')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class IExecuteRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e07fa734-a0b6-5755-9e-87-24-f5-4c-ca-93-72')
    @winrt_commethod(6)
    def get_Parameter(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Parameter = property(get_Parameter, None)
class IFindNextElementOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d88ae22b-46c2-41fc-89-7e-b5-96-19-77-b8-9d')
    @winrt_commethod(6)
    def get_SearchRoot(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def put_SearchRoot(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(8)
    def get_ExclusionRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def put_ExclusionRect(self, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(10)
    def get_HintRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_HintRect(self, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(12)
    def get_XYFocusNavigationStrategyOverride(self) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride: ...
    @winrt_commethod(13)
    def put_XYFocusNavigationStrategyOverride(self, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride) -> Void: ...
    SearchRoot = property(get_SearchRoot, put_SearchRoot)
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    HintRect = property(get_HintRect, put_HintRect)
    XYFocusNavigationStrategyOverride = property(get_XYFocusNavigationStrategyOverride, put_XYFocusNavigationStrategyOverride)
class IFocusManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c843f50b-3b83-4da1-9d-6f-55-7c-11-69-f3-41')
class IFocusManagerGotFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('97aa5d83-535b-507a-86-8e-62-b7-06-f0-6b-61')
    @winrt_commethod(6)
    def get_NewFocusedElement(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_CorrelationId(self) -> Guid: ...
    NewFocusedElement = property(get_NewFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class IFocusManagerLostFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3e157e7a-9578-5cd3-aa-a8-05-1b-3d-39-19-78')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_CorrelationId(self) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class IFocusManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1eccd326-8182-4482-82-6a-09-18-e9-ed-9a-f7')
    @winrt_commethod(6)
    def GetFocusedElement(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IFocusManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a920d761-dd87-4f31-be-da-ef-41-7f-e7-c0-4a')
    @winrt_commethod(6)
    def TryMoveFocus(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Boolean: ...
class IFocusManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('60805ebf-b149-417d-83-f1-ba-eb-56-0e-2a-47')
    @winrt_commethod(6)
    def FindNextFocusableElement(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def FindNextFocusableElementWithHint(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, hintRect: Windows.Foundation.Rect) -> Windows.UI.Xaml.UIElement: ...
class IFocusManagerStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('29276e9c-1c6c-414a-ba-1c-96-ef-d5-96-2b-cd')
    @winrt_commethod(6)
    def TryMoveFocusWithOptions(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: Windows.UI.Xaml.Input.FindNextElementOptions) -> Boolean: ...
    @winrt_commethod(7)
    def FindNextElement(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def FindFirstFocusableElement(self, searchScope: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def FindLastFocusableElement(self, searchScope: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(10)
    def FindNextElementWithOptions(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: Windows.UI.Xaml.Input.FindNextElementOptions) -> Windows.UI.Xaml.DependencyObject: ...
class IFocusManagerStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('280edc61-207a-4d7b-b9-8f-ce-16-5e-1b-20-15')
    @winrt_commethod(6)
    def TryFocusAsync(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.FocusState) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_commethod(7)
    def TryMoveFocusAsync(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_commethod(8)
    def TryMoveFocusWithOptionsAsync(self, focusNavigationDirection: Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: Windows.UI.Xaml.Input.FindNextElementOptions) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Input.FocusMovementResult]: ...
class IFocusManagerStatics6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3546a1b6-20bf-5007-92-9d-e6-d3-2e-16-af-e4')
    @winrt_commethod(6)
    def add_GotFocus(self, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.FocusManagerGotFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GotFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_LostFocus(self, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.FocusManagerLostFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LostFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_GettingFocus(self, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_GettingFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_LosingFocus(self, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_LosingFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IFocusManagerStatics7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('95d6fa97-f0fc-5c32-b2-9d-07-c0-4e-c9-66-b0')
    @winrt_commethod(6)
    def GetFocusedElement(self, xamlRoot: Windows.UI.Xaml.XamlRoot) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IFocusMovementResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('06dfead3-c2ae-44bb-bf-ab-9c-73-de-84-07-a4')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    Succeeded = property(get_Succeeded, None)
class IGettingFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fa05b9ce-c67c-4be8-8f-d4-c4-4d-67-87-7e-0d')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_NewFocusedElement(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def put_NewFocusedElement(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(9)
    def get_FocusState(self) -> Windows.UI.Xaml.FocusState: ...
    @winrt_commethod(10)
    def get_Direction(self) -> Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_InputDevice(self) -> Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_commethod(14)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_Cancel(self, value: Boolean) -> Void: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    FocusState = property(get_FocusState, None)
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    Cancel = property(get_Cancel, put_Cancel)
class IGettingFocusEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('88754d7b-b4b9-4959-8b-ce-89-bf-21-2e-d4-eb')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetNewFocusedElement(self, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
class IGettingFocusEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4e024891-db3f-5e78-b7-5a-62-bf-c3-51-07-35')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
class IHoldingRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c246ff23-d80d-44de-8d-b9-0d-81-5e-26-9a-c0')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_HoldingState(self) -> Windows.UI.Input.HoldingState: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetPosition(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    HoldingState = property(get_HoldingState, None)
    Handled = property(get_Handled, put_Handled)
class IInertiaExpansionBehavior(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('751d87e5-8d42-44c5-96-5e-3c-d3-0c-c9-d6-f7')
    @winrt_commethod(6)
    def get_DesiredDeceleration(self) -> Double: ...
    @winrt_commethod(7)
    def put_DesiredDeceleration(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredExpansion(self) -> Double: ...
    @winrt_commethod(9)
    def put_DesiredExpansion(self, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredExpansion = property(get_DesiredExpansion, put_DesiredExpansion)
class IInertiaRotationBehavior(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('424cfb2e-bbfd-4625-ae-78-20-c6-5b-f1-ef-af')
    @winrt_commethod(6)
    def get_DesiredDeceleration(self) -> Double: ...
    @winrt_commethod(7)
    def put_DesiredDeceleration(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredRotation(self) -> Double: ...
    @winrt_commethod(9)
    def put_DesiredRotation(self, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredRotation = property(get_DesiredRotation, put_DesiredRotation)
class IInertiaTranslationBehavior(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('45d3a512-3b32-4882-a4-c2-ec-fa-2d-4b-6d-f0')
    @winrt_commethod(6)
    def get_DesiredDeceleration(self) -> Double: ...
    @winrt_commethod(7)
    def put_DesiredDeceleration(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredDisplacement(self) -> Double: ...
    @winrt_commethod(9)
    def put_DesiredDisplacement(self, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredDisplacement = property(get_DesiredDisplacement, put_DesiredDisplacement)
class IInputScope(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5c0f85f3-f9d8-4220-b6-66-04-5d-07-4d-9b-fa')
    @winrt_commethod(6)
    def get_Names(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Input.InputScopeName]: ...
    Names = property(get_Names, None)
class IInputScopeName(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fd3e6997-08fb-4cba-a0-21-79-2d-75-89-fd-5a')
    @winrt_commethod(6)
    def get_NameValue(self) -> Windows.UI.Xaml.Input.InputScopeNameValue: ...
    @winrt_commethod(7)
    def put_NameValue(self, value: Windows.UI.Xaml.Input.InputScopeNameValue) -> Void: ...
    NameValue = property(get_NameValue, put_NameValue)
class IInputScopeNameFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4a40bb52-4bd7-4e54-86-17-1c-da-8a-1e-da-7f')
    @winrt_commethod(6)
    def CreateInstance(self, nameValue: Windows.UI.Xaml.Input.InputScopeNameValue) -> Windows.UI.Xaml.Input.InputScopeName: ...
class IKeyRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d4cd3dfe-4079-42e9-a3-9a-30-95-d3-f0-49-c6')
    @winrt_commethod(6)
    def get_Key(self) -> Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Key = property(get_Key, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
class IKeyRoutedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1b02d57a-9634-4f14-91-b2-13-3e-42-fd-b3-cd')
    @winrt_commethod(6)
    def get_OriginalKey(self) -> Windows.System.VirtualKey: ...
    OriginalKey = property(get_OriginalKey, None)
class IKeyRoutedEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2779f5b4-ca41-411b-a8-ef-f4-fc-78-e7-80-57')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IKeyboardAccelerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('92e6181e-19ae-465a-9b-3c-a7-1e-e9-ea-74-20')
    @winrt_commethod(6)
    def get_Key(self) -> Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def put_Key(self, value: Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(8)
    def get_Modifiers(self) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(9)
    def put_Modifiers(self, value: Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(10)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_ScopeOwner(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ScopeOwner(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def add_Invoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Input.KeyboardAccelerator, Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Invoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Key = property(get_Key, put_Key)
    Modifiers = property(get_Modifiers, put_Modifiers)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ScopeOwner = property(get_ScopeOwner, put_ScopeOwner)
class IKeyboardAcceleratorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('44d88a99-4bfd-4a47-a8-93-51-5f-38-86-23-f6')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Input.KeyboardAccelerator: ...
class IKeyboardAcceleratorInvokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c00b03f2-04e7-4415-b1-7d-d7-6b-94-90-de-2b')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Element(self) -> Windows.UI.Xaml.DependencyObject: ...
    Handled = property(get_Handled, put_Handled)
    Element = property(get_Element, None)
class IKeyboardAcceleratorInvokedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('befca4b8-5907-48ee-8e-21-9c-96-90-78-fa-11')
    @winrt_commethod(6)
    def get_KeyboardAccelerator(self) -> Windows.UI.Xaml.Input.KeyboardAccelerator: ...
    KeyboardAccelerator = property(get_KeyboardAccelerator, None)
class IKeyboardAcceleratorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3bd43d51-9bb3-456d-bf-15-80-4a-df-b8-62-61')
    @winrt_commethod(6)
    def get_KeyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ModifiersProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScopeOwnerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeyProperty = property(get_KeyProperty, None)
    ModifiersProperty = property(get_ModifiersProperty, None)
    IsEnabledProperty = property(get_IsEnabledProperty, None)
    ScopeOwnerProperty = property(get_ScopeOwnerProperty, None)
class ILosingFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f9f683c7-d789-472b-aa-93-6d-41-05-e6-da-be')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_NewFocusedElement(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def put_NewFocusedElement(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(9)
    def get_FocusState(self) -> Windows.UI.Xaml.FocusState: ...
    @winrt_commethod(10)
    def get_Direction(self) -> Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_InputDevice(self) -> Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_commethod(14)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_Cancel(self, value: Boolean) -> Void: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    FocusState = property(get_FocusState, None)
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    Cancel = property(get_Cancel, put_Cancel)
class ILosingFocusEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0493fad9-c27f-469f-8e-62-52-b3-a4-f7-cd-54')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetNewFocusedElement(self, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
class ILosingFocusEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c98900bd-0b79-566e-ad-1f-43-6f-a5-13-ae-22')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
class IManipulationCompletedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b5ad9b23-2f41-498e-83-19-01-5e-e8-a7-53-46')
    @winrt_commethod(6)
    def get_Container(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> Windows.UI.Input.ManipulationVelocities: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    IsInertial = property(get_IsInertial, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IManipulationDeltaRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('400d5794-4c6f-491d-82-d6-35-17-10-93-99-c6')
    @winrt_commethod(6)
    def get_Container(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Delta(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(11)
    def get_Velocities(self) -> Windows.UI.Input.ManipulationVelocities: ...
    @winrt_commethod(12)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(15)
    def Complete(self) -> Void: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    IsInertial = property(get_IsInertial, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IManipulationInertiaStartingRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('246a91a9-ca43-4c0b-ac-ef-81-e8-b8-14-75-20')
    @winrt_commethod(6)
    def get_Container(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_ExpansionBehavior(self) -> Windows.UI.Xaml.Input.InertiaExpansionBehavior: ...
    @winrt_commethod(8)
    def put_ExpansionBehavior(self, value: Windows.UI.Xaml.Input.InertiaExpansionBehavior) -> Void: ...
    @winrt_commethod(9)
    def get_RotationBehavior(self) -> Windows.UI.Xaml.Input.InertiaRotationBehavior: ...
    @winrt_commethod(10)
    def put_RotationBehavior(self, value: Windows.UI.Xaml.Input.InertiaRotationBehavior) -> Void: ...
    @winrt_commethod(11)
    def get_TranslationBehavior(self) -> Windows.UI.Xaml.Input.InertiaTranslationBehavior: ...
    @winrt_commethod(12)
    def put_TranslationBehavior(self, value: Windows.UI.Xaml.Input.InertiaTranslationBehavior) -> Void: ...
    @winrt_commethod(13)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(16)
    def get_Delta(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(17)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(18)
    def get_Velocities(self) -> Windows.UI.Input.ManipulationVelocities: ...
    Container = property(get_Container, None)
    ExpansionBehavior = property(get_ExpansionBehavior, put_ExpansionBehavior)
    RotationBehavior = property(get_RotationBehavior, put_RotationBehavior)
    TranslationBehavior = property(get_TranslationBehavior, put_TranslationBehavior)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
class IManipulationPivot(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2e3838a5-e6c2-4998-82-ac-18-74-8b-14-16-66')
    @winrt_commethod(6)
    def get_Center(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Center(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Radius(self) -> Double: ...
    @winrt_commethod(9)
    def put_Radius(self, value: Double) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class IManipulationPivotFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6d05b039-3702-4396-ad-9b-a8-25-ef-a6-3a-3b')
    @winrt_commethod(6)
    def CreateInstanceWithCenterAndRadius(self, center: Windows.Foundation.Point, radius: Double) -> Windows.UI.Xaml.Input.ManipulationPivot: ...
class IManipulationStartedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5db1aa05-9f80-48b6-ae-6c-4f-11-9d-e8-ff-13')
    @winrt_commethod(6)
    def get_Container(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(11)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(12)
    def Complete(self) -> Void: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Cumulative = property(get_Cumulative, None)
class IManipulationStartedRoutedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('84c1daa7-7272-4463-b6-c3-a4-0b-9b-a1-51-fc')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs: ...
class IManipulationStartingRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('18d636b7-53a4-4c15-a4-98-f3-a9-ca-21-2a-42')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_commethod(7)
    def put_Mode(self, value: Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_commethod(8)
    def get_Container(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Container(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def get_Pivot(self) -> Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_commethod(11)
    def put_Pivot(self, value: Windows.UI.Xaml.Input.ManipulationPivot) -> Void: ...
    @winrt_commethod(12)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_Handled(self, value: Boolean) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Container = property(get_Container, put_Container)
    Pivot = property(get_Pivot, put_Pivot)
    Handled = property(get_Handled, put_Handled)
class INoFocusCandidateFoundEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ec3601a7-1007-48f9-b6-b3-ed-0b-ea-53-93-7d')
    @winrt_commethod(6)
    def get_Direction(self) -> Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_InputDevice(self) -> Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
class IPointer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5ee8f39f-747d-4171-90-e6-cd-37-a9-df-fb-11')
    @winrt_commethod(6)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_IsInContact(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsInRange(self) -> Boolean: ...
    PointerId = property(get_PointerId, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    IsInContact = property(get_IsInContact, None)
    IsInRange = property(get_IsInRange, None)
class IPointerRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('da628f0a-9752-49e2-bd-e2-49-ec-ca-b9-19-4d')
    @winrt_commethod(6)
    def get_Pointer(self) -> Windows.UI.Xaml.Input.Pointer: ...
    @winrt_commethod(7)
    def get_KeyModifiers(self) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetCurrentPoint(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(11)
    def GetIntermediatePoints(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
    Pointer = property(get_Pointer, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Handled = property(get_Handled, put_Handled)
class IPointerRoutedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0821f294-1de6-4711-ba-7c-8d-4b-8b-09-11-d0')
    @winrt_commethod(6)
    def get_IsGenerated(self) -> Boolean: ...
    IsGenerated = property(get_IsGenerated, None)
class IProcessKeyboardAcceleratorEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fb79c216-972b-440c-9b-83-2b-41-98-dc-f0-9d')
    @winrt_commethod(6)
    def get_Key(self) -> Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def get_Modifiers(self) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Key = property(get_Key, None)
    Modifiers = property(get_Modifiers, None)
    Handled = property(get_Handled, put_Handled)
class IRightTappedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6834869d-7bd5-4033-b2-37-17-2f-79-ab-e3-93')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class IStandardUICommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d2bf7f43-0504-52d0-8a-a6-0c-b0-f7-56-eb-27')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.UI.Xaml.Input.StandardUICommandKind: ...
    Kind = property(get_Kind, None)
class IStandardUICommand2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e3666069-f9e4-51eb-88-5b-7a-62-0a-07-82-ea')
    @winrt_commethod(6)
    def put_Kind(self, value: Windows.UI.Xaml.Input.StandardUICommandKind) -> Void: ...
    Kind = property(None, put_Kind)
class IStandardUICommandFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8f1a7590-dce1-56e4-ab-63-f5-ce-3c-e4-eb-f6')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Input.StandardUICommand: ...
    @winrt_commethod(7)
    def CreateInstanceWithKind(self, kind: Windows.UI.Xaml.Input.StandardUICommandKind, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Input.StandardUICommand: ...
class IStandardUICommandStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7ea87ed9-2978-5533-9b-2e-67-59-ce-88-56-9f')
    @winrt_commethod(6)
    def get_KindProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KindProperty = property(get_KindProperty, None)
class ITappedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a099e6be-e624-459a-bb-1d-e0-5c-73-e2-cc-66')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class IXamlUICommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8494f8d4-ead1-5f01-ad-2e-a8-ca-d4-f9-dc-0e')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IconSource(self) -> Windows.UI.Xaml.Controls.IconSource: ...
    @winrt_commethod(9)
    def put_IconSource(self, value: Windows.UI.Xaml.Controls.IconSource) -> Void: ...
    @winrt_commethod(10)
    def get_KeyboardAccelerators(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_commethod(11)
    def get_AccessKey(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_AccessKey(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Command(self) -> Windows.UI.Xaml.Input.ICommand: ...
    @winrt_commethod(16)
    def put_Command(self, value: Windows.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_commethod(17)
    def add_ExecuteRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Input.XamlUICommand, Windows.UI.Xaml.Input.ExecuteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ExecuteRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_CanExecuteRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Input.XamlUICommand, Windows.UI.Xaml.Input.CanExecuteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_CanExecuteRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def NotifyCanExecuteChanged(self) -> Void: ...
    Label = property(get_Label, put_Label)
    IconSource = property(get_IconSource, put_IconSource)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    AccessKey = property(get_AccessKey, put_AccessKey)
    Description = property(get_Description, put_Description)
    Command = property(get_Command, put_Command)
class IXamlUICommandFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1eec08c3-e061-5e10-9f-2a-2b-aa-84-08-85-c2')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Input.XamlUICommand: ...
class IXamlUICommandStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('66bc457c-1a0c-58ed-87-6e-71-53-3f-96-6d-b6')
    @winrt_commethod(6)
    def get_LabelProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IconSourceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_KeyboardAcceleratorsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AccessKeyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DescriptionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_CommandProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    LabelProperty = property(get_LabelProperty, None)
    IconSourceProperty = property(get_IconSourceProperty, None)
    KeyboardAcceleratorsProperty = property(get_KeyboardAcceleratorsProperty, None)
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    DescriptionProperty = property(get_DescriptionProperty, None)
    CommandProperty = property(get_CommandProperty, None)
class InertiaExpansionBehavior(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.InertiaExpansionBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: Windows.UI.Xaml.Input.IInertiaExpansionBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: Windows.UI.Xaml.Input.IInertiaExpansionBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredExpansion(self: Windows.UI.Xaml.Input.IInertiaExpansionBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredExpansion(self: Windows.UI.Xaml.Input.IInertiaExpansionBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredExpansion = property(get_DesiredExpansion, put_DesiredExpansion)
class InertiaRotationBehavior(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.InertiaRotationBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: Windows.UI.Xaml.Input.IInertiaRotationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: Windows.UI.Xaml.Input.IInertiaRotationBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredRotation(self: Windows.UI.Xaml.Input.IInertiaRotationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredRotation(self: Windows.UI.Xaml.Input.IInertiaRotationBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredRotation = property(get_DesiredRotation, put_DesiredRotation)
class InertiaTranslationBehavior(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.InertiaTranslationBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: Windows.UI.Xaml.Input.IInertiaTranslationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: Windows.UI.Xaml.Input.IInertiaTranslationBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredDisplacement(self: Windows.UI.Xaml.Input.IInertiaTranslationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDisplacement(self: Windows.UI.Xaml.Input.IInertiaTranslationBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredDisplacement = property(get_DesiredDisplacement, put_DesiredDisplacement)
class InputScope(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Input.InputScope'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.InputScope: ...
    @winrt_mixinmethod
    def get_Names(self: Windows.UI.Xaml.Input.IInputScope) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Input.InputScopeName]: ...
    Names = property(get_Names, None)
class InputScopeName(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Input.InputScopeName'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Input.IInputScopeNameFactory, nameValue: Windows.UI.Xaml.Input.InputScopeNameValue) -> Windows.UI.Xaml.Input.InputScopeName: ...
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.InputScopeName: ...
    @winrt_mixinmethod
    def get_NameValue(self: Windows.UI.Xaml.Input.IInputScopeName) -> Windows.UI.Xaml.Input.InputScopeNameValue: ...
    @winrt_mixinmethod
    def put_NameValue(self: Windows.UI.Xaml.Input.IInputScopeName, value: Windows.UI.Xaml.Input.InputScopeNameValue) -> Void: ...
    NameValue = property(get_NameValue, put_NameValue)
InputScopeNameValue = Int32
InputScopeNameValue_Default: InputScopeNameValue = 0
InputScopeNameValue_Url: InputScopeNameValue = 1
InputScopeNameValue_EmailSmtpAddress: InputScopeNameValue = 5
InputScopeNameValue_PersonalFullName: InputScopeNameValue = 7
InputScopeNameValue_CurrencyAmountAndSymbol: InputScopeNameValue = 20
InputScopeNameValue_CurrencyAmount: InputScopeNameValue = 21
InputScopeNameValue_DateMonthNumber: InputScopeNameValue = 23
InputScopeNameValue_DateDayNumber: InputScopeNameValue = 24
InputScopeNameValue_DateYear: InputScopeNameValue = 25
InputScopeNameValue_Digits: InputScopeNameValue = 28
InputScopeNameValue_Number: InputScopeNameValue = 29
InputScopeNameValue_Password: InputScopeNameValue = 31
InputScopeNameValue_TelephoneNumber: InputScopeNameValue = 32
InputScopeNameValue_TelephoneCountryCode: InputScopeNameValue = 33
InputScopeNameValue_TelephoneAreaCode: InputScopeNameValue = 34
InputScopeNameValue_TelephoneLocalNumber: InputScopeNameValue = 35
InputScopeNameValue_TimeHour: InputScopeNameValue = 37
InputScopeNameValue_TimeMinutesOrSeconds: InputScopeNameValue = 38
InputScopeNameValue_NumberFullWidth: InputScopeNameValue = 39
InputScopeNameValue_AlphanumericHalfWidth: InputScopeNameValue = 40
InputScopeNameValue_AlphanumericFullWidth: InputScopeNameValue = 41
InputScopeNameValue_Hiragana: InputScopeNameValue = 44
InputScopeNameValue_KatakanaHalfWidth: InputScopeNameValue = 45
InputScopeNameValue_KatakanaFullWidth: InputScopeNameValue = 46
InputScopeNameValue_Hanja: InputScopeNameValue = 47
InputScopeNameValue_HangulHalfWidth: InputScopeNameValue = 48
InputScopeNameValue_HangulFullWidth: InputScopeNameValue = 49
InputScopeNameValue_Search: InputScopeNameValue = 50
InputScopeNameValue_Formula: InputScopeNameValue = 51
InputScopeNameValue_SearchIncremental: InputScopeNameValue = 52
InputScopeNameValue_ChineseHalfWidth: InputScopeNameValue = 53
InputScopeNameValue_ChineseFullWidth: InputScopeNameValue = 54
InputScopeNameValue_NativeScript: InputScopeNameValue = 55
InputScopeNameValue_Text: InputScopeNameValue = 57
InputScopeNameValue_Chat: InputScopeNameValue = 58
InputScopeNameValue_NameOrPhoneNumber: InputScopeNameValue = 59
InputScopeNameValue_EmailNameOrAddress: InputScopeNameValue = 60
InputScopeNameValue_Private: InputScopeNameValue = 61
InputScopeNameValue_Maps: InputScopeNameValue = 62
InputScopeNameValue_NumericPassword: InputScopeNameValue = 63
InputScopeNameValue_NumericPin: InputScopeNameValue = 64
InputScopeNameValue_AlphanumericPin: InputScopeNameValue = 65
InputScopeNameValue_FormulaNumber: InputScopeNameValue = 67
InputScopeNameValue_ChatWithoutEmoji: InputScopeNameValue = 68
class KeyEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('7c63d2e5-7a0e-4e12-b9-6a-77-15-aa-6f-f1-c8')
    ClassId = 'Windows.UI.Xaml.Input.KeyEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.KeyRoutedEventArgs) -> Void: ...
class KeyRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.KeyRoutedEventArgs'
    @winrt_mixinmethod
    def get_Key(self: Windows.UI.Xaml.Input.IKeyRoutedEventArgs) -> Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: Windows.UI.Xaml.Input.IKeyRoutedEventArgs) -> Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IKeyRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IKeyRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalKey(self: Windows.UI.Xaml.Input.IKeyRoutedEventArgs2) -> Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.UI.Xaml.Input.IKeyRoutedEventArgs3) -> WinRT_String: ...
    Key = property(get_Key, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
    OriginalKey = property(get_OriginalKey, None)
    DeviceId = property(get_DeviceId, None)
KeyTipPlacementMode = Int32
KeyTipPlacementMode_Auto: KeyTipPlacementMode = 0
KeyTipPlacementMode_Bottom: KeyTipPlacementMode = 1
KeyTipPlacementMode_Top: KeyTipPlacementMode = 2
KeyTipPlacementMode_Left: KeyTipPlacementMode = 3
KeyTipPlacementMode_Right: KeyTipPlacementMode = 4
KeyTipPlacementMode_Center: KeyTipPlacementMode = 5
KeyTipPlacementMode_Hidden: KeyTipPlacementMode = 6
class KeyboardAccelerator(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(21)
    def get_Key(self) -> Windows.System.VirtualKey: ...
    @winrt_commethod(22)
    def put_Key(self, value: Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(23)
    def get_Modifiers(self) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(24)
    def put_Modifiers(self, value: Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(25)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(26)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(27)
    def get_ScopeOwner(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(28)
    def put_ScopeOwner(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(29)
    def add_Invoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Input.KeyboardAccelerator, Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_Invoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_KeyProperty(cls: Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ModifiersProperty(cls: Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScopeOwnerProperty(cls: Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Key = property(get_Key, put_Key)
    Modifiers = property(get_Modifiers, put_Modifiers)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ScopeOwner = property(get_ScopeOwner, put_ScopeOwner)
    KeyProperty = property(get_KeyProperty, None)
    ModifiersProperty = property(get_ModifiersProperty, None)
    IsEnabledProperty = property(get_IsEnabledProperty, None)
    ScopeOwnerProperty = property(get_ScopeOwnerProperty, None)
class KeyboardAcceleratorInvokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Element(self: Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_KeyboardAccelerator(self: Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs2) -> Windows.UI.Xaml.Input.KeyboardAccelerator: ...
    Handled = property(get_Handled, put_Handled)
    Element = property(get_Element, None)
    KeyboardAccelerator = property(get_KeyboardAccelerator, None)
KeyboardAcceleratorPlacementMode = Int32
KeyboardAcceleratorPlacementMode_Auto: KeyboardAcceleratorPlacementMode = 0
KeyboardAcceleratorPlacementMode_Hidden: KeyboardAcceleratorPlacementMode = 1
KeyboardNavigationMode = Int32
KeyboardNavigationMode_Local: KeyboardNavigationMode = 0
KeyboardNavigationMode_Cycle: KeyboardNavigationMode = 1
KeyboardNavigationMode_Once: KeyboardNavigationMode = 2
class LosingFocusEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.LosingFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_NewFocusedElement(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_NewFocusedElement(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_FocusState(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Windows.UI.Xaml.FocusState: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_mixinmethod
    def get_Cancel(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryCancel(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetNewFocusedElement(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs2, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.UI.Xaml.Input.ILosingFocusEventArgs3) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    FocusState = property(get_FocusState, None)
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
class ManipulationCompletedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('38ef4b0f-14f8-42df-9a-1e-a4-bc-c4-af-77-f4')
    ClassId = 'Windows.UI.Xaml.Input.ManipulationCompletedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs) -> Void: ...
class ManipulationCompletedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_IsInertial(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Cumulative(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    IsInertial = property(get_IsInertial, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class ManipulationDeltaEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('aa1160cb-dfb9-4c56-ab-dc-71-1b-63-c8-eb-94')
    ClassId = 'Windows.UI.Xaml.Input.ManipulationDeltaEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs) -> Void: ...
class ManipulationDeltaRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_IsInertial(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Delta(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def Complete(self: Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Void: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    IsInertial = property(get_IsInertial, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class ManipulationInertiaStartingEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d39d6322-7c9c-481b-82-7b-c8-b2-d9-bb-6f-c7')
    ClassId = 'Windows.UI.Xaml.Input.ManipulationInertiaStartingEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs) -> Void: ...
class ManipulationInertiaStartingRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_ExpansionBehavior(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.UI.Xaml.Input.InertiaExpansionBehavior: ...
    @winrt_mixinmethod
    def put_ExpansionBehavior(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: Windows.UI.Xaml.Input.InertiaExpansionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_RotationBehavior(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.UI.Xaml.Input.InertiaRotationBehavior: ...
    @winrt_mixinmethod
    def put_RotationBehavior(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: Windows.UI.Xaml.Input.InertiaRotationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationBehavior(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.UI.Xaml.Input.InertiaTranslationBehavior: ...
    @winrt_mixinmethod
    def put_TranslationBehavior(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: Windows.UI.Xaml.Input.InertiaTranslationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Delta(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Windows.UI.Input.ManipulationVelocities: ...
    Container = property(get_Container, None)
    ExpansionBehavior = property(get_ExpansionBehavior, put_ExpansionBehavior)
    RotationBehavior = property(get_RotationBehavior, put_RotationBehavior)
    TranslationBehavior = property(get_TranslationBehavior, put_TranslationBehavior)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
ManipulationModes = UInt32
ManipulationModes_None: ManipulationModes = 0
ManipulationModes_TranslateX: ManipulationModes = 1
ManipulationModes_TranslateY: ManipulationModes = 2
ManipulationModes_TranslateRailsX: ManipulationModes = 4
ManipulationModes_TranslateRailsY: ManipulationModes = 8
ManipulationModes_Rotate: ManipulationModes = 16
ManipulationModes_Scale: ManipulationModes = 32
ManipulationModes_TranslateInertia: ManipulationModes = 64
ManipulationModes_RotateInertia: ManipulationModes = 128
ManipulationModes_ScaleInertia: ManipulationModes = 256
ManipulationModes_All: ManipulationModes = 65535
ManipulationModes_System: ManipulationModes = 65536
class ManipulationPivot(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.ManipulationPivot'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_factorymethod
    def CreateInstanceWithCenterAndRadius(cls: Windows.UI.Xaml.Input.IManipulationPivotFactory, center: Windows.Foundation.Point, radius: Double) -> Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_mixinmethod
    def get_Center(self: Windows.UI.Xaml.Input.IManipulationPivot) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Center(self: Windows.UI.Xaml.Input.IManipulationPivot, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Radius(self: Windows.UI.Xaml.Input.IManipulationPivot) -> Double: ...
    @winrt_mixinmethod
    def put_Radius(self: Windows.UI.Xaml.Input.IManipulationPivot, value: Double) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class ManipulationStartedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f88345f8-e0a3-4be2-b9-0c-dc-20-e6-d8-be-b0')
    ClassId = 'Windows.UI.Xaml.Input.ManipulationStartedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs) -> Void: ...
class ManipulationStartedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    @winrt_commethod(14)
    def get_Container(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(15)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(16)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(19)
    def get_Cumulative(self) -> Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(20)
    def Complete(self) -> Void: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Cumulative = property(get_Cumulative, None)
class ManipulationStartingEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('10d0b04e-bfe4-42cb-82-3c-3f-ec-d8-77-0e-f8')
    ClassId = 'Windows.UI.Xaml.Input.ManipulationStartingEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs) -> Void: ...
class ManipulationStartingRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_mixinmethod
    def get_Container(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Container(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_Pivot(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_mixinmethod
    def put_Pivot(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: Windows.UI.Xaml.Input.ManipulationPivot) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: Boolean) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Container = property(get_Container, put_Container)
    Pivot = property(get_Pivot, put_Pivot)
    Handled = property(get_Handled, put_Handled)
class NoFocusCandidateFoundEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.NoFocusCandidateFoundEventArgs'
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
class Pointer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.Pointer'
    @winrt_mixinmethod
    def get_PointerId(self: Windows.UI.Xaml.Input.IPointer) -> UInt32: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.IPointer) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_IsInContact(self: Windows.UI.Xaml.Input.IPointer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInRange(self: Windows.UI.Xaml.Input.IPointer) -> Boolean: ...
    PointerId = property(get_PointerId, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    IsInContact = property(get_IsInContact, None)
    IsInRange = property(get_IsInRange, None)
class PointerEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e4385929-c004-4bcf-89-70-35-94-86-e3-9f-88')
    ClassId = 'Windows.UI.Xaml.Input.PointerEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.PointerRoutedEventArgs) -> Void: ...
class PointerRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.PointerRoutedEventArgs'
    @winrt_mixinmethod
    def get_Pointer(self: Windows.UI.Xaml.Input.IPointerRoutedEventArgs) -> Windows.UI.Xaml.Input.Pointer: ...
    @winrt_mixinmethod
    def get_KeyModifiers(self: Windows.UI.Xaml.Input.IPointerRoutedEventArgs) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IPointerRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IPointerRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentPoint(self: Windows.UI.Xaml.Input.IPointerRoutedEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.UI.Input.PointerPoint: ...
    @winrt_mixinmethod
    def GetIntermediatePoints(self: Windows.UI.Xaml.Input.IPointerRoutedEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.PointerPoint]: ...
    @winrt_mixinmethod
    def get_IsGenerated(self: Windows.UI.Xaml.Input.IPointerRoutedEventArgs2) -> Boolean: ...
    Pointer = property(get_Pointer, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Handled = property(get_Handled, put_Handled)
    IsGenerated = property(get_IsGenerated, None)
class ProcessKeyboardAcceleratorEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs'
    @winrt_mixinmethod
    def get_Key(self: Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_Modifiers(self: Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs, value: Boolean) -> Void: ...
    Key = property(get_Key, None)
    Modifiers = property(get_Modifiers, None)
    Handled = property(get_Handled, put_Handled)
class RightTappedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('2532a062-f447-4950-9c-46-f1-e3-4a-2c-22-38')
    ClassId = 'Windows.UI.Xaml.Input.RightTappedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.RightTappedRoutedEventArgs) -> Void: ...
class RightTappedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.RightTappedRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.RightTappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class StandardUICommand(ComPtr):
    extends: Windows.UI.Xaml.Input.XamlUICommand
    @winrt_commethod(38)
    def get_Kind(self) -> Windows.UI.Xaml.Input.StandardUICommandKind: ...
    @winrt_commethod(39)
    def put_Kind(self, value: Windows.UI.Xaml.Input.StandardUICommandKind) -> Void: ...
    @winrt_classmethod
    def get_KindProperty(cls: Windows.UI.Xaml.Input.IStandardUICommandStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Kind = property(get_Kind, put_Kind)
    KindProperty = property(get_KindProperty, None)
StandardUICommandKind = Int32
StandardUICommandKind_None: StandardUICommandKind = 0
StandardUICommandKind_Cut: StandardUICommandKind = 1
StandardUICommandKind_Copy: StandardUICommandKind = 2
StandardUICommandKind_Paste: StandardUICommandKind = 3
StandardUICommandKind_SelectAll: StandardUICommandKind = 4
StandardUICommandKind_Delete: StandardUICommandKind = 5
StandardUICommandKind_Share: StandardUICommandKind = 6
StandardUICommandKind_Save: StandardUICommandKind = 7
StandardUICommandKind_Open: StandardUICommandKind = 8
StandardUICommandKind_Close: StandardUICommandKind = 9
StandardUICommandKind_Pause: StandardUICommandKind = 10
StandardUICommandKind_Play: StandardUICommandKind = 11
StandardUICommandKind_Stop: StandardUICommandKind = 12
StandardUICommandKind_Forward: StandardUICommandKind = 13
StandardUICommandKind_Backward: StandardUICommandKind = 14
StandardUICommandKind_Undo: StandardUICommandKind = 15
StandardUICommandKind_Redo: StandardUICommandKind = 16
class TappedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('68d940cc-9ff0-49ce-b1-41-3f-07-ec-47-7b-97')
    ClassId = 'Windows.UI.Xaml.Input.TappedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Input.TappedRoutedEventArgs) -> Void: ...
class TappedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    ClassId = 'Windows.UI.Xaml.Input.TappedRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Input.TappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.UI.Xaml.Input.ITappedRoutedEventArgs) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Input.ITappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Input.ITappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: Windows.UI.Xaml.Input.ITappedRoutedEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
XYFocusKeyboardNavigationMode = Int32
XYFocusKeyboardNavigationMode_Auto: XYFocusKeyboardNavigationMode = 0
XYFocusKeyboardNavigationMode_Enabled: XYFocusKeyboardNavigationMode = 1
XYFocusKeyboardNavigationMode_Disabled: XYFocusKeyboardNavigationMode = 2
XYFocusNavigationStrategy = Int32
XYFocusNavigationStrategy_Auto: XYFocusNavigationStrategy = 0
XYFocusNavigationStrategy_Projection: XYFocusNavigationStrategy = 1
XYFocusNavigationStrategy_NavigationDirectionDistance: XYFocusNavigationStrategy = 2
XYFocusNavigationStrategy_RectilinearDistance: XYFocusNavigationStrategy = 3
XYFocusNavigationStrategyOverride = Int32
XYFocusNavigationStrategyOverride_None: XYFocusNavigationStrategyOverride = 0
XYFocusNavigationStrategyOverride_Auto: XYFocusNavigationStrategyOverride = 1
XYFocusNavigationStrategyOverride_Projection: XYFocusNavigationStrategyOverride = 2
XYFocusNavigationStrategyOverride_NavigationDirectionDistance: XYFocusNavigationStrategyOverride = 3
XYFocusNavigationStrategyOverride_RectilinearDistance: XYFocusNavigationStrategyOverride = 4
class XamlUICommand(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(33)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(35)
    def get_IconSource(self) -> Windows.UI.Xaml.Controls.IconSource: ...
    @winrt_commethod(36)
    def put_IconSource(self, value: Windows.UI.Xaml.Controls.IconSource) -> Void: ...
    @winrt_commethod(37)
    def get_KeyboardAccelerators(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_commethod(38)
    def get_AccessKey(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def put_AccessKey(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(40)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(41)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(42)
    def get_Command(self) -> Windows.UI.Xaml.Input.ICommand: ...
    @winrt_commethod(43)
    def put_Command(self, value: Windows.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_commethod(44)
    def add_ExecuteRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Input.XamlUICommand, Windows.UI.Xaml.Input.ExecuteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(45)
    def remove_ExecuteRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(46)
    def add_CanExecuteRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Input.XamlUICommand, Windows.UI.Xaml.Input.CanExecuteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(47)
    def remove_CanExecuteRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(48)
    def NotifyCanExecuteChanged(self) -> Void: ...
    @winrt_commethod(49)
    def add_CanExecuteChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(50)
    def remove_CanExecuteChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(51)
    def CanExecute(self, parameter: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_commethod(52)
    def Execute(self, parameter: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_classmethod
    def get_LabelProperty(cls: Windows.UI.Xaml.Input.IXamlUICommandStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IconSourceProperty(cls: Windows.UI.Xaml.Input.IXamlUICommandStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyboardAcceleratorsProperty(cls: Windows.UI.Xaml.Input.IXamlUICommandStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: Windows.UI.Xaml.Input.IXamlUICommandStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DescriptionProperty(cls: Windows.UI.Xaml.Input.IXamlUICommandStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CommandProperty(cls: Windows.UI.Xaml.Input.IXamlUICommandStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Label = property(get_Label, put_Label)
    IconSource = property(get_IconSource, put_IconSource)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    AccessKey = property(get_AccessKey, put_AccessKey)
    Description = property(get_Description, put_Description)
    Command = property(get_Command, put_Command)
    LabelProperty = property(get_LabelProperty, None)
    IconSourceProperty = property(get_IconSourceProperty, None)
    KeyboardAcceleratorsProperty = property(get_KeyboardAcceleratorsProperty, None)
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    DescriptionProperty = property(get_DescriptionProperty, None)
    CommandProperty = property(get_CommandProperty, None)
make_head(_module, 'AccessKeyDisplayDismissedEventArgs')
make_head(_module, 'AccessKeyDisplayRequestedEventArgs')
make_head(_module, 'AccessKeyInvokedEventArgs')
make_head(_module, 'AccessKeyManager')
make_head(_module, 'CanExecuteRequestedEventArgs')
make_head(_module, 'CharacterReceivedRoutedEventArgs')
make_head(_module, 'ContextRequestedEventArgs')
make_head(_module, 'DoubleTappedEventHandler')
make_head(_module, 'DoubleTappedRoutedEventArgs')
make_head(_module, 'ExecuteRequestedEventArgs')
make_head(_module, 'FindNextElementOptions')
make_head(_module, 'FocusManager')
make_head(_module, 'FocusManagerGotFocusEventArgs')
make_head(_module, 'FocusManagerLostFocusEventArgs')
make_head(_module, 'FocusMovementResult')
make_head(_module, 'GettingFocusEventArgs')
make_head(_module, 'HoldingEventHandler')
make_head(_module, 'HoldingRoutedEventArgs')
make_head(_module, 'IAccessKeyDisplayDismissedEventArgs')
make_head(_module, 'IAccessKeyDisplayRequestedEventArgs')
make_head(_module, 'IAccessKeyInvokedEventArgs')
make_head(_module, 'IAccessKeyManager')
make_head(_module, 'IAccessKeyManagerStatics')
make_head(_module, 'IAccessKeyManagerStatics2')
make_head(_module, 'ICanExecuteRequestedEventArgs')
make_head(_module, 'ICharacterReceivedRoutedEventArgs')
make_head(_module, 'ICommand')
make_head(_module, 'IContextRequestedEventArgs')
make_head(_module, 'IDoubleTappedRoutedEventArgs')
make_head(_module, 'IExecuteRequestedEventArgs')
make_head(_module, 'IFindNextElementOptions')
make_head(_module, 'IFocusManager')
make_head(_module, 'IFocusManagerGotFocusEventArgs')
make_head(_module, 'IFocusManagerLostFocusEventArgs')
make_head(_module, 'IFocusManagerStatics')
make_head(_module, 'IFocusManagerStatics2')
make_head(_module, 'IFocusManagerStatics3')
make_head(_module, 'IFocusManagerStatics4')
make_head(_module, 'IFocusManagerStatics5')
make_head(_module, 'IFocusManagerStatics6')
make_head(_module, 'IFocusManagerStatics7')
make_head(_module, 'IFocusMovementResult')
make_head(_module, 'IGettingFocusEventArgs')
make_head(_module, 'IGettingFocusEventArgs2')
make_head(_module, 'IGettingFocusEventArgs3')
make_head(_module, 'IHoldingRoutedEventArgs')
make_head(_module, 'IInertiaExpansionBehavior')
make_head(_module, 'IInertiaRotationBehavior')
make_head(_module, 'IInertiaTranslationBehavior')
make_head(_module, 'IInputScope')
make_head(_module, 'IInputScopeName')
make_head(_module, 'IInputScopeNameFactory')
make_head(_module, 'IKeyRoutedEventArgs')
make_head(_module, 'IKeyRoutedEventArgs2')
make_head(_module, 'IKeyRoutedEventArgs3')
make_head(_module, 'IKeyboardAccelerator')
make_head(_module, 'IKeyboardAcceleratorFactory')
make_head(_module, 'IKeyboardAcceleratorInvokedEventArgs')
make_head(_module, 'IKeyboardAcceleratorInvokedEventArgs2')
make_head(_module, 'IKeyboardAcceleratorStatics')
make_head(_module, 'ILosingFocusEventArgs')
make_head(_module, 'ILosingFocusEventArgs2')
make_head(_module, 'ILosingFocusEventArgs3')
make_head(_module, 'IManipulationCompletedRoutedEventArgs')
make_head(_module, 'IManipulationDeltaRoutedEventArgs')
make_head(_module, 'IManipulationInertiaStartingRoutedEventArgs')
make_head(_module, 'IManipulationPivot')
make_head(_module, 'IManipulationPivotFactory')
make_head(_module, 'IManipulationStartedRoutedEventArgs')
make_head(_module, 'IManipulationStartedRoutedEventArgsFactory')
make_head(_module, 'IManipulationStartingRoutedEventArgs')
make_head(_module, 'INoFocusCandidateFoundEventArgs')
make_head(_module, 'IPointer')
make_head(_module, 'IPointerRoutedEventArgs')
make_head(_module, 'IPointerRoutedEventArgs2')
make_head(_module, 'IProcessKeyboardAcceleratorEventArgs')
make_head(_module, 'IRightTappedRoutedEventArgs')
make_head(_module, 'IStandardUICommand')
make_head(_module, 'IStandardUICommand2')
make_head(_module, 'IStandardUICommandFactory')
make_head(_module, 'IStandardUICommandStatics')
make_head(_module, 'ITappedRoutedEventArgs')
make_head(_module, 'IXamlUICommand')
make_head(_module, 'IXamlUICommandFactory')
make_head(_module, 'IXamlUICommandStatics')
make_head(_module, 'InertiaExpansionBehavior')
make_head(_module, 'InertiaRotationBehavior')
make_head(_module, 'InertiaTranslationBehavior')
make_head(_module, 'InputScope')
make_head(_module, 'InputScopeName')
make_head(_module, 'KeyEventHandler')
make_head(_module, 'KeyRoutedEventArgs')
make_head(_module, 'KeyboardAccelerator')
make_head(_module, 'KeyboardAcceleratorInvokedEventArgs')
make_head(_module, 'LosingFocusEventArgs')
make_head(_module, 'ManipulationCompletedEventHandler')
make_head(_module, 'ManipulationCompletedRoutedEventArgs')
make_head(_module, 'ManipulationDeltaEventHandler')
make_head(_module, 'ManipulationDeltaRoutedEventArgs')
make_head(_module, 'ManipulationInertiaStartingEventHandler')
make_head(_module, 'ManipulationInertiaStartingRoutedEventArgs')
make_head(_module, 'ManipulationPivot')
make_head(_module, 'ManipulationStartedEventHandler')
make_head(_module, 'ManipulationStartedRoutedEventArgs')
make_head(_module, 'ManipulationStartingEventHandler')
make_head(_module, 'ManipulationStartingRoutedEventArgs')
make_head(_module, 'NoFocusCandidateFoundEventArgs')
make_head(_module, 'Pointer')
make_head(_module, 'PointerEventHandler')
make_head(_module, 'PointerRoutedEventArgs')
make_head(_module, 'ProcessKeyboardAcceleratorEventArgs')
make_head(_module, 'RightTappedEventHandler')
make_head(_module, 'RightTappedRoutedEventArgs')
make_head(_module, 'StandardUICommand')
make_head(_module, 'TappedEventHandler')
make_head(_module, 'TappedRoutedEventArgs')
make_head(_module, 'XamlUICommand')
