from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Input
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Controls
import win32more.Windows.UI.Xaml.Input
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AccessKeyDisplayDismissedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IAccessKeyDisplayDismissedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs: ...
class AccessKeyDisplayRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_PressedKeys(self: win32more.Windows.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs) -> WinRT_String: ...
    PressedKeys = property(get_PressedKeys, None)
class AccessKeyInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IAccessKeyInvokedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    _AccessKeyManager_Meta_.AreKeyTipsEnabled = property(get_AreKeyTipsEnabled, put_AreKeyTipsEnabled)
    _AccessKeyManager_Meta_.IsDisplayModeEnabled = property(get_IsDisplayModeEnabled, None)
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
    CanExecute = property(get_CanExecute, put_CanExecute)
    Parameter = property(get_Parameter, None)
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
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
class ContextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IContextRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ContextRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ContextRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs) -> Void: ...
class DoubleTappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.DoubleTappedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.FindNextElementOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    HintRect = property(get_HintRect, put_HintRect)
    SearchRoot = property(get_SearchRoot, put_SearchRoot)
    XYFocusNavigationStrategyOverride = property(get_XYFocusNavigationStrategyOverride, put_XYFocusNavigationStrategyOverride)
class FocusInputDeviceKind(Enum, Int32):
    None_ = 0
    Mouse = 1
    Touch = 2
    Pen = 3
    Keyboard = 4
    GameController = 5
class FocusManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFocusManager
    _classid_ = 'Windows.UI.Xaml.Input.FocusManager'
    @winrt_overload
    @winrt_classmethod
    def GetFocusedElement(cls: win32more.Windows.UI.Xaml.Input.IFocusManagerStatics7, xamlRoot: win32more.Windows.UI.Xaml.XamlRoot) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
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
    @GetFocusedElement.register
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
    CorrelationId = property(get_CorrelationId, None)
    NewFocusedElement = property(get_NewFocusedElement, None)
class FocusManagerLostFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.FocusManagerLostFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: win32more.Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    OldFocusedElement = property(get_OldFocusedElement, None)
class FocusMovementResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IFocusMovementResult
    _classid_ = 'Windows.UI.Xaml.Input.FocusMovementResult'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.UI.Xaml.Input.IFocusMovementResult) -> Boolean: ...
    Succeeded = property(get_Succeeded, None)
class FocusNavigationDirection(Enum, Int32):
    Next = 0
    Previous = 1
    Up = 2
    Down = 3
    Left = 4
    Right = 5
    None_ = 6
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
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
    Direction = property(get_Direction, None)
    FocusState = property(get_FocusState, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    OldFocusedElement = property(get_OldFocusedElement, None)
class HoldingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ecae8ccd-8e5e-4fbe-9846-30a6370afcdf}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.HoldingRoutedEventArgs) -> Void: ...
class HoldingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IHoldingRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.HoldingRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.HoldingRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Handled = property(get_Handled, put_Handled)
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
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
    IsDisplayModeEnabledChanged = event()
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
    CanExecute = property(get_CanExecute, put_CanExecute)
    Parameter = property(get_Parameter, None)
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
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
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
    CanExecuteChanged = event()
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
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
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
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    HintRect = property(get_HintRect, put_HintRect)
    SearchRoot = property(get_SearchRoot, put_SearchRoot)
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
    CorrelationId = property(get_CorrelationId, None)
    NewFocusedElement = property(get_NewFocusedElement, None)
class IFocusManagerLostFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Input.IFocusManagerLostFocusEventArgs'
    _iid_ = Guid('{3e157e7a-9578-5cd3-aaa8-051b3d391978}')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    OldFocusedElement = property(get_OldFocusedElement, None)
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
    GotFocus = event()
    LostFocus = event()
    GettingFocus = event()
    LosingFocus = event()
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
    Cancel = property(get_Cancel, put_Cancel)
    Direction = property(get_Direction, None)
    FocusState = property(get_FocusState, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    OldFocusedElement = property(get_OldFocusedElement, None)
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
    Handled = property(get_Handled, put_Handled)
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
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
    Handled = property(get_Handled, put_Handled)
    Key = property(get_Key, None)
    KeyStatus = property(get_KeyStatus, None)
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
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Key = property(get_Key, put_Key)
    Modifiers = property(get_Modifiers, put_Modifiers)
    ScopeOwner = property(get_ScopeOwner, put_ScopeOwner)
    Invoked = event()
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
    Element = property(get_Element, None)
    Handled = property(get_Handled, put_Handled)
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
    IsEnabledProperty = property(get_IsEnabledProperty, None)
    KeyProperty = property(get_KeyProperty, None)
    ModifiersProperty = property(get_ModifiersProperty, None)
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
    Cancel = property(get_Cancel, put_Cancel)
    Direction = property(get_Direction, None)
    FocusState = property(get_FocusState, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    OldFocusedElement = property(get_OldFocusedElement, None)
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
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    IsInertial = property(get_IsInertial, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
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
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    Handled = property(get_Handled, put_Handled)
    IsInertial = property(get_IsInertial, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
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
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    ExpansionBehavior = property(get_ExpansionBehavior, put_ExpansionBehavior)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    RotationBehavior = property(get_RotationBehavior, put_RotationBehavior)
    TranslationBehavior = property(get_TranslationBehavior, put_TranslationBehavior)
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
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
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
    Container = property(get_Container, put_Container)
    Handled = property(get_Handled, put_Handled)
    Mode = property(get_Mode, put_Mode)
    Pivot = property(get_Pivot, put_Pivot)
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
    IsInContact = property(get_IsInContact, None)
    IsInRange = property(get_IsInRange, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    PointerId = property(get_PointerId, None)
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
    Handled = property(get_Handled, put_Handled)
    KeyModifiers = property(get_KeyModifiers, None)
    Pointer = property(get_Pointer, None)
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
    Handled = property(get_Handled, put_Handled)
    Key = property(get_Key, None)
    Modifiers = property(get_Modifiers, None)
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
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
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
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
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
    AccessKey = property(get_AccessKey, put_AccessKey)
    Command = property(get_Command, put_Command)
    Description = property(get_Description, put_Description)
    IconSource = property(get_IconSource, put_IconSource)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    Label = property(get_Label, put_Label)
    ExecuteRequested = event()
    CanExecuteRequested = event()
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
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    CommandProperty = property(get_CommandProperty, None)
    DescriptionProperty = property(get_DescriptionProperty, None)
    IconSourceProperty = property(get_IconSourceProperty, None)
    KeyboardAcceleratorsProperty = property(get_KeyboardAcceleratorsProperty, None)
    LabelProperty = property(get_LabelProperty, None)
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.InputScope.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.InputScope: ...
    @winrt_mixinmethod
    def get_Names(self: win32more.Windows.UI.Xaml.Input.IInputScope) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Input.InputScopeName]: ...
    Names = property(get_Names, None)
class InputScopeName(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Input.IInputScopeName
    _classid_ = 'Windows.UI.Xaml.Input.InputScopeName'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.InputScopeName.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.InputScopeName.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Input.InputScopeName: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Input.IInputScopeNameFactory, nameValue: win32more.Windows.UI.Xaml.Input.InputScopeNameValue) -> win32more.Windows.UI.Xaml.Input.InputScopeName: ...
    @winrt_mixinmethod
    def get_NameValue(self: win32more.Windows.UI.Xaml.Input.IInputScopeName) -> win32more.Windows.UI.Xaml.Input.InputScopeNameValue: ...
    @winrt_mixinmethod
    def put_NameValue(self: win32more.Windows.UI.Xaml.Input.IInputScopeName, value: win32more.Windows.UI.Xaml.Input.InputScopeNameValue) -> Void: ...
    NameValue = property(get_NameValue, put_NameValue)
class InputScopeNameValue(Enum, Int32):
    Default = 0
    Url = 1
    EmailSmtpAddress = 5
    PersonalFullName = 7
    CurrencyAmountAndSymbol = 20
    CurrencyAmount = 21
    DateMonthNumber = 23
    DateDayNumber = 24
    DateYear = 25
    Digits = 28
    Number = 29
    Password = 31
    TelephoneNumber = 32
    TelephoneCountryCode = 33
    TelephoneAreaCode = 34
    TelephoneLocalNumber = 35
    TimeHour = 37
    TimeMinutesOrSeconds = 38
    NumberFullWidth = 39
    AlphanumericHalfWidth = 40
    AlphanumericFullWidth = 41
    Hiragana = 44
    KatakanaHalfWidth = 45
    KatakanaFullWidth = 46
    Hanja = 47
    HangulHalfWidth = 48
    HangulFullWidth = 49
    Search = 50
    Formula = 51
    SearchIncremental = 52
    ChineseHalfWidth = 53
    ChineseFullWidth = 54
    NativeScript = 55
    Text = 57
    Chat = 58
    NameOrPhoneNumber = 59
    EmailNameOrAddress = 60
    Private = 61
    Maps = 62
    NumericPassword = 63
    NumericPin = 64
    AlphanumericPin = 65
    FormulaNumber = 67
    ChatWithoutEmoji = 68
class KeyEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c63d2e5-7a0e-4e12-b96a-7715aa6ff1c8}')
    @winrt_commethod(3)
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
    DeviceId = property(get_DeviceId, None)
    Handled = property(get_Handled, put_Handled)
    Key = property(get_Key, None)
    KeyStatus = property(get_KeyStatus, None)
    OriginalKey = property(get_OriginalKey, None)
class KeyTipPlacementMode(Enum, Int32):
    Auto = 0
    Bottom = 1
    Top = 2
    Left = 3
    Right = 4
    Center = 5
    Hidden = 6
class _KeyboardAccelerator_Meta_(ComPtr.__class__):
    pass
class KeyboardAccelerator(ComPtr, metaclass=_KeyboardAccelerator_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Input.IKeyboardAccelerator
    _classid_ = 'Windows.UI.Xaml.Input.KeyboardAccelerator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.KeyboardAccelerator.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
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
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Key = property(get_Key, put_Key)
    Modifiers = property(get_Modifiers, put_Modifiers)
    ScopeOwner = property(get_ScopeOwner, put_ScopeOwner)
    _KeyboardAccelerator_Meta_.IsEnabledProperty = property(get_IsEnabledProperty, None)
    _KeyboardAccelerator_Meta_.KeyProperty = property(get_KeyProperty, None)
    _KeyboardAccelerator_Meta_.ModifiersProperty = property(get_ModifiersProperty, None)
    _KeyboardAccelerator_Meta_.ScopeOwnerProperty = property(get_ScopeOwnerProperty, None)
    Invoked = event()
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
    Element = property(get_Element, None)
    Handled = property(get_Handled, put_Handled)
    KeyboardAccelerator = property(get_KeyboardAccelerator, None)
class KeyboardAcceleratorPlacementMode(Enum, Int32):
    Auto = 0
    Hidden = 1
class KeyboardNavigationMode(Enum, Int32):
    Local = 0
    Cycle = 1
    Once = 2
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
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
    Direction = property(get_Direction, None)
    FocusState = property(get_FocusState, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    OldFocusedElement = property(get_OldFocusedElement, None)
class ManipulationCompletedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{38ef4b0f-14f8-42df-9a1e-a4bcc4af77f4}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs) -> Void: ...
class ManipulationCompletedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    IsInertial = property(get_IsInertial, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationDeltaEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa1160cb-dfb9-4c56-abdc-711b63c8eb94}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs) -> Void: ...
class ManipulationDeltaRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    Handled = property(get_Handled, put_Handled)
    IsInertial = property(get_IsInertial, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationInertiaStartingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d39d6322-7c9c-481b-827b-c8b2d9bb6fc7}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs) -> Void: ...
class ManipulationInertiaStartingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    ExpansionBehavior = property(get_ExpansionBehavior, put_ExpansionBehavior)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    RotationBehavior = property(get_RotationBehavior, put_RotationBehavior)
    TranslationBehavior = property(get_TranslationBehavior, put_TranslationBehavior)
    Velocities = property(get_Velocities, None)
class ManipulationModes(Enum, UInt32):
    None_ = 0
    TranslateX = 1
    TranslateY = 2
    TranslateRailsX = 4
    TranslateRailsY = 8
    Rotate = 16
    Scale = 32
    TranslateInertia = 64
    RotateInertia = 128
    ScaleInertia = 256
    All = 65535
    System = 65536
class ManipulationPivot(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationPivot
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationPivot'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ManipulationPivot.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ManipulationPivot.CreateInstanceWithCenterAndRadius(*args))
        else:
            raise ValueError('no matched constructor')
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
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs) -> Void: ...
class ManipulationStartedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ManipulationStartedRoutedEventArgs.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
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
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class ManipulationStartingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10d0b04e-bfe4-42cb-823c-3fecd8770ef8}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs) -> Void: ...
class ManipulationStartingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.ManipulationStartingRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Container = property(get_Container, put_Container)
    Handled = property(get_Handled, put_Handled)
    Mode = property(get_Mode, put_Mode)
    Pivot = property(get_Pivot, put_Pivot)
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
    IsInContact = property(get_IsInContact, None)
    IsInRange = property(get_IsInRange, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    PointerId = property(get_PointerId, None)
class PointerEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e4385929-c004-4bcf-8970-359486e39f88}')
    @winrt_commethod(3)
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
    Handled = property(get_Handled, put_Handled)
    IsGenerated = property(get_IsGenerated, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Pointer = property(get_Pointer, None)
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
    Handled = property(get_Handled, put_Handled)
    Key = property(get_Key, None)
    Modifiers = property(get_Modifiers, None)
class RightTappedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2532a062-f447-4950-9c46-f1e34a2c2238}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.RightTappedRoutedEventArgs) -> Void: ...
class RightTappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.RightTappedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.RightTappedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class _StandardUICommand_Meta_(ComPtr.__class__):
    pass
class StandardUICommand(ComPtr, metaclass=_StandardUICommand_Meta_):
    extends: win32more.Windows.UI.Xaml.Input.XamlUICommand
    default_interface: win32more.Windows.UI.Xaml.Input.IStandardUICommand
    _classid_ = 'Windows.UI.Xaml.Input.StandardUICommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.StandardUICommand.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.StandardUICommand.CreateInstanceWithKind(*args, None, None))
        else:
            raise ValueError('no matched constructor')
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
    _StandardUICommand_Meta_.KindProperty = property(get_KindProperty, None)
class StandardUICommandKind(Enum, Int32):
    None_ = 0
    Cut = 1
    Copy = 2
    Paste = 3
    SelectAll = 4
    Delete = 5
    Share = 6
    Save = 7
    Open = 8
    Close = 9
    Pause = 10
    Play = 11
    Stop = 12
    Forward = 13
    Backward = 14
    Undo = 15
    Redo = 16
class TappedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68d940cc-9ff0-49ce-b141-3f07ec477b97}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Input.TappedRoutedEventArgs) -> Void: ...
class TappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Input.ITappedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Input.TappedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.TappedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class XYFocusKeyboardNavigationMode(Enum, Int32):
    Auto = 0
    Enabled = 1
    Disabled = 2
class XYFocusNavigationStrategy(Enum, Int32):
    Auto = 0
    Projection = 1
    NavigationDirectionDistance = 2
    RectilinearDistance = 3
class XYFocusNavigationStrategyOverride(Enum, Int32):
    None_ = 0
    Auto = 1
    Projection = 2
    NavigationDirectionDistance = 3
    RectilinearDistance = 4
class _XamlUICommand_Meta_(ComPtr.__class__):
    pass
class XamlUICommand(ComPtr, metaclass=_XamlUICommand_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Input.IXamlUICommand
    _classid_ = 'Windows.UI.Xaml.Input.XamlUICommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Input.XamlUICommand.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
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
    AccessKey = property(get_AccessKey, put_AccessKey)
    Command = property(get_Command, put_Command)
    Description = property(get_Description, put_Description)
    IconSource = property(get_IconSource, put_IconSource)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    Label = property(get_Label, put_Label)
    _XamlUICommand_Meta_.AccessKeyProperty = property(get_AccessKeyProperty, None)
    _XamlUICommand_Meta_.CommandProperty = property(get_CommandProperty, None)
    _XamlUICommand_Meta_.DescriptionProperty = property(get_DescriptionProperty, None)
    _XamlUICommand_Meta_.IconSourceProperty = property(get_IconSourceProperty, None)
    _XamlUICommand_Meta_.KeyboardAcceleratorsProperty = property(get_KeyboardAcceleratorsProperty, None)
    _XamlUICommand_Meta_.LabelProperty = property(get_LabelProperty, None)
    ExecuteRequested = event()
    CanExecuteRequested = event()
    CanExecuteChanged = event()


make_ready(__name__)
