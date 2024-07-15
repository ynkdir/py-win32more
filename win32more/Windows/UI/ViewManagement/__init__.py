from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI
import win32more.Windows.UI.Core
import win32more.Windows.UI.Popups
import win32more.Windows.UI.ViewManagement
import win32more.Windows.UI.WindowManagement
import win32more.Windows.Win32.System.WinRT
class AccessibilitySettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IAccessibilitySettings
    _classid_ = 'Windows.UI.ViewManagement.AccessibilitySettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.ViewManagement.AccessibilitySettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.ViewManagement.AccessibilitySettings: ...
    @winrt_mixinmethod
    def get_HighContrast(self: win32more.Windows.UI.ViewManagement.IAccessibilitySettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HighContrastScheme(self: win32more.Windows.UI.ViewManagement.IAccessibilitySettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_HighContrastChanged(self: win32more.Windows.UI.ViewManagement.IAccessibilitySettings, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.AccessibilitySettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HighContrastChanged(self: win32more.Windows.UI.ViewManagement.IAccessibilitySettings, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    HighContrast = property(get_HighContrast, None)
    HighContrastScheme = property(get_HighContrastScheme, None)
    HighContrastChanged = event()
class ActivationViewSwitcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IActivationViewSwitcher
    _classid_ = 'Windows.UI.ViewManagement.ActivationViewSwitcher'
    @winrt_mixinmethod
    def ShowAsStandaloneAsync(self: win32more.Windows.UI.ViewManagement.IActivationViewSwitcher, viewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowAsStandaloneWithSizePreferenceAsync(self: win32more.Windows.UI.ViewManagement.IActivationViewSwitcher, viewId: Int32, sizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def IsViewPresentedOnActivationVirtualDesktop(self: win32more.Windows.UI.ViewManagement.IActivationViewSwitcher, viewId: Int32) -> Boolean: ...
class _ApplicationView_Meta_(ComPtr.__class__):
    pass
class ApplicationView(ComPtr, metaclass=_ApplicationView_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IApplicationView
    _classid_ = 'Windows.UI.ViewManagement.ApplicationView'
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> win32more.Windows.UI.ViewManagement.ApplicationViewOrientation: ...
    @winrt_mixinmethod
    def get_AdjacentToLeftDisplayEdge(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_AdjacentToRightDisplayEdge(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFullScreen(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOnLockScreen(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScreenCaptureEnabled(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScreenCaptureEnabled(self: win32more.Windows.UI.ViewManagement.IApplicationView, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.UI.ViewManagement.IApplicationView, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.ViewManagement.IApplicationView) -> Int32: ...
    @winrt_mixinmethod
    def add_Consolidated(self: win32more.Windows.UI.ViewManagement.IApplicationView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.ApplicationView, win32more.Windows.UI.ViewManagement.ApplicationViewConsolidatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Consolidated(self: win32more.Windows.UI.ViewManagement.IApplicationView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressSystemOverlays(self: win32more.Windows.UI.ViewManagement.IApplicationView2) -> Boolean: ...
    @winrt_mixinmethod
    def put_SuppressSystemOverlays(self: win32more.Windows.UI.ViewManagement.IApplicationView2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_VisibleBounds(self: win32more.Windows.UI.ViewManagement.IApplicationView2) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def add_VisibleBoundsChanged(self: win32more.Windows.UI.ViewManagement.IApplicationView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.ApplicationView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisibleBoundsChanged(self: win32more.Windows.UI.ViewManagement.IApplicationView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetDesiredBoundsMode(self: win32more.Windows.UI.ViewManagement.IApplicationView2, boundsMode: win32more.Windows.UI.ViewManagement.ApplicationViewBoundsMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_DesiredBoundsMode(self: win32more.Windows.UI.ViewManagement.IApplicationView2) -> win32more.Windows.UI.ViewManagement.ApplicationViewBoundsMode: ...
    @winrt_mixinmethod
    def get_TitleBar(self: win32more.Windows.UI.ViewManagement.IApplicationView3) -> win32more.Windows.UI.ViewManagement.ApplicationViewTitleBar: ...
    @winrt_mixinmethod
    def get_FullScreenSystemOverlayMode(self: win32more.Windows.UI.ViewManagement.IApplicationView3) -> win32more.Windows.UI.ViewManagement.FullScreenSystemOverlayMode: ...
    @winrt_mixinmethod
    def put_FullScreenSystemOverlayMode(self: win32more.Windows.UI.ViewManagement.IApplicationView3, value: win32more.Windows.UI.ViewManagement.FullScreenSystemOverlayMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsFullScreenMode(self: win32more.Windows.UI.ViewManagement.IApplicationView3) -> Boolean: ...
    @winrt_mixinmethod
    def TryEnterFullScreenMode(self: win32more.Windows.UI.ViewManagement.IApplicationView3) -> Boolean: ...
    @winrt_mixinmethod
    def ExitFullScreenMode(self: win32more.Windows.UI.ViewManagement.IApplicationView3) -> Void: ...
    @winrt_mixinmethod
    def ShowStandardSystemOverlays(self: win32more.Windows.UI.ViewManagement.IApplicationView3) -> Void: ...
    @winrt_mixinmethod
    def TryResizeView(self: win32more.Windows.UI.ViewManagement.IApplicationView3, value: win32more.Windows.Foundation.Size) -> Boolean: ...
    @winrt_mixinmethod
    def SetPreferredMinSize(self: win32more.Windows.UI.ViewManagement.IApplicationView3, minSize: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_ViewMode(self: win32more.Windows.UI.ViewManagement.IApplicationView4) -> win32more.Windows.UI.ViewManagement.ApplicationViewMode: ...
    @winrt_mixinmethod
    def IsViewModeSupported(self: win32more.Windows.UI.ViewManagement.IApplicationView4, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> Boolean: ...
    @winrt_mixinmethod
    def TryEnterViewModeAsync(self: win32more.Windows.UI.ViewManagement.IApplicationView4, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryEnterViewModeWithPreferencesAsync(self: win32more.Windows.UI.ViewManagement.IApplicationView4, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: win32more.Windows.UI.ViewManagement.ViewModePreferences) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryConsolidateAsync(self: win32more.Windows.UI.ViewManagement.IApplicationView4) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_PersistedStateId(self: win32more.Windows.UI.ViewManagement.IApplicationView7) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PersistedStateId(self: win32more.Windows.UI.ViewManagement.IApplicationView7, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WindowingEnvironment(self: win32more.Windows.UI.ViewManagement.IApplicationView9) -> win32more.Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_mixinmethod
    def GetDisplayRegions(self: win32more.Windows.UI.ViewManagement.IApplicationView9) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.WindowManagement.DisplayRegion]: ...
    @winrt_mixinmethod
    def get_UIContext(self: win32more.Windows.UI.ViewManagement.IApplicationViewWithContext) -> win32more.Windows.UI.UIContext: ...
    @winrt_classmethod
    def ClearAllPersistedState(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics4) -> Void: ...
    @winrt_classmethod
    def ClearPersistedState(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics4, key: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_PreferredLaunchWindowingMode(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics3) -> win32more.Windows.UI.ViewManagement.ApplicationViewWindowingMode: ...
    @winrt_classmethod
    def put_PreferredLaunchWindowingMode(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics3, value: win32more.Windows.UI.ViewManagement.ApplicationViewWindowingMode) -> Void: ...
    @winrt_classmethod
    def get_PreferredLaunchViewSize(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics3) -> win32more.Windows.Foundation.Size: ...
    @winrt_classmethod
    def put_PreferredLaunchViewSize(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics3, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_classmethod
    def TryUnsnapToFullscreen(cls: win32more.Windows.UI.ViewManagement.IApplicationViewFullscreenStatics) -> Boolean: ...
    @winrt_classmethod
    def GetApplicationViewIdForWindow(cls: win32more.Windows.UI.ViewManagement.IApplicationViewInteropStatics, window: win32more.Windows.UI.Core.ICoreWindow) -> Int32: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics2) -> win32more.Windows.UI.ViewManagement.ApplicationView: ...
    @winrt_classmethod
    def get_TerminateAppOnFinalViewClose(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics2) -> Boolean: ...
    @winrt_classmethod
    def put_TerminateAppOnFinalViewClose(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_Value(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics) -> win32more.Windows.UI.ViewManagement.ApplicationViewState: ...
    @winrt_classmethod
    def TryUnsnap(cls: win32more.Windows.UI.ViewManagement.IApplicationViewStatics) -> Boolean: ...
    AdjacentToLeftDisplayEdge = property(get_AdjacentToLeftDisplayEdge, None)
    AdjacentToRightDisplayEdge = property(get_AdjacentToRightDisplayEdge, None)
    DesiredBoundsMode = property(get_DesiredBoundsMode, None)
    FullScreenSystemOverlayMode = property(get_FullScreenSystemOverlayMode, put_FullScreenSystemOverlayMode)
    Id = property(get_Id, None)
    IsFullScreen = property(get_IsFullScreen, None)
    IsFullScreenMode = property(get_IsFullScreenMode, None)
    IsOnLockScreen = property(get_IsOnLockScreen, None)
    IsScreenCaptureEnabled = property(get_IsScreenCaptureEnabled, put_IsScreenCaptureEnabled)
    Orientation = property(get_Orientation, None)
    PersistedStateId = property(get_PersistedStateId, put_PersistedStateId)
    SuppressSystemOverlays = property(get_SuppressSystemOverlays, put_SuppressSystemOverlays)
    Title = property(get_Title, put_Title)
    TitleBar = property(get_TitleBar, None)
    UIContext = property(get_UIContext, None)
    ViewMode = property(get_ViewMode, None)
    VisibleBounds = property(get_VisibleBounds, None)
    WindowingEnvironment = property(get_WindowingEnvironment, None)
    _ApplicationView_Meta_.PreferredLaunchViewSize = property(get_PreferredLaunchViewSize, put_PreferredLaunchViewSize)
    _ApplicationView_Meta_.PreferredLaunchWindowingMode = property(get_PreferredLaunchWindowingMode, put_PreferredLaunchWindowingMode)
    _ApplicationView_Meta_.TerminateAppOnFinalViewClose = property(get_TerminateAppOnFinalViewClose, put_TerminateAppOnFinalViewClose)
    _ApplicationView_Meta_.Value = property(get_Value, None)
    Consolidated = event()
    VisibleBoundsChanged = event()
class ApplicationViewBoundsMode(Enum, Int32):
    UseVisible = 0
    UseCoreWindow = 1
class ApplicationViewConsolidatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewConsolidatedEventArgs'
    @winrt_mixinmethod
    def get_IsUserInitiated(self: win32more.Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAppInitiated(self: win32more.Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs2) -> Boolean: ...
    IsAppInitiated = property(get_IsAppInitiated, None)
    IsUserInitiated = property(get_IsUserInitiated, None)
class ApplicationViewMode(Enum, Int32):
    Default = 0
    CompactOverlay = 1
class ApplicationViewOrientation(Enum, Int32):
    Landscape = 0
    Portrait = 1
class _ApplicationViewScaling_Meta_(ComPtr.__class__):
    pass
class ApplicationViewScaling(ComPtr, metaclass=_ApplicationViewScaling_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IApplicationViewScaling
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewScaling'
    @winrt_classmethod
    def get_DisableLayoutScaling(cls: win32more.Windows.UI.ViewManagement.IApplicationViewScalingStatics) -> Boolean: ...
    @winrt_classmethod
    def TrySetDisableLayoutScaling(cls: win32more.Windows.UI.ViewManagement.IApplicationViewScalingStatics, disableLayoutScaling: Boolean) -> Boolean: ...
    _ApplicationViewScaling_Meta_.DisableLayoutScaling = property(get_DisableLayoutScaling, None)
class ApplicationViewState(Enum, Int32):
    FullScreenLandscape = 0
    Filled = 1
    Snapped = 2
    FullScreenPortrait = 3
class ApplicationViewSwitcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewSwitcher'
    @winrt_classmethod
    def TryShowAsViewModeAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics3, viewId: Int32, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def TryShowAsViewModeWithPreferencesAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics3, viewId: Int32, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: win32more.Windows.UI.ViewManagement.ViewModePreferences) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def DisableSystemViewActivationPolicy(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics2) -> Void: ...
    @winrt_classmethod
    def DisableShowingMainViewOnActivation(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics) -> Void: ...
    @winrt_classmethod
    def TryShowAsStandaloneAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def TryShowAsStandaloneWithSizePreferenceAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32, sizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def TryShowAsStandaloneWithAnchorViewAndSizePreferenceAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32, sizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference, anchorViewId: Int32, anchorSizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def SwitchAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, viewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SwitchFromViewAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, toViewId: Int32, fromViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SwitchFromViewWithOptionsAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, toViewId: Int32, fromViewId: Int32, options: win32more.Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def PrepareForCustomAnimatedSwitchAsync(cls: win32more.Windows.UI.ViewManagement.IApplicationViewSwitcherStatics, toViewId: Int32, fromViewId: Int32, options: win32more.Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ApplicationViewSwitchingOptions(Enum, UInt32):
    Default = 0
    SkipAnimation = 1
    ConsolidateViews = 2
class ApplicationViewTitleBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewTitleBar'
    @winrt_mixinmethod
    def put_ForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonHoverForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonHoverForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonHoverBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonHoverBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonPressedForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonPressedForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonPressedBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonPressedBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_InactiveForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_InactiveForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_InactiveBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_InactiveBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonInactiveForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonInactiveForegroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ButtonInactiveBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonInactiveBackgroundColor(self: win32more.Windows.UI.ViewManagement.IApplicationViewTitleBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ButtonBackgroundColor = property(get_ButtonBackgroundColor, put_ButtonBackgroundColor)
    ButtonForegroundColor = property(get_ButtonForegroundColor, put_ButtonForegroundColor)
    ButtonHoverBackgroundColor = property(get_ButtonHoverBackgroundColor, put_ButtonHoverBackgroundColor)
    ButtonHoverForegroundColor = property(get_ButtonHoverForegroundColor, put_ButtonHoverForegroundColor)
    ButtonInactiveBackgroundColor = property(get_ButtonInactiveBackgroundColor, put_ButtonInactiveBackgroundColor)
    ButtonInactiveForegroundColor = property(get_ButtonInactiveForegroundColor, put_ButtonInactiveForegroundColor)
    ButtonPressedBackgroundColor = property(get_ButtonPressedBackgroundColor, put_ButtonPressedBackgroundColor)
    ButtonPressedForegroundColor = property(get_ButtonPressedForegroundColor, put_ButtonPressedForegroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    InactiveBackgroundColor = property(get_InactiveBackgroundColor, put_InactiveBackgroundColor)
    InactiveForegroundColor = property(get_InactiveForegroundColor, put_InactiveForegroundColor)
class _ApplicationViewTransferContext_Meta_(ComPtr.__class__):
    pass
class ApplicationViewTransferContext(ComPtr, metaclass=_ApplicationViewTransferContext_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IApplicationViewTransferContext
    _classid_ = 'Windows.UI.ViewManagement.ApplicationViewTransferContext'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.ViewManagement.ApplicationViewTransferContext.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.ViewManagement.ApplicationViewTransferContext: ...
    @winrt_mixinmethod
    def get_ViewId(self: win32more.Windows.UI.ViewManagement.IApplicationViewTransferContext) -> Int32: ...
    @winrt_mixinmethod
    def put_ViewId(self: win32more.Windows.UI.ViewManagement.IApplicationViewTransferContext, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_DataPackageFormatId(cls: win32more.Windows.UI.ViewManagement.IApplicationViewTransferContextStatics) -> WinRT_String: ...
    ViewId = property(get_ViewId, put_ViewId)
    _ApplicationViewTransferContext_Meta_.DataPackageFormatId = property(get_DataPackageFormatId, None)
class ApplicationViewWindowingMode(Enum, Int32):
    Auto = 0
    PreferredLaunchViewSize = 1
    FullScreen = 2
    CompactOverlay = 3
    Maximized = 4
class FullScreenSystemOverlayMode(Enum, Int32):
    Standard = 0
    Minimal = 1
class HandPreference(Enum, Int32):
    LeftHanded = 0
    RightHanded = 1
class IAccessibilitySettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IAccessibilitySettings'
    _iid_ = Guid('{fe0e8147-c4c0-4562-b962-1327b52ad5b9}')
    @winrt_commethod(6)
    def get_HighContrast(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HighContrastScheme(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_HighContrastChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.AccessibilitySettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HighContrastChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    HighContrast = property(get_HighContrast, None)
    HighContrastScheme = property(get_HighContrastScheme, None)
    HighContrastChanged = event()
class IActivationViewSwitcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IActivationViewSwitcher'
    _iid_ = Guid('{dca71bb6-7350-492b-aac7-c8a13d7224ad}')
    @winrt_commethod(6)
    def ShowAsStandaloneAsync(self, viewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ShowAsStandaloneWithSizePreferenceAsync(self, viewId: Int32, sizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def IsViewPresentedOnActivationVirtualDesktop(self, viewId: Int32) -> Boolean: ...
class IApplicationView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView'
    _iid_ = Guid('{d222d519-4361-451e-96c4-60f4f9742db0}')
    @winrt_commethod(6)
    def get_Orientation(self) -> win32more.Windows.UI.ViewManagement.ApplicationViewOrientation: ...
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
    def add_Consolidated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.ApplicationView, win32more.Windows.UI.ViewManagement.ApplicationViewConsolidatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_Consolidated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdjacentToLeftDisplayEdge = property(get_AdjacentToLeftDisplayEdge, None)
    AdjacentToRightDisplayEdge = property(get_AdjacentToRightDisplayEdge, None)
    Id = property(get_Id, None)
    IsFullScreen = property(get_IsFullScreen, None)
    IsOnLockScreen = property(get_IsOnLockScreen, None)
    IsScreenCaptureEnabled = property(get_IsScreenCaptureEnabled, put_IsScreenCaptureEnabled)
    Orientation = property(get_Orientation, None)
    Title = property(get_Title, put_Title)
    Consolidated = event()
class IApplicationView2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView2'
    _iid_ = Guid('{e876b196-a545-40dc-b594-450cba68cc00}')
    @winrt_commethod(6)
    def get_SuppressSystemOverlays(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SuppressSystemOverlays(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_VisibleBounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def add_VisibleBoundsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.ApplicationView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_VisibleBoundsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def SetDesiredBoundsMode(self, boundsMode: win32more.Windows.UI.ViewManagement.ApplicationViewBoundsMode) -> Boolean: ...
    @winrt_commethod(12)
    def get_DesiredBoundsMode(self) -> win32more.Windows.UI.ViewManagement.ApplicationViewBoundsMode: ...
    DesiredBoundsMode = property(get_DesiredBoundsMode, None)
    SuppressSystemOverlays = property(get_SuppressSystemOverlays, put_SuppressSystemOverlays)
    VisibleBounds = property(get_VisibleBounds, None)
    VisibleBoundsChanged = event()
class IApplicationView3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView3'
    _iid_ = Guid('{903c9ce5-793a-4fdf-a2b2-af1ac21e3108}')
    @winrt_commethod(6)
    def get_TitleBar(self) -> win32more.Windows.UI.ViewManagement.ApplicationViewTitleBar: ...
    @winrt_commethod(7)
    def get_FullScreenSystemOverlayMode(self) -> win32more.Windows.UI.ViewManagement.FullScreenSystemOverlayMode: ...
    @winrt_commethod(8)
    def put_FullScreenSystemOverlayMode(self, value: win32more.Windows.UI.ViewManagement.FullScreenSystemOverlayMode) -> Void: ...
    @winrt_commethod(9)
    def get_IsFullScreenMode(self) -> Boolean: ...
    @winrt_commethod(10)
    def TryEnterFullScreenMode(self) -> Boolean: ...
    @winrt_commethod(11)
    def ExitFullScreenMode(self) -> Void: ...
    @winrt_commethod(12)
    def ShowStandardSystemOverlays(self) -> Void: ...
    @winrt_commethod(13)
    def TryResizeView(self, value: win32more.Windows.Foundation.Size) -> Boolean: ...
    @winrt_commethod(14)
    def SetPreferredMinSize(self, minSize: win32more.Windows.Foundation.Size) -> Void: ...
    FullScreenSystemOverlayMode = property(get_FullScreenSystemOverlayMode, put_FullScreenSystemOverlayMode)
    IsFullScreenMode = property(get_IsFullScreenMode, None)
    TitleBar = property(get_TitleBar, None)
class IApplicationView4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView4'
    _iid_ = Guid('{15e5cbec-9e0f-46b5-bc3f-9bf653e74b5e}')
    @winrt_commethod(6)
    def get_ViewMode(self) -> win32more.Windows.UI.ViewManagement.ApplicationViewMode: ...
    @winrt_commethod(7)
    def IsViewModeSupported(self, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> Boolean: ...
    @winrt_commethod(8)
    def TryEnterViewModeAsync(self, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def TryEnterViewModeWithPreferencesAsync(self, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: win32more.Windows.UI.ViewManagement.ViewModePreferences) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def TryConsolidateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    ViewMode = property(get_ViewMode, None)
class IApplicationView7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView7'
    _iid_ = Guid('{a0369647-5faf-5aa6-9c38-befbb12a071e}')
    @winrt_commethod(6)
    def get_PersistedStateId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_PersistedStateId(self, value: WinRT_String) -> Void: ...
    PersistedStateId = property(get_PersistedStateId, put_PersistedStateId)
class IApplicationView9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationView9'
    _iid_ = Guid('{9c6516f9-021a-5f01-93e5-9bdad2647574}')
    @winrt_commethod(6)
    def get_WindowingEnvironment(self) -> win32more.Windows.UI.WindowManagement.WindowingEnvironment: ...
    @winrt_commethod(7)
    def GetDisplayRegions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.WindowManagement.DisplayRegion]: ...
    WindowingEnvironment = property(get_WindowingEnvironment, None)
class IApplicationViewConsolidatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs'
    _iid_ = Guid('{514449ec-7ea2-4de7-a6a6-7dfbaaebb6fb}')
    @winrt_commethod(6)
    def get_IsUserInitiated(self) -> Boolean: ...
    IsUserInitiated = property(get_IsUserInitiated, None)
class IApplicationViewConsolidatedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewConsolidatedEventArgs2'
    _iid_ = Guid('{1c199ecc-6dc1-40f4-afee-07d9ea296430}')
    @winrt_commethod(6)
    def get_IsAppInitiated(self) -> Boolean: ...
    IsAppInitiated = property(get_IsAppInitiated, None)
class IApplicationViewFullscreenStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewFullscreenStatics'
    _iid_ = Guid('{bc792ebd-64fe-4b65-a0c0-901ce2b68636}')
    @winrt_commethod(6)
    def TryUnsnapToFullscreen(self) -> Boolean: ...
class IApplicationViewInteropStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewInteropStatics'
    _iid_ = Guid('{c446fb5d-4793-4896-a8e2-be57a8bb0f50}')
    @winrt_commethod(6)
    def GetApplicationViewIdForWindow(self, window: win32more.Windows.UI.Core.ICoreWindow) -> Int32: ...
class IApplicationViewScaling(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewScaling'
    _iid_ = Guid('{1d0ddc23-23f3-4b2d-84fe-74bf37b48b66}')
class IApplicationViewScalingStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewScalingStatics'
    _iid_ = Guid('{b08fecf0-b946-45c8-a5e3-71f5aa78f861}')
    @winrt_commethod(6)
    def get_DisableLayoutScaling(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetDisableLayoutScaling(self, disableLayoutScaling: Boolean) -> Boolean: ...
    DisableLayoutScaling = property(get_DisableLayoutScaling, None)
class IApplicationViewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics'
    _iid_ = Guid('{010a6306-c433-44e5-a9f2-bd84d4030a95}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.UI.ViewManagement.ApplicationViewState: ...
    @winrt_commethod(7)
    def TryUnsnap(self) -> Boolean: ...
    Value = property(get_Value, None)
class IApplicationViewStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics2'
    _iid_ = Guid('{af338ae5-cf64-423c-85e5-f3e72448fb23}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.ViewManagement.ApplicationView: ...
    @winrt_commethod(7)
    def get_TerminateAppOnFinalViewClose(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_TerminateAppOnFinalViewClose(self, value: Boolean) -> Void: ...
    TerminateAppOnFinalViewClose = property(get_TerminateAppOnFinalViewClose, put_TerminateAppOnFinalViewClose)
class IApplicationViewStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics3'
    _iid_ = Guid('{a28d7594-8c41-4e13-9719-5164796fe4c7}')
    @winrt_commethod(6)
    def get_PreferredLaunchWindowingMode(self) -> win32more.Windows.UI.ViewManagement.ApplicationViewWindowingMode: ...
    @winrt_commethod(7)
    def put_PreferredLaunchWindowingMode(self, value: win32more.Windows.UI.ViewManagement.ApplicationViewWindowingMode) -> Void: ...
    @winrt_commethod(8)
    def get_PreferredLaunchViewSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_PreferredLaunchViewSize(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    PreferredLaunchViewSize = property(get_PreferredLaunchViewSize, put_PreferredLaunchViewSize)
    PreferredLaunchWindowingMode = property(get_PreferredLaunchWindowingMode, put_PreferredLaunchWindowingMode)
class IApplicationViewStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewStatics4'
    _iid_ = Guid('{08fd8d33-2611-5336-a315-d98e6366c9db}')
    @winrt_commethod(6)
    def ClearAllPersistedState(self) -> Void: ...
    @winrt_commethod(7)
    def ClearPersistedState(self, key: WinRT_String) -> Void: ...
class IApplicationViewSwitcherStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewSwitcherStatics'
    _iid_ = Guid('{975f2f1e-e656-4c5e-a0a1-717c6ffa7d64}')
    @winrt_commethod(6)
    def DisableShowingMainViewOnActivation(self) -> Void: ...
    @winrt_commethod(7)
    def TryShowAsStandaloneAsync(self, viewId: Int32) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryShowAsStandaloneWithSizePreferenceAsync(self, viewId: Int32, sizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def TryShowAsStandaloneWithAnchorViewAndSizePreferenceAsync(self, viewId: Int32, sizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference, anchorViewId: Int32, anchorSizePreference: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def SwitchAsync(self, viewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def SwitchFromViewAsync(self, toViewId: Int32, fromViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def SwitchFromViewWithOptionsAsync(self, toViewId: Int32, fromViewId: Int32, options: win32more.Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def PrepareForCustomAnimatedSwitchAsync(self, toViewId: Int32, fromViewId: Int32, options: win32more.Windows.UI.ViewManagement.ApplicationViewSwitchingOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IApplicationViewSwitcherStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewSwitcherStatics2'
    _iid_ = Guid('{60e995cd-4fc2-48c4-b8e3-395f2b9f0fc1}')
    @winrt_commethod(6)
    def DisableSystemViewActivationPolicy(self) -> Void: ...
class IApplicationViewSwitcherStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewSwitcherStatics3'
    _iid_ = Guid('{92059420-80a7-486d-b21f-c7a4a242a383}')
    @winrt_commethod(6)
    def TryShowAsViewModeAsync(self, viewId: Int32, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TryShowAsViewModeWithPreferencesAsync(self, viewId: Int32, viewMode: win32more.Windows.UI.ViewManagement.ApplicationViewMode, viewModePreferences: win32more.Windows.UI.ViewManagement.ViewModePreferences) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IApplicationViewTitleBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewTitleBar'
    _iid_ = Guid('{00924ac0-932b-4a6b-9c4b-dc38c82478ce}')
    @winrt_commethod(6)
    def put_ForegroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(7)
    def get_ForegroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(8)
    def put_BackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(9)
    def get_BackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(10)
    def put_ButtonForegroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(11)
    def get_ButtonForegroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(12)
    def put_ButtonBackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(13)
    def get_ButtonBackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(14)
    def put_ButtonHoverForegroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(15)
    def get_ButtonHoverForegroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(16)
    def put_ButtonHoverBackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(17)
    def get_ButtonHoverBackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(18)
    def put_ButtonPressedForegroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(19)
    def get_ButtonPressedForegroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(20)
    def put_ButtonPressedBackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(21)
    def get_ButtonPressedBackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(22)
    def put_InactiveForegroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(23)
    def get_InactiveForegroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(24)
    def put_InactiveBackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(25)
    def get_InactiveBackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(26)
    def put_ButtonInactiveForegroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(27)
    def get_ButtonInactiveForegroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(28)
    def put_ButtonInactiveBackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(29)
    def get_ButtonInactiveBackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ButtonBackgroundColor = property(get_ButtonBackgroundColor, put_ButtonBackgroundColor)
    ButtonForegroundColor = property(get_ButtonForegroundColor, put_ButtonForegroundColor)
    ButtonHoverBackgroundColor = property(get_ButtonHoverBackgroundColor, put_ButtonHoverBackgroundColor)
    ButtonHoverForegroundColor = property(get_ButtonHoverForegroundColor, put_ButtonHoverForegroundColor)
    ButtonInactiveBackgroundColor = property(get_ButtonInactiveBackgroundColor, put_ButtonInactiveBackgroundColor)
    ButtonInactiveForegroundColor = property(get_ButtonInactiveForegroundColor, put_ButtonInactiveForegroundColor)
    ButtonPressedBackgroundColor = property(get_ButtonPressedBackgroundColor, put_ButtonPressedBackgroundColor)
    ButtonPressedForegroundColor = property(get_ButtonPressedForegroundColor, put_ButtonPressedForegroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    InactiveBackgroundColor = property(get_InactiveBackgroundColor, put_InactiveBackgroundColor)
    InactiveForegroundColor = property(get_InactiveForegroundColor, put_InactiveForegroundColor)
class IApplicationViewTransferContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewTransferContext'
    _iid_ = Guid('{8574bc63-3c17-408e-9408-8a1a9ea81bfa}')
    @winrt_commethod(6)
    def get_ViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ViewId(self, value: Int32) -> Void: ...
    ViewId = property(get_ViewId, put_ViewId)
class IApplicationViewTransferContextStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewTransferContextStatics'
    _iid_ = Guid('{15a89d92-dd79-4b0b-bc47-d5f195f14661}')
    @winrt_commethod(6)
    def get_DataPackageFormatId(self) -> WinRT_String: ...
    DataPackageFormatId = property(get_DataPackageFormatId, None)
class IApplicationViewWithContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IApplicationViewWithContext'
    _iid_ = Guid('{bd55d512-9dc1-44fc-8501-666625df60dc}')
    @winrt_commethod(6)
    def get_UIContext(self) -> win32more.Windows.UI.UIContext: ...
    UIContext = property(get_UIContext, None)
class IInputPane(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPane'
    _iid_ = Guid('{640ada70-06f3-4c87-a678-9829c9127c28}')
    @winrt_commethod(6)
    def add_Showing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.InputPane, win32more.Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Showing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Hiding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.InputPane, win32more.Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Hiding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_OccludedRect(self) -> win32more.Windows.Foundation.Rect: ...
    OccludedRect = property(get_OccludedRect, None)
    Showing = event()
    Hiding = event()
class IInputPane2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPane2'
    _iid_ = Guid('{8a6b3f26-7090-4793-944c-c3f2cde26276}')
    @winrt_commethod(6)
    def TryShow(self) -> Boolean: ...
    @winrt_commethod(7)
    def TryHide(self) -> Boolean: ...
class IInputPaneControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneControl'
    _iid_ = Guid('{088bb24f-962f-489d-aa6e-c6be1a0a6e52}')
    @winrt_commethod(6)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Visible(self, value: Boolean) -> Void: ...
    Visible = property(get_Visible, put_Visible)
class IInputPaneStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneStatics'
    _iid_ = Guid('{95f4af3a-ef47-424a-9741-fd2815eba2bd}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.ViewManagement.InputPane: ...
class IInputPaneStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneStatics2'
    _iid_ = Guid('{1b63529b-d9ec-4531-8445-71bab9fb828e}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: win32more.Windows.UI.UIContext) -> win32more.Windows.UI.ViewManagement.InputPane: ...
class IInputPaneVisibilityEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs'
    _iid_ = Guid('{d243e016-d907-4fcc-bb8d-f77baa5028f1}')
    @winrt_commethod(6)
    def get_OccludedRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_EnsuredFocusedElementInView(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_EnsuredFocusedElementInView(self) -> Boolean: ...
    EnsuredFocusedElementInView = property(get_EnsuredFocusedElementInView, put_EnsuredFocusedElementInView)
    OccludedRect = property(get_OccludedRect, None)
class IProjectionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IProjectionManagerStatics'
    _iid_ = Guid('{b65f913d-e2f0-4ffd-ba95-34241647e45c}')
    @winrt_commethod(6)
    def StartProjectingAsync(self, projectionViewId: Int32, anchorViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def SwapDisplaysForViewsAsync(self, projectionViewId: Int32, anchorViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def StopProjectingAsync(self, projectionViewId: Int32, anchorViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_ProjectionDisplayAvailable(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_ProjectionDisplayAvailableChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ProjectionDisplayAvailableChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProjectionDisplayAvailable = property(get_ProjectionDisplayAvailable, None)
    ProjectionDisplayAvailableChanged = event()
class IProjectionManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IProjectionManagerStatics2'
    _iid_ = Guid('{f33d2f43-2749-4cde-b977-c0c41e7415d1}')
    @winrt_commethod(6)
    def StartProjectingWithDeviceInfoAsync(self, projectionViewId: Int32, anchorViewId: Int32, displayDeviceInfo: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RequestStartProjectingAsync(self, projectionViewId: Int32, anchorViewId: Int32, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def RequestStartProjectingWithPlacementAsync(self, projectionViewId: Int32, anchorViewId: Int32, selection: win32more.Windows.Foundation.Rect, prefferedPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IStatusBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IStatusBar'
    _iid_ = Guid('{0ffcc5bf-98d0-4864-b1e8-b3f4020be8b4}')
    @winrt_commethod(6)
    def ShowAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def HideAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_BackgroundOpacity(self) -> Double: ...
    @winrt_commethod(9)
    def put_BackgroundOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ForegroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(11)
    def put_ForegroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(13)
    def put_BackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(14)
    def get_ProgressIndicator(self) -> win32more.Windows.UI.ViewManagement.StatusBarProgressIndicator: ...
    @winrt_commethod(15)
    def get_OccludedRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(16)
    def add_Showing(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.StatusBar, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_Showing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_Hiding(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.StatusBar, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_Hiding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    BackgroundOpacity = property(get_BackgroundOpacity, put_BackgroundOpacity)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    OccludedRect = property(get_OccludedRect, None)
    ProgressIndicator = property(get_ProgressIndicator, None)
    Showing = event()
    Hiding = event()
class IStatusBarProgressIndicator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IStatusBarProgressIndicator'
    _iid_ = Guid('{76cb2670-a3d7-49cf-8200-4f3eedca27bb}')
    @winrt_commethod(6)
    def ShowAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def HideAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ProgressValue(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def put_ProgressValue(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    ProgressValue = property(get_ProgressValue, put_ProgressValue)
    Text = property(get_Text, put_Text)
class IStatusBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IStatusBarStatics'
    _iid_ = Guid('{8b463fdf-422f-4561-8806-fb1289cadfb7}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.ViewManagement.StatusBar: ...
class IUISettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings'
    _iid_ = Guid('{85361600-1c63-4627-bcb1-3a89e0bc9c55}')
    @winrt_commethod(6)
    def get_HandPreference(self) -> win32more.Windows.UI.ViewManagement.HandPreference: ...
    @winrt_commethod(7)
    def get_CursorSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_ScrollBarSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def get_ScrollBarArrowSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def get_ScrollBarThumbBoxSize(self) -> win32more.Windows.Foundation.Size: ...
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
    def UIElementColor(self, desiredElement: win32more.Windows.UI.ViewManagement.UIElementType) -> win32more.Windows.UI.Color: ...
    AnimationsEnabled = property(get_AnimationsEnabled, None)
    CaretBlinkRate = property(get_CaretBlinkRate, None)
    CaretBrowsingEnabled = property(get_CaretBrowsingEnabled, None)
    CaretWidth = property(get_CaretWidth, None)
    CursorSize = property(get_CursorSize, None)
    DoubleClickTime = property(get_DoubleClickTime, None)
    HandPreference = property(get_HandPreference, None)
    MessageDuration = property(get_MessageDuration, None)
    MouseHoverTime = property(get_MouseHoverTime, None)
    ScrollBarArrowSize = property(get_ScrollBarArrowSize, None)
    ScrollBarSize = property(get_ScrollBarSize, None)
    ScrollBarThumbBoxSize = property(get_ScrollBarThumbBoxSize, None)
class IUISettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings2'
    _iid_ = Guid('{bad82401-2721-44f9-bb91-2bb228be442f}')
    @winrt_commethod(6)
    def get_TextScaleFactor(self) -> Double: ...
    @winrt_commethod(7)
    def add_TextScaleFactorChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_TextScaleFactorChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    TextScaleFactor = property(get_TextScaleFactor, None)
    TextScaleFactorChanged = event()
class IUISettings3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings3'
    _iid_ = Guid('{03021be4-5254-4781-8194-5168f7d06d7b}')
    @winrt_commethod(6)
    def GetColorValue(self, desiredColor: win32more.Windows.UI.ViewManagement.UIColorType) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def add_ColorValuesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ColorValuesChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ColorValuesChanged = event()
class IUISettings4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings4'
    _iid_ = Guid('{52bb3002-919b-4d6b-9b78-8dd66ff4b93b}')
    @winrt_commethod(6)
    def get_AdvancedEffectsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_AdvancedEffectsEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AdvancedEffectsEnabledChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdvancedEffectsEnabled = property(get_AdvancedEffectsEnabled, None)
    AdvancedEffectsEnabledChanged = event()
class IUISettings5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings5'
    _iid_ = Guid('{5349d588-0cb5-5f05-bd34-706b3231f0bd}')
    @winrt_commethod(6)
    def get_AutoHideScrollBars(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_AutoHideScrollBarsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.UI.ViewManagement.UISettingsAutoHideScrollBarsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AutoHideScrollBarsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoHideScrollBars = property(get_AutoHideScrollBars, None)
    AutoHideScrollBarsChanged = event()
class IUISettings6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettings6'
    _iid_ = Guid('{aef19bd7-fe31-5a04-ada4-469aaec6dfa9}')
    @winrt_commethod(6)
    def add_AnimationsEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.UI.ViewManagement.UISettingsAnimationsEnabledChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AnimationsEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_MessageDurationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.UI.ViewManagement.UISettingsMessageDurationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageDurationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AnimationsEnabledChanged = event()
    MessageDurationChanged = event()
class IUISettingsAnimationsEnabledChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettingsAnimationsEnabledChangedEventArgs'
    _iid_ = Guid('{0c7b4b3d-2ea1-533e-894d-415bc5243c29}')
class IUISettingsAutoHideScrollBarsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettingsAutoHideScrollBarsChangedEventArgs'
    _iid_ = Guid('{87afd4b2-9146-5f02-8f6b-06d454174c0f}')
class IUISettingsMessageDurationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUISettingsMessageDurationChangedEventArgs'
    _iid_ = Guid('{338aad52-4a5d-5b59-8002-d930f608fd6e}')
class IUIViewSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUIViewSettings'
    _iid_ = Guid('{c63657f6-8850-470d-88f8-455e16ea2c26}')
    @winrt_commethod(6)
    def get_UserInteractionMode(self) -> win32more.Windows.UI.ViewManagement.UserInteractionMode: ...
    UserInteractionMode = property(get_UserInteractionMode, None)
class IUIViewSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IUIViewSettingsStatics'
    _iid_ = Guid('{595c97a5-f8f6-41cf-b0fb-aacdb81fd5f6}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.ViewManagement.UIViewSettings: ...
class IViewModePreferences(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IViewModePreferences'
    _iid_ = Guid('{878fcd3a-0b99-42c9-84d0-d3f1d403554b}')
    @winrt_commethod(6)
    def get_ViewSizePreference(self) -> win32more.Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_commethod(7)
    def put_ViewSizePreference(self, value: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    @winrt_commethod(8)
    def get_CustomSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_CustomSize(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    CustomSize = property(get_CustomSize, put_CustomSize)
    ViewSizePreference = property(get_ViewSizePreference, put_ViewSizePreference)
class IViewModePreferencesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.IViewModePreferencesStatics'
    _iid_ = Guid('{69b60a65-5de5-40d8-8306-3833df7a2274}')
    @winrt_commethod(6)
    def CreateDefault(self, mode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> win32more.Windows.UI.ViewManagement.ViewModePreferences: ...
class InputPane(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IInputPane
    _classid_ = 'Windows.UI.ViewManagement.InputPane'
    @winrt_mixinmethod
    def add_Showing(self: win32more.Windows.UI.ViewManagement.IInputPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.InputPane, win32more.Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Showing(self: win32more.Windows.UI.ViewManagement.IInputPane, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Hiding(self: win32more.Windows.UI.ViewManagement.IInputPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.InputPane, win32more.Windows.UI.ViewManagement.InputPaneVisibilityEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Hiding(self: win32more.Windows.UI.ViewManagement.IInputPane, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OccludedRect(self: win32more.Windows.UI.ViewManagement.IInputPane) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def TryShow(self: win32more.Windows.UI.ViewManagement.IInputPane2) -> Boolean: ...
    @winrt_mixinmethod
    def TryHide(self: win32more.Windows.UI.ViewManagement.IInputPane2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.UI.ViewManagement.IInputPaneControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Visible(self: win32more.Windows.UI.ViewManagement.IInputPaneControl, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: win32more.Windows.UI.ViewManagement.IInputPaneStatics2, context: win32more.Windows.UI.UIContext) -> win32more.Windows.UI.ViewManagement.InputPane: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ViewManagement.IInputPaneStatics) -> win32more.Windows.UI.ViewManagement.InputPane: ...
    OccludedRect = property(get_OccludedRect, None)
    Visible = property(get_Visible, put_Visible)
    Showing = event()
    Hiding = event()
class InputPaneVisibilityEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs
    _classid_ = 'Windows.UI.ViewManagement.InputPaneVisibilityEventArgs'
    @winrt_mixinmethod
    def get_OccludedRect(self: win32more.Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_EnsuredFocusedElementInView(self: win32more.Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_EnsuredFocusedElementInView(self: win32more.Windows.UI.ViewManagement.IInputPaneVisibilityEventArgs) -> Boolean: ...
    EnsuredFocusedElementInView = property(get_EnsuredFocusedElementInView, put_EnsuredFocusedElementInView)
    OccludedRect = property(get_OccludedRect, None)
class _ProjectionManager_Meta_(ComPtr.__class__):
    pass
class ProjectionManager(ComPtr, metaclass=_ProjectionManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.ProjectionManager'
    @winrt_classmethod
    def StartProjectingWithDeviceInfoAsync(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics2, projectionViewId: Int32, anchorViewId: Int32, displayDeviceInfo: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RequestStartProjectingAsync(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics2, projectionViewId: Int32, anchorViewId: Int32, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RequestStartProjectingWithPlacementAsync(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics2, projectionViewId: Int32, anchorViewId: Int32, selection: win32more.Windows.Foundation.Rect, prefferedPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def StartProjectingAsync(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics, projectionViewId: Int32, anchorViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SwapDisplaysForViewsAsync(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics, projectionViewId: Int32, anchorViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def StopProjectingAsync(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics, projectionViewId: Int32, anchorViewId: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_ProjectionDisplayAvailable(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def add_ProjectionDisplayAvailableChanged(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProjectionDisplayAvailableChanged(cls: win32more.Windows.UI.ViewManagement.IProjectionManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _ProjectionManager_Meta_.ProjectionDisplayAvailable = property(get_ProjectionDisplayAvailable, None)
class ScreenCaptureDisabledBehavior(Enum, Int32):
    DrawAsBlack = 0
    ExcludeFromCapture = 1
class StatusBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IStatusBar
    _classid_ = 'Windows.UI.ViewManagement.StatusBar'
    @winrt_mixinmethod
    def ShowAsync(self: win32more.Windows.UI.ViewManagement.IStatusBar) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def HideAsync(self: win32more.Windows.UI.ViewManagement.IStatusBar) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_BackgroundOpacity(self: win32more.Windows.UI.ViewManagement.IStatusBar) -> Double: ...
    @winrt_mixinmethod
    def put_BackgroundOpacity(self: win32more.Windows.UI.ViewManagement.IStatusBar, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: win32more.Windows.UI.ViewManagement.IStatusBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: win32more.Windows.UI.ViewManagement.IStatusBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.ViewManagement.IStatusBar) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.UI.ViewManagement.IStatusBar, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ProgressIndicator(self: win32more.Windows.UI.ViewManagement.IStatusBar) -> win32more.Windows.UI.ViewManagement.StatusBarProgressIndicator: ...
    @winrt_mixinmethod
    def get_OccludedRect(self: win32more.Windows.UI.ViewManagement.IStatusBar) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def add_Showing(self: win32more.Windows.UI.ViewManagement.IStatusBar, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.StatusBar, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Showing(self: win32more.Windows.UI.ViewManagement.IStatusBar, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Hiding(self: win32more.Windows.UI.ViewManagement.IStatusBar, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.StatusBar, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Hiding(self: win32more.Windows.UI.ViewManagement.IStatusBar, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ViewManagement.IStatusBarStatics) -> win32more.Windows.UI.ViewManagement.StatusBar: ...
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    BackgroundOpacity = property(get_BackgroundOpacity, put_BackgroundOpacity)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    OccludedRect = property(get_OccludedRect, None)
    ProgressIndicator = property(get_ProgressIndicator, None)
    Showing = event()
    Hiding = event()
class StatusBarProgressIndicator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IStatusBarProgressIndicator
    _classid_ = 'Windows.UI.ViewManagement.StatusBarProgressIndicator'
    @winrt_mixinmethod
    def ShowAsync(self: win32more.Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def HideAsync(self: win32more.Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.UI.ViewManagement.IStatusBarProgressIndicator, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProgressValue(self: win32more.Windows.UI.ViewManagement.IStatusBarProgressIndicator) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_ProgressValue(self: win32more.Windows.UI.ViewManagement.IStatusBarProgressIndicator, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    ProgressValue = property(get_ProgressValue, put_ProgressValue)
    Text = property(get_Text, put_Text)
class UIColorType(Enum, Int32):
    Background = 0
    Foreground = 1
    AccentDark3 = 2
    AccentDark2 = 3
    AccentDark1 = 4
    Accent = 5
    AccentLight1 = 6
    AccentLight2 = 7
    AccentLight3 = 8
    Complement = 9
class UIElementType(Enum, Int32):
    ActiveCaption = 0
    Background = 1
    ButtonFace = 2
    ButtonText = 3
    CaptionText = 4
    GrayText = 5
    Highlight = 6
    HighlightText = 7
    Hotlight = 8
    InactiveCaption = 9
    InactiveCaptionText = 10
    Window = 11
    WindowText = 12
    AccentColor = 1000
    TextHigh = 1001
    TextMedium = 1002
    TextLow = 1003
    TextContrastWithHigh = 1004
    NonTextHigh = 1005
    NonTextMediumHigh = 1006
    NonTextMedium = 1007
    NonTextMediumLow = 1008
    NonTextLow = 1009
    PageBackground = 1010
    PopupBackground = 1011
    OverlayOutsidePopup = 1012
class UISettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IUISettings
    _classid_ = 'Windows.UI.ViewManagement.UISettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.ViewManagement.UISettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.ViewManagement.UISettings: ...
    @winrt_mixinmethod
    def get_HandPreference(self: win32more.Windows.UI.ViewManagement.IUISettings) -> win32more.Windows.UI.ViewManagement.HandPreference: ...
    @winrt_mixinmethod
    def get_CursorSize(self: win32more.Windows.UI.ViewManagement.IUISettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ScrollBarSize(self: win32more.Windows.UI.ViewManagement.IUISettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ScrollBarArrowSize(self: win32more.Windows.UI.ViewManagement.IUISettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ScrollBarThumbBoxSize(self: win32more.Windows.UI.ViewManagement.IUISettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_MessageDuration(self: win32more.Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_AnimationsEnabled(self: win32more.Windows.UI.ViewManagement.IUISettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_CaretBrowsingEnabled(self: win32more.Windows.UI.ViewManagement.IUISettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_CaretBlinkRate(self: win32more.Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_CaretWidth(self: win32more.Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_DoubleClickTime(self: win32more.Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def get_MouseHoverTime(self: win32more.Windows.UI.ViewManagement.IUISettings) -> UInt32: ...
    @winrt_mixinmethod
    def UIElementColor(self: win32more.Windows.UI.ViewManagement.IUISettings, desiredElement: win32more.Windows.UI.ViewManagement.UIElementType) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_TextScaleFactor(self: win32more.Windows.UI.ViewManagement.IUISettings2) -> Double: ...
    @winrt_mixinmethod
    def add_TextScaleFactorChanged(self: win32more.Windows.UI.ViewManagement.IUISettings2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextScaleFactorChanged(self: win32more.Windows.UI.ViewManagement.IUISettings2, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetColorValue(self: win32more.Windows.UI.ViewManagement.IUISettings3, desiredColor: win32more.Windows.UI.ViewManagement.UIColorType) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def add_ColorValuesChanged(self: win32more.Windows.UI.ViewManagement.IUISettings3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ColorValuesChanged(self: win32more.Windows.UI.ViewManagement.IUISettings3, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AdvancedEffectsEnabled(self: win32more.Windows.UI.ViewManagement.IUISettings4) -> Boolean: ...
    @winrt_mixinmethod
    def add_AdvancedEffectsEnabledChanged(self: win32more.Windows.UI.ViewManagement.IUISettings4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvancedEffectsEnabledChanged(self: win32more.Windows.UI.ViewManagement.IUISettings4, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AutoHideScrollBars(self: win32more.Windows.UI.ViewManagement.IUISettings5) -> Boolean: ...
    @winrt_mixinmethod
    def add_AutoHideScrollBarsChanged(self: win32more.Windows.UI.ViewManagement.IUISettings5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.UI.ViewManagement.UISettingsAutoHideScrollBarsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AutoHideScrollBarsChanged(self: win32more.Windows.UI.ViewManagement.IUISettings5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AnimationsEnabledChanged(self: win32more.Windows.UI.ViewManagement.IUISettings6, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.UI.ViewManagement.UISettingsAnimationsEnabledChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AnimationsEnabledChanged(self: win32more.Windows.UI.ViewManagement.IUISettings6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MessageDurationChanged(self: win32more.Windows.UI.ViewManagement.IUISettings6, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.UISettings, win32more.Windows.UI.ViewManagement.UISettingsMessageDurationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageDurationChanged(self: win32more.Windows.UI.ViewManagement.IUISettings6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdvancedEffectsEnabled = property(get_AdvancedEffectsEnabled, None)
    AnimationsEnabled = property(get_AnimationsEnabled, None)
    AutoHideScrollBars = property(get_AutoHideScrollBars, None)
    CaretBlinkRate = property(get_CaretBlinkRate, None)
    CaretBrowsingEnabled = property(get_CaretBrowsingEnabled, None)
    CaretWidth = property(get_CaretWidth, None)
    CursorSize = property(get_CursorSize, None)
    DoubleClickTime = property(get_DoubleClickTime, None)
    HandPreference = property(get_HandPreference, None)
    MessageDuration = property(get_MessageDuration, None)
    MouseHoverTime = property(get_MouseHoverTime, None)
    ScrollBarArrowSize = property(get_ScrollBarArrowSize, None)
    ScrollBarSize = property(get_ScrollBarSize, None)
    ScrollBarThumbBoxSize = property(get_ScrollBarThumbBoxSize, None)
    TextScaleFactor = property(get_TextScaleFactor, None)
    TextScaleFactorChanged = event()
    ColorValuesChanged = event()
    AdvancedEffectsEnabledChanged = event()
    AutoHideScrollBarsChanged = event()
    AnimationsEnabledChanged = event()
    MessageDurationChanged = event()
class UISettingsAnimationsEnabledChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IUISettingsAnimationsEnabledChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.UISettingsAnimationsEnabledChangedEventArgs'
class UISettingsAutoHideScrollBarsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IUISettingsAutoHideScrollBarsChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.UISettingsAutoHideScrollBarsChangedEventArgs'
class UISettingsMessageDurationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IUISettingsMessageDurationChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.UISettingsMessageDurationChangedEventArgs'
class UIViewSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IUIViewSettings
    _classid_ = 'Windows.UI.ViewManagement.UIViewSettings'
    @winrt_mixinmethod
    def get_UserInteractionMode(self: win32more.Windows.UI.ViewManagement.IUIViewSettings) -> win32more.Windows.UI.ViewManagement.UserInteractionMode: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ViewManagement.IUIViewSettingsStatics) -> win32more.Windows.UI.ViewManagement.UIViewSettings: ...
    UserInteractionMode = property(get_UserInteractionMode, None)
class UserInteractionMode(Enum, Int32):
    Mouse = 0
    Touch = 1
ViewManagementViewScalingContract: UInt32 = 65536
class ViewModePreferences(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.IViewModePreferences
    _classid_ = 'Windows.UI.ViewManagement.ViewModePreferences'
    @winrt_mixinmethod
    def get_ViewSizePreference(self: win32more.Windows.UI.ViewManagement.IViewModePreferences) -> win32more.Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_mixinmethod
    def put_ViewSizePreference(self: win32more.Windows.UI.ViewManagement.IViewModePreferences, value: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    @winrt_mixinmethod
    def get_CustomSize(self: win32more.Windows.UI.ViewManagement.IViewModePreferences) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CustomSize(self: win32more.Windows.UI.ViewManagement.IViewModePreferences, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_classmethod
    def CreateDefault(cls: win32more.Windows.UI.ViewManagement.IViewModePreferencesStatics, mode: win32more.Windows.UI.ViewManagement.ApplicationViewMode) -> win32more.Windows.UI.ViewManagement.ViewModePreferences: ...
    CustomSize = property(get_CustomSize, put_CustomSize)
    ViewSizePreference = property(get_ViewSizePreference, put_ViewSizePreference)
class ViewSizePreference(Enum, Int32):
    Default = 0
    UseLess = 1
    UseHalf = 2
    UseMore = 3
    UseMinimum = 4
    UseNone = 5
    Custom = 6


make_ready(__name__)
