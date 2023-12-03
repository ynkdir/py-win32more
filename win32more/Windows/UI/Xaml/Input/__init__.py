from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Input
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Controls
import win32more.Windows.UI.Xaml.Input
class AccessKeyDisplayDismissedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IAccessKeyDisplayDismissedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs: ...
class AccessKeyDisplayRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_PressedKeys(self: win32more.Windows.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs) -> WinRT_String: ...
    PressedKeys = property(get_PressedKeys, None)
class AccessKeyInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IAccessKeyInvokedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IAccessKeyInvokedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IAccessKeyInvokedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class _AccessKeyManager_Meta_(ComPtr.__class__):
    pass
class AccessKeyManager(ComPtr, metaclass=_AccessKeyManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IAccessKeyManager
    _classid_ = 'Windows.UI.Xaml.Input.AccessKeyManager'
    @winrt_classmethod
    def get_AreKeyTipsEnabled(cls: win32more.Windows.UI.Xaml.Input.IAccessKeyManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def put_AreKeyTipsEnabled(cls: win32more.Windows.UI.Xaml.Input.IAccessKeyManagerStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsDisplayModeEnabled(cls: win32more.Windows.UI.Xaml.Input.IAccessKeyManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def add_IsDisplayModeEnabledChanged(cls: win32more.Windows.UI.Xaml.Input.IAccessKeyManagerStatics, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_IsDisplayModeEnabledChanged(cls: win32more.Windows.UI.Xaml.Input.IAccessKeyManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def ExitDisplayMode(cls: win32more.Windows.UI.Xaml.Input.IAccessKeyManagerStatics) -> Void: ...
    _AccessKeyManager_Meta_.AreKeyTipsEnabled = property(get_AreKeyTipsEnabled.__wrapped__, put_AreKeyTipsEnabled.__wrapped__)
    _AccessKeyManager_Meta_.IsDisplayModeEnabled = property(get_IsDisplayModeEnabled.__wrapped__, None)
class CanExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.CanExecuteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_CanExecute(self: win32more.Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanExecute(self: win32more.Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs, value: Boolean) -> Void: ...
    Parameter = property(get_Parameter, None)
    CanExecute = property(get_CanExecute, put_CanExecute)
class CharacterReceivedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.CharacterReceivedRoutedEventArgs'
    @winrt_mixinmethod
    def get_Character(self: win32more.Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> Char: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs, value: Boolean) -> Void: ...
    Character = property(get_Character, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
class ContextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IContextRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ContextRequestedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.ContextRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IContextRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IContextRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryGetPosition(self: win32more.Windows.UI.Xaml.Input.IContextRequestedEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement, point: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class DoubleTappedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3124d025-04a7-4d45-825e-8204a624dbf4}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs) -> Void: ...
class DoubleTappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class ExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IExecuteRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ExecuteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Windows.UI.Xaml.Input.IExecuteRequestedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Parameter = property(get_Parameter, None)
class FindNextElementOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions
    _classid_ = 'Windows.UI.Xaml.Input.FindNextElementOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.FindNextElementOptions: ...
    @winrt_mixinmethod
    def get_SearchRoot(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_SearchRoot(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExclusionRect(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_ExclusionRect(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_HintRect(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_HintRect(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusNavigationStrategyOverride(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride: ...
    @winrt_mixinmethod
    def put_XYFocusNavigationStrategyOverride(self: win32more.Windows.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFocusManager
    _classid_ = 'Windows.UI.Xaml.Input.FocusManager'
    @winrt_classmethod
    def GetFocusedElement(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics, xamlRoot: win32more.Windows.UI.Xaml.XamlRoot) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def add_GotFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.FocusManagerGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GotFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LostFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.FocusManagerLostFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LostFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GettingFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GettingFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LosingFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LosingFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryFocusAsync(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics5, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.FocusState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusAsync(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics5, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusWithOptionsAsync(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics5, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Windows.UI.Xaml.Input.FindNextElementOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusWithOptions(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics4, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Windows.UI.Xaml.Input.FindNextElementOptions) -> Boolean: ...
    @winrt_classmethod
    def FindNextElement(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics4, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindFirstFocusableElement(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics4, searchScope: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindLastFocusableElement(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics4, searchScope: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindNextElementWithOptions(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics4, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Windows.UI.Xaml.Input.FindNextElementOptions) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindNextFocusableElement(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics3, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def FindNextFocusableElementWithHint(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics3, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def TryMoveFocus(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics2, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> Boolean: ...
    @winrt_classmethod
    def GetFocusedElement(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class FocusManagerGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFocusManagerGotFocusEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.FocusManagerGotFocusEventArgs'
    @winrt_mixinmethod
    def get_NewFocusedElement(self: win32more.Windows.UI.Xaml.Input.IFocusManagerGotFocusEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.UI.Xaml.Input.IFocusManagerGotFocusEventArgs) -> Guid: ...
    NewFocusedElement = property(get_NewFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class FocusManagerLostFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.FocusManagerLostFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: win32more.Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class FocusMovementResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFocusMovementResult
    _classid_ = 'Windows.UI.Xaml.Input.FocusMovementResult'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.UI.Xaml.Input.IFocusMovementResult) -> Boolean: ...
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
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.GettingFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_NewFocusedElement(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_NewFocusedElement(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_FocusState(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Windows.UI.Xaml.FocusState: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryCancel(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetNewFocusedElement(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs2, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.UI.Xaml.Input.IGettingFocusEventArgs3) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    FocusState = property(get_FocusState, None)
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
class HoldingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ecae8ccd-8e5e-4fbe-9846-30a6370afcdf}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.HoldingRoutedEventArgs) -> Void: ...
class HoldingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IHoldingRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.HoldingRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.HoldingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IHoldingRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_HoldingState(self: win32more.Windows.UI.Xaml.Input.IHoldingRoutedEventArgs) -> win32more.Windows.UI.Input.HoldingState: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IHoldingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IHoldingRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Windows.UI.Xaml.Input.IHoldingRoutedEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    HoldingState = property(get_HoldingState, None)
    Handled = property(get_Handled, put_Handled)
class IAccessKeyDisplayDismissedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IAccessKeyDisplayDismissedEventArgs'
    _iid_ = Guid('{8a610dc6-d72d-4ca8-9f66-556f35b513da}')
class IAccessKeyDisplayRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs'
    _iid_ = Guid('{0c079e55-13fe-4d03-a61d-e12f06567286}')
    @winrt_commethod(6)
    def get_PressedKeys(self) -> WinRT_String: ...
    PressedKeys = property(get_PressedKeys, None)
class IAccessKeyInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IAccessKeyInvokedEventArgs'
    _iid_ = Guid('{cfe9cd97-c718-4091-b7dd-adf1c072b1e1}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class IAccessKeyManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IAccessKeyManager'
    _iid_ = Guid('{ecc973b0-2ee9-4b1c-98d7-6e0e816d334b}')
class IAccessKeyManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IAccessKeyManagerStatics'
    _iid_ = Guid('{4ca0efe6-d9c8-4ebc-b4c7-30d1838a81f1}')
    @winrt_commethod(6)
    def get_IsDisplayModeEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsDisplayModeEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsDisplayModeEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def ExitDisplayMode(self) -> Void: ...
    IsDisplayModeEnabled = property(get_IsDisplayModeEnabled, None)
class IAccessKeyManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IAccessKeyManagerStatics2'
    _iid_ = Guid('{962bb594-2ab3-47c5-954b-7092f355f797}')
    @winrt_commethod(6)
    def get_AreKeyTipsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreKeyTipsEnabled(self, value: Boolean) -> Void: ...
    AreKeyTipsEnabled = property(get_AreKeyTipsEnabled, put_AreKeyTipsEnabled)
class ICanExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.ICanExecuteRequestedEventArgs'
    _iid_ = Guid('{c8e75256-1950-505d-993b-75907ef96830}')
    @winrt_commethod(6)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_CanExecute(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_CanExecute(self, value: Boolean) -> Void: ...
    Parameter = property(get_Parameter, None)
    CanExecute = property(get_CanExecute, put_CanExecute)
class ICharacterReceivedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs'
    _iid_ = Guid('{7849fd82-48e4-444d-9419-93ab8892c107}')
    @winrt_commethod(6)
    def get_Character(self) -> Char: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Character = property(get_Character, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
class ICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.ICommand'
    _iid_ = Guid('{e5af3542-ca67-4081-995b-709dd13792df}')
    @winrt_commethod(6)
    def add_CanExecuteChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CanExecuteChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def CanExecute(self, parameter: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_commethod(9)
    def Execute(self, parameter: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class IContextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IContextRequestedEventArgs'
    _iid_ = Guid('{42618e0a-1cb6-46fb-8374-0aec68aa5e51}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def TryGetPosition(self, relativeTo: win32more.Windows.UI.Xaml.UIElement, point: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class IDoubleTappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs'
    _iid_ = Guid('{af404424-26df-44f4-8714-9359249b62d3}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class IExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IExecuteRequestedEventArgs'
    _iid_ = Guid('{e07fa734-a0b6-5755-9e87-24f54cca9372}')
    @winrt_commethod(6)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Parameter = property(get_Parameter, None)
class IFindNextElementOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFindNextElementOptions'
    _iid_ = Guid('{d88ae22b-46c2-41fc-897e-b5961977b89d}')
    @winrt_commethod(6)
    def get_SearchRoot(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def put_SearchRoot(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(8)
    def get_ExclusionRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def put_ExclusionRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(10)
    def get_HintRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_HintRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(12)
    def get_XYFocusNavigationStrategyOverride(self) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride: ...
    @winrt_commethod(13)
    def put_XYFocusNavigationStrategyOverride(self, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategyOverride) -> Void: ...
    SearchRoot = property(get_SearchRoot, put_SearchRoot)
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    HintRect = property(get_HintRect, put_HintRect)
    XYFocusNavigationStrategyOverride = property(get_XYFocusNavigationStrategyOverride, put_XYFocusNavigationStrategyOverride)
class IFocusManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManager'
    _iid_ = Guid('{c843f50b-3b83-4da1-9d6f-557c1169f341}')
class IFocusManagerGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerGotFocusEventArgs'
    _iid_ = Guid('{97aa5d83-535b-507a-868e-62b706f06b61}')
    @winrt_commethod(6)
    def get_NewFocusedElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_CorrelationId(self) -> Guid: ...
    NewFocusedElement = property(get_NewFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class IFocusManagerLostFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs'
    _iid_ = Guid('{3e157e7a-9578-5cd3-aaa8-051b3d391978}')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_CorrelationId(self) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    CorrelationId = property(get_CorrelationId, None)
class IFocusManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerStatics'
    _iid_ = Guid('{1eccd326-8182-4482-826a-0918e9ed9af7}')
    @winrt_commethod(6)
    def GetFocusedElement(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IFocusManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerStatics2'
    _iid_ = Guid('{a920d761-dd87-4f31-beda-ef417fe7c04a}')
    @winrt_commethod(6)
    def TryMoveFocus(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> Boolean: ...
class IFocusManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerStatics3'
    _iid_ = Guid('{60805ebf-b149-417d-83f1-baeb560e2a47}')
    @winrt_commethod(6)
    def FindNextFocusableElement(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def FindNextFocusableElementWithHint(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Xaml.UIElement: ...
class IFocusManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerStatics4'
    _iid_ = Guid('{29276e9c-1c6c-414a-ba1c-96efd5962bcd}')
    @winrt_commethod(6)
    def TryMoveFocusWithOptions(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Windows.UI.Xaml.Input.FindNextElementOptions) -> Boolean: ...
    @winrt_commethod(7)
    def FindNextElement(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def FindFirstFocusableElement(self, searchScope: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def FindLastFocusableElement(self, searchScope: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(10)
    def FindNextElementWithOptions(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Windows.UI.Xaml.Input.FindNextElementOptions) -> win32more.Windows.UI.Xaml.DependencyObject: ...
class IFocusManagerStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerStatics5'
    _iid_ = Guid('{280edc61-207a-4d7b-b98f-ce165e1b2015}')
    @winrt_commethod(6)
    def TryFocusAsync(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.FocusState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_commethod(7)
    def TryMoveFocusAsync(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_commethod(8)
    def TryMoveFocusWithOptionsAsync(self, focusNavigationDirection: win32more.Windows.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Windows.UI.Xaml.Input.FindNextElementOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Input.FocusMovementResult]: ...
class IFocusManagerStatics6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerStatics6'
    _iid_ = Guid('{3546a1b6-20bf-5007-929d-e6d32e16afe4}')
    @winrt_commethod(6)
    def add_GotFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.FocusManagerGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_LostFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.FocusManagerLostFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LostFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_GettingFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_GettingFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_LosingFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_LosingFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IFocusManagerStatics7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerStatics7'
    _iid_ = Guid('{95d6fa97-f0fc-5c32-b29d-07c04ec966b0}')
    @winrt_commethod(6)
    def GetFocusedElement(self, xamlRoot: win32more.Windows.UI.Xaml.XamlRoot) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IFocusMovementResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusMovementResult'
    _iid_ = Guid('{06dfead3-c2ae-44bb-bfab-9c73de8407a4}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    Succeeded = property(get_Succeeded, None)
class IGettingFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IGettingFocusEventArgs'
    _iid_ = Guid('{fa05b9ce-c67c-4be8-8fd4-c44d67877e0d}')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_NewFocusedElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def put_NewFocusedElement(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(9)
    def get_FocusState(self) -> win32more.Windows.UI.Xaml.FocusState: ...
    @winrt_commethod(10)
    def get_Direction(self) -> win32more.Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_InputDevice(self) -> win32more.Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IGettingFocusEventArgs2'
    _iid_ = Guid('{88754d7b-b4b9-4959-8bce-89bf212ed4eb}')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetNewFocusedElement(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
class IGettingFocusEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IGettingFocusEventArgs3'
    _iid_ = Guid('{4e024891-db3f-5e78-b75a-62bfc3510735}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
class IHoldingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IHoldingRoutedEventArgs'
    _iid_ = Guid('{c246ff23-d80d-44de-8db9-0d815e269ac0}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_HoldingState(self) -> win32more.Windows.UI.Input.HoldingState: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetPosition(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    HoldingState = property(get_HoldingState, None)
    Handled = property(get_Handled, put_Handled)
class IInertiaExpansionBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IInertiaExpansionBehavior'
    _iid_ = Guid('{751d87e5-8d42-44c5-965e-3cd30cc9d6f7}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IInertiaRotationBehavior'
    _iid_ = Guid('{424cfb2e-bbfd-4625-ae78-20c65bf1efaf}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IInertiaTranslationBehavior'
    _iid_ = Guid('{45d3a512-3b32-4882-a4c2-ecfa2d4b6df0}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IInputScope'
    _iid_ = Guid('{5c0f85f3-f9d8-4220-b666-045d074d9bfa}')
    @winrt_commethod(6)
    def get_Names(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Input.InputScopeName]: ...
    Names = property(get_Names, None)
class IInputScopeName(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IInputScopeName'
    _iid_ = Guid('{fd3e6997-08fb-4cba-a021-792d7589fd5a}')
    @winrt_commethod(6)
    def get_NameValue(self) -> win32more.Windows.UI.Xaml.Input.InputScopeNameValue: ...
    @winrt_commethod(7)
    def put_NameValue(self, value: win32more.Windows.UI.Xaml.Input.InputScopeNameValue) -> Void: ...
    NameValue = property(get_NameValue, put_NameValue)
class IInputScopeNameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IInputScopeNameFactory'
    _iid_ = Guid('{4a40bb52-4bd7-4e54-8617-1cda8a1eda7f}')
    @winrt_commethod(6)
    def CreateInstance(self, nameValue: win32more.Windows.UI.Xaml.Input.InputScopeNameValue) -> win32more.Windows.UI.Xaml.Input.InputScopeName: ...
class IKeyRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyRoutedEventArgs'
    _iid_ = Guid('{d4cd3dfe-4079-42e9-a39a-3095d3f049c6}')
    @winrt_commethod(6)
    def get_Key(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Key = property(get_Key, None)
    KeyStatus = property(get_KeyStatus, None)
    Handled = property(get_Handled, put_Handled)
class IKeyRoutedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyRoutedEventArgs2'
    _iid_ = Guid('{1b02d57a-9634-4f14-91b2-133e42fdb3cd}')
    @winrt_commethod(6)
    def get_OriginalKey(self) -> win32more.Windows.System.VirtualKey: ...
    OriginalKey = property(get_OriginalKey, None)
class IKeyRoutedEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyRoutedEventArgs3'
    _iid_ = Guid('{2779f5b4-ca41-411b-a8ef-f4fc78e78057}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IKeyboardAccelerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyboardAccelerator'
    _iid_ = Guid('{92e6181e-19ae-465a-9b3c-a71ee9ea7420}')
    @winrt_commethod(6)
    def get_Key(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def put_Key(self, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(8)
    def get_Modifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(9)
    def put_Modifiers(self, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_commethod(10)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_ScopeOwner(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ScopeOwner(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def add_Invoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Input.KeyboardAccelerator, win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Invoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Key = property(get_Key, put_Key)
    Modifiers = property(get_Modifiers, put_Modifiers)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ScopeOwner = property(get_ScopeOwner, put_ScopeOwner)
class IKeyboardAcceleratorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyboardAcceleratorFactory'
    _iid_ = Guid('{44d88a99-4bfd-4a47-a893-515f388623f6}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.KeyboardAccelerator: ...
class IKeyboardAcceleratorInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs'
    _iid_ = Guid('{c00b03f2-04e7-4415-b17d-d76b9490de2b}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Element(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    Handled = property(get_Handled, put_Handled)
    Element = property(get_Element, None)
class IKeyboardAcceleratorInvokedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs2'
    _iid_ = Guid('{befca4b8-5907-48ee-8e21-9c969078fa11}')
    @winrt_commethod(6)
    def get_KeyboardAccelerator(self) -> win32more.Windows.UI.Xaml.Input.KeyboardAccelerator: ...
    KeyboardAccelerator = property(get_KeyboardAccelerator, None)
class IKeyboardAcceleratorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics'
    _iid_ = Guid('{3bd43d51-9bb3-456d-bf15-804adfb86261}')
    @winrt_commethod(6)
    def get_KeyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ModifiersProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScopeOwnerProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KeyProperty = property(get_KeyProperty, None)
    ModifiersProperty = property(get_ModifiersProperty, None)
    IsEnabledProperty = property(get_IsEnabledProperty, None)
    ScopeOwnerProperty = property(get_ScopeOwnerProperty, None)
class ILosingFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.ILosingFocusEventArgs'
    _iid_ = Guid('{f9f683c7-d789-472b-aa93-6d4105e6dabe}')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_NewFocusedElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def put_NewFocusedElement(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(9)
    def get_FocusState(self) -> win32more.Windows.UI.Xaml.FocusState: ...
    @winrt_commethod(10)
    def get_Direction(self) -> win32more.Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_InputDevice(self) -> win32more.Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.ILosingFocusEventArgs2'
    _iid_ = Guid('{0493fad9-c27f-469f-8e62-52b3a4f7cd54}')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetNewFocusedElement(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
class ILosingFocusEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.ILosingFocusEventArgs3'
    _iid_ = Guid('{c98900bd-0b79-566e-ad1f-436fa513ae22}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
class IManipulationCompletedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs'
    _iid_ = Guid('{b5ad9b23-2f41-498e-8319-015ee8a75346}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    IsInertial = property(get_IsInertial, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IManipulationDeltaRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs'
    _iid_ = Guid('{400d5794-4c6f-491d-82d6-3517109399c6}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Delta(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(11)
    def get_Velocities(self) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    @winrt_commethod(12)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs'
    _iid_ = Guid('{246a91a9-ca43-4c0b-acef-81e8b8147520}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_ExpansionBehavior(self) -> win32more.Windows.UI.Xaml.Input.InertiaExpansionBehavior: ...
    @winrt_commethod(8)
    def put_ExpansionBehavior(self, value: win32more.Windows.UI.Xaml.Input.InertiaExpansionBehavior) -> Void: ...
    @winrt_commethod(9)
    def get_RotationBehavior(self) -> win32more.Windows.UI.Xaml.Input.InertiaRotationBehavior: ...
    @winrt_commethod(10)
    def put_RotationBehavior(self, value: win32more.Windows.UI.Xaml.Input.InertiaRotationBehavior) -> Void: ...
    @winrt_commethod(11)
    def get_TranslationBehavior(self) -> win32more.Windows.UI.Xaml.Input.InertiaTranslationBehavior: ...
    @winrt_commethod(12)
    def put_TranslationBehavior(self, value: win32more.Windows.UI.Xaml.Input.InertiaTranslationBehavior) -> Void: ...
    @winrt_commethod(13)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(16)
    def get_Delta(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(17)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(18)
    def get_Velocities(self) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationPivot'
    _iid_ = Guid('{2e3838a5-e6c2-4998-82ac-18748b141666}')
    @winrt_commethod(6)
    def get_Center(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Center(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Radius(self) -> Double: ...
    @winrt_commethod(9)
    def put_Radius(self, value: Double) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class IManipulationPivotFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationPivotFactory'
    _iid_ = Guid('{6d05b039-3702-4396-ad9b-a825efa63a3b}')
    @winrt_commethod(6)
    def CreateInstanceWithCenterAndRadius(self, center: win32more.Windows.Foundation.Point, radius: Double) -> win32more.Windows.UI.Xaml.Input.ManipulationPivot: ...
class IManipulationStartedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs'
    _iid_ = Guid('{5db1aa05-9f80-48b6-ae6c-4f119de8ff13}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(11)
    def get_Cumulative(self) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_commethod(12)
    def Complete(self) -> Void: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Cumulative = property(get_Cumulative, None)
class IManipulationStartedRoutedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgsFactory'
    _iid_ = Guid('{84c1daa7-7272-4463-b6c3-a40b9ba151fc}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs: ...
class IManipulationStartingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs'
    _iid_ = Guid('{18d636b7-53a4-4c15-a498-f3a9ca212a42}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_commethod(8)
    def get_Container(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Container(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def get_Pivot(self) -> win32more.Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_commethod(11)
    def put_Pivot(self, value: win32more.Windows.UI.Xaml.Input.ManipulationPivot) -> Void: ...
    @winrt_commethod(12)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_Handled(self, value: Boolean) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Container = property(get_Container, put_Container)
    Pivot = property(get_Pivot, put_Pivot)
    Handled = property(get_Handled, put_Handled)
class INoFocusCandidateFoundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs'
    _iid_ = Guid('{ec3601a7-1007-48f9-b6b3-ed0bea53937d}')
    @winrt_commethod(6)
    def get_Direction(self) -> win32more.Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_InputDevice(self) -> win32more.Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
class IPointer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IPointer'
    _iid_ = Guid('{5ee8f39f-747d-4171-90e6-cd37a9dffb11}')
    @winrt_commethod(6)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_IsInContact(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsInRange(self) -> Boolean: ...
    PointerId = property(get_PointerId, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    IsInContact = property(get_IsInContact, None)
    IsInRange = property(get_IsInRange, None)
class IPointerRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IPointerRoutedEventArgs'
    _iid_ = Guid('{da628f0a-9752-49e2-bde2-49eccab9194d}')
    @winrt_commethod(6)
    def get_Pointer(self) -> win32more.Windows.UI.Xaml.Input.Pointer: ...
    @winrt_commethod(7)
    def get_KeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetCurrentPoint(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(11)
    def GetIntermediatePoints(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]: ...
    Pointer = property(get_Pointer, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Handled = property(get_Handled, put_Handled)
class IPointerRoutedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IPointerRoutedEventArgs2'
    _iid_ = Guid('{0821f294-1de6-4711-ba7c-8d4b8b0911d0}')
    @winrt_commethod(6)
    def get_IsGenerated(self) -> Boolean: ...
    IsGenerated = property(get_IsGenerated, None)
class IProcessKeyboardAcceleratorEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs'
    _iid_ = Guid('{fb79c216-972b-440c-9b83-2b4198dcf09d}')
    @winrt_commethod(6)
    def get_Key(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def get_Modifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Key = property(get_Key, None)
    Modifiers = property(get_Modifiers, None)
    Handled = property(get_Handled, put_Handled)
class IRightTappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs'
    _iid_ = Guid('{6834869d-7bd5-4033-b237-172f79abe393}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class IStandardUICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IStandardUICommand'
    _iid_ = Guid('{d2bf7f43-0504-52d0-8aa6-0cb0f756eb27}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.UI.Xaml.Input.StandardUICommandKind: ...
    Kind = property(get_Kind, None)
class IStandardUICommand2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IStandardUICommand2'
    _iid_ = Guid('{e3666069-f9e4-51eb-885b-7a620a0782ea}')
    @winrt_commethod(6)
    def put_Kind(self, value: win32more.Windows.UI.Xaml.Input.StandardUICommandKind) -> Void: ...
    Kind = property(None, put_Kind)
class IStandardUICommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IStandardUICommandFactory'
    _iid_ = Guid('{8f1a7590-dce1-56e4-ab63-f5ce3ce4ebf6}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.StandardUICommand: ...
    @winrt_commethod(7)
    def CreateInstanceWithKind(self, kind: win32more.Windows.UI.Xaml.Input.StandardUICommandKind, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.StandardUICommand: ...
class IStandardUICommandStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IStandardUICommandStatics'
    _iid_ = Guid('{7ea87ed9-2978-5533-9b2e-6759ce88569f}')
    @winrt_commethod(6)
    def get_KindProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    KindProperty = property(get_KindProperty, None)
class ITappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.ITappedRoutedEventArgs'
    _iid_ = Guid('{a099e6be-e624-459a-bb1d-e05c73e2cc66}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class IXamlUICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IXamlUICommand'
    _iid_ = Guid('{8494f8d4-ead1-5f01-ad2e-a8cad4f9dc0e}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IconSource(self) -> win32more.Windows.UI.Xaml.Controls.IconSource: ...
    @winrt_commethod(9)
    def put_IconSource(self, value: win32more.Windows.UI.Xaml.Controls.IconSource) -> Void: ...
    @winrt_commethod(10)
    def get_KeyboardAccelerators(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_commethod(11)
    def get_AccessKey(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_AccessKey(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Command(self) -> win32more.Windows.UI.Xaml.Input.ICommand: ...
    @winrt_commethod(16)
    def put_Command(self, value: win32more.Windows.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_commethod(17)
    def add_ExecuteRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Input.XamlUICommand, win32more.Windows.UI.Xaml.Input.ExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ExecuteRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_CanExecuteRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Input.XamlUICommand, win32more.Windows.UI.Xaml.Input.CanExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_CanExecuteRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def NotifyCanExecuteChanged(self) -> Void: ...
    Label = property(get_Label, put_Label)
    IconSource = property(get_IconSource, put_IconSource)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    AccessKey = property(get_AccessKey, put_AccessKey)
    Description = property(get_Description, put_Description)
    Command = property(get_Command, put_Command)
class IXamlUICommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IXamlUICommandFactory'
    _iid_ = Guid('{1eec08c3-e061-5e10-9f2a-2baa840885c2}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.XamlUICommand: ...
class IXamlUICommandStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IXamlUICommandStatics'
    _iid_ = Guid('{66bc457c-1a0c-58ed-876e-71533f966db6}')
    @winrt_commethod(6)
    def get_LabelProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IconSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_KeyboardAcceleratorsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AccessKeyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DescriptionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_CommandProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    LabelProperty = property(get_LabelProperty, None)
    IconSourceProperty = property(get_IconSourceProperty, None)
    KeyboardAcceleratorsProperty = property(get_KeyboardAcceleratorsProperty, None)
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    DescriptionProperty = property(get_DescriptionProperty, None)
    CommandProperty = property(get_CommandProperty, None)
class InertiaExpansionBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IInertiaExpansionBehavior
    _classid_ = 'Windows.UI.Xaml.Input.InertiaExpansionBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: win32more.Windows.UI.Xaml.Input.IInertiaExpansionBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: win32more.Windows.UI.Xaml.Input.IInertiaExpansionBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredExpansion(self: win32more.Windows.UI.Xaml.Input.IInertiaExpansionBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredExpansion(self: win32more.Windows.UI.Xaml.Input.IInertiaExpansionBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredExpansion = property(get_DesiredExpansion, put_DesiredExpansion)
class InertiaRotationBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IInertiaRotationBehavior
    _classid_ = 'Windows.UI.Xaml.Input.InertiaRotationBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: win32more.Windows.UI.Xaml.Input.IInertiaRotationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: win32more.Windows.UI.Xaml.Input.IInertiaRotationBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredRotation(self: win32more.Windows.UI.Xaml.Input.IInertiaRotationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredRotation(self: win32more.Windows.UI.Xaml.Input.IInertiaRotationBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredRotation = property(get_DesiredRotation, put_DesiredRotation)
class InertiaTranslationBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IInertiaTranslationBehavior
    _classid_ = 'Windows.UI.Xaml.Input.InertiaTranslationBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: win32more.Windows.UI.Xaml.Input.IInertiaTranslationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: win32more.Windows.UI.Xaml.Input.IInertiaTranslationBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredDisplacement(self: win32more.Windows.UI.Xaml.Input.IInertiaTranslationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDisplacement(self: win32more.Windows.UI.Xaml.Input.IInertiaTranslationBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredDisplacement = property(get_DesiredDisplacement, put_DesiredDisplacement)
class InputScope(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Input.IInputScope
    _classid_ = 'Windows.UI.Xaml.Input.InputScope'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.InputScope: ...
    @winrt_mixinmethod
    def get_Names(self: win32more.Windows.UI.Xaml.Input.IInputScope) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Input.InputScopeName]: ...
    Names = property(get_Names, None)
class InputScopeName(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Input.IInputScopeName
    _classid_ = 'Windows.UI.Xaml.Input.InputScopeName'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.InputScopeName: ...
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Input.IInputScopeNameFactory, nameValue: win32more.Windows.UI.Xaml.Input.InputScopeNameValue) -> win32more.Windows.UI.Xaml.Input.InputScopeName: ...
    @winrt_mixinmethod
    def get_NameValue(self: win32more.Windows.UI.Xaml.Input.IInputScopeName) -> win32more.Windows.UI.Xaml.Input.InputScopeNameValue: ...
    @winrt_mixinmethod
    def put_NameValue(self: win32more.Windows.UI.Xaml.Input.IInputScopeName, value: win32more.Windows.UI.Xaml.Input.InputScopeNameValue) -> Void: ...
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
class KeyEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c63d2e5-7a0e-4e12-b96a-7715aa6ff1c8}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.KeyRoutedEventArgs) -> Void: ...
class KeyRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IKeyRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.KeyRoutedEventArgs'
    @winrt_mixinmethod
    def get_Key(self: win32more.Windows.UI.Xaml.Input.IKeyRoutedEventArgs) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Windows.UI.Xaml.Input.IKeyRoutedEventArgs) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IKeyRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IKeyRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalKey(self: win32more.Windows.UI.Xaml.Input.IKeyRoutedEventArgs2) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.UI.Xaml.Input.IKeyRoutedEventArgs3) -> WinRT_String: ...
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
class _KeyboardAccelerator_Meta_(ComPtr.__class__):
    pass
class KeyboardAccelerator(ComPtr, metaclass=_KeyboardAccelerator_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator
    _classid_ = 'Windows.UI.Xaml.Input.KeyboardAccelerator'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.KeyboardAccelerator: ...
    @winrt_mixinmethod
    def get_Key(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_Key(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_Modifiers(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_Modifiers(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ScopeOwner(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ScopeOwner(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def add_Invoked(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Input.KeyboardAccelerator, win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Invoked(self: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_KeyProperty(cls: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ModifiersProperty(cls: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScopeOwnerProperty(cls: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Key = property(get_Key, put_Key)
    Modifiers = property(get_Modifiers, put_Modifiers)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ScopeOwner = property(get_ScopeOwner, put_ScopeOwner)
    _KeyboardAccelerator_Meta_.KeyProperty = property(get_KeyProperty.__wrapped__, None)
    _KeyboardAccelerator_Meta_.ModifiersProperty = property(get_ModifiersProperty.__wrapped__, None)
    _KeyboardAccelerator_Meta_.IsEnabledProperty = property(get_IsEnabledProperty.__wrapped__, None)
    _KeyboardAccelerator_Meta_.ScopeOwnerProperty = property(get_ScopeOwnerProperty.__wrapped__, None)
class KeyboardAcceleratorInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Element(self: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_KeyboardAccelerator(self: win32more.Windows.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs2) -> win32more.Windows.UI.Xaml.Input.KeyboardAccelerator: ...
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
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.LosingFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_NewFocusedElement(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_NewFocusedElement(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_FocusState(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Windows.UI.Xaml.FocusState: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryCancel(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetNewFocusedElement(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs2, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.UI.Xaml.Input.ILosingFocusEventArgs3) -> Guid: ...
    OldFocusedElement = property(get_OldFocusedElement, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    FocusState = property(get_FocusState, None)
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
class ManipulationCompletedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{38ef4b0f-14f8-42df-9a1e-a4bcc4af77f4}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs) -> Void: ...
class ManipulationCompletedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_IsInertial(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    IsInertial = property(get_IsInertial, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class ManipulationDeltaEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa1160cb-dfb9-4c56-abdc-711b63c8eb94}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs) -> Void: ...
class ManipulationDeltaRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_IsInertial(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Delta(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Void: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    IsInertial = property(get_IsInertial, None)
    Delta = property(get_Delta, None)
    Cumulative = property(get_Cumulative, None)
    Velocities = property(get_Velocities, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class ManipulationInertiaStartingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d39d6322-7c9c-481b-827b-c8b2d9bb6fc7}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs) -> Void: ...
class ManipulationInertiaStartingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_ExpansionBehavior(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.UI.Xaml.Input.InertiaExpansionBehavior: ...
    @winrt_mixinmethod
    def put_ExpansionBehavior(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: win32more.Windows.UI.Xaml.Input.InertiaExpansionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_RotationBehavior(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.UI.Xaml.Input.InertiaRotationBehavior: ...
    @winrt_mixinmethod
    def put_RotationBehavior(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: win32more.Windows.UI.Xaml.Input.InertiaRotationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationBehavior(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.UI.Xaml.Input.InertiaTranslationBehavior: ...
    @winrt_mixinmethod
    def put_TranslationBehavior(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: win32more.Windows.UI.Xaml.Input.InertiaTranslationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Delta(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationVelocities: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationPivot
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationPivot'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_factorymethod
    def CreateInstanceWithCenterAndRadius(cls: win32more.Windows.UI.Xaml.Input.IManipulationPivotFactory, center: win32more.Windows.Foundation.Point, radius: Double) -> win32more.Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.UI.Xaml.Input.IManipulationPivot) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Center(self: win32more.Windows.UI.Xaml.Input.IManipulationPivot, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Radius(self: win32more.Windows.UI.Xaml.Input.IManipulationPivot) -> Double: ...
    @winrt_mixinmethod
    def put_Radius(self: win32more.Windows.UI.Xaml.Input.IManipulationPivot, value: Double) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class ManipulationStartedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f88345f8-e0a3-4be2-b90c-dc20e6d8beb0}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs) -> Void: ...
class ManipulationStartedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Windows.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> Void: ...
    Container = property(get_Container, None)
    Position = property(get_Position, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Cumulative = property(get_Cumulative, None)
class ManipulationStartingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10d0b04e-bfe4-42cb-823c-3fecd8770ef8}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs) -> Void: ...
class ManipulationStartingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> win32more.Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: win32more.Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Container(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_Pivot(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> win32more.Windows.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_mixinmethod
    def put_Pivot(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: win32more.Windows.UI.Xaml.Input.ManipulationPivot) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: Boolean) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Container = property(get_Container, put_Container)
    Pivot = property(get_Pivot, put_Pivot)
    Handled = property(get_Handled, put_Handled)
class NoFocusCandidateFoundEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.NoFocusCandidateFoundEventArgs'
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> win32more.Windows.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: win32more.Windows.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> win32more.Windows.UI.Xaml.Input.FocusInputDeviceKind: ...
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
class Pointer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IPointer
    _classid_ = 'Windows.UI.Xaml.Input.Pointer'
    @winrt_mixinmethod
    def get_PointerId(self: win32more.Windows.UI.Xaml.Input.IPointer) -> UInt32: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IPointer) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_IsInContact(self: win32more.Windows.UI.Xaml.Input.IPointer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInRange(self: win32more.Windows.UI.Xaml.Input.IPointer) -> Boolean: ...
    PointerId = property(get_PointerId, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    IsInContact = property(get_IsInContact, None)
    IsInRange = property(get_IsInRange, None)
class PointerEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e4385929-c004-4bcf-8970-359486e39f88}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.PointerRoutedEventArgs) -> Void: ...
class PointerRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.PointerRoutedEventArgs'
    @winrt_mixinmethod
    def get_Pointer(self: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs) -> win32more.Windows.UI.Xaml.Input.Pointer: ...
    @winrt_mixinmethod
    def get_KeyModifiers(self: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentPoint(self: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_mixinmethod
    def GetIntermediatePoints(self: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.PointerPoint]: ...
    @winrt_mixinmethod
    def get_IsGenerated(self: win32more.Windows.UI.Xaml.Input.IPointerRoutedEventArgs2) -> Boolean: ...
    Pointer = property(get_Pointer, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Handled = property(get_Handled, put_Handled)
    IsGenerated = property(get_IsGenerated, None)
class ProcessKeyboardAcceleratorEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs'
    @winrt_mixinmethod
    def get_Key(self: win32more.Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_Modifiers(self: win32more.Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs, value: Boolean) -> Void: ...
    Key = property(get_Key, None)
    Modifiers = property(get_Modifiers, None)
    Handled = property(get_Handled, put_Handled)
class RightTappedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2532a062-f447-4950-9c46-f1e34a2c2238}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.RightTappedRoutedEventArgs) -> Void: ...
class RightTappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.RightTappedRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.RightTappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Handled = property(get_Handled, put_Handled)
class _StandardUICommand_Meta_(ComPtr.__class__):
    pass
class StandardUICommand(ComPtr, metaclass=_StandardUICommand_Meta_):
    extends: win32more.Windows.UI.Xaml.Input.XamlUICommand
    default_interface: win32more.Windows.UI.Xaml.Input.IStandardUICommand
    _classid_ = 'Windows.UI.Xaml.Input.StandardUICommand'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Input.IStandardUICommandFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.StandardUICommand: ...
    @winrt_factorymethod
    def CreateInstanceWithKind(cls: win32more.Windows.UI.Xaml.Input.IStandardUICommandFactory, kind: win32more.Windows.UI.Xaml.Input.StandardUICommandKind, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.StandardUICommand: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Xaml.Input.IStandardUICommand) -> win32more.Windows.UI.Xaml.Input.StandardUICommandKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.UI.Xaml.Input.IStandardUICommand2, value: win32more.Windows.UI.Xaml.Input.StandardUICommandKind) -> Void: ...
    @winrt_classmethod
    def get_KindProperty(cls: win32more.Windows.UI.Xaml.Input.IStandardUICommandStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Kind = property(get_Kind, put_Kind)
    _StandardUICommand_Meta_.KindProperty = property(get_KindProperty.__wrapped__, None)
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
class TappedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68d940cc-9ff0-49ce-b141-3f07ec477b97}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.TappedRoutedEventArgs) -> Void: ...
class TappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.ITappedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.TappedRoutedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.TappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.UI.Xaml.Input.ITappedRoutedEventArgs) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Input.ITappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Input.ITappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Windows.UI.Xaml.Input.ITappedRoutedEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
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
class _XamlUICommand_Meta_(ComPtr.__class__):
    pass
class XamlUICommand(ComPtr, metaclass=_XamlUICommand_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Input.IXamlUICommand
    _classid_ = 'Windows.UI.Xaml.Input.XamlUICommand'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Input.IXamlUICommandFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Input.XamlUICommand: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IconSource(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand) -> win32more.Windows.UI.Xaml.Controls.IconSource: ...
    @winrt_mixinmethod
    def put_IconSource(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, value: win32more.Windows.UI.Xaml.Controls.IconSource) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAccelerators(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_mixinmethod
    def get_AccessKey(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AccessKey(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand) -> win32more.Windows.UI.Xaml.Input.ICommand: ...
    @winrt_mixinmethod
    def put_Command(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, value: win32more.Windows.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_mixinmethod
    def add_ExecuteRequested(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Input.XamlUICommand, win32more.Windows.UI.Xaml.Input.ExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ExecuteRequested(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CanExecuteRequested(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Input.XamlUICommand, win32more.Windows.UI.Xaml.Input.CanExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CanExecuteRequested(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyCanExecuteChanged(self: win32more.Windows.UI.Xaml.Input.IXamlUICommand) -> Void: ...
    @winrt_mixinmethod
    def add_CanExecuteChanged(self: win32more.Windows.UI.Xaml.Input.ICommand, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CanExecuteChanged(self: win32more.Windows.UI.Xaml.Input.ICommand, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CanExecute(self: win32more.Windows.UI.Xaml.Input.ICommand, parameter: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Execute(self: win32more.Windows.UI.Xaml.Input.ICommand, parameter: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_classmethod
    def get_LabelProperty(cls: win32more.Windows.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IconSourceProperty(cls: win32more.Windows.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyboardAcceleratorsProperty(cls: win32more.Windows.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: win32more.Windows.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DescriptionProperty(cls: win32more.Windows.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CommandProperty(cls: win32more.Windows.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Label = property(get_Label, put_Label)
    IconSource = property(get_IconSource, put_IconSource)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    AccessKey = property(get_AccessKey, put_AccessKey)
    Description = property(get_Description, put_Description)
    Command = property(get_Command, put_Command)
    _XamlUICommand_Meta_.LabelProperty = property(get_LabelProperty.__wrapped__, None)
    _XamlUICommand_Meta_.IconSourceProperty = property(get_IconSourceProperty.__wrapped__, None)
    _XamlUICommand_Meta_.KeyboardAcceleratorsProperty = property(get_KeyboardAcceleratorsProperty.__wrapped__, None)
    _XamlUICommand_Meta_.AccessKeyProperty = property(get_AccessKeyProperty.__wrapped__, None)
    _XamlUICommand_Meta_.DescriptionProperty = property(get_DescriptionProperty.__wrapped__, None)
    _XamlUICommand_Meta_.CommandProperty = property(get_CommandProperty.__wrapped__, None)
make_ready(__name__)
