from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.ApplicationModel.DataTransfer.DragDrop
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.Imaging
import win32more.Windows.UI
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Automation.Peers
import win32more.Windows.UI.Xaml.Controls
import win32more.Windows.UI.Xaml.Controls.Primitives
import win32more.Windows.UI.Xaml.Data
import win32more.Windows.UI.Xaml.Input
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.UI.Xaml.Media
import win32more.Windows.UI.Xaml.Media.Animation
import win32more.Windows.UI.Xaml.Media.Imaging
import win32more.Windows.UI.Xaml.Media.Media3D
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class _AdaptiveTrigger_Meta_(ComPtr.__class__):
    pass
class AdaptiveTrigger(ComPtr, metaclass=_AdaptiveTrigger_Meta_):
    extends: win32more.Windows.UI.Xaml.StateTriggerBase
    default_interface: win32more.Windows.UI.Xaml.IAdaptiveTrigger
    _classid_ = 'Windows.UI.Xaml.AdaptiveTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.AdaptiveTrigger.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IAdaptiveTriggerFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.AdaptiveTrigger: ...
    @winrt_mixinmethod
    def get_MinWindowWidth(self: win32more.Windows.UI.Xaml.IAdaptiveTrigger) -> Double: ...
    @winrt_mixinmethod
    def put_MinWindowWidth(self: win32more.Windows.UI.Xaml.IAdaptiveTrigger, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MinWindowHeight(self: win32more.Windows.UI.Xaml.IAdaptiveTrigger) -> Double: ...
    @winrt_mixinmethod
    def put_MinWindowHeight(self: win32more.Windows.UI.Xaml.IAdaptiveTrigger, value: Double) -> Void: ...
    @winrt_classmethod
    def get_MinWindowWidthProperty(cls: win32more.Windows.UI.Xaml.IAdaptiveTriggerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinWindowHeightProperty(cls: win32more.Windows.UI.Xaml.IAdaptiveTriggerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MinWindowHeight = property(get_MinWindowHeight, put_MinWindowHeight)
    MinWindowWidth = property(get_MinWindowWidth, put_MinWindowWidth)
    _AdaptiveTrigger_Meta_.MinWindowHeightProperty = property(get_MinWindowHeightProperty, None)
    _AdaptiveTrigger_Meta_.MinWindowWidthProperty = property(get_MinWindowWidthProperty, None)
class _Application_Meta_(ComPtr.__class__):
    pass
class Application(ComPtr, metaclass=_Application_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IApplication
    _classid_ = 'Windows.UI.Xaml.Application'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Application.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IApplicationFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Application: ...
    @winrt_mixinmethod
    def get_Resources(self: win32more.Windows.UI.Xaml.IApplication) -> win32more.Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_mixinmethod
    def put_Resources(self: win32more.Windows.UI.Xaml.IApplication, value: win32more.Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_mixinmethod
    def get_DebugSettings(self: win32more.Windows.UI.Xaml.IApplication) -> win32more.Windows.UI.Xaml.DebugSettings: ...
    @winrt_mixinmethod
    def get_RequestedTheme(self: win32more.Windows.UI.Xaml.IApplication) -> win32more.Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_mixinmethod
    def put_RequestedTheme(self: win32more.Windows.UI.Xaml.IApplication, value: win32more.Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_mixinmethod
    def add_UnhandledException(self: win32more.Windows.UI.Xaml.IApplication, handler: win32more.Windows.UI.Xaml.UnhandledExceptionEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnhandledException(self: win32more.Windows.UI.Xaml.IApplication, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Suspending(self: win32more.Windows.UI.Xaml.IApplication, handler: win32more.Windows.UI.Xaml.SuspendingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Suspending(self: win32more.Windows.UI.Xaml.IApplication, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Resuming(self: win32more.Windows.UI.Xaml.IApplication, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Resuming(self: win32more.Windows.UI.Xaml.IApplication, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Exit(self: win32more.Windows.UI.Xaml.IApplication) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualKind(self: win32more.Windows.UI.Xaml.IApplication2) -> win32more.Windows.UI.Xaml.FocusVisualKind: ...
    @winrt_mixinmethod
    def put_FocusVisualKind(self: win32more.Windows.UI.Xaml.IApplication2, value: win32more.Windows.UI.Xaml.FocusVisualKind) -> Void: ...
    @winrt_mixinmethod
    def get_RequiresPointerMode(self: win32more.Windows.UI.Xaml.IApplication2) -> win32more.Windows.UI.Xaml.ApplicationRequiresPointerMode: ...
    @winrt_mixinmethod
    def put_RequiresPointerMode(self: win32more.Windows.UI.Xaml.IApplication2, value: win32more.Windows.UI.Xaml.ApplicationRequiresPointerMode) -> Void: ...
    @winrt_mixinmethod
    def add_LeavingBackground(self: win32more.Windows.UI.Xaml.IApplication2, handler: win32more.Windows.UI.Xaml.LeavingBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LeavingBackground(self: win32more.Windows.UI.Xaml.IApplication2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnteredBackground(self: win32more.Windows.UI.Xaml.IApplication2, handler: win32more.Windows.UI.Xaml.EnteredBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnteredBackground(self: win32more.Windows.UI.Xaml.IApplication2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HighContrastAdjustment(self: win32more.Windows.UI.Xaml.IApplication3) -> win32more.Windows.UI.Xaml.ApplicationHighContrastAdjustment: ...
    @winrt_mixinmethod
    def put_HighContrastAdjustment(self: win32more.Windows.UI.Xaml.IApplication3, value: win32more.Windows.UI.Xaml.ApplicationHighContrastAdjustment) -> Void: ...
    @winrt_mixinmethod
    def OnActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnLaunched(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.LaunchActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnFileActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.FileActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnSearchActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.SearchActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnShareTargetActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.ShareTargetActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnFileOpenPickerActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.FileOpenPickerActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnFileSavePickerActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.FileSavePickerActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnCachedFileUpdaterActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.ApplicationModel.Activation.CachedFileUpdaterActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnWindowCreated(self: win32more.Windows.UI.Xaml.IApplicationOverrides, args: win32more.Windows.UI.Xaml.WindowCreatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnBackgroundActivated(self: win32more.Windows.UI.Xaml.IApplicationOverrides2, args: win32more.Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs) -> Void: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.UI.Xaml.IApplicationStatics) -> win32more.Windows.UI.Xaml.Application: ...
    @winrt_classmethod
    def Start(cls: win32more.Windows.UI.Xaml.IApplicationStatics, callback: win32more.Windows.UI.Xaml.ApplicationInitializationCallback) -> Void: ...
    @winrt_classmethod
    def LoadComponent(cls: win32more.Windows.UI.Xaml.IApplicationStatics, component: win32more.Windows.Win32.System.WinRT.IInspectable, resourceLocator: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def LoadComponentWithResourceLocation(cls: win32more.Windows.UI.Xaml.IApplicationStatics, component: win32more.Windows.Win32.System.WinRT.IInspectable, resourceLocator: win32more.Windows.Foundation.Uri, componentResourceLocation: win32more.Windows.UI.Xaml.Controls.Primitives.ComponentResourceLocation) -> Void: ...
    DebugSettings = property(get_DebugSettings, None)
    FocusVisualKind = property(get_FocusVisualKind, put_FocusVisualKind)
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
    RequiresPointerMode = property(get_RequiresPointerMode, put_RequiresPointerMode)
    Resources = property(get_Resources, put_Resources)
    _Application_Meta_.Current = property(get_Current, None)
    UnhandledException = event()
    Suspending = event()
    Resuming = event()
    LeavingBackground = event()
    EnteredBackground = event()
class ApplicationHighContrastAdjustment(Enum, UInt32):
    None_ = 0
    Auto = 4294967295
class ApplicationInitializationCallback(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b6351c55-c284-46e4-8310-fb0967fab76f}')
    @winrt_commethod(3)
    def Invoke(self, p: win32more.Windows.UI.Xaml.ApplicationInitializationCallbackParams) -> Void: ...
class ApplicationInitializationCallbackParams(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IApplicationInitializationCallbackParams
    _classid_ = 'Windows.UI.Xaml.ApplicationInitializationCallbackParams'
class ApplicationRequiresPointerMode(Enum, Int32):
    Auto = 0
    WhenRequested = 1
class ApplicationTheme(Enum, Int32):
    Light = 0
    Dark = 1
class AutomationTextAttributesEnum(Enum, Int32):
    AnimationStyleAttribute = 40000
    BackgroundColorAttribute = 40001
    BulletStyleAttribute = 40002
    CapStyleAttribute = 40003
    CultureAttribute = 40004
    FontNameAttribute = 40005
    FontSizeAttribute = 40006
    FontWeightAttribute = 40007
    ForegroundColorAttribute = 40008
    HorizontalTextAlignmentAttribute = 40009
    IndentationFirstLineAttribute = 40010
    IndentationLeadingAttribute = 40011
    IndentationTrailingAttribute = 40012
    IsHiddenAttribute = 40013
    IsItalicAttribute = 40014
    IsReadOnlyAttribute = 40015
    IsSubscriptAttribute = 40016
    IsSuperscriptAttribute = 40017
    MarginBottomAttribute = 40018
    MarginLeadingAttribute = 40019
    MarginTopAttribute = 40020
    MarginTrailingAttribute = 40021
    OutlineStylesAttribute = 40022
    OverlineColorAttribute = 40023
    OverlineStyleAttribute = 40024
    StrikethroughColorAttribute = 40025
    StrikethroughStyleAttribute = 40026
    TabsAttribute = 40027
    TextFlowDirectionsAttribute = 40028
    UnderlineColorAttribute = 40029
    UnderlineStyleAttribute = 40030
    AnnotationTypesAttribute = 40031
    AnnotationObjectsAttribute = 40032
    StyleNameAttribute = 40033
    StyleIdAttribute = 40034
    LinkAttribute = 40035
    IsActiveAttribute = 40036
    SelectionActiveEndAttribute = 40037
    CaretPositionAttribute = 40038
    CaretBidiModeAttribute = 40039
class BindingFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IBindingFailedEventArgs
    _classid_ = 'Windows.UI.Xaml.BindingFailedEventArgs'
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.UI.Xaml.IBindingFailedEventArgs) -> WinRT_String: ...
    Message = property(get_Message, None)
class BindingFailedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{136b1782-54ba-420d-a1aa-82828721cde6}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.BindingFailedEventArgs) -> Void: ...
class BringIntoViewOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IBringIntoViewOptions
    _classid_ = 'Windows.UI.Xaml.BringIntoViewOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.BringIntoViewOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.BringIntoViewOptions: ...
    @winrt_mixinmethod
    def get_AnimationDesired(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AnimationDesired(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TargetRect(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_TargetRect(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalAlignmentRatio(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalAlignmentRatio(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    TargetRect = property(get_TargetRect, put_TargetRect)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
class BringIntoViewRequestedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.BringIntoViewRequestedEventArgs'
    @winrt_mixinmethod
    def get_TargetElement(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_TargetElement(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_AnimationDesired(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_AnimationDesired(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TargetRect(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_TargetRect(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Boolean) -> Void: ...
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    Handled = property(get_Handled, put_Handled)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, None)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    TargetElement = property(get_TargetElement, put_TargetElement)
    TargetRect = property(get_TargetRect, put_TargetRect)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, None)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
class BrushTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IBrushTransition
    _classid_ = 'Windows.UI.Xaml.BrushTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.BrushTransition.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IBrushTransitionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.BrushTransition: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Xaml.IBrushTransition) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.UI.Xaml.IBrushTransition, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class ColorPaletteResources(ComPtr):
    extends: win32more.Windows.UI.Xaml.ResourceDictionary
    default_interface: win32more.Windows.UI.Xaml.IColorPaletteResources
    _classid_ = 'Windows.UI.Xaml.ColorPaletteResources'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.ColorPaletteResources.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IColorPaletteResourcesFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ColorPaletteResources: ...
    @winrt_mixinmethod
    def get_AltHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltMediumHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltMediumHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseMediumHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseMediumHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeAltLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeAltLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeDisabledHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeDisabledHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeDisabledLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeDisabledLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeHigh(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeMediumLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeWhite(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeWhite(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeGray(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeGray(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ListLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ListLow(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ListMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ListMedium(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ErrorText(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_Accent(self: win32more.Windows.UI.Xaml.IColorPaletteResources) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_Accent(self: win32more.Windows.UI.Xaml.IColorPaletteResources, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    Accent = property(get_Accent, put_Accent)
    AltHigh = property(get_AltHigh, put_AltHigh)
    AltLow = property(get_AltLow, put_AltLow)
    AltMedium = property(get_AltMedium, put_AltMedium)
    AltMediumHigh = property(get_AltMediumHigh, put_AltMediumHigh)
    AltMediumLow = property(get_AltMediumLow, put_AltMediumLow)
    BaseHigh = property(get_BaseHigh, put_BaseHigh)
    BaseLow = property(get_BaseLow, put_BaseLow)
    BaseMedium = property(get_BaseMedium, put_BaseMedium)
    BaseMediumHigh = property(get_BaseMediumHigh, put_BaseMediumHigh)
    BaseMediumLow = property(get_BaseMediumLow, put_BaseMediumLow)
    ChromeAltLow = property(get_ChromeAltLow, put_ChromeAltLow)
    ChromeBlackHigh = property(get_ChromeBlackHigh, put_ChromeBlackHigh)
    ChromeBlackLow = property(get_ChromeBlackLow, put_ChromeBlackLow)
    ChromeBlackMedium = property(get_ChromeBlackMedium, put_ChromeBlackMedium)
    ChromeBlackMediumLow = property(get_ChromeBlackMediumLow, put_ChromeBlackMediumLow)
    ChromeDisabledHigh = property(get_ChromeDisabledHigh, put_ChromeDisabledHigh)
    ChromeDisabledLow = property(get_ChromeDisabledLow, put_ChromeDisabledLow)
    ChromeGray = property(get_ChromeGray, put_ChromeGray)
    ChromeHigh = property(get_ChromeHigh, put_ChromeHigh)
    ChromeLow = property(get_ChromeLow, put_ChromeLow)
    ChromeMedium = property(get_ChromeMedium, put_ChromeMedium)
    ChromeMediumLow = property(get_ChromeMediumLow, put_ChromeMediumLow)
    ChromeWhite = property(get_ChromeWhite, put_ChromeWhite)
    ErrorText = property(get_ErrorText, put_ErrorText)
    ListLow = property(get_ListLow, put_ListLow)
    ListMedium = property(get_ListMedium, put_ListMedium)
class CornerRadius(Structure):
    TopLeft: Double
    TopRight: Double
    BottomRight: Double
    BottomLeft: Double
class CornerRadiusHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.ICornerRadiusHelper
    _classid_ = 'Windows.UI.Xaml.CornerRadiusHelper'
    @winrt_classmethod
    def FromRadii(cls: win32more.Windows.UI.Xaml.ICornerRadiusHelperStatics, topLeft: Double, topRight: Double, bottomRight: Double, bottomLeft: Double) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_classmethod
    def FromUniformRadius(cls: win32more.Windows.UI.Xaml.ICornerRadiusHelperStatics, uniformRadius: Double) -> win32more.Windows.UI.Xaml.CornerRadius: ...
class CreateDefaultValueCallback(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6ecb12c-15b5-4ec8-b95c-cdd208f08153}')
    @winrt_commethod(3)
    def Invoke(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class DataContextChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDataContextChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.DataContextChangedEventArgs'
    @winrt_mixinmethod
    def get_NewValue(self: win32more.Windows.UI.Xaml.IDataContextChangedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.IDataContextChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.IDataContextChangedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    NewValue = property(get_NewValue, None)
class _DataTemplate_Meta_(ComPtr.__class__):
    pass
class DataTemplate(ComPtr, metaclass=_DataTemplate_Meta_):
    extends: win32more.Windows.UI.Xaml.FrameworkTemplate
    default_interface: win32more.Windows.UI.Xaml.IDataTemplate
    _classid_ = 'Windows.UI.Xaml.DataTemplate'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.DataTemplate.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IDataTemplateFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DataTemplate: ...
    @winrt_mixinmethod
    def LoadContent(self: win32more.Windows.UI.Xaml.IDataTemplate) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def GetElement(self: win32more.Windows.UI.Xaml.IElementFactory, args: win32more.Windows.UI.Xaml.ElementFactoryGetArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def RecycleElement(self: win32more.Windows.UI.Xaml.IElementFactory, args: win32more.Windows.UI.Xaml.ElementFactoryRecycleArgs) -> Void: ...
    @winrt_classmethod
    def get_ExtensionInstanceProperty(cls: win32more.Windows.UI.Xaml.IDataTemplateStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetExtensionInstance(cls: win32more.Windows.UI.Xaml.IDataTemplateStatics2, element: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.UI.Xaml.IDataTemplateExtension: ...
    @winrt_classmethod
    def SetExtensionInstance(cls: win32more.Windows.UI.Xaml.IDataTemplateStatics2, element: win32more.Windows.UI.Xaml.FrameworkElement, value: win32more.Windows.UI.Xaml.IDataTemplateExtension) -> Void: ...
    _DataTemplate_Meta_.ExtensionInstanceProperty = property(get_ExtensionInstanceProperty, None)
class DataTemplateKey(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDataTemplateKey
    _classid_ = 'Windows.UI.Xaml.DataTemplateKey'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.DataTemplateKey.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.DataTemplateKey.CreateInstanceWithType(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IDataTemplateKeyFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DataTemplateKey: ...
    @winrt_factorymethod
    def CreateInstanceWithType(cls: win32more.Windows.UI.Xaml.IDataTemplateKeyFactory, dataType: win32more.Windows.Win32.System.WinRT.IInspectable, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DataTemplateKey: ...
    @winrt_mixinmethod
    def get_DataType(self: win32more.Windows.UI.Xaml.IDataTemplateKey) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_DataType(self: win32more.Windows.UI.Xaml.IDataTemplateKey, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    DataType = property(get_DataType, put_DataType)
class DebugSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDebugSettings
    _classid_ = 'Windows.UI.Xaml.DebugSettings'
    @winrt_mixinmethod
    def get_EnableFrameRateCounter(self: win32more.Windows.UI.Xaml.IDebugSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableFrameRateCounter(self: win32more.Windows.UI.Xaml.IDebugSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBindingTracingEnabled(self: win32more.Windows.UI.Xaml.IDebugSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBindingTracingEnabled(self: win32more.Windows.UI.Xaml.IDebugSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsOverdrawHeatMapEnabled(self: win32more.Windows.UI.Xaml.IDebugSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOverdrawHeatMapEnabled(self: win32more.Windows.UI.Xaml.IDebugSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_BindingFailed(self: win32more.Windows.UI.Xaml.IDebugSettings, handler: win32more.Windows.UI.Xaml.BindingFailedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BindingFailed(self: win32more.Windows.UI.Xaml.IDebugSettings, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_EnableRedrawRegions(self: win32more.Windows.UI.Xaml.IDebugSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableRedrawRegions(self: win32more.Windows.UI.Xaml.IDebugSettings2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsTextPerformanceVisualizationEnabled(self: win32more.Windows.UI.Xaml.IDebugSettings3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTextPerformanceVisualizationEnabled(self: win32more.Windows.UI.Xaml.IDebugSettings3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FailFastOnErrors(self: win32more.Windows.UI.Xaml.IDebugSettings4) -> Boolean: ...
    @winrt_mixinmethod
    def put_FailFastOnErrors(self: win32more.Windows.UI.Xaml.IDebugSettings4, value: Boolean) -> Void: ...
    EnableFrameRateCounter = property(get_EnableFrameRateCounter, put_EnableFrameRateCounter)
    EnableRedrawRegions = property(get_EnableRedrawRegions, put_EnableRedrawRegions)
    FailFastOnErrors = property(get_FailFastOnErrors, put_FailFastOnErrors)
    IsBindingTracingEnabled = property(get_IsBindingTracingEnabled, put_IsBindingTracingEnabled)
    IsOverdrawHeatMapEnabled = property(get_IsOverdrawHeatMapEnabled, put_IsOverdrawHeatMapEnabled)
    IsTextPerformanceVisualizationEnabled = property(get_IsTextPerformanceVisualizationEnabled, put_IsTextPerformanceVisualizationEnabled)
    BindingFailed = event()
class DependencyObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDependencyObject
    _classid_ = 'Windows.UI.Xaml.DependencyObject'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.DependencyObject.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IDependencyObjectFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def GetValue(self: win32more.Windows.UI.Xaml.IDependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def SetValue(self: win32more.Windows.UI.Xaml.IDependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def ClearValue(self: win32more.Windows.UI.Xaml.IDependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_mixinmethod
    def ReadLocalValue(self: win32more.Windows.UI.Xaml.IDependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetAnimationBaseValue(self: win32more.Windows.UI.Xaml.IDependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: win32more.Windows.UI.Xaml.IDependencyObject) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def RegisterPropertyChangedCallback(self: win32more.Windows.UI.Xaml.IDependencyObject2, dp: win32more.Windows.UI.Xaml.DependencyProperty, callback: win32more.Windows.UI.Xaml.DependencyPropertyChangedCallback) -> Int64: ...
    @winrt_mixinmethod
    def UnregisterPropertyChangedCallback(self: win32more.Windows.UI.Xaml.IDependencyObject2, dp: win32more.Windows.UI.Xaml.DependencyProperty, token: Int64) -> Void: ...
    Dispatcher = property(get_Dispatcher, None)
class DependencyObjectCollection(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.DependencyObject]]
    default_interface: win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.UI.Xaml.DependencyObject]
    _classid_ = 'Windows.UI.Xaml.DependencyObjectCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.DependencyObjectCollection.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IDependencyObjectCollectionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DependencyObjectCollection: ...
    @winrt_mixinmethod
    def add_VectorChanged(self: win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.UI.Xaml.DependencyObject], vhnd: win32more.Windows.Foundation.Collections.VectorChangedEventHandler[win32more.Windows.UI.Xaml.DependencyObject]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VectorChanged(self: win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.UI.Xaml.DependencyObject], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], index: UInt32) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], value: win32more.Windows.UI.Xaml.DependencyObject, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], index: UInt32, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], index: UInt32, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.DependencyObject]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject], items: PassArray[win32more.Windows.UI.Xaml.DependencyObject]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.DependencyObject]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.DependencyObject]: ...
    Size = property(get_Size, None)
    VectorChanged = event()
class _DependencyProperty_Meta_(ComPtr.__class__):
    pass
class DependencyProperty(ComPtr, metaclass=_DependencyProperty_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDependencyProperty
    _classid_ = 'Windows.UI.Xaml.DependencyProperty'
    @winrt_mixinmethod
    def GetMetadata(self: win32more.Windows.UI.Xaml.IDependencyProperty, forType: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def get_UnsetValue(cls: win32more.Windows.UI.Xaml.IDependencyPropertyStatics) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def Register(cls: win32more.Windows.UI.Xaml.IDependencyPropertyStatics, name: WinRT_String, propertyType: win32more.Windows.UI.Xaml.Interop.TypeName, ownerType: win32more.Windows.UI.Xaml.Interop.TypeName, typeMetadata: win32more.Windows.UI.Xaml.PropertyMetadata) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def RegisterAttached(cls: win32more.Windows.UI.Xaml.IDependencyPropertyStatics, name: WinRT_String, propertyType: win32more.Windows.UI.Xaml.Interop.TypeName, ownerType: win32more.Windows.UI.Xaml.Interop.TypeName, defaultMetadata: win32more.Windows.UI.Xaml.PropertyMetadata) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    _DependencyProperty_Meta_.UnsetValue = property(get_UnsetValue, None)
class DependencyPropertyChangedCallback(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45883d16-27bf-4bc1-ac26-94c1601f3a49}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.UI.Xaml.DependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> Void: ...
class DependencyPropertyChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDependencyPropertyChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.DependencyPropertyChangedEventArgs'
    @winrt_mixinmethod
    def get_Property(self: win32more.Windows.UI.Xaml.IDependencyPropertyChangedEventArgs) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_mixinmethod
    def get_OldValue(self: win32more.Windows.UI.Xaml.IDependencyPropertyChangedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_NewValue(self: win32more.Windows.UI.Xaml.IDependencyPropertyChangedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    NewValue = property(get_NewValue, None)
    OldValue = property(get_OldValue, None)
    Property = property(get_Property, None)
class DependencyPropertyChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09223e5a-75be-4499-8180-1ddc005421c0}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.DependencyPropertyChangedEventArgs) -> Void: ...
class DispatcherTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDispatcherTimer
    _classid_ = 'Windows.UI.Xaml.DispatcherTimer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.DispatcherTimer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IDispatcherTimerFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DispatcherTimer: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Windows.UI.Xaml.IDispatcherTimer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Interval(self: win32more.Windows.UI.Xaml.IDispatcherTimer, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.UI.Xaml.IDispatcherTimer) -> Boolean: ...
    @winrt_mixinmethod
    def add_Tick(self: win32more.Windows.UI.Xaml.IDispatcherTimer, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tick(self: win32more.Windows.UI.Xaml.IDispatcherTimer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.UI.Xaml.IDispatcherTimer) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.UI.Xaml.IDispatcherTimer) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsEnabled = property(get_IsEnabled, None)
    Tick = event()
class DragEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.IDragEventArgs
    _classid_ = 'Windows.UI.Xaml.DragEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.IDragEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.IDragEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.UI.Xaml.IDragEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.UI.Xaml.IDragEventArgs, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Windows.UI.Xaml.IDragEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_DataView(self: win32more.Windows.UI.Xaml.IDragEventArgs2) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_DragUIOverride(self: win32more.Windows.UI.Xaml.IDragEventArgs2) -> win32more.Windows.UI.Xaml.DragUIOverride: ...
    @winrt_mixinmethod
    def get_Modifiers(self: win32more.Windows.UI.Xaml.IDragEventArgs2) -> win32more.Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers: ...
    @winrt_mixinmethod
    def get_AcceptedOperation(self: win32more.Windows.UI.Xaml.IDragEventArgs2) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_AcceptedOperation(self: win32more.Windows.UI.Xaml.IDragEventArgs2, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Xaml.IDragEventArgs2) -> win32more.Windows.UI.Xaml.DragOperationDeferral: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: win32more.Windows.UI.Xaml.IDragEventArgs3) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    AcceptedOperation = property(get_AcceptedOperation, put_AcceptedOperation)
    AllowedOperations = property(get_AllowedOperations, None)
    Data = property(get_Data, put_Data)
    DataView = property(get_DataView, None)
    DragUIOverride = property(get_DragUIOverride, None)
    Handled = property(get_Handled, put_Handled)
    Modifiers = property(get_Modifiers, None)
class DragEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2ab1a205-1e73-4bcf-aabc-57b97e21961d}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.DragEventArgs) -> Void: ...
class DragOperationDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDragOperationDeferral
    _classid_ = 'Windows.UI.Xaml.DragOperationDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.Xaml.IDragOperationDeferral) -> Void: ...
class DragStartingEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.IDragStartingEventArgs
    _classid_ = 'Windows.UI.Xaml.DragStartingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def get_DragUI(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs) -> win32more.Windows.UI.Xaml.DragUI: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs) -> win32more.Windows.UI.Xaml.DragOperationDeferral: ...
    @winrt_mixinmethod
    def GetPosition(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs2) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_AllowedOperations(self: win32more.Windows.UI.Xaml.IDragStartingEventArgs2, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
    Cancel = property(get_Cancel, put_Cancel)
    Data = property(get_Data, None)
    DragUI = property(get_DragUI, None)
class DragUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDragUI
    _classid_ = 'Windows.UI.Xaml.DragUI'
    @winrt_mixinmethod
    def SetContentFromBitmapImage(self: win32more.Windows.UI.Xaml.IDragUI, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromBitmapImageWithAnchorPoint(self: win32more.Windows.UI.Xaml.IDragUI, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmap(self: win32more.Windows.UI.Xaml.IDragUI, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmapWithAnchorPoint(self: win32more.Windows.UI.Xaml.IDragUI, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromDataPackage(self: win32more.Windows.UI.Xaml.IDragUI) -> Void: ...
class DragUIOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDragUIOverride
    _classid_ = 'Windows.UI.Xaml.DragUIOverride'
    @winrt_mixinmethod
    def get_Caption(self: win32more.Windows.UI.Xaml.IDragUIOverride) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Caption(self: win32more.Windows.UI.Xaml.IDragUIOverride, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsContentVisible(self: win32more.Windows.UI.Xaml.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsContentVisible(self: win32more.Windows.UI.Xaml.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCaptionVisible(self: win32more.Windows.UI.Xaml.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCaptionVisible(self: win32more.Windows.UI.Xaml.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsGlyphVisible(self: win32more.Windows.UI.Xaml.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGlyphVisible(self: win32more.Windows.UI.Xaml.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.UI.Xaml.IDragUIOverride) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromBitmapImage(self: win32more.Windows.UI.Xaml.IDragUIOverride, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromBitmapImageWithAnchorPoint(self: win32more.Windows.UI.Xaml.IDragUIOverride, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmap(self: win32more.Windows.UI.Xaml.IDragUIOverride, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmapWithAnchorPoint(self: win32more.Windows.UI.Xaml.IDragUIOverride, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    Caption = property(get_Caption, put_Caption)
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class DropCompletedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.IDropCompletedEventArgs
    _classid_ = 'Windows.UI.Xaml.DropCompletedEventArgs'
    @winrt_mixinmethod
    def get_DropResult(self: win32more.Windows.UI.Xaml.IDropCompletedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    DropResult = property(get_DropResult, None)
class Duration(Structure):
    TimeSpan: win32more.Windows.Foundation.TimeSpan
    Type: win32more.Windows.UI.Xaml.DurationType
class _DurationHelper_Meta_(ComPtr.__class__):
    pass
class DurationHelper(ComPtr, metaclass=_DurationHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IDurationHelper
    _classid_ = 'Windows.UI.Xaml.DurationHelper'
    @winrt_classmethod
    def get_Automatic(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def get_Forever(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def Compare(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics, duration1: win32more.Windows.UI.Xaml.Duration, duration2: win32more.Windows.UI.Xaml.Duration) -> Int32: ...
    @winrt_classmethod
    def FromTimeSpan(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics, timeSpan: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def GetHasTimeSpan(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics, target: win32more.Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_classmethod
    def Add(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics, target: win32more.Windows.UI.Xaml.Duration, duration: win32more.Windows.UI.Xaml.Duration) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def Equals(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics, target: win32more.Windows.UI.Xaml.Duration, value: win32more.Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_classmethod
    def Subtract(cls: win32more.Windows.UI.Xaml.IDurationHelperStatics, target: win32more.Windows.UI.Xaml.Duration, duration: win32more.Windows.UI.Xaml.Duration) -> win32more.Windows.UI.Xaml.Duration: ...
    _DurationHelper_Meta_.Automatic = property(get_Automatic, None)
    _DurationHelper_Meta_.Forever = property(get_Forever, None)
class DurationType(Enum, Int32):
    Automatic = 0
    TimeSpan = 1
    Forever = 2
class EffectiveViewportChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IEffectiveViewportChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.EffectiveViewportChangedEventArgs'
    @winrt_mixinmethod
    def get_EffectiveViewport(self: win32more.Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_MaxViewport(self: win32more.Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_BringIntoViewDistanceX(self: win32more.Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_BringIntoViewDistanceY(self: win32more.Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> Double: ...
    BringIntoViewDistanceX = property(get_BringIntoViewDistanceX, None)
    BringIntoViewDistanceY = property(get_BringIntoViewDistanceY, None)
    EffectiveViewport = property(get_EffectiveViewport, None)
    MaxViewport = property(get_MaxViewport, None)
class ElementFactoryGetArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IElementFactoryGetArgs
    _classid_ = 'Windows.UI.Xaml.ElementFactoryGetArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.ElementFactoryGetArgs.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IElementFactoryGetArgsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ElementFactoryGetArgs: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.UI.Xaml.IElementFactoryGetArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.UI.Xaml.IElementFactoryGetArgs, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Xaml.IElementFactoryGetArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Parent(self: win32more.Windows.UI.Xaml.IElementFactoryGetArgs, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    Data = property(get_Data, put_Data)
    Parent = property(get_Parent, put_Parent)
class ElementFactoryRecycleArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IElementFactoryRecycleArgs
    _classid_ = 'Windows.UI.Xaml.ElementFactoryRecycleArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.ElementFactoryRecycleArgs.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IElementFactoryRecycleArgsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ElementFactoryRecycleArgs: ...
    @winrt_mixinmethod
    def get_Element(self: win32more.Windows.UI.Xaml.IElementFactoryRecycleArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Element(self: win32more.Windows.UI.Xaml.IElementFactoryRecycleArgs, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Xaml.IElementFactoryRecycleArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Parent(self: win32more.Windows.UI.Xaml.IElementFactoryRecycleArgs, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    Element = property(get_Element, put_Element)
    Parent = property(get_Parent, put_Parent)
class ElementHighContrastAdjustment(Enum, UInt32):
    None_ = 0
    Application = 2147483648
    Auto = 4294967295
class ElementSoundKind(Enum, Int32):
    Focus = 0
    Invoke = 1
    Show = 2
    Hide = 3
    MovePrevious = 4
    MoveNext = 5
    GoBack = 6
class ElementSoundMode(Enum, Int32):
    Default = 0
    FocusOnly = 1
    Off = 2
class _ElementSoundPlayer_Meta_(ComPtr.__class__):
    pass
class ElementSoundPlayer(ComPtr, metaclass=_ElementSoundPlayer_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IElementSoundPlayer
    _classid_ = 'Windows.UI.Xaml.ElementSoundPlayer'
    @winrt_classmethod
    def get_SpatialAudioMode(cls: win32more.Windows.UI.Xaml.IElementSoundPlayerStatics2) -> win32more.Windows.UI.Xaml.ElementSpatialAudioMode: ...
    @winrt_classmethod
    def put_SpatialAudioMode(cls: win32more.Windows.UI.Xaml.IElementSoundPlayerStatics2, value: win32more.Windows.UI.Xaml.ElementSpatialAudioMode) -> Void: ...
    @winrt_classmethod
    def get_Volume(cls: win32more.Windows.UI.Xaml.IElementSoundPlayerStatics) -> Double: ...
    @winrt_classmethod
    def put_Volume(cls: win32more.Windows.UI.Xaml.IElementSoundPlayerStatics, value: Double) -> Void: ...
    @winrt_classmethod
    def get_State(cls: win32more.Windows.UI.Xaml.IElementSoundPlayerStatics) -> win32more.Windows.UI.Xaml.ElementSoundPlayerState: ...
    @winrt_classmethod
    def put_State(cls: win32more.Windows.UI.Xaml.IElementSoundPlayerStatics, value: win32more.Windows.UI.Xaml.ElementSoundPlayerState) -> Void: ...
    @winrt_classmethod
    def Play(cls: win32more.Windows.UI.Xaml.IElementSoundPlayerStatics, sound: win32more.Windows.UI.Xaml.ElementSoundKind) -> Void: ...
    _ElementSoundPlayer_Meta_.SpatialAudioMode = property(get_SpatialAudioMode, put_SpatialAudioMode)
    _ElementSoundPlayer_Meta_.State = property(get_State, put_State)
    _ElementSoundPlayer_Meta_.Volume = property(get_Volume, put_Volume)
class ElementSoundPlayerState(Enum, Int32):
    Auto = 0
    Off = 1
    On = 2
class ElementSpatialAudioMode(Enum, Int32):
    Auto = 0
    Off = 1
    On = 2
class ElementTheme(Enum, Int32):
    Default = 0
    Light = 1
    Dark = 2
class EnteredBackgroundEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{93a956ae-1d7f-438b-b7b8-227d96b609c0}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.ApplicationModel.EnteredBackgroundEventArgs) -> Void: ...
class EventTrigger(ComPtr):
    extends: win32more.Windows.UI.Xaml.TriggerBase
    default_interface: win32more.Windows.UI.Xaml.IEventTrigger
    _classid_ = 'Windows.UI.Xaml.EventTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.EventTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.EventTrigger: ...
    @winrt_mixinmethod
    def get_RoutedEvent(self: win32more.Windows.UI.Xaml.IEventTrigger) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_mixinmethod
    def put_RoutedEvent(self: win32more.Windows.UI.Xaml.IEventTrigger, value: win32more.Windows.UI.Xaml.RoutedEvent) -> Void: ...
    @winrt_mixinmethod
    def get_Actions(self: win32more.Windows.UI.Xaml.IEventTrigger) -> win32more.Windows.UI.Xaml.TriggerActionCollection: ...
    Actions = property(get_Actions, None)
    RoutedEvent = property(get_RoutedEvent, put_RoutedEvent)
class ExceptionRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.IExceptionRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.ExceptionRoutedEventArgs'
    @winrt_mixinmethod
    def get_ErrorMessage(self: win32more.Windows.UI.Xaml.IExceptionRoutedEventArgs) -> WinRT_String: ...
    ErrorMessage = property(get_ErrorMessage, None)
class ExceptionRoutedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68e0e810-f6ea-42bc-855b-5d9b67e6a262}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.ExceptionRoutedEventArgs) -> Void: ...
class FlowDirection(Enum, Int32):
    LeftToRight = 0
    RightToLeft = 1
class FocusState(Enum, Int32):
    Unfocused = 0
    Pointer = 1
    Keyboard = 2
    Programmatic = 3
class FocusVisualKind(Enum, Int32):
    DottedLine = 0
    HighVisibility = 1
    Reveal = 2
class FontCapitals(Enum, Int32):
    Normal = 0
    AllSmallCaps = 1
    SmallCaps = 2
    AllPetiteCaps = 3
    PetiteCaps = 4
    Unicase = 5
    Titling = 6
class FontEastAsianLanguage(Enum, Int32):
    Normal = 0
    HojoKanji = 1
    Jis04 = 2
    Jis78 = 3
    Jis83 = 4
    Jis90 = 5
    NlcKanji = 6
    Simplified = 7
    Traditional = 8
    TraditionalNames = 9
class FontEastAsianWidths(Enum, Int32):
    Normal = 0
    Full = 1
    Half = 2
    Proportional = 3
    Quarter = 4
    Third = 5
class FontFraction(Enum, Int32):
    Normal = 0
    Stacked = 1
    Slashed = 2
class FontNumeralAlignment(Enum, Int32):
    Normal = 0
    Proportional = 1
    Tabular = 2
class FontNumeralStyle(Enum, Int32):
    Normal = 0
    Lining = 1
    OldStyle = 2
class FontVariants(Enum, Int32):
    Normal = 0
    Superscript = 1
    Subscript = 2
    Ordinal = 3
    Inferior = 4
    Ruby = 5
class _FrameworkElement_Meta_(ComPtr.__class__):
    pass
class FrameworkElement(ComPtr, metaclass=_FrameworkElement_Meta_):
    extends: win32more.Windows.UI.Xaml.UIElement
    default_interface: win32more.Windows.UI.Xaml.IFrameworkElement
    _classid_ = 'Windows.UI.Xaml.FrameworkElement'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.FrameworkElement.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IFrameworkElementFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.FrameworkElement: ...
    @winrt_mixinmethod
    def get_Triggers(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.TriggerCollection: ...
    @winrt_mixinmethod
    def get_Resources(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_mixinmethod
    def put_Resources(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ActualWidth(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def get_ActualHeight(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_Width(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_Height(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MinWidth(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MinWidth(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MaxWidth(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MaxWidth(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MinHeight(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MinHeight(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MaxHeight(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MaxHeight(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignment(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_mixinmethod
    def put_HorizontalAlignment(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignment(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_mixinmethod
    def put_VerticalAlignment(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_Margin(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_Margin(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_DataContext(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_DataContext(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_Style(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.Style: ...
    @winrt_mixinmethod
    def put_Style(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.UI.Xaml.Style) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_FlowDirection(self: win32more.Windows.UI.Xaml.IFrameworkElement) -> win32more.Windows.UI.Xaml.FlowDirection: ...
    @winrt_mixinmethod
    def put_FlowDirection(self: win32more.Windows.UI.Xaml.IFrameworkElement, value: win32more.Windows.UI.Xaml.FlowDirection) -> Void: ...
    @winrt_mixinmethod
    def add_Loaded(self: win32more.Windows.UI.Xaml.IFrameworkElement, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Loaded(self: win32more.Windows.UI.Xaml.IFrameworkElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Unloaded(self: win32more.Windows.UI.Xaml.IFrameworkElement, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Unloaded(self: win32more.Windows.UI.Xaml.IFrameworkElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SizeChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement, handler: win32more.Windows.UI.Xaml.SizeChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SizeChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LayoutUpdated(self: win32more.Windows.UI.Xaml.IFrameworkElement, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LayoutUpdated(self: win32more.Windows.UI.Xaml.IFrameworkElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindName(self: win32more.Windows.UI.Xaml.IFrameworkElement, name: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def SetBinding(self: win32more.Windows.UI.Xaml.IFrameworkElement, dp: win32more.Windows.UI.Xaml.DependencyProperty, binding: win32more.Windows.UI.Xaml.Data.BindingBase) -> Void: ...
    @winrt_mixinmethod
    def get_RequestedTheme(self: win32more.Windows.UI.Xaml.IFrameworkElement2) -> win32more.Windows.UI.Xaml.ElementTheme: ...
    @winrt_mixinmethod
    def put_RequestedTheme(self: win32more.Windows.UI.Xaml.IFrameworkElement2, value: win32more.Windows.UI.Xaml.ElementTheme) -> Void: ...
    @winrt_mixinmethod
    def add_DataContextChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.UI.Xaml.DataContextChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataContextChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetBindingExpression(self: win32more.Windows.UI.Xaml.IFrameworkElement2, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.UI.Xaml.Data.BindingExpression: ...
    @winrt_mixinmethod
    def add_Loading(self: win32more.Windows.UI.Xaml.IFrameworkElement3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Loading(self: win32more.Windows.UI.Xaml.IFrameworkElement3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllowFocusOnInteraction(self: win32more.Windows.UI.Xaml.IFrameworkElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusOnInteraction(self: win32more.Windows.UI.Xaml.IFrameworkElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualMargin(self: win32more.Windows.UI.Xaml.IFrameworkElement4) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_FocusVisualMargin(self: win32more.Windows.UI.Xaml.IFrameworkElement4, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualSecondaryThickness(self: win32more.Windows.UI.Xaml.IFrameworkElement4) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_FocusVisualSecondaryThickness(self: win32more.Windows.UI.Xaml.IFrameworkElement4, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualPrimaryThickness(self: win32more.Windows.UI.Xaml.IFrameworkElement4) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_FocusVisualPrimaryThickness(self: win32more.Windows.UI.Xaml.IFrameworkElement4, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualSecondaryBrush(self: win32more.Windows.UI.Xaml.IFrameworkElement4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusVisualSecondaryBrush(self: win32more.Windows.UI.Xaml.IFrameworkElement4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualPrimaryBrush(self: win32more.Windows.UI.Xaml.IFrameworkElement4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusVisualPrimaryBrush(self: win32more.Windows.UI.Xaml.IFrameworkElement4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_AllowFocusWhenDisabled(self: win32more.Windows.UI.Xaml.IFrameworkElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusWhenDisabled(self: win32more.Windows.UI.Xaml.IFrameworkElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ActualTheme(self: win32more.Windows.UI.Xaml.IFrameworkElement6) -> win32more.Windows.UI.Xaml.ElementTheme: ...
    @winrt_mixinmethod
    def add_ActualThemeChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement6, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualThemeChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsLoaded(self: win32more.Windows.UI.Xaml.IFrameworkElement7) -> Boolean: ...
    @winrt_mixinmethod
    def add_EffectiveViewportChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement7, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.UI.Xaml.EffectiveViewportChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EffectiveViewportChanged(self: win32more.Windows.UI.Xaml.IFrameworkElement7, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def InvalidateViewport(self: win32more.Windows.UI.Xaml.IFrameworkElementProtected7) -> Void: ...
    @winrt_mixinmethod
    def MeasureOverride(self: win32more.Windows.UI.Xaml.IFrameworkElementOverrides, availableSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def ArrangeOverride(self: win32more.Windows.UI.Xaml.IFrameworkElementOverrides, finalSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def OnApplyTemplate(self: win32more.Windows.UI.Xaml.IFrameworkElementOverrides) -> Void: ...
    @winrt_mixinmethod
    def GoToElementStateCore(self: win32more.Windows.UI.Xaml.IFrameworkElementOverrides2, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
    @winrt_classmethod
    def get_ActualThemeProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics6) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def DeferTree(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_AllowFocusOnInteractionProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualMarginProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualSecondaryThicknessProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualPrimaryThicknessProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualSecondaryBrushProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualPrimaryBrushProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowFocusWhenDisabledProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RequestedThemeProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TagProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LanguageProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ActualWidthProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ActualHeightProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_WidthProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HeightProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinWidthProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxWidthProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinHeightProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxHeightProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalAlignmentProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalAlignmentProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MarginProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_NameProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DataContextProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StyleProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FlowDirectionProperty(cls: win32more.Windows.UI.Xaml.IFrameworkElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ActualHeight = property(get_ActualHeight, None)
    ActualTheme = property(get_ActualTheme, None)
    ActualWidth = property(get_ActualWidth, None)
    AllowFocusOnInteraction = property(get_AllowFocusOnInteraction, put_AllowFocusOnInteraction)
    AllowFocusWhenDisabled = property(get_AllowFocusWhenDisabled, put_AllowFocusWhenDisabled)
    BaseUri = property(get_BaseUri, None)
    DataContext = property(get_DataContext, put_DataContext)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    FocusVisualMargin = property(get_FocusVisualMargin, put_FocusVisualMargin)
    FocusVisualPrimaryBrush = property(get_FocusVisualPrimaryBrush, put_FocusVisualPrimaryBrush)
    FocusVisualPrimaryThickness = property(get_FocusVisualPrimaryThickness, put_FocusVisualPrimaryThickness)
    FocusVisualSecondaryBrush = property(get_FocusVisualSecondaryBrush, put_FocusVisualSecondaryBrush)
    FocusVisualSecondaryThickness = property(get_FocusVisualSecondaryThickness, put_FocusVisualSecondaryThickness)
    Height = property(get_Height, put_Height)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    IsLoaded = property(get_IsLoaded, None)
    Language = property(get_Language, put_Language)
    Margin = property(get_Margin, put_Margin)
    MaxHeight = property(get_MaxHeight, put_MaxHeight)
    MaxWidth = property(get_MaxWidth, put_MaxWidth)
    MinHeight = property(get_MinHeight, put_MinHeight)
    MinWidth = property(get_MinWidth, put_MinWidth)
    Name = property(get_Name, put_Name)
    Parent = property(get_Parent, None)
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
    Resources = property(get_Resources, put_Resources)
    Style = property(get_Style, put_Style)
    Tag = property(get_Tag, put_Tag)
    Triggers = property(get_Triggers, None)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    Width = property(get_Width, put_Width)
    _FrameworkElement_Meta_.ActualHeightProperty = property(get_ActualHeightProperty, None)
    _FrameworkElement_Meta_.ActualThemeProperty = property(get_ActualThemeProperty, None)
    _FrameworkElement_Meta_.ActualWidthProperty = property(get_ActualWidthProperty, None)
    _FrameworkElement_Meta_.AllowFocusOnInteractionProperty = property(get_AllowFocusOnInteractionProperty, None)
    _FrameworkElement_Meta_.AllowFocusWhenDisabledProperty = property(get_AllowFocusWhenDisabledProperty, None)
    _FrameworkElement_Meta_.DataContextProperty = property(get_DataContextProperty, None)
    _FrameworkElement_Meta_.FlowDirectionProperty = property(get_FlowDirectionProperty, None)
    _FrameworkElement_Meta_.FocusVisualMarginProperty = property(get_FocusVisualMarginProperty, None)
    _FrameworkElement_Meta_.FocusVisualPrimaryBrushProperty = property(get_FocusVisualPrimaryBrushProperty, None)
    _FrameworkElement_Meta_.FocusVisualPrimaryThicknessProperty = property(get_FocusVisualPrimaryThicknessProperty, None)
    _FrameworkElement_Meta_.FocusVisualSecondaryBrushProperty = property(get_FocusVisualSecondaryBrushProperty, None)
    _FrameworkElement_Meta_.FocusVisualSecondaryThicknessProperty = property(get_FocusVisualSecondaryThicknessProperty, None)
    _FrameworkElement_Meta_.HeightProperty = property(get_HeightProperty, None)
    _FrameworkElement_Meta_.HorizontalAlignmentProperty = property(get_HorizontalAlignmentProperty, None)
    _FrameworkElement_Meta_.LanguageProperty = property(get_LanguageProperty, None)
    _FrameworkElement_Meta_.MarginProperty = property(get_MarginProperty, None)
    _FrameworkElement_Meta_.MaxHeightProperty = property(get_MaxHeightProperty, None)
    _FrameworkElement_Meta_.MaxWidthProperty = property(get_MaxWidthProperty, None)
    _FrameworkElement_Meta_.MinHeightProperty = property(get_MinHeightProperty, None)
    _FrameworkElement_Meta_.MinWidthProperty = property(get_MinWidthProperty, None)
    _FrameworkElement_Meta_.NameProperty = property(get_NameProperty, None)
    _FrameworkElement_Meta_.RequestedThemeProperty = property(get_RequestedThemeProperty, None)
    _FrameworkElement_Meta_.StyleProperty = property(get_StyleProperty, None)
    _FrameworkElement_Meta_.TagProperty = property(get_TagProperty, None)
    _FrameworkElement_Meta_.VerticalAlignmentProperty = property(get_VerticalAlignmentProperty, None)
    _FrameworkElement_Meta_.WidthProperty = property(get_WidthProperty, None)
    Loaded = event()
    Unloaded = event()
    SizeChanged = event()
    LayoutUpdated = event()
    DataContextChanged = event()
    Loading = event()
    ActualThemeChanged = event()
    EffectiveViewportChanged = event()
class FrameworkTemplate(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IFrameworkTemplate
    _classid_ = 'Windows.UI.Xaml.FrameworkTemplate'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.FrameworkTemplate.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IFrameworkTemplateFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.FrameworkTemplate: ...
class FrameworkView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IFrameworkView
    _classid_ = 'Windows.UI.Xaml.FrameworkView'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.FrameworkView.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.FrameworkView: ...
    @winrt_mixinmethod
    def Initialize(self: win32more.Windows.ApplicationModel.Core.IFrameworkView, applicationView: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> Void: ...
    @winrt_mixinmethod
    def SetWindow(self: win32more.Windows.ApplicationModel.Core.IFrameworkView, window: win32more.Windows.UI.Core.CoreWindow) -> Void: ...
    @winrt_mixinmethod
    def Load(self: win32more.Windows.ApplicationModel.Core.IFrameworkView, entryPoint: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Run(self: win32more.Windows.ApplicationModel.Core.IFrameworkView) -> Void: ...
    @winrt_mixinmethod
    def Uninitialize(self: win32more.Windows.ApplicationModel.Core.IFrameworkView) -> Void: ...
class FrameworkViewSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IFrameworkViewSource
    _classid_ = 'Windows.UI.Xaml.FrameworkViewSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.FrameworkViewSource.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.FrameworkViewSource: ...
    @winrt_mixinmethod
    def CreateView(self: win32more.Windows.ApplicationModel.Core.IFrameworkViewSource) -> win32more.Windows.ApplicationModel.Core.IFrameworkView: ...
class GridLength(Structure):
    Value: Double
    GridUnitType: win32more.Windows.UI.Xaml.GridUnitType
class _GridLengthHelper_Meta_(ComPtr.__class__):
    pass
class GridLengthHelper(ComPtr, metaclass=_GridLengthHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IGridLengthHelper
    _classid_ = 'Windows.UI.Xaml.GridLengthHelper'
    @winrt_classmethod
    def get_Auto(cls: win32more.Windows.UI.Xaml.IGridLengthHelperStatics) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_classmethod
    def FromPixels(cls: win32more.Windows.UI.Xaml.IGridLengthHelperStatics, pixels: Double) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_classmethod
    def FromValueAndType(cls: win32more.Windows.UI.Xaml.IGridLengthHelperStatics, value: Double, type: win32more.Windows.UI.Xaml.GridUnitType) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_classmethod
    def GetIsAbsolute(cls: win32more.Windows.UI.Xaml.IGridLengthHelperStatics, target: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_classmethod
    def GetIsAuto(cls: win32more.Windows.UI.Xaml.IGridLengthHelperStatics, target: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_classmethod
    def GetIsStar(cls: win32more.Windows.UI.Xaml.IGridLengthHelperStatics, target: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: win32more.Windows.UI.Xaml.IGridLengthHelperStatics, target: win32more.Windows.UI.Xaml.GridLength, value: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    _GridLengthHelper_Meta_.Auto = property(get_Auto, None)
class GridUnitType(Enum, Int32):
    Auto = 0
    Pixel = 1
    Star = 2
class HorizontalAlignment(Enum, Int32):
    Left = 0
    Center = 1
    Right = 2
    Stretch = 3
class IAdaptiveTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IAdaptiveTrigger'
    _iid_ = Guid('{a5f04119-0cd9-49f1-a23f-44e547ab9f1a}')
    @winrt_commethod(6)
    def get_MinWindowWidth(self) -> Double: ...
    @winrt_commethod(7)
    def put_MinWindowWidth(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_MinWindowHeight(self) -> Double: ...
    @winrt_commethod(9)
    def put_MinWindowHeight(self, value: Double) -> Void: ...
    MinWindowHeight = property(get_MinWindowHeight, put_MinWindowHeight)
    MinWindowWidth = property(get_MinWindowWidth, put_MinWindowWidth)
class IAdaptiveTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IAdaptiveTriggerFactory'
    _iid_ = Guid('{c966d482-5aeb-4841-9247-c1a0bdd6f59f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.AdaptiveTrigger: ...
class IAdaptiveTriggerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IAdaptiveTriggerStatics'
    _iid_ = Guid('{b92e29ea-1615-4350-9c3b-92b2986bf444}')
    @winrt_commethod(6)
    def get_MinWindowWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MinWindowHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MinWindowHeightProperty = property(get_MinWindowHeightProperty, None)
    MinWindowWidthProperty = property(get_MinWindowWidthProperty, None)
class IApplication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplication'
    _iid_ = Guid('{74b861a1-7487-46a9-9a6e-c78b512726c5}')
    @winrt_commethod(6)
    def get_Resources(self) -> win32more.Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_commethod(7)
    def put_Resources(self, value: win32more.Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_commethod(8)
    def get_DebugSettings(self) -> win32more.Windows.UI.Xaml.DebugSettings: ...
    @winrt_commethod(9)
    def get_RequestedTheme(self) -> win32more.Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_commethod(10)
    def put_RequestedTheme(self, value: win32more.Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_commethod(11)
    def add_UnhandledException(self, handler: win32more.Windows.UI.Xaml.UnhandledExceptionEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_UnhandledException(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Suspending(self, handler: win32more.Windows.UI.Xaml.SuspendingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Suspending(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_Resuming(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Resuming(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def Exit(self) -> Void: ...
    DebugSettings = property(get_DebugSettings, None)
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
    Resources = property(get_Resources, put_Resources)
    UnhandledException = event()
    Suspending = event()
    Resuming = event()
class IApplication2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplication2'
    _iid_ = Guid('{019104be-522a-5904-f52f-de72010429e0}')
    @winrt_commethod(6)
    def get_FocusVisualKind(self) -> win32more.Windows.UI.Xaml.FocusVisualKind: ...
    @winrt_commethod(7)
    def put_FocusVisualKind(self, value: win32more.Windows.UI.Xaml.FocusVisualKind) -> Void: ...
    @winrt_commethod(8)
    def get_RequiresPointerMode(self) -> win32more.Windows.UI.Xaml.ApplicationRequiresPointerMode: ...
    @winrt_commethod(9)
    def put_RequiresPointerMode(self, value: win32more.Windows.UI.Xaml.ApplicationRequiresPointerMode) -> Void: ...
    @winrt_commethod(10)
    def add_LeavingBackground(self, handler: win32more.Windows.UI.Xaml.LeavingBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LeavingBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnteredBackground(self, handler: win32more.Windows.UI.Xaml.EnteredBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnteredBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    FocusVisualKind = property(get_FocusVisualKind, put_FocusVisualKind)
    RequiresPointerMode = property(get_RequiresPointerMode, put_RequiresPointerMode)
    LeavingBackground = event()
    EnteredBackground = event()
class IApplication3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplication3'
    _iid_ = Guid('{b775ad7c-18b8-45ca-a1b0-dc483e4b1028}')
    @winrt_commethod(6)
    def get_HighContrastAdjustment(self) -> win32more.Windows.UI.Xaml.ApplicationHighContrastAdjustment: ...
    @winrt_commethod(7)
    def put_HighContrastAdjustment(self, value: win32more.Windows.UI.Xaml.ApplicationHighContrastAdjustment) -> Void: ...
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
class IApplicationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationFactory'
    _iid_ = Guid('{93bbe361-be5a-4ee3-b4a3-95118dc97a89}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Application: ...
class IApplicationInitializationCallbackParams(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationInitializationCallbackParams'
    _iid_ = Guid('{751b792e-5772-4488-8b87-f547faa64474}')
class IApplicationOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationOverrides'
    _iid_ = Guid('{25f99ff7-9347-459a-9fac-b2d0e11c1a0f}')
    @winrt_commethod(6)
    def OnActivated(self, args: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Void: ...
    @winrt_commethod(7)
    def OnLaunched(self, args: win32more.Windows.ApplicationModel.Activation.LaunchActivatedEventArgs) -> Void: ...
    @winrt_commethod(8)
    def OnFileActivated(self, args: win32more.Windows.ApplicationModel.Activation.FileActivatedEventArgs) -> Void: ...
    @winrt_commethod(9)
    def OnSearchActivated(self, args: win32more.Windows.ApplicationModel.Activation.SearchActivatedEventArgs) -> Void: ...
    @winrt_commethod(10)
    def OnShareTargetActivated(self, args: win32more.Windows.ApplicationModel.Activation.ShareTargetActivatedEventArgs) -> Void: ...
    @winrt_commethod(11)
    def OnFileOpenPickerActivated(self, args: win32more.Windows.ApplicationModel.Activation.FileOpenPickerActivatedEventArgs) -> Void: ...
    @winrt_commethod(12)
    def OnFileSavePickerActivated(self, args: win32more.Windows.ApplicationModel.Activation.FileSavePickerActivatedEventArgs) -> Void: ...
    @winrt_commethod(13)
    def OnCachedFileUpdaterActivated(self, args: win32more.Windows.ApplicationModel.Activation.CachedFileUpdaterActivatedEventArgs) -> Void: ...
    @winrt_commethod(14)
    def OnWindowCreated(self, args: win32more.Windows.UI.Xaml.WindowCreatedEventArgs) -> Void: ...
class IApplicationOverrides2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationOverrides2'
    _iid_ = Guid('{db5cd2b9-d3b4-558c-c64e-0434fd1bd889}')
    @winrt_commethod(6)
    def OnBackgroundActivated(self, args: win32more.Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs) -> Void: ...
class IApplicationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationStatics'
    _iid_ = Guid('{06499997-f7b4-45fe-b763-7577d1d3cb4a}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.UI.Xaml.Application: ...
    @winrt_commethod(7)
    def Start(self, callback: win32more.Windows.UI.Xaml.ApplicationInitializationCallback) -> Void: ...
    @winrt_commethod(8)
    def LoadComponent(self, component: win32more.Windows.Win32.System.WinRT.IInspectable, resourceLocator: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(9)
    def LoadComponentWithResourceLocation(self, component: win32more.Windows.Win32.System.WinRT.IInspectable, resourceLocator: win32more.Windows.Foundation.Uri, componentResourceLocation: win32more.Windows.UI.Xaml.Controls.Primitives.ComponentResourceLocation) -> Void: ...
    Current = property(get_Current, None)
class IBindingFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBindingFailedEventArgs'
    _iid_ = Guid('{32c1d013-4dbd-446d-bbb8-0de35048a449}')
    @winrt_commethod(6)
    def get_Message(self) -> WinRT_String: ...
    Message = property(get_Message, None)
class IBringIntoViewOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBringIntoViewOptions'
    _iid_ = Guid('{19bdd1b5-c7cb-46d9-a4dd-a1bbe83ef2fb}')
    @winrt_commethod(6)
    def get_AnimationDesired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AnimationDesired(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TargetRect(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_TargetRect(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    TargetRect = property(get_TargetRect, put_TargetRect)
class IBringIntoViewOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBringIntoViewOptions2'
    _iid_ = Guid('{e855e08e-64b6-1211-bddb-1fddbb6e8231}')
    @winrt_commethod(6)
    def get_HorizontalAlignmentRatio(self) -> Double: ...
    @winrt_commethod(7)
    def put_HorizontalAlignmentRatio(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_VerticalAlignmentRatio(self) -> Double: ...
    @winrt_commethod(9)
    def put_VerticalAlignmentRatio(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(11)
    def put_HorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_VerticalOffset(self) -> Double: ...
    @winrt_commethod(13)
    def put_VerticalOffset(self, value: Double) -> Void: ...
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
class IBringIntoViewRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBringIntoViewRequestedEventArgs'
    _iid_ = Guid('{0e629ec4-2206-4c8b-94ae-bdb66a4ebfd1}')
    @winrt_commethod(6)
    def get_TargetElement(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_TargetElement(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_AnimationDesired(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AnimationDesired(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_TargetRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_TargetRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(12)
    def get_HorizontalAlignmentRatio(self) -> Double: ...
    @winrt_commethod(13)
    def get_VerticalAlignmentRatio(self) -> Double: ...
    @winrt_commethod(14)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(15)
    def put_HorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_VerticalOffset(self) -> Double: ...
    @winrt_commethod(17)
    def put_VerticalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_Handled(self, value: Boolean) -> Void: ...
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    Handled = property(get_Handled, put_Handled)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, None)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    TargetElement = property(get_TargetElement, put_TargetElement)
    TargetRect = property(get_TargetRect, put_TargetRect)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, None)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
class IBrushTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBrushTransition'
    _iid_ = Guid('{1116972c-9dad-5429-a7dd-b2b7d061ab8e}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class IBrushTransitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBrushTransitionFactory'
    _iid_ = Guid('{3dbe7368-13d4-510c-a215-7539f4787b52}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.BrushTransition: ...
class IColorPaletteResources(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IColorPaletteResources'
    _iid_ = Guid('{258088c4-aef2-5d3f-833b-c36db6278ed9}')
    @winrt_commethod(6)
    def get_AltHigh(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(7)
    def put_AltHigh(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(8)
    def get_AltLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(9)
    def put_AltLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(10)
    def get_AltMedium(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(11)
    def put_AltMedium(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(12)
    def get_AltMediumHigh(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(13)
    def put_AltMediumHigh(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(14)
    def get_AltMediumLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(15)
    def put_AltMediumLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(16)
    def get_BaseHigh(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(17)
    def put_BaseHigh(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(18)
    def get_BaseLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(19)
    def put_BaseLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(20)
    def get_BaseMedium(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(21)
    def put_BaseMedium(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(22)
    def get_BaseMediumHigh(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(23)
    def put_BaseMediumHigh(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(24)
    def get_BaseMediumLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(25)
    def put_BaseMediumLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(26)
    def get_ChromeAltLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(27)
    def put_ChromeAltLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(28)
    def get_ChromeBlackHigh(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(29)
    def put_ChromeBlackHigh(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(30)
    def get_ChromeBlackLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(31)
    def put_ChromeBlackLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(32)
    def get_ChromeBlackMediumLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(33)
    def put_ChromeBlackMediumLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(34)
    def get_ChromeBlackMedium(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(35)
    def put_ChromeBlackMedium(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(36)
    def get_ChromeDisabledHigh(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(37)
    def put_ChromeDisabledHigh(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(38)
    def get_ChromeDisabledLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(39)
    def put_ChromeDisabledLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(40)
    def get_ChromeHigh(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(41)
    def put_ChromeHigh(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(42)
    def get_ChromeLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(43)
    def put_ChromeLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(44)
    def get_ChromeMedium(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(45)
    def put_ChromeMedium(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(46)
    def get_ChromeMediumLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(47)
    def put_ChromeMediumLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(48)
    def get_ChromeWhite(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(49)
    def put_ChromeWhite(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(50)
    def get_ChromeGray(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(51)
    def put_ChromeGray(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(52)
    def get_ListLow(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(53)
    def put_ListLow(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(54)
    def get_ListMedium(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(55)
    def put_ListMedium(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(56)
    def get_ErrorText(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(57)
    def put_ErrorText(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(58)
    def get_Accent(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(59)
    def put_Accent(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    Accent = property(get_Accent, put_Accent)
    AltHigh = property(get_AltHigh, put_AltHigh)
    AltLow = property(get_AltLow, put_AltLow)
    AltMedium = property(get_AltMedium, put_AltMedium)
    AltMediumHigh = property(get_AltMediumHigh, put_AltMediumHigh)
    AltMediumLow = property(get_AltMediumLow, put_AltMediumLow)
    BaseHigh = property(get_BaseHigh, put_BaseHigh)
    BaseLow = property(get_BaseLow, put_BaseLow)
    BaseMedium = property(get_BaseMedium, put_BaseMedium)
    BaseMediumHigh = property(get_BaseMediumHigh, put_BaseMediumHigh)
    BaseMediumLow = property(get_BaseMediumLow, put_BaseMediumLow)
    ChromeAltLow = property(get_ChromeAltLow, put_ChromeAltLow)
    ChromeBlackHigh = property(get_ChromeBlackHigh, put_ChromeBlackHigh)
    ChromeBlackLow = property(get_ChromeBlackLow, put_ChromeBlackLow)
    ChromeBlackMedium = property(get_ChromeBlackMedium, put_ChromeBlackMedium)
    ChromeBlackMediumLow = property(get_ChromeBlackMediumLow, put_ChromeBlackMediumLow)
    ChromeDisabledHigh = property(get_ChromeDisabledHigh, put_ChromeDisabledHigh)
    ChromeDisabledLow = property(get_ChromeDisabledLow, put_ChromeDisabledLow)
    ChromeGray = property(get_ChromeGray, put_ChromeGray)
    ChromeHigh = property(get_ChromeHigh, put_ChromeHigh)
    ChromeLow = property(get_ChromeLow, put_ChromeLow)
    ChromeMedium = property(get_ChromeMedium, put_ChromeMedium)
    ChromeMediumLow = property(get_ChromeMediumLow, put_ChromeMediumLow)
    ChromeWhite = property(get_ChromeWhite, put_ChromeWhite)
    ErrorText = property(get_ErrorText, put_ErrorText)
    ListLow = property(get_ListLow, put_ListLow)
    ListMedium = property(get_ListMedium, put_ListMedium)
class IColorPaletteResourcesFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IColorPaletteResourcesFactory'
    _iid_ = Guid('{a57f0783-1876-5cc0-8ea5-bc77b17e0f7e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ColorPaletteResources: ...
class ICornerRadiusHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ICornerRadiusHelper'
    _iid_ = Guid('{fd7be182-1cdb-4288-b8c8-85ee79297bfc}')
class ICornerRadiusHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ICornerRadiusHelperStatics'
    _iid_ = Guid('{f4a1f659-d4d4-451f-a387-d6bf4b2451d4}')
    @winrt_commethod(6)
    def FromRadii(self, topLeft: Double, topRight: Double, bottomRight: Double, bottomLeft: Double) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_commethod(7)
    def FromUniformRadius(self, uniformRadius: Double) -> win32more.Windows.UI.Xaml.CornerRadius: ...
class IDataContextChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataContextChangedEventArgs'
    _iid_ = Guid('{7da68e21-0b8f-4f9f-a143-f8e7780136a2}')
    @winrt_commethod(6)
    def get_NewValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    NewValue = property(get_NewValue, None)
class IDataTemplate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplate'
    _iid_ = Guid('{9910aec7-8ab5-4118-9bc6-09f45a35073d}')
    @winrt_commethod(6)
    def LoadContent(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
class IDataTemplateExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateExtension'
    _iid_ = Guid('{595e9547-cdff-4b92-b773-ab396878f353}')
    @winrt_commethod(6)
    def ResetTemplate(self) -> Void: ...
    @winrt_commethod(7)
    def ProcessBinding(self, phase: UInt32) -> Boolean: ...
    @winrt_commethod(8)
    def ProcessBindings(self, arg: win32more.Windows.UI.Xaml.Controls.ContainerContentChangingEventArgs) -> Int32: ...
class IDataTemplateFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateFactory'
    _iid_ = Guid('{51ed9d7e-2b53-475b-9c88-0c1832c8351a}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DataTemplate: ...
class IDataTemplateKey(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateKey'
    _iid_ = Guid('{873b6c28-cceb-4b61-86fa-b2cec39cc2fa}')
    @winrt_commethod(6)
    def get_DataType(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_DataType(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    DataType = property(get_DataType, put_DataType)
class IDataTemplateKeyFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateKeyFactory'
    _iid_ = Guid('{e96b2959-d982-4152-91cb-de0e4dfd7693}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DataTemplateKey: ...
    @winrt_commethod(7)
    def CreateInstanceWithType(self, dataType: win32more.Windows.Win32.System.WinRT.IInspectable, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DataTemplateKey: ...
class IDataTemplateStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateStatics2'
    _iid_ = Guid('{8af77d73-aa01-471e-bedd-8bad86219b77}')
    @winrt_commethod(6)
    def get_ExtensionInstanceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetExtensionInstance(self, element: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.UI.Xaml.IDataTemplateExtension: ...
    @winrt_commethod(8)
    def SetExtensionInstance(self, element: win32more.Windows.UI.Xaml.FrameworkElement, value: win32more.Windows.UI.Xaml.IDataTemplateExtension) -> Void: ...
    ExtensionInstanceProperty = property(get_ExtensionInstanceProperty, None)
class IDebugSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDebugSettings'
    _iid_ = Guid('{3d451f98-c6a7-4d17-8398-d83a067183d8}')
    @winrt_commethod(6)
    def get_EnableFrameRateCounter(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_EnableFrameRateCounter(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsBindingTracingEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsBindingTracingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsOverdrawHeatMapEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsOverdrawHeatMapEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def add_BindingFailed(self, handler: win32more.Windows.UI.Xaml.BindingFailedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_BindingFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    EnableFrameRateCounter = property(get_EnableFrameRateCounter, put_EnableFrameRateCounter)
    IsBindingTracingEnabled = property(get_IsBindingTracingEnabled, put_IsBindingTracingEnabled)
    IsOverdrawHeatMapEnabled = property(get_IsOverdrawHeatMapEnabled, put_IsOverdrawHeatMapEnabled)
    BindingFailed = event()
class IDebugSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDebugSettings2'
    _iid_ = Guid('{48d37585-e1a6-469b-83c8-30825037119e}')
    @winrt_commethod(6)
    def get_EnableRedrawRegions(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_EnableRedrawRegions(self, value: Boolean) -> Void: ...
    EnableRedrawRegions = property(get_EnableRedrawRegions, put_EnableRedrawRegions)
class IDebugSettings3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDebugSettings3'
    _iid_ = Guid('{e6bb5022-0625-479f-8e32-4b583d73b7ac}')
    @winrt_commethod(6)
    def get_IsTextPerformanceVisualizationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsTextPerformanceVisualizationEnabled(self, value: Boolean) -> Void: ...
    IsTextPerformanceVisualizationEnabled = property(get_IsTextPerformanceVisualizationEnabled, put_IsTextPerformanceVisualizationEnabled)
class IDebugSettings4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDebugSettings4'
    _iid_ = Guid('{c9001e45-e824-5a5f-866c-e20cec88a8fc}')
    @winrt_commethod(6)
    def get_FailFastOnErrors(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_FailFastOnErrors(self, value: Boolean) -> Void: ...
    FailFastOnErrors = property(get_FailFastOnErrors, put_FailFastOnErrors)
class IDependencyObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObject'
    _iid_ = Guid('{5c526665-f60e-4912-af59-5fe0680f089d}')
    @winrt_commethod(6)
    def GetValue(self, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def SetValue(self, dp: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def ClearValue(self, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_commethod(9)
    def ReadLocalValue(self, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(10)
    def GetAnimationBaseValue(self, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def get_Dispatcher(self) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    Dispatcher = property(get_Dispatcher, None)
class IDependencyObject2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObject2'
    _iid_ = Guid('{29fed85d-3d22-43a1-add0-17027c08b212}')
    @winrt_commethod(6)
    def RegisterPropertyChangedCallback(self, dp: win32more.Windows.UI.Xaml.DependencyProperty, callback: win32more.Windows.UI.Xaml.DependencyPropertyChangedCallback) -> Int64: ...
    @winrt_commethod(7)
    def UnregisterPropertyChangedCallback(self, dp: win32more.Windows.UI.Xaml.DependencyProperty, token: Int64) -> Void: ...
class IDependencyObjectCollectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObjectCollectionFactory'
    _iid_ = Guid('{051e79ff-b3a8-49ee-b5af-ac8f68b649e4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DependencyObjectCollection: ...
class IDependencyObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObjectFactory'
    _iid_ = Guid('{9a03af92-7d8a-4937-884f-ecf34fe02acb}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DependencyObject: ...
class IDependencyProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyProperty'
    _iid_ = Guid('{85b13970-9bc4-4e96-acf1-30c8fd3d55c8}')
    @winrt_commethod(6)
    def GetMetadata(self, forType: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
class IDependencyPropertyChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyPropertyChangedEventArgs'
    _iid_ = Guid('{81212c2b-24d0-4957-abc3-224470a93a4e}')
    @winrt_commethod(6)
    def get_Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OldValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def get_NewValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    NewValue = property(get_NewValue, None)
    OldValue = property(get_OldValue, None)
    Property = property(get_Property, None)
class IDependencyPropertyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyPropertyStatics'
    _iid_ = Guid('{49e5f28f-8259-4d5c-aae0-83d56dbb68d9}')
    @winrt_commethod(6)
    def get_UnsetValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def Register(self, name: WinRT_String, propertyType: win32more.Windows.UI.Xaml.Interop.TypeName, ownerType: win32more.Windows.UI.Xaml.Interop.TypeName, typeMetadata: win32more.Windows.UI.Xaml.PropertyMetadata) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def RegisterAttached(self, name: WinRT_String, propertyType: win32more.Windows.UI.Xaml.Interop.TypeName, ownerType: win32more.Windows.UI.Xaml.Interop.TypeName, defaultMetadata: win32more.Windows.UI.Xaml.PropertyMetadata) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    UnsetValue = property(get_UnsetValue, None)
class IDispatcherTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDispatcherTimer'
    _iid_ = Guid('{d160ce46-cd22-4f5f-8c97-40e61da3e2dc}')
    @winrt_commethod(6)
    def get_Interval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Interval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def add_Tick(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Tick(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    @winrt_commethod(12)
    def Stop(self) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsEnabled = property(get_IsEnabled, None)
    Tick = event()
class IDispatcherTimerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDispatcherTimerFactory'
    _iid_ = Guid('{e9961e6e-3626-403a-afe0-040d58165632}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.DispatcherTimer: ...
class IDragEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragEventArgs'
    _iid_ = Guid('{b440c7c3-02b4-4980-9342-25dae1c0f188}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(9)
    def put_Data(self, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_commethod(10)
    def GetPosition(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Data = property(get_Data, put_Data)
    Handled = property(get_Handled, put_Handled)
class IDragEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragEventArgs2'
    _iid_ = Guid('{26336658-2917-411d-bfc3-2f22471cbbe7}')
    @winrt_commethod(6)
    def get_DataView(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_DragUIOverride(self) -> win32more.Windows.UI.Xaml.DragUIOverride: ...
    @winrt_commethod(8)
    def get_Modifiers(self) -> win32more.Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers: ...
    @winrt_commethod(9)
    def get_AcceptedOperation(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(10)
    def put_AcceptedOperation(self, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.UI.Xaml.DragOperationDeferral: ...
    AcceptedOperation = property(get_AcceptedOperation, put_AcceptedOperation)
    DataView = property(get_DataView, None)
    DragUIOverride = property(get_DragUIOverride, None)
    Modifiers = property(get_Modifiers, None)
class IDragEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragEventArgs3'
    _iid_ = Guid('{d04fc3c6-8119-427a-8152-5f9550cc0416}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    AllowedOperations = property(get_AllowedOperations, None)
class IDragOperationDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragOperationDeferral'
    _iid_ = Guid('{ba73ecba-1b73-4086-b3d3-c223beea1633}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDragStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragStartingEventArgs'
    _iid_ = Guid('{6800d3fa-90b8-46f9-8e30-5ac25f73f0f9}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(9)
    def get_DragUI(self) -> win32more.Windows.UI.Xaml.DragUI: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.UI.Xaml.DragOperationDeferral: ...
    @winrt_commethod(11)
    def GetPosition(self, relativeTo: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Point: ...
    Cancel = property(get_Cancel, put_Cancel)
    Data = property(get_Data, None)
    DragUI = property(get_DragUI, None)
class IDragStartingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragStartingEventArgs2'
    _iid_ = Guid('{d855e08e-44b6-4211-bd0b-7fddbb6e8231}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(7)
    def put_AllowedOperations(self, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
class IDragUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragUI'
    _iid_ = Guid('{2d9bd838-7c60-4842-9170-346fe10a226a}')
    @winrt_commethod(6)
    def SetContentFromBitmapImage(self, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_commethod(7)
    def SetContentFromBitmapImageWithAnchorPoint(self, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def SetContentFromSoftwareBitmap(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(9)
    def SetContentFromSoftwareBitmapWithAnchorPoint(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def SetContentFromDataPackage(self) -> Void: ...
class IDragUIOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragUIOverride'
    _iid_ = Guid('{bd6c9dfa-c961-4861-b7a5-bf4fe4a8a6ef}')
    @winrt_commethod(6)
    def get_Caption(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Caption(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IsContentVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsContentVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsCaptionVisible(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsCaptionVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsGlyphVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsGlyphVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def Clear(self) -> Void: ...
    @winrt_commethod(15)
    def SetContentFromBitmapImage(self, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_commethod(16)
    def SetContentFromBitmapImageWithAnchorPoint(self, bitmapImage: win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(17)
    def SetContentFromSoftwareBitmap(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(18)
    def SetContentFromSoftwareBitmapWithAnchorPoint(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    Caption = property(get_Caption, put_Caption)
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class IDropCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDropCompletedEventArgs'
    _iid_ = Guid('{6c4fc188-95bc-4261-9ec5-21cab677b734}')
    @winrt_commethod(6)
    def get_DropResult(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    DropResult = property(get_DropResult, None)
class IDurationHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDurationHelper'
    _iid_ = Guid('{25c1659f-4497-4135-940f-ee96f4d6e934}')
class IDurationHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDurationHelperStatics'
    _iid_ = Guid('{bc88093e-3547-4ec0-b519-ffa8f9c4838c}')
    @winrt_commethod(6)
    def get_Automatic(self) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_commethod(7)
    def get_Forever(self) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_commethod(8)
    def Compare(self, duration1: win32more.Windows.UI.Xaml.Duration, duration2: win32more.Windows.UI.Xaml.Duration) -> Int32: ...
    @winrt_commethod(9)
    def FromTimeSpan(self, timeSpan: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_commethod(10)
    def GetHasTimeSpan(self, target: win32more.Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_commethod(11)
    def Add(self, target: win32more.Windows.UI.Xaml.Duration, duration: win32more.Windows.UI.Xaml.Duration) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_commethod(12)
    def Equals(self, target: win32more.Windows.UI.Xaml.Duration, value: win32more.Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_commethod(13)
    def Subtract(self, target: win32more.Windows.UI.Xaml.Duration, duration: win32more.Windows.UI.Xaml.Duration) -> win32more.Windows.UI.Xaml.Duration: ...
    Automatic = property(get_Automatic, None)
    Forever = property(get_Forever, None)
class IEffectiveViewportChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IEffectiveViewportChangedEventArgs'
    _iid_ = Guid('{55ee2e81-1c18-59ed-bd3d-c4ca8fa7d190}')
    @winrt_commethod(6)
    def get_EffectiveViewport(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_MaxViewport(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_BringIntoViewDistanceX(self) -> Double: ...
    @winrt_commethod(9)
    def get_BringIntoViewDistanceY(self) -> Double: ...
    BringIntoViewDistanceX = property(get_BringIntoViewDistanceX, None)
    BringIntoViewDistanceY = property(get_BringIntoViewDistanceY, None)
    EffectiveViewport = property(get_EffectiveViewport, None)
    MaxViewport = property(get_MaxViewport, None)
class IElementFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactory'
    _iid_ = Guid('{17d2ad90-1370-55c8-80e1-78b49004a9e1}')
    @winrt_commethod(6)
    def GetElement(self, args: win32more.Windows.UI.Xaml.ElementFactoryGetArgs) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def RecycleElement(self, args: win32more.Windows.UI.Xaml.ElementFactoryRecycleArgs) -> Void: ...
class IElementFactoryGetArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryGetArgs'
    _iid_ = Guid('{fb508774-41a3-5829-9255-cf452d041df4}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_Data(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_Parent(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Parent(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    Data = property(get_Data, put_Data)
    Parent = property(get_Parent, put_Parent)
class IElementFactoryGetArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryGetArgsFactory'
    _iid_ = Guid('{c3b6dae7-883b-5fd7-be80-2059d877e783}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ElementFactoryGetArgs: ...
class IElementFactoryRecycleArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryRecycleArgs'
    _iid_ = Guid('{86f16b14-37e8-5dd8-a90c-25d3710318b0}')
    @winrt_commethod(6)
    def get_Element(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_Element(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_Parent(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Parent(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    Element = property(get_Element, put_Element)
    Parent = property(get_Parent, put_Parent)
class IElementFactoryRecycleArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryRecycleArgsFactory'
    _iid_ = Guid('{8d926509-ea0d-541b-8271-f9e9118f5e7c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ElementFactoryRecycleArgs: ...
class IElementSoundPlayer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementSoundPlayer'
    _iid_ = Guid('{387773a5-f036-460c-9b81-f3d6ea43f6f2}')
class IElementSoundPlayerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementSoundPlayerStatics'
    _iid_ = Guid('{217a9004-981d-41c9-b152-ada911a4b13a}')
    @winrt_commethod(6)
    def get_Volume(self) -> Double: ...
    @winrt_commethod(7)
    def put_Volume(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.UI.Xaml.ElementSoundPlayerState: ...
    @winrt_commethod(9)
    def put_State(self, value: win32more.Windows.UI.Xaml.ElementSoundPlayerState) -> Void: ...
    @winrt_commethod(10)
    def Play(self, sound: win32more.Windows.UI.Xaml.ElementSoundKind) -> Void: ...
    State = property(get_State, put_State)
    Volume = property(get_Volume, put_Volume)
class IElementSoundPlayerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementSoundPlayerStatics2'
    _iid_ = Guid('{f2505956-ed41-48d7-aae8-f2abcb444929}')
    @winrt_commethod(6)
    def get_SpatialAudioMode(self) -> win32more.Windows.UI.Xaml.ElementSpatialAudioMode: ...
    @winrt_commethod(7)
    def put_SpatialAudioMode(self, value: win32more.Windows.UI.Xaml.ElementSpatialAudioMode) -> Void: ...
    SpatialAudioMode = property(get_SpatialAudioMode, put_SpatialAudioMode)
class IEventTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IEventTrigger'
    _iid_ = Guid('{def8f855-0b49-4087-b1a9-b8b38488f786}')
    @winrt_commethod(6)
    def get_RoutedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def put_RoutedEvent(self, value: win32more.Windows.UI.Xaml.RoutedEvent) -> Void: ...
    @winrt_commethod(8)
    def get_Actions(self) -> win32more.Windows.UI.Xaml.TriggerActionCollection: ...
    Actions = property(get_Actions, None)
    RoutedEvent = property(get_RoutedEvent, put_RoutedEvent)
class IExceptionRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IExceptionRoutedEventArgs'
    _iid_ = Guid('{dd9ff16a-4b62-4a6c-a49d-0671ef6136be}')
    @winrt_commethod(6)
    def get_ErrorMessage(self) -> WinRT_String: ...
    ErrorMessage = property(get_ErrorMessage, None)
class IExceptionRoutedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IExceptionRoutedEventArgsFactory'
    _iid_ = Guid('{bba9826d-5d7a-44e7-b893-b2ae0dd24273}')
class IFrameworkElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement'
    _iid_ = Guid('{a391d09b-4a99-4b7c-9d8d-6fa5d01f6fbf}')
    @winrt_commethod(6)
    def get_Triggers(self) -> win32more.Windows.UI.Xaml.TriggerCollection: ...
    @winrt_commethod(7)
    def get_Resources(self) -> win32more.Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_commethod(8)
    def put_Resources(self, value: win32more.Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_commethod(9)
    def get_Tag(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(10)
    def put_Tag(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(11)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_ActualWidth(self) -> Double: ...
    @winrt_commethod(14)
    def get_ActualHeight(self) -> Double: ...
    @winrt_commethod(15)
    def get_Width(self) -> Double: ...
    @winrt_commethod(16)
    def put_Width(self, value: Double) -> Void: ...
    @winrt_commethod(17)
    def get_Height(self) -> Double: ...
    @winrt_commethod(18)
    def put_Height(self, value: Double) -> Void: ...
    @winrt_commethod(19)
    def get_MinWidth(self) -> Double: ...
    @winrt_commethod(20)
    def put_MinWidth(self, value: Double) -> Void: ...
    @winrt_commethod(21)
    def get_MaxWidth(self) -> Double: ...
    @winrt_commethod(22)
    def put_MaxWidth(self, value: Double) -> Void: ...
    @winrt_commethod(23)
    def get_MinHeight(self) -> Double: ...
    @winrt_commethod(24)
    def put_MinHeight(self, value: Double) -> Void: ...
    @winrt_commethod(25)
    def get_MaxHeight(self) -> Double: ...
    @winrt_commethod(26)
    def put_MaxHeight(self, value: Double) -> Void: ...
    @winrt_commethod(27)
    def get_HorizontalAlignment(self) -> win32more.Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_commethod(28)
    def put_HorizontalAlignment(self, value: win32more.Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_commethod(29)
    def get_VerticalAlignment(self) -> win32more.Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_commethod(30)
    def put_VerticalAlignment(self, value: win32more.Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_commethod(31)
    def get_Margin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(32)
    def put_Margin(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(33)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(35)
    def get_BaseUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(36)
    def get_DataContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(37)
    def put_DataContext(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(38)
    def get_Style(self) -> win32more.Windows.UI.Xaml.Style: ...
    @winrt_commethod(39)
    def put_Style(self, value: win32more.Windows.UI.Xaml.Style) -> Void: ...
    @winrt_commethod(40)
    def get_Parent(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(41)
    def get_FlowDirection(self) -> win32more.Windows.UI.Xaml.FlowDirection: ...
    @winrt_commethod(42)
    def put_FlowDirection(self, value: win32more.Windows.UI.Xaml.FlowDirection) -> Void: ...
    @winrt_commethod(43)
    def add_Loaded(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(44)
    def remove_Loaded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(45)
    def add_Unloaded(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(46)
    def remove_Unloaded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(47)
    def add_SizeChanged(self, handler: win32more.Windows.UI.Xaml.SizeChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(48)
    def remove_SizeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(49)
    def add_LayoutUpdated(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(50)
    def remove_LayoutUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(51)
    def FindName(self, name: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(52)
    def SetBinding(self, dp: win32more.Windows.UI.Xaml.DependencyProperty, binding: win32more.Windows.UI.Xaml.Data.BindingBase) -> Void: ...
    ActualHeight = property(get_ActualHeight, None)
    ActualWidth = property(get_ActualWidth, None)
    BaseUri = property(get_BaseUri, None)
    DataContext = property(get_DataContext, put_DataContext)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    Height = property(get_Height, put_Height)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    Language = property(get_Language, put_Language)
    Margin = property(get_Margin, put_Margin)
    MaxHeight = property(get_MaxHeight, put_MaxHeight)
    MaxWidth = property(get_MaxWidth, put_MaxWidth)
    MinHeight = property(get_MinHeight, put_MinHeight)
    MinWidth = property(get_MinWidth, put_MinWidth)
    Name = property(get_Name, put_Name)
    Parent = property(get_Parent, None)
    Resources = property(get_Resources, put_Resources)
    Style = property(get_Style, put_Style)
    Tag = property(get_Tag, put_Tag)
    Triggers = property(get_Triggers, None)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    Width = property(get_Width, put_Width)
    Loaded = event()
    Unloaded = event()
    SizeChanged = event()
    LayoutUpdated = event()
class IFrameworkElement2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement2'
    _iid_ = Guid('{f19104be-422a-4904-a52f-ee72010429e5}')
    @winrt_commethod(6)
    def get_RequestedTheme(self) -> win32more.Windows.UI.Xaml.ElementTheme: ...
    @winrt_commethod(7)
    def put_RequestedTheme(self, value: win32more.Windows.UI.Xaml.ElementTheme) -> Void: ...
    @winrt_commethod(8)
    def add_DataContextChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.UI.Xaml.DataContextChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DataContextChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetBindingExpression(self, dp: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.UI.Xaml.Data.BindingExpression: ...
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
    DataContextChanged = event()
class IFrameworkElement3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement3'
    _iid_ = Guid('{c81c2720-5c52-4bbe-a199-2b1e34f00f70}')
    @winrt_commethod(6)
    def add_Loading(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Loading(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Loading = event()
class IFrameworkElement4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement4'
    _iid_ = Guid('{6b765bb3-fba3-4404-bdee-1a45d1ca5f21}')
    @winrt_commethod(6)
    def get_AllowFocusOnInteraction(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowFocusOnInteraction(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_FocusVisualMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(9)
    def put_FocusVisualMargin(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(10)
    def get_FocusVisualSecondaryThickness(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(11)
    def put_FocusVisualSecondaryThickness(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(12)
    def get_FocusVisualPrimaryThickness(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(13)
    def put_FocusVisualPrimaryThickness(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(14)
    def get_FocusVisualSecondaryBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(15)
    def put_FocusVisualSecondaryBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(16)
    def get_FocusVisualPrimaryBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_FocusVisualPrimaryBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(18)
    def get_AllowFocusWhenDisabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_AllowFocusWhenDisabled(self, value: Boolean) -> Void: ...
    AllowFocusOnInteraction = property(get_AllowFocusOnInteraction, put_AllowFocusOnInteraction)
    AllowFocusWhenDisabled = property(get_AllowFocusWhenDisabled, put_AllowFocusWhenDisabled)
    FocusVisualMargin = property(get_FocusVisualMargin, put_FocusVisualMargin)
    FocusVisualPrimaryBrush = property(get_FocusVisualPrimaryBrush, put_FocusVisualPrimaryBrush)
    FocusVisualPrimaryThickness = property(get_FocusVisualPrimaryThickness, put_FocusVisualPrimaryThickness)
    FocusVisualSecondaryBrush = property(get_FocusVisualSecondaryBrush, put_FocusVisualSecondaryBrush)
    FocusVisualSecondaryThickness = property(get_FocusVisualSecondaryThickness, put_FocusVisualSecondaryThickness)
class IFrameworkElement6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement6'
    _iid_ = Guid('{792a5d91-62a1-40bf-a0ce-f9c131fcb7a7}')
    @winrt_commethod(6)
    def get_ActualTheme(self) -> win32more.Windows.UI.Xaml.ElementTheme: ...
    @winrt_commethod(7)
    def add_ActualThemeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ActualThemeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ActualTheme = property(get_ActualTheme, None)
    ActualThemeChanged = event()
class IFrameworkElement7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement7'
    _iid_ = Guid('{2263886c-c069-570f-b9cc-9e21dd028d8e}')
    @winrt_commethod(6)
    def get_IsLoaded(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_EffectiveViewportChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.FrameworkElement, win32more.Windows.UI.Xaml.EffectiveViewportChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_EffectiveViewportChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsLoaded = property(get_IsLoaded, None)
    EffectiveViewportChanged = event()
class IFrameworkElementFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementFactory'
    _iid_ = Guid('{deaee126-03ca-4966-b576-604cce93b5e8}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.FrameworkElement: ...
class IFrameworkElementOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementOverrides'
    _iid_ = Guid('{da007e54-b3c2-4b9a-aa8e-d3f071262b97}')
    @winrt_commethod(6)
    def MeasureOverride(self, availableSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def ArrangeOverride(self, finalSize: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def OnApplyTemplate(self) -> Void: ...
class IFrameworkElementOverrides2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementOverrides2'
    _iid_ = Guid('{cb5cd2b9-e3b4-458c-b64e-1434fd1bd88a}')
    @winrt_commethod(6)
    def GoToElementStateCore(self, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
class IFrameworkElementProtected7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementProtected7'
    _iid_ = Guid('{65aa0480-22e3-5103-ad2a-b626f88ca5ae}')
    @winrt_commethod(6)
    def InvalidateViewport(self) -> Void: ...
class IFrameworkElementStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics'
    _iid_ = Guid('{48383032-fbeb-4f8a-aed2-ee21fb27a57b}')
    @winrt_commethod(6)
    def get_TagProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LanguageProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ActualWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ActualHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_WidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_HeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_MinWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_MaxWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_MinHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_MaxHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_HorizontalAlignmentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_VerticalAlignmentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_MarginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_NameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_DataContextProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_StyleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_FlowDirectionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ActualHeightProperty = property(get_ActualHeightProperty, None)
    ActualWidthProperty = property(get_ActualWidthProperty, None)
    DataContextProperty = property(get_DataContextProperty, None)
    FlowDirectionProperty = property(get_FlowDirectionProperty, None)
    HeightProperty = property(get_HeightProperty, None)
    HorizontalAlignmentProperty = property(get_HorizontalAlignmentProperty, None)
    LanguageProperty = property(get_LanguageProperty, None)
    MarginProperty = property(get_MarginProperty, None)
    MaxHeightProperty = property(get_MaxHeightProperty, None)
    MaxWidthProperty = property(get_MaxWidthProperty, None)
    MinHeightProperty = property(get_MinHeightProperty, None)
    MinWidthProperty = property(get_MinWidthProperty, None)
    NameProperty = property(get_NameProperty, None)
    StyleProperty = property(get_StyleProperty, None)
    TagProperty = property(get_TagProperty, None)
    VerticalAlignmentProperty = property(get_VerticalAlignmentProperty, None)
    WidthProperty = property(get_WidthProperty, None)
class IFrameworkElementStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics2'
    _iid_ = Guid('{9695db02-c0d8-4fa2-b100-3fa2df8b9538}')
    @winrt_commethod(6)
    def get_RequestedThemeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RequestedThemeProperty = property(get_RequestedThemeProperty, None)
class IFrameworkElementStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics4'
    _iid_ = Guid('{9c41b155-c5d8-4663-bff2-d8d54fb5dbb3}')
    @winrt_commethod(6)
    def get_AllowFocusOnInteractionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FocusVisualMarginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FocusVisualSecondaryThicknessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_FocusVisualPrimaryThicknessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_FocusVisualSecondaryBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_FocusVisualPrimaryBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_AllowFocusWhenDisabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AllowFocusOnInteractionProperty = property(get_AllowFocusOnInteractionProperty, None)
    AllowFocusWhenDisabledProperty = property(get_AllowFocusWhenDisabledProperty, None)
    FocusVisualMarginProperty = property(get_FocusVisualMarginProperty, None)
    FocusVisualPrimaryBrushProperty = property(get_FocusVisualPrimaryBrushProperty, None)
    FocusVisualPrimaryThicknessProperty = property(get_FocusVisualPrimaryThicknessProperty, None)
    FocusVisualSecondaryBrushProperty = property(get_FocusVisualSecondaryBrushProperty, None)
    FocusVisualSecondaryThicknessProperty = property(get_FocusVisualSecondaryThicknessProperty, None)
class IFrameworkElementStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics5'
    _iid_ = Guid('{525d3941-0b3c-4be6-9978-19a8025c09d8}')
    @winrt_commethod(6)
    def DeferTree(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
class IFrameworkElementStatics6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics6'
    _iid_ = Guid('{fcc1529a-69db-4582-a7be-cf6a1cfdacd0}')
    @winrt_commethod(6)
    def get_ActualThemeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ActualThemeProperty = property(get_ActualThemeProperty, None)
class IFrameworkTemplate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkTemplate'
    _iid_ = Guid('{a1e254d8-a446-4a27-9a9d-a0f59e1258a5}')
class IFrameworkTemplateFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkTemplateFactory'
    _iid_ = Guid('{1a78a0a5-937d-46d4-832b-94ff14dab061}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.FrameworkTemplate: ...
class IFrameworkView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkView'
    _iid_ = Guid('{ddba664b-b603-47aa-942d-3833174f0d80}')
class IFrameworkViewSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkViewSource'
    _iid_ = Guid('{e3b077da-35ad-4b09-b5b2-27420041ba9f}')
class IGridLengthHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IGridLengthHelper'
    _iid_ = Guid('{7a826ce1-07a0-4083-b6d1-b1d917b976ac}')
class IGridLengthHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IGridLengthHelperStatics'
    _iid_ = Guid('{9d457b9b-019f-4266-8872-215f198f6a9d}')
    @winrt_commethod(6)
    def get_Auto(self) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(7)
    def FromPixels(self, pixels: Double) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(8)
    def FromValueAndType(self, value: Double, type: win32more.Windows.UI.Xaml.GridUnitType) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(9)
    def GetIsAbsolute(self, target: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_commethod(10)
    def GetIsAuto(self, target: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_commethod(11)
    def GetIsStar(self, target: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_commethod(12)
    def Equals(self, target: win32more.Windows.UI.Xaml.GridLength, value: win32more.Windows.UI.Xaml.GridLength) -> Boolean: ...
    Auto = property(get_Auto, None)
class IMediaFailedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IMediaFailedRoutedEventArgs'
    _iid_ = Guid('{46d1fa8d-5149-4153-ba3c-b03e64ee531e}')
    @winrt_commethod(6)
    def get_ErrorTrace(self) -> WinRT_String: ...
    ErrorTrace = property(get_ErrorTrace, None)
class IPointHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPointHelper'
    _iid_ = Guid('{727bdd92-64b0-49cf-a321-a9793e73e2e7}')
class IPointHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPointHelperStatics'
    _iid_ = Guid('{015aca75-76d8-4b7e-8a33-7d79204691ee}')
    @winrt_commethod(6)
    def FromCoordinates(self, x: Single, y: Single) -> win32more.Windows.Foundation.Point: ...
class IPropertyMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyMetadata'
    _iid_ = Guid('{814ef30d-8d18-448a-8644-f2cb51e70380}')
    @winrt_commethod(6)
    def get_DefaultValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_CreateDefaultValueCallback(self) -> win32more.Windows.UI.Xaml.CreateDefaultValueCallback: ...
    CreateDefaultValueCallback = property(get_CreateDefaultValueCallback, None)
    DefaultValue = property(get_DefaultValue, None)
class IPropertyMetadataFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyMetadataFactory'
    _iid_ = Guid('{c1b81cc0-57cd-4f2f-b0a9-e1801b28f76b}')
    @winrt_commethod(6)
    def CreateInstanceWithDefaultValue(self, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(7)
    def CreateInstanceWithDefaultValueAndCallback(self, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable, propertyChangedCallback: win32more.Windows.UI.Xaml.PropertyChangedCallback, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
class IPropertyMetadataStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyMetadataStatics'
    _iid_ = Guid('{3b01077a-6e06-45e9-8b5c-af243458c062}')
    @winrt_commethod(6)
    def CreateWithDefaultValue(self, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(7)
    def CreateWithDefaultValueAndCallback(self, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable, propertyChangedCallback: win32more.Windows.UI.Xaml.PropertyChangedCallback) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(8)
    def CreateWithFactory(self, createDefaultValueCallback: win32more.Windows.UI.Xaml.CreateDefaultValueCallback) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(9)
    def CreateWithFactoryAndCallback(self, createDefaultValueCallback: win32more.Windows.UI.Xaml.CreateDefaultValueCallback, propertyChangedCallback: win32more.Windows.UI.Xaml.PropertyChangedCallback) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
class IPropertyPath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyPath'
    _iid_ = Guid('{300e5d8a-1ff3-4d2c-95ec-27f81debacb8}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class IPropertyPathFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyPathFactory'
    _iid_ = Guid('{4e4cdf99-9826-4e56-847c-ca055f162905}')
    @winrt_commethod(6)
    def CreateInstance(self, path: WinRT_String) -> win32more.Windows.UI.Xaml.PropertyPath: ...
class IRectHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRectHelper'
    _iid_ = Guid('{a38781e2-4bfb-4ee2-afe5-89f31b37478d}')
class IRectHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRectHelperStatics'
    _iid_ = Guid('{5ee163e4-c17e-494f-b580-2f0574fc3a15}')
    @winrt_commethod(6)
    def get_Empty(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def FromCoordinatesAndDimensions(self, x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def FromPoints(self, point1: win32more.Windows.Foundation.Point, point2: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def FromLocationAndSize(self, location: win32more.Windows.Foundation.Point, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def GetIsEmpty(self, target: win32more.Windows.Foundation.Rect) -> Boolean: ...
    @winrt_commethod(11)
    def GetBottom(self, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(12)
    def GetLeft(self, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(13)
    def GetRight(self, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(14)
    def GetTop(self, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(15)
    def Contains(self, target: win32more.Windows.Foundation.Rect, point: win32more.Windows.Foundation.Point) -> Boolean: ...
    @winrt_commethod(16)
    def Equals(self, target: win32more.Windows.Foundation.Rect, value: win32more.Windows.Foundation.Rect) -> Boolean: ...
    @winrt_commethod(17)
    def Intersect(self, target: win32more.Windows.Foundation.Rect, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(18)
    def UnionWithPoint(self, target: win32more.Windows.Foundation.Rect, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(19)
    def UnionWithRect(self, target: win32more.Windows.Foundation.Rect, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    Empty = property(get_Empty, None)
class IResourceDictionary(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IResourceDictionary'
    _iid_ = Guid('{c1ea4f24-d6de-4191-8e3a-f48601f7489c}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Source(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_MergedDictionaries(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.ResourceDictionary]: ...
    @winrt_commethod(9)
    def get_ThemeDictionaries(self) -> win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    MergedDictionaries = property(get_MergedDictionaries, None)
    Source = property(get_Source, put_Source)
    ThemeDictionaries = property(get_ThemeDictionaries, None)
class IResourceDictionaryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IResourceDictionaryFactory'
    _iid_ = Guid('{ea3639b5-31b7-4271-92c9-7c9584a91c22}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ResourceDictionary: ...
class IRoutedEvent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRoutedEvent'
    _iid_ = Guid('{a6b25818-43c1-4c70-865c-7bdd5a32e327}')
class IRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRoutedEventArgs'
    _iid_ = Guid('{5c985ac6-d802-4b38-a223-bf070c43fedf}')
    @winrt_commethod(6)
    def get_OriginalSource(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    OriginalSource = property(get_OriginalSource, None)
class IRoutedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRoutedEventArgsFactory'
    _iid_ = Guid('{b61c4d87-70e5-412e-b520-1a41ee76bbf4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.RoutedEventArgs: ...
class IScalarTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IScalarTransition'
    _iid_ = Guid('{4cb68238-e15d-524e-a73c-9d4dcfbea226}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class IScalarTransitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IScalarTransitionFactory'
    _iid_ = Guid('{c9b1e9ee-90da-5ddd-be64-3e47977ea280}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ScalarTransition: ...
class ISetter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetter'
    _iid_ = Guid('{a73ded29-b4ae-4a81-be85-e690ba0d3b6e}')
    @winrt_commethod(6)
    def get_Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def put_Property(self, value: win32more.Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(9)
    def put_Value(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    Property = property(get_Property, put_Property)
    Value = property(get_Value, put_Value)
class ISetter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetter2'
    _iid_ = Guid('{70169561-05b1-4fa3-9d53-8e0c8c747afc}')
    @winrt_commethod(6)
    def get_Target(self) -> win32more.Windows.UI.Xaml.TargetPropertyPath: ...
    @winrt_commethod(7)
    def put_Target(self, value: win32more.Windows.UI.Xaml.TargetPropertyPath) -> Void: ...
    Target = property(get_Target, put_Target)
class ISetterBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterBase'
    _iid_ = Guid('{418be27c-2ac4-4f22-8097-dea3aeeb2fb3}')
    @winrt_commethod(6)
    def get_IsSealed(self) -> Boolean: ...
    IsSealed = property(get_IsSealed, None)
class ISetterBaseCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterBaseCollection'
    _iid_ = Guid('{03c40ca8-909e-4117-811c-a4529496bdf1}')
    @winrt_commethod(6)
    def get_IsSealed(self) -> Boolean: ...
    IsSealed = property(get_IsSealed, None)
class ISetterBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterBaseFactory'
    _iid_ = Guid('{81f8ad60-1ce8-469d-a667-16e37cef8ba9}')
class ISetterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterFactory'
    _iid_ = Guid('{d3ca3d42-09b1-49d5-8891-e7b5648e02a2}')
    @winrt_commethod(6)
    def CreateInstance(self, targetProperty: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.Setter: ...
class ISizeChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISizeChangedEventArgs'
    _iid_ = Guid('{d5312e60-5cc1-42a1-920c-1af46be2f986}')
    @winrt_commethod(6)
    def get_PreviousSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_NewSize(self) -> win32more.Windows.Foundation.Size: ...
    NewSize = property(get_NewSize, None)
    PreviousSize = property(get_PreviousSize, None)
class ISizeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISizeHelper'
    _iid_ = Guid('{e7225a94-5d03-4a03-ba94-967fc68fcefe}')
class ISizeHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISizeHelperStatics'
    _iid_ = Guid('{6286c5b2-cf78-4915-aa40-76004a165f5e}')
    @winrt_commethod(6)
    def get_Empty(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def FromDimensions(self, width: Single, height: Single) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def GetIsEmpty(self, target: win32more.Windows.Foundation.Size) -> Boolean: ...
    @winrt_commethod(9)
    def Equals(self, target: win32more.Windows.Foundation.Size, value: win32more.Windows.Foundation.Size) -> Boolean: ...
    Empty = property(get_Empty, None)
class IStateTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTrigger'
    _iid_ = Guid('{67adef2e-d8d9-49f7-a1fd-2e35eedd23cd}')
    @winrt_commethod(6)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsActive(self, value: Boolean) -> Void: ...
    IsActive = property(get_IsActive, put_IsActive)
class IStateTriggerBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerBase'
    _iid_ = Guid('{48b20698-af06-466c-8052-93666dde0e49}')
class IStateTriggerBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerBaseFactory'
    _iid_ = Guid('{970e2c4b-bfaf-47b0-be42-c1d711bb2e9f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.StateTriggerBase: ...
class IStateTriggerBaseProtected(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerBaseProtected'
    _iid_ = Guid('{3c41e253-8d14-4216-994c-f9930429f6e5}')
    @winrt_commethod(6)
    def SetActive(self, IsActive: Boolean) -> Void: ...
class IStateTriggerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerStatics'
    _iid_ = Guid('{71e95c90-b3fe-4dd3-a8a8-44a2ce25e0b8}')
    @winrt_commethod(6)
    def get_IsActiveProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsActiveProperty = property(get_IsActiveProperty, None)
class IStyle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStyle'
    _iid_ = Guid('{c4a9f225-9db7-4a7d-b6d1-f74edb9293c2}')
    @winrt_commethod(6)
    def get_IsSealed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Setters(self) -> win32more.Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_commethod(8)
    def get_TargetType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(9)
    def put_TargetType(self, value: win32more.Windows.UI.Xaml.Interop.TypeName) -> Void: ...
    @winrt_commethod(10)
    def get_BasedOn(self) -> win32more.Windows.UI.Xaml.Style: ...
    @winrt_commethod(11)
    def put_BasedOn(self, value: win32more.Windows.UI.Xaml.Style) -> Void: ...
    @winrt_commethod(12)
    def Seal(self) -> Void: ...
    BasedOn = property(get_BasedOn, put_BasedOn)
    IsSealed = property(get_IsSealed, None)
    Setters = property(get_Setters, None)
    TargetType = property(get_TargetType, put_TargetType)
class IStyleFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStyleFactory'
    _iid_ = Guid('{a36824e3-3d81-4ce5-aa51-8b410f602fcd}')
    @winrt_commethod(6)
    def CreateInstance(self, targetType: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Windows.UI.Xaml.Style: ...
class ITargetPropertyPath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITargetPropertyPath'
    _iid_ = Guid('{40740f8e-085f-4ced-be70-6f47acf15ad0}')
    @winrt_commethod(6)
    def get_Path(self) -> win32more.Windows.UI.Xaml.PropertyPath: ...
    @winrt_commethod(7)
    def put_Path(self, value: win32more.Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_commethod(8)
    def get_Target(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(9)
    def put_Target(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    Path = property(get_Path, put_Path)
    Target = property(get_Target, put_Target)
class ITargetPropertyPathFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITargetPropertyPathFactory'
    _iid_ = Guid('{88eeccc8-99e2-4a44-9907-b44bc86e2bbe}')
    @winrt_commethod(6)
    def CreateInstance(self, targetProperty: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.UI.Xaml.TargetPropertyPath: ...
class IThicknessHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IThicknessHelper'
    _iid_ = Guid('{a86bae4b-1e8f-4eeb-9013-0b2838a97b34}')
class IThicknessHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IThicknessHelperStatics'
    _iid_ = Guid('{c0991a7c-070c-4da6-8784-01ca800eb73a}')
    @winrt_commethod(6)
    def FromLengths(self, left: Double, top: Double, right: Double, bottom: Double) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(7)
    def FromUniformLength(self, uniformLength: Double) -> win32more.Windows.UI.Xaml.Thickness: ...
class ITriggerAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerAction'
    _iid_ = Guid('{a2c0df02-63d5-4b46-9b83-0868d3079621}')
class ITriggerActionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerActionFactory'
    _iid_ = Guid('{68d2c0b9-3289-414f-8f6e-c6b97aedda03}')
class ITriggerBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerBase'
    _iid_ = Guid('{e7ea222f-dee6-4393-a8b2-8923d641f395}')
class ITriggerBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerBaseFactory'
    _iid_ = Guid('{6a3b9e57-fc5d-42d0-8cb9-ca50667af746}')
class IUIElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement'
    _iid_ = Guid('{676d0be9-b65c-41c6-ba40-58cf87f201c1}')
    @winrt_commethod(6)
    def get_DesiredSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_AllowDrop(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowDrop(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(10)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def get_Clip(self) -> win32more.Windows.UI.Xaml.Media.RectangleGeometry: ...
    @winrt_commethod(12)
    def put_Clip(self, value: win32more.Windows.UI.Xaml.Media.RectangleGeometry) -> Void: ...
    @winrt_commethod(13)
    def get_RenderTransform(self) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(14)
    def put_RenderTransform(self, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(15)
    def get_Projection(self) -> win32more.Windows.UI.Xaml.Media.Projection: ...
    @winrt_commethod(16)
    def put_Projection(self, value: win32more.Windows.UI.Xaml.Media.Projection) -> Void: ...
    @winrt_commethod(17)
    def get_RenderTransformOrigin(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(18)
    def put_RenderTransformOrigin(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(19)
    def get_IsHitTestVisible(self) -> Boolean: ...
    @winrt_commethod(20)
    def put_IsHitTestVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_Visibility(self) -> win32more.Windows.UI.Xaml.Visibility: ...
    @winrt_commethod(22)
    def put_Visibility(self, value: win32more.Windows.UI.Xaml.Visibility) -> Void: ...
    @winrt_commethod(23)
    def get_RenderSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(24)
    def get_UseLayoutRounding(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_UseLayoutRounding(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def get_Transitions(self) -> win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_commethod(27)
    def put_Transitions(self, value: win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_commethod(28)
    def get_CacheMode(self) -> win32more.Windows.UI.Xaml.Media.CacheMode: ...
    @winrt_commethod(29)
    def put_CacheMode(self, value: win32more.Windows.UI.Xaml.Media.CacheMode) -> Void: ...
    @winrt_commethod(30)
    def get_IsTapEnabled(self) -> Boolean: ...
    @winrt_commethod(31)
    def put_IsTapEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(32)
    def get_IsDoubleTapEnabled(self) -> Boolean: ...
    @winrt_commethod(33)
    def put_IsDoubleTapEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(34)
    def get_IsRightTapEnabled(self) -> Boolean: ...
    @winrt_commethod(35)
    def put_IsRightTapEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(36)
    def get_IsHoldingEnabled(self) -> Boolean: ...
    @winrt_commethod(37)
    def put_IsHoldingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(38)
    def get_ManipulationMode(self) -> win32more.Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_commethod(39)
    def put_ManipulationMode(self, value: win32more.Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_commethod(40)
    def get_PointerCaptures(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Input.Pointer]: ...
    @winrt_commethod(41)
    def add_KeyUp(self, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(42)
    def remove_KeyUp(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(43)
    def add_KeyDown(self, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(44)
    def remove_KeyDown(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(45)
    def add_GotFocus(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(46)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(47)
    def add_LostFocus(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(48)
    def remove_LostFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(49)
    def add_DragEnter(self, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(50)
    def remove_DragEnter(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(51)
    def add_DragLeave(self, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(52)
    def remove_DragLeave(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(53)
    def add_DragOver(self, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(54)
    def remove_DragOver(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(55)
    def add_Drop(self, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(56)
    def remove_Drop(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(57)
    def add_PointerPressed(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(58)
    def remove_PointerPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(59)
    def add_PointerMoved(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(60)
    def remove_PointerMoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(61)
    def add_PointerReleased(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(62)
    def remove_PointerReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(63)
    def add_PointerEntered(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(64)
    def remove_PointerEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(65)
    def add_PointerExited(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(66)
    def remove_PointerExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(67)
    def add_PointerCaptureLost(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(68)
    def remove_PointerCaptureLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(69)
    def add_PointerCanceled(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(70)
    def remove_PointerCanceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(71)
    def add_PointerWheelChanged(self, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(72)
    def remove_PointerWheelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(73)
    def add_Tapped(self, handler: win32more.Windows.UI.Xaml.Input.TappedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(74)
    def remove_Tapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(75)
    def add_DoubleTapped(self, handler: win32more.Windows.UI.Xaml.Input.DoubleTappedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(76)
    def remove_DoubleTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(77)
    def add_Holding(self, handler: win32more.Windows.UI.Xaml.Input.HoldingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(78)
    def remove_Holding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(79)
    def add_RightTapped(self, handler: win32more.Windows.UI.Xaml.Input.RightTappedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(80)
    def remove_RightTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(81)
    def add_ManipulationStarting(self, handler: win32more.Windows.UI.Xaml.Input.ManipulationStartingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(82)
    def remove_ManipulationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(83)
    def add_ManipulationInertiaStarting(self, handler: win32more.Windows.UI.Xaml.Input.ManipulationInertiaStartingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(84)
    def remove_ManipulationInertiaStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(85)
    def add_ManipulationStarted(self, handler: win32more.Windows.UI.Xaml.Input.ManipulationStartedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(86)
    def remove_ManipulationStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(87)
    def add_ManipulationDelta(self, handler: win32more.Windows.UI.Xaml.Input.ManipulationDeltaEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(88)
    def remove_ManipulationDelta(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(89)
    def add_ManipulationCompleted(self, handler: win32more.Windows.UI.Xaml.Input.ManipulationCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(90)
    def remove_ManipulationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(91)
    def Measure(self, availableSize: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(92)
    def Arrange(self, finalRect: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(93)
    def CapturePointer(self, value: win32more.Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    @winrt_commethod(94)
    def ReleasePointerCapture(self, value: win32more.Windows.UI.Xaml.Input.Pointer) -> Void: ...
    @winrt_commethod(95)
    def ReleasePointerCaptures(self) -> Void: ...
    @winrt_commethod(96)
    def AddHandler(self, routedEvent: win32more.Windows.UI.Xaml.RoutedEvent, handler: win32more.Windows.Win32.System.WinRT.IInspectable, handledEventsToo: Boolean) -> Void: ...
    @winrt_commethod(97)
    def RemoveHandler(self, routedEvent: win32more.Windows.UI.Xaml.RoutedEvent, handler: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(98)
    def TransformToVisual(self, visual: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(99)
    def InvalidateMeasure(self) -> Void: ...
    @winrt_commethod(100)
    def InvalidateArrange(self) -> Void: ...
    @winrt_commethod(101)
    def UpdateLayout(self) -> Void: ...
    AllowDrop = property(get_AllowDrop, put_AllowDrop)
    CacheMode = property(get_CacheMode, put_CacheMode)
    Clip = property(get_Clip, put_Clip)
    DesiredSize = property(get_DesiredSize, None)
    IsDoubleTapEnabled = property(get_IsDoubleTapEnabled, put_IsDoubleTapEnabled)
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
    IsHoldingEnabled = property(get_IsHoldingEnabled, put_IsHoldingEnabled)
    IsRightTapEnabled = property(get_IsRightTapEnabled, put_IsRightTapEnabled)
    IsTapEnabled = property(get_IsTapEnabled, put_IsTapEnabled)
    ManipulationMode = property(get_ManipulationMode, put_ManipulationMode)
    Opacity = property(get_Opacity, put_Opacity)
    PointerCaptures = property(get_PointerCaptures, None)
    Projection = property(get_Projection, put_Projection)
    RenderSize = property(get_RenderSize, None)
    RenderTransform = property(get_RenderTransform, put_RenderTransform)
    RenderTransformOrigin = property(get_RenderTransformOrigin, put_RenderTransformOrigin)
    Transitions = property(get_Transitions, put_Transitions)
    UseLayoutRounding = property(get_UseLayoutRounding, put_UseLayoutRounding)
    Visibility = property(get_Visibility, put_Visibility)
    KeyUp = event()
    KeyDown = event()
    GotFocus = event()
    LostFocus = event()
    DragEnter = event()
    DragLeave = event()
    DragOver = event()
    Drop = event()
    PointerPressed = event()
    PointerMoved = event()
    PointerReleased = event()
    PointerEntered = event()
    PointerExited = event()
    PointerCaptureLost = event()
    PointerCanceled = event()
    PointerWheelChanged = event()
    Tapped = event()
    DoubleTapped = event()
    Holding = event()
    RightTapped = event()
    ManipulationStarting = event()
    ManipulationInertiaStarting = event()
    ManipulationStarted = event()
    ManipulationDelta = event()
    ManipulationCompleted = event()
class IUIElement10(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement10'
    _iid_ = Guid('{d531c629-ad2c-5f6b-adcf-fb87287d18d7}')
    @winrt_commethod(6)
    def get_ActualOffset(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_ActualSize(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(8)
    def get_XamlRoot(self) -> win32more.Windows.UI.Xaml.XamlRoot: ...
    @winrt_commethod(9)
    def put_XamlRoot(self, value: win32more.Windows.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_commethod(10)
    def get_UIContext(self) -> win32more.Windows.UI.UIContext: ...
    @winrt_commethod(11)
    def get_Shadow(self) -> win32more.Windows.UI.Xaml.Media.Shadow: ...
    @winrt_commethod(12)
    def put_Shadow(self, value: win32more.Windows.UI.Xaml.Media.Shadow) -> Void: ...
    ActualOffset = property(get_ActualOffset, None)
    ActualSize = property(get_ActualSize, None)
    Shadow = property(get_Shadow, put_Shadow)
    UIContext = property(get_UIContext, None)
    XamlRoot = property(get_XamlRoot, put_XamlRoot)
class IUIElement2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement2'
    _iid_ = Guid('{676d0bf9-b66c-41d6-ba50-58cf87f201d1}')
    @winrt_commethod(6)
    def get_CompositeMode(self) -> win32more.Windows.UI.Xaml.Media.ElementCompositeMode: ...
    @winrt_commethod(7)
    def put_CompositeMode(self, value: win32more.Windows.UI.Xaml.Media.ElementCompositeMode) -> Void: ...
    @winrt_commethod(8)
    def CancelDirectManipulations(self) -> Boolean: ...
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
class IUIElement3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement3'
    _iid_ = Guid('{bc2b28f1-26f2-4aab-b256-3b5350881e37}')
    @winrt_commethod(6)
    def get_Transform3D(self) -> win32more.Windows.UI.Xaml.Media.Media3D.Transform3D: ...
    @winrt_commethod(7)
    def put_Transform3D(self, value: win32more.Windows.UI.Xaml.Media.Media3D.Transform3D) -> Void: ...
    @winrt_commethod(8)
    def get_CanDrag(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CanDrag(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def add_DragStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.DragStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DragStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_DropCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.DropCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DropCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def StartDragAsync(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    CanDrag = property(get_CanDrag, put_CanDrag)
    Transform3D = property(get_Transform3D, put_Transform3D)
    DragStarting = event()
    DropCompleted = event()
class IUIElement4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement4'
    _iid_ = Guid('{69145cd4-199a-4657-9e57-e99e8f136712}')
    @winrt_commethod(6)
    def get_ContextFlyout(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_commethod(7)
    def put_ContextFlyout(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_commethod(8)
    def get_ExitDisplayModeOnAccessKeyInvoked(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_ExitDisplayModeOnAccessKeyInvoked(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsAccessKeyScope(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsAccessKeyScope(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_AccessKeyScopeOwner(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_AccessKeyScopeOwner(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_AccessKey(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_AccessKey(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def add_ContextRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.ContextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ContextRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ContextCanceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.RoutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ContextCanceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_AccessKeyDisplayRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_AccessKeyDisplayRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_AccessKeyDisplayDismissed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_AccessKeyDisplayDismissed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_AccessKeyInvoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_AccessKeyInvoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AccessKey = property(get_AccessKey, put_AccessKey)
    AccessKeyScopeOwner = property(get_AccessKeyScopeOwner, put_AccessKeyScopeOwner)
    ContextFlyout = property(get_ContextFlyout, put_ContextFlyout)
    ExitDisplayModeOnAccessKeyInvoked = property(get_ExitDisplayModeOnAccessKeyInvoked, put_ExitDisplayModeOnAccessKeyInvoked)
    IsAccessKeyScope = property(get_IsAccessKeyScope, put_IsAccessKeyScope)
    ContextRequested = event()
    ContextCanceled = event()
    AccessKeyDisplayRequested = event()
    AccessKeyDisplayDismissed = event()
    AccessKeyInvoked = event()
class IUIElement5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement5'
    _iid_ = Guid('{8eed9bc2-a58c-4453-af0f-a92ee06d0317}')
    @winrt_commethod(6)
    def get_Lights(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.XamlLight]: ...
    @winrt_commethod(7)
    def get_KeyTipPlacementMode(self) -> win32more.Windows.UI.Xaml.Input.KeyTipPlacementMode: ...
    @winrt_commethod(8)
    def put_KeyTipPlacementMode(self, value: win32more.Windows.UI.Xaml.Input.KeyTipPlacementMode) -> Void: ...
    @winrt_commethod(9)
    def get_KeyTipHorizontalOffset(self) -> Double: ...
    @winrt_commethod(10)
    def put_KeyTipHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def get_KeyTipVerticalOffset(self) -> Double: ...
    @winrt_commethod(12)
    def put_KeyTipVerticalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(13)
    def get_XYFocusKeyboardNavigation(self) -> win32more.Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode: ...
    @winrt_commethod(14)
    def put_XYFocusKeyboardNavigation(self, value: win32more.Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode) -> Void: ...
    @winrt_commethod(15)
    def get_XYFocusUpNavigationStrategy(self) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(16)
    def put_XYFocusUpNavigationStrategy(self, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(17)
    def get_XYFocusDownNavigationStrategy(self) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(18)
    def put_XYFocusDownNavigationStrategy(self, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(19)
    def get_XYFocusLeftNavigationStrategy(self) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(20)
    def put_XYFocusLeftNavigationStrategy(self, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(21)
    def get_XYFocusRightNavigationStrategy(self) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(22)
    def put_XYFocusRightNavigationStrategy(self, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(23)
    def get_HighContrastAdjustment(self) -> win32more.Windows.UI.Xaml.ElementHighContrastAdjustment: ...
    @winrt_commethod(24)
    def put_HighContrastAdjustment(self, value: win32more.Windows.UI.Xaml.ElementHighContrastAdjustment) -> Void: ...
    @winrt_commethod(25)
    def get_TabFocusNavigation(self) -> win32more.Windows.UI.Xaml.Input.KeyboardNavigationMode: ...
    @winrt_commethod(26)
    def put_TabFocusNavigation(self, value: win32more.Windows.UI.Xaml.Input.KeyboardNavigationMode) -> Void: ...
    @winrt_commethod(27)
    def add_GettingFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_GettingFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_LosingFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_LosingFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_NoFocusCandidateFound(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.NoFocusCandidateFoundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_NoFocusCandidateFound(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def StartBringIntoView(self) -> Void: ...
    @winrt_commethod(34)
    def StartBringIntoViewWithOptions(self, options: win32more.Windows.UI.Xaml.BringIntoViewOptions) -> Void: ...
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    KeyTipHorizontalOffset = property(get_KeyTipHorizontalOffset, put_KeyTipHorizontalOffset)
    KeyTipPlacementMode = property(get_KeyTipPlacementMode, put_KeyTipPlacementMode)
    KeyTipVerticalOffset = property(get_KeyTipVerticalOffset, put_KeyTipVerticalOffset)
    Lights = property(get_Lights, None)
    TabFocusNavigation = property(get_TabFocusNavigation, put_TabFocusNavigation)
    XYFocusDownNavigationStrategy = property(get_XYFocusDownNavigationStrategy, put_XYFocusDownNavigationStrategy)
    XYFocusKeyboardNavigation = property(get_XYFocusKeyboardNavigation, put_XYFocusKeyboardNavigation)
    XYFocusLeftNavigationStrategy = property(get_XYFocusLeftNavigationStrategy, put_XYFocusLeftNavigationStrategy)
    XYFocusRightNavigationStrategy = property(get_XYFocusRightNavigationStrategy, put_XYFocusRightNavigationStrategy)
    XYFocusUpNavigationStrategy = property(get_XYFocusUpNavigationStrategy, put_XYFocusUpNavigationStrategy)
    GettingFocus = event()
    LosingFocus = event()
    NoFocusCandidateFound = event()
class IUIElement7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement7'
    _iid_ = Guid('{cafc4968-6369-4249-80f9-3d656319e811}')
    @winrt_commethod(6)
    def get_KeyboardAccelerators(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_commethod(7)
    def add_CharacterReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.CharacterReceivedRoutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_CharacterReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_ProcessKeyboardAccelerators(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ProcessKeyboardAccelerators(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_PreviewKeyDown(self, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_PreviewKeyDown(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_PreviewKeyUp(self, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_PreviewKeyUp(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def TryInvokeKeyboardAccelerator(self, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    CharacterReceived = event()
    ProcessKeyboardAccelerators = event()
    PreviewKeyDown = event()
    PreviewKeyUp = event()
class IUIElement8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement8'
    _iid_ = Guid('{3ab70e85-d508-4477-b6f8-0e435701c836}')
    @winrt_commethod(6)
    def get_KeyTipTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def put_KeyTipTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(8)
    def get_KeyboardAcceleratorPlacementTarget(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_KeyboardAcceleratorPlacementTarget(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_KeyboardAcceleratorPlacementMode(self) -> win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode: ...
    @winrt_commethod(11)
    def put_KeyboardAcceleratorPlacementMode(self, value: win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode) -> Void: ...
    @winrt_commethod(12)
    def add_BringIntoViewRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.BringIntoViewRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_BringIntoViewRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    KeyTipTarget = property(get_KeyTipTarget, put_KeyTipTarget)
    KeyboardAcceleratorPlacementMode = property(get_KeyboardAcceleratorPlacementMode, put_KeyboardAcceleratorPlacementMode)
    KeyboardAcceleratorPlacementTarget = property(get_KeyboardAcceleratorPlacementTarget, put_KeyboardAcceleratorPlacementTarget)
    BringIntoViewRequested = event()
class IUIElement9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement9'
    _iid_ = Guid('{b4a04776-4e88-50ca-8f2b-08940d6c5f94}')
    @winrt_commethod(6)
    def get_CanBeScrollAnchor(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanBeScrollAnchor(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_OpacityTransition(self) -> win32more.Windows.UI.Xaml.ScalarTransition: ...
    @winrt_commethod(9)
    def put_OpacityTransition(self, value: win32more.Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_commethod(10)
    def get_Translation(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_Translation(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(12)
    def get_TranslationTransition(self) -> win32more.Windows.UI.Xaml.Vector3Transition: ...
    @winrt_commethod(13)
    def put_TranslationTransition(self, value: win32more.Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_commethod(14)
    def get_Rotation(self) -> Single: ...
    @winrt_commethod(15)
    def put_Rotation(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_RotationTransition(self) -> win32more.Windows.UI.Xaml.ScalarTransition: ...
    @winrt_commethod(17)
    def put_RotationTransition(self, value: win32more.Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_commethod(18)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(19)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(20)
    def get_ScaleTransition(self) -> win32more.Windows.UI.Xaml.Vector3Transition: ...
    @winrt_commethod(21)
    def put_ScaleTransition(self, value: win32more.Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_commethod(22)
    def get_TransformMatrix(self) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_commethod(23)
    def put_TransformMatrix(self, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_commethod(24)
    def get_CenterPoint(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(25)
    def put_CenterPoint(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(26)
    def get_RotationAxis(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(27)
    def put_RotationAxis(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(28)
    def StartAnimation(self, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(29)
    def StopAnimation(self, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    CanBeScrollAnchor = property(get_CanBeScrollAnchor, put_CanBeScrollAnchor)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    OpacityTransition = property(get_OpacityTransition, put_OpacityTransition)
    Rotation = property(get_Rotation, put_Rotation)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    RotationTransition = property(get_RotationTransition, put_RotationTransition)
    Scale = property(get_Scale, put_Scale)
    ScaleTransition = property(get_ScaleTransition, put_ScaleTransition)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    Translation = property(get_Translation, put_Translation)
    TranslationTransition = property(get_TranslationTransition, put_TranslationTransition)
class IUIElementFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementFactory'
    _iid_ = Guid('{b9ee93fe-a338-419f-ac32-91dcaadf5d08}')
class IUIElementOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides'
    _iid_ = Guid('{608d2f1d-7858-4aeb-89e4-b54e2c7ed3d3}')
    @winrt_commethod(6)
    def OnCreateAutomationPeer(self) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def OnDisconnectVisualChildren(self) -> Void: ...
    @winrt_commethod(8)
    def FindSubElementsForTouchTargeting(self, point: win32more.Windows.Foundation.Point, boundingRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]]: ...
class IUIElementOverrides7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides7'
    _iid_ = Guid('{b97f7f68-c29b-4c99-a1c3-952619d6e720}')
    @winrt_commethod(6)
    def GetChildrenInTabFocusOrder(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(7)
    def OnProcessKeyboardAccelerators(self, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
class IUIElementOverrides8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides8'
    _iid_ = Guid('{4a5a645c-548d-48cf-b998-7844d6e235a1}')
    @winrt_commethod(6)
    def OnKeyboardAcceleratorInvoked(self, args: win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs) -> Void: ...
    @winrt_commethod(7)
    def OnBringIntoViewRequested(self, e: win32more.Windows.UI.Xaml.BringIntoViewRequestedEventArgs) -> Void: ...
class IUIElementOverrides9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides9'
    _iid_ = Guid('{9a6e5973-6d63-54f2-90fa-62813b20b7b9}')
    @winrt_commethod(6)
    def PopulatePropertyInfoOverride(self, propertyName: WinRT_String, animationPropertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
class IUIElementStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics'
    _iid_ = Guid('{58d3573b-f52c-45be-988b-a5869564873c}')
    @winrt_commethod(6)
    def get_KeyDownEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_KeyUpEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_PointerEnteredEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(9)
    def get_PointerPressedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(10)
    def get_PointerMovedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(11)
    def get_PointerReleasedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(12)
    def get_PointerExitedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(13)
    def get_PointerCaptureLostEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(14)
    def get_PointerCanceledEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(15)
    def get_PointerWheelChangedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(16)
    def get_TappedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(17)
    def get_DoubleTappedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(18)
    def get_HoldingEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(19)
    def get_RightTappedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(20)
    def get_ManipulationStartingEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(21)
    def get_ManipulationInertiaStartingEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(22)
    def get_ManipulationStartedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(23)
    def get_ManipulationDeltaEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(24)
    def get_ManipulationCompletedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(25)
    def get_DragEnterEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(26)
    def get_DragLeaveEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(27)
    def get_DragOverEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(28)
    def get_DropEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(29)
    def get_AllowDropProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(30)
    def get_OpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(31)
    def get_ClipProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(32)
    def get_RenderTransformProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(33)
    def get_ProjectionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(34)
    def get_RenderTransformOriginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(35)
    def get_IsHitTestVisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(36)
    def get_VisibilityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(37)
    def get_UseLayoutRoundingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(38)
    def get_TransitionsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(39)
    def get_CacheModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(40)
    def get_IsTapEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(41)
    def get_IsDoubleTapEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(42)
    def get_IsRightTapEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(43)
    def get_IsHoldingEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(44)
    def get_ManipulationModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(45)
    def get_PointerCapturesProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AllowDropProperty = property(get_AllowDropProperty, None)
    CacheModeProperty = property(get_CacheModeProperty, None)
    ClipProperty = property(get_ClipProperty, None)
    DoubleTappedEvent = property(get_DoubleTappedEvent, None)
    DragEnterEvent = property(get_DragEnterEvent, None)
    DragLeaveEvent = property(get_DragLeaveEvent, None)
    DragOverEvent = property(get_DragOverEvent, None)
    DropEvent = property(get_DropEvent, None)
    HoldingEvent = property(get_HoldingEvent, None)
    IsDoubleTapEnabledProperty = property(get_IsDoubleTapEnabledProperty, None)
    IsHitTestVisibleProperty = property(get_IsHitTestVisibleProperty, None)
    IsHoldingEnabledProperty = property(get_IsHoldingEnabledProperty, None)
    IsRightTapEnabledProperty = property(get_IsRightTapEnabledProperty, None)
    IsTapEnabledProperty = property(get_IsTapEnabledProperty, None)
    KeyDownEvent = property(get_KeyDownEvent, None)
    KeyUpEvent = property(get_KeyUpEvent, None)
    ManipulationCompletedEvent = property(get_ManipulationCompletedEvent, None)
    ManipulationDeltaEvent = property(get_ManipulationDeltaEvent, None)
    ManipulationInertiaStartingEvent = property(get_ManipulationInertiaStartingEvent, None)
    ManipulationModeProperty = property(get_ManipulationModeProperty, None)
    ManipulationStartedEvent = property(get_ManipulationStartedEvent, None)
    ManipulationStartingEvent = property(get_ManipulationStartingEvent, None)
    OpacityProperty = property(get_OpacityProperty, None)
    PointerCanceledEvent = property(get_PointerCanceledEvent, None)
    PointerCaptureLostEvent = property(get_PointerCaptureLostEvent, None)
    PointerCapturesProperty = property(get_PointerCapturesProperty, None)
    PointerEnteredEvent = property(get_PointerEnteredEvent, None)
    PointerExitedEvent = property(get_PointerExitedEvent, None)
    PointerMovedEvent = property(get_PointerMovedEvent, None)
    PointerPressedEvent = property(get_PointerPressedEvent, None)
    PointerReleasedEvent = property(get_PointerReleasedEvent, None)
    PointerWheelChangedEvent = property(get_PointerWheelChangedEvent, None)
    ProjectionProperty = property(get_ProjectionProperty, None)
    RenderTransformOriginProperty = property(get_RenderTransformOriginProperty, None)
    RenderTransformProperty = property(get_RenderTransformProperty, None)
    RightTappedEvent = property(get_RightTappedEvent, None)
    TappedEvent = property(get_TappedEvent, None)
    TransitionsProperty = property(get_TransitionsProperty, None)
    UseLayoutRoundingProperty = property(get_UseLayoutRoundingProperty, None)
    VisibilityProperty = property(get_VisibilityProperty, None)
class IUIElementStatics10(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics10'
    _iid_ = Guid('{60d25362-4b3e-53da-8b78-38db94ae8f26}')
    @winrt_commethod(6)
    def get_ShadowProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ShadowProperty = property(get_ShadowProperty, None)
class IUIElementStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics2'
    _iid_ = Guid('{58d3574b-f53c-45be-989b-a5869564874c}')
    @winrt_commethod(6)
    def get_CompositeModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CompositeModeProperty = property(get_CompositeModeProperty, None)
class IUIElementStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics3'
    _iid_ = Guid('{d1f87ade-eca1-4561-a32b-64601b4e0597}')
    @winrt_commethod(6)
    def get_Transform3DProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CanDragProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def TryStartDirectManipulation(self, value: win32more.Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    CanDragProperty = property(get_CanDragProperty, None)
    Transform3DProperty = property(get_Transform3DProperty, None)
class IUIElementStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics4'
    _iid_ = Guid('{1d157d61-16af-411f-b774-272375a4ac2c}')
    @winrt_commethod(6)
    def get_ContextFlyoutProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ExitDisplayModeOnAccessKeyInvokedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsAccessKeyScopeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AccessKeyScopeOwnerProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_AccessKeyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    AccessKeyScopeOwnerProperty = property(get_AccessKeyScopeOwnerProperty, None)
    ContextFlyoutProperty = property(get_ContextFlyoutProperty, None)
    ExitDisplayModeOnAccessKeyInvokedProperty = property(get_ExitDisplayModeOnAccessKeyInvokedProperty, None)
    IsAccessKeyScopeProperty = property(get_IsAccessKeyScopeProperty, None)
class IUIElementStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics5'
    _iid_ = Guid('{59bd7d91-8fa3-4c65-ba1b-40df38556cbb}')
    @winrt_commethod(6)
    def get_LightsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTipPlacementModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_KeyTipHorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_KeyTipVerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_XYFocusKeyboardNavigationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_XYFocusUpNavigationStrategyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_XYFocusDownNavigationStrategyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_XYFocusLeftNavigationStrategyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_XYFocusRightNavigationStrategyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_HighContrastAdjustmentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_TabFocusNavigationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    HighContrastAdjustmentProperty = property(get_HighContrastAdjustmentProperty, None)
    KeyTipHorizontalOffsetProperty = property(get_KeyTipHorizontalOffsetProperty, None)
    KeyTipPlacementModeProperty = property(get_KeyTipPlacementModeProperty, None)
    KeyTipVerticalOffsetProperty = property(get_KeyTipVerticalOffsetProperty, None)
    LightsProperty = property(get_LightsProperty, None)
    TabFocusNavigationProperty = property(get_TabFocusNavigationProperty, None)
    XYFocusDownNavigationStrategyProperty = property(get_XYFocusDownNavigationStrategyProperty, None)
    XYFocusKeyboardNavigationProperty = property(get_XYFocusKeyboardNavigationProperty, None)
    XYFocusLeftNavigationStrategyProperty = property(get_XYFocusLeftNavigationStrategyProperty, None)
    XYFocusRightNavigationStrategyProperty = property(get_XYFocusRightNavigationStrategyProperty, None)
    XYFocusUpNavigationStrategyProperty = property(get_XYFocusUpNavigationStrategyProperty, None)
class IUIElementStatics6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics6'
    _iid_ = Guid('{647e03b7-036a-4dea-9540-1dd7fd1266f1}')
    @winrt_commethod(6)
    def get_GettingFocusEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_LosingFocusEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_NoFocusCandidateFoundEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    GettingFocusEvent = property(get_GettingFocusEvent, None)
    LosingFocusEvent = property(get_LosingFocusEvent, None)
    NoFocusCandidateFoundEvent = property(get_NoFocusCandidateFoundEvent, None)
class IUIElementStatics7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics7'
    _iid_ = Guid('{da9b4493-a695-4145-ae93-888024396a0f}')
    @winrt_commethod(6)
    def get_PreviewKeyDownEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_CharacterReceivedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_PreviewKeyUpEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    CharacterReceivedEvent = property(get_CharacterReceivedEvent, None)
    PreviewKeyDownEvent = property(get_PreviewKeyDownEvent, None)
    PreviewKeyUpEvent = property(get_PreviewKeyUpEvent, None)
class IUIElementStatics8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics8'
    _iid_ = Guid('{17be3487-4875-4915-b0b1-a4c0f851df3f}')
    @winrt_commethod(6)
    def get_BringIntoViewRequestedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_ContextRequestedEvent(self) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_KeyTipTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_KeyboardAcceleratorPlacementTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_KeyboardAcceleratorPlacementModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def RegisterAsScrollPort(self, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    BringIntoViewRequestedEvent = property(get_BringIntoViewRequestedEvent, None)
    ContextRequestedEvent = property(get_ContextRequestedEvent, None)
    KeyTipTargetProperty = property(get_KeyTipTargetProperty, None)
    KeyboardAcceleratorPlacementModeProperty = property(get_KeyboardAcceleratorPlacementModeProperty, None)
    KeyboardAcceleratorPlacementTargetProperty = property(get_KeyboardAcceleratorPlacementTargetProperty, None)
class IUIElementStatics9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics9'
    _iid_ = Guid('{71467e77-8ca3-5ed7-95db-d51cdad77f81}')
    @winrt_commethod(6)
    def get_CanBeScrollAnchorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CanBeScrollAnchorProperty = property(get_CanBeScrollAnchorProperty, None)
class IUIElementWeakCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementWeakCollection'
    _iid_ = Guid('{10341223-e66d-519e-acf8-556bd244eac3}')
class IUIElementWeakCollectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementWeakCollectionFactory'
    _iid_ = Guid('{57242561-188a-5304-8792-a43f35d90f99}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.UIElementWeakCollection: ...
class IUnhandledExceptionEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUnhandledExceptionEventArgs'
    _iid_ = Guid('{7230269c-054e-4cf3-86c5-be90eb6863d5}')
    @winrt_commethod(6)
    def get_Exception(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    Message = property(get_Message, None)
class IVector3Transition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVector3Transition'
    _iid_ = Guid('{d2e209dc-c4a2-5101-9a68-fa0150505589}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Components(self) -> win32more.Windows.UI.Xaml.Vector3TransitionComponents: ...
    @winrt_commethod(9)
    def put_Components(self, value: win32more.Windows.UI.Xaml.Vector3TransitionComponents) -> Void: ...
    Components = property(get_Components, put_Components)
    Duration = property(get_Duration, put_Duration)
class IVector3TransitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVector3TransitionFactory'
    _iid_ = Guid('{c3706699-ee9b-50dc-8807-f51d5a759495}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Vector3Transition: ...
class IVisualState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualState'
    _iid_ = Guid('{6320affc-c31a-4450-afde-f6ea7bd1f586}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Storyboard(self) -> win32more.Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(8)
    def put_Storyboard(self, value: win32more.Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    Name = property(get_Name, None)
    Storyboard = property(get_Storyboard, put_Storyboard)
class IVisualState2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualState2'
    _iid_ = Guid('{0fa0f896-64c0-45fb-8d24-fb83298c0d93}')
    @winrt_commethod(6)
    def get_Setters(self) -> win32more.Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_commethod(7)
    def get_StateTriggers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.StateTriggerBase]: ...
    Setters = property(get_Setters, None)
    StateTriggers = property(get_StateTriggers, None)
class IVisualStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateChangedEventArgs'
    _iid_ = Guid('{fe216ab1-f31f-4791-8989-c70e1d9b59ff}')
    @winrt_commethod(6)
    def get_OldState(self) -> win32more.Windows.UI.Xaml.VisualState: ...
    @winrt_commethod(7)
    def put_OldState(self, value: win32more.Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_commethod(8)
    def get_NewState(self) -> win32more.Windows.UI.Xaml.VisualState: ...
    @winrt_commethod(9)
    def put_NewState(self, value: win32more.Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_commethod(10)
    def get_Control(self) -> win32more.Windows.UI.Xaml.Controls.Control: ...
    @winrt_commethod(11)
    def put_Control(self, value: win32more.Windows.UI.Xaml.Controls.Control) -> Void: ...
    Control = property(get_Control, put_Control)
    NewState = property(get_NewState, put_NewState)
    OldState = property(get_OldState, put_OldState)
class IVisualStateGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateGroup'
    _iid_ = Guid('{e4f9d9a4-e028-44de-9b15-4929ae0a26c2}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Transitions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.VisualTransition]: ...
    @winrt_commethod(8)
    def get_States(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.VisualState]: ...
    @winrt_commethod(9)
    def get_CurrentState(self) -> win32more.Windows.UI.Xaml.VisualState: ...
    @winrt_commethod(10)
    def add_CurrentStateChanged(self, handler: win32more.Windows.UI.Xaml.VisualStateChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CurrentStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CurrentStateChanging(self, handler: win32more.Windows.UI.Xaml.VisualStateChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CurrentStateChanging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentState = property(get_CurrentState, None)
    Name = property(get_Name, None)
    States = property(get_States, None)
    Transitions = property(get_Transitions, None)
    CurrentStateChanged = event()
    CurrentStateChanging = event()
class IVisualStateManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManager'
    _iid_ = Guid('{6fda9f9a-6fab-4112-9258-1006a3c3476e}')
class IVisualStateManagerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerFactory'
    _iid_ = Guid('{85e598fd-a575-47b6-9e30-383cd08585f2}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.VisualStateManager: ...
class IVisualStateManagerOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerOverrides'
    _iid_ = Guid('{4a66910e-7979-43c8-8ff4-ec6122750006}')
    @winrt_commethod(6)
    def GoToStateCore(self, control: win32more.Windows.UI.Xaml.Controls.Control, templateRoot: win32more.Windows.UI.Xaml.FrameworkElement, stateName: WinRT_String, group: win32more.Windows.UI.Xaml.VisualStateGroup, state: win32more.Windows.UI.Xaml.VisualState, useTransitions: Boolean) -> Boolean: ...
class IVisualStateManagerProtected(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerProtected'
    _iid_ = Guid('{4b3b8640-b0b7-404c-9ef4-d949640e245d}')
    @winrt_commethod(6)
    def RaiseCurrentStateChanging(self, stateGroup: win32more.Windows.UI.Xaml.VisualStateGroup, oldState: win32more.Windows.UI.Xaml.VisualState, newState: win32more.Windows.UI.Xaml.VisualState, control: win32more.Windows.UI.Xaml.Controls.Control) -> Void: ...
    @winrt_commethod(7)
    def RaiseCurrentStateChanged(self, stateGroup: win32more.Windows.UI.Xaml.VisualStateGroup, oldState: win32more.Windows.UI.Xaml.VisualState, newState: win32more.Windows.UI.Xaml.VisualState, control: win32more.Windows.UI.Xaml.Controls.Control) -> Void: ...
class IVisualStateManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerStatics'
    _iid_ = Guid('{01d0e9e0-d713-414e-a74e-e63ec7ac8c3d}')
    @winrt_commethod(6)
    def GetVisualStateGroups(self, obj: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.VisualStateGroup]: ...
    @winrt_commethod(7)
    def get_CustomVisualStateManagerProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetCustomVisualStateManager(self, obj: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.UI.Xaml.VisualStateManager: ...
    @winrt_commethod(9)
    def SetCustomVisualStateManager(self, obj: win32more.Windows.UI.Xaml.FrameworkElement, value: win32more.Windows.UI.Xaml.VisualStateManager) -> Void: ...
    @winrt_commethod(10)
    def GoToState(self, control: win32more.Windows.UI.Xaml.Controls.Control, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
    CustomVisualStateManagerProperty = property(get_CustomVisualStateManagerProperty, None)
class IVisualTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualTransition'
    _iid_ = Guid('{55c5905e-2bc7-400d-aaa4-1a2981491ee0}')
    @winrt_commethod(6)
    def get_GeneratedDuration(self) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_commethod(7)
    def put_GeneratedDuration(self, value: win32more.Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_commethod(8)
    def get_GeneratedEasingFunction(self) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(9)
    def put_GeneratedEasingFunction(self, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(10)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_From(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Storyboard(self) -> win32more.Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(15)
    def put_Storyboard(self, value: win32more.Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    From = property(get_From, put_From)
    GeneratedDuration = property(get_GeneratedDuration, put_GeneratedDuration)
    GeneratedEasingFunction = property(get_GeneratedEasingFunction, put_GeneratedEasingFunction)
    Storyboard = property(get_Storyboard, put_Storyboard)
    To = property(get_To, put_To)
class IVisualTransitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualTransitionFactory'
    _iid_ = Guid('{ea75864f-d1e0-4dae-b429-89fc322724f4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.VisualTransition: ...
class IWindow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow'
    _iid_ = Guid('{3276167d-c9f6-462d-9de2-ae4c1fd8c2e5}')
    @winrt_commethod(6)
    def get_Bounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Content(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Content(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def get_CoreWindow(self) -> win32more.Windows.UI.Core.CoreWindow: ...
    @winrt_commethod(11)
    def get_Dispatcher(self) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_commethod(12)
    def add_Activated(self, handler: win32more.Windows.UI.Xaml.WindowActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Closed(self, handler: win32more.Windows.UI.Xaml.WindowClosedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_SizeChanged(self, handler: win32more.Windows.UI.Xaml.WindowSizeChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SizeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_VisibilityChanged(self, handler: win32more.Windows.UI.Xaml.WindowVisibilityChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_VisibilityChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def Activate(self) -> Void: ...
    @winrt_commethod(21)
    def Close(self) -> Void: ...
    Bounds = property(get_Bounds, None)
    Content = property(get_Content, put_Content)
    CoreWindow = property(get_CoreWindow, None)
    Dispatcher = property(get_Dispatcher, None)
    Visible = property(get_Visible, None)
    Activated = event()
    Closed = event()
    SizeChanged = event()
    VisibilityChanged = event()
class IWindow2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow2'
    _iid_ = Guid('{d384759f-34f6-4482-8435-f552f9b24cc8}')
    @winrt_commethod(6)
    def SetTitleBar(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
class IWindow3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow3'
    _iid_ = Guid('{b70bdc9d-1c35-462a-9b97-808d5af9f28e}')
    @winrt_commethod(6)
    def get_Compositor(self) -> win32more.Windows.UI.Composition.Compositor: ...
    Compositor = property(get_Compositor, None)
class IWindow4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow4'
    _iid_ = Guid('{bfe1b8ce-6c40-50f9-854c-7021d2bc9de6}')
    @winrt_commethod(6)
    def get_UIContext(self) -> win32more.Windows.UI.UIContext: ...
    UIContext = property(get_UIContext, None)
class IWindowCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindowCreatedEventArgs'
    _iid_ = Guid('{31b71470-feff-4654-af48-9b398ab5772b}')
    @winrt_commethod(6)
    def get_Window(self) -> win32more.Windows.UI.Xaml.Window: ...
    Window = property(get_Window, None)
class IWindowStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindowStatics'
    _iid_ = Guid('{93328409-4ea1-4afa-83dc-0c4e73e88bb1}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.UI.Xaml.Window: ...
    Current = property(get_Current, None)
class IXamlRoot(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IXamlRoot'
    _iid_ = Guid('{34b50756-1696-5b6d-8e9b-c71464ccad5a}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_RasterizationScale(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsHostVisible(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_UIContext(self) -> win32more.Windows.UI.UIContext: ...
    @winrt_commethod(11)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.XamlRoot, win32more.Windows.UI.Xaml.XamlRootChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Content = property(get_Content, None)
    IsHostVisible = property(get_IsHostVisible, None)
    RasterizationScale = property(get_RasterizationScale, None)
    Size = property(get_Size, None)
    UIContext = property(get_UIContext, None)
    Changed = event()
class IXamlRootChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IXamlRootChangedEventArgs'
    _iid_ = Guid('{92d71c21-d23c-5a17-bcb8-001504b6bb19}')
class LeavingBackgroundEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aaad5dad-4fc6-4aa4-b7cf-877e36ada4f6}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.ApplicationModel.LeavingBackgroundEventArgs) -> Void: ...
class LineStackingStrategy(Enum, Int32):
    MaxHeight = 0
    BlockLineHeight = 1
    BaselineToBaseline = 2
class MediaFailedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.ExceptionRoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.IMediaFailedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.MediaFailedRoutedEventArgs'
    @winrt_mixinmethod
    def get_ErrorTrace(self: win32more.Windows.UI.Xaml.IMediaFailedRoutedEventArgs) -> WinRT_String: ...
    ErrorTrace = property(get_ErrorTrace, None)
class OpticalMarginAlignment(Enum, Int32):
    None_ = 0
    TrimSideBearings = 1
class PointHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IPointHelper
    _classid_ = 'Windows.UI.Xaml.PointHelper'
    @winrt_classmethod
    def FromCoordinates(cls: win32more.Windows.UI.Xaml.IPointHelperStatics, x: Single, y: Single) -> win32more.Windows.Foundation.Point: ...
class PropertyChangedCallback(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5a9f8a25-d142-44a4-8231-fd676724f29b}')
    @winrt_commethod(3)
    def Invoke(self, d: win32more.Windows.UI.Xaml.DependencyObject, e: win32more.Windows.UI.Xaml.DependencyPropertyChangedEventArgs) -> Void: ...
class PropertyMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IPropertyMetadata
    _classid_ = 'Windows.UI.Xaml.PropertyMetadata'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.PropertyMetadata.CreateInstanceWithDefaultValue(*args, None, None))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.PropertyMetadata.CreateInstanceWithDefaultValueAndCallback(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithDefaultValue(cls: win32more.Windows.UI.Xaml.IPropertyMetadataFactory, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_factorymethod
    def CreateInstanceWithDefaultValueAndCallback(cls: win32more.Windows.UI.Xaml.IPropertyMetadataFactory, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable, propertyChangedCallback: win32more.Windows.UI.Xaml.PropertyChangedCallback, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_mixinmethod
    def get_DefaultValue(self: win32more.Windows.UI.Xaml.IPropertyMetadata) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_CreateDefaultValueCallback(self: win32more.Windows.UI.Xaml.IPropertyMetadata) -> win32more.Windows.UI.Xaml.CreateDefaultValueCallback: ...
    @winrt_classmethod
    def CreateWithDefaultValue(cls: win32more.Windows.UI.Xaml.IPropertyMetadataStatics, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def CreateWithDefaultValueAndCallback(cls: win32more.Windows.UI.Xaml.IPropertyMetadataStatics, defaultValue: win32more.Windows.Win32.System.WinRT.IInspectable, propertyChangedCallback: win32more.Windows.UI.Xaml.PropertyChangedCallback) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def CreateWithFactory(cls: win32more.Windows.UI.Xaml.IPropertyMetadataStatics, createDefaultValueCallback: win32more.Windows.UI.Xaml.CreateDefaultValueCallback) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def CreateWithFactoryAndCallback(cls: win32more.Windows.UI.Xaml.IPropertyMetadataStatics, createDefaultValueCallback: win32more.Windows.UI.Xaml.CreateDefaultValueCallback, propertyChangedCallback: win32more.Windows.UI.Xaml.PropertyChangedCallback) -> win32more.Windows.UI.Xaml.PropertyMetadata: ...
    CreateDefaultValueCallback = property(get_CreateDefaultValueCallback, None)
    DefaultValue = property(get_DefaultValue, None)
class PropertyPath(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IPropertyPath
    _classid_ = 'Windows.UI.Xaml.PropertyPath'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.PropertyPath.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IPropertyPathFactory, path: WinRT_String) -> win32more.Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.UI.Xaml.IPropertyPath) -> WinRT_String: ...
    Path = property(get_Path, None)
class _RectHelper_Meta_(ComPtr.__class__):
    pass
class RectHelper(ComPtr, metaclass=_RectHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IRectHelper
    _classid_ = 'Windows.UI.Xaml.RectHelper'
    @winrt_classmethod
    def get_Empty(cls: win32more.Windows.UI.Xaml.IRectHelperStatics) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def FromCoordinatesAndDimensions(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def FromPoints(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, point1: win32more.Windows.Foundation.Point, point2: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def FromLocationAndSize(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, location: win32more.Windows.Foundation.Point, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def GetIsEmpty(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect) -> Boolean: ...
    @winrt_classmethod
    def GetBottom(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def GetLeft(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def GetRight(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def GetTop(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def Contains(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect, point: win32more.Windows.Foundation.Point) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect, value: win32more.Windows.Foundation.Rect) -> Boolean: ...
    @winrt_classmethod
    def Intersect(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def UnionWithPoint(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def UnionWithRect(cls: win32more.Windows.UI.Xaml.IRectHelperStatics, target: win32more.Windows.Foundation.Rect, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    _RectHelper_Meta_.Empty = property(get_Empty, None)
class ResourceDictionary(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    implements: Tuple[MappingProtocol[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]]
    default_interface: win32more.Windows.UI.Xaml.IResourceDictionary
    _classid_ = 'Windows.UI.Xaml.ResourceDictionary'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.ResourceDictionary.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IResourceDictionaryFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Xaml.IResourceDictionary) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.UI.Xaml.IResourceDictionary, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_MergedDictionaries(self: win32more.Windows.UI.Xaml.IResourceDictionary) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.ResourceDictionary]: ...
    @winrt_mixinmethod
    def get_ThemeDictionaries(self: win32more.Windows.UI.Xaml.IResourceDictionary) -> win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable], key: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable], key: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable], key: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable], key: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    MergedDictionaries = property(get_MergedDictionaries, None)
    Size = property(get_Size, None)
    Source = property(get_Source, put_Source)
    ThemeDictionaries = property(get_ThemeDictionaries, None)
class RoutedEvent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IRoutedEvent
    _classid_ = 'Windows.UI.Xaml.RoutedEvent'
class RoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.RoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.RoutedEventArgs.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IRoutedEventArgsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.RoutedEventArgs: ...
    @winrt_mixinmethod
    def get_OriginalSource(self: win32more.Windows.UI.Xaml.IRoutedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    OriginalSource = property(get_OriginalSource, None)
class RoutedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a856e674-b0b6-4bc3-bba8-1ba06e40d4b5}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.RoutedEventArgs) -> Void: ...
class ScalarTransition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IScalarTransition
    _classid_ = 'Windows.UI.Xaml.ScalarTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.ScalarTransition.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IScalarTransitionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.ScalarTransition: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Xaml.IScalarTransition) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.UI.Xaml.IScalarTransition, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class Setter(ComPtr):
    extends: win32more.Windows.UI.Xaml.SetterBase
    default_interface: win32more.Windows.UI.Xaml.ISetter
    _classid_ = 'Windows.UI.Xaml.Setter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Setter.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Setter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Setter: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.ISetterFactory, targetProperty: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.Setter: ...
    @winrt_mixinmethod
    def get_Property(self: win32more.Windows.UI.Xaml.ISetter) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_mixinmethod
    def put_Property(self: win32more.Windows.UI.Xaml.ISetter, value: win32more.Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Xaml.ISetter) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.UI.Xaml.ISetter, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: win32more.Windows.UI.Xaml.ISetter2) -> win32more.Windows.UI.Xaml.TargetPropertyPath: ...
    @winrt_mixinmethod
    def put_Target(self: win32more.Windows.UI.Xaml.ISetter2, value: win32more.Windows.UI.Xaml.TargetPropertyPath) -> Void: ...
    Property = property(get_Property, put_Property)
    Target = property(get_Target, put_Target)
    Value = property(get_Value, put_Value)
class SetterBase(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.ISetterBase
    _classid_ = 'Windows.UI.Xaml.SetterBase'
    @winrt_mixinmethod
    def get_IsSealed(self: win32more.Windows.UI.Xaml.ISetterBase) -> Boolean: ...
    IsSealed = property(get_IsSealed, None)
class SetterBaseCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.SetterBase]]
    default_interface: win32more.Windows.UI.Xaml.ISetterBaseCollection
    _classid_ = 'Windows.UI.Xaml.SetterBaseCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.SetterBaseCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_mixinmethod
    def get_IsSealed(self: win32more.Windows.UI.Xaml.ISetterBaseCollection) -> Boolean: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], index: UInt32) -> win32more.Windows.UI.Xaml.SetterBase: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.SetterBase]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], value: win32more.Windows.UI.Xaml.SetterBase, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], index: UInt32, value: win32more.Windows.UI.Xaml.SetterBase) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], index: UInt32, value: win32more.Windows.UI.Xaml.SetterBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], value: win32more.Windows.UI.Xaml.SetterBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.SetterBase]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.SetterBase], items: PassArray[win32more.Windows.UI.Xaml.SetterBase]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.SetterBase]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.SetterBase]: ...
    IsSealed = property(get_IsSealed, None)
    Size = property(get_Size, None)
class SizeChangedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.ISizeChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.SizeChangedEventArgs'
    @winrt_mixinmethod
    def get_PreviousSize(self: win32more.Windows.UI.Xaml.ISizeChangedEventArgs) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_NewSize(self: win32more.Windows.UI.Xaml.ISizeChangedEventArgs) -> win32more.Windows.Foundation.Size: ...
    NewSize = property(get_NewSize, None)
    PreviousSize = property(get_PreviousSize, None)
class SizeChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1115b13c-25d2-480b-89dc-eb3dcbd6b7fa}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.SizeChangedEventArgs) -> Void: ...
class _SizeHelper_Meta_(ComPtr.__class__):
    pass
class SizeHelper(ComPtr, metaclass=_SizeHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.ISizeHelper
    _classid_ = 'Windows.UI.Xaml.SizeHelper'
    @winrt_classmethod
    def get_Empty(cls: win32more.Windows.UI.Xaml.ISizeHelperStatics) -> win32more.Windows.Foundation.Size: ...
    @winrt_classmethod
    def FromDimensions(cls: win32more.Windows.UI.Xaml.ISizeHelperStatics, width: Single, height: Single) -> win32more.Windows.Foundation.Size: ...
    @winrt_classmethod
    def GetIsEmpty(cls: win32more.Windows.UI.Xaml.ISizeHelperStatics, target: win32more.Windows.Foundation.Size) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: win32more.Windows.UI.Xaml.ISizeHelperStatics, target: win32more.Windows.Foundation.Size, value: win32more.Windows.Foundation.Size) -> Boolean: ...
    _SizeHelper_Meta_.Empty = property(get_Empty, None)
class _StateTrigger_Meta_(ComPtr.__class__):
    pass
class StateTrigger(ComPtr, metaclass=_StateTrigger_Meta_):
    extends: win32more.Windows.UI.Xaml.StateTriggerBase
    default_interface: win32more.Windows.UI.Xaml.IStateTrigger
    _classid_ = 'Windows.UI.Xaml.StateTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.StateTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.StateTrigger: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.UI.Xaml.IStateTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsActive(self: win32more.Windows.UI.Xaml.IStateTrigger, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsActiveProperty(cls: win32more.Windows.UI.Xaml.IStateTriggerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsActive = property(get_IsActive, put_IsActive)
    _StateTrigger_Meta_.IsActiveProperty = property(get_IsActiveProperty, None)
class StateTriggerBase(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IStateTriggerBase
    _classid_ = 'Windows.UI.Xaml.StateTriggerBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.StateTriggerBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IStateTriggerBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.StateTriggerBase: ...
    @winrt_mixinmethod
    def SetActive(self: win32more.Windows.UI.Xaml.IStateTriggerBaseProtected, IsActive: Boolean) -> Void: ...
class Style(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IStyle
    _classid_ = 'Windows.UI.Xaml.Style'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Style.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Style.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Style: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IStyleFactory, targetType: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Windows.UI.Xaml.Style: ...
    @winrt_mixinmethod
    def get_IsSealed(self: win32more.Windows.UI.Xaml.IStyle) -> Boolean: ...
    @winrt_mixinmethod
    def get_Setters(self: win32more.Windows.UI.Xaml.IStyle) -> win32more.Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_mixinmethod
    def get_TargetType(self: win32more.Windows.UI.Xaml.IStyle) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def put_TargetType(self: win32more.Windows.UI.Xaml.IStyle, value: win32more.Windows.UI.Xaml.Interop.TypeName) -> Void: ...
    @winrt_mixinmethod
    def get_BasedOn(self: win32more.Windows.UI.Xaml.IStyle) -> win32more.Windows.UI.Xaml.Style: ...
    @winrt_mixinmethod
    def put_BasedOn(self: win32more.Windows.UI.Xaml.IStyle, value: win32more.Windows.UI.Xaml.Style) -> Void: ...
    @winrt_mixinmethod
    def Seal(self: win32more.Windows.UI.Xaml.IStyle) -> Void: ...
    BasedOn = property(get_BasedOn, put_BasedOn)
    IsSealed = property(get_IsSealed, None)
    Setters = property(get_Setters, None)
    TargetType = property(get_TargetType, put_TargetType)
class SuspendingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23429465-e36a-40e2-b139-a4704602a6e1}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.ApplicationModel.SuspendingEventArgs) -> Void: ...
class TargetPropertyPath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.ITargetPropertyPath
    _classid_ = 'Windows.UI.Xaml.TargetPropertyPath'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.TargetPropertyPath.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.TargetPropertyPath.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.TargetPropertyPath: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.ITargetPropertyPathFactory, targetProperty: win32more.Windows.UI.Xaml.DependencyProperty) -> win32more.Windows.UI.Xaml.TargetPropertyPath: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.UI.Xaml.ITargetPropertyPath) -> win32more.Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Windows.UI.Xaml.ITargetPropertyPath, value: win32more.Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: win32more.Windows.UI.Xaml.ITargetPropertyPath) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Target(self: win32more.Windows.UI.Xaml.ITargetPropertyPath, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    Path = property(get_Path, put_Path)
    Target = property(get_Target, put_Target)
class TextAlignment(Enum, Int32):
    Center = 0
    Left = 1
    Start = 1
    Right = 2
    End = 2
    Justify = 3
    DetectFromContent = 4
class TextLineBounds(Enum, Int32):
    Full = 0
    TrimToCapHeight = 1
    TrimToBaseline = 2
    Tight = 3
class TextReadingOrder(Enum, Int32):
    Default = 0
    UseFlowDirection = 0
    DetectFromContent = 1
class TextTrimming(Enum, Int32):
    None_ = 0
    CharacterEllipsis = 1
    WordEllipsis = 2
    Clip = 3
class TextWrapping(Enum, Int32):
    NoWrap = 1
    Wrap = 2
    WrapWholeWords = 3
class Thickness(Structure):
    Left: Double
    Top: Double
    Right: Double
    Bottom: Double
class ThicknessHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IThicknessHelper
    _classid_ = 'Windows.UI.Xaml.ThicknessHelper'
    @winrt_classmethod
    def FromLengths(cls: win32more.Windows.UI.Xaml.IThicknessHelperStatics, left: Double, top: Double, right: Double, bottom: Double) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_classmethod
    def FromUniformLength(cls: win32more.Windows.UI.Xaml.IThicknessHelperStatics, uniformLength: Double) -> win32more.Windows.UI.Xaml.Thickness: ...
class TriggerAction(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.ITriggerAction
    _classid_ = 'Windows.UI.Xaml.TriggerAction'
class TriggerActionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.TriggerAction]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction]
    _classid_ = 'Windows.UI.Xaml.TriggerActionCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.TriggerActionCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.TriggerActionCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], index: UInt32) -> win32more.Windows.UI.Xaml.TriggerAction: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.TriggerAction]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], value: win32more.Windows.UI.Xaml.TriggerAction, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], index: UInt32, value: win32more.Windows.UI.Xaml.TriggerAction) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], index: UInt32, value: win32more.Windows.UI.Xaml.TriggerAction) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], value: win32more.Windows.UI.Xaml.TriggerAction) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.TriggerAction]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerAction], items: PassArray[win32more.Windows.UI.Xaml.TriggerAction]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.TriggerAction]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.TriggerAction]: ...
    Size = property(get_Size, None)
class TriggerBase(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.ITriggerBase
    _classid_ = 'Windows.UI.Xaml.TriggerBase'
class TriggerCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.TriggerBase]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase]
    _classid_ = 'Windows.UI.Xaml.TriggerCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], index: UInt32) -> win32more.Windows.UI.Xaml.TriggerBase: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.TriggerBase]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], value: win32more.Windows.UI.Xaml.TriggerBase, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], index: UInt32, value: win32more.Windows.UI.Xaml.TriggerBase) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], index: UInt32, value: win32more.Windows.UI.Xaml.TriggerBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], value: win32more.Windows.UI.Xaml.TriggerBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.TriggerBase]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.TriggerBase], items: PassArray[win32more.Windows.UI.Xaml.TriggerBase]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.TriggerBase]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.TriggerBase]: ...
    Size = property(get_Size, None)
class _UIElement_Meta_(ComPtr.__class__):
    pass
class UIElement(ComPtr, metaclass=_UIElement_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IUIElement
    _classid_ = 'Windows.UI.Xaml.UIElement'
    @winrt_mixinmethod
    def get_DesiredSize(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_AllowDrop(self: win32more.Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowDrop(self: win32more.Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Windows.UI.Xaml.IUIElement) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Windows.UI.Xaml.IUIElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Clip(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.UI.Xaml.Media.RectangleGeometry: ...
    @winrt_mixinmethod
    def put_Clip(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Media.RectangleGeometry) -> Void: ...
    @winrt_mixinmethod
    def get_RenderTransform(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_RenderTransform(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def get_Projection(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.UI.Xaml.Media.Projection: ...
    @winrt_mixinmethod
    def put_Projection(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Media.Projection) -> Void: ...
    @winrt_mixinmethod
    def get_RenderTransformOrigin(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_RenderTransformOrigin(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_IsHitTestVisible(self: win32more.Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHitTestVisible(self: win32more.Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Visibility(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.UI.Xaml.Visibility: ...
    @winrt_mixinmethod
    def put_Visibility(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Visibility) -> Void: ...
    @winrt_mixinmethod
    def get_RenderSize(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_UseLayoutRounding(self: win32more.Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseLayoutRounding(self: win32more.Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Transitions(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_mixinmethod
    def put_Transitions(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_mixinmethod
    def get_CacheMode(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.UI.Xaml.Media.CacheMode: ...
    @winrt_mixinmethod
    def put_CacheMode(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Media.CacheMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsTapEnabled(self: win32more.Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTapEnabled(self: win32more.Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDoubleTapEnabled(self: win32more.Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDoubleTapEnabled(self: win32more.Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRightTapEnabled(self: win32more.Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRightTapEnabled(self: win32more.Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsHoldingEnabled(self: win32more.Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHoldingEnabled(self: win32more.Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ManipulationMode(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_mixinmethod
    def put_ManipulationMode(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_mixinmethod
    def get_PointerCaptures(self: win32more.Windows.UI.Xaml.IUIElement) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Input.Pointer]: ...
    @winrt_mixinmethod
    def add_KeyUp(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyUp(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyDown(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyDown(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LostFocus(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LostFocus(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragEnter(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragEnter(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragLeave(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragLeave(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragOver(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragOver(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Drop(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.DragEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Drop(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerEntered(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerCaptureLost(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCaptureLost(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerCanceled(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCanceled(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerWheelChanged(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.PointerEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerWheelChanged(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.TappedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DoubleTapped(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.DoubleTappedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DoubleTapped(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Holding(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.HoldingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Holding(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RightTapped(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.RightTappedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RightTapped(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarting(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.ManipulationStartingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarting(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationInertiaStarting(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.ManipulationInertiaStartingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationInertiaStarting(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.ManipulationStartedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationDelta(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.ManipulationDeltaEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationDelta(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: win32more.Windows.UI.Xaml.IUIElement, handler: win32more.Windows.UI.Xaml.Input.ManipulationCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: win32more.Windows.UI.Xaml.IUIElement, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Measure(self: win32more.Windows.UI.Xaml.IUIElement, availableSize: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def Arrange(self: win32more.Windows.UI.Xaml.IUIElement, finalRect: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def CapturePointer(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    @winrt_mixinmethod
    def ReleasePointerCapture(self: win32more.Windows.UI.Xaml.IUIElement, value: win32more.Windows.UI.Xaml.Input.Pointer) -> Void: ...
    @winrt_mixinmethod
    def ReleasePointerCaptures(self: win32more.Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def AddHandler(self: win32more.Windows.UI.Xaml.IUIElement, routedEvent: win32more.Windows.UI.Xaml.RoutedEvent, handler: win32more.Windows.Win32.System.WinRT.IInspectable, handledEventsToo: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RemoveHandler(self: win32more.Windows.UI.Xaml.IUIElement, routedEvent: win32more.Windows.UI.Xaml.RoutedEvent, handler: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def TransformToVisual(self: win32more.Windows.UI.Xaml.IUIElement, visual: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def InvalidateMeasure(self: win32more.Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def InvalidateArrange(self: win32more.Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def UpdateLayout(self: win32more.Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def get_CompositeMode(self: win32more.Windows.UI.Xaml.IUIElement2) -> win32more.Windows.UI.Xaml.Media.ElementCompositeMode: ...
    @winrt_mixinmethod
    def put_CompositeMode(self: win32more.Windows.UI.Xaml.IUIElement2, value: win32more.Windows.UI.Xaml.Media.ElementCompositeMode) -> Void: ...
    @winrt_mixinmethod
    def CancelDirectManipulations(self: win32more.Windows.UI.Xaml.IUIElement2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Transform3D(self: win32more.Windows.UI.Xaml.IUIElement3) -> win32more.Windows.UI.Xaml.Media.Media3D.Transform3D: ...
    @winrt_mixinmethod
    def put_Transform3D(self: win32more.Windows.UI.Xaml.IUIElement3, value: win32more.Windows.UI.Xaml.Media.Media3D.Transform3D) -> Void: ...
    @winrt_mixinmethod
    def get_CanDrag(self: win32more.Windows.UI.Xaml.IUIElement3) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanDrag(self: win32more.Windows.UI.Xaml.IUIElement3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_DragStarting(self: win32more.Windows.UI.Xaml.IUIElement3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.DragStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragStarting(self: win32more.Windows.UI.Xaml.IUIElement3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DropCompleted(self: win32more.Windows.UI.Xaml.IUIElement3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.DropCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DropCompleted(self: win32more.Windows.UI.Xaml.IUIElement3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartDragAsync(self: win32more.Windows.UI.Xaml.IUIElement3, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_mixinmethod
    def get_ContextFlyout(self: win32more.Windows.UI.Xaml.IUIElement4) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_mixinmethod
    def put_ContextFlyout(self: win32more.Windows.UI.Xaml.IUIElement4, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_mixinmethod
    def get_ExitDisplayModeOnAccessKeyInvoked(self: win32more.Windows.UI.Xaml.IUIElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExitDisplayModeOnAccessKeyInvoked(self: win32more.Windows.UI.Xaml.IUIElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAccessKeyScope(self: win32more.Windows.UI.Xaml.IUIElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAccessKeyScope(self: win32more.Windows.UI.Xaml.IUIElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AccessKeyScopeOwner(self: win32more.Windows.UI.Xaml.IUIElement4) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_AccessKeyScopeOwner(self: win32more.Windows.UI.Xaml.IUIElement4, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_AccessKey(self: win32more.Windows.UI.Xaml.IUIElement4) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AccessKey(self: win32more.Windows.UI.Xaml.IUIElement4, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_ContextRequested(self: win32more.Windows.UI.Xaml.IUIElement4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.ContextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContextRequested(self: win32more.Windows.UI.Xaml.IUIElement4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContextCanceled(self: win32more.Windows.UI.Xaml.IUIElement4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.RoutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContextCanceled(self: win32more.Windows.UI.Xaml.IUIElement4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccessKeyDisplayRequested(self: win32more.Windows.UI.Xaml.IUIElement4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessKeyDisplayRequested(self: win32more.Windows.UI.Xaml.IUIElement4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccessKeyDisplayDismissed(self: win32more.Windows.UI.Xaml.IUIElement4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessKeyDisplayDismissed(self: win32more.Windows.UI.Xaml.IUIElement4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccessKeyInvoked(self: win32more.Windows.UI.Xaml.IUIElement4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessKeyInvoked(self: win32more.Windows.UI.Xaml.IUIElement4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Lights(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.XamlLight]: ...
    @winrt_mixinmethod
    def get_KeyTipPlacementMode(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.Input.KeyTipPlacementMode: ...
    @winrt_mixinmethod
    def put_KeyTipPlacementMode(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.Input.KeyTipPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTipHorizontalOffset(self: win32more.Windows.UI.Xaml.IUIElement5) -> Double: ...
    @winrt_mixinmethod
    def put_KeyTipHorizontalOffset(self: win32more.Windows.UI.Xaml.IUIElement5, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTipVerticalOffset(self: win32more.Windows.UI.Xaml.IUIElement5) -> Double: ...
    @winrt_mixinmethod
    def put_KeyTipVerticalOffset(self: win32more.Windows.UI.Xaml.IUIElement5, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusKeyboardNavigation(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode: ...
    @winrt_mixinmethod
    def put_XYFocusKeyboardNavigation(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusUpNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusUpNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusDownNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusDownNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusLeftNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusLeftNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusRightNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusRightNavigationStrategy(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_HighContrastAdjustment(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.ElementHighContrastAdjustment: ...
    @winrt_mixinmethod
    def put_HighContrastAdjustment(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.ElementHighContrastAdjustment) -> Void: ...
    @winrt_mixinmethod
    def get_TabFocusNavigation(self: win32more.Windows.UI.Xaml.IUIElement5) -> win32more.Windows.UI.Xaml.Input.KeyboardNavigationMode: ...
    @winrt_mixinmethod
    def put_TabFocusNavigation(self: win32more.Windows.UI.Xaml.IUIElement5, value: win32more.Windows.UI.Xaml.Input.KeyboardNavigationMode) -> Void: ...
    @winrt_mixinmethod
    def add_GettingFocus(self: win32more.Windows.UI.Xaml.IUIElement5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GettingFocus(self: win32more.Windows.UI.Xaml.IUIElement5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LosingFocus(self: win32more.Windows.UI.Xaml.IUIElement5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LosingFocus(self: win32more.Windows.UI.Xaml.IUIElement5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NoFocusCandidateFound(self: win32more.Windows.UI.Xaml.IUIElement5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.NoFocusCandidateFoundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NoFocusCandidateFound(self: win32more.Windows.UI.Xaml.IUIElement5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartBringIntoView(self: win32more.Windows.UI.Xaml.IUIElement5) -> Void: ...
    @winrt_mixinmethod
    def StartBringIntoViewWithOptions(self: win32more.Windows.UI.Xaml.IUIElement5, options: win32more.Windows.UI.Xaml.BringIntoViewOptions) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAccelerators(self: win32more.Windows.UI.Xaml.IUIElement7) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_mixinmethod
    def add_CharacterReceived(self: win32more.Windows.UI.Xaml.IUIElement7, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.CharacterReceivedRoutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CharacterReceived(self: win32more.Windows.UI.Xaml.IUIElement7, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProcessKeyboardAccelerators(self: win32more.Windows.UI.Xaml.IUIElement7, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProcessKeyboardAccelerators(self: win32more.Windows.UI.Xaml.IUIElement7, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PreviewKeyDown(self: win32more.Windows.UI.Xaml.IUIElement7, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PreviewKeyDown(self: win32more.Windows.UI.Xaml.IUIElement7, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PreviewKeyUp(self: win32more.Windows.UI.Xaml.IUIElement7, handler: win32more.Windows.UI.Xaml.Input.KeyEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PreviewKeyUp(self: win32more.Windows.UI.Xaml.IUIElement7, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryInvokeKeyboardAccelerator(self: win32more.Windows.UI.Xaml.IUIElement7, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTipTarget(self: win32more.Windows.UI.Xaml.IUIElement8) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_KeyTipTarget(self: win32more.Windows.UI.Xaml.IUIElement8, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAcceleratorPlacementTarget(self: win32more.Windows.UI.Xaml.IUIElement8) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_KeyboardAcceleratorPlacementTarget(self: win32more.Windows.UI.Xaml.IUIElement8, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAcceleratorPlacementMode(self: win32more.Windows.UI.Xaml.IUIElement8) -> win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode: ...
    @winrt_mixinmethod
    def put_KeyboardAcceleratorPlacementMode(self: win32more.Windows.UI.Xaml.IUIElement8, value: win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def add_BringIntoViewRequested(self: win32more.Windows.UI.Xaml.IUIElement8, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.UIElement, win32more.Windows.UI.Xaml.BringIntoViewRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BringIntoViewRequested(self: win32more.Windows.UI.Xaml.IUIElement8, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CanBeScrollAnchor(self: win32more.Windows.UI.Xaml.IUIElement9) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanBeScrollAnchor(self: win32more.Windows.UI.Xaml.IUIElement9, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OpacityTransition(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.UI.Xaml.ScalarTransition: ...
    @winrt_mixinmethod
    def put_OpacityTransition(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_mixinmethod
    def get_Translation(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Translation(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationTransition(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.UI.Xaml.Vector3Transition: ...
    @winrt_mixinmethod
    def put_TranslationTransition(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: win32more.Windows.UI.Xaml.IUIElement9) -> Single: ...
    @winrt_mixinmethod
    def put_Rotation(self: win32more.Windows.UI.Xaml.IUIElement9, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationTransition(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.UI.Xaml.ScalarTransition: ...
    @winrt_mixinmethod
    def put_RotationTransition(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleTransition(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.UI.Xaml.Vector3Transition: ...
    @winrt_mixinmethod
    def put_ScaleTransition(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAxis(self: win32more.Windows.UI.Xaml.IUIElement9) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RotationAxis(self: win32more.Windows.UI.Xaml.IUIElement9, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def StartAnimation(self: win32more.Windows.UI.Xaml.IUIElement9, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def StopAnimation(self: win32more.Windows.UI.Xaml.IUIElement9, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def get_ActualOffset(self: win32more.Windows.UI.Xaml.IUIElement10) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ActualSize(self: win32more.Windows.UI.Xaml.IUIElement10) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_XamlRoot(self: win32more.Windows.UI.Xaml.IUIElement10) -> win32more.Windows.UI.Xaml.XamlRoot: ...
    @winrt_mixinmethod
    def put_XamlRoot(self: win32more.Windows.UI.Xaml.IUIElement10, value: win32more.Windows.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_mixinmethod
    def get_UIContext(self: win32more.Windows.UI.Xaml.IUIElement10) -> win32more.Windows.UI.UIContext: ...
    @winrt_mixinmethod
    def get_Shadow(self: win32more.Windows.UI.Xaml.IUIElement10) -> win32more.Windows.UI.Xaml.Media.Shadow: ...
    @winrt_mixinmethod
    def put_Shadow(self: win32more.Windows.UI.Xaml.IUIElement10, value: win32more.Windows.UI.Xaml.Media.Shadow) -> Void: ...
    @winrt_mixinmethod
    def OnCreateAutomationPeer(self: win32more.Windows.UI.Xaml.IUIElementOverrides) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def OnDisconnectVisualChildren(self: win32more.Windows.UI.Xaml.IUIElementOverrides) -> Void: ...
    @winrt_mixinmethod
    def FindSubElementsForTouchTargeting(self: win32more.Windows.UI.Xaml.IUIElementOverrides, point: win32more.Windows.Foundation.Point, boundingRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]]: ...
    @winrt_mixinmethod
    def GetChildrenInTabFocusOrder(self: win32more.Windows.UI.Xaml.IUIElementOverrides7) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def OnProcessKeyboardAccelerators(self: win32more.Windows.UI.Xaml.IUIElementOverrides7, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnKeyboardAcceleratorInvoked(self: win32more.Windows.UI.Xaml.IUIElementOverrides8, args: win32more.Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnBringIntoViewRequested(self: win32more.Windows.UI.Xaml.IUIElementOverrides8, e: win32more.Windows.UI.Xaml.BringIntoViewRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfoOverride(self: win32more.Windows.UI.Xaml.IUIElementOverrides9, propertyName: WinRT_String, animationPropertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfo(self: win32more.Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, propertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_classmethod
    def get_ShadowProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics10) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanBeScrollAnchorProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics9) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BringIntoViewRequestedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics8) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ContextRequestedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics8) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_KeyTipTargetProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyboardAcceleratorPlacementTargetProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyboardAcceleratorPlacementModeProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def RegisterAsScrollPort(cls: win32more.Windows.UI.Xaml.IUIElementStatics8, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_PreviewKeyDownEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics7) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_CharacterReceivedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics7) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PreviewKeyUpEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics7) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_GettingFocusEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics6) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_LosingFocusEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics6) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_NoFocusCandidateFoundEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics6) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_LightsProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTipPlacementModeProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTipHorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTipVerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusKeyboardNavigationProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusUpNavigationStrategyProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusDownNavigationStrategyProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusLeftNavigationStrategyProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusRightNavigationStrategyProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HighContrastAdjustmentProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TabFocusNavigationProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContextFlyoutProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitDisplayModeOnAccessKeyInvokedProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsAccessKeyScopeProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AccessKeyScopeOwnerProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Transform3DProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanDragProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def TryStartDirectManipulation(cls: win32more.Windows.UI.Xaml.IUIElementStatics3, value: win32more.Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    @winrt_classmethod
    def get_CompositeModeProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyDownEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_KeyUpEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerEnteredEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerPressedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerMovedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerReleasedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerExitedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerCaptureLostEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerCanceledEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerWheelChangedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_TappedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DoubleTappedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_HoldingEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_RightTappedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationStartingEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationInertiaStartingEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationStartedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationDeltaEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationCompletedEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DragEnterEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DragLeaveEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DragOverEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DropEvent(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_AllowDropProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpacityProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClipProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RenderTransformProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ProjectionProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RenderTransformOriginProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsHitTestVisibleProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibilityProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_UseLayoutRoundingProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransitionsProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CacheModeProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsTapEnabledProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsDoubleTapEnabledProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsRightTapEnabledProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsHoldingEnabledProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ManipulationModeProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerCapturesProperty(cls: win32more.Windows.UI.Xaml.IUIElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AccessKey = property(get_AccessKey, put_AccessKey)
    AccessKeyScopeOwner = property(get_AccessKeyScopeOwner, put_AccessKeyScopeOwner)
    ActualOffset = property(get_ActualOffset, None)
    ActualSize = property(get_ActualSize, None)
    AllowDrop = property(get_AllowDrop, put_AllowDrop)
    CacheMode = property(get_CacheMode, put_CacheMode)
    CanBeScrollAnchor = property(get_CanBeScrollAnchor, put_CanBeScrollAnchor)
    CanDrag = property(get_CanDrag, put_CanDrag)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Clip = property(get_Clip, put_Clip)
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
    ContextFlyout = property(get_ContextFlyout, put_ContextFlyout)
    DesiredSize = property(get_DesiredSize, None)
    ExitDisplayModeOnAccessKeyInvoked = property(get_ExitDisplayModeOnAccessKeyInvoked, put_ExitDisplayModeOnAccessKeyInvoked)
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    IsAccessKeyScope = property(get_IsAccessKeyScope, put_IsAccessKeyScope)
    IsDoubleTapEnabled = property(get_IsDoubleTapEnabled, put_IsDoubleTapEnabled)
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
    IsHoldingEnabled = property(get_IsHoldingEnabled, put_IsHoldingEnabled)
    IsRightTapEnabled = property(get_IsRightTapEnabled, put_IsRightTapEnabled)
    IsTapEnabled = property(get_IsTapEnabled, put_IsTapEnabled)
    KeyTipHorizontalOffset = property(get_KeyTipHorizontalOffset, put_KeyTipHorizontalOffset)
    KeyTipPlacementMode = property(get_KeyTipPlacementMode, put_KeyTipPlacementMode)
    KeyTipTarget = property(get_KeyTipTarget, put_KeyTipTarget)
    KeyTipVerticalOffset = property(get_KeyTipVerticalOffset, put_KeyTipVerticalOffset)
    KeyboardAcceleratorPlacementMode = property(get_KeyboardAcceleratorPlacementMode, put_KeyboardAcceleratorPlacementMode)
    KeyboardAcceleratorPlacementTarget = property(get_KeyboardAcceleratorPlacementTarget, put_KeyboardAcceleratorPlacementTarget)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    Lights = property(get_Lights, None)
    ManipulationMode = property(get_ManipulationMode, put_ManipulationMode)
    Opacity = property(get_Opacity, put_Opacity)
    OpacityTransition = property(get_OpacityTransition, put_OpacityTransition)
    PointerCaptures = property(get_PointerCaptures, None)
    Projection = property(get_Projection, put_Projection)
    RenderSize = property(get_RenderSize, None)
    RenderTransform = property(get_RenderTransform, put_RenderTransform)
    RenderTransformOrigin = property(get_RenderTransformOrigin, put_RenderTransformOrigin)
    Rotation = property(get_Rotation, put_Rotation)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    RotationTransition = property(get_RotationTransition, put_RotationTransition)
    Scale = property(get_Scale, put_Scale)
    ScaleTransition = property(get_ScaleTransition, put_ScaleTransition)
    Shadow = property(get_Shadow, put_Shadow)
    TabFocusNavigation = property(get_TabFocusNavigation, put_TabFocusNavigation)
    Transform3D = property(get_Transform3D, put_Transform3D)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    Transitions = property(get_Transitions, put_Transitions)
    Translation = property(get_Translation, put_Translation)
    TranslationTransition = property(get_TranslationTransition, put_TranslationTransition)
    UIContext = property(get_UIContext, None)
    UseLayoutRounding = property(get_UseLayoutRounding, put_UseLayoutRounding)
    Visibility = property(get_Visibility, put_Visibility)
    XYFocusDownNavigationStrategy = property(get_XYFocusDownNavigationStrategy, put_XYFocusDownNavigationStrategy)
    XYFocusKeyboardNavigation = property(get_XYFocusKeyboardNavigation, put_XYFocusKeyboardNavigation)
    XYFocusLeftNavigationStrategy = property(get_XYFocusLeftNavigationStrategy, put_XYFocusLeftNavigationStrategy)
    XYFocusRightNavigationStrategy = property(get_XYFocusRightNavigationStrategy, put_XYFocusRightNavigationStrategy)
    XYFocusUpNavigationStrategy = property(get_XYFocusUpNavigationStrategy, put_XYFocusUpNavigationStrategy)
    XamlRoot = property(get_XamlRoot, put_XamlRoot)
    _UIElement_Meta_.AccessKeyProperty = property(get_AccessKeyProperty, None)
    _UIElement_Meta_.AccessKeyScopeOwnerProperty = property(get_AccessKeyScopeOwnerProperty, None)
    _UIElement_Meta_.AllowDropProperty = property(get_AllowDropProperty, None)
    _UIElement_Meta_.BringIntoViewRequestedEvent = property(get_BringIntoViewRequestedEvent, None)
    _UIElement_Meta_.CacheModeProperty = property(get_CacheModeProperty, None)
    _UIElement_Meta_.CanBeScrollAnchorProperty = property(get_CanBeScrollAnchorProperty, None)
    _UIElement_Meta_.CanDragProperty = property(get_CanDragProperty, None)
    _UIElement_Meta_.CharacterReceivedEvent = property(get_CharacterReceivedEvent, None)
    _UIElement_Meta_.ClipProperty = property(get_ClipProperty, None)
    _UIElement_Meta_.CompositeModeProperty = property(get_CompositeModeProperty, None)
    _UIElement_Meta_.ContextFlyoutProperty = property(get_ContextFlyoutProperty, None)
    _UIElement_Meta_.ContextRequestedEvent = property(get_ContextRequestedEvent, None)
    _UIElement_Meta_.DoubleTappedEvent = property(get_DoubleTappedEvent, None)
    _UIElement_Meta_.DragEnterEvent = property(get_DragEnterEvent, None)
    _UIElement_Meta_.DragLeaveEvent = property(get_DragLeaveEvent, None)
    _UIElement_Meta_.DragOverEvent = property(get_DragOverEvent, None)
    _UIElement_Meta_.DropEvent = property(get_DropEvent, None)
    _UIElement_Meta_.ExitDisplayModeOnAccessKeyInvokedProperty = property(get_ExitDisplayModeOnAccessKeyInvokedProperty, None)
    _UIElement_Meta_.GettingFocusEvent = property(get_GettingFocusEvent, None)
    _UIElement_Meta_.HighContrastAdjustmentProperty = property(get_HighContrastAdjustmentProperty, None)
    _UIElement_Meta_.HoldingEvent = property(get_HoldingEvent, None)
    _UIElement_Meta_.IsAccessKeyScopeProperty = property(get_IsAccessKeyScopeProperty, None)
    _UIElement_Meta_.IsDoubleTapEnabledProperty = property(get_IsDoubleTapEnabledProperty, None)
    _UIElement_Meta_.IsHitTestVisibleProperty = property(get_IsHitTestVisibleProperty, None)
    _UIElement_Meta_.IsHoldingEnabledProperty = property(get_IsHoldingEnabledProperty, None)
    _UIElement_Meta_.IsRightTapEnabledProperty = property(get_IsRightTapEnabledProperty, None)
    _UIElement_Meta_.IsTapEnabledProperty = property(get_IsTapEnabledProperty, None)
    _UIElement_Meta_.KeyDownEvent = property(get_KeyDownEvent, None)
    _UIElement_Meta_.KeyTipHorizontalOffsetProperty = property(get_KeyTipHorizontalOffsetProperty, None)
    _UIElement_Meta_.KeyTipPlacementModeProperty = property(get_KeyTipPlacementModeProperty, None)
    _UIElement_Meta_.KeyTipTargetProperty = property(get_KeyTipTargetProperty, None)
    _UIElement_Meta_.KeyTipVerticalOffsetProperty = property(get_KeyTipVerticalOffsetProperty, None)
    _UIElement_Meta_.KeyUpEvent = property(get_KeyUpEvent, None)
    _UIElement_Meta_.KeyboardAcceleratorPlacementModeProperty = property(get_KeyboardAcceleratorPlacementModeProperty, None)
    _UIElement_Meta_.KeyboardAcceleratorPlacementTargetProperty = property(get_KeyboardAcceleratorPlacementTargetProperty, None)
    _UIElement_Meta_.LightsProperty = property(get_LightsProperty, None)
    _UIElement_Meta_.LosingFocusEvent = property(get_LosingFocusEvent, None)
    _UIElement_Meta_.ManipulationCompletedEvent = property(get_ManipulationCompletedEvent, None)
    _UIElement_Meta_.ManipulationDeltaEvent = property(get_ManipulationDeltaEvent, None)
    _UIElement_Meta_.ManipulationInertiaStartingEvent = property(get_ManipulationInertiaStartingEvent, None)
    _UIElement_Meta_.ManipulationModeProperty = property(get_ManipulationModeProperty, None)
    _UIElement_Meta_.ManipulationStartedEvent = property(get_ManipulationStartedEvent, None)
    _UIElement_Meta_.ManipulationStartingEvent = property(get_ManipulationStartingEvent, None)
    _UIElement_Meta_.NoFocusCandidateFoundEvent = property(get_NoFocusCandidateFoundEvent, None)
    _UIElement_Meta_.OpacityProperty = property(get_OpacityProperty, None)
    _UIElement_Meta_.PointerCanceledEvent = property(get_PointerCanceledEvent, None)
    _UIElement_Meta_.PointerCaptureLostEvent = property(get_PointerCaptureLostEvent, None)
    _UIElement_Meta_.PointerCapturesProperty = property(get_PointerCapturesProperty, None)
    _UIElement_Meta_.PointerEnteredEvent = property(get_PointerEnteredEvent, None)
    _UIElement_Meta_.PointerExitedEvent = property(get_PointerExitedEvent, None)
    _UIElement_Meta_.PointerMovedEvent = property(get_PointerMovedEvent, None)
    _UIElement_Meta_.PointerPressedEvent = property(get_PointerPressedEvent, None)
    _UIElement_Meta_.PointerReleasedEvent = property(get_PointerReleasedEvent, None)
    _UIElement_Meta_.PointerWheelChangedEvent = property(get_PointerWheelChangedEvent, None)
    _UIElement_Meta_.PreviewKeyDownEvent = property(get_PreviewKeyDownEvent, None)
    _UIElement_Meta_.PreviewKeyUpEvent = property(get_PreviewKeyUpEvent, None)
    _UIElement_Meta_.ProjectionProperty = property(get_ProjectionProperty, None)
    _UIElement_Meta_.RenderTransformOriginProperty = property(get_RenderTransformOriginProperty, None)
    _UIElement_Meta_.RenderTransformProperty = property(get_RenderTransformProperty, None)
    _UIElement_Meta_.RightTappedEvent = property(get_RightTappedEvent, None)
    _UIElement_Meta_.ShadowProperty = property(get_ShadowProperty, None)
    _UIElement_Meta_.TabFocusNavigationProperty = property(get_TabFocusNavigationProperty, None)
    _UIElement_Meta_.TappedEvent = property(get_TappedEvent, None)
    _UIElement_Meta_.Transform3DProperty = property(get_Transform3DProperty, None)
    _UIElement_Meta_.TransitionsProperty = property(get_TransitionsProperty, None)
    _UIElement_Meta_.UseLayoutRoundingProperty = property(get_UseLayoutRoundingProperty, None)
    _UIElement_Meta_.VisibilityProperty = property(get_VisibilityProperty, None)
    _UIElement_Meta_.XYFocusDownNavigationStrategyProperty = property(get_XYFocusDownNavigationStrategyProperty, None)
    _UIElement_Meta_.XYFocusKeyboardNavigationProperty = property(get_XYFocusKeyboardNavigationProperty, None)
    _UIElement_Meta_.XYFocusLeftNavigationStrategyProperty = property(get_XYFocusLeftNavigationStrategyProperty, None)
    _UIElement_Meta_.XYFocusRightNavigationStrategyProperty = property(get_XYFocusRightNavigationStrategyProperty, None)
    _UIElement_Meta_.XYFocusUpNavigationStrategyProperty = property(get_XYFocusUpNavigationStrategyProperty, None)
    KeyUp = event()
    KeyDown = event()
    GotFocus = event()
    LostFocus = event()
    DragEnter = event()
    DragLeave = event()
    DragOver = event()
    Drop = event()
    PointerPressed = event()
    PointerMoved = event()
    PointerReleased = event()
    PointerEntered = event()
    PointerExited = event()
    PointerCaptureLost = event()
    PointerCanceled = event()
    PointerWheelChanged = event()
    Tapped = event()
    DoubleTapped = event()
    Holding = event()
    RightTapped = event()
    ManipulationStarting = event()
    ManipulationInertiaStarting = event()
    ManipulationStarted = event()
    ManipulationDelta = event()
    ManipulationCompleted = event()
    DragStarting = event()
    DropCompleted = event()
    ContextRequested = event()
    ContextCanceled = event()
    AccessKeyDisplayRequested = event()
    AccessKeyDisplayDismissed = event()
    AccessKeyInvoked = event()
    GettingFocus = event()
    LosingFocus = event()
    NoFocusCandidateFound = event()
    CharacterReceived = event()
    ProcessKeyboardAccelerators = event()
    PreviewKeyDown = event()
    PreviewKeyUp = event()
    BringIntoViewRequested = event()
class UIElementWeakCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.UIElement]]
    default_interface: win32more.Windows.UI.Xaml.IUIElementWeakCollection
    _classid_ = 'Windows.UI.Xaml.UIElementWeakCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.UIElementWeakCollection.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IUIElementWeakCollectionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.UIElementWeakCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], index: UInt32) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], value: win32more.Windows.UI.Xaml.UIElement, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], index: UInt32, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], index: UInt32, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.UIElement]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement], items: PassArray[win32more.Windows.UI.Xaml.UIElement]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.UIElement]: ...
    Size = property(get_Size, None)
class UnhandledExceptionEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IUnhandledExceptionEventArgs
    _classid_ = 'Windows.UI.Xaml.UnhandledExceptionEventArgs'
    @winrt_mixinmethod
    def get_Exception(self: win32more.Windows.UI.Xaml.IUnhandledExceptionEventArgs) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.UI.Xaml.IUnhandledExceptionEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.IUnhandledExceptionEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.IUnhandledExceptionEventArgs, value: Boolean) -> Void: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    Message = property(get_Message, None)
class UnhandledExceptionEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9274e6bd-49a1-4958-beee-d0e19587b6e3}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.UnhandledExceptionEventArgs) -> Void: ...
class Vector3Transition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IVector3Transition
    _classid_ = 'Windows.UI.Xaml.Vector3Transition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Vector3Transition.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IVector3TransitionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Vector3Transition: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Xaml.IVector3Transition) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.UI.Xaml.IVector3Transition, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Components(self: win32more.Windows.UI.Xaml.IVector3Transition) -> win32more.Windows.UI.Xaml.Vector3TransitionComponents: ...
    @winrt_mixinmethod
    def put_Components(self: win32more.Windows.UI.Xaml.IVector3Transition, value: win32more.Windows.UI.Xaml.Vector3TransitionComponents) -> Void: ...
    Components = property(get_Components, put_Components)
    Duration = property(get_Duration, put_Duration)
class Vector3TransitionComponents(Enum, UInt32):
    X = 1
    Y = 2
    Z = 4
class VerticalAlignment(Enum, Int32):
    Top = 0
    Center = 1
    Bottom = 2
    Stretch = 3
class Visibility(Enum, Int32):
    Visible = 0
    Collapsed = 1
class VisualState(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IVisualState
    _classid_ = 'Windows.UI.Xaml.VisualState'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.VisualState.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.UI.Xaml.IVisualState) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Storyboard(self: win32more.Windows.UI.Xaml.IVisualState) -> win32more.Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: win32more.Windows.UI.Xaml.IVisualState, value: win32more.Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    @winrt_mixinmethod
    def get_Setters(self: win32more.Windows.UI.Xaml.IVisualState2) -> win32more.Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_mixinmethod
    def get_StateTriggers(self: win32more.Windows.UI.Xaml.IVisualState2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.StateTriggerBase]: ...
    Name = property(get_Name, None)
    Setters = property(get_Setters, None)
    StateTriggers = property(get_StateTriggers, None)
    Storyboard = property(get_Storyboard, put_Storyboard)
class VisualStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IVisualStateChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.VisualStateChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.VisualStateChangedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.VisualStateChangedEventArgs: ...
    @winrt_mixinmethod
    def get_OldState(self: win32more.Windows.UI.Xaml.IVisualStateChangedEventArgs) -> win32more.Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def put_OldState(self: win32more.Windows.UI.Xaml.IVisualStateChangedEventArgs, value: win32more.Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_mixinmethod
    def get_NewState(self: win32more.Windows.UI.Xaml.IVisualStateChangedEventArgs) -> win32more.Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def put_NewState(self: win32more.Windows.UI.Xaml.IVisualStateChangedEventArgs, value: win32more.Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_mixinmethod
    def get_Control(self: win32more.Windows.UI.Xaml.IVisualStateChangedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Control: ...
    @winrt_mixinmethod
    def put_Control(self: win32more.Windows.UI.Xaml.IVisualStateChangedEventArgs, value: win32more.Windows.UI.Xaml.Controls.Control) -> Void: ...
    Control = property(get_Control, put_Control)
    NewState = property(get_NewState, put_NewState)
    OldState = property(get_OldState, put_OldState)
class VisualStateChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e6d5bbd5-e029-43a6-b36d-84a81042d774}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.VisualStateChangedEventArgs) -> Void: ...
class VisualStateGroup(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IVisualStateGroup
    _classid_ = 'Windows.UI.Xaml.VisualStateGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.VisualStateGroup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.VisualStateGroup: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.UI.Xaml.IVisualStateGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Transitions(self: win32more.Windows.UI.Xaml.IVisualStateGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.VisualTransition]: ...
    @winrt_mixinmethod
    def get_States(self: win32more.Windows.UI.Xaml.IVisualStateGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.VisualState]: ...
    @winrt_mixinmethod
    def get_CurrentState(self: win32more.Windows.UI.Xaml.IVisualStateGroup) -> win32more.Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def add_CurrentStateChanged(self: win32more.Windows.UI.Xaml.IVisualStateGroup, handler: win32more.Windows.UI.Xaml.VisualStateChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentStateChanged(self: win32more.Windows.UI.Xaml.IVisualStateGroup, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CurrentStateChanging(self: win32more.Windows.UI.Xaml.IVisualStateGroup, handler: win32more.Windows.UI.Xaml.VisualStateChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentStateChanging(self: win32more.Windows.UI.Xaml.IVisualStateGroup, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentState = property(get_CurrentState, None)
    Name = property(get_Name, None)
    States = property(get_States, None)
    Transitions = property(get_Transitions, None)
    CurrentStateChanged = event()
    CurrentStateChanging = event()
class _VisualStateManager_Meta_(ComPtr.__class__):
    pass
class VisualStateManager(ComPtr, metaclass=_VisualStateManager_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IVisualStateManager
    _classid_ = 'Windows.UI.Xaml.VisualStateManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.VisualStateManager.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IVisualStateManagerFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.VisualStateManager: ...
    @winrt_mixinmethod
    def RaiseCurrentStateChanging(self: win32more.Windows.UI.Xaml.IVisualStateManagerProtected, stateGroup: win32more.Windows.UI.Xaml.VisualStateGroup, oldState: win32more.Windows.UI.Xaml.VisualState, newState: win32more.Windows.UI.Xaml.VisualState, control: win32more.Windows.UI.Xaml.Controls.Control) -> Void: ...
    @winrt_mixinmethod
    def RaiseCurrentStateChanged(self: win32more.Windows.UI.Xaml.IVisualStateManagerProtected, stateGroup: win32more.Windows.UI.Xaml.VisualStateGroup, oldState: win32more.Windows.UI.Xaml.VisualState, newState: win32more.Windows.UI.Xaml.VisualState, control: win32more.Windows.UI.Xaml.Controls.Control) -> Void: ...
    @winrt_mixinmethod
    def GoToStateCore(self: win32more.Windows.UI.Xaml.IVisualStateManagerOverrides, control: win32more.Windows.UI.Xaml.Controls.Control, templateRoot: win32more.Windows.UI.Xaml.FrameworkElement, stateName: WinRT_String, group: win32more.Windows.UI.Xaml.VisualStateGroup, state: win32more.Windows.UI.Xaml.VisualState, useTransitions: Boolean) -> Boolean: ...
    @winrt_classmethod
    def GetVisualStateGroups(cls: win32more.Windows.UI.Xaml.IVisualStateManagerStatics, obj: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.VisualStateGroup]: ...
    @winrt_classmethod
    def get_CustomVisualStateManagerProperty(cls: win32more.Windows.UI.Xaml.IVisualStateManagerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetCustomVisualStateManager(cls: win32more.Windows.UI.Xaml.IVisualStateManagerStatics, obj: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.UI.Xaml.VisualStateManager: ...
    @winrt_classmethod
    def SetCustomVisualStateManager(cls: win32more.Windows.UI.Xaml.IVisualStateManagerStatics, obj: win32more.Windows.UI.Xaml.FrameworkElement, value: win32more.Windows.UI.Xaml.VisualStateManager) -> Void: ...
    @winrt_classmethod
    def GoToState(cls: win32more.Windows.UI.Xaml.IVisualStateManagerStatics, control: win32more.Windows.UI.Xaml.Controls.Control, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
    _VisualStateManager_Meta_.CustomVisualStateManagerProperty = property(get_CustomVisualStateManagerProperty, None)
class VisualTransition(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.IVisualTransition
    _classid_ = 'Windows.UI.Xaml.VisualTransition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.VisualTransition.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.IVisualTransitionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.VisualTransition: ...
    @winrt_mixinmethod
    def get_GeneratedDuration(self: win32more.Windows.UI.Xaml.IVisualTransition) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_mixinmethod
    def put_GeneratedDuration(self: win32more.Windows.UI.Xaml.IVisualTransition, value: win32more.Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_mixinmethod
    def get_GeneratedEasingFunction(self: win32more.Windows.UI.Xaml.IVisualTransition) -> win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_GeneratedEasingFunction(self: win32more.Windows.UI.Xaml.IVisualTransition, value: win32more.Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.UI.Xaml.IVisualTransition) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Windows.UI.Xaml.IVisualTransition, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.UI.Xaml.IVisualTransition) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Windows.UI.Xaml.IVisualTransition, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Storyboard(self: win32more.Windows.UI.Xaml.IVisualTransition) -> win32more.Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: win32more.Windows.UI.Xaml.IVisualTransition, value: win32more.Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    From = property(get_From, put_From)
    GeneratedDuration = property(get_GeneratedDuration, put_GeneratedDuration)
    GeneratedEasingFunction = property(get_GeneratedEasingFunction, put_GeneratedEasingFunction)
    Storyboard = property(get_Storyboard, put_Storyboard)
    To = property(get_To, put_To)
class _Window_Meta_(ComPtr.__class__):
    pass
class Window(ComPtr, metaclass=_Window_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IWindow
    _classid_ = 'Windows.UI.Xaml.Window'
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.UI.Xaml.IWindow) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.UI.Xaml.IWindow) -> Boolean: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Xaml.IWindow) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.UI.Xaml.IWindow, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_CoreWindow(self: win32more.Windows.UI.Xaml.IWindow) -> win32more.Windows.UI.Core.CoreWindow: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: win32more.Windows.UI.Xaml.IWindow) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Windows.UI.Xaml.IWindow, handler: win32more.Windows.UI.Xaml.WindowActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Windows.UI.Xaml.IWindow, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.UI.Xaml.IWindow, handler: win32more.Windows.UI.Xaml.WindowClosedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.UI.Xaml.IWindow, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SizeChanged(self: win32more.Windows.UI.Xaml.IWindow, handler: win32more.Windows.UI.Xaml.WindowSizeChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SizeChanged(self: win32more.Windows.UI.Xaml.IWindow, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VisibilityChanged(self: win32more.Windows.UI.Xaml.IWindow, handler: win32more.Windows.UI.Xaml.WindowVisibilityChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisibilityChanged(self: win32more.Windows.UI.Xaml.IWindow, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Activate(self: win32more.Windows.UI.Xaml.IWindow) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.UI.Xaml.IWindow) -> Void: ...
    @winrt_mixinmethod
    def SetTitleBar(self: win32more.Windows.UI.Xaml.IWindow2, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_Compositor(self: win32more.Windows.UI.Xaml.IWindow3) -> win32more.Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def get_UIContext(self: win32more.Windows.UI.Xaml.IWindow4) -> win32more.Windows.UI.UIContext: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.UI.Xaml.IWindowStatics) -> win32more.Windows.UI.Xaml.Window: ...
    Bounds = property(get_Bounds, None)
    Compositor = property(get_Compositor, None)
    Content = property(get_Content, put_Content)
    CoreWindow = property(get_CoreWindow, None)
    Dispatcher = property(get_Dispatcher, None)
    UIContext = property(get_UIContext, None)
    Visible = property(get_Visible, None)
    _Window_Meta_.Current = property(get_Current, None)
    Activated = event()
    Closed = event()
    SizeChanged = event()
    VisibilityChanged = event()
class WindowActivatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18026348-8619-4c7b-b534-ced45d9de219}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Core.WindowActivatedEventArgs) -> Void: ...
class WindowClosedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0db89161-20d7-45df-9122-ba89576703ba}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Core.CoreWindowEventArgs) -> Void: ...
class WindowCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IWindowCreatedEventArgs
    _classid_ = 'Windows.UI.Xaml.WindowCreatedEventArgs'
    @winrt_mixinmethod
    def get_Window(self: win32more.Windows.UI.Xaml.IWindowCreatedEventArgs) -> win32more.Windows.UI.Xaml.Window: ...
    Window = property(get_Window, None)
class WindowSizeChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5c21c742-2ced-4fd9-ba38-7118d40e966b}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Core.WindowSizeChangedEventArgs) -> Void: ...
class WindowVisibilityChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10406ad6-b090-4a4a-b2ad-d682df27130f}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Core.VisibilityChangedEventArgs) -> Void: ...
class XamlRoot(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IXamlRoot
    _classid_ = 'Windows.UI.Xaml.XamlRoot'
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Xaml.IXamlRoot) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Xaml.IXamlRoot) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_RasterizationScale(self: win32more.Windows.UI.Xaml.IXamlRoot) -> Double: ...
    @winrt_mixinmethod
    def get_IsHostVisible(self: win32more.Windows.UI.Xaml.IXamlRoot) -> Boolean: ...
    @winrt_mixinmethod
    def get_UIContext(self: win32more.Windows.UI.Xaml.IXamlRoot) -> win32more.Windows.UI.UIContext: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.UI.Xaml.IXamlRoot, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.XamlRoot, win32more.Windows.UI.Xaml.XamlRootChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.UI.Xaml.IXamlRoot, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Content = property(get_Content, None)
    IsHostVisible = property(get_IsHostVisible, None)
    RasterizationScale = property(get_RasterizationScale, None)
    Size = property(get_Size, None)
    UIContext = property(get_UIContext, None)
    Changed = event()
class XamlRootChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.IXamlRootChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.XamlRootChangedEventArgs'


make_ready(__name__)
