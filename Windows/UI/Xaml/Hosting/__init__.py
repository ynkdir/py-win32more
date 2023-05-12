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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.UI.Composition
import Windows.UI.WindowManagement
import Windows.UI.Xaml
import Windows.UI.Xaml.Controls
import Windows.UI.Xaml.Controls.Primitives
import Windows.UI.Xaml.Hosting
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DesignerAppExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IDesignerAppExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Hosting.DesignerAppExitedEventArgs'
    @winrt_mixinmethod
    def get_ExitCode(self: Windows.UI.Xaml.Hosting.IDesignerAppExitedEventArgs) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class DesignerAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IDesignerAppManager
    _classid_ = 'Windows.UI.Xaml.Hosting.DesignerAppManager'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Xaml.Hosting.IDesignerAppManagerFactory, appUserModelId: WinRT_String) -> Windows.UI.Xaml.Hosting.DesignerAppManager: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.UI.Xaml.Hosting.IDesignerAppManager) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_DesignerAppExited(self: Windows.UI.Xaml.Hosting.IDesignerAppManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Hosting.DesignerAppManager, Windows.UI.Xaml.Hosting.DesignerAppExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DesignerAppExited(self: Windows.UI.Xaml.Hosting.IDesignerAppManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateNewViewAsync(self: Windows.UI.Xaml.Hosting.IDesignerAppManager, initialViewState: Windows.UI.Xaml.Hosting.DesignerAppViewState, initialViewSize: Windows.Foundation.Size) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Hosting.DesignerAppView]: ...
    @winrt_mixinmethod
    def LoadObjectIntoAppAsync(self: Windows.UI.Xaml.Hosting.IDesignerAppManager, dllName: WinRT_String, classId: Guid, initializationData: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    AppUserModelId = property(get_AppUserModelId, None)
class DesignerAppView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IDesignerAppView
    _classid_ = 'Windows.UI.Xaml.Hosting.DesignerAppView'
    @winrt_mixinmethod
    def get_ApplicationViewId(self: Windows.UI.Xaml.Hosting.IDesignerAppView) -> Int32: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.UI.Xaml.Hosting.IDesignerAppView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ViewState(self: Windows.UI.Xaml.Hosting.IDesignerAppView) -> Windows.UI.Xaml.Hosting.DesignerAppViewState: ...
    @winrt_mixinmethod
    def get_ViewSize(self: Windows.UI.Xaml.Hosting.IDesignerAppView) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def UpdateViewAsync(self: Windows.UI.Xaml.Hosting.IDesignerAppView, viewState: Windows.UI.Xaml.Hosting.DesignerAppViewState, viewSize: Windows.Foundation.Size) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ViewState = property(get_ViewState, None)
    ViewSize = property(get_ViewSize, None)
DesignerAppViewState = Int32
DesignerAppViewState_Visible: DesignerAppViewState = 0
DesignerAppViewState_Hidden: DesignerAppViewState = 1
class DesktopWindowXamlSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource
    _classid_ = 'Windows.UI.Xaml.Hosting.DesktopWindowXamlSource'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Hosting.DesktopWindowXamlSource: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Content(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_HasFocus(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> Boolean: ...
    @winrt_mixinmethod
    def add_TakeFocusRequested(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TakeFocusRequested(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NavigateFocus(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, request: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Content = property(get_Content, put_Content)
    HasFocus = property(get_HasFocus, None)
class DesktopWindowXamlSourceGotFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs
    _classid_ = 'Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class DesktopWindowXamlSourceTakeFocusRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class ElementCompositionPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IElementCompositionPreview
    _classid_ = 'Windows.UI.Xaml.Hosting.ElementCompositionPreview'
    @winrt_classmethod
    def SetAppWindowContent(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3, appWindow: Windows.UI.WindowManagement.AppWindow, xamlContent: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def GetAppWindowContent(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3, appWindow: Windows.UI.WindowManagement.AppWindow) -> Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def SetImplicitShowAnimation(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetImplicitHideAnimation(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetIsTranslationEnabled(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetPointerPositionPropertySet(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, targetElement: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_classmethod
    def GetElementVisual(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_classmethod
    def GetElementChildVisual(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_classmethod
    def SetElementChildVisual(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: Windows.UI.Xaml.UIElement, visual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_classmethod
    def GetScrollViewerManipulationPropertySet(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, scrollViewer: Windows.UI.Xaml.Controls.ScrollViewer) -> Windows.UI.Composition.CompositionPropertySet: ...
HostingContract: UInt32 = 327680
class IDesignerAppExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppExitedEventArgs'
    _iid_ = Guid('{f6aac86a-0cad-410c-8f62-dc2936151c74}')
    @winrt_commethod(6)
    def get_ExitCode(self) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class IDesignerAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppManager'
    _iid_ = Guid('{a6272caa-d5c6-40cb-abd9-27ba43831bb7}')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_DesignerAppExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Hosting.DesignerAppManager, Windows.UI.Xaml.Hosting.DesignerAppExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_DesignerAppExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def CreateNewViewAsync(self, initialViewState: Windows.UI.Xaml.Hosting.DesignerAppViewState, initialViewSize: Windows.Foundation.Size) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Hosting.DesignerAppView]: ...
    @winrt_commethod(10)
    def LoadObjectIntoAppAsync(self, dllName: WinRT_String, classId: Guid, initializationData: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    AppUserModelId = property(get_AppUserModelId, None)
class IDesignerAppManagerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppManagerFactory'
    _iid_ = Guid('{8f9d633b-1266-4c0e-8499-0db85bbd4c43}')
    @winrt_commethod(6)
    def Create(self, appUserModelId: WinRT_String) -> Windows.UI.Xaml.Hosting.DesignerAppManager: ...
class IDesignerAppView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppView'
    _iid_ = Guid('{5c777cea-dd71-4a84-a56f-dacb4b14706f}')
    @winrt_commethod(6)
    def get_ApplicationViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ViewState(self) -> Windows.UI.Xaml.Hosting.DesignerAppViewState: ...
    @winrt_commethod(9)
    def get_ViewSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def UpdateViewAsync(self, viewState: Windows.UI.Xaml.Hosting.DesignerAppViewState, viewSize: Windows.Foundation.Size) -> Windows.Foundation.IAsyncAction: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ViewState = property(get_ViewState, None)
    ViewSize = property(get_ViewSize, None)
class IDesktopWindowXamlSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource'
    _iid_ = Guid('{d585bfe1-00ff-51be-ba1d-a1329956ea0a}')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_Content(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_HasFocus(self) -> Boolean: ...
    @winrt_commethod(9)
    def add_TakeFocusRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_TakeFocusRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_GotFocus(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_GotFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def NavigateFocus(self, request: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    Content = property(get_Content, put_Content)
    HasFocus = property(get_HasFocus, None)
class IDesktopWindowXamlSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceFactory'
    _iid_ = Guid('{5cd61dc0-2561-56e1-8e75-6e44173805e3}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Hosting.DesktopWindowXamlSource: ...
class IDesktopWindowXamlSourceGotFocusEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs'
    _iid_ = Guid('{39be4849-d9cc-5b70-8f05-1ad9a4aaa342}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class IDesktopWindowXamlSourceTakeFocusRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs'
    _iid_ = Guid('{fe61e4b9-a7af-52b3-bdb9-c3305c0b8df2}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class IElementCompositionPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreview'
    _iid_ = Guid('{b6f1a676-cfe6-46ac-acf6-c4687bb65e60}')
class IElementCompositionPreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics'
    _iid_ = Guid('{08c92b38-ec99-4c55-bc85-a1c180b27646}')
    @winrt_commethod(6)
    def GetElementVisual(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def GetElementChildVisual(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(8)
    def SetElementChildVisual(self, element: Windows.UI.Xaml.UIElement, visual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def GetScrollViewerManipulationPropertySet(self, scrollViewer: Windows.UI.Xaml.Controls.ScrollViewer) -> Windows.UI.Composition.CompositionPropertySet: ...
class IElementCompositionPreviewStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2'
    _iid_ = Guid('{24148fbb-23d6-4f37-ba0c-0733e799722d}')
    @winrt_commethod(6)
    def SetImplicitShowAnimation(self, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(7)
    def SetImplicitHideAnimation(self, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(8)
    def SetIsTranslationEnabled(self, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPointerPositionPropertySet(self, targetElement: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.CompositionPropertySet: ...
class IElementCompositionPreviewStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3'
    _iid_ = Guid('{843bc4c3-c105-59fe-a3d1-373c1d3e6fbc}')
    @winrt_commethod(6)
    def SetAppWindowContent(self, appWindow: Windows.UI.WindowManagement.AppWindow, xamlContent: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(7)
    def GetAppWindowContent(self, appWindow: Windows.UI.WindowManagement.AppWindow) -> Windows.UI.Xaml.UIElement: ...
class IWindowsXamlManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IWindowsXamlManager'
    _iid_ = Guid('{56096c31-1aa0-5288-8818-6e74a2dcaff5}')
class IWindowsXamlManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics'
    _iid_ = Guid('{28258a12-7d82-505b-b210-712b04a58882}')
    @winrt_commethod(6)
    def InitializeForCurrentThread(self) -> Windows.UI.Xaml.Hosting.WindowsXamlManager: ...
class IXamlSourceFocusNavigationRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest'
    _iid_ = Guid('{fbb93bb5-1496-5a80-ac00-e757359755e6}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason: ...
    @winrt_commethod(7)
    def get_HintRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_CorrelationId(self) -> Guid: ...
    Reason = property(get_Reason, None)
    HintRect = property(get_HintRect, None)
    CorrelationId = property(get_CorrelationId, None)
class IXamlSourceFocusNavigationRequestFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory'
    _iid_ = Guid('{e746ab8f-b4ef-5390-97e5-cc0a2779c574}')
    @winrt_commethod(6)
    def CreateInstance(self, reason: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_commethod(7)
    def CreateInstanceWithHintRect(self, reason: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: Windows.Foundation.Rect) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_commethod(8)
    def CreateInstanceWithHintRectAndCorrelationId(self, reason: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: Windows.Foundation.Rect, correlationId: Guid) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
class IXamlSourceFocusNavigationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult'
    _iid_ = Guid('{88d55a5f-9603-5d8f-9cc7-d1c4070d9801}')
    @winrt_commethod(6)
    def get_WasFocusMoved(self) -> Boolean: ...
    WasFocusMoved = property(get_WasFocusMoved, None)
class IXamlSourceFocusNavigationResultFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResultFactory'
    _iid_ = Guid('{43bbadbf-f9e1-5527-b8c5-09339ff2ca76}')
    @winrt_commethod(6)
    def CreateInstance(self, focusMoved: Boolean) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
class IXamlUIPresenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenter'
    _iid_ = Guid('{a714944a-1619-4fc6-b31b-89512ef022a2}')
    @winrt_commethod(6)
    def get_RootElement(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_RootElement(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_ThemeKey(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ThemeKey(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ThemeResourcesXaml(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ThemeResourcesXaml(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def SetSize(self, width: Int32, height: Int32) -> Void: ...
    @winrt_commethod(13)
    def Render(self) -> Void: ...
    @winrt_commethod(14)
    def Present(self) -> Void: ...
    RootElement = property(get_RootElement, put_RootElement)
    ThemeKey = property(get_ThemeKey, put_ThemeKey)
    ThemeResourcesXaml = property(get_ThemeResourcesXaml, put_ThemeResourcesXaml)
class IXamlUIPresenterHost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterHost'
    _iid_ = Guid('{aafb84cd-9f6d-4f80-ac2c-0e6cb9f31659}')
    @winrt_commethod(6)
    def ResolveFileResource(self, path: WinRT_String) -> WinRT_String: ...
class IXamlUIPresenterHost2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterHost2'
    _iid_ = Guid('{61595672-7ca4-4a21-b56a-88f4812388ca}')
    @winrt_commethod(6)
    def GetGenericXamlFilePath(self) -> WinRT_String: ...
class IXamlUIPresenterHost3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterHost3'
    _iid_ = Guid('{b14292bf-7320-41bb-9f26-4d6fd34db45a}')
    @winrt_commethod(6)
    def ResolveDictionaryResource(self, dictionary: Windows.UI.Xaml.ResourceDictionary, dictionaryKey: Windows.Win32.System.WinRT.IInspectable_head, suggestedValue: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IXamlUIPresenterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics'
    _iid_ = Guid('{71eaeac8-45e1-4192-85aa-3a422edd23cf}')
    @winrt_commethod(6)
    def get_CompleteTimelinesAutomatically(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CompleteTimelinesAutomatically(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def SetHost(self, host: Windows.UI.Xaml.Hosting.IXamlUIPresenterHost) -> Void: ...
    @winrt_commethod(9)
    def NotifyWindowSizeChanged(self) -> Void: ...
    CompleteTimelinesAutomatically = property(get_CompleteTimelinesAutomatically, put_CompleteTimelinesAutomatically)
class IXamlUIPresenterStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics2'
    _iid_ = Guid('{5c6b68d2-cf1c-4f53-bf09-6a745f7a9703}')
    @winrt_commethod(6)
    def GetFlyoutPlacementTargetInfo(self, placementTarget: Windows.UI.Xaml.FrameworkElement, preferredPlacement: Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, targetPreferredPlacement: POINTER(Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode), allowFallbacks: POINTER(Boolean)) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def GetFlyoutPlacement(self, placementTargetBounds: Windows.Foundation.Rect, controlSize: Windows.Foundation.Size, minControlSize: Windows.Foundation.Size, containerRect: Windows.Foundation.Rect, targetPreferredPlacement: Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, allowFallbacks: Boolean, chosenPlacement: POINTER(Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode)) -> Windows.Foundation.Rect: ...
class WindowsXamlManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IWindowsXamlManager
    _classid_ = 'Windows.UI.Xaml.Hosting.WindowsXamlManager'
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def InitializeForCurrentThread(cls: Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics) -> Windows.UI.Xaml.Hosting.WindowsXamlManager: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest
    _classid_ = 'Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_factorymethod
    def CreateInstanceWithHintRect(cls: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: Windows.Foundation.Rect) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_factorymethod
    def CreateInstanceWithHintRectAndCorrelationId(cls: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: Windows.Foundation.Rect, correlationId: Guid) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason: ...
    @winrt_mixinmethod
    def get_HintRect(self: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> Guid: ...
    Reason = property(get_Reason, None)
    HintRect = property(get_HintRect, None)
    CorrelationId = property(get_CorrelationId, None)
class XamlSourceFocusNavigationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult
    _classid_ = 'Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResultFactory, focusMoved: Boolean) -> Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    @winrt_mixinmethod
    def get_WasFocusMoved(self: Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult) -> Boolean: ...
    WasFocusMoved = property(get_WasFocusMoved, None)
class _XamlUIPresenter_Meta_(ComPtr.__class__):
    pass
class XamlUIPresenter(ComPtr, metaclass=_XamlUIPresenter_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Hosting.IXamlUIPresenter
    _classid_ = 'Windows.UI.Xaml.Hosting.XamlUIPresenter'
    @winrt_mixinmethod
    def get_RootElement(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_RootElement(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_ThemeKey(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ThemeKey(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ThemeResourcesXaml(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ThemeResourcesXaml(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetSize(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter, width: Int32, height: Int32) -> Void: ...
    @winrt_mixinmethod
    def Render(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> Void: ...
    @winrt_mixinmethod
    def Present(self: Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> Void: ...
    @winrt_classmethod
    def GetFlyoutPlacementTargetInfo(cls: Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics2, placementTarget: Windows.UI.Xaml.FrameworkElement, preferredPlacement: Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, targetPreferredPlacement: POINTER(Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode), allowFallbacks: POINTER(Boolean)) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def GetFlyoutPlacement(cls: Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics2, placementTargetBounds: Windows.Foundation.Rect, controlSize: Windows.Foundation.Size, minControlSize: Windows.Foundation.Size, containerRect: Windows.Foundation.Rect, targetPreferredPlacement: Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, allowFallbacks: Boolean, chosenPlacement: POINTER(Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode)) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def get_CompleteTimelinesAutomatically(cls: Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics) -> Boolean: ...
    @winrt_classmethod
    def put_CompleteTimelinesAutomatically(cls: Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def SetHost(cls: Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics, host: Windows.UI.Xaml.Hosting.IXamlUIPresenterHost) -> Void: ...
    @winrt_classmethod
    def NotifyWindowSizeChanged(cls: Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics) -> Void: ...
    RootElement = property(get_RootElement, put_RootElement)
    ThemeKey = property(get_ThemeKey, put_ThemeKey)
    ThemeResourcesXaml = property(get_ThemeResourcesXaml, put_ThemeResourcesXaml)
    _XamlUIPresenter_Meta_.CompleteTimelinesAutomatically = property(get_CompleteTimelinesAutomatically.__wrapped__, put_CompleteTimelinesAutomatically.__wrapped__)
make_head(_module, 'DesignerAppExitedEventArgs')
make_head(_module, 'DesignerAppManager')
make_head(_module, 'DesignerAppView')
make_head(_module, 'DesktopWindowXamlSource')
make_head(_module, 'DesktopWindowXamlSourceGotFocusEventArgs')
make_head(_module, 'DesktopWindowXamlSourceTakeFocusRequestedEventArgs')
make_head(_module, 'ElementCompositionPreview')
make_head(_module, 'IDesignerAppExitedEventArgs')
make_head(_module, 'IDesignerAppManager')
make_head(_module, 'IDesignerAppManagerFactory')
make_head(_module, 'IDesignerAppView')
make_head(_module, 'IDesktopWindowXamlSource')
make_head(_module, 'IDesktopWindowXamlSourceFactory')
make_head(_module, 'IDesktopWindowXamlSourceGotFocusEventArgs')
make_head(_module, 'IDesktopWindowXamlSourceTakeFocusRequestedEventArgs')
make_head(_module, 'IElementCompositionPreview')
make_head(_module, 'IElementCompositionPreviewStatics')
make_head(_module, 'IElementCompositionPreviewStatics2')
make_head(_module, 'IElementCompositionPreviewStatics3')
make_head(_module, 'IWindowsXamlManager')
make_head(_module, 'IWindowsXamlManagerStatics')
make_head(_module, 'IXamlSourceFocusNavigationRequest')
make_head(_module, 'IXamlSourceFocusNavigationRequestFactory')
make_head(_module, 'IXamlSourceFocusNavigationResult')
make_head(_module, 'IXamlSourceFocusNavigationResultFactory')
make_head(_module, 'IXamlUIPresenter')
make_head(_module, 'IXamlUIPresenterHost')
make_head(_module, 'IXamlUIPresenterHost2')
make_head(_module, 'IXamlUIPresenterHost3')
make_head(_module, 'IXamlUIPresenterStatics')
make_head(_module, 'IXamlUIPresenterStatics2')
make_head(_module, 'WindowsXamlManager')
make_head(_module, 'XamlSourceFocusNavigationRequest')
make_head(_module, 'XamlSourceFocusNavigationResult')
make_head(_module, 'XamlUIPresenter')
