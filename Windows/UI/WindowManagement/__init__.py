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
import Windows.UI.WindowManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AppWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindow
    _classid_ = 'Windows.UI.WindowManagement.AppWindow'
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.UI.UIContentRoot: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def get_Frame(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.UI.WindowManagement.AppWindowFrame: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.UI.WindowManagement.IAppWindow) -> Boolean: ...
    @winrt_mixinmethod
    def get_PersistedStateId(self: Windows.UI.WindowManagement.IAppWindow) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PersistedStateId(self: Windows.UI.WindowManagement.IAppWindow, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Presenter(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.UI.WindowManagement.AppWindowPresenter: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.UI.WindowManagement.IAppWindow) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.UI.WindowManagement.IAppWindow, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TitleBar(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.UI.WindowManagement.AppWindowTitleBar: ...
    @winrt_mixinmethod
    def get_UIContext(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.UI.UIContext: ...
    @winrt_mixinmethod
    def get_WindowingEnvironment(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_mixinmethod
    def CloseAsync(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetPlacement(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.UI.WindowManagement.AppWindowPlacement: ...
    @winrt_mixinmethod
    def GetDisplayRegions(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.DisplayRegion]: ...
    @winrt_mixinmethod
    def RequestMoveToDisplayRegion(self: Windows.UI.WindowManagement.IAppWindow, displayRegion: Windows.UI.WindowManagement.DisplayRegion) -> Void: ...
    @winrt_mixinmethod
    def RequestMoveAdjacentToCurrentView(self: Windows.UI.WindowManagement.IAppWindow) -> Void: ...
    @winrt_mixinmethod
    def RequestMoveAdjacentToWindow(self: Windows.UI.WindowManagement.IAppWindow, anchorWindow: Windows.UI.WindowManagement.AppWindow) -> Void: ...
    @winrt_mixinmethod
    def RequestMoveRelativeToWindowContent(self: Windows.UI.WindowManagement.IAppWindow, anchorWindow: Windows.UI.WindowManagement.AppWindow, contentOffset: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def RequestMoveRelativeToCurrentViewContent(self: Windows.UI.WindowManagement.IAppWindow, contentOffset: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def RequestMoveRelativeToDisplayRegion(self: Windows.UI.WindowManagement.IAppWindow, displayRegion: Windows.UI.WindowManagement.DisplayRegion, displayRegionOffset: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def RequestSize(self: Windows.UI.WindowManagement.IAppWindow, frameSize: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def TryShowAsync(self: Windows.UI.WindowManagement.IAppWindow) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.UI.WindowManagement.IAppWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.AppWindow, Windows.UI.WindowManagement.AppWindowChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.UI.WindowManagement.IAppWindow, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.UI.WindowManagement.IAppWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.AppWindow, Windows.UI.WindowManagement.AppWindowClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.UI.WindowManagement.IAppWindow, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CloseRequested(self: Windows.UI.WindowManagement.IAppWindow, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.AppWindow, Windows.UI.WindowManagement.AppWindowCloseRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CloseRequested(self: Windows.UI.WindowManagement.IAppWindow, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryCreateAsync(cls: Windows.UI.WindowManagement.IAppWindowStatics) -> Windows.Foundation.IAsyncOperation[Windows.UI.WindowManagement.AppWindow]: ...
    @winrt_classmethod
    def ClearAllPersistedState(cls: Windows.UI.WindowManagement.IAppWindowStatics) -> Void: ...
    @winrt_classmethod
    def ClearPersistedState(cls: Windows.UI.WindowManagement.IAppWindowStatics, key: WinRT_String) -> Void: ...
    Content = property(get_Content, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
    Frame = property(get_Frame, None)
    IsVisible = property(get_IsVisible, None)
    PersistedStateId = property(get_PersistedStateId, put_PersistedStateId)
    Presenter = property(get_Presenter, None)
    Title = property(get_Title, put_Title)
    TitleBar = property(get_TitleBar, None)
    UIContext = property(get_UIContext, None)
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class AppWindowChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowChangedEventArgs
    _classid_ = 'Windows.UI.WindowManagement.AppWindowChangedEventArgs'
    @winrt_mixinmethod
    def get_DidAvailableWindowPresentationsChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_DidDisplayRegionsChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_DidFrameChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_DidSizeChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_DidTitleBarChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_DidVisibilityChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_DidWindowingEnvironmentChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_DidWindowPresentationChange(self: Windows.UI.WindowManagement.IAppWindowChangedEventArgs) -> Boolean: ...
    DidAvailableWindowPresentationsChange = property(get_DidAvailableWindowPresentationsChange, None)
    DidDisplayRegionsChange = property(get_DidDisplayRegionsChange, None)
    DidFrameChange = property(get_DidFrameChange, None)
    DidSizeChange = property(get_DidSizeChange, None)
    DidTitleBarChange = property(get_DidTitleBarChange, None)
    DidVisibilityChange = property(get_DidVisibilityChange, None)
    DidWindowingEnvironmentChange = property(get_DidWindowingEnvironmentChange, None)
    DidWindowPresentationChange = property(get_DidWindowPresentationChange, None)
class AppWindowCloseRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowCloseRequestedEventArgs
    _classid_ = 'Windows.UI.WindowManagement.AppWindowCloseRequestedEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: Windows.UI.WindowManagement.IAppWindowCloseRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.UI.WindowManagement.IAppWindowCloseRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.WindowManagement.IAppWindowCloseRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
class AppWindowClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowClosedEventArgs
    _classid_ = 'Windows.UI.WindowManagement.AppWindowClosedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.UI.WindowManagement.IAppWindowClosedEventArgs) -> Windows.UI.WindowManagement.AppWindowClosedReason: ...
    Reason = property(get_Reason, None)
AppWindowClosedReason = Int32
AppWindowClosedReason_Other: AppWindowClosedReason = 0
AppWindowClosedReason_AppInitiated: AppWindowClosedReason = 1
AppWindowClosedReason_UserInitiated: AppWindowClosedReason = 2
class AppWindowFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowFrame
    _classid_ = 'Windows.UI.WindowManagement.AppWindowFrame'
    @winrt_mixinmethod
    def GetFrameStyle(self: Windows.UI.WindowManagement.IAppWindowFrameStyle) -> Windows.UI.WindowManagement.AppWindowFrameStyle: ...
    @winrt_mixinmethod
    def SetFrameStyle(self: Windows.UI.WindowManagement.IAppWindowFrameStyle, frameStyle: Windows.UI.WindowManagement.AppWindowFrameStyle) -> Void: ...
    @winrt_mixinmethod
    def get_DragRegionVisuals(self: Windows.UI.WindowManagement.IAppWindowFrame) -> Windows.Foundation.Collections.IVector[Windows.UI.Composition.IVisualElement]: ...
    DragRegionVisuals = property(get_DragRegionVisuals, None)
AppWindowFrameStyle = Int32
AppWindowFrameStyle_Default: AppWindowFrameStyle = 0
AppWindowFrameStyle_NoFrame: AppWindowFrameStyle = 1
class AppWindowPlacement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowPlacement
    _classid_ = 'Windows.UI.WindowManagement.AppWindowPlacement'
    @winrt_mixinmethod
    def get_DisplayRegion(self: Windows.UI.WindowManagement.IAppWindowPlacement) -> Windows.UI.WindowManagement.DisplayRegion: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.WindowManagement.IAppWindowPlacement) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.WindowManagement.IAppWindowPlacement) -> Windows.Foundation.Size: ...
    DisplayRegion = property(get_DisplayRegion, None)
    Offset = property(get_Offset, None)
    Size = property(get_Size, None)
class AppWindowPresentationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowPresentationConfiguration
    _classid_ = 'Windows.UI.WindowManagement.AppWindowPresentationConfiguration'
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.UI.WindowManagement.AppWindowPresentationKind: ...
    Kind = property(get_Kind, None)
AppWindowPresentationKind = Int32
AppWindowPresentationKind_Default: AppWindowPresentationKind = 0
AppWindowPresentationKind_CompactOverlay: AppWindowPresentationKind = 1
AppWindowPresentationKind_FullScreen: AppWindowPresentationKind = 2
class AppWindowPresenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowPresenter
    _classid_ = 'Windows.UI.WindowManagement.AppWindowPresenter'
    @winrt_mixinmethod
    def GetConfiguration(self: Windows.UI.WindowManagement.IAppWindowPresenter) -> Windows.UI.WindowManagement.AppWindowPresentationConfiguration: ...
    @winrt_mixinmethod
    def IsPresentationSupported(self: Windows.UI.WindowManagement.IAppWindowPresenter, presentationKind: Windows.UI.WindowManagement.AppWindowPresentationKind) -> Boolean: ...
    @winrt_mixinmethod
    def RequestPresentation(self: Windows.UI.WindowManagement.IAppWindowPresenter, configuration: Windows.UI.WindowManagement.AppWindowPresentationConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def RequestPresentationByKind(self: Windows.UI.WindowManagement.IAppWindowPresenter, presentationKind: Windows.UI.WindowManagement.AppWindowPresentationKind) -> Boolean: ...
class AppWindowTitleBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowTitleBar
    _classid_ = 'Windows.UI.WindowManagement.AppWindowTitleBar'
    @winrt_mixinmethod
    def GetPreferredVisibility(self: Windows.UI.WindowManagement.IAppWindowTitleBarVisibility) -> Windows.UI.WindowManagement.AppWindowTitleBarVisibility: ...
    @winrt_mixinmethod
    def SetPreferredVisibility(self: Windows.UI.WindowManagement.IAppWindowTitleBarVisibility, visibilityMode: Windows.UI.WindowManagement.AppWindowTitleBarVisibility) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonHoverBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonHoverBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonHoverForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonHoverForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonInactiveBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonInactiveBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonInactiveForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonInactiveForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonPressedBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonPressedBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonPressedForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonPressedForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ExtendsContentIntoTitleBar(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExtendsContentIntoTitleBar(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_InactiveBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_InactiveBackgroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_InactiveForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_InactiveForegroundColor(self: Windows.UI.WindowManagement.IAppWindowTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Boolean: ...
    @winrt_mixinmethod
    def GetTitleBarOcclusions(self: Windows.UI.WindowManagement.IAppWindowTitleBar) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.AppWindowTitleBarOcclusion]: ...
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ButtonBackgroundColor = property(get_ButtonBackgroundColor, put_ButtonBackgroundColor)
    ButtonForegroundColor = property(get_ButtonForegroundColor, put_ButtonForegroundColor)
    ButtonHoverBackgroundColor = property(get_ButtonHoverBackgroundColor, put_ButtonHoverBackgroundColor)
    ButtonHoverForegroundColor = property(get_ButtonHoverForegroundColor, put_ButtonHoverForegroundColor)
    ButtonInactiveBackgroundColor = property(get_ButtonInactiveBackgroundColor, put_ButtonInactiveBackgroundColor)
    ButtonInactiveForegroundColor = property(get_ButtonInactiveForegroundColor, put_ButtonInactiveForegroundColor)
    ButtonPressedBackgroundColor = property(get_ButtonPressedBackgroundColor, put_ButtonPressedBackgroundColor)
    ButtonPressedForegroundColor = property(get_ButtonPressedForegroundColor, put_ButtonPressedForegroundColor)
    ExtendsContentIntoTitleBar = property(get_ExtendsContentIntoTitleBar, put_ExtendsContentIntoTitleBar)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    InactiveBackgroundColor = property(get_InactiveBackgroundColor, put_InactiveBackgroundColor)
    InactiveForegroundColor = property(get_InactiveForegroundColor, put_InactiveForegroundColor)
    IsVisible = property(get_IsVisible, None)
class AppWindowTitleBarOcclusion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IAppWindowTitleBarOcclusion
    _classid_ = 'Windows.UI.WindowManagement.AppWindowTitleBarOcclusion'
    @winrt_mixinmethod
    def get_OccludingRect(self: Windows.UI.WindowManagement.IAppWindowTitleBarOcclusion) -> Windows.Foundation.Rect: ...
    OccludingRect = property(get_OccludingRect, None)
AppWindowTitleBarVisibility = Int32
AppWindowTitleBarVisibility_Default: AppWindowTitleBarVisibility = 0
AppWindowTitleBarVisibility_AlwaysHidden: AppWindowTitleBarVisibility = 1
class CompactOverlayPresentationConfiguration(ComPtr):
    extends: Windows.UI.WindowManagement.AppWindowPresentationConfiguration
    default_interface: Windows.UI.WindowManagement.ICompactOverlayPresentationConfiguration
    _classid_ = 'Windows.UI.WindowManagement.CompactOverlayPresentationConfiguration'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.WindowManagement.CompactOverlayPresentationConfiguration: ...
class DefaultPresentationConfiguration(ComPtr):
    extends: Windows.UI.WindowManagement.AppWindowPresentationConfiguration
    default_interface: Windows.UI.WindowManagement.IDefaultPresentationConfiguration
    _classid_ = 'Windows.UI.WindowManagement.DefaultPresentationConfiguration'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.WindowManagement.DefaultPresentationConfiguration: ...
class DisplayRegion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IDisplayRegion
    _classid_ = 'Windows.UI.WindowManagement.DisplayRegion'
    @winrt_mixinmethod
    def get_DisplayMonitorDeviceId(self: Windows.UI.WindowManagement.IDisplayRegion) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.UI.WindowManagement.IDisplayRegion) -> Boolean: ...
    @winrt_mixinmethod
    def get_WorkAreaOffset(self: Windows.UI.WindowManagement.IDisplayRegion) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_WorkAreaSize(self: Windows.UI.WindowManagement.IDisplayRegion) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_WindowingEnvironment(self: Windows.UI.WindowManagement.IDisplayRegion) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.UI.WindowManagement.IDisplayRegion, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.DisplayRegion, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.UI.WindowManagement.IDisplayRegion, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DisplayMonitorDeviceId = property(get_DisplayMonitorDeviceId, None)
    IsVisible = property(get_IsVisible, None)
    WorkAreaOffset = property(get_WorkAreaOffset, None)
    WorkAreaSize = property(get_WorkAreaSize, None)
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class FullScreenPresentationConfiguration(ComPtr):
    extends: Windows.UI.WindowManagement.AppWindowPresentationConfiguration
    default_interface: Windows.UI.WindowManagement.IFullScreenPresentationConfiguration
    _classid_ = 'Windows.UI.WindowManagement.FullScreenPresentationConfiguration'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.WindowManagement.FullScreenPresentationConfiguration: ...
    @winrt_mixinmethod
    def get_IsExclusive(self: Windows.UI.WindowManagement.IFullScreenPresentationConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsExclusive(self: Windows.UI.WindowManagement.IFullScreenPresentationConfiguration, value: Boolean) -> Void: ...
    IsExclusive = property(get_IsExclusive, put_IsExclusive)
class IAppWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindow'
    _iid_ = Guid('{663014a6-b75e-5dbd-995c-f0117fa3fb61}')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.UI.UIContentRoot: ...
    @winrt_commethod(7)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    @winrt_commethod(8)
    def get_Frame(self) -> Windows.UI.WindowManagement.AppWindowFrame: ...
    @winrt_commethod(9)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_PersistedStateId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_PersistedStateId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Presenter(self) -> Windows.UI.WindowManagement.AppWindowPresenter: ...
    @winrt_commethod(13)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_TitleBar(self) -> Windows.UI.WindowManagement.AppWindowTitleBar: ...
    @winrt_commethod(16)
    def get_UIContext(self) -> Windows.UI.UIContext: ...
    @winrt_commethod(17)
    def get_WindowingEnvironment(self) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_commethod(18)
    def CloseAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def GetPlacement(self) -> Windows.UI.WindowManagement.AppWindowPlacement: ...
    @winrt_commethod(20)
    def GetDisplayRegions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.DisplayRegion]: ...
    @winrt_commethod(21)
    def RequestMoveToDisplayRegion(self, displayRegion: Windows.UI.WindowManagement.DisplayRegion) -> Void: ...
    @winrt_commethod(22)
    def RequestMoveAdjacentToCurrentView(self) -> Void: ...
    @winrt_commethod(23)
    def RequestMoveAdjacentToWindow(self, anchorWindow: Windows.UI.WindowManagement.AppWindow) -> Void: ...
    @winrt_commethod(24)
    def RequestMoveRelativeToWindowContent(self, anchorWindow: Windows.UI.WindowManagement.AppWindow, contentOffset: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(25)
    def RequestMoveRelativeToCurrentViewContent(self, contentOffset: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(26)
    def RequestMoveRelativeToDisplayRegion(self, displayRegion: Windows.UI.WindowManagement.DisplayRegion, displayRegionOffset: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(27)
    def RequestSize(self, frameSize: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(28)
    def TryShowAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(29)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.AppWindow, Windows.UI.WindowManagement.AppWindowChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.AppWindow, Windows.UI.WindowManagement.AppWindowClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def add_CloseRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.AppWindow, Windows.UI.WindowManagement.AppWindowCloseRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(34)
    def remove_CloseRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Content = property(get_Content, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
    Frame = property(get_Frame, None)
    IsVisible = property(get_IsVisible, None)
    PersistedStateId = property(get_PersistedStateId, put_PersistedStateId)
    Presenter = property(get_Presenter, None)
    Title = property(get_Title, put_Title)
    TitleBar = property(get_TitleBar, None)
    UIContext = property(get_UIContext, None)
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class IAppWindowChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowChangedEventArgs'
    _iid_ = Guid('{1de1f3be-a655-55ad-b2b6-eb240f880356}')
    @winrt_commethod(6)
    def get_DidAvailableWindowPresentationsChange(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_DidDisplayRegionsChange(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_DidFrameChange(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_DidSizeChange(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_DidTitleBarChange(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_DidVisibilityChange(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_DidWindowingEnvironmentChange(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_DidWindowPresentationChange(self) -> Boolean: ...
    DidAvailableWindowPresentationsChange = property(get_DidAvailableWindowPresentationsChange, None)
    DidDisplayRegionsChange = property(get_DidDisplayRegionsChange, None)
    DidFrameChange = property(get_DidFrameChange, None)
    DidSizeChange = property(get_DidSizeChange, None)
    DidTitleBarChange = property(get_DidTitleBarChange, None)
    DidVisibilityChange = property(get_DidVisibilityChange, None)
    DidWindowingEnvironmentChange = property(get_DidWindowingEnvironmentChange, None)
    DidWindowPresentationChange = property(get_DidWindowPresentationChange, None)
class IAppWindowCloseRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowCloseRequestedEventArgs'
    _iid_ = Guid('{e9ff01da-e7a2-57a8-8b5e-39c4003afdbb}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
class IAppWindowClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowClosedEventArgs'
    _iid_ = Guid('{cc7df816-9520-5a06-821e-456ad8b358aa}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.UI.WindowManagement.AppWindowClosedReason: ...
    Reason = property(get_Reason, None)
class IAppWindowFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowFrame'
    _iid_ = Guid('{9ee22601-7e5d-52af-846b-01dc6c296567}')
    @winrt_commethod(6)
    def get_DragRegionVisuals(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Composition.IVisualElement]: ...
    DragRegionVisuals = property(get_DragRegionVisuals, None)
class IAppWindowFrameStyle(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowFrameStyle'
    _iid_ = Guid('{ac412946-e1ac-5230-944a-c60873dcf4a9}')
    @winrt_commethod(6)
    def GetFrameStyle(self) -> Windows.UI.WindowManagement.AppWindowFrameStyle: ...
    @winrt_commethod(7)
    def SetFrameStyle(self, frameStyle: Windows.UI.WindowManagement.AppWindowFrameStyle) -> Void: ...
class IAppWindowPlacement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowPlacement'
    _iid_ = Guid('{03dc815e-e7a9-5857-9c03-7d670594410e}')
    @winrt_commethod(6)
    def get_DisplayRegion(self) -> Windows.UI.WindowManagement.DisplayRegion: ...
    @winrt_commethod(7)
    def get_Offset(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Size(self) -> Windows.Foundation.Size: ...
    DisplayRegion = property(get_DisplayRegion, None)
    Offset = property(get_Offset, None)
    Size = property(get_Size, None)
class IAppWindowPresentationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowPresentationConfiguration'
    _iid_ = Guid('{b5a43ee3-df33-5e67-bd31-1072457300df}')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.UI.WindowManagement.AppWindowPresentationKind: ...
    Kind = property(get_Kind, None)
class IAppWindowPresentationConfigurationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowPresentationConfigurationFactory'
    _iid_ = Guid('{fd3606a6-7875-5de8-84ff-6351ee13dd0d}')
class IAppWindowPresenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowPresenter'
    _iid_ = Guid('{5ae9ed73-e1fd-5317-ad78-5a3ed271bbde}')
    @winrt_commethod(6)
    def GetConfiguration(self) -> Windows.UI.WindowManagement.AppWindowPresentationConfiguration: ...
    @winrt_commethod(7)
    def IsPresentationSupported(self, presentationKind: Windows.UI.WindowManagement.AppWindowPresentationKind) -> Boolean: ...
    @winrt_commethod(8)
    def RequestPresentation(self, configuration: Windows.UI.WindowManagement.AppWindowPresentationConfiguration) -> Boolean: ...
    @winrt_commethod(9)
    def RequestPresentationByKind(self, presentationKind: Windows.UI.WindowManagement.AppWindowPresentationKind) -> Boolean: ...
class IAppWindowStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowStatics'
    _iid_ = Guid('{ff1f3ea3-b769-50ef-9873-108cd0e89746}')
    @winrt_commethod(6)
    def TryCreateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.WindowManagement.AppWindow]: ...
    @winrt_commethod(7)
    def ClearAllPersistedState(self) -> Void: ...
    @winrt_commethod(8)
    def ClearPersistedState(self, key: WinRT_String) -> Void: ...
class IAppWindowTitleBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowTitleBar'
    _iid_ = Guid('{6e932c84-f644-541d-a2d7-0c262437842d}')
    @winrt_commethod(6)
    def get_BackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(7)
    def put_BackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(8)
    def get_ButtonBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(9)
    def put_ButtonBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(10)
    def get_ButtonForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(11)
    def put_ButtonForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(12)
    def get_ButtonHoverBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(13)
    def put_ButtonHoverBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(14)
    def get_ButtonHoverForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(15)
    def put_ButtonHoverForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(16)
    def get_ButtonInactiveBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(17)
    def put_ButtonInactiveBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(18)
    def get_ButtonInactiveForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(19)
    def put_ButtonInactiveForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(20)
    def get_ButtonPressedBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(21)
    def put_ButtonPressedBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(22)
    def get_ButtonPressedForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(23)
    def put_ButtonPressedForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(24)
    def get_ExtendsContentIntoTitleBar(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_ExtendsContentIntoTitleBar(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def get_ForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(27)
    def put_ForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(28)
    def get_InactiveBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(29)
    def put_InactiveBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(30)
    def get_InactiveForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(31)
    def put_InactiveForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(32)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(33)
    def GetTitleBarOcclusions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.AppWindowTitleBarOcclusion]: ...
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ButtonBackgroundColor = property(get_ButtonBackgroundColor, put_ButtonBackgroundColor)
    ButtonForegroundColor = property(get_ButtonForegroundColor, put_ButtonForegroundColor)
    ButtonHoverBackgroundColor = property(get_ButtonHoverBackgroundColor, put_ButtonHoverBackgroundColor)
    ButtonHoverForegroundColor = property(get_ButtonHoverForegroundColor, put_ButtonHoverForegroundColor)
    ButtonInactiveBackgroundColor = property(get_ButtonInactiveBackgroundColor, put_ButtonInactiveBackgroundColor)
    ButtonInactiveForegroundColor = property(get_ButtonInactiveForegroundColor, put_ButtonInactiveForegroundColor)
    ButtonPressedBackgroundColor = property(get_ButtonPressedBackgroundColor, put_ButtonPressedBackgroundColor)
    ButtonPressedForegroundColor = property(get_ButtonPressedForegroundColor, put_ButtonPressedForegroundColor)
    ExtendsContentIntoTitleBar = property(get_ExtendsContentIntoTitleBar, put_ExtendsContentIntoTitleBar)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    InactiveBackgroundColor = property(get_InactiveBackgroundColor, put_InactiveBackgroundColor)
    InactiveForegroundColor = property(get_InactiveForegroundColor, put_InactiveForegroundColor)
    IsVisible = property(get_IsVisible, None)
class IAppWindowTitleBarOcclusion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowTitleBarOcclusion'
    _iid_ = Guid('{fea3cffd-2ccf-5fc3-aeae-f843876bf37e}')
    @winrt_commethod(6)
    def get_OccludingRect(self) -> Windows.Foundation.Rect: ...
    OccludingRect = property(get_OccludingRect, None)
class IAppWindowTitleBarVisibility(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IAppWindowTitleBarVisibility'
    _iid_ = Guid('{a215a4e3-6e7e-5651-8c3b-624819528154}')
    @winrt_commethod(6)
    def GetPreferredVisibility(self) -> Windows.UI.WindowManagement.AppWindowTitleBarVisibility: ...
    @winrt_commethod(7)
    def SetPreferredVisibility(self, visibilityMode: Windows.UI.WindowManagement.AppWindowTitleBarVisibility) -> Void: ...
class ICompactOverlayPresentationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.ICompactOverlayPresentationConfiguration'
    _iid_ = Guid('{a7e5750f-5730-56c6-8e1f-d63ff4d7980d}')
class IDefaultPresentationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IDefaultPresentationConfiguration'
    _iid_ = Guid('{d8c2b53b-2168-5703-a853-d525589fe2b9}')
class IDisplayRegion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IDisplayRegion'
    _iid_ = Guid('{db50c3a2-4094-5f47-8cb1-ea01ddafaa94}')
    @winrt_commethod(6)
    def get_DisplayMonitorDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_WorkAreaOffset(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_WorkAreaSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def get_WindowingEnvironment(self) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_commethod(11)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.DisplayRegion, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DisplayMonitorDeviceId = property(get_DisplayMonitorDeviceId, None)
    IsVisible = property(get_IsVisible, None)
    WorkAreaOffset = property(get_WorkAreaOffset, None)
    WorkAreaSize = property(get_WorkAreaSize, None)
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class IFullScreenPresentationConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IFullScreenPresentationConfiguration'
    _iid_ = Guid('{43d3dcd8-d2a8-503d-a626-15533d6d5f62}')
    @winrt_commethod(6)
    def get_IsExclusive(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsExclusive(self, value: Boolean) -> Void: ...
    IsExclusive = property(get_IsExclusive, put_IsExclusive)
class IWindowServicesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IWindowServicesStatics'
    _iid_ = Guid('{cff4d519-50a6-5c64-97f6-c2d96add7f42}')
    @winrt_commethod(6)
    def FindAllTopLevelWindowIds(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowId]: ...
class IWindowingEnvironment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IWindowingEnvironment'
    _iid_ = Guid('{264363c0-2a49-5417-b3ae-48a71c63a3bd}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.UI.WindowManagement.WindowingEnvironmentKind: ...
    @winrt_commethod(8)
    def GetDisplayRegions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.DisplayRegion]: ...
    @winrt_commethod(9)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.WindowingEnvironment, Windows.UI.WindowManagement.WindowingEnvironmentChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    Kind = property(get_Kind, None)
class IWindowingEnvironmentAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IWindowingEnvironmentAddedEventArgs'
    _iid_ = Guid('{ff2a5b7f-f183-5c66-99b2-429082069299}')
    @winrt_commethod(6)
    def get_WindowingEnvironment(self) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class IWindowingEnvironmentChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IWindowingEnvironmentChangedEventArgs'
    _iid_ = Guid('{4160cfc6-023d-5e9a-b431-350e67dc978a}')
class IWindowingEnvironmentRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IWindowingEnvironmentRemovedEventArgs'
    _iid_ = Guid('{2e5b5473-beff-5e53-9316-7e775fe568b3}')
    @winrt_commethod(6)
    def get_WindowingEnvironment(self) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class IWindowingEnvironmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.IWindowingEnvironmentStatics'
    _iid_ = Guid('{874e9fb7-c642-55ab-8aa2-162f734a9a72}')
    @winrt_commethod(6)
    def FindAll(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.WindowingEnvironment]: ...
    @winrt_commethod(7)
    def FindAllWithKind(self, kind: Windows.UI.WindowManagement.WindowingEnvironmentKind) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.WindowingEnvironment]: ...
class WindowServices(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.WindowServices'
    @winrt_classmethod
    def FindAllTopLevelWindowIds(cls: Windows.UI.WindowManagement.IWindowServicesStatics) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowId]: ...
class WindowingEnvironment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IWindowingEnvironment
    _classid_ = 'Windows.UI.WindowManagement.WindowingEnvironment'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.UI.WindowManagement.IWindowingEnvironment) -> Boolean: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.WindowManagement.IWindowingEnvironment) -> Windows.UI.WindowManagement.WindowingEnvironmentKind: ...
    @winrt_mixinmethod
    def GetDisplayRegions(self: Windows.UI.WindowManagement.IWindowingEnvironment) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.DisplayRegion]: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.UI.WindowManagement.IWindowingEnvironment, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WindowManagement.WindowingEnvironment, Windows.UI.WindowManagement.WindowingEnvironmentChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.UI.WindowManagement.IWindowingEnvironment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def FindAll(cls: Windows.UI.WindowManagement.IWindowingEnvironmentStatics) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.WindowingEnvironment]: ...
    @winrt_classmethod
    def FindAllWithKind(cls: Windows.UI.WindowManagement.IWindowingEnvironmentStatics, kind: Windows.UI.WindowManagement.WindowingEnvironmentKind) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.WindowingEnvironment]: ...
    IsEnabled = property(get_IsEnabled, None)
    Kind = property(get_Kind, None)
class WindowingEnvironmentAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IWindowingEnvironmentAddedEventArgs
    _classid_ = 'Windows.UI.WindowManagement.WindowingEnvironmentAddedEventArgs'
    @winrt_mixinmethod
    def get_WindowingEnvironment(self: Windows.UI.WindowManagement.IWindowingEnvironmentAddedEventArgs) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class WindowingEnvironmentChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IWindowingEnvironmentChangedEventArgs
    _classid_ = 'Windows.UI.WindowManagement.WindowingEnvironmentChangedEventArgs'
WindowingEnvironmentKind = Int32
WindowingEnvironmentKind_Unknown: WindowingEnvironmentKind = 0
WindowingEnvironmentKind_Overlapped: WindowingEnvironmentKind = 1
WindowingEnvironmentKind_Tiled: WindowingEnvironmentKind = 2
class WindowingEnvironmentRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.IWindowingEnvironmentRemovedEventArgs
    _classid_ = 'Windows.UI.WindowManagement.WindowingEnvironmentRemovedEventArgs'
    @winrt_mixinmethod
    def get_WindowingEnvironment(self: Windows.UI.WindowManagement.IWindowingEnvironmentRemovedEventArgs) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    WindowingEnvironment = property(get_WindowingEnvironment, None)
make_head(_module, 'AppWindow')
make_head(_module, 'AppWindowChangedEventArgs')
make_head(_module, 'AppWindowCloseRequestedEventArgs')
make_head(_module, 'AppWindowClosedEventArgs')
make_head(_module, 'AppWindowFrame')
make_head(_module, 'AppWindowPlacement')
make_head(_module, 'AppWindowPresentationConfiguration')
make_head(_module, 'AppWindowPresenter')
make_head(_module, 'AppWindowTitleBar')
make_head(_module, 'AppWindowTitleBarOcclusion')
make_head(_module, 'CompactOverlayPresentationConfiguration')
make_head(_module, 'DefaultPresentationConfiguration')
make_head(_module, 'DisplayRegion')
make_head(_module, 'FullScreenPresentationConfiguration')
make_head(_module, 'IAppWindow')
make_head(_module, 'IAppWindowChangedEventArgs')
make_head(_module, 'IAppWindowCloseRequestedEventArgs')
make_head(_module, 'IAppWindowClosedEventArgs')
make_head(_module, 'IAppWindowFrame')
make_head(_module, 'IAppWindowFrameStyle')
make_head(_module, 'IAppWindowPlacement')
make_head(_module, 'IAppWindowPresentationConfiguration')
make_head(_module, 'IAppWindowPresentationConfigurationFactory')
make_head(_module, 'IAppWindowPresenter')
make_head(_module, 'IAppWindowStatics')
make_head(_module, 'IAppWindowTitleBar')
make_head(_module, 'IAppWindowTitleBarOcclusion')
make_head(_module, 'IAppWindowTitleBarVisibility')
make_head(_module, 'ICompactOverlayPresentationConfiguration')
make_head(_module, 'IDefaultPresentationConfiguration')
make_head(_module, 'IDisplayRegion')
make_head(_module, 'IFullScreenPresentationConfiguration')
make_head(_module, 'IWindowServicesStatics')
make_head(_module, 'IWindowingEnvironment')
make_head(_module, 'IWindowingEnvironmentAddedEventArgs')
make_head(_module, 'IWindowingEnvironmentChangedEventArgs')
make_head(_module, 'IWindowingEnvironmentRemovedEventArgs')
make_head(_module, 'IWindowingEnvironmentStatics')
make_head(_module, 'WindowServices')
make_head(_module, 'WindowingEnvironment')
make_head(_module, 'WindowingEnvironmentAddedEventArgs')
make_head(_module, 'WindowingEnvironmentChangedEventArgs')
make_head(_module, 'WindowingEnvironmentRemovedEventArgs')
