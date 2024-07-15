from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Input
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Controls
import win32more.Microsoft.UI.Xaml.Input
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.UI.Core
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AccessKeyDisplayDismissedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IAccessKeyDisplayDismissedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs: ...
class AccessKeyDisplayRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_PressedKeys(self: win32more.Microsoft.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs) -> WinRT_String: ...
    PressedKeys = property(get_PressedKeys, None)
class AccessKeyInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IAccessKeyInvokedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.AccessKeyInvokedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.AccessKeyInvokedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.AccessKeyInvokedEventArgs: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IAccessKeyInvokedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IAccessKeyInvokedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class _AccessKeyManager_Meta_(ComPtr.__class__):
    pass
class AccessKeyManager(ComPtr, metaclass=_AccessKeyManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManager
    _classid_ = 'Microsoft.UI.Xaml.Input.AccessKeyManager'
    @winrt_classmethod
    def EnterDisplayModeForXamlRoot(cls: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics2, XamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_classmethod
    def get_IsDisplayModeEnabled(cls: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def get_AreKeyTipsEnabled(cls: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def put_AreKeyTipsEnabled(cls: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def add_IsDisplayModeEnabledChanged(cls: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_IsDisplayModeEnabledChanged(cls: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def ExitDisplayMode(cls: win32more.Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics) -> Void: ...
    _AccessKeyManager_Meta_.AreKeyTipsEnabled = property(get_AreKeyTipsEnabled, put_AreKeyTipsEnabled)
    _AccessKeyManager_Meta_.IsDisplayModeEnabled = property(get_IsDisplayModeEnabled, None)
class CanExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.ICanExecuteRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.CanExecuteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Microsoft.UI.Xaml.Input.ICanExecuteRequestedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_CanExecute(self: win32more.Microsoft.UI.Xaml.Input.ICanExecuteRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanExecute(self: win32more.Microsoft.UI.Xaml.Input.ICanExecuteRequestedEventArgs, value: Boolean) -> Void: ...
    CanExecute = property(get_CanExecute, put_CanExecute)
    Parameter = property(get_Parameter, None)
class CharacterReceivedRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.CharacterReceivedRoutedEventArgs'
    @winrt_mixinmethod
    def get_Character(self: win32more.Microsoft.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> Char: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Microsoft.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs, value: Boolean) -> Void: ...
    Character = property(get_Character, None)
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
class ContextRequestedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IContextRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ContextRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ContextRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.ContextRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IContextRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IContextRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryGetPosition(self: win32more.Microsoft.UI.Xaml.Input.IContextRequestedEventArgs, relativeTo: win32more.Microsoft.UI.Xaml.UIElement, point: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class DoubleTappedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7a501b9-e277-5611-87b0-0e0607622183}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.DoubleTappedRoutedEventArgs) -> Void: ...
class DoubleTappedRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IDoubleTappedRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.DoubleTappedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.DoubleTappedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.DoubleTappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IDoubleTappedRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IDoubleTappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IDoubleTappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Microsoft.UI.Xaml.Input.IDoubleTappedRoutedEventArgs, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class ExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IExecuteRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ExecuteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Microsoft.UI.Xaml.Input.IExecuteRequestedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Parameter = property(get_Parameter, None)
class FindNextElementOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions
    _classid_ = 'Microsoft.UI.Xaml.Input.FindNextElementOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions: ...
    @winrt_mixinmethod
    def get_SearchRoot(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_SearchRoot(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_ExclusionRect(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_ExclusionRect(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_HintRect(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_HintRect(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusNavigationStrategyOverride(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions) -> win32more.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategyOverride: ...
    @winrt_mixinmethod
    def put_XYFocusNavigationStrategyOverride(self: win32more.Microsoft.UI.Xaml.Input.IFindNextElementOptions, value: win32more.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategyOverride) -> Void: ...
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
    default_interface: win32more.Microsoft.UI.Xaml.Input.IFocusManager
    _classid_ = 'Microsoft.UI.Xaml.Input.FocusManager'
    @winrt_classmethod
    def add_GotFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.FocusManagerGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GotFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LostFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.FocusManagerLostFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LostFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GettingFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.GettingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GettingFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LosingFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.LosingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LosingFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryFocusAsync(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.FocusState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusAsync(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusWithOptionsAsync(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_classmethod
    def TryMoveFocusWithOptions(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions) -> Boolean: ...
    @winrt_classmethod
    def FindNextElement(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindFirstFocusableElement(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, searchScope: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindLastFocusableElement(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, searchScope: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindNextElementWithOptions(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def FindNextFocusableElement(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def FindNextFocusableElementWithHint(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def TryMoveFocus(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> Boolean: ...
    @winrt_classmethod
    def GetFocusedElement(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def GetFocusedElementWithRoot(cls: win32more.Microsoft.UI.Xaml.Input.IFocusManagerStatics, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class FocusManagerGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IFocusManagerGotFocusEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.FocusManagerGotFocusEventArgs'
    @winrt_mixinmethod
    def get_NewFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.IFocusManagerGotFocusEventArgs) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Input.IFocusManagerGotFocusEventArgs) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    NewFocusedElement = property(get_NewFocusedElement, None)
class FocusManagerLostFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IFocusManagerLostFocusEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.FocusManagerLostFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Input.IFocusManagerLostFocusEventArgs) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    OldFocusedElement = property(get_OldFocusedElement, None)
class FocusMovementResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IFocusMovementResult
    _classid_ = 'Microsoft.UI.Xaml.Input.FocusMovementResult'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Microsoft.UI.Xaml.Input.IFocusMovementResult) -> Boolean: ...
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
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.GettingFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_NewFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_NewFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_FocusState(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.FocusState: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def TryCancel(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetNewFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.IGettingFocusEventArgs, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
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
    _iid_ = Guid('{fe23c5bd-4984-56b6-b92b-fc9d1216b24e}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.HoldingRoutedEventArgs) -> Void: ...
class HoldingRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IHoldingRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.HoldingRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.HoldingRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.HoldingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IHoldingRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_HoldingState(self: win32more.Microsoft.UI.Xaml.Input.IHoldingRoutedEventArgs) -> win32more.Microsoft.UI.Input.HoldingState: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IHoldingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IHoldingRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Microsoft.UI.Xaml.Input.IHoldingRoutedEventArgs, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IAccessKeyDisplayDismissedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IAccessKeyDisplayDismissedEventArgs'
    _iid_ = Guid('{125a83d8-7f86-5ea9-9063-b9407e644587}')
class IAccessKeyDisplayRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IAccessKeyDisplayRequestedEventArgs'
    _iid_ = Guid('{c4ed84d8-2b27-59b1-9cf0-7f9164de58cb}')
    @winrt_commethod(6)
    def get_PressedKeys(self) -> WinRT_String: ...
    PressedKeys = property(get_PressedKeys, None)
class IAccessKeyInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IAccessKeyInvokedEventArgs'
    _iid_ = Guid('{d00c11a4-f9fb-5707-9692-98b80bb8546d}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class IAccessKeyManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IAccessKeyManager'
    _iid_ = Guid('{8f2a4402-a635-53dc-bc17-da911eabaade}')
class IAccessKeyManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics'
    _iid_ = Guid('{3375aef7-742f-5e84-b76f-c187e08253bf}')
    @winrt_commethod(6)
    def get_IsDisplayModeEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AreKeyTipsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AreKeyTipsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def add_IsDisplayModeEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_IsDisplayModeEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def ExitDisplayMode(self) -> Void: ...
    AreKeyTipsEnabled = property(get_AreKeyTipsEnabled, put_AreKeyTipsEnabled)
    IsDisplayModeEnabled = property(get_IsDisplayModeEnabled, None)
    IsDisplayModeEnabledChanged = event()
class IAccessKeyManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IAccessKeyManagerStatics2'
    _iid_ = Guid('{512c9f63-24ad-5df2-b8ed-472406db31c0}')
    @winrt_commethod(6)
    def EnterDisplayModeForXamlRoot(self, XamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
class ICanExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.ICanExecuteRequestedEventArgs'
    _iid_ = Guid('{e4bf6d7d-f6eb-53ca-a2d4-c741ec871e38}')
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
    _classid_ = 'Microsoft.UI.Xaml.Input.ICharacterReceivedRoutedEventArgs'
    _iid_ = Guid('{e26ca5bb-34c3-5c1e-9a16-00b80b07a899}')
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
    _classid_ = 'Microsoft.UI.Xaml.Input.ICommand'
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IContextRequestedEventArgs'
    _iid_ = Guid('{bcedcb98-77b5-53c0-802e-fd52f3806e51}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def TryGetPosition(self, relativeTo: win32more.Microsoft.UI.Xaml.UIElement, point: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    Handled = property(get_Handled, put_Handled)
class IDoubleTappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IDoubleTappedRoutedEventArgs'
    _iid_ = Guid('{32b9549d-11d8-53a5-a953-02409537a11f}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IExecuteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IExecuteRequestedEventArgs'
    _iid_ = Guid('{e1a9fd0c-34d0-5ae2-8f5d-377e7a8a2708}')
    @winrt_commethod(6)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Parameter = property(get_Parameter, None)
class IFindNextElementOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IFindNextElementOptions'
    _iid_ = Guid('{7f88e76b-7417-5447-aed4-2fabd291bdc6}')
    @winrt_commethod(6)
    def get_SearchRoot(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def put_SearchRoot(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(8)
    def get_ExclusionRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def put_ExclusionRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(10)
    def get_HintRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_HintRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(12)
    def get_XYFocusNavigationStrategyOverride(self) -> win32more.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategyOverride: ...
    @winrt_commethod(13)
    def put_XYFocusNavigationStrategyOverride(self, value: win32more.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategyOverride) -> Void: ...
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    HintRect = property(get_HintRect, put_HintRect)
    SearchRoot = property(get_SearchRoot, put_SearchRoot)
    XYFocusNavigationStrategyOverride = property(get_XYFocusNavigationStrategyOverride, put_XYFocusNavigationStrategyOverride)
class IFocusManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IFocusManager'
    _iid_ = Guid('{9fd07bc5-d2d4-53fe-a31a-846de8b7a257}')
class IFocusManagerGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IFocusManagerGotFocusEventArgs'
    _iid_ = Guid('{50aca341-4519-59cf-83b1-c9c45cfdb816}')
    @winrt_commethod(6)
    def get_NewFocusedElement(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    NewFocusedElement = property(get_NewFocusedElement, None)
class IFocusManagerLostFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IFocusManagerLostFocusEventArgs'
    _iid_ = Guid('{fdaf2c3f-a22e-5902-abce-b60758fbed1e}')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    OldFocusedElement = property(get_OldFocusedElement, None)
class IFocusManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IFocusManagerStatics'
    _iid_ = Guid('{e73dce04-e23a-5fb3-96ab-7df04c51dff2}')
    @winrt_commethod(6)
    def add_GotFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.FocusManagerGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_LostFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.FocusManagerLostFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LostFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_GettingFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.GettingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_GettingFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_LosingFocus(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Input.LosingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_LosingFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def TryFocusAsync(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.FocusState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_commethod(15)
    def TryMoveFocusAsync(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_commethod(16)
    def TryMoveFocusWithOptionsAsync(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Input.FocusMovementResult]: ...
    @winrt_commethod(17)
    def TryMoveFocusWithOptions(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions) -> Boolean: ...
    @winrt_commethod(18)
    def FindNextElement(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(19)
    def FindFirstFocusableElement(self, searchScope: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(20)
    def FindLastFocusableElement(self, searchScope: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(21)
    def FindNextElementWithOptions(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, focusNavigationOptions: win32more.Microsoft.UI.Xaml.Input.FindNextElementOptions) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(22)
    def FindNextFocusableElement(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(23)
    def FindNextFocusableElementWithHint(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(24)
    def TryMoveFocus(self, focusNavigationDirection: win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection) -> Boolean: ...
    @winrt_commethod(25)
    def GetFocusedElement(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(26)
    def GetFocusedElementWithRoot(self, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    GotFocus = event()
    LostFocus = event()
    GettingFocus = event()
    LosingFocus = event()
class IFocusMovementResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IFocusMovementResult'
    _iid_ = Guid('{a46259fd-3edd-554b-a188-0a47b71e4e1a}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    Succeeded = property(get_Succeeded, None)
class IGettingFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IGettingFocusEventArgs'
    _iid_ = Guid('{37fd3af0-bd3c-5bf5-a9cd-71a1e87af950}')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_NewFocusedElement(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def put_NewFocusedElement(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(9)
    def get_FocusState(self) -> win32more.Microsoft.UI.Xaml.FocusState: ...
    @winrt_commethod(10)
    def get_Direction(self) -> win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_InputDevice(self) -> win32more.Microsoft.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_commethod(14)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_CorrelationId(self) -> Guid: ...
    @winrt_commethod(17)
    def TryCancel(self) -> Boolean: ...
    @winrt_commethod(18)
    def TrySetNewFocusedElement(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
    Direction = property(get_Direction, None)
    FocusState = property(get_FocusState, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    OldFocusedElement = property(get_OldFocusedElement, None)
class IHoldingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IHoldingRoutedEventArgs'
    _iid_ = Guid('{8272a4b2-2221-551e-b0bb-16e29138ab20}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_HoldingState(self) -> win32more.Microsoft.UI.Input.HoldingState: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetPosition(self, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IInertiaExpansionBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IInertiaExpansionBehavior'
    _iid_ = Guid('{d60029b7-f0cd-5aea-abe5-7410d09118c6}')
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IInertiaRotationBehavior'
    _iid_ = Guid('{27b4bd03-9149-5691-bce5-fa33b32c4a81}')
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IInertiaTranslationBehavior'
    _iid_ = Guid('{d4f91cf5-3317-5914-b25a-ea6ee55b96d0}')
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IInputScope'
    _iid_ = Guid('{76ea58b1-e910-5176-9147-695cc95e7da2}')
    @winrt_commethod(6)
    def get_Names(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Input.InputScopeName]: ...
    Names = property(get_Names, None)
class IInputScopeName(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IInputScopeName'
    _iid_ = Guid('{ee99a66d-28d0-53cb-82ee-1b6ee58bcc35}')
    @winrt_commethod(6)
    def get_NameValue(self) -> win32more.Microsoft.UI.Xaml.Input.InputScopeNameValue: ...
    @winrt_commethod(7)
    def put_NameValue(self, value: win32more.Microsoft.UI.Xaml.Input.InputScopeNameValue) -> Void: ...
    NameValue = property(get_NameValue, put_NameValue)
class IInputScopeNameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IInputScopeNameFactory'
    _iid_ = Guid('{feec2efd-bc09-5cd6-9b47-6d35d1d87c61}')
    @winrt_commethod(6)
    def CreateInstance(self, nameValue: win32more.Microsoft.UI.Xaml.Input.InputScopeNameValue) -> win32more.Microsoft.UI.Xaml.Input.InputScopeName: ...
class IKeyRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs'
    _iid_ = Guid('{ee357007-a2d6-5c75-9431-05fd66ec7915}')
    @winrt_commethod(6)
    def get_Key(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OriginalKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(11)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Handled = property(get_Handled, put_Handled)
    Key = property(get_Key, None)
    KeyStatus = property(get_KeyStatus, None)
    OriginalKey = property(get_OriginalKey, None)
class IKeyboardAccelerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IKeyboardAccelerator'
    _iid_ = Guid('{6f8bf1e2-4e91-5cf9-a6be-4770caf3d770}')
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
    def get_ScopeOwner(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_ScopeOwner(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def add_Invoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator, win32more.Microsoft.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Invoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Key = property(get_Key, put_Key)
    Modifiers = property(get_Modifiers, put_Modifiers)
    ScopeOwner = property(get_ScopeOwner, put_ScopeOwner)
    Invoked = event()
class IKeyboardAcceleratorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IKeyboardAcceleratorFactory'
    _iid_ = Guid('{ca1d410a-af2a-51b9-a1de-6c0af9f3b598}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator: ...
class IKeyboardAcceleratorInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs'
    _iid_ = Guid('{62c9fdb0-b574-527d-97eb-5c7f674441e0}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Element(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def get_KeyboardAccelerator(self) -> win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator: ...
    Element = property(get_Element, None)
    Handled = property(get_Handled, put_Handled)
    KeyboardAccelerator = property(get_KeyboardAccelerator, None)
class IKeyboardAcceleratorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IKeyboardAcceleratorStatics'
    _iid_ = Guid('{73e674ca-73f4-5e77-b8d6-ff7852a63b0b}')
    @winrt_commethod(6)
    def get_KeyProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ModifiersProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScopeOwnerProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsEnabledProperty = property(get_IsEnabledProperty, None)
    KeyProperty = property(get_KeyProperty, None)
    ModifiersProperty = property(get_ModifiersProperty, None)
    ScopeOwnerProperty = property(get_ScopeOwnerProperty, None)
class ILosingFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.ILosingFocusEventArgs'
    _iid_ = Guid('{fa0e5ffa-2b1b-52f8-bb66-e35f51e73cf3}')
    @winrt_commethod(6)
    def get_OldFocusedElement(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def get_NewFocusedElement(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(8)
    def put_NewFocusedElement(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(9)
    def get_FocusState(self) -> win32more.Microsoft.UI.Xaml.FocusState: ...
    @winrt_commethod(10)
    def get_Direction(self) -> win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_InputDevice(self) -> win32more.Microsoft.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_commethod(14)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_CorrelationId(self) -> Guid: ...
    @winrt_commethod(17)
    def TryCancel(self) -> Boolean: ...
    @winrt_commethod(18)
    def TrySetNewFocusedElement(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    Cancel = property(get_Cancel, put_Cancel)
    CorrelationId = property(get_CorrelationId, None)
    Direction = property(get_Direction, None)
    FocusState = property(get_FocusState, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
    NewFocusedElement = property(get_NewFocusedElement, put_NewFocusedElement)
    OldFocusedElement = property(get_OldFocusedElement, None)
class IManipulationCompletedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs'
    _iid_ = Guid('{e3be9e4e-c5fb-5859-a81d-ce12fc3a2f4d}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    Container = property(get_Container, None)
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    IsInertial = property(get_IsInertial, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class IManipulationDeltaRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs'
    _iid_ = Guid('{51369745-960f-54ac-93fa-763d22910dea}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Delta(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(10)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(11)
    def get_Velocities(self) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    @winrt_commethod(12)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs'
    _iid_ = Guid('{17d510be-5514-5952-9afd-959b60ab9394}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_ExpansionBehavior(self) -> win32more.Microsoft.UI.Xaml.Input.InertiaExpansionBehavior: ...
    @winrt_commethod(8)
    def put_ExpansionBehavior(self, value: win32more.Microsoft.UI.Xaml.Input.InertiaExpansionBehavior) -> Void: ...
    @winrt_commethod(9)
    def get_RotationBehavior(self) -> win32more.Microsoft.UI.Xaml.Input.InertiaRotationBehavior: ...
    @winrt_commethod(10)
    def put_RotationBehavior(self, value: win32more.Microsoft.UI.Xaml.Input.InertiaRotationBehavior) -> Void: ...
    @winrt_commethod(11)
    def get_TranslationBehavior(self) -> win32more.Microsoft.UI.Xaml.Input.InertiaTranslationBehavior: ...
    @winrt_commethod(12)
    def put_TranslationBehavior(self, value: win32more.Microsoft.UI.Xaml.Input.InertiaTranslationBehavior) -> Void: ...
    @winrt_commethod(13)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(16)
    def get_Delta(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(17)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(18)
    def get_Velocities(self) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationPivot'
    _iid_ = Guid('{286baba4-313d-507c-adc5-f739732cea27}')
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationPivotFactory'
    _iid_ = Guid('{67143ccd-ea6c-5fe2-bef2-adcbd7af52fd}')
    @winrt_commethod(6)
    def CreateInstanceWithCenterAndRadius(self, center: win32more.Windows.Foundation.Point, radius: Double) -> win32more.Microsoft.UI.Xaml.Input.ManipulationPivot: ...
class IManipulationStartedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs'
    _iid_ = Guid('{61857950-5821-5652-9fdf-c6277c5886f5}')
    @winrt_commethod(6)
    def get_Container(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(11)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(12)
    def Complete(self) -> Void: ...
    Container = property(get_Container, None)
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IManipulationStartedRoutedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgsFactory'
    _iid_ = Guid('{5681b0de-3fa7-503e-9c46-a80339760292}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.ManipulationStartedRoutedEventArgs: ...
class IManipulationStartingRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs'
    _iid_ = Guid('{93a99f86-f5a0-5326-91b0-851c897af79f}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Microsoft.UI.Xaml.Input.ManipulationModes: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Microsoft.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_commethod(8)
    def get_Container(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Container(self, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def get_Pivot(self) -> win32more.Microsoft.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_commethod(11)
    def put_Pivot(self, value: win32more.Microsoft.UI.Xaml.Input.ManipulationPivot) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Input.INoFocusCandidateFoundEventArgs'
    _iid_ = Guid('{a2d7153a-cd2a-59cb-a574-ac82e30b9201}')
    @winrt_commethod(6)
    def get_Direction(self) -> win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_InputDevice(self) -> win32more.Microsoft.UI.Xaml.Input.FocusInputDeviceKind: ...
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
class IPointer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IPointer'
    _iid_ = Guid('{1f9afbf5-11a3-5e68-aa1b-72febfa0ab23}')
    @winrt_commethod(6)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs'
    _iid_ = Guid('{66e78a9a-1bec-5f92-b1a1-ea6334ee511c}')
    @winrt_commethod(6)
    def get_Pointer(self) -> win32more.Microsoft.UI.Xaml.Input.Pointer: ...
    @winrt_commethod(7)
    def get_KeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsGenerated(self) -> Boolean: ...
    @winrt_commethod(11)
    def GetCurrentPoint(self, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    @winrt_commethod(12)
    def GetIntermediatePoints(self, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]: ...
    Handled = property(get_Handled, put_Handled)
    IsGenerated = property(get_IsGenerated, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Pointer = property(get_Pointer, None)
class IProcessKeyboardAcceleratorEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs'
    _iid_ = Guid('{9be0d058-3d26-5811-b50a-3bb80ca766c9}')
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IRightTappedRoutedEventArgs'
    _iid_ = Guid('{3972fafb-2915-5c62-bb6b-54ad84ff400d}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IStandardUICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IStandardUICommand'
    _iid_ = Guid('{5f395d50-5449-59ab-9cb2-4e3700033f03}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.UI.Xaml.Input.StandardUICommandKind: ...
    @winrt_commethod(7)
    def put_Kind(self, value: win32more.Microsoft.UI.Xaml.Input.StandardUICommandKind) -> Void: ...
    Kind = property(get_Kind, put_Kind)
class IStandardUICommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IStandardUICommandFactory'
    _iid_ = Guid('{5800f099-3746-5bcf-b1ce-af3d6bf8e83f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.StandardUICommand: ...
    @winrt_commethod(7)
    def CreateInstanceWithKind(self, kind: win32more.Microsoft.UI.Xaml.Input.StandardUICommandKind, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.StandardUICommand: ...
class IStandardUICommandStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IStandardUICommandStatics'
    _iid_ = Guid('{ab80c197-85cc-5d36-81aa-156cd63be31a}')
    @winrt_commethod(6)
    def get_KindProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KindProperty = property(get_KindProperty, None)
class ITappedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.ITappedRoutedEventArgs'
    _iid_ = Guid('{73f74b8c-3709-547e-8e0c-51c03c89126a}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPosition(self, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class IXamlUICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IXamlUICommand'
    _iid_ = Guid('{a457f2cb-51e0-541c-9c42-dd1dcbdf58fb}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IconSource(self) -> win32more.Microsoft.UI.Xaml.Controls.IconSource: ...
    @winrt_commethod(9)
    def put_IconSource(self, value: win32more.Microsoft.UI.Xaml.Controls.IconSource) -> Void: ...
    @winrt_commethod(10)
    def get_KeyboardAccelerators(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_commethod(11)
    def get_AccessKey(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_AccessKey(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Command(self) -> win32more.Microsoft.UI.Xaml.Input.ICommand: ...
    @winrt_commethod(16)
    def put_Command(self, value: win32more.Microsoft.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_commethod(17)
    def add_ExecuteRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Input.XamlUICommand, win32more.Microsoft.UI.Xaml.Input.ExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ExecuteRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_CanExecuteRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Input.XamlUICommand, win32more.Microsoft.UI.Xaml.Input.CanExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Input.IXamlUICommandFactory'
    _iid_ = Guid('{f1f80a20-0e31-5505-8bc3-cdd1f0947f1d}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.XamlUICommand: ...
class IXamlUICommandStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Input.IXamlUICommandStatics'
    _iid_ = Guid('{981dbda6-cdcb-5e35-b24b-c4f60ba148d9}')
    @winrt_commethod(6)
    def get_LabelProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IconSourceProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_KeyboardAcceleratorsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AccessKeyProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DescriptionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_CommandProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    CommandProperty = property(get_CommandProperty, None)
    DescriptionProperty = property(get_DescriptionProperty, None)
    IconSourceProperty = property(get_IconSourceProperty, None)
    KeyboardAcceleratorsProperty = property(get_KeyboardAcceleratorsProperty, None)
    LabelProperty = property(get_LabelProperty, None)
class InertiaExpansionBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IInertiaExpansionBehavior
    _classid_ = 'Microsoft.UI.Xaml.Input.InertiaExpansionBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: win32more.Microsoft.UI.Xaml.Input.IInertiaExpansionBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: win32more.Microsoft.UI.Xaml.Input.IInertiaExpansionBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredExpansion(self: win32more.Microsoft.UI.Xaml.Input.IInertiaExpansionBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredExpansion(self: win32more.Microsoft.UI.Xaml.Input.IInertiaExpansionBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredExpansion = property(get_DesiredExpansion, put_DesiredExpansion)
class InertiaRotationBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IInertiaRotationBehavior
    _classid_ = 'Microsoft.UI.Xaml.Input.InertiaRotationBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: win32more.Microsoft.UI.Xaml.Input.IInertiaRotationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: win32more.Microsoft.UI.Xaml.Input.IInertiaRotationBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredRotation(self: win32more.Microsoft.UI.Xaml.Input.IInertiaRotationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredRotation(self: win32more.Microsoft.UI.Xaml.Input.IInertiaRotationBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredRotation = property(get_DesiredRotation, put_DesiredRotation)
class InertiaTranslationBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IInertiaTranslationBehavior
    _classid_ = 'Microsoft.UI.Xaml.Input.InertiaTranslationBehavior'
    @winrt_mixinmethod
    def get_DesiredDeceleration(self: win32more.Microsoft.UI.Xaml.Input.IInertiaTranslationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDeceleration(self: win32more.Microsoft.UI.Xaml.Input.IInertiaTranslationBehavior, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredDisplacement(self: win32more.Microsoft.UI.Xaml.Input.IInertiaTranslationBehavior) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredDisplacement(self: win32more.Microsoft.UI.Xaml.Input.IInertiaTranslationBehavior, value: Double) -> Void: ...
    DesiredDeceleration = property(get_DesiredDeceleration, put_DesiredDeceleration)
    DesiredDisplacement = property(get_DesiredDisplacement, put_DesiredDisplacement)
class InputScope(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Input.IInputScope
    _classid_ = 'Microsoft.UI.Xaml.Input.InputScope'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.InputScope.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.InputScope: ...
    @winrt_mixinmethod
    def get_Names(self: win32more.Microsoft.UI.Xaml.Input.IInputScope) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Input.InputScopeName]: ...
    Names = property(get_Names, None)
class InputScopeName(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Input.IInputScopeName
    _classid_ = 'Microsoft.UI.Xaml.Input.InputScopeName'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.InputScopeName.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.InputScopeName.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.InputScopeName: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Input.IInputScopeNameFactory, nameValue: win32more.Microsoft.UI.Xaml.Input.InputScopeNameValue) -> win32more.Microsoft.UI.Xaml.Input.InputScopeName: ...
    @winrt_mixinmethod
    def get_NameValue(self: win32more.Microsoft.UI.Xaml.Input.IInputScopeName) -> win32more.Microsoft.UI.Xaml.Input.InputScopeNameValue: ...
    @winrt_mixinmethod
    def put_NameValue(self: win32more.Microsoft.UI.Xaml.Input.IInputScopeName, value: win32more.Microsoft.UI.Xaml.Input.InputScopeNameValue) -> Void: ...
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
    Maps = 62
    NumericPassword = 63
    NumericPin = 64
    AlphanumericPin = 65
    FormulaNumber = 67
    ChatWithoutEmoji = 68
class KeyEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db68e7cc-9a2b-527d-9989-25284daccc03}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.KeyRoutedEventArgs) -> Void: ...
class KeyRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.KeyRoutedEventArgs'
    @winrt_mixinmethod
    def get_Key(self: win32more.Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalKey(self: win32more.Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Microsoft.UI.Xaml.Input.IKeyRoutedEventArgs) -> WinRT_String: ...
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
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator
    _classid_ = 'Microsoft.UI.Xaml.Input.KeyboardAccelerator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator: ...
    @winrt_mixinmethod
    def get_Key(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def put_Key(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator, value: win32more.Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def get_Modifiers(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def put_Modifiers(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator, value: win32more.Windows.System.VirtualKeyModifiers) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ScopeOwner(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_ScopeOwner(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def add_Invoked(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator, win32more.Microsoft.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Invoked(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAccelerator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_KeyProperty(cls: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ModifiersProperty(cls: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScopeOwnerProperty(cls: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    default_interface: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Element(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_KeyboardAccelerator(self: win32more.Microsoft.UI.Xaml.Input.IKeyboardAcceleratorInvokedEventArgs) -> win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator: ...
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
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.LosingFocusEventArgs'
    @winrt_mixinmethod
    def get_OldFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_NewFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_NewFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_FocusState(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.FocusState: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> win32more.Microsoft.UI.Xaml.Input.FocusInputDeviceKind: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def TryCancel(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetNewFocusedElement(self: win32more.Microsoft.UI.Xaml.Input.ILosingFocusEventArgs, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
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
    _iid_ = Guid('{d51df8db-71cd-5bfd-8426-767218ee55ec}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs) -> Void: ...
class ManipulationCompletedRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.ManipulationCompletedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_IsInertial(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    Container = property(get_Container, None)
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    IsInertial = property(get_IsInertial, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationDeltaEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83f2d4ce-105f-5392-a38a-b7467b7c2ea5}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs) -> Void: ...
class ManipulationDeltaRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.ManipulationDeltaRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_IsInertial(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Delta(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Microsoft.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs) -> Void: ...
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
    _iid_ = Guid('{5de296bd-6f1c-5f60-9180-10705282576c}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs) -> Void: ...
class ManipulationInertiaStartingRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.ManipulationInertiaStartingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_ExpansionBehavior(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.Input.InertiaExpansionBehavior: ...
    @winrt_mixinmethod
    def put_ExpansionBehavior(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: win32more.Microsoft.UI.Xaml.Input.InertiaExpansionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_RotationBehavior(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.Input.InertiaRotationBehavior: ...
    @winrt_mixinmethod
    def put_RotationBehavior(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: win32more.Microsoft.UI.Xaml.Input.InertiaRotationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationBehavior(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.Input.InertiaTranslationBehavior: ...
    @winrt_mixinmethod
    def put_TranslationBehavior(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: win32more.Microsoft.UI.Xaml.Input.InertiaTranslationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Delta(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Microsoft.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
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
    default_interface: win32more.Microsoft.UI.Xaml.Input.IManipulationPivot
    _classid_ = 'Microsoft.UI.Xaml.Input.ManipulationPivot'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ManipulationPivot.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ManipulationPivot.CreateInstanceWithCenterAndRadius(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_factorymethod
    def CreateInstanceWithCenterAndRadius(cls: win32more.Microsoft.UI.Xaml.Input.IManipulationPivotFactory, center: win32more.Windows.Foundation.Point, radius: Double) -> win32more.Microsoft.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Microsoft.UI.Xaml.Input.IManipulationPivot) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Center(self: win32more.Microsoft.UI.Xaml.Input.IManipulationPivot, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Radius(self: win32more.Microsoft.UI.Xaml.Input.IManipulationPivot) -> Double: ...
    @winrt_mixinmethod
    def put_Radius(self: win32more.Microsoft.UI.Xaml.Input.IManipulationPivot, value: Double) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class ManipulationStartedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41060669-304c-53ac-9d43-bc311235aae4}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.ManipulationStartedRoutedEventArgs) -> Void: ...
class ManipulationStartedRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ManipulationStartedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ManipulationStartedRoutedEventArgs.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.ManipulationStartedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartedRoutedEventArgs) -> Void: ...
    Container = property(get_Container, None)
    Cumulative = property(get_Cumulative, None)
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class ManipulationStartingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44f528f1-f0e4-505c-a0bb-0c4839b29df5}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.ManipulationStartingRoutedEventArgs) -> Void: ...
class ManipulationStartingRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ManipulationStartingRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.ManipulationStartingRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.ManipulationStartingRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.Input.ManipulationModes: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: win32more.Microsoft.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_mixinmethod
    def get_Container(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Container(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_Pivot(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.Input.ManipulationPivot: ...
    @winrt_mixinmethod
    def put_Pivot(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: win32more.Microsoft.UI.Xaml.Input.ManipulationPivot) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IManipulationStartingRoutedEventArgs, value: Boolean) -> Void: ...
    Container = property(get_Container, put_Container)
    Handled = property(get_Handled, put_Handled)
    Mode = property(get_Mode, put_Mode)
    Pivot = property(get_Pivot, put_Pivot)
class NoFocusCandidateFoundEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.INoFocusCandidateFoundEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.NoFocusCandidateFoundEventArgs'
    @winrt_mixinmethod
    def get_Direction(self: win32more.Microsoft.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> win32more.Microsoft.UI.Xaml.Input.FocusNavigationDirection: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.INoFocusCandidateFoundEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevice(self: win32more.Microsoft.UI.Xaml.Input.INoFocusCandidateFoundEventArgs) -> win32more.Microsoft.UI.Xaml.Input.FocusInputDeviceKind: ...
    Direction = property(get_Direction, None)
    Handled = property(get_Handled, put_Handled)
    InputDevice = property(get_InputDevice, None)
class Pointer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IPointer
    _classid_ = 'Microsoft.UI.Xaml.Input.Pointer'
    @winrt_mixinmethod
    def get_PointerId(self: win32more.Microsoft.UI.Xaml.Input.IPointer) -> UInt32: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IPointer) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_IsInContact(self: win32more.Microsoft.UI.Xaml.Input.IPointer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInRange(self: win32more.Microsoft.UI.Xaml.Input.IPointer) -> Boolean: ...
    IsInContact = property(get_IsInContact, None)
    IsInRange = property(get_IsInRange, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    PointerId = property(get_PointerId, None)
class PointerEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a48a71e1-8bb4-5597-9e31-903a3f6a04fb}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.PointerRoutedEventArgs) -> Void: ...
class PointerRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.PointerRoutedEventArgs'
    @winrt_mixinmethod
    def get_Pointer(self: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs) -> win32more.Microsoft.UI.Xaml.Input.Pointer: ...
    @winrt_mixinmethod
    def get_KeyModifiers(self: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsGenerated(self: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetCurrentPoint(self: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    @winrt_mixinmethod
    def GetIntermediatePoints(self: win32more.Microsoft.UI.Xaml.Input.IPointerRoutedEventArgs, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]: ...
    Handled = property(get_Handled, put_Handled)
    IsGenerated = property(get_IsGenerated, None)
    KeyModifiers = property(get_KeyModifiers, None)
    Pointer = property(get_Pointer, None)
class ProcessKeyboardAcceleratorEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs'
    @winrt_mixinmethod
    def get_Key(self: win32more.Microsoft.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_Modifiers(self: win32more.Microsoft.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Key = property(get_Key, None)
    Modifiers = property(get_Modifiers, None)
class RightTappedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5070e32f-3dc7-56cf-8fdd-de1b40d0b472}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.RightTappedRoutedEventArgs) -> Void: ...
class RightTappedRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.IRightTappedRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.RightTappedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.RightTappedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.RightTappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.IRightTappedRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.IRightTappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.IRightTappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Microsoft.UI.Xaml.Input.IRightTappedRoutedEventArgs, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    PointerDeviceType = property(get_PointerDeviceType, None)
class _StandardUICommand_Meta_(ComPtr.__class__):
    pass
class StandardUICommand(ComPtr, metaclass=_StandardUICommand_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Input.XamlUICommand
    default_interface: win32more.Microsoft.UI.Xaml.Input.IStandardUICommand
    _classid_ = 'Microsoft.UI.Xaml.Input.StandardUICommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.StandardUICommand.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.StandardUICommand.CreateInstanceWithKind(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Input.IStandardUICommandFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.StandardUICommand: ...
    @winrt_factorymethod
    def CreateInstanceWithKind(cls: win32more.Microsoft.UI.Xaml.Input.IStandardUICommandFactory, kind: win32more.Microsoft.UI.Xaml.Input.StandardUICommandKind, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.StandardUICommand: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.UI.Xaml.Input.IStandardUICommand) -> win32more.Microsoft.UI.Xaml.Input.StandardUICommandKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Microsoft.UI.Xaml.Input.IStandardUICommand, value: win32more.Microsoft.UI.Xaml.Input.StandardUICommandKind) -> Void: ...
    @winrt_classmethod
    def get_KindProperty(cls: win32more.Microsoft.UI.Xaml.Input.IStandardUICommandStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    _iid_ = Guid('{b60074f3-125b-534e-8f9c-9769bd3f0f64}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Input.TappedRoutedEventArgs) -> Void: ...
class TappedRoutedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Input.ITappedRoutedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Input.TappedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.TappedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Input.TappedRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Xaml.Input.ITappedRoutedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Input.ITappedRoutedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Input.ITappedRoutedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Microsoft.UI.Xaml.Input.ITappedRoutedEventArgs, relativeTo: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
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
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand
    _classid_ = 'Microsoft.UI.Xaml.Input.XamlUICommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Input.XamlUICommand.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Input.IXamlUICommandFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Input.XamlUICommand: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IconSource(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand) -> win32more.Microsoft.UI.Xaml.Controls.IconSource: ...
    @winrt_mixinmethod
    def put_IconSource(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, value: win32more.Microsoft.UI.Xaml.Controls.IconSource) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAccelerators(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_mixinmethod
    def get_AccessKey(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AccessKey(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Command(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand) -> win32more.Microsoft.UI.Xaml.Input.ICommand: ...
    @winrt_mixinmethod
    def put_Command(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, value: win32more.Microsoft.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_mixinmethod
    def add_ExecuteRequested(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Input.XamlUICommand, win32more.Microsoft.UI.Xaml.Input.ExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ExecuteRequested(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CanExecuteRequested(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Input.XamlUICommand, win32more.Microsoft.UI.Xaml.Input.CanExecuteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CanExecuteRequested(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyCanExecuteChanged(self: win32more.Microsoft.UI.Xaml.Input.IXamlUICommand) -> Void: ...
    @winrt_mixinmethod
    def add_CanExecuteChanged(self: win32more.Microsoft.UI.Xaml.Input.ICommand, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CanExecuteChanged(self: win32more.Microsoft.UI.Xaml.Input.ICommand, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CanExecute(self: win32more.Microsoft.UI.Xaml.Input.ICommand, parameter: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Execute(self: win32more.Microsoft.UI.Xaml.Input.ICommand, parameter: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_classmethod
    def get_LabelProperty(cls: win32more.Microsoft.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IconSourceProperty(cls: win32more.Microsoft.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyboardAcceleratorsProperty(cls: win32more.Microsoft.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: win32more.Microsoft.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DescriptionProperty(cls: win32more.Microsoft.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CommandProperty(cls: win32more.Microsoft.UI.Xaml.Input.IXamlUICommandStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
