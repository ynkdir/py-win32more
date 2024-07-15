from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.UI.Composition
import win32more.Windows.UI.WindowManagement
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Controls
import win32more.Windows.UI.Xaml.Controls.Primitives
import win32more.Windows.UI.Xaml.Hosting
import win32more.Windows.Win32.System.WinRT
class DesignerAppExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Hosting.IDesignerAppExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Hosting.DesignerAppExitedEventArgs'
    @winrt_mixinmethod
    def get_ExitCode(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppExitedEventArgs) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class DesignerAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Xaml.Hosting.IDesignerAppManager
    _classid_ = 'Windows.UI.Xaml.Hosting.DesignerAppManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Hosting.DesignerAppManager.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.UI.Xaml.Hosting.IDesignerAppManagerFactory, appUserModelId: WinRT_String) -> win32more.Windows.UI.Xaml.Hosting.DesignerAppManager: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppManager) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_DesignerAppExited(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Hosting.DesignerAppManager, win32more.Windows.UI.Xaml.Hosting.DesignerAppExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DesignerAppExited(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateNewViewAsync(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppManager, initialViewState: win32more.Windows.UI.Xaml.Hosting.DesignerAppViewState, initialViewSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Hosting.DesignerAppView]: ...
    @winrt_mixinmethod
    def LoadObjectIntoAppAsync(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppManager, dllName: WinRT_String, classId: Guid, initializationData: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    AppUserModelId = property(get_AppUserModelId, None)
    DesignerAppExited = event()
class DesignerAppView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Xaml.Hosting.IDesignerAppView
    _classid_ = 'Windows.UI.Xaml.Hosting.DesignerAppView'
    @winrt_mixinmethod
    def get_ApplicationViewId(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppView) -> Int32: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ViewState(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppView) -> win32more.Windows.UI.Xaml.Hosting.DesignerAppViewState: ...
    @winrt_mixinmethod
    def get_ViewSize(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppView) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def UpdateViewAsync(self: win32more.Windows.UI.Xaml.Hosting.IDesignerAppView, viewState: win32more.Windows.UI.Xaml.Hosting.DesignerAppViewState, viewSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ApplicationViewId = property(get_ApplicationViewId, None)
    ViewSize = property(get_ViewSize, None)
    ViewState = property(get_ViewState, None)
class DesignerAppViewState(Enum, Int32):
    Visible = 0
    Hidden = 1
class DesktopWindowXamlSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource
    _classid_ = 'Windows.UI.Xaml.Hosting.DesktopWindowXamlSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_HasFocus(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource) -> Boolean: ...
    @winrt_mixinmethod
    def add_TakeFocusRequested(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TakeFocusRequested(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NavigateFocus(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, request: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Content = property(get_Content, put_Content)
    HasFocus = property(get_HasFocus, None)
    TakeFocusRequested = event()
    GotFocus = event()
class DesktopWindowXamlSourceGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs
    _classid_ = 'Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class DesktopWindowXamlSourceTakeFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class ElementCompositionPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreview
    _classid_ = 'Windows.UI.Xaml.Hosting.ElementCompositionPreview'
    @winrt_classmethod
    def SetAppWindowContent(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3, appWindow: win32more.Windows.UI.WindowManagement.AppWindow, xamlContent: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def GetAppWindowContent(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3, appWindow: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def SetImplicitShowAnimation(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: win32more.Windows.UI.Xaml.UIElement, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetImplicitHideAnimation(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: win32more.Windows.UI.Xaml.UIElement, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetIsTranslationEnabled(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetPointerPositionPropertySet(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, targetElement: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_classmethod
    def GetElementVisual(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_classmethod
    def GetElementChildVisual(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_classmethod
    def SetElementChildVisual(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: win32more.Windows.UI.Xaml.UIElement, visual: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_classmethod
    def GetScrollViewerManipulationPropertySet(cls: win32more.Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, scrollViewer: win32more.Windows.UI.Xaml.Controls.ScrollViewer) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
HostingContract: UInt32 = 327680
class IDesignerAppExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppExitedEventArgs'
    _iid_ = Guid('{f6aac86a-0cad-410c-8f62-dc2936151c74}')
    @winrt_commethod(6)
    def get_ExitCode(self) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class IDesignerAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppManager'
    _iid_ = Guid('{a6272caa-d5c6-40cb-abd9-27ba43831bb7}')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_DesignerAppExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Hosting.DesignerAppManager, win32more.Windows.UI.Xaml.Hosting.DesignerAppExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_DesignerAppExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def CreateNewViewAsync(self, initialViewState: win32more.Windows.UI.Xaml.Hosting.DesignerAppViewState, initialViewSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Hosting.DesignerAppView]: ...
    @winrt_commethod(10)
    def LoadObjectIntoAppAsync(self, dllName: WinRT_String, classId: Guid, initializationData: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppUserModelId = property(get_AppUserModelId, None)
    DesignerAppExited = event()
class IDesignerAppManagerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppManagerFactory'
    _iid_ = Guid('{8f9d633b-1266-4c0e-8499-0db85bbd4c43}')
    @winrt_commethod(6)
    def Create(self, appUserModelId: WinRT_String) -> win32more.Windows.UI.Xaml.Hosting.DesignerAppManager: ...
class IDesignerAppView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesignerAppView'
    _iid_ = Guid('{5c777cea-dd71-4a84-a56f-dacb4b14706f}')
    @winrt_commethod(6)
    def get_ApplicationViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ViewState(self) -> win32more.Windows.UI.Xaml.Hosting.DesignerAppViewState: ...
    @winrt_commethod(9)
    def get_ViewSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def UpdateViewAsync(self, viewState: win32more.Windows.UI.Xaml.Hosting.DesignerAppViewState, viewSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ApplicationViewId = property(get_ApplicationViewId, None)
    ViewSize = property(get_ViewSize, None)
    ViewState = property(get_ViewState, None)
class IDesktopWindowXamlSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource'
    _iid_ = Guid('{d585bfe1-00ff-51be-ba1d-a1329956ea0a}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_Content(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_HasFocus(self) -> Boolean: ...
    @winrt_commethod(9)
    def add_TakeFocusRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceTakeFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_TakeFocusRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_GotFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource, win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSourceGotFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def NavigateFocus(self, request: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    Content = property(get_Content, put_Content)
    HasFocus = property(get_HasFocus, None)
    TakeFocusRequested = event()
    GotFocus = event()
class IDesktopWindowXamlSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceFactory'
    _iid_ = Guid('{5cd61dc0-2561-56e1-8e75-6e44173805e3}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource: ...
class IDesktopWindowXamlSourceGotFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs'
    _iid_ = Guid('{39be4849-d9cc-5b70-8f05-1ad9a4aaa342}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class IDesktopWindowXamlSourceTakeFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs'
    _iid_ = Guid('{fe61e4b9-a7af-52b3-bdb9-c3305c0b8df2}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    Request = property(get_Request, None)
class IElementCompositionPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreview'
    _iid_ = Guid('{b6f1a676-cfe6-46ac-acf6-c4687bb65e60}')
class IElementCompositionPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics'
    _iid_ = Guid('{08c92b38-ec99-4c55-bc85-a1c180b27646}')
    @winrt_commethod(6)
    def GetElementVisual(self, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def GetElementChildVisual(self, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(8)
    def SetElementChildVisual(self, element: win32more.Windows.UI.Xaml.UIElement, visual: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def GetScrollViewerManipulationPropertySet(self, scrollViewer: win32more.Windows.UI.Xaml.Controls.ScrollViewer) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
class IElementCompositionPreviewStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2'
    _iid_ = Guid('{24148fbb-23d6-4f37-ba0c-0733e799722d}')
    @winrt_commethod(6)
    def SetImplicitShowAnimation(self, element: win32more.Windows.UI.Xaml.UIElement, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(7)
    def SetImplicitHideAnimation(self, element: win32more.Windows.UI.Xaml.UIElement, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(8)
    def SetIsTranslationEnabled(self, element: win32more.Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPointerPositionPropertySet(self, targetElement: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
class IElementCompositionPreviewStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3'
    _iid_ = Guid('{843bc4c3-c105-59fe-a3d1-373c1d3e6fbc}')
    @winrt_commethod(6)
    def SetAppWindowContent(self, appWindow: win32more.Windows.UI.WindowManagement.AppWindow, xamlContent: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(7)
    def GetAppWindowContent(self, appWindow: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Xaml.UIElement: ...
class IWindowsXamlManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IWindowsXamlManager'
    _iid_ = Guid('{56096c31-1aa0-5288-8818-6e74a2dcaff5}')
class IWindowsXamlManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics'
    _iid_ = Guid('{28258a12-7d82-505b-b210-712b04a58882}')
    @winrt_commethod(6)
    def InitializeForCurrentThread(self) -> win32more.Windows.UI.Xaml.Hosting.WindowsXamlManager: ...
class IXamlSourceFocusNavigationRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest'
    _iid_ = Guid('{fbb93bb5-1496-5a80-ac00-e757359755e6}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason: ...
    @winrt_commethod(7)
    def get_HintRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_CorrelationId(self) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    HintRect = property(get_HintRect, None)
    Reason = property(get_Reason, None)
class IXamlSourceFocusNavigationRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory'
    _iid_ = Guid('{e746ab8f-b4ef-5390-97e5-cc0a2779c574}')
    @winrt_commethod(6)
    def CreateInstance(self, reason: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_commethod(7)
    def CreateInstanceWithHintRect(self, reason: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_commethod(8)
    def CreateInstanceWithHintRectAndCorrelationId(self, reason: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect, correlationId: Guid) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
class IXamlSourceFocusNavigationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult'
    _iid_ = Guid('{88d55a5f-9603-5d8f-9cc7-d1c4070d9801}')
    @winrt_commethod(6)
    def get_WasFocusMoved(self) -> Boolean: ...
    WasFocusMoved = property(get_WasFocusMoved, None)
class IXamlSourceFocusNavigationResultFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResultFactory'
    _iid_ = Guid('{43bbadbf-f9e1-5527-b8c5-09339ff2ca76}')
    @winrt_commethod(6)
    def CreateInstance(self, focusMoved: Boolean) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
class IXamlUIPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenter'
    _iid_ = Guid('{a714944a-1619-4fc6-b31b-89512ef022a2}')
    @winrt_commethod(6)
    def get_RootElement(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_RootElement(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterHost'
    _iid_ = Guid('{aafb84cd-9f6d-4f80-ac2c-0e6cb9f31659}')
    @winrt_commethod(6)
    def ResolveFileResource(self, path: WinRT_String) -> WinRT_String: ...
class IXamlUIPresenterHost2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterHost2'
    _iid_ = Guid('{61595672-7ca4-4a21-b56a-88f4812388ca}')
    @winrt_commethod(6)
    def GetGenericXamlFilePath(self) -> WinRT_String: ...
class IXamlUIPresenterHost3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterHost3'
    _iid_ = Guid('{b14292bf-7320-41bb-9f26-4d6fd34db45a}')
    @winrt_commethod(6)
    def ResolveDictionaryResource(self, dictionary: win32more.Windows.UI.Xaml.ResourceDictionary, dictionaryKey: win32more.Windows.Win32.System.WinRT.IInspectable, suggestedValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IXamlUIPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics'
    _iid_ = Guid('{71eaeac8-45e1-4192-85aa-3a422edd23cf}')
    @winrt_commethod(6)
    def get_CompleteTimelinesAutomatically(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CompleteTimelinesAutomatically(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def SetHost(self, host: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterHost) -> Void: ...
    @winrt_commethod(9)
    def NotifyWindowSizeChanged(self) -> Void: ...
    CompleteTimelinesAutomatically = property(get_CompleteTimelinesAutomatically, put_CompleteTimelinesAutomatically)
class IXamlUIPresenterStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics2'
    _iid_ = Guid('{5c6b68d2-cf1c-4f53-bf09-6a745f7a9703}')
    @winrt_commethod(6)
    def GetFlyoutPlacementTargetInfo(self, placementTarget: win32more.Windows.UI.Xaml.FrameworkElement, preferredPlacement: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, targetPreferredPlacement: POINTER(win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode), allowFallbacks: POINTER(Boolean)) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def GetFlyoutPlacement(self, placementTargetBounds: win32more.Windows.Foundation.Rect, controlSize: win32more.Windows.Foundation.Size, minControlSize: win32more.Windows.Foundation.Size, containerRect: win32more.Windows.Foundation.Rect, targetPreferredPlacement: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, allowFallbacks: Boolean, chosenPlacement: POINTER(win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode)) -> win32more.Windows.Foundation.Rect: ...
class WindowsXamlManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Xaml.Hosting.IWindowsXamlManager
    _classid_ = 'Windows.UI.Xaml.Hosting.WindowsXamlManager'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def InitializeForCurrentThread(cls: win32more.Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics) -> win32more.Windows.UI.Xaml.Hosting.WindowsXamlManager: ...
class XamlSourceFocusNavigationReason(Enum, Int32):
    Programmatic = 0
    Restore = 1
    First = 3
    Last = 4
    Left = 7
    Up = 8
    Right = 9
    Down = 10
class XamlSourceFocusNavigationRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest
    _classid_ = 'Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest.CreateInstanceWithHintRect(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest.CreateInstanceWithHintRectAndCorrelationId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_factorymethod
    def CreateInstanceWithHintRect(cls: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_factorymethod
    def CreateInstanceWithHintRectAndCorrelationId(cls: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequestFactory, reason: win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect, correlationId: Guid) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationRequest: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason: ...
    @winrt_mixinmethod
    def get_HintRect(self: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest) -> Guid: ...
    CorrelationId = property(get_CorrelationId, None)
    HintRect = property(get_HintRect, None)
    Reason = property(get_Reason, None)
class XamlSourceFocusNavigationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult
    _classid_ = 'Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResultFactory, focusMoved: Boolean) -> win32more.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationResult: ...
    @winrt_mixinmethod
    def get_WasFocusMoved(self: win32more.Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult) -> Boolean: ...
    WasFocusMoved = property(get_WasFocusMoved, None)
class _XamlUIPresenter_Meta_(ComPtr.__class__):
    pass
class XamlUIPresenter(ComPtr, metaclass=_XamlUIPresenter_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter
    _classid_ = 'Windows.UI.Xaml.Hosting.XamlUIPresenter'
    @winrt_mixinmethod
    def get_RootElement(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_RootElement(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_ThemeKey(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ThemeKey(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ThemeResourcesXaml(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ThemeResourcesXaml(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetSize(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter, width: Int32, height: Int32) -> Void: ...
    @winrt_mixinmethod
    def Render(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> Void: ...
    @winrt_mixinmethod
    def Present(self: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenter) -> Void: ...
    @winrt_classmethod
    def GetFlyoutPlacementTargetInfo(cls: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics2, placementTarget: win32more.Windows.UI.Xaml.FrameworkElement, preferredPlacement: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, targetPreferredPlacement: POINTER(win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode), allowFallbacks: POINTER(Boolean)) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def GetFlyoutPlacement(cls: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics2, placementTargetBounds: win32more.Windows.Foundation.Rect, controlSize: win32more.Windows.Foundation.Size, minControlSize: win32more.Windows.Foundation.Size, containerRect: win32more.Windows.Foundation.Rect, targetPreferredPlacement: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode, allowFallbacks: Boolean, chosenPlacement: POINTER(win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode)) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def get_CompleteTimelinesAutomatically(cls: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics) -> Boolean: ...
    @winrt_classmethod
    def put_CompleteTimelinesAutomatically(cls: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def SetHost(cls: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics, host: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterHost) -> Void: ...
    @winrt_classmethod
    def NotifyWindowSizeChanged(cls: win32more.Windows.UI.Xaml.Hosting.IXamlUIPresenterStatics) -> Void: ...
    RootElement = property(get_RootElement, put_RootElement)
    ThemeKey = property(get_ThemeKey, put_ThemeKey)
    ThemeResourcesXaml = property(get_ThemeResourcesXaml, put_ThemeResourcesXaml)
    _XamlUIPresenter_Meta_.CompleteTimelinesAutomatically = property(get_CompleteTimelinesAutomatically, put_CompleteTimelinesAutomatically)


make_ready(__name__)
