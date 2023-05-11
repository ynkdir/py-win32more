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
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.UI
import Windows.UI.Core
import Windows.UI.Popups
import Windows.UI.ViewManagement
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
class AccessibilitySettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IAccessibilitySettings
    _classid_ = 'Windows.UI.ViewManagement.AccessibilitySettings'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.ViewManagement.AccessibilitySettings: ...
    @winrt_mixinmethod
    def get_HighContrast(self: Windows.UI.ViewManagement.IAccessibilitySettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HighContrastScheme(self: Windows.UI.ViewManagement.IAccessibilitySettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_HighContrastChanged(self: Windows.UI.ViewManagement.IAccessibilitySettings, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.AccessibilitySettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HighContrastChanged(self: Windows.UI.ViewManagement.IAccessibilitySettings, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    HighContrast = property(get_HighContrast, None)
    HighContrastScheme = property(get_HighContrastScheme, None)
class ActivationViewSwitcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IActivationViewSwitcher
    _classid_ = 'Windows.UI.ViewManagement.ActivationViewSwitcher'
    @winrt_mixinmethod
    def ShowAsStandaloneAsync(self: Windows.UI.ViewManagement.IActivationViewSwitcher, viewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowAsStandaloneWithSizePreferenceAsync(self: Windows.UI.ViewManagement.IActivationViewSwitcher, viewId: Int32, sizePreference: Windows.UI.ViewManagement.ViewSizePreference) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def IsViewPresentedOnActivationVirtualDesktop(self: Windows.UI.ViewManagement.IActivationViewSwitcher, viewId: Int32) -> Boolean: ...
class _ApplicationView_Meta_(ComPtr.__class__):
    pass
class ApplicationView(ComPtr, metaclass=_ApplicationView_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IApplicationView
    _classid_ = 'Windows.UI.ViewManagement.ApplicationView'
    @winrt_mixinmethod
    def get_Orientation(self: Windows.UI.ViewManagement.IApplicationView) -> Windows.UI.ViewManagement.ApplicationViewOrientation: ...
    @winrt_mixinmethod
    def get_AdjacentToLeftDisplayEdge(self: Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_AdjacentToRightDisplayEdge(self: Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFullScreen(self: Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOnLockScreen(self: Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScreenCaptureEnabled(self: Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScreenCaptureEnabled(self: Windows.UI.ViewManagement.IApplicationView, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.UI.ViewManagement.IApplicationView, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.UI.ViewManagement.IApplicationView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.ViewManagement.IApplicationView) -> Int32: ...
    @winrt_mixinmethod
    def add_Consolidated(self: Windows.UI.ViewManagement.IApplicationView, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.ApplicationView, Windows.UI.ViewManagement.ApplicationViewConsolidatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Consolidated(self: Windows.UI.ViewManagement.IApplicationView, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressSystemOverlays(self: Windows.UI.ViewManagement.IApplicationView2) -> Boolean: ...
    @winrt_mixinmethod
    def put_SuppressSystemOverlays(self: Windows.UI.ViewManagement.IApplicationView2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_VisibleBounds(self: Windows.UI.ViewManagement.IApplicationView2) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def add_VisibleBoundsChanged(self: Windows.UI.ViewManagement.IApplicationView2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.ApplicationView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisibleBoundsChanged(self: Windows.UI.ViewManagement.IApplicationView2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetDesiredBoundsMode(self: Windows.UI.ViewManagement.IApplicationView2, boundsMode: Windows.UI.ViewManagement.ApplicationViewBoundsMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_DesiredBoundsMode(self: Windows.UI.ViewManagement.IApplicationView2) -> Windows.UI.ViewManagement.ApplicationViewBoundsMode: ...
    @winrt_mixinmethod
    def get_TitleBar(self: Windows.UI.ViewManagement.IApplicationView3) -> Windows.UI.ViewManagement.ApplicationViewTitleBar: ...
    @winrt_mixinmethod
    def get_FullScreenSystemOverlayMode(self: Windows.UI.ViewManagement.IApplicationView3) -> Windows.UI.ViewManagement.FullScreenSystemOverlayMode: ...
    @winrt_mixinmethod
    def put_FullScreenSystemOverlayMode(self: Windows.UI.ViewManagement.IApplicationView3, value: Windows.UI.ViewManagement.FullScreenSystemOverlayMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsFullScreenMode(self: Windows.UI.ViewManagement.IApplicationView3) -> Boolean: ...
    @winrt_mixinmethod
    def TryEnterFullScreenMode(self: Windows.UI.ViewManagement.IApplicationView3) -> Boolean: ...
    @winrt_mixinmethod
    def ExitFullScreenMode(self: Windows.UI.ViewManagement.IApplicationView3) -> Void: ...
    @winrt_mixinmethod
    def ShowStandardSystemOverlays(self: Windows.UI.ViewManagement.IApplicationView3) -> Void: ...
    @winrt_mixinmethod
    def TryResizeView(self: Windows.UI.ViewManagement.IApplicationView3, value: Windows.Foundation.Size) -> Boolean: ...
    @winrt_mixinmethod
    def SetPreferredMinSize(self: Windows.UI.ViewManagement.IApplicationView3, minSize: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_ViewMode(self: Windows.UI.ViewManagement.IApplicationView4) -> Windows.UI.ViewManagement.ApplicationViewMode: ...
    @winrt_mixinmethod
    def IsViewModeSupported(self: Windows.UI.ViewManagement.IApplicationView4, viewMode: Windows.UI.ViewManagement.ApplicationViewMode) -> Boolean: ...
    @winrt_mixinmethod
    def TryEnterViewModeAsync(self: Windows.UI.ViewManagement.IApplicationView4, viewMode: Windows.UI.ViewManagement.ApplicationViewMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryEnterViewModeWithPreferencesAsync(self: Windows.UI.ViewManagement.IApplicationView4, viewMode: Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: Windows.UI.ViewManagement.ViewModePreferences) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryConsolidateAsync(self: Windows.UI.ViewManagement.IApplicationView4) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_PersistedStateId(self: Windows.UI.ViewManagement.IApplicationView7) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PersistedStateId(self: Windows.UI.ViewManagement.IApplicationView7, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WindowingEnvironment(self: Windows.UI.ViewManagement.IApplicationView9) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_mixinmethod
    def GetDisplayRegions(self: Windows.UI.ViewManagement.IApplicationView9) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.DisplayRegion]: ...
    @winrt_mixinmethod
    def get_UIContext(self: Windows.UI.ViewManagement.IApplicationViewWithContext) -> Windows.UI.UIContext: ...
    @winrt_classmethod
    def ClearAllPersistedState(cls: Windows.UI.ViewManagement.IApplicationViewStatics4) -> Void: ...
    @winrt_classmethod
    def ClearPersistedState(cls: Windows.UI.ViewManagement.IApplicationViewStatics4, key: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_PreferredLaunchWindowingMode(cls: Windows.UI.ViewManagement.IApplicationViewStatics3) -> Windows.UI.ViewManagement.ApplicationViewWindowingMode: ...
    @winrt_classmethod
    def put_PreferredLaunchWindowingMode(cls: Windows.UI.ViewManagement.IApplicationViewStatics3, value: Windows.UI.ViewManagement.ApplicationViewWindowingMode) -> Void: ...
    @winrt_classmethod
    def get_PreferredLaunchViewSize(cls: Windows.UI.ViewManagement.IApplicationViewStatics3) -> Windows.Foundation.Size: ...
    @winrt_classmethod
    def put_PreferredLaunchViewSize(cls: Windows.UI.ViewManagement.IApplicationViewStatics3, value: Windows.Foundation.Size) -> Void: ...
    @winrt_classmethod
    def TryUnsnapToFullscreen(cls: Windows.UI.ViewManagement.IApplicationViewFullscreenStatics) -> Boolean: ...
    @winrt_classmethod
    def GetApplicationViewIdForWindow(cls: Windows.UI.ViewManagement.IApplicationViewInteropStatics, window: Windows.UI.Core.ICoreWindow) -> Int32: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.ViewManagement.IApplicationViewStatics2) -> Windows.UI.ViewManagement.ApplicationView: ...
    @winrt_classmethod
    def get_TerminateAppOnFinalViewClose(cls: Windows.UI.ViewManagement.IApplicationViewStatics2) -> Boolean: ...
    @winrt_classmethod
    def put_TerminateAppOnFinalViewClose(cls: Windows.UI.ViewManagement.IApplicationViewStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_Value(cls: Windows.UI.ViewManagement.IApplicationViewStatics) -> Windows.UI.ViewManagement.ApplicationViewState: ...
    @winrt_classmethod
    def TryUnsnap(cls: Windows.UI.ViewManagement.IApplicationViewStatics) -> Boolean: ...
    Orientation = property(get_Orientation, None)
    AdjacentToLeftDisplayEdge = property(get_AdjacentToLeftDisplayEdge, None)
    AdjacentToRightDisplayEdge = property(get_AdjacentToRightDisplayEdge, None)
    IsFullScreen = property(get_IsFullScreen, None)
    IsOnLockScreen = property(get_IsOnLockScreen, None)
    IsScreenCaptureEnabled = property(get_IsScreenCaptureEnabled, put_IsScreenCaptureEnabled)
    Title = property(get_Title, put_Title)
    Id = property(get_Id, None)
    SuppressSystemOverlays = property(get_SuppressSystemOverlays, put_SuppressSystemOverlays)
    VisibleBounds = property(get_VisibleBounds, None)
    DesiredBoundsMode = property(get_DesiredBoundsMode, None)
    TitleBar = property(get_TitleBar, None)
    FullScreenSystemOverlayMode = property(get_FullScreenSystemOverlayMode, put_FullScreenSystemOverlayMode)
    IsFullScreenMode = property(get_IsFullScreenMode, None)
    ViewMode = property(get_ViewMode, None)
    PersistedStateId = property(get_PersistedStateId, put_PersistedStateId)
    WindowingEnvironment = property(get_WindowingEnvironment, None)
    UIContext = property(get_UIContext, None)
    _ApplicationView_Meta_.PreferredLaunchWindowingMode = property(get_PreferredLaunchWindowingMode.__wrapped__, put_PreferredLaunchWindowingMode.__wrapped__)
    _ApplicationView_Meta_.PreferredLaunchViewSize = property(get_PreferredLaunchViewSize.__wrapped__, put_PreferredLaunchViewSize.__wrapped__)
    _ApplicationView_Meta_.TerminateAppOnFinalViewClose = property(get_TerminateAppOnFinalViewClose.__wrapped__, put_TerminateAppOnFinalViewClose.__wrapped__)
    _ApplicationView_Meta_.Value = property(get_Value.__wrapped__, None)
ApplicationViewBoundsMode = Int32
ApplicationViewBoundsMode_UseVisible: ApplicationViewBoundsMode = 0
ApplicationViewBoundsMode_UseCoreWindow: ApplicationViewBoundsMode = 1
class ApplicationViewConsolidatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewConsolidatedEventArgs'
    @winrt_mixinmethod
    def get_IsUserInitiated(self: Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAppInitiated(self: Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs2) -> Boolean: ...
    IsUserInitiated = property(get_IsUserInitiated, None)
    IsAppInitiated = property(get_IsAppInitiated, None)
ApplicationViewMode = Int32
ApplicationViewMode_Default: ApplicationViewMode = 0
ApplicationViewMode_CompactOverlay: ApplicationViewMode = 1
ApplicationViewOrientation = Int32
ApplicationViewOrientation_Landscape: ApplicationViewOrientation = 0
ApplicationViewOrientation_Portrait: ApplicationViewOrientation = 1
class _ApplicationViewScaling_Meta_(ComPtr.__class__):
    pass
class ApplicationViewScaling(ComPtr, metaclass=_ApplicationViewScaling_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IApplicationViewScaling
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewScaling'
    @winrt_classmethod
    def get_DisableLayoutScaling(cls: Windows.UI.ViewManagement.IApplicationViewScalingStatics) -> Boolean: ...
    @winrt_classmethod
    def TrySetDisableLayoutScaling(cls: Windows.UI.ViewManagement.IApplicationViewScalingStatics, disableLayoutScaling: Boolean) -> Boolean: ...
    _ApplicationViewScaling_Meta_.DisableLayoutScaling = property(get_DisableLayoutScaling.__wrapped__, None)
ApplicationViewState = Int32
ApplicationViewState_FullScreenLandscape: ApplicationViewState = 0
ApplicationViewState_Filled: ApplicationViewState = 1
ApplicationViewState_Snapped: ApplicationViewState = 2
ApplicationViewState_FullScreenPortrait: ApplicationViewState = 3
class ApplicationViewSwitcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewSwitcher'
    @winrt_classmethod
    def TryShowAsViewModeAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics3, viewId: Int32, viewMode: Windows.UI.ViewManagement.ApplicationViewMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def TryShowAsViewModeWithPreferencesAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics3, viewId: Int32, viewMode: Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: Windows.UI.ViewManagement.ViewModePreferences) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def DisableSystemViewActivationPolicy(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics2) -> Void: ...
    @winrt_classmethod
    def DisableShowingMainViewOnActivation(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics) -> Void: ...
    @winrt_classmethod
    def TryShowAsStandaloneAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def TryShowAsStandaloneWithSizePreferenceAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32, sizePreference: Windows.UI.ViewManagement.ViewSizePreference) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def TryShowAsStandaloneWithAnchorViewAndSizePreferenceAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32, sizePreference: Windows.UI.ViewManagement.ViewSizePreference, anchorViewId: Int32, anchorSizePreference: Windows.UI.ViewManagement.ViewSizePreference) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def SwitchAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SwitchFromViewAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, toViewId: Int32, fromViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SwitchFromViewWithOptionsAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, toViewId: Int32, fromViewId: Int32, options: Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def PrepareForCustomAnimatedSwitchAsync(cls: Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, toViewId: Int32, fromViewId: Int32, options: Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
ApplicationViewSwitchingOptions = UInt32
ApplicationViewSwitchingOptions_Default: ApplicationViewSwitchingOptions = 0
ApplicationViewSwitchingOptions_SkipAnimation: ApplicationViewSwitchingOptions = 1
ApplicationViewSwitchingOptions_ConsolidateViews: ApplicationViewSwitchingOptions = 2
class ApplicationViewTitleBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IApplicationViewTitleBar
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewTitleBar'
    @winrt_mixinmethod
    def put_ForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonHoverForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonHoverForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonHoverBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonHoverBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonPressedForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonPressedForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonPressedBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonPressedBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_InactiveForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_InactiveForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_InactiveBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_InactiveBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonInactiveForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonInactiveForegroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonInactiveBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonInactiveBackgroundColor(self: Windows.UI.ViewManagement.IApplicationViewTitleBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ButtonForegroundColor = property(get_ButtonForegroundColor, put_ButtonForegroundColor)
    ButtonBackgroundColor = property(get_ButtonBackgroundColor, put_ButtonBackgroundColor)
    ButtonHoverForegroundColor = property(get_ButtonHoverForegroundColor, put_ButtonHoverForegroundColor)
    ButtonHoverBackgroundColor = property(get_ButtonHoverBackgroundColor, put_ButtonHoverBackgroundColor)
    ButtonPressedForegroundColor = property(get_ButtonPressedForegroundColor, put_ButtonPressedForegroundColor)
    ButtonPressedBackgroundColor = property(get_ButtonPressedBackgroundColor, put_ButtonPressedBackgroundColor)
    InactiveForegroundColor = property(get_InactiveForegroundColor, put_InactiveForegroundColor)
    InactiveBackgroundColor = property(get_InactiveBackgroundColor, put_InactiveBackgroundColor)
    ButtonInactiveForegroundColor = property(get_ButtonInactiveForegroundColor, put_ButtonInactiveForegroundColor)
    ButtonInactiveBackgroundColor = property(get_ButtonInactiveBackgroundColor, put_ButtonInactiveBackgroundColor)
class _ApplicationViewTransferContext_Meta_(ComPtr.__class__):
    pass
class ApplicationViewTransferContext(ComPtr, metaclass=_ApplicationViewTransferContext_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IApplicationViewTransferContext
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewTransferContext'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.ViewManagement.ApplicationViewTransferContext: ...
    @winrt_mixinmethod
    def get_ViewId(self: Windows.UI.ViewManagement.IApplicationViewTransferContext) -> Int32: ...
    @winrt_mixinmethod
    def put_ViewId(self: Windows.UI.ViewManagement.IApplicationViewTransferContext, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_DataPackageFormatId(cls: Windows.UI.ViewManagement.IApplicationViewTransferContextStatics) -> WinRT_String: ...
    ViewId = property(get_ViewId, put_ViewId)
    _ApplicationViewTransferContext_Meta_.DataPackageFormatId = property(get_DataPackageFormatId.__wrapped__, None)
ApplicationViewWindowingMode = Int32
ApplicationViewWindowingMode_Auto: ApplicationViewWindowingMode = 0
ApplicationViewWindowingMode_PreferredLaunchViewSize: ApplicationViewWindowingMode = 1
ApplicationViewWindowingMode_FullScreen: ApplicationViewWindowingMode = 2
ApplicationViewWindowingMode_CompactOverlay: ApplicationViewWindowingMode = 3
ApplicationViewWindowingMode_Maximized: ApplicationViewWindowingMode = 4
FullScreenSystemOverlayMode = Int32
FullScreenSystemOverlayMode_Standard: FullScreenSystemOverlayMode = 0
FullScreenSystemOverlayMode_Minimal: FullScreenSystemOverlayMode = 1
HandPreference = Int32
HandPreference_LeftHanded: HandPreference = 0
HandPreference_RightHanded: HandPreference = 1
class IAccessibilitySettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IAccessibilitySettings'
    _iid_ = Guid('{fe0e8147-c4c0-4562-b962-1327b52ad5b9}')
    @winrt_commethod(6)
    def get_HighContrast(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HighContrastScheme(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_HighContrastChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.AccessibilitySettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HighContrastChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    HighContrast = property(get_HighContrast, None)
    HighContrastScheme = property(get_HighContrastScheme, None)
class IActivationViewSwitcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IActivationViewSwitcher'
    _iid_ = Guid('{dca71bb6-7350-492b-aac7-c8a13d7224ad}')
    @winrt_commethod(6)
    def ShowAsStandaloneAsync(self, viewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ShowAsStandaloneWithSizePreferenceAsync(self, viewId: Int32, sizePreference: Windows.UI.ViewManagement.ViewSizePreference) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def IsViewPresentedOnActivationVirtualDesktop(self, viewId: Int32) -> Boolean: ...
class IApplicationView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView'
    _iid_ = Guid('{d222d519-4361-451e-96c4-60f4f9742db0}')
    @winrt_commethod(6)
    def get_Orientation(self) -> Windows.UI.ViewManagement.ApplicationViewOrientation: ...
    @winrt_commethod(7)
    def get_AdjacentToLeftDisplayEdge(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_AdjacentToRightDisplayEdge(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsFullScreen(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsOnLockScreen(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsScreenCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_IsScreenCaptureEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Id(self) -> Int32: ...
    @winrt_commethod(16)
    def add_Consolidated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.ApplicationView, Windows.UI.ViewManagement.ApplicationViewConsolidatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_Consolidated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Orientation = property(get_Orientation, None)
    AdjacentToLeftDisplayEdge = property(get_AdjacentToLeftDisplayEdge, None)
    AdjacentToRightDisplayEdge = property(get_AdjacentToRightDisplayEdge, None)
    IsFullScreen = property(get_IsFullScreen, None)
    IsOnLockScreen = property(get_IsOnLockScreen, None)
    IsScreenCaptureEnabled = property(get_IsScreenCaptureEnabled, put_IsScreenCaptureEnabled)
    Title = property(get_Title, put_Title)
    Id = property(get_Id, None)
class IApplicationView2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView2'
    _iid_ = Guid('{e876b196-a545-40dc-b594-450cba68cc00}')
    @winrt_commethod(6)
    def get_SuppressSystemOverlays(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SuppressSystemOverlays(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_VisibleBounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def add_VisibleBoundsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.ApplicationView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_VisibleBoundsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def SetDesiredBoundsMode(self, boundsMode: Windows.UI.ViewManagement.ApplicationViewBoundsMode) -> Boolean: ...
    @winrt_commethod(12)
    def get_DesiredBoundsMode(self) -> Windows.UI.ViewManagement.ApplicationViewBoundsMode: ...
    SuppressSystemOverlays = property(get_SuppressSystemOverlays, put_SuppressSystemOverlays)
    VisibleBounds = property(get_VisibleBounds, None)
    DesiredBoundsMode = property(get_DesiredBoundsMode, None)
class IApplicationView3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView3'
    _iid_ = Guid('{903c9ce5-793a-4fdf-a2b2-af1ac21e3108}')
    @winrt_commethod(6)
    def get_TitleBar(self) -> Windows.UI.ViewManagement.ApplicationViewTitleBar: ...
    @winrt_commethod(7)
    def get_FullScreenSystemOverlayMode(self) -> Windows.UI.ViewManagement.FullScreenSystemOverlayMode: ...
    @winrt_commethod(8)
    def put_FullScreenSystemOverlayMode(self, value: Windows.UI.ViewManagement.FullScreenSystemOverlayMode) -> Void: ...
    @winrt_commethod(9)
    def get_IsFullScreenMode(self) -> Boolean: ...
    @winrt_commethod(10)
    def TryEnterFullScreenMode(self) -> Boolean: ...
    @winrt_commethod(11)
    def ExitFullScreenMode(self) -> Void: ...
    @winrt_commethod(12)
    def ShowStandardSystemOverlays(self) -> Void: ...
    @winrt_commethod(13)
    def TryResizeView(self, value: Windows.Foundation.Size) -> Boolean: ...
    @winrt_commethod(14)
    def SetPreferredMinSize(self, minSize: Windows.Foundation.Size) -> Void: ...
    TitleBar = property(get_TitleBar, None)
    FullScreenSystemOverlayMode = property(get_FullScreenSystemOverlayMode, put_FullScreenSystemOverlayMode)
    IsFullScreenMode = property(get_IsFullScreenMode, None)
class IApplicationView4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView4'
    _iid_ = Guid('{15e5cbec-9e0f-46b5-bc3f-9bf653e74b5e}')
    @winrt_commethod(6)
    def get_ViewMode(self) -> Windows.UI.ViewManagement.ApplicationViewMode: ...
    @winrt_commethod(7)
    def IsViewModeSupported(self, viewMode: Windows.UI.ViewManagement.ApplicationViewMode) -> Boolean: ...
    @winrt_commethod(8)
    def TryEnterViewModeAsync(self, viewMode: Windows.UI.ViewManagement.ApplicationViewMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def TryEnterViewModeWithPreferencesAsync(self, viewMode: Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: Windows.UI.ViewManagement.ViewModePreferences) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def TryConsolidateAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    ViewMode = property(get_ViewMode, None)
class IApplicationView7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView7'
    _iid_ = Guid('{a0369647-5faf-5aa6-9c38-befbb12a071e}')
    @winrt_commethod(6)
    def get_PersistedStateId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_PersistedStateId(self, value: WinRT_String) -> Void: ...
    PersistedStateId = property(get_PersistedStateId, put_PersistedStateId)
class IApplicationView9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView9'
    _iid_ = Guid('{9c6516f9-021a-5f01-93e5-9bdad2647574}')
    @winrt_commethod(6)
    def get_WindowingEnvironment(self) -> Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_commethod(7)
    def GetDisplayRegions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.WindowManagement.DisplayRegion]: ...
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class IApplicationViewConsolidatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs'
    _iid_ = Guid('{514449ec-7ea2-4de7-a6a6-7dfbaaebb6fb}')
    @winrt_commethod(6)
    def get_IsUserInitiated(self) -> Boolean: ...
    IsUserInitiated = property(get_IsUserInitiated, None)
class IApplicationViewConsolidatedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs2'
    _iid_ = Guid('{1c199ecc-6dc1-40f4-afee-07d9ea296430}')
    @winrt_commethod(6)
    def get_IsAppInitiated(self) -> Boolean: ...
    IsAppInitiated = property(get_IsAppInitiated, None)
class IApplicationViewFullscreenStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewFullscreenStatics'
    _iid_ = Guid('{bc792ebd-64fe-4b65-a0c0-901ce2b68636}')
    @winrt_commethod(6)
    def TryUnsnapToFullscreen(self) -> Boolean: ...
class IApplicationViewInteropStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewInteropStatics'
    _iid_ = Guid('{c446fb5d-4793-4896-a8e2-be57a8bb0f50}')
    @winrt_commethod(6)
    def GetApplicationViewIdForWindow(self, window: Windows.UI.Core.ICoreWindow) -> Int32: ...
class IApplicationViewScaling(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewScaling'
    _iid_ = Guid('{1d0ddc23-23f3-4b2d-84fe-74bf37b48b66}')
class IApplicationViewScalingStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewScalingStatics'
    _iid_ = Guid('{b08fecf0-b946-45c8-a5e3-71f5aa78f861}')
    @winrt_commethod(6)
    def get_DisableLayoutScaling(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetDisableLayoutScaling(self, disableLayoutScaling: Boolean) -> Boolean: ...
    DisableLayoutScaling = property(get_DisableLayoutScaling, None)
class IApplicationViewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics'
    _iid_ = Guid('{010a6306-c433-44e5-a9f2-bd84d4030a95}')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.UI.ViewManagement.ApplicationViewState: ...
    @winrt_commethod(7)
    def TryUnsnap(self) -> Boolean: ...
    Value = property(get_Value, None)
class IApplicationViewStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics2'
    _iid_ = Guid('{af338ae5-cf64-423c-85e5-f3e72448fb23}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.ViewManagement.ApplicationView: ...
    @winrt_commethod(7)
    def get_TerminateAppOnFinalViewClose(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_TerminateAppOnFinalViewClose(self, value: Boolean) -> Void: ...
    TerminateAppOnFinalViewClose = property(get_TerminateAppOnFinalViewClose, put_TerminateAppOnFinalViewClose)
class IApplicationViewStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics3'
    _iid_ = Guid('{a28d7594-8c41-4e13-9719-5164796fe4c7}')
    @winrt_commethod(6)
    def get_PreferredLaunchWindowingMode(self) -> Windows.UI.ViewManagement.ApplicationViewWindowingMode: ...
    @winrt_commethod(7)
    def put_PreferredLaunchWindowingMode(self, value: Windows.UI.ViewManagement.ApplicationViewWindowingMode) -> Void: ...
    @winrt_commethod(8)
    def get_PreferredLaunchViewSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_PreferredLaunchViewSize(self, value: Windows.Foundation.Size) -> Void: ...
    PreferredLaunchWindowingMode = property(get_PreferredLaunchWindowingMode, put_PreferredLaunchWindowingMode)
    PreferredLaunchViewSize = property(get_PreferredLaunchViewSize, put_PreferredLaunchViewSize)
class IApplicationViewStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics4'
    _iid_ = Guid('{08fd8d33-2611-5336-a315-d98e6366c9db}')
    @winrt_commethod(6)
    def ClearAllPersistedState(self) -> Void: ...
    @winrt_commethod(7)
    def ClearPersistedState(self, key: WinRT_String) -> Void: ...
class IApplicationViewSwitcherStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewSwitcherStatics'
    _iid_ = Guid('{975f2f1e-e656-4c5e-a0a1-717c6ffa7d64}')
    @winrt_commethod(6)
    def DisableShowingMainViewOnActivation(self) -> Void: ...
    @winrt_commethod(7)
    def TryShowAsStandaloneAsync(self, viewId: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryShowAsStandaloneWithSizePreferenceAsync(self, viewId: Int32, sizePreference: Windows.UI.ViewManagement.ViewSizePreference) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def TryShowAsStandaloneWithAnchorViewAndSizePreferenceAsync(self, viewId: Int32, sizePreference: Windows.UI.ViewManagement.ViewSizePreference, anchorViewId: Int32, anchorSizePreference: Windows.UI.ViewManagement.ViewSizePreference) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def SwitchAsync(self, viewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def SwitchFromViewAsync(self, toViewId: Int32, fromViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def SwitchFromViewWithOptionsAsync(self, toViewId: Int32, fromViewId: Int32, options: Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def PrepareForCustomAnimatedSwitchAsync(self, toViewId: Int32, fromViewId: Int32, options: Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IApplicationViewSwitcherStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewSwitcherStatics2'
    _iid_ = Guid('{60e995cd-4fc2-48c4-b8e3-395f2b9f0fc1}')
    @winrt_commethod(6)
    def DisableSystemViewActivationPolicy(self) -> Void: ...
class IApplicationViewSwitcherStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewSwitcherStatics3'
    _iid_ = Guid('{92059420-80a7-486d-b21f-c7a4a242a383}')
    @winrt_commethod(6)
    def TryShowAsViewModeAsync(self, viewId: Int32, viewMode: Windows.UI.ViewManagement.ApplicationViewMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TryShowAsViewModeWithPreferencesAsync(self, viewId: Int32, viewMode: Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: Windows.UI.ViewManagement.ViewModePreferences) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IApplicationViewTitleBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewTitleBar'
    _iid_ = Guid('{00924ac0-932b-4a6b-9c4b-dc38c82478ce}')
    @winrt_commethod(6)
    def put_ForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(7)
    def get_ForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(8)
    def put_BackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(9)
    def get_BackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(10)
    def put_ButtonForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(11)
    def get_ButtonForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(12)
    def put_ButtonBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(13)
    def get_ButtonBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(14)
    def put_ButtonHoverForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(15)
    def get_ButtonHoverForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(16)
    def put_ButtonHoverBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(17)
    def get_ButtonHoverBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(18)
    def put_ButtonPressedForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(19)
    def get_ButtonPressedForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(20)
    def put_ButtonPressedBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(21)
    def get_ButtonPressedBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(22)
    def put_InactiveForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(23)
    def get_InactiveForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(24)
    def put_InactiveBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(25)
    def get_InactiveBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(26)
    def put_ButtonInactiveForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(27)
    def get_ButtonInactiveForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(28)
    def put_ButtonInactiveBackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(29)
    def get_ButtonInactiveBackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ButtonForegroundColor = property(get_ButtonForegroundColor, put_ButtonForegroundColor)
    ButtonBackgroundColor = property(get_ButtonBackgroundColor, put_ButtonBackgroundColor)
    ButtonHoverForegroundColor = property(get_ButtonHoverForegroundColor, put_ButtonHoverForegroundColor)
    ButtonHoverBackgroundColor = property(get_ButtonHoverBackgroundColor, put_ButtonHoverBackgroundColor)
    ButtonPressedForegroundColor = property(get_ButtonPressedForegroundColor, put_ButtonPressedForegroundColor)
    ButtonPressedBackgroundColor = property(get_ButtonPressedBackgroundColor, put_ButtonPressedBackgroundColor)
    InactiveForegroundColor = property(get_InactiveForegroundColor, put_InactiveForegroundColor)
    InactiveBackgroundColor = property(get_InactiveBackgroundColor, put_InactiveBackgroundColor)
    ButtonInactiveForegroundColor = property(get_ButtonInactiveForegroundColor, put_ButtonInactiveForegroundColor)
    ButtonInactiveBackgroundColor = property(get_ButtonInactiveBackgroundColor, put_ButtonInactiveBackgroundColor)
class IApplicationViewTransferContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewTransferContext'
    _iid_ = Guid('{8574bc63-3c17-408e-9408-8a1a9ea81bfa}')
    @winrt_commethod(6)
    def get_ViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ViewId(self, value: Int32) -> Void: ...
    ViewId = property(get_ViewId, put_ViewId)
class IApplicationViewTransferContextStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewTransferContextStatics'
    _iid_ = Guid('{15a89d92-dd79-4b0b-bc47-d5f195f14661}')
    @winrt_commethod(6)
    def get_DataPackageFormatId(self) -> WinRT_String: ...
    DataPackageFormatId = property(get_DataPackageFormatId, None)
class IApplicationViewWithContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewWithContext'
    _iid_ = Guid('{bd55d512-9dc1-44fc-8501-666625df60dc}')
    @winrt_commethod(6)
    def get_UIContext(self) -> Windows.UI.UIContext: ...
    UIContext = property(get_UIContext, None)
class IInputPane(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPane'
    _iid_ = Guid('{640ada70-06f3-4c87-a678-9829c9127c28}')
    @winrt_commethod(6)
    def add_Showing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.InputPane, Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Showing(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Hiding(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.InputPane, Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Hiding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_OccludedRect(self) -> Windows.Foundation.Rect: ...
    OccludedRect = property(get_OccludedRect, None)
class IInputPane2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPane2'
    _iid_ = Guid('{8a6b3f26-7090-4793-944c-c3f2cde26276}')
    @winrt_commethod(6)
    def TryShow(self) -> Boolean: ...
    @winrt_commethod(7)
    def TryHide(self) -> Boolean: ...
class IInputPaneControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneControl'
    _iid_ = Guid('{088bb24f-962f-489d-aa6e-c6be1a0a6e52}')
    @winrt_commethod(6)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Visible(self, value: Boolean) -> Void: ...
    Visible = property(get_Visible, put_Visible)
class IInputPaneStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneStatics'
    _iid_ = Guid('{95f4af3a-ef47-424a-9741-fd2815eba2bd}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.ViewManagement.InputPane: ...
class IInputPaneStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneStatics2'
    _iid_ = Guid('{1b63529b-d9ec-4531-8445-71bab9fb828e}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: Windows.UI.UIContext) -> Windows.UI.ViewManagement.InputPane: ...
class IInputPaneVisibilityEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs'
    _iid_ = Guid('{d243e016-d907-4fcc-bb8d-f77baa5028f1}')
    @winrt_commethod(6)
    def get_OccludedRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_EnsuredFocusedElementInView(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_EnsuredFocusedElementInView(self) -> Boolean: ...
    OccludedRect = property(get_OccludedRect, None)
    EnsuredFocusedElementInView = property(get_EnsuredFocusedElementInView, put_EnsuredFocusedElementInView)
class IProjectionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IProjectionManagerStatics'
    _iid_ = Guid('{b65f913d-e2f0-4ffd-ba95-34241647e45c}')
    @winrt_commethod(6)
    def StartProjectingAsync(self, projectionViewId: Int32, anchorViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def SwapDisplaysForViewsAsync(self, projectionViewId: Int32, anchorViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def StopProjectingAsync(self, projectionViewId: Int32, anchorViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_ProjectionDisplayAvailable(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_ProjectionDisplayAvailableChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ProjectionDisplayAvailableChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProjectionDisplayAvailable = property(get_ProjectionDisplayAvailable, None)
class IProjectionManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IProjectionManagerStatics2'
    _iid_ = Guid('{f33d2f43-2749-4cde-b977-c0c41e7415d1}')
    @winrt_commethod(6)
    def StartProjectingWithDeviceInfoAsync(self, projectionViewId: Int32, anchorViewId: Int32, displayDeviceInfo: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RequestStartProjectingAsync(self, projectionViewId: Int32, anchorViewId: Int32, selection: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def RequestStartProjectingWithPlacementAsync(self, projectionViewId: Int32, anchorViewId: Int32, selection: Windows.Foundation.Rect, prefferedPlacement: Windows.UI.Popups.Placement) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IStatusBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IStatusBar'
    _iid_ = Guid('{0ffcc5bf-98d0-4864-b1e8-b3f4020be8b4}')
    @winrt_commethod(6)
    def ShowAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def HideAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_BackgroundOpacity(self) -> Double: ...
    @winrt_commethod(9)
    def put_BackgroundOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ForegroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(11)
    def put_ForegroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(13)
    def put_BackgroundColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(14)
    def get_ProgressIndicator(self) -> Windows.UI.ViewManagement.StatusBarProgressIndicator: ...
    @winrt_commethod(15)
    def get_OccludedRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(16)
    def add_Showing(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.StatusBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_Showing(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_Hiding(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.StatusBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_Hiding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    BackgroundOpacity = property(get_BackgroundOpacity, put_BackgroundOpacity)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ProgressIndicator = property(get_ProgressIndicator, None)
    OccludedRect = property(get_OccludedRect, None)
class IStatusBarProgressIndicator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IStatusBarProgressIndicator'
    _iid_ = Guid('{76cb2670-a3d7-49cf-8200-4f3eedca27bb}')
    @winrt_commethod(6)
    def ShowAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def HideAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ProgressValue(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def put_ProgressValue(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    Text = property(get_Text, put_Text)
    ProgressValue = property(get_ProgressValue, put_ProgressValue)
class IStatusBarStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IStatusBarStatics'
    _iid_ = Guid('{8b463fdf-422f-4561-8806-fb1289cadfb7}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.ViewManagement.StatusBar: ...
class IUISettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings'
    _iid_ = Guid('{85361600-1c63-4627-bcb1-3a89e0bc9c55}')
    @winrt_commethod(6)
    def get_HandPreference(self) -> Windows.UI.ViewManagement.HandPreference: ...
    @winrt_commethod(7)
    def get_CursorSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_ScrollBarSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def get_ScrollBarArrowSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def get_ScrollBarThumbBoxSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def get_MessageDuration(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_AnimationsEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_CaretBrowsingEnabled(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_CaretBlinkRate(self) -> UInt32: ...
    @winrt_commethod(15)
    def get_CaretWidth(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_DoubleClickTime(self) -> UInt32: ...
    @winrt_commethod(17)
    def get_MouseHoverTime(self) -> UInt32: ...
    @winrt_commethod(18)
    def UIElementColor(self, desiredElement: Windows.UI.ViewManagement.UIElementType) -> Windows.UI.Color: ...
    HandPreference = property(get_HandPreference, None)
    CursorSize = property(get_CursorSize, None)
    ScrollBarSize = property(get_ScrollBarSize, None)
    ScrollBarArrowSize = property(get_ScrollBarArrowSize, None)
    ScrollBarThumbBoxSize = property(get_ScrollBarThumbBoxSize, None)
    MessageDuration = property(get_MessageDuration, None)
    AnimationsEnabled = property(get_AnimationsEnabled, None)
    CaretBrowsingEnabled = property(get_CaretBrowsingEnabled, None)
    CaretBlinkRate = property(get_CaretBlinkRate, None)
    CaretWidth = property(get_CaretWidth, None)
    DoubleClickTime = property(get_DoubleClickTime, None)
    MouseHoverTime = property(get_MouseHoverTime, None)
class IUISettings2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings2'
    _iid_ = Guid('{bad82401-2721-44f9-bb91-2bb228be442f}')
    @winrt_commethod(6)
    def get_TextScaleFactor(self) -> Double: ...
    @winrt_commethod(7)
    def add_TextScaleFactorChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_TextScaleFactorChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    TextScaleFactor = property(get_TextScaleFactor, None)
class IUISettings3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings3'
    _iid_ = Guid('{03021be4-5254-4781-8194-5168f7d06d7b}')
    @winrt_commethod(6)
    def GetColorValue(self, desiredColor: Windows.UI.ViewManagement.UIColorType) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def add_ColorValuesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ColorValuesChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUISettings4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings4'
    _iid_ = Guid('{52bb3002-919b-4d6b-9b78-8dd66ff4b93b}')
    @winrt_commethod(6)
    def get_AdvancedEffectsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_AdvancedEffectsEnabledChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AdvancedEffectsEnabledChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdvancedEffectsEnabled = property(get_AdvancedEffectsEnabled, None)
class IUISettings5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings5'
    _iid_ = Guid('{5349d588-0cb5-5f05-bd34-706b3231f0bd}')
    @winrt_commethod(6)
    def get_AutoHideScrollBars(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_AutoHideScrollBarsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.UI.ViewManagement.UISettingsAutoHideScrollBarsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AutoHideScrollBarsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoHideScrollBars = property(get_AutoHideScrollBars, None)
class IUISettings6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings6'
    _iid_ = Guid('{aef19bd7-fe31-5a04-ada4-469aaec6dfa9}')
    @winrt_commethod(6)
    def add_AnimationsEnabledChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.UI.ViewManagement.UISettingsAnimationsEnabledChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AnimationsEnabledChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_MessageDurationChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.UI.ViewManagement.UISettingsMessageDurationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageDurationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUISettingsAnimationsEnabledChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettingsAnimationsEnabledChangedEventArgs'
    _iid_ = Guid('{0c7b4b3d-2ea1-533e-894d-415bc5243c29}')
class IUISettingsAutoHideScrollBarsChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettingsAutoHideScrollBarsChangedEventArgs'
    _iid_ = Guid('{87afd4b2-9146-5f02-8f6b-06d454174c0f}')
class IUISettingsMessageDurationChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettingsMessageDurationChangedEventArgs'
    _iid_ = Guid('{338aad52-4a5d-5b59-8002-d930f608fd6e}')
class IUIViewSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUIViewSettings'
    _iid_ = Guid('{c63657f6-8850-470d-88f8-455e16ea2c26}')
    @winrt_commethod(6)
    def get_UserInteractionMode(self) -> Windows.UI.ViewManagement.UserInteractionMode: ...
    UserInteractionMode = property(get_UserInteractionMode, None)
class IUIViewSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUIViewSettingsStatics'
    _iid_ = Guid('{595c97a5-f8f6-41cf-b0fb-aacdb81fd5f6}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.ViewManagement.UIViewSettings: ...
class IViewModePreferences(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IViewModePreferences'
    _iid_ = Guid('{878fcd3a-0b99-42c9-84d0-d3f1d403554b}')
    @winrt_commethod(6)
    def get_ViewSizePreference(self) -> Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_commethod(7)
    def put_ViewSizePreference(self, value: Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    @winrt_commethod(8)
    def get_CustomSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_CustomSize(self, value: Windows.Foundation.Size) -> Void: ...
    ViewSizePreference = property(get_ViewSizePreference, put_ViewSizePreference)
    CustomSize = property(get_CustomSize, put_CustomSize)
class IViewModePreferencesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IViewModePreferencesStatics'
    _iid_ = Guid('{69b60a65-5de5-40d8-8306-3833df7a2274}')
    @winrt_commethod(6)
    def CreateDefault(self, mode: Windows.UI.ViewManagement.ApplicationViewMode) -> Windows.UI.ViewManagement.ViewModePreferences: ...
class InputPane(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IInputPane
    _classid_ = 'Windows.UI.ViewManagement.InputPane'
    @winrt_mixinmethod
    def add_Showing(self: Windows.UI.ViewManagement.IInputPane, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.InputPane, Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Showing(self: Windows.UI.ViewManagement.IInputPane, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Hiding(self: Windows.UI.ViewManagement.IInputPane, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.InputPane, Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Hiding(self: Windows.UI.ViewManagement.IInputPane, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OccludedRect(self: Windows.UI.ViewManagement.IInputPane) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def TryShow(self: Windows.UI.ViewManagement.IInputPane2) -> Boolean: ...
    @winrt_mixinmethod
    def TryHide(self: Windows.UI.ViewManagement.IInputPane2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Visible(self: Windows.UI.ViewManagement.IInputPaneControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Visible(self: Windows.UI.ViewManagement.IInputPaneControl, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: Windows.UI.ViewManagement.IInputPaneStatics2, context: Windows.UI.UIContext) -> Windows.UI.ViewManagement.InputPane: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.ViewManagement.IInputPaneStatics) -> Windows.UI.ViewManagement.InputPane: ...
    OccludedRect = property(get_OccludedRect, None)
    Visible = property(get_Visible, put_Visible)
class InputPaneVisibilityEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs
    _classid_ = 'Windows.UI.ViewManagement.InputPaneVisibilityEventArgs'
    @winrt_mixinmethod
    def get_OccludedRect(self: Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_EnsuredFocusedElementInView(self: Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_EnsuredFocusedElementInView(self: Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs) -> Boolean: ...
    OccludedRect = property(get_OccludedRect, None)
    EnsuredFocusedElementInView = property(get_EnsuredFocusedElementInView, put_EnsuredFocusedElementInView)
class _ProjectionManager_Meta_(ComPtr.__class__):
    pass
class ProjectionManager(ComPtr, metaclass=_ProjectionManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.ProjectionManager'
    @winrt_classmethod
    def StartProjectingWithDeviceInfoAsync(cls: Windows.UI.ViewManagement.IProjectionManagerStatics2, projectionViewId: Int32, anchorViewId: Int32, displayDeviceInfo: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RequestStartProjectingAsync(cls: Windows.UI.ViewManagement.IProjectionManagerStatics2, projectionViewId: Int32, anchorViewId: Int32, selection: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RequestStartProjectingWithPlacementAsync(cls: Windows.UI.ViewManagement.IProjectionManagerStatics2, projectionViewId: Int32, anchorViewId: Int32, selection: Windows.Foundation.Rect, prefferedPlacement: Windows.UI.Popups.Placement) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.UI.ViewManagement.IProjectionManagerStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def StartProjectingAsync(cls: Windows.UI.ViewManagement.IProjectionManagerStatics, projectionViewId: Int32, anchorViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SwapDisplaysForViewsAsync(cls: Windows.UI.ViewManagement.IProjectionManagerStatics, projectionViewId: Int32, anchorViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def StopProjectingAsync(cls: Windows.UI.ViewManagement.IProjectionManagerStatics, projectionViewId: Int32, anchorViewId: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_ProjectionDisplayAvailable(cls: Windows.UI.ViewManagement.IProjectionManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def add_ProjectionDisplayAvailableChanged(cls: Windows.UI.ViewManagement.IProjectionManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProjectionDisplayAvailableChanged(cls: Windows.UI.ViewManagement.IProjectionManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    _ProjectionManager_Meta_.ProjectionDisplayAvailable = property(get_ProjectionDisplayAvailable.__wrapped__, None)
ScreenCaptureDisabledBehavior = Int32
ScreenCaptureDisabledBehavior_DrawAsBlack: ScreenCaptureDisabledBehavior = 0
ScreenCaptureDisabledBehavior_ExcludeFromCapture: ScreenCaptureDisabledBehavior = 1
class StatusBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IStatusBar
    _classid_ = 'Windows.UI.ViewManagement.StatusBar'
    @winrt_mixinmethod
    def ShowAsync(self: Windows.UI.ViewManagement.IStatusBar) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def HideAsync(self: Windows.UI.ViewManagement.IStatusBar) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_BackgroundOpacity(self: Windows.UI.ViewManagement.IStatusBar) -> Double: ...
    @winrt_mixinmethod
    def put_BackgroundOpacity(self: Windows.UI.ViewManagement.IStatusBar, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: Windows.UI.ViewManagement.IStatusBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: Windows.UI.ViewManagement.IStatusBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.UI.ViewManagement.IStatusBar) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.UI.ViewManagement.IStatusBar, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ProgressIndicator(self: Windows.UI.ViewManagement.IStatusBar) -> Windows.UI.ViewManagement.StatusBarProgressIndicator: ...
    @winrt_mixinmethod
    def get_OccludedRect(self: Windows.UI.ViewManagement.IStatusBar) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def add_Showing(self: Windows.UI.ViewManagement.IStatusBar, eventHandler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.StatusBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Showing(self: Windows.UI.ViewManagement.IStatusBar, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Hiding(self: Windows.UI.ViewManagement.IStatusBar, eventHandler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.StatusBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Hiding(self: Windows.UI.ViewManagement.IStatusBar, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.ViewManagement.IStatusBarStatics) -> Windows.UI.ViewManagement.StatusBar: ...
    BackgroundOpacity = property(get_BackgroundOpacity, put_BackgroundOpacity)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ProgressIndicator = property(get_ProgressIndicator, None)
    OccludedRect = property(get_OccludedRect, None)
class StatusBarProgressIndicator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IStatusBarProgressIndicator
    _classid_ = 'Windows.UI.ViewManagement.StatusBarProgressIndicator'
    @winrt_mixinmethod
    def ShowAsync(self: Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def HideAsync(self: Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.UI.ViewManagement.IStatusBarProgressIndicator, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProgressValue(self: Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_ProgressValue(self: Windows.UI.ViewManagement.IStatusBarProgressIndicator, value: Windows.Foundation.IReference[Double]) -> Void: ...
    Text = property(get_Text, put_Text)
    ProgressValue = property(get_ProgressValue, put_ProgressValue)
UIColorType = Int32
UIColorType_Background: UIColorType = 0
UIColorType_Foreground: UIColorType = 1
UIColorType_AccentDark3: UIColorType = 2
UIColorType_AccentDark2: UIColorType = 3
UIColorType_AccentDark1: UIColorType = 4
UIColorType_Accent: UIColorType = 5
UIColorType_AccentLight1: UIColorType = 6
UIColorType_AccentLight2: UIColorType = 7
UIColorType_AccentLight3: UIColorType = 8
UIColorType_Complement: UIColorType = 9
UIElementType = Int32
UIElementType_ActiveCaption: UIElementType = 0
UIElementType_Background: UIElementType = 1
UIElementType_ButtonFace: UIElementType = 2
UIElementType_ButtonText: UIElementType = 3
UIElementType_CaptionText: UIElementType = 4
UIElementType_GrayText: UIElementType = 5
UIElementType_Highlight: UIElementType = 6
UIElementType_HighlightText: UIElementType = 7
UIElementType_Hotlight: UIElementType = 8
UIElementType_InactiveCaption: UIElementType = 9
UIElementType_InactiveCaptionText: UIElementType = 10
UIElementType_Window: UIElementType = 11
UIElementType_WindowText: UIElementType = 12
UIElementType_AccentColor: UIElementType = 1000
UIElementType_TextHigh: UIElementType = 1001
UIElementType_TextMedium: UIElementType = 1002
UIElementType_TextLow: UIElementType = 1003
UIElementType_TextContrastWithHigh: UIElementType = 1004
UIElementType_NonTextHigh: UIElementType = 1005
UIElementType_NonTextMediumHigh: UIElementType = 1006
UIElementType_NonTextMedium: UIElementType = 1007
UIElementType_NonTextMediumLow: UIElementType = 1008
UIElementType_NonTextLow: UIElementType = 1009
UIElementType_PageBackground: UIElementType = 1010
UIElementType_PopupBackground: UIElementType = 1011
UIElementType_OverlayOutsidePopup: UIElementType = 1012
class UISettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IUISettings
    _classid_ = 'Windows.UI.ViewManagement.UISettings'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.ViewManagement.UISettings: ...
    @winrt_mixinmethod
    def get_HandPreference(self: Windows.UI.ViewManagement.IUISettings) -> Windows.UI.ViewManagement.HandPreference: ...
    @winrt_mixinmethod
    def get_CursorSize(self: Windows.UI.ViewManagement.IUISettings) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ScrollBarSize(self: Windows.UI.ViewManagement.IUISettings) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ScrollBarArrowSize(self: Windows.UI.ViewManagement.IUISettings) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ScrollBarThumbBoxSize(self: Windows.UI.ViewManagement.IUISettings) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_MessageDuration(self: Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_AnimationsEnabled(self: Windows.UI.ViewManagement.IUISettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_CaretBrowsingEnabled(self: Windows.UI.ViewManagement.IUISettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_CaretBlinkRate(self: Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_CaretWidth(self: Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_DoubleClickTime(self: Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_MouseHoverTime(self: Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def UIElementColor(self: Windows.UI.ViewManagement.IUISettings, desiredElement: Windows.UI.ViewManagement.UIElementType) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_TextScaleFactor(self: Windows.UI.ViewManagement.IUISettings2) -> Double: ...
    @winrt_mixinmethod
    def add_TextScaleFactorChanged(self: Windows.UI.ViewManagement.IUISettings2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextScaleFactorChanged(self: Windows.UI.ViewManagement.IUISettings2, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetColorValue(self: Windows.UI.ViewManagement.IUISettings3, desiredColor: Windows.UI.ViewManagement.UIColorType) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def add_ColorValuesChanged(self: Windows.UI.ViewManagement.IUISettings3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ColorValuesChanged(self: Windows.UI.ViewManagement.IUISettings3, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AdvancedEffectsEnabled(self: Windows.UI.ViewManagement.IUISettings4) -> Boolean: ...
    @winrt_mixinmethod
    def add_AdvancedEffectsEnabledChanged(self: Windows.UI.ViewManagement.IUISettings4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvancedEffectsEnabledChanged(self: Windows.UI.ViewManagement.IUISettings4, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AutoHideScrollBars(self: Windows.UI.ViewManagement.IUISettings5) -> Boolean: ...
    @winrt_mixinmethod
    def add_AutoHideScrollBarsChanged(self: Windows.UI.ViewManagement.IUISettings5, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.UI.ViewManagement.UISettingsAutoHideScrollBarsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AutoHideScrollBarsChanged(self: Windows.UI.ViewManagement.IUISettings5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AnimationsEnabledChanged(self: Windows.UI.ViewManagement.IUISettings6, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.UI.ViewManagement.UISettingsAnimationsEnabledChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AnimationsEnabledChanged(self: Windows.UI.ViewManagement.IUISettings6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MessageDurationChanged(self: Windows.UI.ViewManagement.IUISettings6, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.UISettings, Windows.UI.ViewManagement.UISettingsMessageDurationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageDurationChanged(self: Windows.UI.ViewManagement.IUISettings6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    HandPreference = property(get_HandPreference, None)
    CursorSize = property(get_CursorSize, None)
    ScrollBarSize = property(get_ScrollBarSize, None)
    ScrollBarArrowSize = property(get_ScrollBarArrowSize, None)
    ScrollBarThumbBoxSize = property(get_ScrollBarThumbBoxSize, None)
    MessageDuration = property(get_MessageDuration, None)
    AnimationsEnabled = property(get_AnimationsEnabled, None)
    CaretBrowsingEnabled = property(get_CaretBrowsingEnabled, None)
    CaretBlinkRate = property(get_CaretBlinkRate, None)
    CaretWidth = property(get_CaretWidth, None)
    DoubleClickTime = property(get_DoubleClickTime, None)
    MouseHoverTime = property(get_MouseHoverTime, None)
    TextScaleFactor = property(get_TextScaleFactor, None)
    AdvancedEffectsEnabled = property(get_AdvancedEffectsEnabled, None)
    AutoHideScrollBars = property(get_AutoHideScrollBars, None)
class UISettingsAnimationsEnabledChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IUISettingsAnimationsEnabledChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.UISettingsAnimationsEnabledChangedEventArgs'
class UISettingsAutoHideScrollBarsChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IUISettingsAutoHideScrollBarsChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.UISettingsAutoHideScrollBarsChangedEventArgs'
class UISettingsMessageDurationChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IUISettingsMessageDurationChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.UISettingsMessageDurationChangedEventArgs'
class UIViewSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IUIViewSettings
    _classid_ = 'Windows.UI.ViewManagement.UIViewSettings'
    @winrt_mixinmethod
    def get_UserInteractionMode(self: Windows.UI.ViewManagement.IUIViewSettings) -> Windows.UI.ViewManagement.UserInteractionMode: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.ViewManagement.IUIViewSettingsStatics) -> Windows.UI.ViewManagement.UIViewSettings: ...
    UserInteractionMode = property(get_UserInteractionMode, None)
UserInteractionMode = Int32
UserInteractionMode_Mouse: UserInteractionMode = 0
UserInteractionMode_Touch: UserInteractionMode = 1
ViewManagementViewScalingContract: UInt32 = 65536
class ViewModePreferences(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.ViewManagement.IViewModePreferences
    _classid_ = 'Windows.UI.ViewManagement.ViewModePreferences'
    @winrt_mixinmethod
    def get_ViewSizePreference(self: Windows.UI.ViewManagement.IViewModePreferences) -> Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_mixinmethod
    def put_ViewSizePreference(self: Windows.UI.ViewManagement.IViewModePreferences, value: Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    @winrt_mixinmethod
    def get_CustomSize(self: Windows.UI.ViewManagement.IViewModePreferences) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CustomSize(self: Windows.UI.ViewManagement.IViewModePreferences, value: Windows.Foundation.Size) -> Void: ...
    @winrt_classmethod
    def CreateDefault(cls: Windows.UI.ViewManagement.IViewModePreferencesStatics, mode: Windows.UI.ViewManagement.ApplicationViewMode) -> Windows.UI.ViewManagement.ViewModePreferences: ...
    ViewSizePreference = property(get_ViewSizePreference, put_ViewSizePreference)
    CustomSize = property(get_CustomSize, put_CustomSize)
ViewSizePreference = Int32
ViewSizePreference_Default: ViewSizePreference = 0
ViewSizePreference_UseLess: ViewSizePreference = 1
ViewSizePreference_UseHalf: ViewSizePreference = 2
ViewSizePreference_UseMore: ViewSizePreference = 3
ViewSizePreference_UseMinimum: ViewSizePreference = 4
ViewSizePreference_UseNone: ViewSizePreference = 5
ViewSizePreference_Custom: ViewSizePreference = 6
make_head(_module, 'AccessibilitySettings')
make_head(_module, 'ActivationViewSwitcher')
make_head(_module, 'ApplicationView')
make_head(_module, 'ApplicationViewConsolidatedEventArgs')
make_head(_module, 'ApplicationViewScaling')
make_head(_module, 'ApplicationViewSwitcher')
make_head(_module, 'ApplicationViewTitleBar')
make_head(_module, 'ApplicationViewTransferContext')
make_head(_module, 'IAccessibilitySettings')
make_head(_module, 'IActivationViewSwitcher')
make_head(_module, 'IApplicationView')
make_head(_module, 'IApplicationView2')
make_head(_module, 'IApplicationView3')
make_head(_module, 'IApplicationView4')
make_head(_module, 'IApplicationView7')
make_head(_module, 'IApplicationView9')
make_head(_module, 'IApplicationViewConsolidatedEventArgs')
make_head(_module, 'IApplicationViewConsolidatedEventArgs2')
make_head(_module, 'IApplicationViewFullscreenStatics')
make_head(_module, 'IApplicationViewInteropStatics')
make_head(_module, 'IApplicationViewScaling')
make_head(_module, 'IApplicationViewScalingStatics')
make_head(_module, 'IApplicationViewStatics')
make_head(_module, 'IApplicationViewStatics2')
make_head(_module, 'IApplicationViewStatics3')
make_head(_module, 'IApplicationViewStatics4')
make_head(_module, 'IApplicationViewSwitcherStatics')
make_head(_module, 'IApplicationViewSwitcherStatics2')
make_head(_module, 'IApplicationViewSwitcherStatics3')
make_head(_module, 'IApplicationViewTitleBar')
make_head(_module, 'IApplicationViewTransferContext')
make_head(_module, 'IApplicationViewTransferContextStatics')
make_head(_module, 'IApplicationViewWithContext')
make_head(_module, 'IInputPane')
make_head(_module, 'IInputPane2')
make_head(_module, 'IInputPaneControl')
make_head(_module, 'IInputPaneStatics')
make_head(_module, 'IInputPaneStatics2')
make_head(_module, 'IInputPaneVisibilityEventArgs')
make_head(_module, 'IProjectionManagerStatics')
make_head(_module, 'IProjectionManagerStatics2')
make_head(_module, 'IStatusBar')
make_head(_module, 'IStatusBarProgressIndicator')
make_head(_module, 'IStatusBarStatics')
make_head(_module, 'IUISettings')
make_head(_module, 'IUISettings2')
make_head(_module, 'IUISettings3')
make_head(_module, 'IUISettings4')
make_head(_module, 'IUISettings5')
make_head(_module, 'IUISettings6')
make_head(_module, 'IUISettingsAnimationsEnabledChangedEventArgs')
make_head(_module, 'IUISettingsAutoHideScrollBarsChangedEventArgs')
make_head(_module, 'IUISettingsMessageDurationChangedEventArgs')
make_head(_module, 'IUIViewSettings')
make_head(_module, 'IUIViewSettingsStatics')
make_head(_module, 'IViewModePreferences')
make_head(_module, 'IViewModePreferencesStatics')
make_head(_module, 'InputPane')
make_head(_module, 'InputPaneVisibilityEventArgs')
make_head(_module, 'ProjectionManager')
make_head(_module, 'StatusBar')
make_head(_module, 'StatusBarProgressIndicator')
make_head(_module, 'UISettings')
make_head(_module, 'UISettingsAnimationsEnabledChangedEventArgs')
make_head(_module, 'UISettingsAutoHideScrollBarsChangedEventArgs')
make_head(_module, 'UISettingsMessageDurationChangedEventArgs')
make_head(_module, 'UIViewSettings')
make_head(_module, 'ViewModePreferences')
