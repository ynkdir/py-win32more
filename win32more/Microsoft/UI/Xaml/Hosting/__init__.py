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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Content
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Controls
import win32more.Microsoft.UI.Xaml.Hosting
import win32more.Microsoft.UI.Xaml.Media
import win32more.Windows.Foundation
class DesktopWindowXamlSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource
    _classid_ = 'Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource.CreateInstance(*args, None, None)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_HasFocus(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_mixinmethod
    def put_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    @winrt_mixinmethod
    def get_SiteBridge(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> win32more.Microsoft.UI.Content.DesktopChildSiteBridge: ...
    @winrt_mixinmethod
    def add_TakeFocusRequested(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TakeFocusRequested(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NavigateFocus(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, request: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    @winrt_mixinmethod
    def Initialize(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource, parentWindowId: win32more.Microsoft.UI.WindowId) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Content = property(get_Content, put_Content)
    HasFocus = property(get_HasFocus, None)
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
    SiteBridge = property(get_SiteBridge, None)
class DesktopWindowXamlSourceGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class DesktopWindowXamlSourceTakeFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class ElementCompositionPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreview
    _classid_ = 'Microsoft.UI.Xaml.Hosting.ElementCompositionPreview'
    @winrt_classmethod
    def GetElementVisual(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Composition.Visual: ...
    @winrt_classmethod
    def GetElementChildVisual(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Composition.Visual: ...
    @winrt_classmethod
    def SetElementChildVisual(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Microsoft.UI.Xaml.UIElement, visual: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_classmethod
    def GetScrollViewerManipulationPropertySet(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, scrollViewer: win32more.Microsoft.UI.Xaml.Controls.ScrollViewer) -> win32more.Microsoft.UI.Composition.CompositionPropertySet: ...
    @winrt_classmethod
    def SetImplicitShowAnimation(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Microsoft.UI.Xaml.UIElement, animation: win32more.Microsoft.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetImplicitHideAnimation(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Microsoft.UI.Xaml.UIElement, animation: win32more.Microsoft.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetIsTranslationEnabled(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetPointerPositionPropertySet(cls: win32more.Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics, targetElement: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Composition.CompositionPropertySet: ...
class IDesktopWindowXamlSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSource'
    _iid_ = Guid('{553af92c-1381-51d6-bee0-f34beb042ea8}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_Content(self, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_HasFocus(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SystemBackdrop(self) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_commethod(10)
    def put_SystemBackdrop(self, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    @winrt_commethod(11)
    def get_SiteBridge(self) -> win32more.Microsoft.UI.Content.DesktopChildSiteBridge: ...
    @winrt_commethod(12)
    def add_TakeFocusRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_TakeFocusRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_GotFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def NavigateFocus(self, request: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    @winrt_commethod(17)
    def Initialize(self, parentWindowId: win32more.Microsoft.UI.WindowId) -> Void: ...
    Content = property(get_Content, put_Content)
    HasFocus = property(get_HasFocus, None)
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
    SiteBridge = property(get_SiteBridge, None)
class IDesktopWindowXamlSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceFactory'
    _iid_ = Guid('{7d2db617-14e7-5d49-aeec-ae10887e595d}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Hosting.DesktopWindowXamlSource: ...
class IDesktopWindowXamlSourceGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs'
    _iid_ = Guid('{cc63d863-2071-5f6b-aef9-c0ba35f3b8df}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class IDesktopWindowXamlSourceTakeFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs'
    _iid_ = Guid('{4f5a0e2c-4ddc-5c03-939f-6f3bda560363}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class IElementCompositionPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IElementCompositionPreview'
    _iid_ = Guid('{c8ad1ef4-a93f-5a25-85bd-7c498d9856d3}')
class IElementCompositionPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IElementCompositionPreviewStatics'
    _iid_ = Guid('{84da5a6c-0cfa-532b-9b15-ccd986374342}')
    @winrt_commethod(6)
    def GetElementVisual(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def GetElementChildVisual(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Composition.Visual: ...
    @winrt_commethod(8)
    def SetElementChildVisual(self, element: win32more.Microsoft.UI.Xaml.UIElement, visual: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def GetScrollViewerManipulationPropertySet(self, scrollViewer: win32more.Microsoft.UI.Xaml.Controls.ScrollViewer) -> win32more.Microsoft.UI.Composition.CompositionPropertySet: ...
    @winrt_commethod(10)
    def SetImplicitShowAnimation(self, element: win32more.Microsoft.UI.Xaml.UIElement, animation: win32more.Microsoft.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(11)
    def SetImplicitHideAnimation(self, element: win32more.Microsoft.UI.Xaml.UIElement, animation: win32more.Microsoft.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(12)
    def SetIsTranslationEnabled(self, element: win32more.Microsoft.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def GetPointerPositionPropertySet(self, targetElement: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Composition.CompositionPropertySet: ...
class IWindowsXamlManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IWindowsXamlManager'
    _iid_ = Guid('{85a2e562-7e8f-5333-a104-a3e672a2ffee}')
class IWindowsXamlManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IWindowsXamlManagerStatics'
    _iid_ = Guid('{56cb591d-de97-539f-881d-8ccdc44fa6c4}')
    @winrt_commethod(6)
    def InitializeForCurrentThread(self) -> win32more.Microsoft.UI.Xaml.Hosting.WindowsXamlManager: ...
class IXamlSourceFocusNavigationRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest'
    _iid_ = Guid('{c883ea8b-4ce2-58be-b547-66dedf620312}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason: ...
    @winrt_commethod(7)
    def get_HintRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_CorrelationId(self) -> Guid: ...
    Reason = property(get_Reason, None)
    HintRect = property(get_HintRect, None)
    CorrelationId = property(get_CorrelationId, None)
class IXamlSourceFocusNavigationRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory'
    _iid_ = Guid('{7a5124dd-2876-5ed8-b564-5867731d7f1e}')
    @winrt_commethod(6)
    def CreateInstance(self, reason: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_commethod(7)
    def CreateInstanceWithHintRect(self, reason: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_commethod(8)
    def CreateInstanceWithHintRectAndCorrelationId(self, reason: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect, correlationId: Guid) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
class IXamlSourceFocusNavigationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult'
    _iid_ = Guid('{d6bf378e-2aac-5e5b-ac8a-6c5d9a4c1cb8}')
    @winrt_commethod(6)
    def get_WasFocusMoved(self) -> Boolean: ...
    WasFocusMoved = property(get_WasFocusMoved, None)
class IXamlSourceFocusNavigationResultFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationResultFactory'
    _iid_ = Guid('{f533f53b-5c00-5c88-9a41-3888cb86e495}')
    @winrt_commethod(6)
    def CreateInstance(self, focusMoved: Boolean) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
class WindowsXamlManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Hosting.IWindowsXamlManager
    _classid_ = 'Microsoft.UI.Xaml.Hosting.WindowsXamlManager'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def InitializeForCurrentThread(cls: win32more.Microsoft.UI.Xaml.Hosting.IWindowsXamlManagerStatics) -> win32more.Microsoft.UI.Xaml.Hosting.WindowsXamlManager: ...
XamlSourceFocusNavigationReason = Int32
XamlSourceFocusNavigationReason_Programmatic: XamlSourceFocusNavigationReason = 0
XamlSourceFocusNavigationReason_Restore: XamlSourceFocusNavigationReason = 1
XamlSourceFocusNavigationReason_First: XamlSourceFocusNavigationReason = 3
XamlSourceFocusNavigationReason_Last: XamlSourceFocusNavigationReason = 4
XamlSourceFocusNavigationReason_Left: XamlSourceFocusNavigationReason = 7
XamlSourceFocusNavigationReason_Up: XamlSourceFocusNavigationReason = 8
XamlSourceFocusNavigationReason_Right: XamlSourceFocusNavigationReason = 9
XamlSourceFocusNavigationReason_Down: XamlSourceFocusNavigationReason = 10
class XamlSourceFocusNavigationRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest
    _classid_ = 'Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest.CreateInstance(*args)
        elif len(args) == 2:
            instance = win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest.CreateInstanceWithHintRect(*args)
        elif len(args) == 3:
            instance = win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest.CreateInstanceWithHintRectAndCorrelationId(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_factorymethod
    def CreateInstanceWithHintRect(cls: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_factorymethod
    def CreateInstanceWithHintRectAndCorrelationId(cls: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect, correlationId: Guid) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason: ...
    @winrt_mixinmethod
    def get_HintRect(self: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> Guid: ...
    Reason = property(get_Reason, None)
    HintRect = property(get_HintRect, None)
    CorrelationId = property(get_CorrelationId, None)
class XamlSourceFocusNavigationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult
    _classid_ = 'Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationResult'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationResult.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationResultFactory, focusMoved: Boolean) -> win32more.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    @winrt_mixinmethod
    def get_WasFocusMoved(self: win32more.Microsoft.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult) -> Boolean: ...
    WasFocusMoved = property(get_WasFocusMoved, None)
make_ready(__name__)
