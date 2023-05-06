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
import Windows.ApplicationModel
import Windows.ApplicationModel.Activation
import Windows.ApplicationModel.Core
import Windows.ApplicationModel.DataTransfer
import Windows.ApplicationModel.DataTransfer.DragDrop
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics.Imaging
import Windows.UI
import Windows.UI.Composition
import Windows.UI.Core
import Windows.UI.Input
import Windows.UI.Xaml
import Windows.UI.Xaml.Automation.Peers
import Windows.UI.Xaml.Controls
import Windows.UI.Xaml.Controls.Primitives
import Windows.UI.Xaml.Data
import Windows.UI.Xaml.Input
import Windows.UI.Xaml.Interop
import Windows.UI.Xaml.Media
import Windows.UI.Xaml.Media.Animation
import Windows.UI.Xaml.Media.Imaging
import Windows.UI.Xaml.Media.Media3D
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _AdaptiveTrigger_Meta_(ComPtr.__class__):
    pass
class AdaptiveTrigger(ComPtr, metaclass=_AdaptiveTrigger_Meta_):
    extends: Windows.UI.Xaml.StateTriggerBase
    default_interface: Windows.UI.Xaml.IAdaptiveTrigger
    _classid_ = 'Windows.UI.Xaml.AdaptiveTrigger'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IAdaptiveTriggerFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.AdaptiveTrigger: ...
    @winrt_mixinmethod
    def get_MinWindowWidth(self: Windows.UI.Xaml.IAdaptiveTrigger) -> Double: ...
    @winrt_mixinmethod
    def put_MinWindowWidth(self: Windows.UI.Xaml.IAdaptiveTrigger, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MinWindowHeight(self: Windows.UI.Xaml.IAdaptiveTrigger) -> Double: ...
    @winrt_mixinmethod
    def put_MinWindowHeight(self: Windows.UI.Xaml.IAdaptiveTrigger, value: Double) -> Void: ...
    @winrt_classmethod
    def get_MinWindowWidthProperty(cls: Windows.UI.Xaml.IAdaptiveTriggerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinWindowHeightProperty(cls: Windows.UI.Xaml.IAdaptiveTriggerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    MinWindowWidth = property(get_MinWindowWidth, put_MinWindowWidth)
    MinWindowHeight = property(get_MinWindowHeight, put_MinWindowHeight)
    _AdaptiveTrigger_Meta_.MinWindowWidthProperty = property(get_MinWindowWidthProperty.__wrapped__, None)
    _AdaptiveTrigger_Meta_.MinWindowHeightProperty = property(get_MinWindowHeightProperty.__wrapped__, None)
class _Application_Meta_(ComPtr.__class__):
    pass
class Application(ComPtr, metaclass=_Application_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IApplication
    _classid_ = 'Windows.UI.Xaml.Application'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IApplicationFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Application: ...
    @winrt_mixinmethod
    def get_Resources(self: Windows.UI.Xaml.IApplication) -> Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_mixinmethod
    def put_Resources(self: Windows.UI.Xaml.IApplication, value: Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_mixinmethod
    def get_DebugSettings(self: Windows.UI.Xaml.IApplication) -> Windows.UI.Xaml.DebugSettings: ...
    @winrt_mixinmethod
    def get_RequestedTheme(self: Windows.UI.Xaml.IApplication) -> Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_mixinmethod
    def put_RequestedTheme(self: Windows.UI.Xaml.IApplication, value: Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_mixinmethod
    def add_UnhandledException(self: Windows.UI.Xaml.IApplication, handler: Windows.UI.Xaml.UnhandledExceptionEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnhandledException(self: Windows.UI.Xaml.IApplication, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Suspending(self: Windows.UI.Xaml.IApplication, handler: Windows.UI.Xaml.SuspendingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Suspending(self: Windows.UI.Xaml.IApplication, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Resuming(self: Windows.UI.Xaml.IApplication, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Resuming(self: Windows.UI.Xaml.IApplication, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Exit(self: Windows.UI.Xaml.IApplication) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualKind(self: Windows.UI.Xaml.IApplication2) -> Windows.UI.Xaml.FocusVisualKind: ...
    @winrt_mixinmethod
    def put_FocusVisualKind(self: Windows.UI.Xaml.IApplication2, value: Windows.UI.Xaml.FocusVisualKind) -> Void: ...
    @winrt_mixinmethod
    def get_RequiresPointerMode(self: Windows.UI.Xaml.IApplication2) -> Windows.UI.Xaml.ApplicationRequiresPointerMode: ...
    @winrt_mixinmethod
    def put_RequiresPointerMode(self: Windows.UI.Xaml.IApplication2, value: Windows.UI.Xaml.ApplicationRequiresPointerMode) -> Void: ...
    @winrt_mixinmethod
    def add_LeavingBackground(self: Windows.UI.Xaml.IApplication2, handler: Windows.UI.Xaml.LeavingBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LeavingBackground(self: Windows.UI.Xaml.IApplication2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnteredBackground(self: Windows.UI.Xaml.IApplication2, handler: Windows.UI.Xaml.EnteredBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnteredBackground(self: Windows.UI.Xaml.IApplication2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HighContrastAdjustment(self: Windows.UI.Xaml.IApplication3) -> Windows.UI.Xaml.ApplicationHighContrastAdjustment: ...
    @winrt_mixinmethod
    def put_HighContrastAdjustment(self: Windows.UI.Xaml.IApplication3, value: Windows.UI.Xaml.ApplicationHighContrastAdjustment) -> Void: ...
    @winrt_mixinmethod
    def OnActivated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnLaunched(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.LaunchActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnFileActivated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.FileActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnSearchActivated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.SearchActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnShareTargetActivated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.ShareTargetActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnFileOpenPickerActivated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.FileOpenPickerActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnFileSavePickerActivated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.FileSavePickerActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnCachedFileUpdaterActivated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.ApplicationModel.Activation.CachedFileUpdaterActivatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnWindowCreated(self: Windows.UI.Xaml.IApplicationOverrides, args: Windows.UI.Xaml.WindowCreatedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnBackgroundActivated(self: Windows.UI.Xaml.IApplicationOverrides2, args: Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs) -> Void: ...
    @winrt_classmethod
    def get_Current(cls: Windows.UI.Xaml.IApplicationStatics) -> Windows.UI.Xaml.Application: ...
    @winrt_classmethod
    def Start(cls: Windows.UI.Xaml.IApplicationStatics, callback: Windows.UI.Xaml.ApplicationInitializationCallback) -> Void: ...
    @winrt_classmethod
    def LoadComponent(cls: Windows.UI.Xaml.IApplicationStatics, component: Windows.Win32.System.WinRT.IInspectable_head, resourceLocator: Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def LoadComponentWithResourceLocation(cls: Windows.UI.Xaml.IApplicationStatics, component: Windows.Win32.System.WinRT.IInspectable_head, resourceLocator: Windows.Foundation.Uri, componentResourceLocation: Windows.UI.Xaml.Controls.Primitives.ComponentResourceLocation) -> Void: ...
    Resources = property(get_Resources, put_Resources)
    DebugSettings = property(get_DebugSettings, None)
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
    FocusVisualKind = property(get_FocusVisualKind, put_FocusVisualKind)
    RequiresPointerMode = property(get_RequiresPointerMode, put_RequiresPointerMode)
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    _Application_Meta_.Current = property(get_Current.__wrapped__, None)
ApplicationHighContrastAdjustment = UInt32
ApplicationHighContrastAdjustment_None: ApplicationHighContrastAdjustment = 0
ApplicationHighContrastAdjustment_Auto: ApplicationHighContrastAdjustment = 4294967295
class ApplicationInitializationCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.ApplicationInitializationCallback'
    _iid_ = Guid('{b6351c55-c284-46e4-8310-fb0967fab76f}')
    @winrt_commethod(3)
    def Invoke(self, p: Windows.UI.Xaml.ApplicationInitializationCallbackParams) -> Void: ...
class ApplicationInitializationCallbackParams(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IApplicationInitializationCallbackParams
    _classid_ = 'Windows.UI.Xaml.ApplicationInitializationCallbackParams'
ApplicationRequiresPointerMode = Int32
ApplicationRequiresPointerMode_Auto: ApplicationRequiresPointerMode = 0
ApplicationRequiresPointerMode_WhenRequested: ApplicationRequiresPointerMode = 1
ApplicationTheme = Int32
ApplicationTheme_Light: ApplicationTheme = 0
ApplicationTheme_Dark: ApplicationTheme = 1
AutomationTextAttributesEnum = Int32
AutomationTextAttributesEnum_AnimationStyleAttribute: AutomationTextAttributesEnum = 40000
AutomationTextAttributesEnum_BackgroundColorAttribute: AutomationTextAttributesEnum = 40001
AutomationTextAttributesEnum_BulletStyleAttribute: AutomationTextAttributesEnum = 40002
AutomationTextAttributesEnum_CapStyleAttribute: AutomationTextAttributesEnum = 40003
AutomationTextAttributesEnum_CultureAttribute: AutomationTextAttributesEnum = 40004
AutomationTextAttributesEnum_FontNameAttribute: AutomationTextAttributesEnum = 40005
AutomationTextAttributesEnum_FontSizeAttribute: AutomationTextAttributesEnum = 40006
AutomationTextAttributesEnum_FontWeightAttribute: AutomationTextAttributesEnum = 40007
AutomationTextAttributesEnum_ForegroundColorAttribute: AutomationTextAttributesEnum = 40008
AutomationTextAttributesEnum_HorizontalTextAlignmentAttribute: AutomationTextAttributesEnum = 40009
AutomationTextAttributesEnum_IndentationFirstLineAttribute: AutomationTextAttributesEnum = 40010
AutomationTextAttributesEnum_IndentationLeadingAttribute: AutomationTextAttributesEnum = 40011
AutomationTextAttributesEnum_IndentationTrailingAttribute: AutomationTextAttributesEnum = 40012
AutomationTextAttributesEnum_IsHiddenAttribute: AutomationTextAttributesEnum = 40013
AutomationTextAttributesEnum_IsItalicAttribute: AutomationTextAttributesEnum = 40014
AutomationTextAttributesEnum_IsReadOnlyAttribute: AutomationTextAttributesEnum = 40015
AutomationTextAttributesEnum_IsSubscriptAttribute: AutomationTextAttributesEnum = 40016
AutomationTextAttributesEnum_IsSuperscriptAttribute: AutomationTextAttributesEnum = 40017
AutomationTextAttributesEnum_MarginBottomAttribute: AutomationTextAttributesEnum = 40018
AutomationTextAttributesEnum_MarginLeadingAttribute: AutomationTextAttributesEnum = 40019
AutomationTextAttributesEnum_MarginTopAttribute: AutomationTextAttributesEnum = 40020
AutomationTextAttributesEnum_MarginTrailingAttribute: AutomationTextAttributesEnum = 40021
AutomationTextAttributesEnum_OutlineStylesAttribute: AutomationTextAttributesEnum = 40022
AutomationTextAttributesEnum_OverlineColorAttribute: AutomationTextAttributesEnum = 40023
AutomationTextAttributesEnum_OverlineStyleAttribute: AutomationTextAttributesEnum = 40024
AutomationTextAttributesEnum_StrikethroughColorAttribute: AutomationTextAttributesEnum = 40025
AutomationTextAttributesEnum_StrikethroughStyleAttribute: AutomationTextAttributesEnum = 40026
AutomationTextAttributesEnum_TabsAttribute: AutomationTextAttributesEnum = 40027
AutomationTextAttributesEnum_TextFlowDirectionsAttribute: AutomationTextAttributesEnum = 40028
AutomationTextAttributesEnum_UnderlineColorAttribute: AutomationTextAttributesEnum = 40029
AutomationTextAttributesEnum_UnderlineStyleAttribute: AutomationTextAttributesEnum = 40030
AutomationTextAttributesEnum_AnnotationTypesAttribute: AutomationTextAttributesEnum = 40031
AutomationTextAttributesEnum_AnnotationObjectsAttribute: AutomationTextAttributesEnum = 40032
AutomationTextAttributesEnum_StyleNameAttribute: AutomationTextAttributesEnum = 40033
AutomationTextAttributesEnum_StyleIdAttribute: AutomationTextAttributesEnum = 40034
AutomationTextAttributesEnum_LinkAttribute: AutomationTextAttributesEnum = 40035
AutomationTextAttributesEnum_IsActiveAttribute: AutomationTextAttributesEnum = 40036
AutomationTextAttributesEnum_SelectionActiveEndAttribute: AutomationTextAttributesEnum = 40037
AutomationTextAttributesEnum_CaretPositionAttribute: AutomationTextAttributesEnum = 40038
AutomationTextAttributesEnum_CaretBidiModeAttribute: AutomationTextAttributesEnum = 40039
class BindingFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IBindingFailedEventArgs
    _classid_ = 'Windows.UI.Xaml.BindingFailedEventArgs'
    @winrt_mixinmethod
    def get_Message(self: Windows.UI.Xaml.IBindingFailedEventArgs) -> WinRT_String: ...
    Message = property(get_Message, None)
class BindingFailedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.BindingFailedEventHandler'
    _iid_ = Guid('{136b1782-54ba-420d-a1aa-82828721cde6}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.BindingFailedEventArgs) -> Void: ...
class BringIntoViewOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IBringIntoViewOptions
    _classid_ = 'Windows.UI.Xaml.BringIntoViewOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.BringIntoViewOptions: ...
    @winrt_mixinmethod
    def get_AnimationDesired(self: Windows.UI.Xaml.IBringIntoViewOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AnimationDesired(self: Windows.UI.Xaml.IBringIntoViewOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TargetRect(self: Windows.UI.Xaml.IBringIntoViewOptions) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_TargetRect(self: Windows.UI.Xaml.IBringIntoViewOptions, value: Windows.Foundation.IReference[Windows.Foundation.Rect]) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalAlignmentRatio(self: Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalAlignmentRatio(self: Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: Windows.UI.Xaml.IBringIntoViewOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: Windows.UI.Xaml.IBringIntoViewOptions2, value: Double) -> Void: ...
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    TargetRect = property(get_TargetRect, put_TargetRect)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
class BringIntoViewRequestedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.BringIntoViewRequestedEventArgs'
    @winrt_mixinmethod
    def get_TargetElement(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_TargetElement(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_AnimationDesired(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_AnimationDesired(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TargetRect(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_TargetRect(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.IBringIntoViewRequestedEventArgs, value: Boolean) -> Void: ...
    TargetElement = property(get_TargetElement, put_TargetElement)
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    TargetRect = property(get_TargetRect, put_TargetRect)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, None)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, None)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    Handled = property(get_Handled, put_Handled)
class BrushTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IBrushTransition
    _classid_ = 'Windows.UI.Xaml.BrushTransition'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IBrushTransitionFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.BrushTransition: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.UI.Xaml.IBrushTransition) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.UI.Xaml.IBrushTransition, value: Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class ColorPaletteResources(ComPtr):
    extends: Windows.UI.Xaml.ResourceDictionary
    default_interface: Windows.UI.Xaml.IColorPaletteResources
    _classid_ = 'Windows.UI.Xaml.ColorPaletteResources'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IColorPaletteResourcesFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ColorPaletteResources: ...
    @winrt_mixinmethod
    def get_AltHigh(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltHigh(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltMedium(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltMedium(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltMediumHigh(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltMediumHigh(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_AltMediumLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_AltMediumLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseHigh(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseHigh(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseMedium(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseMedium(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseMediumHigh(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseMediumHigh(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_BaseMediumLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_BaseMediumLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeAltLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeAltLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackHigh(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackHigh(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackMediumLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackMediumLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeBlackMedium(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeBlackMedium(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeDisabledHigh(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeDisabledHigh(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeDisabledLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeDisabledLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeHigh(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeHigh(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeMedium(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeMedium(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeMediumLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeMediumLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeWhite(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeWhite(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ChromeGray(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ChromeGray(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ListLow(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ListLow(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ListMedium(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ListMedium(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def get_Accent(self: Windows.UI.Xaml.IColorPaletteResources) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_Accent(self: Windows.UI.Xaml.IColorPaletteResources, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
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
    ChromeBlackMediumLow = property(get_ChromeBlackMediumLow, put_ChromeBlackMediumLow)
    ChromeBlackMedium = property(get_ChromeBlackMedium, put_ChromeBlackMedium)
    ChromeDisabledHigh = property(get_ChromeDisabledHigh, put_ChromeDisabledHigh)
    ChromeDisabledLow = property(get_ChromeDisabledLow, put_ChromeDisabledLow)
    ChromeHigh = property(get_ChromeHigh, put_ChromeHigh)
    ChromeLow = property(get_ChromeLow, put_ChromeLow)
    ChromeMedium = property(get_ChromeMedium, put_ChromeMedium)
    ChromeMediumLow = property(get_ChromeMediumLow, put_ChromeMediumLow)
    ChromeWhite = property(get_ChromeWhite, put_ChromeWhite)
    ChromeGray = property(get_ChromeGray, put_ChromeGray)
    ListLow = property(get_ListLow, put_ListLow)
    ListMedium = property(get_ListMedium, put_ListMedium)
    ErrorText = property(get_ErrorText, put_ErrorText)
    Accent = property(get_Accent, put_Accent)
class CornerRadius(EasyCastStructure):
    TopLeft: Double
    TopRight: Double
    BottomRight: Double
    BottomLeft: Double
class CornerRadiusHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.ICornerRadiusHelper
    _classid_ = 'Windows.UI.Xaml.CornerRadiusHelper'
    @winrt_classmethod
    def FromRadii(cls: Windows.UI.Xaml.ICornerRadiusHelperStatics, topLeft: Double, topRight: Double, bottomRight: Double, bottomLeft: Double) -> Windows.UI.Xaml.CornerRadius: ...
    @winrt_classmethod
    def FromUniformRadius(cls: Windows.UI.Xaml.ICornerRadiusHelperStatics, uniformRadius: Double) -> Windows.UI.Xaml.CornerRadius: ...
class CreateDefaultValueCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.CreateDefaultValueCallback'
    _iid_ = Guid('{d6ecb12c-15b5-4ec8-b95c-cdd208f08153}')
    @winrt_commethod(3)
    def Invoke(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class DataContextChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDataContextChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.DataContextChangedEventArgs'
    @winrt_mixinmethod
    def get_NewValue(self: Windows.UI.Xaml.IDataContextChangedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.IDataContextChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.IDataContextChangedEventArgs, value: Boolean) -> Void: ...
    NewValue = property(get_NewValue, None)
    Handled = property(get_Handled, put_Handled)
class _DataTemplate_Meta_(ComPtr.__class__):
    pass
class DataTemplate(ComPtr, metaclass=_DataTemplate_Meta_):
    extends: Windows.UI.Xaml.FrameworkTemplate
    default_interface: Windows.UI.Xaml.IDataTemplate
    _classid_ = 'Windows.UI.Xaml.DataTemplate'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IDataTemplateFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DataTemplate: ...
    @winrt_mixinmethod
    def LoadContent(self: Windows.UI.Xaml.IDataTemplate) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def GetElement(self: Windows.UI.Xaml.IElementFactory, args: Windows.UI.Xaml.ElementFactoryGetArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def RecycleElement(self: Windows.UI.Xaml.IElementFactory, args: Windows.UI.Xaml.ElementFactoryRecycleArgs) -> Void: ...
    @winrt_classmethod
    def get_ExtensionInstanceProperty(cls: Windows.UI.Xaml.IDataTemplateStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetExtensionInstance(cls: Windows.UI.Xaml.IDataTemplateStatics2, element: Windows.UI.Xaml.FrameworkElement) -> Windows.UI.Xaml.IDataTemplateExtension: ...
    @winrt_classmethod
    def SetExtensionInstance(cls: Windows.UI.Xaml.IDataTemplateStatics2, element: Windows.UI.Xaml.FrameworkElement, value: Windows.UI.Xaml.IDataTemplateExtension) -> Void: ...
    _DataTemplate_Meta_.ExtensionInstanceProperty = property(get_ExtensionInstanceProperty.__wrapped__, None)
class DataTemplateKey(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDataTemplateKey
    _classid_ = 'Windows.UI.Xaml.DataTemplateKey'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IDataTemplateKeyFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DataTemplateKey: ...
    @winrt_factorymethod
    def CreateInstanceWithType(cls: Windows.UI.Xaml.IDataTemplateKeyFactory, dataType: Windows.Win32.System.WinRT.IInspectable_head, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DataTemplateKey: ...
    @winrt_mixinmethod
    def get_DataType(self: Windows.UI.Xaml.IDataTemplateKey) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_DataType(self: Windows.UI.Xaml.IDataTemplateKey, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    DataType = property(get_DataType, put_DataType)
class DebugSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDebugSettings
    _classid_ = 'Windows.UI.Xaml.DebugSettings'
    @winrt_mixinmethod
    def get_EnableFrameRateCounter(self: Windows.UI.Xaml.IDebugSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableFrameRateCounter(self: Windows.UI.Xaml.IDebugSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBindingTracingEnabled(self: Windows.UI.Xaml.IDebugSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBindingTracingEnabled(self: Windows.UI.Xaml.IDebugSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsOverdrawHeatMapEnabled(self: Windows.UI.Xaml.IDebugSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOverdrawHeatMapEnabled(self: Windows.UI.Xaml.IDebugSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_BindingFailed(self: Windows.UI.Xaml.IDebugSettings, handler: Windows.UI.Xaml.BindingFailedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BindingFailed(self: Windows.UI.Xaml.IDebugSettings, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_EnableRedrawRegions(self: Windows.UI.Xaml.IDebugSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableRedrawRegions(self: Windows.UI.Xaml.IDebugSettings2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsTextPerformanceVisualizationEnabled(self: Windows.UI.Xaml.IDebugSettings3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTextPerformanceVisualizationEnabled(self: Windows.UI.Xaml.IDebugSettings3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FailFastOnErrors(self: Windows.UI.Xaml.IDebugSettings4) -> Boolean: ...
    @winrt_mixinmethod
    def put_FailFastOnErrors(self: Windows.UI.Xaml.IDebugSettings4, value: Boolean) -> Void: ...
    EnableFrameRateCounter = property(get_EnableFrameRateCounter, put_EnableFrameRateCounter)
    IsBindingTracingEnabled = property(get_IsBindingTracingEnabled, put_IsBindingTracingEnabled)
    IsOverdrawHeatMapEnabled = property(get_IsOverdrawHeatMapEnabled, put_IsOverdrawHeatMapEnabled)
    EnableRedrawRegions = property(get_EnableRedrawRegions, put_EnableRedrawRegions)
    IsTextPerformanceVisualizationEnabled = property(get_IsTextPerformanceVisualizationEnabled, put_IsTextPerformanceVisualizationEnabled)
    FailFastOnErrors = property(get_FailFastOnErrors, put_FailFastOnErrors)
class DependencyObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDependencyObject
    _classid_ = 'Windows.UI.Xaml.DependencyObject'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IDependencyObjectFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def GetValue(self: Windows.UI.Xaml.IDependencyObject, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def SetValue(self: Windows.UI.Xaml.IDependencyObject, dp: Windows.UI.Xaml.DependencyProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def ClearValue(self: Windows.UI.Xaml.IDependencyObject, dp: Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_mixinmethod
    def ReadLocalValue(self: Windows.UI.Xaml.IDependencyObject, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetAnimationBaseValue(self: Windows.UI.Xaml.IDependencyObject, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.UI.Xaml.IDependencyObject) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def RegisterPropertyChangedCallback(self: Windows.UI.Xaml.IDependencyObject2, dp: Windows.UI.Xaml.DependencyProperty, callback: Windows.UI.Xaml.DependencyPropertyChangedCallback) -> Int64: ...
    @winrt_mixinmethod
    def UnregisterPropertyChangedCallback(self: Windows.UI.Xaml.IDependencyObject2, dp: Windows.UI.Xaml.DependencyProperty, token: Int64) -> Void: ...
    Dispatcher = property(get_Dispatcher, None)
class DependencyObjectCollection(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.Foundation.Collections.IObservableVector[Windows.UI.Xaml.DependencyObject]
    _classid_ = 'Windows.UI.Xaml.DependencyObjectCollection'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IDependencyObjectCollectionFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DependencyObjectCollection: ...
    @winrt_mixinmethod
    def add_VectorChanged(self: Windows.Foundation.Collections.IObservableVector[Windows.UI.Xaml.DependencyObject], vhnd: Windows.Foundation.Collections.VectorChangedEventHandler[Windows.UI.Xaml.DependencyObject]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VectorChanged(self: Windows.Foundation.Collections.IObservableVector[Windows.UI.Xaml.DependencyObject], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], index: UInt32) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], value: Windows.UI.Xaml.DependencyObject, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], index: UInt32, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], index: UInt32, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.DependencyObject)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject], items: POINTER(Windows.UI.Xaml.DependencyObject)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.DependencyObject]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.DependencyObject]: ...
    Size = property(get_Size, None)
class _DependencyProperty_Meta_(ComPtr.__class__):
    pass
class DependencyProperty(ComPtr, metaclass=_DependencyProperty_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDependencyProperty
    _classid_ = 'Windows.UI.Xaml.DependencyProperty'
    @winrt_mixinmethod
    def GetMetadata(self: Windows.UI.Xaml.IDependencyProperty, forType: Windows.UI.Xaml.Interop.TypeName) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def get_UnsetValue(cls: Windows.UI.Xaml.IDependencyPropertyStatics) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def Register(cls: Windows.UI.Xaml.IDependencyPropertyStatics, name: WinRT_String, propertyType: Windows.UI.Xaml.Interop.TypeName, ownerType: Windows.UI.Xaml.Interop.TypeName, typeMetadata: Windows.UI.Xaml.PropertyMetadata) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def RegisterAttached(cls: Windows.UI.Xaml.IDependencyPropertyStatics, name: WinRT_String, propertyType: Windows.UI.Xaml.Interop.TypeName, ownerType: Windows.UI.Xaml.Interop.TypeName, defaultMetadata: Windows.UI.Xaml.PropertyMetadata) -> Windows.UI.Xaml.DependencyProperty: ...
    _DependencyProperty_Meta_.UnsetValue = property(get_UnsetValue.__wrapped__, None)
class DependencyPropertyChangedCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.DependencyPropertyChangedCallback'
    _iid_ = Guid('{45883d16-27bf-4bc1-ac26-94c1601f3a49}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.UI.Xaml.DependencyObject, dp: Windows.UI.Xaml.DependencyProperty) -> Void: ...
class DependencyPropertyChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDependencyPropertyChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.DependencyPropertyChangedEventArgs'
    @winrt_mixinmethod
    def get_Property(self: Windows.UI.Xaml.IDependencyPropertyChangedEventArgs) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_mixinmethod
    def get_OldValue(self: Windows.UI.Xaml.IDependencyPropertyChangedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_NewValue(self: Windows.UI.Xaml.IDependencyPropertyChangedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Property = property(get_Property, None)
    OldValue = property(get_OldValue, None)
    NewValue = property(get_NewValue, None)
class DependencyPropertyChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.DependencyPropertyChangedEventHandler'
    _iid_ = Guid('{09223e5a-75be-4499-8180-1ddc005421c0}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.DependencyPropertyChangedEventArgs) -> Void: ...
class DispatcherTimer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDispatcherTimer
    _classid_ = 'Windows.UI.Xaml.DispatcherTimer'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IDispatcherTimerFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DispatcherTimer: ...
    @winrt_mixinmethod
    def get_Interval(self: Windows.UI.Xaml.IDispatcherTimer) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Interval(self: Windows.UI.Xaml.IDispatcherTimer, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.UI.Xaml.IDispatcherTimer) -> Boolean: ...
    @winrt_mixinmethod
    def add_Tick(self: Windows.UI.Xaml.IDispatcherTimer, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tick(self: Windows.UI.Xaml.IDispatcherTimer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.UI.Xaml.IDispatcherTimer) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.UI.Xaml.IDispatcherTimer) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsEnabled = property(get_IsEnabled, None)
class DragEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.IDragEventArgs
    _classid_ = 'Windows.UI.Xaml.DragEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.IDragEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.IDragEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.UI.Xaml.IDragEventArgs) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.UI.Xaml.IDragEventArgs, value: Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_mixinmethod
    def GetPosition(self: Windows.UI.Xaml.IDragEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_DataView(self: Windows.UI.Xaml.IDragEventArgs2) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_DragUIOverride(self: Windows.UI.Xaml.IDragEventArgs2) -> Windows.UI.Xaml.DragUIOverride: ...
    @winrt_mixinmethod
    def get_Modifiers(self: Windows.UI.Xaml.IDragEventArgs2) -> Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers: ...
    @winrt_mixinmethod
    def get_AcceptedOperation(self: Windows.UI.Xaml.IDragEventArgs2) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_AcceptedOperation(self: Windows.UI.Xaml.IDragEventArgs2, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.Xaml.IDragEventArgs2) -> Windows.UI.Xaml.DragOperationDeferral: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: Windows.UI.Xaml.IDragEventArgs3) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Handled = property(get_Handled, put_Handled)
    Data = property(get_Data, put_Data)
    DataView = property(get_DataView, None)
    DragUIOverride = property(get_DragUIOverride, None)
    Modifiers = property(get_Modifiers, None)
    AcceptedOperation = property(get_AcceptedOperation, put_AcceptedOperation)
    AllowedOperations = property(get_AllowedOperations, None)
class DragEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.DragEventHandler'
    _iid_ = Guid('{2ab1a205-1e73-4bcf-aabc-57b97e21961d}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.DragEventArgs) -> Void: ...
class DragOperationDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDragOperationDeferral
    _classid_ = 'Windows.UI.Xaml.DragOperationDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.UI.Xaml.IDragOperationDeferral) -> Void: ...
class DragStartingEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.IDragStartingEventArgs
    _classid_ = 'Windows.UI.Xaml.DragStartingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: Windows.UI.Xaml.IDragStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.UI.Xaml.IDragStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.UI.Xaml.IDragStartingEventArgs) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def get_DragUI(self: Windows.UI.Xaml.IDragStartingEventArgs) -> Windows.UI.Xaml.DragUI: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.Xaml.IDragStartingEventArgs) -> Windows.UI.Xaml.DragOperationDeferral: ...
    @winrt_mixinmethod
    def GetPosition(self: Windows.UI.Xaml.IDragStartingEventArgs, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: Windows.UI.Xaml.IDragStartingEventArgs2) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_AllowedOperations(self: Windows.UI.Xaml.IDragStartingEventArgs2, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    Cancel = property(get_Cancel, put_Cancel)
    Data = property(get_Data, None)
    DragUI = property(get_DragUI, None)
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
class DragUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDragUI
    _classid_ = 'Windows.UI.Xaml.DragUI'
    @winrt_mixinmethod
    def SetContentFromBitmapImage(self: Windows.UI.Xaml.IDragUI, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromBitmapImageWithAnchorPoint(self: Windows.UI.Xaml.IDragUI, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmap(self: Windows.UI.Xaml.IDragUI, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmapWithAnchorPoint(self: Windows.UI.Xaml.IDragUI, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromDataPackage(self: Windows.UI.Xaml.IDragUI) -> Void: ...
class DragUIOverride(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDragUIOverride
    _classid_ = 'Windows.UI.Xaml.DragUIOverride'
    @winrt_mixinmethod
    def get_Caption(self: Windows.UI.Xaml.IDragUIOverride) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Caption(self: Windows.UI.Xaml.IDragUIOverride, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsContentVisible(self: Windows.UI.Xaml.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsContentVisible(self: Windows.UI.Xaml.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCaptionVisible(self: Windows.UI.Xaml.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCaptionVisible(self: Windows.UI.Xaml.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsGlyphVisible(self: Windows.UI.Xaml.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGlyphVisible(self: Windows.UI.Xaml.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.UI.Xaml.IDragUIOverride) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromBitmapImage(self: Windows.UI.Xaml.IDragUIOverride, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromBitmapImageWithAnchorPoint(self: Windows.UI.Xaml.IDragUIOverride, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmap(self: Windows.UI.Xaml.IDragUIOverride, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmapWithAnchorPoint(self: Windows.UI.Xaml.IDragUIOverride, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    Caption = property(get_Caption, put_Caption)
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class DropCompletedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.IDropCompletedEventArgs
    _classid_ = 'Windows.UI.Xaml.DropCompletedEventArgs'
    @winrt_mixinmethod
    def get_DropResult(self: Windows.UI.Xaml.IDropCompletedEventArgs) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    DropResult = property(get_DropResult, None)
class Duration(EasyCastStructure):
    TimeSpan: Windows.Foundation.TimeSpan
    Type: Windows.UI.Xaml.DurationType
class _DurationHelper_Meta_(ComPtr.__class__):
    pass
class DurationHelper(ComPtr, metaclass=_DurationHelper_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IDurationHelper
    _classid_ = 'Windows.UI.Xaml.DurationHelper'
    @winrt_classmethod
    def get_Automatic(cls: Windows.UI.Xaml.IDurationHelperStatics) -> Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def get_Forever(cls: Windows.UI.Xaml.IDurationHelperStatics) -> Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def Compare(cls: Windows.UI.Xaml.IDurationHelperStatics, duration1: Windows.UI.Xaml.Duration, duration2: Windows.UI.Xaml.Duration) -> Int32: ...
    @winrt_classmethod
    def FromTimeSpan(cls: Windows.UI.Xaml.IDurationHelperStatics, timeSpan: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def GetHasTimeSpan(cls: Windows.UI.Xaml.IDurationHelperStatics, target: Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_classmethod
    def Add(cls: Windows.UI.Xaml.IDurationHelperStatics, target: Windows.UI.Xaml.Duration, duration: Windows.UI.Xaml.Duration) -> Windows.UI.Xaml.Duration: ...
    @winrt_classmethod
    def Equals(cls: Windows.UI.Xaml.IDurationHelperStatics, target: Windows.UI.Xaml.Duration, value: Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_classmethod
    def Subtract(cls: Windows.UI.Xaml.IDurationHelperStatics, target: Windows.UI.Xaml.Duration, duration: Windows.UI.Xaml.Duration) -> Windows.UI.Xaml.Duration: ...
    _DurationHelper_Meta_.Automatic = property(get_Automatic.__wrapped__, None)
    _DurationHelper_Meta_.Forever = property(get_Forever.__wrapped__, None)
DurationType = Int32
DurationType_Automatic: DurationType = 0
DurationType_TimeSpan: DurationType = 1
DurationType_Forever: DurationType = 2
class EffectiveViewportChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IEffectiveViewportChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.EffectiveViewportChangedEventArgs'
    @winrt_mixinmethod
    def get_EffectiveViewport(self: Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_MaxViewport(self: Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_BringIntoViewDistanceX(self: Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_BringIntoViewDistanceY(self: Windows.UI.Xaml.IEffectiveViewportChangedEventArgs) -> Double: ...
    EffectiveViewport = property(get_EffectiveViewport, None)
    MaxViewport = property(get_MaxViewport, None)
    BringIntoViewDistanceX = property(get_BringIntoViewDistanceX, None)
    BringIntoViewDistanceY = property(get_BringIntoViewDistanceY, None)
class ElementFactoryGetArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IElementFactoryGetArgs
    _classid_ = 'Windows.UI.Xaml.ElementFactoryGetArgs'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IElementFactoryGetArgsFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ElementFactoryGetArgs: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.UI.Xaml.IElementFactoryGetArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.UI.Xaml.IElementFactoryGetArgs, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Xaml.IElementFactoryGetArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Parent(self: Windows.UI.Xaml.IElementFactoryGetArgs, value: Windows.UI.Xaml.UIElement) -> Void: ...
    Data = property(get_Data, put_Data)
    Parent = property(get_Parent, put_Parent)
class ElementFactoryRecycleArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IElementFactoryRecycleArgs
    _classid_ = 'Windows.UI.Xaml.ElementFactoryRecycleArgs'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IElementFactoryRecycleArgsFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ElementFactoryRecycleArgs: ...
    @winrt_mixinmethod
    def get_Element(self: Windows.UI.Xaml.IElementFactoryRecycleArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Element(self: Windows.UI.Xaml.IElementFactoryRecycleArgs, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Xaml.IElementFactoryRecycleArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Parent(self: Windows.UI.Xaml.IElementFactoryRecycleArgs, value: Windows.UI.Xaml.UIElement) -> Void: ...
    Element = property(get_Element, put_Element)
    Parent = property(get_Parent, put_Parent)
ElementHighContrastAdjustment = UInt32
ElementHighContrastAdjustment_None: ElementHighContrastAdjustment = 0
ElementHighContrastAdjustment_Application: ElementHighContrastAdjustment = 2147483648
ElementHighContrastAdjustment_Auto: ElementHighContrastAdjustment = 4294967295
ElementSoundKind = Int32
ElementSoundKind_Focus: ElementSoundKind = 0
ElementSoundKind_Invoke: ElementSoundKind = 1
ElementSoundKind_Show: ElementSoundKind = 2
ElementSoundKind_Hide: ElementSoundKind = 3
ElementSoundKind_MovePrevious: ElementSoundKind = 4
ElementSoundKind_MoveNext: ElementSoundKind = 5
ElementSoundKind_GoBack: ElementSoundKind = 6
ElementSoundMode = Int32
ElementSoundMode_Default: ElementSoundMode = 0
ElementSoundMode_FocusOnly: ElementSoundMode = 1
ElementSoundMode_Off: ElementSoundMode = 2
class _ElementSoundPlayer_Meta_(ComPtr.__class__):
    pass
class ElementSoundPlayer(ComPtr, metaclass=_ElementSoundPlayer_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IElementSoundPlayer
    _classid_ = 'Windows.UI.Xaml.ElementSoundPlayer'
    @winrt_classmethod
    def get_SpatialAudioMode(cls: Windows.UI.Xaml.IElementSoundPlayerStatics2) -> Windows.UI.Xaml.ElementSpatialAudioMode: ...
    @winrt_classmethod
    def put_SpatialAudioMode(cls: Windows.UI.Xaml.IElementSoundPlayerStatics2, value: Windows.UI.Xaml.ElementSpatialAudioMode) -> Void: ...
    @winrt_classmethod
    def get_Volume(cls: Windows.UI.Xaml.IElementSoundPlayerStatics) -> Double: ...
    @winrt_classmethod
    def put_Volume(cls: Windows.UI.Xaml.IElementSoundPlayerStatics, value: Double) -> Void: ...
    @winrt_classmethod
    def get_State(cls: Windows.UI.Xaml.IElementSoundPlayerStatics) -> Windows.UI.Xaml.ElementSoundPlayerState: ...
    @winrt_classmethod
    def put_State(cls: Windows.UI.Xaml.IElementSoundPlayerStatics, value: Windows.UI.Xaml.ElementSoundPlayerState) -> Void: ...
    @winrt_classmethod
    def Play(cls: Windows.UI.Xaml.IElementSoundPlayerStatics, sound: Windows.UI.Xaml.ElementSoundKind) -> Void: ...
    _ElementSoundPlayer_Meta_.SpatialAudioMode = property(get_SpatialAudioMode.__wrapped__, put_SpatialAudioMode.__wrapped__)
    _ElementSoundPlayer_Meta_.Volume = property(get_Volume.__wrapped__, put_Volume.__wrapped__)
    _ElementSoundPlayer_Meta_.State = property(get_State.__wrapped__, put_State.__wrapped__)
ElementSoundPlayerState = Int32
ElementSoundPlayerState_Auto: ElementSoundPlayerState = 0
ElementSoundPlayerState_Off: ElementSoundPlayerState = 1
ElementSoundPlayerState_On: ElementSoundPlayerState = 2
ElementSpatialAudioMode = Int32
ElementSpatialAudioMode_Auto: ElementSpatialAudioMode = 0
ElementSpatialAudioMode_Off: ElementSpatialAudioMode = 1
ElementSpatialAudioMode_On: ElementSpatialAudioMode = 2
ElementTheme = Int32
ElementTheme_Default: ElementTheme = 0
ElementTheme_Light: ElementTheme = 1
ElementTheme_Dark: ElementTheme = 2
class EnteredBackgroundEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.EnteredBackgroundEventHandler'
    _iid_ = Guid('{93a956ae-1d7f-438b-b7b8-227d96b609c0}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.ApplicationModel.EnteredBackgroundEventArgs) -> Void: ...
class EventTrigger(ComPtr):
    extends: Windows.UI.Xaml.TriggerBase
    default_interface: Windows.UI.Xaml.IEventTrigger
    _classid_ = 'Windows.UI.Xaml.EventTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.EventTrigger: ...
    @winrt_mixinmethod
    def get_RoutedEvent(self: Windows.UI.Xaml.IEventTrigger) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_mixinmethod
    def put_RoutedEvent(self: Windows.UI.Xaml.IEventTrigger, value: Windows.UI.Xaml.RoutedEvent) -> Void: ...
    @winrt_mixinmethod
    def get_Actions(self: Windows.UI.Xaml.IEventTrigger) -> Windows.UI.Xaml.TriggerActionCollection: ...
    RoutedEvent = property(get_RoutedEvent, put_RoutedEvent)
    Actions = property(get_Actions, None)
class ExceptionRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.IExceptionRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.ExceptionRoutedEventArgs'
    @winrt_mixinmethod
    def get_ErrorMessage(self: Windows.UI.Xaml.IExceptionRoutedEventArgs) -> WinRT_String: ...
    ErrorMessage = property(get_ErrorMessage, None)
class ExceptionRoutedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.ExceptionRoutedEventHandler'
    _iid_ = Guid('{68e0e810-f6ea-42bc-855b-5d9b67e6a262}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.ExceptionRoutedEventArgs) -> Void: ...
FlowDirection = Int32
FlowDirection_LeftToRight: FlowDirection = 0
FlowDirection_RightToLeft: FlowDirection = 1
FocusState = Int32
FocusState_Unfocused: FocusState = 0
FocusState_Pointer: FocusState = 1
FocusState_Keyboard: FocusState = 2
FocusState_Programmatic: FocusState = 3
FocusVisualKind = Int32
FocusVisualKind_DottedLine: FocusVisualKind = 0
FocusVisualKind_HighVisibility: FocusVisualKind = 1
FocusVisualKind_Reveal: FocusVisualKind = 2
FontCapitals = Int32
FontCapitals_Normal: FontCapitals = 0
FontCapitals_AllSmallCaps: FontCapitals = 1
FontCapitals_SmallCaps: FontCapitals = 2
FontCapitals_AllPetiteCaps: FontCapitals = 3
FontCapitals_PetiteCaps: FontCapitals = 4
FontCapitals_Unicase: FontCapitals = 5
FontCapitals_Titling: FontCapitals = 6
FontEastAsianLanguage = Int32
FontEastAsianLanguage_Normal: FontEastAsianLanguage = 0
FontEastAsianLanguage_HojoKanji: FontEastAsianLanguage = 1
FontEastAsianLanguage_Jis04: FontEastAsianLanguage = 2
FontEastAsianLanguage_Jis78: FontEastAsianLanguage = 3
FontEastAsianLanguage_Jis83: FontEastAsianLanguage = 4
FontEastAsianLanguage_Jis90: FontEastAsianLanguage = 5
FontEastAsianLanguage_NlcKanji: FontEastAsianLanguage = 6
FontEastAsianLanguage_Simplified: FontEastAsianLanguage = 7
FontEastAsianLanguage_Traditional: FontEastAsianLanguage = 8
FontEastAsianLanguage_TraditionalNames: FontEastAsianLanguage = 9
FontEastAsianWidths = Int32
FontEastAsianWidths_Normal: FontEastAsianWidths = 0
FontEastAsianWidths_Full: FontEastAsianWidths = 1
FontEastAsianWidths_Half: FontEastAsianWidths = 2
FontEastAsianWidths_Proportional: FontEastAsianWidths = 3
FontEastAsianWidths_Quarter: FontEastAsianWidths = 4
FontEastAsianWidths_Third: FontEastAsianWidths = 5
FontFraction = Int32
FontFraction_Normal: FontFraction = 0
FontFraction_Stacked: FontFraction = 1
FontFraction_Slashed: FontFraction = 2
FontNumeralAlignment = Int32
FontNumeralAlignment_Normal: FontNumeralAlignment = 0
FontNumeralAlignment_Proportional: FontNumeralAlignment = 1
FontNumeralAlignment_Tabular: FontNumeralAlignment = 2
FontNumeralStyle = Int32
FontNumeralStyle_Normal: FontNumeralStyle = 0
FontNumeralStyle_Lining: FontNumeralStyle = 1
FontNumeralStyle_OldStyle: FontNumeralStyle = 2
FontVariants = Int32
FontVariants_Normal: FontVariants = 0
FontVariants_Superscript: FontVariants = 1
FontVariants_Subscript: FontVariants = 2
FontVariants_Ordinal: FontVariants = 3
FontVariants_Inferior: FontVariants = 4
FontVariants_Ruby: FontVariants = 5
class _FrameworkElement_Meta_(ComPtr.__class__):
    pass
class FrameworkElement(ComPtr, metaclass=_FrameworkElement_Meta_):
    extends: Windows.UI.Xaml.UIElement
    default_interface: Windows.UI.Xaml.IFrameworkElement
    _classid_ = 'Windows.UI.Xaml.FrameworkElement'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IFrameworkElementFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.FrameworkElement: ...
    @winrt_mixinmethod
    def get_Triggers(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.TriggerCollection: ...
    @winrt_mixinmethod
    def get_Resources(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_mixinmethod
    def put_Resources(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.UI.Xaml.IFrameworkElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.UI.Xaml.IFrameworkElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ActualWidth(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def get_ActualHeight(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_Width(self: Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_Height(self: Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MinWidth(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MinWidth(self: Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MaxWidth(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MaxWidth(self: Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MinHeight(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MinHeight(self: Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MaxHeight(self: Windows.UI.Xaml.IFrameworkElement) -> Double: ...
    @winrt_mixinmethod
    def put_MaxHeight(self: Windows.UI.Xaml.IFrameworkElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignment(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_mixinmethod
    def put_HorizontalAlignment(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignment(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_mixinmethod
    def put_VerticalAlignment(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_Margin(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_Margin(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.UI.Xaml.IFrameworkElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.UI.Xaml.IFrameworkElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_DataContext(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_DataContext(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_Style(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.Style: ...
    @winrt_mixinmethod
    def put_Style(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.UI.Xaml.Style) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def get_FlowDirection(self: Windows.UI.Xaml.IFrameworkElement) -> Windows.UI.Xaml.FlowDirection: ...
    @winrt_mixinmethod
    def put_FlowDirection(self: Windows.UI.Xaml.IFrameworkElement, value: Windows.UI.Xaml.FlowDirection) -> Void: ...
    @winrt_mixinmethod
    def add_Loaded(self: Windows.UI.Xaml.IFrameworkElement, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Loaded(self: Windows.UI.Xaml.IFrameworkElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Unloaded(self: Windows.UI.Xaml.IFrameworkElement, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Unloaded(self: Windows.UI.Xaml.IFrameworkElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SizeChanged(self: Windows.UI.Xaml.IFrameworkElement, handler: Windows.UI.Xaml.SizeChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SizeChanged(self: Windows.UI.Xaml.IFrameworkElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LayoutUpdated(self: Windows.UI.Xaml.IFrameworkElement, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LayoutUpdated(self: Windows.UI.Xaml.IFrameworkElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindName(self: Windows.UI.Xaml.IFrameworkElement, name: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def SetBinding(self: Windows.UI.Xaml.IFrameworkElement, dp: Windows.UI.Xaml.DependencyProperty, binding: Windows.UI.Xaml.Data.BindingBase) -> Void: ...
    @winrt_mixinmethod
    def get_RequestedTheme(self: Windows.UI.Xaml.IFrameworkElement2) -> Windows.UI.Xaml.ElementTheme: ...
    @winrt_mixinmethod
    def put_RequestedTheme(self: Windows.UI.Xaml.IFrameworkElement2, value: Windows.UI.Xaml.ElementTheme) -> Void: ...
    @winrt_mixinmethod
    def add_DataContextChanged(self: Windows.UI.Xaml.IFrameworkElement2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.UI.Xaml.DataContextChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataContextChanged(self: Windows.UI.Xaml.IFrameworkElement2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetBindingExpression(self: Windows.UI.Xaml.IFrameworkElement2, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.UI.Xaml.Data.BindingExpression: ...
    @winrt_mixinmethod
    def add_Loading(self: Windows.UI.Xaml.IFrameworkElement3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Loading(self: Windows.UI.Xaml.IFrameworkElement3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllowFocusOnInteraction(self: Windows.UI.Xaml.IFrameworkElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusOnInteraction(self: Windows.UI.Xaml.IFrameworkElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualMargin(self: Windows.UI.Xaml.IFrameworkElement4) -> Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_FocusVisualMargin(self: Windows.UI.Xaml.IFrameworkElement4, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualSecondaryThickness(self: Windows.UI.Xaml.IFrameworkElement4) -> Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_FocusVisualSecondaryThickness(self: Windows.UI.Xaml.IFrameworkElement4, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualPrimaryThickness(self: Windows.UI.Xaml.IFrameworkElement4) -> Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_FocusVisualPrimaryThickness(self: Windows.UI.Xaml.IFrameworkElement4, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualSecondaryBrush(self: Windows.UI.Xaml.IFrameworkElement4) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusVisualSecondaryBrush(self: Windows.UI.Xaml.IFrameworkElement4, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusVisualPrimaryBrush(self: Windows.UI.Xaml.IFrameworkElement4) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusVisualPrimaryBrush(self: Windows.UI.Xaml.IFrameworkElement4, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_AllowFocusWhenDisabled(self: Windows.UI.Xaml.IFrameworkElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusWhenDisabled(self: Windows.UI.Xaml.IFrameworkElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ActualTheme(self: Windows.UI.Xaml.IFrameworkElement6) -> Windows.UI.Xaml.ElementTheme: ...
    @winrt_mixinmethod
    def add_ActualThemeChanged(self: Windows.UI.Xaml.IFrameworkElement6, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualThemeChanged(self: Windows.UI.Xaml.IFrameworkElement6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsLoaded(self: Windows.UI.Xaml.IFrameworkElement7) -> Boolean: ...
    @winrt_mixinmethod
    def add_EffectiveViewportChanged(self: Windows.UI.Xaml.IFrameworkElement7, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.UI.Xaml.EffectiveViewportChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EffectiveViewportChanged(self: Windows.UI.Xaml.IFrameworkElement7, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def InvalidateViewport(self: Windows.UI.Xaml.IFrameworkElementProtected7) -> Void: ...
    @winrt_mixinmethod
    def MeasureOverride(self: Windows.UI.Xaml.IFrameworkElementOverrides, availableSize: Windows.Foundation.Size) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def ArrangeOverride(self: Windows.UI.Xaml.IFrameworkElementOverrides, finalSize: Windows.Foundation.Size) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def OnApplyTemplate(self: Windows.UI.Xaml.IFrameworkElementOverrides) -> Void: ...
    @winrt_mixinmethod
    def GoToElementStateCore(self: Windows.UI.Xaml.IFrameworkElementOverrides2, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
    @winrt_classmethod
    def get_ActualThemeProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics6) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def DeferTree(cls: Windows.UI.Xaml.IFrameworkElementStatics5, element: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_classmethod
    def get_AllowFocusOnInteractionProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualMarginProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualSecondaryThicknessProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualPrimaryThicknessProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualSecondaryBrushProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusVisualPrimaryBrushProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowFocusWhenDisabledProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RequestedThemeProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TagProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LanguageProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ActualWidthProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ActualHeightProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_WidthProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HeightProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinWidthProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxWidthProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinHeightProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxHeightProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalAlignmentProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalAlignmentProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MarginProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_NameProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DataContextProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StyleProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FlowDirectionProperty(cls: Windows.UI.Xaml.IFrameworkElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Triggers = property(get_Triggers, None)
    Resources = property(get_Resources, put_Resources)
    Tag = property(get_Tag, put_Tag)
    Language = property(get_Language, put_Language)
    ActualWidth = property(get_ActualWidth, None)
    ActualHeight = property(get_ActualHeight, None)
    Width = property(get_Width, put_Width)
    Height = property(get_Height, put_Height)
    MinWidth = property(get_MinWidth, put_MinWidth)
    MaxWidth = property(get_MaxWidth, put_MaxWidth)
    MinHeight = property(get_MinHeight, put_MinHeight)
    MaxHeight = property(get_MaxHeight, put_MaxHeight)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    Margin = property(get_Margin, put_Margin)
    Name = property(get_Name, put_Name)
    BaseUri = property(get_BaseUri, None)
    DataContext = property(get_DataContext, put_DataContext)
    Style = property(get_Style, put_Style)
    Parent = property(get_Parent, None)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
    AllowFocusOnInteraction = property(get_AllowFocusOnInteraction, put_AllowFocusOnInteraction)
    FocusVisualMargin = property(get_FocusVisualMargin, put_FocusVisualMargin)
    FocusVisualSecondaryThickness = property(get_FocusVisualSecondaryThickness, put_FocusVisualSecondaryThickness)
    FocusVisualPrimaryThickness = property(get_FocusVisualPrimaryThickness, put_FocusVisualPrimaryThickness)
    FocusVisualSecondaryBrush = property(get_FocusVisualSecondaryBrush, put_FocusVisualSecondaryBrush)
    FocusVisualPrimaryBrush = property(get_FocusVisualPrimaryBrush, put_FocusVisualPrimaryBrush)
    AllowFocusWhenDisabled = property(get_AllowFocusWhenDisabled, put_AllowFocusWhenDisabled)
    ActualTheme = property(get_ActualTheme, None)
    IsLoaded = property(get_IsLoaded, None)
    _FrameworkElement_Meta_.ActualThemeProperty = property(get_ActualThemeProperty.__wrapped__, None)
    _FrameworkElement_Meta_.AllowFocusOnInteractionProperty = property(get_AllowFocusOnInteractionProperty.__wrapped__, None)
    _FrameworkElement_Meta_.FocusVisualMarginProperty = property(get_FocusVisualMarginProperty.__wrapped__, None)
    _FrameworkElement_Meta_.FocusVisualSecondaryThicknessProperty = property(get_FocusVisualSecondaryThicknessProperty.__wrapped__, None)
    _FrameworkElement_Meta_.FocusVisualPrimaryThicknessProperty = property(get_FocusVisualPrimaryThicknessProperty.__wrapped__, None)
    _FrameworkElement_Meta_.FocusVisualSecondaryBrushProperty = property(get_FocusVisualSecondaryBrushProperty.__wrapped__, None)
    _FrameworkElement_Meta_.FocusVisualPrimaryBrushProperty = property(get_FocusVisualPrimaryBrushProperty.__wrapped__, None)
    _FrameworkElement_Meta_.AllowFocusWhenDisabledProperty = property(get_AllowFocusWhenDisabledProperty.__wrapped__, None)
    _FrameworkElement_Meta_.RequestedThemeProperty = property(get_RequestedThemeProperty.__wrapped__, None)
    _FrameworkElement_Meta_.TagProperty = property(get_TagProperty.__wrapped__, None)
    _FrameworkElement_Meta_.LanguageProperty = property(get_LanguageProperty.__wrapped__, None)
    _FrameworkElement_Meta_.ActualWidthProperty = property(get_ActualWidthProperty.__wrapped__, None)
    _FrameworkElement_Meta_.ActualHeightProperty = property(get_ActualHeightProperty.__wrapped__, None)
    _FrameworkElement_Meta_.WidthProperty = property(get_WidthProperty.__wrapped__, None)
    _FrameworkElement_Meta_.HeightProperty = property(get_HeightProperty.__wrapped__, None)
    _FrameworkElement_Meta_.MinWidthProperty = property(get_MinWidthProperty.__wrapped__, None)
    _FrameworkElement_Meta_.MaxWidthProperty = property(get_MaxWidthProperty.__wrapped__, None)
    _FrameworkElement_Meta_.MinHeightProperty = property(get_MinHeightProperty.__wrapped__, None)
    _FrameworkElement_Meta_.MaxHeightProperty = property(get_MaxHeightProperty.__wrapped__, None)
    _FrameworkElement_Meta_.HorizontalAlignmentProperty = property(get_HorizontalAlignmentProperty.__wrapped__, None)
    _FrameworkElement_Meta_.VerticalAlignmentProperty = property(get_VerticalAlignmentProperty.__wrapped__, None)
    _FrameworkElement_Meta_.MarginProperty = property(get_MarginProperty.__wrapped__, None)
    _FrameworkElement_Meta_.NameProperty = property(get_NameProperty.__wrapped__, None)
    _FrameworkElement_Meta_.DataContextProperty = property(get_DataContextProperty.__wrapped__, None)
    _FrameworkElement_Meta_.StyleProperty = property(get_StyleProperty.__wrapped__, None)
    _FrameworkElement_Meta_.FlowDirectionProperty = property(get_FlowDirectionProperty.__wrapped__, None)
class FrameworkTemplate(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IFrameworkTemplate
    _classid_ = 'Windows.UI.Xaml.FrameworkTemplate'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IFrameworkTemplateFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.FrameworkTemplate: ...
class FrameworkView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IFrameworkView
    _classid_ = 'Windows.UI.Xaml.FrameworkView'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.FrameworkView: ...
    @winrt_mixinmethod
    def Initialize(self: Windows.ApplicationModel.Core.IFrameworkView, applicationView: Windows.ApplicationModel.Core.CoreApplicationView) -> Void: ...
    @winrt_mixinmethod
    def SetWindow(self: Windows.ApplicationModel.Core.IFrameworkView, window: Windows.UI.Core.CoreWindow) -> Void: ...
    @winrt_mixinmethod
    def Load(self: Windows.ApplicationModel.Core.IFrameworkView, entryPoint: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Run(self: Windows.ApplicationModel.Core.IFrameworkView) -> Void: ...
    @winrt_mixinmethod
    def Uninitialize(self: Windows.ApplicationModel.Core.IFrameworkView) -> Void: ...
class FrameworkViewSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IFrameworkViewSource
    _classid_ = 'Windows.UI.Xaml.FrameworkViewSource'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.FrameworkViewSource: ...
    @winrt_mixinmethod
    def CreateView(self: Windows.ApplicationModel.Core.IFrameworkViewSource) -> Windows.ApplicationModel.Core.IFrameworkView: ...
class GridLength(EasyCastStructure):
    Value: Double
    GridUnitType: Windows.UI.Xaml.GridUnitType
class _GridLengthHelper_Meta_(ComPtr.__class__):
    pass
class GridLengthHelper(ComPtr, metaclass=_GridLengthHelper_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IGridLengthHelper
    _classid_ = 'Windows.UI.Xaml.GridLengthHelper'
    @winrt_classmethod
    def get_Auto(cls: Windows.UI.Xaml.IGridLengthHelperStatics) -> Windows.UI.Xaml.GridLength: ...
    @winrt_classmethod
    def FromPixels(cls: Windows.UI.Xaml.IGridLengthHelperStatics, pixels: Double) -> Windows.UI.Xaml.GridLength: ...
    @winrt_classmethod
    def FromValueAndType(cls: Windows.UI.Xaml.IGridLengthHelperStatics, value: Double, type: Windows.UI.Xaml.GridUnitType) -> Windows.UI.Xaml.GridLength: ...
    @winrt_classmethod
    def GetIsAbsolute(cls: Windows.UI.Xaml.IGridLengthHelperStatics, target: Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_classmethod
    def GetIsAuto(cls: Windows.UI.Xaml.IGridLengthHelperStatics, target: Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_classmethod
    def GetIsStar(cls: Windows.UI.Xaml.IGridLengthHelperStatics, target: Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: Windows.UI.Xaml.IGridLengthHelperStatics, target: Windows.UI.Xaml.GridLength, value: Windows.UI.Xaml.GridLength) -> Boolean: ...
    _GridLengthHelper_Meta_.Auto = property(get_Auto.__wrapped__, None)
GridUnitType = Int32
GridUnitType_Auto: GridUnitType = 0
GridUnitType_Pixel: GridUnitType = 1
GridUnitType_Star: GridUnitType = 2
HorizontalAlignment = Int32
HorizontalAlignment_Left: HorizontalAlignment = 0
HorizontalAlignment_Center: HorizontalAlignment = 1
HorizontalAlignment_Right: HorizontalAlignment = 2
HorizontalAlignment_Stretch: HorizontalAlignment = 3
class IAdaptiveTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    MinWindowWidth = property(get_MinWindowWidth, put_MinWindowWidth)
    MinWindowHeight = property(get_MinWindowHeight, put_MinWindowHeight)
class IAdaptiveTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IAdaptiveTriggerFactory'
    _iid_ = Guid('{c966d482-5aeb-4841-9247-c1a0bdd6f59f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.AdaptiveTrigger: ...
class IAdaptiveTriggerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IAdaptiveTriggerStatics'
    _iid_ = Guid('{b92e29ea-1615-4350-9c3b-92b2986bf444}')
    @winrt_commethod(6)
    def get_MinWindowWidthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MinWindowHeightProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    MinWindowWidthProperty = property(get_MinWindowWidthProperty, None)
    MinWindowHeightProperty = property(get_MinWindowHeightProperty, None)
class IApplication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplication'
    _iid_ = Guid('{74b861a1-7487-46a9-9a6e-c78b512726c5}')
    @winrt_commethod(6)
    def get_Resources(self) -> Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_commethod(7)
    def put_Resources(self, value: Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_commethod(8)
    def get_DebugSettings(self) -> Windows.UI.Xaml.DebugSettings: ...
    @winrt_commethod(9)
    def get_RequestedTheme(self) -> Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_commethod(10)
    def put_RequestedTheme(self, value: Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_commethod(11)
    def add_UnhandledException(self, handler: Windows.UI.Xaml.UnhandledExceptionEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_UnhandledException(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Suspending(self, handler: Windows.UI.Xaml.SuspendingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Suspending(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_Resuming(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Resuming(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def Exit(self) -> Void: ...
    Resources = property(get_Resources, put_Resources)
    DebugSettings = property(get_DebugSettings, None)
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
class IApplication2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplication2'
    _iid_ = Guid('{019104be-522a-5904-f52f-de72010429e0}')
    @winrt_commethod(6)
    def get_FocusVisualKind(self) -> Windows.UI.Xaml.FocusVisualKind: ...
    @winrt_commethod(7)
    def put_FocusVisualKind(self, value: Windows.UI.Xaml.FocusVisualKind) -> Void: ...
    @winrt_commethod(8)
    def get_RequiresPointerMode(self) -> Windows.UI.Xaml.ApplicationRequiresPointerMode: ...
    @winrt_commethod(9)
    def put_RequiresPointerMode(self, value: Windows.UI.Xaml.ApplicationRequiresPointerMode) -> Void: ...
    @winrt_commethod(10)
    def add_LeavingBackground(self, handler: Windows.UI.Xaml.LeavingBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LeavingBackground(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnteredBackground(self, handler: Windows.UI.Xaml.EnteredBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnteredBackground(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    FocusVisualKind = property(get_FocusVisualKind, put_FocusVisualKind)
    RequiresPointerMode = property(get_RequiresPointerMode, put_RequiresPointerMode)
class IApplication3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplication3'
    _iid_ = Guid('{b775ad7c-18b8-45ca-a1b0-dc483e4b1028}')
    @winrt_commethod(6)
    def get_HighContrastAdjustment(self) -> Windows.UI.Xaml.ApplicationHighContrastAdjustment: ...
    @winrt_commethod(7)
    def put_HighContrastAdjustment(self, value: Windows.UI.Xaml.ApplicationHighContrastAdjustment) -> Void: ...
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
class IApplicationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationFactory'
    _iid_ = Guid('{93bbe361-be5a-4ee3-b4a3-95118dc97a89}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Application: ...
class IApplicationInitializationCallbackParams(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationInitializationCallbackParams'
    _iid_ = Guid('{751b792e-5772-4488-8b87-f547faa64474}')
class IApplicationOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationOverrides'
    _iid_ = Guid('{25f99ff7-9347-459a-9fac-b2d0e11c1a0f}')
    @winrt_commethod(6)
    def OnActivated(self, args: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Void: ...
    @winrt_commethod(7)
    def OnLaunched(self, args: Windows.ApplicationModel.Activation.LaunchActivatedEventArgs) -> Void: ...
    @winrt_commethod(8)
    def OnFileActivated(self, args: Windows.ApplicationModel.Activation.FileActivatedEventArgs) -> Void: ...
    @winrt_commethod(9)
    def OnSearchActivated(self, args: Windows.ApplicationModel.Activation.SearchActivatedEventArgs) -> Void: ...
    @winrt_commethod(10)
    def OnShareTargetActivated(self, args: Windows.ApplicationModel.Activation.ShareTargetActivatedEventArgs) -> Void: ...
    @winrt_commethod(11)
    def OnFileOpenPickerActivated(self, args: Windows.ApplicationModel.Activation.FileOpenPickerActivatedEventArgs) -> Void: ...
    @winrt_commethod(12)
    def OnFileSavePickerActivated(self, args: Windows.ApplicationModel.Activation.FileSavePickerActivatedEventArgs) -> Void: ...
    @winrt_commethod(13)
    def OnCachedFileUpdaterActivated(self, args: Windows.ApplicationModel.Activation.CachedFileUpdaterActivatedEventArgs) -> Void: ...
    @winrt_commethod(14)
    def OnWindowCreated(self, args: Windows.UI.Xaml.WindowCreatedEventArgs) -> Void: ...
class IApplicationOverrides2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationOverrides2'
    _iid_ = Guid('{db5cd2b9-d3b4-558c-c64e-0434fd1bd889}')
    @winrt_commethod(6)
    def OnBackgroundActivated(self, args: Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs) -> Void: ...
class IApplicationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IApplicationStatics'
    _iid_ = Guid('{06499997-f7b4-45fe-b763-7577d1d3cb4a}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.UI.Xaml.Application: ...
    @winrt_commethod(7)
    def Start(self, callback: Windows.UI.Xaml.ApplicationInitializationCallback) -> Void: ...
    @winrt_commethod(8)
    def LoadComponent(self, component: Windows.Win32.System.WinRT.IInspectable_head, resourceLocator: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(9)
    def LoadComponentWithResourceLocation(self, component: Windows.Win32.System.WinRT.IInspectable_head, resourceLocator: Windows.Foundation.Uri, componentResourceLocation: Windows.UI.Xaml.Controls.Primitives.ComponentResourceLocation) -> Void: ...
    Current = property(get_Current, None)
class IBindingFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBindingFailedEventArgs'
    _iid_ = Guid('{32c1d013-4dbd-446d-bbb8-0de35048a449}')
    @winrt_commethod(6)
    def get_Message(self) -> WinRT_String: ...
    Message = property(get_Message, None)
class IBringIntoViewOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBringIntoViewOptions'
    _iid_ = Guid('{19bdd1b5-c7cb-46d9-a4dd-a1bbe83ef2fb}')
    @winrt_commethod(6)
    def get_AnimationDesired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AnimationDesired(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TargetRect(self) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_TargetRect(self, value: Windows.Foundation.IReference[Windows.Foundation.Rect]) -> Void: ...
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    TargetRect = property(get_TargetRect, put_TargetRect)
class IBringIntoViewOptions2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
class IBringIntoViewRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBringIntoViewRequestedEventArgs'
    _iid_ = Guid('{0e629ec4-2206-4c8b-94ae-bdb66a4ebfd1}')
    @winrt_commethod(6)
    def get_TargetElement(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_TargetElement(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_AnimationDesired(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AnimationDesired(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_TargetRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_TargetRect(self, value: Windows.Foundation.Rect) -> Void: ...
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
    TargetElement = property(get_TargetElement, put_TargetElement)
    AnimationDesired = property(get_AnimationDesired, put_AnimationDesired)
    TargetRect = property(get_TargetRect, put_TargetRect)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, None)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, None)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    Handled = property(get_Handled, put_Handled)
class IBrushTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBrushTransition'
    _iid_ = Guid('{1116972c-9dad-5429-a7dd-b2b7d061ab8e}')
    @winrt_commethod(6)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class IBrushTransitionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IBrushTransitionFactory'
    _iid_ = Guid('{3dbe7368-13d4-510c-a215-7539f4787b52}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.BrushTransition: ...
class IColorPaletteResources(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IColorPaletteResources'
    _iid_ = Guid('{258088c4-aef2-5d3f-833b-c36db6278ed9}')
    @winrt_commethod(6)
    def get_AltHigh(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(7)
    def put_AltHigh(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(8)
    def get_AltLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(9)
    def put_AltLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(10)
    def get_AltMedium(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(11)
    def put_AltMedium(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(12)
    def get_AltMediumHigh(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(13)
    def put_AltMediumHigh(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(14)
    def get_AltMediumLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(15)
    def put_AltMediumLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(16)
    def get_BaseHigh(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(17)
    def put_BaseHigh(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(18)
    def get_BaseLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(19)
    def put_BaseLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(20)
    def get_BaseMedium(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(21)
    def put_BaseMedium(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(22)
    def get_BaseMediumHigh(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(23)
    def put_BaseMediumHigh(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(24)
    def get_BaseMediumLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(25)
    def put_BaseMediumLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(26)
    def get_ChromeAltLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(27)
    def put_ChromeAltLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(28)
    def get_ChromeBlackHigh(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(29)
    def put_ChromeBlackHigh(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(30)
    def get_ChromeBlackLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(31)
    def put_ChromeBlackLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(32)
    def get_ChromeBlackMediumLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(33)
    def put_ChromeBlackMediumLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(34)
    def get_ChromeBlackMedium(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(35)
    def put_ChromeBlackMedium(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(36)
    def get_ChromeDisabledHigh(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(37)
    def put_ChromeDisabledHigh(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(38)
    def get_ChromeDisabledLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(39)
    def put_ChromeDisabledLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(40)
    def get_ChromeHigh(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(41)
    def put_ChromeHigh(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(42)
    def get_ChromeLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(43)
    def put_ChromeLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(44)
    def get_ChromeMedium(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(45)
    def put_ChromeMedium(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(46)
    def get_ChromeMediumLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(47)
    def put_ChromeMediumLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(48)
    def get_ChromeWhite(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(49)
    def put_ChromeWhite(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(50)
    def get_ChromeGray(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(51)
    def put_ChromeGray(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(52)
    def get_ListLow(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(53)
    def put_ListLow(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(54)
    def get_ListMedium(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(55)
    def put_ListMedium(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(56)
    def get_ErrorText(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(57)
    def put_ErrorText(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    @winrt_commethod(58)
    def get_Accent(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(59)
    def put_Accent(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
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
    ChromeBlackMediumLow = property(get_ChromeBlackMediumLow, put_ChromeBlackMediumLow)
    ChromeBlackMedium = property(get_ChromeBlackMedium, put_ChromeBlackMedium)
    ChromeDisabledHigh = property(get_ChromeDisabledHigh, put_ChromeDisabledHigh)
    ChromeDisabledLow = property(get_ChromeDisabledLow, put_ChromeDisabledLow)
    ChromeHigh = property(get_ChromeHigh, put_ChromeHigh)
    ChromeLow = property(get_ChromeLow, put_ChromeLow)
    ChromeMedium = property(get_ChromeMedium, put_ChromeMedium)
    ChromeMediumLow = property(get_ChromeMediumLow, put_ChromeMediumLow)
    ChromeWhite = property(get_ChromeWhite, put_ChromeWhite)
    ChromeGray = property(get_ChromeGray, put_ChromeGray)
    ListLow = property(get_ListLow, put_ListLow)
    ListMedium = property(get_ListMedium, put_ListMedium)
    ErrorText = property(get_ErrorText, put_ErrorText)
    Accent = property(get_Accent, put_Accent)
class IColorPaletteResourcesFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IColorPaletteResourcesFactory'
    _iid_ = Guid('{a57f0783-1876-5cc0-8ea5-bc77b17e0f7e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ColorPaletteResources: ...
class ICornerRadiusHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ICornerRadiusHelper'
    _iid_ = Guid('{fd7be182-1cdb-4288-b8c8-85ee79297bfc}')
class ICornerRadiusHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ICornerRadiusHelperStatics'
    _iid_ = Guid('{f4a1f659-d4d4-451f-a387-d6bf4b2451d4}')
    @winrt_commethod(6)
    def FromRadii(self, topLeft: Double, topRight: Double, bottomRight: Double, bottomLeft: Double) -> Windows.UI.Xaml.CornerRadius: ...
    @winrt_commethod(7)
    def FromUniformRadius(self, uniformRadius: Double) -> Windows.UI.Xaml.CornerRadius: ...
class IDataContextChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataContextChangedEventArgs'
    _iid_ = Guid('{7da68e21-0b8f-4f9f-a143-f8e7780136a2}')
    @winrt_commethod(6)
    def get_NewValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    NewValue = property(get_NewValue, None)
    Handled = property(get_Handled, put_Handled)
class IDataTemplate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplate'
    _iid_ = Guid('{9910aec7-8ab5-4118-9bc6-09f45a35073d}')
    @winrt_commethod(6)
    def LoadContent(self) -> Windows.UI.Xaml.DependencyObject: ...
class IDataTemplateExtension(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateExtension'
    _iid_ = Guid('{595e9547-cdff-4b92-b773-ab396878f353}')
    @winrt_commethod(6)
    def ResetTemplate(self) -> Void: ...
    @winrt_commethod(7)
    def ProcessBinding(self, phase: UInt32) -> Boolean: ...
    @winrt_commethod(8)
    def ProcessBindings(self, arg: Windows.UI.Xaml.Controls.ContainerContentChangingEventArgs) -> Int32: ...
class IDataTemplateFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateFactory'
    _iid_ = Guid('{51ed9d7e-2b53-475b-9c88-0c1832c8351a}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DataTemplate: ...
class IDataTemplateKey(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateKey'
    _iid_ = Guid('{873b6c28-cceb-4b61-86fa-b2cec39cc2fa}')
    @winrt_commethod(6)
    def get_DataType(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def put_DataType(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    DataType = property(get_DataType, put_DataType)
class IDataTemplateKeyFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateKeyFactory'
    _iid_ = Guid('{e96b2959-d982-4152-91cb-de0e4dfd7693}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DataTemplateKey: ...
    @winrt_commethod(7)
    def CreateInstanceWithType(self, dataType: Windows.Win32.System.WinRT.IInspectable_head, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DataTemplateKey: ...
class IDataTemplateStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDataTemplateStatics2'
    _iid_ = Guid('{8af77d73-aa01-471e-bedd-8bad86219b77}')
    @winrt_commethod(6)
    def get_ExtensionInstanceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetExtensionInstance(self, element: Windows.UI.Xaml.FrameworkElement) -> Windows.UI.Xaml.IDataTemplateExtension: ...
    @winrt_commethod(8)
    def SetExtensionInstance(self, element: Windows.UI.Xaml.FrameworkElement, value: Windows.UI.Xaml.IDataTemplateExtension) -> Void: ...
    ExtensionInstanceProperty = property(get_ExtensionInstanceProperty, None)
class IDebugSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def add_BindingFailed(self, handler: Windows.UI.Xaml.BindingFailedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_BindingFailed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    EnableFrameRateCounter = property(get_EnableFrameRateCounter, put_EnableFrameRateCounter)
    IsBindingTracingEnabled = property(get_IsBindingTracingEnabled, put_IsBindingTracingEnabled)
    IsOverdrawHeatMapEnabled = property(get_IsOverdrawHeatMapEnabled, put_IsOverdrawHeatMapEnabled)
class IDebugSettings2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDebugSettings2'
    _iid_ = Guid('{48d37585-e1a6-469b-83c8-30825037119e}')
    @winrt_commethod(6)
    def get_EnableRedrawRegions(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_EnableRedrawRegions(self, value: Boolean) -> Void: ...
    EnableRedrawRegions = property(get_EnableRedrawRegions, put_EnableRedrawRegions)
class IDebugSettings3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDebugSettings3'
    _iid_ = Guid('{e6bb5022-0625-479f-8e32-4b583d73b7ac}')
    @winrt_commethod(6)
    def get_IsTextPerformanceVisualizationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsTextPerformanceVisualizationEnabled(self, value: Boolean) -> Void: ...
    IsTextPerformanceVisualizationEnabled = property(get_IsTextPerformanceVisualizationEnabled, put_IsTextPerformanceVisualizationEnabled)
class IDebugSettings4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDebugSettings4'
    _iid_ = Guid('{c9001e45-e824-5a5f-866c-e20cec88a8fc}')
    @winrt_commethod(6)
    def get_FailFastOnErrors(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_FailFastOnErrors(self, value: Boolean) -> Void: ...
    FailFastOnErrors = property(get_FailFastOnErrors, put_FailFastOnErrors)
class IDependencyObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObject'
    _iid_ = Guid('{5c526665-f60e-4912-af59-5fe0680f089d}')
    @winrt_commethod(6)
    def GetValue(self, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def SetValue(self, dp: Windows.UI.Xaml.DependencyProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def ClearValue(self, dp: Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_commethod(9)
    def ReadLocalValue(self, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def GetAnimationBaseValue(self, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def get_Dispatcher(self) -> Windows.UI.Core.CoreDispatcher: ...
    Dispatcher = property(get_Dispatcher, None)
class IDependencyObject2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObject2'
    _iid_ = Guid('{29fed85d-3d22-43a1-add0-17027c08b212}')
    @winrt_commethod(6)
    def RegisterPropertyChangedCallback(self, dp: Windows.UI.Xaml.DependencyProperty, callback: Windows.UI.Xaml.DependencyPropertyChangedCallback) -> Int64: ...
    @winrt_commethod(7)
    def UnregisterPropertyChangedCallback(self, dp: Windows.UI.Xaml.DependencyProperty, token: Int64) -> Void: ...
class IDependencyObjectCollectionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObjectCollectionFactory'
    _iid_ = Guid('{051e79ff-b3a8-49ee-b5af-ac8f68b649e4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DependencyObjectCollection: ...
class IDependencyObjectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyObjectFactory'
    _iid_ = Guid('{9a03af92-7d8a-4937-884f-ecf34fe02acb}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DependencyObject: ...
class IDependencyProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyProperty'
    _iid_ = Guid('{85b13970-9bc4-4e96-acf1-30c8fd3d55c8}')
    @winrt_commethod(6)
    def GetMetadata(self, forType: Windows.UI.Xaml.Interop.TypeName) -> Windows.UI.Xaml.PropertyMetadata: ...
class IDependencyPropertyChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyPropertyChangedEventArgs'
    _iid_ = Guid('{81212c2b-24d0-4957-abc3-224470a93a4e}')
    @winrt_commethod(6)
    def get_Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OldValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def get_NewValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Property = property(get_Property, None)
    OldValue = property(get_OldValue, None)
    NewValue = property(get_NewValue, None)
class IDependencyPropertyStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDependencyPropertyStatics'
    _iid_ = Guid('{49e5f28f-8259-4d5c-aae0-83d56dbb68d9}')
    @winrt_commethod(6)
    def get_UnsetValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def Register(self, name: WinRT_String, propertyType: Windows.UI.Xaml.Interop.TypeName, ownerType: Windows.UI.Xaml.Interop.TypeName, typeMetadata: Windows.UI.Xaml.PropertyMetadata) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def RegisterAttached(self, name: WinRT_String, propertyType: Windows.UI.Xaml.Interop.TypeName, ownerType: Windows.UI.Xaml.Interop.TypeName, defaultMetadata: Windows.UI.Xaml.PropertyMetadata) -> Windows.UI.Xaml.DependencyProperty: ...
    UnsetValue = property(get_UnsetValue, None)
class IDispatcherTimer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDispatcherTimer'
    _iid_ = Guid('{d160ce46-cd22-4f5f-8c97-40e61da3e2dc}')
    @winrt_commethod(6)
    def get_Interval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Interval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def add_Tick(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Tick(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    @winrt_commethod(12)
    def Stop(self) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsEnabled = property(get_IsEnabled, None)
class IDispatcherTimerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDispatcherTimerFactory'
    _iid_ = Guid('{e9961e6e-3626-403a-afe0-040d58165632}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.DispatcherTimer: ...
class IDragEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragEventArgs'
    _iid_ = Guid('{b440c7c3-02b4-4980-9342-25dae1c0f188}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(9)
    def put_Data(self, value: Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_commethod(10)
    def GetPosition(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    Handled = property(get_Handled, put_Handled)
    Data = property(get_Data, put_Data)
class IDragEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragEventArgs2'
    _iid_ = Guid('{26336658-2917-411d-bfc3-2f22471cbbe7}')
    @winrt_commethod(6)
    def get_DataView(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_DragUIOverride(self) -> Windows.UI.Xaml.DragUIOverride: ...
    @winrt_commethod(8)
    def get_Modifiers(self) -> Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers: ...
    @winrt_commethod(9)
    def get_AcceptedOperation(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(10)
    def put_AcceptedOperation(self, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> Windows.UI.Xaml.DragOperationDeferral: ...
    DataView = property(get_DataView, None)
    DragUIOverride = property(get_DragUIOverride, None)
    Modifiers = property(get_Modifiers, None)
    AcceptedOperation = property(get_AcceptedOperation, put_AcceptedOperation)
class IDragEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragEventArgs3'
    _iid_ = Guid('{d04fc3c6-8119-427a-8152-5f9550cc0416}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    AllowedOperations = property(get_AllowedOperations, None)
class IDragOperationDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragOperationDeferral'
    _iid_ = Guid('{ba73ecba-1b73-4086-b3d3-c223beea1633}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDragStartingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragStartingEventArgs'
    _iid_ = Guid('{6800d3fa-90b8-46f9-8e30-5ac25f73f0f9}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(9)
    def get_DragUI(self) -> Windows.UI.Xaml.DragUI: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> Windows.UI.Xaml.DragOperationDeferral: ...
    @winrt_commethod(11)
    def GetPosition(self, relativeTo: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Point: ...
    Cancel = property(get_Cancel, put_Cancel)
    Data = property(get_Data, None)
    DragUI = property(get_DragUI, None)
class IDragStartingEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragStartingEventArgs2'
    _iid_ = Guid('{d855e08e-44b6-4211-bd0b-7fddbb6e8231}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(7)
    def put_AllowedOperations(self, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
class IDragUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDragUI'
    _iid_ = Guid('{2d9bd838-7c60-4842-9170-346fe10a226a}')
    @winrt_commethod(6)
    def SetContentFromBitmapImage(self, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_commethod(7)
    def SetContentFromBitmapImageWithAnchorPoint(self, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def SetContentFromSoftwareBitmap(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(9)
    def SetContentFromSoftwareBitmapWithAnchorPoint(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def SetContentFromDataPackage(self) -> Void: ...
class IDragUIOverride(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def SetContentFromBitmapImage(self, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage) -> Void: ...
    @winrt_commethod(16)
    def SetContentFromBitmapImageWithAnchorPoint(self, bitmapImage: Windows.UI.Xaml.Media.Imaging.BitmapImage, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(17)
    def SetContentFromSoftwareBitmap(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(18)
    def SetContentFromSoftwareBitmapWithAnchorPoint(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    Caption = property(get_Caption, put_Caption)
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class IDropCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDropCompletedEventArgs'
    _iid_ = Guid('{6c4fc188-95bc-4261-9ec5-21cab677b734}')
    @winrt_commethod(6)
    def get_DropResult(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    DropResult = property(get_DropResult, None)
class IDurationHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDurationHelper'
    _iid_ = Guid('{25c1659f-4497-4135-940f-ee96f4d6e934}')
class IDurationHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IDurationHelperStatics'
    _iid_ = Guid('{bc88093e-3547-4ec0-b519-ffa8f9c4838c}')
    @winrt_commethod(6)
    def get_Automatic(self) -> Windows.UI.Xaml.Duration: ...
    @winrt_commethod(7)
    def get_Forever(self) -> Windows.UI.Xaml.Duration: ...
    @winrt_commethod(8)
    def Compare(self, duration1: Windows.UI.Xaml.Duration, duration2: Windows.UI.Xaml.Duration) -> Int32: ...
    @winrt_commethod(9)
    def FromTimeSpan(self, timeSpan: Windows.Foundation.TimeSpan) -> Windows.UI.Xaml.Duration: ...
    @winrt_commethod(10)
    def GetHasTimeSpan(self, target: Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_commethod(11)
    def Add(self, target: Windows.UI.Xaml.Duration, duration: Windows.UI.Xaml.Duration) -> Windows.UI.Xaml.Duration: ...
    @winrt_commethod(12)
    def Equals(self, target: Windows.UI.Xaml.Duration, value: Windows.UI.Xaml.Duration) -> Boolean: ...
    @winrt_commethod(13)
    def Subtract(self, target: Windows.UI.Xaml.Duration, duration: Windows.UI.Xaml.Duration) -> Windows.UI.Xaml.Duration: ...
    Automatic = property(get_Automatic, None)
    Forever = property(get_Forever, None)
class IEffectiveViewportChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IEffectiveViewportChangedEventArgs'
    _iid_ = Guid('{55ee2e81-1c18-59ed-bd3d-c4ca8fa7d190}')
    @winrt_commethod(6)
    def get_EffectiveViewport(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_MaxViewport(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_BringIntoViewDistanceX(self) -> Double: ...
    @winrt_commethod(9)
    def get_BringIntoViewDistanceY(self) -> Double: ...
    EffectiveViewport = property(get_EffectiveViewport, None)
    MaxViewport = property(get_MaxViewport, None)
    BringIntoViewDistanceX = property(get_BringIntoViewDistanceX, None)
    BringIntoViewDistanceY = property(get_BringIntoViewDistanceY, None)
class IElementFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactory'
    _iid_ = Guid('{17d2ad90-1370-55c8-80e1-78b49004a9e1}')
    @winrt_commethod(6)
    def GetElement(self, args: Windows.UI.Xaml.ElementFactoryGetArgs) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def RecycleElement(self, args: Windows.UI.Xaml.ElementFactoryRecycleArgs) -> Void: ...
class IElementFactoryGetArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryGetArgs'
    _iid_ = Guid('{fb508774-41a3-5829-9255-cf452d041df4}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def put_Data(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def get_Parent(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Parent(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    Data = property(get_Data, put_Data)
    Parent = property(get_Parent, put_Parent)
class IElementFactoryGetArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryGetArgsFactory'
    _iid_ = Guid('{c3b6dae7-883b-5fd7-be80-2059d877e783}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ElementFactoryGetArgs: ...
class IElementFactoryRecycleArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryRecycleArgs'
    _iid_ = Guid('{86f16b14-37e8-5dd8-a90c-25d3710318b0}')
    @winrt_commethod(6)
    def get_Element(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_Element(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_Parent(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Parent(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    Element = property(get_Element, put_Element)
    Parent = property(get_Parent, put_Parent)
class IElementFactoryRecycleArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementFactoryRecycleArgsFactory'
    _iid_ = Guid('{8d926509-ea0d-541b-8271-f9e9118f5e7c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ElementFactoryRecycleArgs: ...
class IElementSoundPlayer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementSoundPlayer'
    _iid_ = Guid('{387773a5-f036-460c-9b81-f3d6ea43f6f2}')
class IElementSoundPlayerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementSoundPlayerStatics'
    _iid_ = Guid('{217a9004-981d-41c9-b152-ada911a4b13a}')
    @winrt_commethod(6)
    def get_Volume(self) -> Double: ...
    @winrt_commethod(7)
    def put_Volume(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> Windows.UI.Xaml.ElementSoundPlayerState: ...
    @winrt_commethod(9)
    def put_State(self, value: Windows.UI.Xaml.ElementSoundPlayerState) -> Void: ...
    @winrt_commethod(10)
    def Play(self, sound: Windows.UI.Xaml.ElementSoundKind) -> Void: ...
    Volume = property(get_Volume, put_Volume)
    State = property(get_State, put_State)
class IElementSoundPlayerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IElementSoundPlayerStatics2'
    _iid_ = Guid('{f2505956-ed41-48d7-aae8-f2abcb444929}')
    @winrt_commethod(6)
    def get_SpatialAudioMode(self) -> Windows.UI.Xaml.ElementSpatialAudioMode: ...
    @winrt_commethod(7)
    def put_SpatialAudioMode(self, value: Windows.UI.Xaml.ElementSpatialAudioMode) -> Void: ...
    SpatialAudioMode = property(get_SpatialAudioMode, put_SpatialAudioMode)
class IEventTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IEventTrigger'
    _iid_ = Guid('{def8f855-0b49-4087-b1a9-b8b38488f786}')
    @winrt_commethod(6)
    def get_RoutedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def put_RoutedEvent(self, value: Windows.UI.Xaml.RoutedEvent) -> Void: ...
    @winrt_commethod(8)
    def get_Actions(self) -> Windows.UI.Xaml.TriggerActionCollection: ...
    RoutedEvent = property(get_RoutedEvent, put_RoutedEvent)
    Actions = property(get_Actions, None)
class IExceptionRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IExceptionRoutedEventArgs'
    _iid_ = Guid('{dd9ff16a-4b62-4a6c-a49d-0671ef6136be}')
    @winrt_commethod(6)
    def get_ErrorMessage(self) -> WinRT_String: ...
    ErrorMessage = property(get_ErrorMessage, None)
class IExceptionRoutedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IExceptionRoutedEventArgsFactory'
    _iid_ = Guid('{bba9826d-5d7a-44e7-b893-b2ae0dd24273}')
class IFrameworkElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement'
    _iid_ = Guid('{a391d09b-4a99-4b7c-9d8d-6fa5d01f6fbf}')
    @winrt_commethod(6)
    def get_Triggers(self) -> Windows.UI.Xaml.TriggerCollection: ...
    @winrt_commethod(7)
    def get_Resources(self) -> Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_commethod(8)
    def put_Resources(self, value: Windows.UI.Xaml.ResourceDictionary) -> Void: ...
    @winrt_commethod(9)
    def get_Tag(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def put_Tag(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
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
    def get_HorizontalAlignment(self) -> Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_commethod(28)
    def put_HorizontalAlignment(self, value: Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_commethod(29)
    def get_VerticalAlignment(self) -> Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_commethod(30)
    def put_VerticalAlignment(self, value: Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_commethod(31)
    def get_Margin(self) -> Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(32)
    def put_Margin(self, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(33)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(35)
    def get_BaseUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(36)
    def get_DataContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(37)
    def put_DataContext(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(38)
    def get_Style(self) -> Windows.UI.Xaml.Style: ...
    @winrt_commethod(39)
    def put_Style(self, value: Windows.UI.Xaml.Style) -> Void: ...
    @winrt_commethod(40)
    def get_Parent(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(41)
    def get_FlowDirection(self) -> Windows.UI.Xaml.FlowDirection: ...
    @winrt_commethod(42)
    def put_FlowDirection(self, value: Windows.UI.Xaml.FlowDirection) -> Void: ...
    @winrt_commethod(43)
    def add_Loaded(self, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(44)
    def remove_Loaded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(45)
    def add_Unloaded(self, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(46)
    def remove_Unloaded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(47)
    def add_SizeChanged(self, handler: Windows.UI.Xaml.SizeChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(48)
    def remove_SizeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(49)
    def add_LayoutUpdated(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(50)
    def remove_LayoutUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(51)
    def FindName(self, name: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(52)
    def SetBinding(self, dp: Windows.UI.Xaml.DependencyProperty, binding: Windows.UI.Xaml.Data.BindingBase) -> Void: ...
    Triggers = property(get_Triggers, None)
    Resources = property(get_Resources, put_Resources)
    Tag = property(get_Tag, put_Tag)
    Language = property(get_Language, put_Language)
    ActualWidth = property(get_ActualWidth, None)
    ActualHeight = property(get_ActualHeight, None)
    Width = property(get_Width, put_Width)
    Height = property(get_Height, put_Height)
    MinWidth = property(get_MinWidth, put_MinWidth)
    MaxWidth = property(get_MaxWidth, put_MaxWidth)
    MinHeight = property(get_MinHeight, put_MinHeight)
    MaxHeight = property(get_MaxHeight, put_MaxHeight)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    Margin = property(get_Margin, put_Margin)
    Name = property(get_Name, put_Name)
    BaseUri = property(get_BaseUri, None)
    DataContext = property(get_DataContext, put_DataContext)
    Style = property(get_Style, put_Style)
    Parent = property(get_Parent, None)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
class IFrameworkElement2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement2'
    _iid_ = Guid('{f19104be-422a-4904-a52f-ee72010429e5}')
    @winrt_commethod(6)
    def get_RequestedTheme(self) -> Windows.UI.Xaml.ElementTheme: ...
    @winrt_commethod(7)
    def put_RequestedTheme(self, value: Windows.UI.Xaml.ElementTheme) -> Void: ...
    @winrt_commethod(8)
    def add_DataContextChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.UI.Xaml.DataContextChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DataContextChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetBindingExpression(self, dp: Windows.UI.Xaml.DependencyProperty) -> Windows.UI.Xaml.Data.BindingExpression: ...
    RequestedTheme = property(get_RequestedTheme, put_RequestedTheme)
class IFrameworkElement3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement3'
    _iid_ = Guid('{c81c2720-5c52-4bbe-a199-2b1e34f00f70}')
    @winrt_commethod(6)
    def add_Loading(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Loading(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IFrameworkElement4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement4'
    _iid_ = Guid('{6b765bb3-fba3-4404-bdee-1a45d1ca5f21}')
    @winrt_commethod(6)
    def get_AllowFocusOnInteraction(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowFocusOnInteraction(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_FocusVisualMargin(self) -> Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(9)
    def put_FocusVisualMargin(self, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(10)
    def get_FocusVisualSecondaryThickness(self) -> Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(11)
    def put_FocusVisualSecondaryThickness(self, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(12)
    def get_FocusVisualPrimaryThickness(self) -> Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(13)
    def put_FocusVisualPrimaryThickness(self, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(14)
    def get_FocusVisualSecondaryBrush(self) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(15)
    def put_FocusVisualSecondaryBrush(self, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(16)
    def get_FocusVisualPrimaryBrush(self) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_FocusVisualPrimaryBrush(self, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(18)
    def get_AllowFocusWhenDisabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_AllowFocusWhenDisabled(self, value: Boolean) -> Void: ...
    AllowFocusOnInteraction = property(get_AllowFocusOnInteraction, put_AllowFocusOnInteraction)
    FocusVisualMargin = property(get_FocusVisualMargin, put_FocusVisualMargin)
    FocusVisualSecondaryThickness = property(get_FocusVisualSecondaryThickness, put_FocusVisualSecondaryThickness)
    FocusVisualPrimaryThickness = property(get_FocusVisualPrimaryThickness, put_FocusVisualPrimaryThickness)
    FocusVisualSecondaryBrush = property(get_FocusVisualSecondaryBrush, put_FocusVisualSecondaryBrush)
    FocusVisualPrimaryBrush = property(get_FocusVisualPrimaryBrush, put_FocusVisualPrimaryBrush)
    AllowFocusWhenDisabled = property(get_AllowFocusWhenDisabled, put_AllowFocusWhenDisabled)
class IFrameworkElement6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement6'
    _iid_ = Guid('{792a5d91-62a1-40bf-a0ce-f9c131fcb7a7}')
    @winrt_commethod(6)
    def get_ActualTheme(self) -> Windows.UI.Xaml.ElementTheme: ...
    @winrt_commethod(7)
    def add_ActualThemeChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ActualThemeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ActualTheme = property(get_ActualTheme, None)
class IFrameworkElement7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElement7'
    _iid_ = Guid('{2263886c-c069-570f-b9cc-9e21dd028d8e}')
    @winrt_commethod(6)
    def get_IsLoaded(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_EffectiveViewportChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.FrameworkElement, Windows.UI.Xaml.EffectiveViewportChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_EffectiveViewportChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsLoaded = property(get_IsLoaded, None)
class IFrameworkElementFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementFactory'
    _iid_ = Guid('{deaee126-03ca-4966-b576-604cce93b5e8}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.FrameworkElement: ...
class IFrameworkElementOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementOverrides'
    _iid_ = Guid('{da007e54-b3c2-4b9a-aa8e-d3f071262b97}')
    @winrt_commethod(6)
    def MeasureOverride(self, availableSize: Windows.Foundation.Size) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def ArrangeOverride(self, finalSize: Windows.Foundation.Size) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def OnApplyTemplate(self) -> Void: ...
class IFrameworkElementOverrides2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementOverrides2'
    _iid_ = Guid('{cb5cd2b9-e3b4-458c-b64e-1434fd1bd88a}')
    @winrt_commethod(6)
    def GoToElementStateCore(self, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
class IFrameworkElementProtected7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementProtected7'
    _iid_ = Guid('{65aa0480-22e3-5103-ad2a-b626f88ca5ae}')
    @winrt_commethod(6)
    def InvalidateViewport(self) -> Void: ...
class IFrameworkElementStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics'
    _iid_ = Guid('{48383032-fbeb-4f8a-aed2-ee21fb27a57b}')
    @winrt_commethod(6)
    def get_TagProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LanguageProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ActualWidthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ActualHeightProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_WidthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_HeightProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_MinWidthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_MaxWidthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_MinHeightProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_MaxHeightProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_HorizontalAlignmentProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_VerticalAlignmentProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_MarginProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_NameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_DataContextProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_StyleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_FlowDirectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TagProperty = property(get_TagProperty, None)
    LanguageProperty = property(get_LanguageProperty, None)
    ActualWidthProperty = property(get_ActualWidthProperty, None)
    ActualHeightProperty = property(get_ActualHeightProperty, None)
    WidthProperty = property(get_WidthProperty, None)
    HeightProperty = property(get_HeightProperty, None)
    MinWidthProperty = property(get_MinWidthProperty, None)
    MaxWidthProperty = property(get_MaxWidthProperty, None)
    MinHeightProperty = property(get_MinHeightProperty, None)
    MaxHeightProperty = property(get_MaxHeightProperty, None)
    HorizontalAlignmentProperty = property(get_HorizontalAlignmentProperty, None)
    VerticalAlignmentProperty = property(get_VerticalAlignmentProperty, None)
    MarginProperty = property(get_MarginProperty, None)
    NameProperty = property(get_NameProperty, None)
    DataContextProperty = property(get_DataContextProperty, None)
    StyleProperty = property(get_StyleProperty, None)
    FlowDirectionProperty = property(get_FlowDirectionProperty, None)
class IFrameworkElementStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics2'
    _iid_ = Guid('{9695db02-c0d8-4fa2-b100-3fa2df8b9538}')
    @winrt_commethod(6)
    def get_RequestedThemeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    RequestedThemeProperty = property(get_RequestedThemeProperty, None)
class IFrameworkElementStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics4'
    _iid_ = Guid('{9c41b155-c5d8-4663-bff2-d8d54fb5dbb3}')
    @winrt_commethod(6)
    def get_AllowFocusOnInteractionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FocusVisualMarginProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FocusVisualSecondaryThicknessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_FocusVisualPrimaryThicknessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_FocusVisualSecondaryBrushProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_FocusVisualPrimaryBrushProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_AllowFocusWhenDisabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    AllowFocusOnInteractionProperty = property(get_AllowFocusOnInteractionProperty, None)
    FocusVisualMarginProperty = property(get_FocusVisualMarginProperty, None)
    FocusVisualSecondaryThicknessProperty = property(get_FocusVisualSecondaryThicknessProperty, None)
    FocusVisualPrimaryThicknessProperty = property(get_FocusVisualPrimaryThicknessProperty, None)
    FocusVisualSecondaryBrushProperty = property(get_FocusVisualSecondaryBrushProperty, None)
    FocusVisualPrimaryBrushProperty = property(get_FocusVisualPrimaryBrushProperty, None)
    AllowFocusWhenDisabledProperty = property(get_AllowFocusWhenDisabledProperty, None)
class IFrameworkElementStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics5'
    _iid_ = Guid('{525d3941-0b3c-4be6-9978-19a8025c09d8}')
    @winrt_commethod(6)
    def DeferTree(self, element: Windows.UI.Xaml.DependencyObject) -> Void: ...
class IFrameworkElementStatics6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkElementStatics6'
    _iid_ = Guid('{fcc1529a-69db-4582-a7be-cf6a1cfdacd0}')
    @winrt_commethod(6)
    def get_ActualThemeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ActualThemeProperty = property(get_ActualThemeProperty, None)
class IFrameworkTemplate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkTemplate'
    _iid_ = Guid('{a1e254d8-a446-4a27-9a9d-a0f59e1258a5}')
class IFrameworkTemplateFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkTemplateFactory'
    _iid_ = Guid('{1a78a0a5-937d-46d4-832b-94ff14dab061}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.FrameworkTemplate: ...
class IFrameworkView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkView'
    _iid_ = Guid('{ddba664b-b603-47aa-942d-3833174f0d80}')
class IFrameworkViewSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IFrameworkViewSource'
    _iid_ = Guid('{e3b077da-35ad-4b09-b5b2-27420041ba9f}')
class IGridLengthHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IGridLengthHelper'
    _iid_ = Guid('{7a826ce1-07a0-4083-b6d1-b1d917b976ac}')
class IGridLengthHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IGridLengthHelperStatics'
    _iid_ = Guid('{9d457b9b-019f-4266-8872-215f198f6a9d}')
    @winrt_commethod(6)
    def get_Auto(self) -> Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(7)
    def FromPixels(self, pixels: Double) -> Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(8)
    def FromValueAndType(self, value: Double, type: Windows.UI.Xaml.GridUnitType) -> Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(9)
    def GetIsAbsolute(self, target: Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_commethod(10)
    def GetIsAuto(self, target: Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_commethod(11)
    def GetIsStar(self, target: Windows.UI.Xaml.GridLength) -> Boolean: ...
    @winrt_commethod(12)
    def Equals(self, target: Windows.UI.Xaml.GridLength, value: Windows.UI.Xaml.GridLength) -> Boolean: ...
    Auto = property(get_Auto, None)
class IMediaFailedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IMediaFailedRoutedEventArgs'
    _iid_ = Guid('{46d1fa8d-5149-4153-ba3c-b03e64ee531e}')
    @winrt_commethod(6)
    def get_ErrorTrace(self) -> WinRT_String: ...
    ErrorTrace = property(get_ErrorTrace, None)
class IPointHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPointHelper'
    _iid_ = Guid('{727bdd92-64b0-49cf-a321-a9793e73e2e7}')
class IPointHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPointHelperStatics'
    _iid_ = Guid('{015aca75-76d8-4b7e-8a33-7d79204691ee}')
    @winrt_commethod(6)
    def FromCoordinates(self, x: Single, y: Single) -> Windows.Foundation.Point: ...
class IPropertyMetadata(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyMetadata'
    _iid_ = Guid('{814ef30d-8d18-448a-8644-f2cb51e70380}')
    @winrt_commethod(6)
    def get_DefaultValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_CreateDefaultValueCallback(self) -> Windows.UI.Xaml.CreateDefaultValueCallback: ...
    DefaultValue = property(get_DefaultValue, None)
    CreateDefaultValueCallback = property(get_CreateDefaultValueCallback, None)
class IPropertyMetadataFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyMetadataFactory'
    _iid_ = Guid('{c1b81cc0-57cd-4f2f-b0a9-e1801b28f76b}')
    @winrt_commethod(6)
    def CreateInstanceWithDefaultValue(self, defaultValue: Windows.Win32.System.WinRT.IInspectable_head, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(7)
    def CreateInstanceWithDefaultValueAndCallback(self, defaultValue: Windows.Win32.System.WinRT.IInspectable_head, propertyChangedCallback: Windows.UI.Xaml.PropertyChangedCallback, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.PropertyMetadata: ...
class IPropertyMetadataStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyMetadataStatics'
    _iid_ = Guid('{3b01077a-6e06-45e9-8b5c-af243458c062}')
    @winrt_commethod(6)
    def CreateWithDefaultValue(self, defaultValue: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(7)
    def CreateWithDefaultValueAndCallback(self, defaultValue: Windows.Win32.System.WinRT.IInspectable_head, propertyChangedCallback: Windows.UI.Xaml.PropertyChangedCallback) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(8)
    def CreateWithFactory(self, createDefaultValueCallback: Windows.UI.Xaml.CreateDefaultValueCallback) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_commethod(9)
    def CreateWithFactoryAndCallback(self, createDefaultValueCallback: Windows.UI.Xaml.CreateDefaultValueCallback, propertyChangedCallback: Windows.UI.Xaml.PropertyChangedCallback) -> Windows.UI.Xaml.PropertyMetadata: ...
class IPropertyPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyPath'
    _iid_ = Guid('{300e5d8a-1ff3-4d2c-95ec-27f81debacb8}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class IPropertyPathFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IPropertyPathFactory'
    _iid_ = Guid('{4e4cdf99-9826-4e56-847c-ca055f162905}')
    @winrt_commethod(6)
    def CreateInstance(self, path: WinRT_String) -> Windows.UI.Xaml.PropertyPath: ...
class IRectHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRectHelper'
    _iid_ = Guid('{a38781e2-4bfb-4ee2-afe5-89f31b37478d}')
class IRectHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRectHelperStatics'
    _iid_ = Guid('{5ee163e4-c17e-494f-b580-2f0574fc3a15}')
    @winrt_commethod(6)
    def get_Empty(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def FromCoordinatesAndDimensions(self, x: Single, y: Single, width: Single, height: Single) -> Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def FromPoints(self, point1: Windows.Foundation.Point, point2: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def FromLocationAndSize(self, location: Windows.Foundation.Point, size: Windows.Foundation.Size) -> Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def GetIsEmpty(self, target: Windows.Foundation.Rect) -> Boolean: ...
    @winrt_commethod(11)
    def GetBottom(self, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(12)
    def GetLeft(self, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(13)
    def GetRight(self, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(14)
    def GetTop(self, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_commethod(15)
    def Contains(self, target: Windows.Foundation.Rect, point: Windows.Foundation.Point) -> Boolean: ...
    @winrt_commethod(16)
    def Equals(self, target: Windows.Foundation.Rect, value: Windows.Foundation.Rect) -> Boolean: ...
    @winrt_commethod(17)
    def Intersect(self, target: Windows.Foundation.Rect, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    @winrt_commethod(18)
    def UnionWithPoint(self, target: Windows.Foundation.Rect, point: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_commethod(19)
    def UnionWithRect(self, target: Windows.Foundation.Rect, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    Empty = property(get_Empty, None)
class IResourceDictionary(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IResourceDictionary'
    _iid_ = Guid('{c1ea4f24-d6de-4191-8e3a-f48601f7489c}')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Source(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_MergedDictionaries(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.ResourceDictionary]: ...
    @winrt_commethod(9)
    def get_ThemeDictionaries(self) -> Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Source = property(get_Source, put_Source)
    MergedDictionaries = property(get_MergedDictionaries, None)
    ThemeDictionaries = property(get_ThemeDictionaries, None)
class IResourceDictionaryFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IResourceDictionaryFactory'
    _iid_ = Guid('{ea3639b5-31b7-4271-92c9-7c9584a91c22}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ResourceDictionary: ...
class IRoutedEvent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRoutedEvent'
    _iid_ = Guid('{a6b25818-43c1-4c70-865c-7bdd5a32e327}')
class IRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRoutedEventArgs'
    _iid_ = Guid('{5c985ac6-d802-4b38-a223-bf070c43fedf}')
    @winrt_commethod(6)
    def get_OriginalSource(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    OriginalSource = property(get_OriginalSource, None)
class IRoutedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IRoutedEventArgsFactory'
    _iid_ = Guid('{b61c4d87-70e5-412e-b520-1a41ee76bbf4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.RoutedEventArgs: ...
class IScalarTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IScalarTransition'
    _iid_ = Guid('{4cb68238-e15d-524e-a73c-9d4dcfbea226}')
    @winrt_commethod(6)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class IScalarTransitionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IScalarTransitionFactory'
    _iid_ = Guid('{c9b1e9ee-90da-5ddd-be64-3e47977ea280}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ScalarTransition: ...
class ISetter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetter'
    _iid_ = Guid('{a73ded29-b4ae-4a81-be85-e690ba0d3b6e}')
    @winrt_commethod(6)
    def get_Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def put_Property(self, value: Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def put_Value(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Property = property(get_Property, put_Property)
    Value = property(get_Value, put_Value)
class ISetter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetter2'
    _iid_ = Guid('{70169561-05b1-4fa3-9d53-8e0c8c747afc}')
    @winrt_commethod(6)
    def get_Target(self) -> Windows.UI.Xaml.TargetPropertyPath: ...
    @winrt_commethod(7)
    def put_Target(self, value: Windows.UI.Xaml.TargetPropertyPath) -> Void: ...
    Target = property(get_Target, put_Target)
class ISetterBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterBase'
    _iid_ = Guid('{418be27c-2ac4-4f22-8097-dea3aeeb2fb3}')
    @winrt_commethod(6)
    def get_IsSealed(self) -> Boolean: ...
    IsSealed = property(get_IsSealed, None)
class ISetterBaseCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterBaseCollection'
    _iid_ = Guid('{03c40ca8-909e-4117-811c-a4529496bdf1}')
    @winrt_commethod(6)
    def get_IsSealed(self) -> Boolean: ...
    IsSealed = property(get_IsSealed, None)
class ISetterBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterBaseFactory'
    _iid_ = Guid('{81f8ad60-1ce8-469d-a667-16e37cef8ba9}')
class ISetterFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISetterFactory'
    _iid_ = Guid('{d3ca3d42-09b1-49d5-8891-e7b5648e02a2}')
    @winrt_commethod(6)
    def CreateInstance(self, targetProperty: Windows.UI.Xaml.DependencyProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Setter: ...
class ISizeChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISizeChangedEventArgs'
    _iid_ = Guid('{d5312e60-5cc1-42a1-920c-1af46be2f986}')
    @winrt_commethod(6)
    def get_PreviousSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_NewSize(self) -> Windows.Foundation.Size: ...
    PreviousSize = property(get_PreviousSize, None)
    NewSize = property(get_NewSize, None)
class ISizeHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISizeHelper'
    _iid_ = Guid('{e7225a94-5d03-4a03-ba94-967fc68fcefe}')
class ISizeHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ISizeHelperStatics'
    _iid_ = Guid('{6286c5b2-cf78-4915-aa40-76004a165f5e}')
    @winrt_commethod(6)
    def get_Empty(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def FromDimensions(self, width: Single, height: Single) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def GetIsEmpty(self, target: Windows.Foundation.Size) -> Boolean: ...
    @winrt_commethod(9)
    def Equals(self, target: Windows.Foundation.Size, value: Windows.Foundation.Size) -> Boolean: ...
    Empty = property(get_Empty, None)
class IStateTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTrigger'
    _iid_ = Guid('{67adef2e-d8d9-49f7-a1fd-2e35eedd23cd}')
    @winrt_commethod(6)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsActive(self, value: Boolean) -> Void: ...
    IsActive = property(get_IsActive, put_IsActive)
class IStateTriggerBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerBase'
    _iid_ = Guid('{48b20698-af06-466c-8052-93666dde0e49}')
class IStateTriggerBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerBaseFactory'
    _iid_ = Guid('{970e2c4b-bfaf-47b0-be42-c1d711bb2e9f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.StateTriggerBase: ...
class IStateTriggerBaseProtected(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerBaseProtected'
    _iid_ = Guid('{3c41e253-8d14-4216-994c-f9930429f6e5}')
    @winrt_commethod(6)
    def SetActive(self, IsActive: Boolean) -> Void: ...
class IStateTriggerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStateTriggerStatics'
    _iid_ = Guid('{71e95c90-b3fe-4dd3-a8a8-44a2ce25e0b8}')
    @winrt_commethod(6)
    def get_IsActiveProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    IsActiveProperty = property(get_IsActiveProperty, None)
class IStyle(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStyle'
    _iid_ = Guid('{c4a9f225-9db7-4a7d-b6d1-f74edb9293c2}')
    @winrt_commethod(6)
    def get_IsSealed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Setters(self) -> Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_commethod(8)
    def get_TargetType(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(9)
    def put_TargetType(self, value: Windows.UI.Xaml.Interop.TypeName) -> Void: ...
    @winrt_commethod(10)
    def get_BasedOn(self) -> Windows.UI.Xaml.Style: ...
    @winrt_commethod(11)
    def put_BasedOn(self, value: Windows.UI.Xaml.Style) -> Void: ...
    @winrt_commethod(12)
    def Seal(self) -> Void: ...
    IsSealed = property(get_IsSealed, None)
    Setters = property(get_Setters, None)
    TargetType = property(get_TargetType, put_TargetType)
    BasedOn = property(get_BasedOn, put_BasedOn)
class IStyleFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IStyleFactory'
    _iid_ = Guid('{a36824e3-3d81-4ce5-aa51-8b410f602fcd}')
    @winrt_commethod(6)
    def CreateInstance(self, targetType: Windows.UI.Xaml.Interop.TypeName) -> Windows.UI.Xaml.Style: ...
class ITargetPropertyPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITargetPropertyPath'
    _iid_ = Guid('{40740f8e-085f-4ced-be70-6f47acf15ad0}')
    @winrt_commethod(6)
    def get_Path(self) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_commethod(7)
    def put_Path(self, value: Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_commethod(8)
    def get_Target(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def put_Target(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Path = property(get_Path, put_Path)
    Target = property(get_Target, put_Target)
class ITargetPropertyPathFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITargetPropertyPathFactory'
    _iid_ = Guid('{88eeccc8-99e2-4a44-9907-b44bc86e2bbe}')
    @winrt_commethod(6)
    def CreateInstance(self, targetProperty: Windows.UI.Xaml.DependencyProperty) -> Windows.UI.Xaml.TargetPropertyPath: ...
class IThicknessHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IThicknessHelper'
    _iid_ = Guid('{a86bae4b-1e8f-4eeb-9013-0b2838a97b34}')
class IThicknessHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IThicknessHelperStatics'
    _iid_ = Guid('{c0991a7c-070c-4da6-8784-01ca800eb73a}')
    @winrt_commethod(6)
    def FromLengths(self, left: Double, top: Double, right: Double, bottom: Double) -> Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(7)
    def FromUniformLength(self, uniformLength: Double) -> Windows.UI.Xaml.Thickness: ...
class ITriggerAction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerAction'
    _iid_ = Guid('{a2c0df02-63d5-4b46-9b83-0868d3079621}')
class ITriggerActionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerActionFactory'
    _iid_ = Guid('{68d2c0b9-3289-414f-8f6e-c6b97aedda03}')
class ITriggerBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerBase'
    _iid_ = Guid('{e7ea222f-dee6-4393-a8b2-8923d641f395}')
class ITriggerBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.ITriggerBaseFactory'
    _iid_ = Guid('{6a3b9e57-fc5d-42d0-8cb9-ca50667af746}')
class IUIElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement'
    _iid_ = Guid('{676d0be9-b65c-41c6-ba40-58cf87f201c1}')
    @winrt_commethod(6)
    def get_DesiredSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_AllowDrop(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowDrop(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(10)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def get_Clip(self) -> Windows.UI.Xaml.Media.RectangleGeometry: ...
    @winrt_commethod(12)
    def put_Clip(self, value: Windows.UI.Xaml.Media.RectangleGeometry) -> Void: ...
    @winrt_commethod(13)
    def get_RenderTransform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(14)
    def put_RenderTransform(self, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(15)
    def get_Projection(self) -> Windows.UI.Xaml.Media.Projection: ...
    @winrt_commethod(16)
    def put_Projection(self, value: Windows.UI.Xaml.Media.Projection) -> Void: ...
    @winrt_commethod(17)
    def get_RenderTransformOrigin(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(18)
    def put_RenderTransformOrigin(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(19)
    def get_IsHitTestVisible(self) -> Boolean: ...
    @winrt_commethod(20)
    def put_IsHitTestVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_Visibility(self) -> Windows.UI.Xaml.Visibility: ...
    @winrt_commethod(22)
    def put_Visibility(self, value: Windows.UI.Xaml.Visibility) -> Void: ...
    @winrt_commethod(23)
    def get_RenderSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(24)
    def get_UseLayoutRounding(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_UseLayoutRounding(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def get_Transitions(self) -> Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_commethod(27)
    def put_Transitions(self, value: Windows.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_commethod(28)
    def get_CacheMode(self) -> Windows.UI.Xaml.Media.CacheMode: ...
    @winrt_commethod(29)
    def put_CacheMode(self, value: Windows.UI.Xaml.Media.CacheMode) -> Void: ...
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
    def get_ManipulationMode(self) -> Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_commethod(39)
    def put_ManipulationMode(self, value: Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_commethod(40)
    def get_PointerCaptures(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Input.Pointer]: ...
    @winrt_commethod(41)
    def add_KeyUp(self, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(42)
    def remove_KeyUp(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(43)
    def add_KeyDown(self, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(44)
    def remove_KeyDown(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(45)
    def add_GotFocus(self, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(46)
    def remove_GotFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(47)
    def add_LostFocus(self, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(48)
    def remove_LostFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(49)
    def add_DragEnter(self, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(50)
    def remove_DragEnter(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(51)
    def add_DragLeave(self, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(52)
    def remove_DragLeave(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(53)
    def add_DragOver(self, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(54)
    def remove_DragOver(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(55)
    def add_Drop(self, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(56)
    def remove_Drop(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(57)
    def add_PointerPressed(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(58)
    def remove_PointerPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(59)
    def add_PointerMoved(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(60)
    def remove_PointerMoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(61)
    def add_PointerReleased(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(62)
    def remove_PointerReleased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(63)
    def add_PointerEntered(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(64)
    def remove_PointerEntered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(65)
    def add_PointerExited(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(66)
    def remove_PointerExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(67)
    def add_PointerCaptureLost(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(68)
    def remove_PointerCaptureLost(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(69)
    def add_PointerCanceled(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(70)
    def remove_PointerCanceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(71)
    def add_PointerWheelChanged(self, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(72)
    def remove_PointerWheelChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(73)
    def add_Tapped(self, handler: Windows.UI.Xaml.Input.TappedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(74)
    def remove_Tapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(75)
    def add_DoubleTapped(self, handler: Windows.UI.Xaml.Input.DoubleTappedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(76)
    def remove_DoubleTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(77)
    def add_Holding(self, handler: Windows.UI.Xaml.Input.HoldingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(78)
    def remove_Holding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(79)
    def add_RightTapped(self, handler: Windows.UI.Xaml.Input.RightTappedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(80)
    def remove_RightTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(81)
    def add_ManipulationStarting(self, handler: Windows.UI.Xaml.Input.ManipulationStartingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(82)
    def remove_ManipulationStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(83)
    def add_ManipulationInertiaStarting(self, handler: Windows.UI.Xaml.Input.ManipulationInertiaStartingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(84)
    def remove_ManipulationInertiaStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(85)
    def add_ManipulationStarted(self, handler: Windows.UI.Xaml.Input.ManipulationStartedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(86)
    def remove_ManipulationStarted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(87)
    def add_ManipulationDelta(self, handler: Windows.UI.Xaml.Input.ManipulationDeltaEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(88)
    def remove_ManipulationDelta(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(89)
    def add_ManipulationCompleted(self, handler: Windows.UI.Xaml.Input.ManipulationCompletedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(90)
    def remove_ManipulationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(91)
    def Measure(self, availableSize: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(92)
    def Arrange(self, finalRect: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(93)
    def CapturePointer(self, value: Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    @winrt_commethod(94)
    def ReleasePointerCapture(self, value: Windows.UI.Xaml.Input.Pointer) -> Void: ...
    @winrt_commethod(95)
    def ReleasePointerCaptures(self) -> Void: ...
    @winrt_commethod(96)
    def AddHandler(self, routedEvent: Windows.UI.Xaml.RoutedEvent, handler: Windows.Win32.System.WinRT.IInspectable_head, handledEventsToo: Boolean) -> Void: ...
    @winrt_commethod(97)
    def RemoveHandler(self, routedEvent: Windows.UI.Xaml.RoutedEvent, handler: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(98)
    def TransformToVisual(self, visual: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(99)
    def InvalidateMeasure(self) -> Void: ...
    @winrt_commethod(100)
    def InvalidateArrange(self) -> Void: ...
    @winrt_commethod(101)
    def UpdateLayout(self) -> Void: ...
    DesiredSize = property(get_DesiredSize, None)
    AllowDrop = property(get_AllowDrop, put_AllowDrop)
    Opacity = property(get_Opacity, put_Opacity)
    Clip = property(get_Clip, put_Clip)
    RenderTransform = property(get_RenderTransform, put_RenderTransform)
    Projection = property(get_Projection, put_Projection)
    RenderTransformOrigin = property(get_RenderTransformOrigin, put_RenderTransformOrigin)
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
    Visibility = property(get_Visibility, put_Visibility)
    RenderSize = property(get_RenderSize, None)
    UseLayoutRounding = property(get_UseLayoutRounding, put_UseLayoutRounding)
    Transitions = property(get_Transitions, put_Transitions)
    CacheMode = property(get_CacheMode, put_CacheMode)
    IsTapEnabled = property(get_IsTapEnabled, put_IsTapEnabled)
    IsDoubleTapEnabled = property(get_IsDoubleTapEnabled, put_IsDoubleTapEnabled)
    IsRightTapEnabled = property(get_IsRightTapEnabled, put_IsRightTapEnabled)
    IsHoldingEnabled = property(get_IsHoldingEnabled, put_IsHoldingEnabled)
    ManipulationMode = property(get_ManipulationMode, put_ManipulationMode)
    PointerCaptures = property(get_PointerCaptures, None)
class IUIElement10(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement10'
    _iid_ = Guid('{d531c629-ad2c-5f6b-adcf-fb87287d18d7}')
    @winrt_commethod(6)
    def get_ActualOffset(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_ActualSize(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(8)
    def get_XamlRoot(self) -> Windows.UI.Xaml.XamlRoot: ...
    @winrt_commethod(9)
    def put_XamlRoot(self, value: Windows.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_commethod(10)
    def get_UIContext(self) -> Windows.UI.UIContext: ...
    @winrt_commethod(11)
    def get_Shadow(self) -> Windows.UI.Xaml.Media.Shadow: ...
    @winrt_commethod(12)
    def put_Shadow(self, value: Windows.UI.Xaml.Media.Shadow) -> Void: ...
    ActualOffset = property(get_ActualOffset, None)
    ActualSize = property(get_ActualSize, None)
    XamlRoot = property(get_XamlRoot, put_XamlRoot)
    UIContext = property(get_UIContext, None)
    Shadow = property(get_Shadow, put_Shadow)
class IUIElement2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement2'
    _iid_ = Guid('{676d0bf9-b66c-41d6-ba50-58cf87f201d1}')
    @winrt_commethod(6)
    def get_CompositeMode(self) -> Windows.UI.Xaml.Media.ElementCompositeMode: ...
    @winrt_commethod(7)
    def put_CompositeMode(self, value: Windows.UI.Xaml.Media.ElementCompositeMode) -> Void: ...
    @winrt_commethod(8)
    def CancelDirectManipulations(self) -> Boolean: ...
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
class IUIElement3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement3'
    _iid_ = Guid('{bc2b28f1-26f2-4aab-b256-3b5350881e37}')
    @winrt_commethod(6)
    def get_Transform3D(self) -> Windows.UI.Xaml.Media.Media3D.Transform3D: ...
    @winrt_commethod(7)
    def put_Transform3D(self, value: Windows.UI.Xaml.Media.Media3D.Transform3D) -> Void: ...
    @winrt_commethod(8)
    def get_CanDrag(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CanDrag(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def add_DragStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.DragStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DragStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_DropCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.DropCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DropCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def StartDragAsync(self, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    Transform3D = property(get_Transform3D, put_Transform3D)
    CanDrag = property(get_CanDrag, put_CanDrag)
class IUIElement4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement4'
    _iid_ = Guid('{69145cd4-199a-4657-9e57-e99e8f136712}')
    @winrt_commethod(6)
    def get_ContextFlyout(self) -> Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_commethod(7)
    def put_ContextFlyout(self, value: Windows.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_commethod(8)
    def get_ExitDisplayModeOnAccessKeyInvoked(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_ExitDisplayModeOnAccessKeyInvoked(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsAccessKeyScope(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsAccessKeyScope(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_AccessKeyScopeOwner(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def put_AccessKeyScopeOwner(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(14)
    def get_AccessKey(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_AccessKey(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def add_ContextRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.ContextRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ContextRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ContextCanceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.RoutedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ContextCanceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_AccessKeyDisplayRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_AccessKeyDisplayRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_AccessKeyDisplayDismissed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_AccessKeyDisplayDismissed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_AccessKeyInvoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_AccessKeyInvoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ContextFlyout = property(get_ContextFlyout, put_ContextFlyout)
    ExitDisplayModeOnAccessKeyInvoked = property(get_ExitDisplayModeOnAccessKeyInvoked, put_ExitDisplayModeOnAccessKeyInvoked)
    IsAccessKeyScope = property(get_IsAccessKeyScope, put_IsAccessKeyScope)
    AccessKeyScopeOwner = property(get_AccessKeyScopeOwner, put_AccessKeyScopeOwner)
    AccessKey = property(get_AccessKey, put_AccessKey)
class IUIElement5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement5'
    _iid_ = Guid('{8eed9bc2-a58c-4453-af0f-a92ee06d0317}')
    @winrt_commethod(6)
    def get_Lights(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.XamlLight]: ...
    @winrt_commethod(7)
    def get_KeyTipPlacementMode(self) -> Windows.UI.Xaml.Input.KeyTipPlacementMode: ...
    @winrt_commethod(8)
    def put_KeyTipPlacementMode(self, value: Windows.UI.Xaml.Input.KeyTipPlacementMode) -> Void: ...
    @winrt_commethod(9)
    def get_KeyTipHorizontalOffset(self) -> Double: ...
    @winrt_commethod(10)
    def put_KeyTipHorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def get_KeyTipVerticalOffset(self) -> Double: ...
    @winrt_commethod(12)
    def put_KeyTipVerticalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(13)
    def get_XYFocusKeyboardNavigation(self) -> Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode: ...
    @winrt_commethod(14)
    def put_XYFocusKeyboardNavigation(self, value: Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode) -> Void: ...
    @winrt_commethod(15)
    def get_XYFocusUpNavigationStrategy(self) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(16)
    def put_XYFocusUpNavigationStrategy(self, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(17)
    def get_XYFocusDownNavigationStrategy(self) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(18)
    def put_XYFocusDownNavigationStrategy(self, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(19)
    def get_XYFocusLeftNavigationStrategy(self) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(20)
    def put_XYFocusLeftNavigationStrategy(self, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(21)
    def get_XYFocusRightNavigationStrategy(self) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_commethod(22)
    def put_XYFocusRightNavigationStrategy(self, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_commethod(23)
    def get_HighContrastAdjustment(self) -> Windows.UI.Xaml.ElementHighContrastAdjustment: ...
    @winrt_commethod(24)
    def put_HighContrastAdjustment(self, value: Windows.UI.Xaml.ElementHighContrastAdjustment) -> Void: ...
    @winrt_commethod(25)
    def get_TabFocusNavigation(self) -> Windows.UI.Xaml.Input.KeyboardNavigationMode: ...
    @winrt_commethod(26)
    def put_TabFocusNavigation(self, value: Windows.UI.Xaml.Input.KeyboardNavigationMode) -> Void: ...
    @winrt_commethod(27)
    def add_GettingFocus(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_GettingFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_LosingFocus(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_LosingFocus(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_NoFocusCandidateFound(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.NoFocusCandidateFoundEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_NoFocusCandidateFound(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def StartBringIntoView(self) -> Void: ...
    @winrt_commethod(34)
    def StartBringIntoViewWithOptions(self, options: Windows.UI.Xaml.BringIntoViewOptions) -> Void: ...
    Lights = property(get_Lights, None)
    KeyTipPlacementMode = property(get_KeyTipPlacementMode, put_KeyTipPlacementMode)
    KeyTipHorizontalOffset = property(get_KeyTipHorizontalOffset, put_KeyTipHorizontalOffset)
    KeyTipVerticalOffset = property(get_KeyTipVerticalOffset, put_KeyTipVerticalOffset)
    XYFocusKeyboardNavigation = property(get_XYFocusKeyboardNavigation, put_XYFocusKeyboardNavigation)
    XYFocusUpNavigationStrategy = property(get_XYFocusUpNavigationStrategy, put_XYFocusUpNavigationStrategy)
    XYFocusDownNavigationStrategy = property(get_XYFocusDownNavigationStrategy, put_XYFocusDownNavigationStrategy)
    XYFocusLeftNavigationStrategy = property(get_XYFocusLeftNavigationStrategy, put_XYFocusLeftNavigationStrategy)
    XYFocusRightNavigationStrategy = property(get_XYFocusRightNavigationStrategy, put_XYFocusRightNavigationStrategy)
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    TabFocusNavigation = property(get_TabFocusNavigation, put_TabFocusNavigation)
class IUIElement7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement7'
    _iid_ = Guid('{cafc4968-6369-4249-80f9-3d656319e811}')
    @winrt_commethod(6)
    def get_KeyboardAccelerators(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_commethod(7)
    def add_CharacterReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.CharacterReceivedRoutedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_CharacterReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_ProcessKeyboardAccelerators(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ProcessKeyboardAccelerators(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_PreviewKeyDown(self, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_PreviewKeyDown(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_PreviewKeyUp(self, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_PreviewKeyUp(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def TryInvokeKeyboardAccelerator(self, args: Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
class IUIElement8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement8'
    _iid_ = Guid('{3ab70e85-d508-4477-b6f8-0e435701c836}')
    @winrt_commethod(6)
    def get_KeyTipTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def put_KeyTipTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(8)
    def get_KeyboardAcceleratorPlacementTarget(self) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(9)
    def put_KeyboardAcceleratorPlacementTarget(self, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(10)
    def get_KeyboardAcceleratorPlacementMode(self) -> Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode: ...
    @winrt_commethod(11)
    def put_KeyboardAcceleratorPlacementMode(self, value: Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode) -> Void: ...
    @winrt_commethod(12)
    def add_BringIntoViewRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.BringIntoViewRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_BringIntoViewRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    KeyTipTarget = property(get_KeyTipTarget, put_KeyTipTarget)
    KeyboardAcceleratorPlacementTarget = property(get_KeyboardAcceleratorPlacementTarget, put_KeyboardAcceleratorPlacementTarget)
    KeyboardAcceleratorPlacementMode = property(get_KeyboardAcceleratorPlacementMode, put_KeyboardAcceleratorPlacementMode)
class IUIElement9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElement9'
    _iid_ = Guid('{b4a04776-4e88-50ca-8f2b-08940d6c5f94}')
    @winrt_commethod(6)
    def get_CanBeScrollAnchor(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanBeScrollAnchor(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_OpacityTransition(self) -> Windows.UI.Xaml.ScalarTransition: ...
    @winrt_commethod(9)
    def put_OpacityTransition(self, value: Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_commethod(10)
    def get_Translation(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_Translation(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(12)
    def get_TranslationTransition(self) -> Windows.UI.Xaml.Vector3Transition: ...
    @winrt_commethod(13)
    def put_TranslationTransition(self, value: Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_commethod(14)
    def get_Rotation(self) -> Single: ...
    @winrt_commethod(15)
    def put_Rotation(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_RotationTransition(self) -> Windows.UI.Xaml.ScalarTransition: ...
    @winrt_commethod(17)
    def put_RotationTransition(self, value: Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_commethod(18)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(19)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(20)
    def get_ScaleTransition(self) -> Windows.UI.Xaml.Vector3Transition: ...
    @winrt_commethod(21)
    def put_ScaleTransition(self, value: Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_commethod(22)
    def get_TransformMatrix(self) -> Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_commethod(23)
    def put_TransformMatrix(self, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_commethod(24)
    def get_CenterPoint(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(25)
    def put_CenterPoint(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(26)
    def get_RotationAxis(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(27)
    def put_RotationAxis(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(28)
    def StartAnimation(self, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(29)
    def StopAnimation(self, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    CanBeScrollAnchor = property(get_CanBeScrollAnchor, put_CanBeScrollAnchor)
    OpacityTransition = property(get_OpacityTransition, put_OpacityTransition)
    Translation = property(get_Translation, put_Translation)
    TranslationTransition = property(get_TranslationTransition, put_TranslationTransition)
    Rotation = property(get_Rotation, put_Rotation)
    RotationTransition = property(get_RotationTransition, put_RotationTransition)
    Scale = property(get_Scale, put_Scale)
    ScaleTransition = property(get_ScaleTransition, put_ScaleTransition)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
class IUIElementFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementFactory'
    _iid_ = Guid('{b9ee93fe-a338-419f-ac32-91dcaadf5d08}')
class IUIElementOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides'
    _iid_ = Guid('{608d2f1d-7858-4aeb-89e4-b54e2c7ed3d3}')
    @winrt_commethod(6)
    def OnCreateAutomationPeer(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def OnDisconnectVisualChildren(self) -> Void: ...
    @winrt_commethod(8)
    def FindSubElementsForTouchTargeting(self, point: Windows.Foundation.Point, boundingRect: Windows.Foundation.Rect) -> Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]]: ...
class IUIElementOverrides7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides7'
    _iid_ = Guid('{b97f7f68-c29b-4c99-a1c3-952619d6e720}')
    @winrt_commethod(6)
    def GetChildrenInTabFocusOrder(self) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(7)
    def OnProcessKeyboardAccelerators(self, args: Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
class IUIElementOverrides8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides8'
    _iid_ = Guid('{4a5a645c-548d-48cf-b998-7844d6e235a1}')
    @winrt_commethod(6)
    def OnKeyboardAcceleratorInvoked(self, args: Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs) -> Void: ...
    @winrt_commethod(7)
    def OnBringIntoViewRequested(self, e: Windows.UI.Xaml.BringIntoViewRequestedEventArgs) -> Void: ...
class IUIElementOverrides9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementOverrides9'
    _iid_ = Guid('{9a6e5973-6d63-54f2-90fa-62813b20b7b9}')
    @winrt_commethod(6)
    def PopulatePropertyInfoOverride(self, propertyName: WinRT_String, animationPropertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
class IUIElementStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics'
    _iid_ = Guid('{58d3573b-f52c-45be-988b-a5869564873c}')
    @winrt_commethod(6)
    def get_KeyDownEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_KeyUpEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_PointerEnteredEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(9)
    def get_PointerPressedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(10)
    def get_PointerMovedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(11)
    def get_PointerReleasedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(12)
    def get_PointerExitedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(13)
    def get_PointerCaptureLostEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(14)
    def get_PointerCanceledEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(15)
    def get_PointerWheelChangedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(16)
    def get_TappedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(17)
    def get_DoubleTappedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(18)
    def get_HoldingEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(19)
    def get_RightTappedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(20)
    def get_ManipulationStartingEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(21)
    def get_ManipulationInertiaStartingEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(22)
    def get_ManipulationStartedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(23)
    def get_ManipulationDeltaEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(24)
    def get_ManipulationCompletedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(25)
    def get_DragEnterEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(26)
    def get_DragLeaveEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(27)
    def get_DragOverEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(28)
    def get_DropEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(29)
    def get_AllowDropProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(30)
    def get_OpacityProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(31)
    def get_ClipProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(32)
    def get_RenderTransformProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(33)
    def get_ProjectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(34)
    def get_RenderTransformOriginProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(35)
    def get_IsHitTestVisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(36)
    def get_VisibilityProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(37)
    def get_UseLayoutRoundingProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(38)
    def get_TransitionsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(39)
    def get_CacheModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(40)
    def get_IsTapEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(41)
    def get_IsDoubleTapEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(42)
    def get_IsRightTapEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(43)
    def get_IsHoldingEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(44)
    def get_ManipulationModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(45)
    def get_PointerCapturesProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    KeyDownEvent = property(get_KeyDownEvent, None)
    KeyUpEvent = property(get_KeyUpEvent, None)
    PointerEnteredEvent = property(get_PointerEnteredEvent, None)
    PointerPressedEvent = property(get_PointerPressedEvent, None)
    PointerMovedEvent = property(get_PointerMovedEvent, None)
    PointerReleasedEvent = property(get_PointerReleasedEvent, None)
    PointerExitedEvent = property(get_PointerExitedEvent, None)
    PointerCaptureLostEvent = property(get_PointerCaptureLostEvent, None)
    PointerCanceledEvent = property(get_PointerCanceledEvent, None)
    PointerWheelChangedEvent = property(get_PointerWheelChangedEvent, None)
    TappedEvent = property(get_TappedEvent, None)
    DoubleTappedEvent = property(get_DoubleTappedEvent, None)
    HoldingEvent = property(get_HoldingEvent, None)
    RightTappedEvent = property(get_RightTappedEvent, None)
    ManipulationStartingEvent = property(get_ManipulationStartingEvent, None)
    ManipulationInertiaStartingEvent = property(get_ManipulationInertiaStartingEvent, None)
    ManipulationStartedEvent = property(get_ManipulationStartedEvent, None)
    ManipulationDeltaEvent = property(get_ManipulationDeltaEvent, None)
    ManipulationCompletedEvent = property(get_ManipulationCompletedEvent, None)
    DragEnterEvent = property(get_DragEnterEvent, None)
    DragLeaveEvent = property(get_DragLeaveEvent, None)
    DragOverEvent = property(get_DragOverEvent, None)
    DropEvent = property(get_DropEvent, None)
    AllowDropProperty = property(get_AllowDropProperty, None)
    OpacityProperty = property(get_OpacityProperty, None)
    ClipProperty = property(get_ClipProperty, None)
    RenderTransformProperty = property(get_RenderTransformProperty, None)
    ProjectionProperty = property(get_ProjectionProperty, None)
    RenderTransformOriginProperty = property(get_RenderTransformOriginProperty, None)
    IsHitTestVisibleProperty = property(get_IsHitTestVisibleProperty, None)
    VisibilityProperty = property(get_VisibilityProperty, None)
    UseLayoutRoundingProperty = property(get_UseLayoutRoundingProperty, None)
    TransitionsProperty = property(get_TransitionsProperty, None)
    CacheModeProperty = property(get_CacheModeProperty, None)
    IsTapEnabledProperty = property(get_IsTapEnabledProperty, None)
    IsDoubleTapEnabledProperty = property(get_IsDoubleTapEnabledProperty, None)
    IsRightTapEnabledProperty = property(get_IsRightTapEnabledProperty, None)
    IsHoldingEnabledProperty = property(get_IsHoldingEnabledProperty, None)
    ManipulationModeProperty = property(get_ManipulationModeProperty, None)
    PointerCapturesProperty = property(get_PointerCapturesProperty, None)
class IUIElementStatics10(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics10'
    _iid_ = Guid('{60d25362-4b3e-53da-8b78-38db94ae8f26}')
    @winrt_commethod(6)
    def get_ShadowProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ShadowProperty = property(get_ShadowProperty, None)
class IUIElementStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics2'
    _iid_ = Guid('{58d3574b-f53c-45be-989b-a5869564874c}')
    @winrt_commethod(6)
    def get_CompositeModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CompositeModeProperty = property(get_CompositeModeProperty, None)
class IUIElementStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics3'
    _iid_ = Guid('{d1f87ade-eca1-4561-a32b-64601b4e0597}')
    @winrt_commethod(6)
    def get_Transform3DProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CanDragProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def TryStartDirectManipulation(self, value: Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    Transform3DProperty = property(get_Transform3DProperty, None)
    CanDragProperty = property(get_CanDragProperty, None)
class IUIElementStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics4'
    _iid_ = Guid('{1d157d61-16af-411f-b774-272375a4ac2c}')
    @winrt_commethod(6)
    def get_ContextFlyoutProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ExitDisplayModeOnAccessKeyInvokedProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsAccessKeyScopeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AccessKeyScopeOwnerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_AccessKeyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ContextFlyoutProperty = property(get_ContextFlyoutProperty, None)
    ExitDisplayModeOnAccessKeyInvokedProperty = property(get_ExitDisplayModeOnAccessKeyInvokedProperty, None)
    IsAccessKeyScopeProperty = property(get_IsAccessKeyScopeProperty, None)
    AccessKeyScopeOwnerProperty = property(get_AccessKeyScopeOwnerProperty, None)
    AccessKeyProperty = property(get_AccessKeyProperty, None)
class IUIElementStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics5'
    _iid_ = Guid('{59bd7d91-8fa3-4c65-ba1b-40df38556cbb}')
    @winrt_commethod(6)
    def get_LightsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_KeyTipPlacementModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_KeyTipHorizontalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_KeyTipVerticalOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_XYFocusKeyboardNavigationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_XYFocusUpNavigationStrategyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_XYFocusDownNavigationStrategyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_XYFocusLeftNavigationStrategyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_XYFocusRightNavigationStrategyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_HighContrastAdjustmentProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_TabFocusNavigationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    LightsProperty = property(get_LightsProperty, None)
    KeyTipPlacementModeProperty = property(get_KeyTipPlacementModeProperty, None)
    KeyTipHorizontalOffsetProperty = property(get_KeyTipHorizontalOffsetProperty, None)
    KeyTipVerticalOffsetProperty = property(get_KeyTipVerticalOffsetProperty, None)
    XYFocusKeyboardNavigationProperty = property(get_XYFocusKeyboardNavigationProperty, None)
    XYFocusUpNavigationStrategyProperty = property(get_XYFocusUpNavigationStrategyProperty, None)
    XYFocusDownNavigationStrategyProperty = property(get_XYFocusDownNavigationStrategyProperty, None)
    XYFocusLeftNavigationStrategyProperty = property(get_XYFocusLeftNavigationStrategyProperty, None)
    XYFocusRightNavigationStrategyProperty = property(get_XYFocusRightNavigationStrategyProperty, None)
    HighContrastAdjustmentProperty = property(get_HighContrastAdjustmentProperty, None)
    TabFocusNavigationProperty = property(get_TabFocusNavigationProperty, None)
class IUIElementStatics6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics6'
    _iid_ = Guid('{647e03b7-036a-4dea-9540-1dd7fd1266f1}')
    @winrt_commethod(6)
    def get_GettingFocusEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_LosingFocusEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_NoFocusCandidateFoundEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    GettingFocusEvent = property(get_GettingFocusEvent, None)
    LosingFocusEvent = property(get_LosingFocusEvent, None)
    NoFocusCandidateFoundEvent = property(get_NoFocusCandidateFoundEvent, None)
class IUIElementStatics7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics7'
    _iid_ = Guid('{da9b4493-a695-4145-ae93-888024396a0f}')
    @winrt_commethod(6)
    def get_PreviewKeyDownEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_CharacterReceivedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_PreviewKeyUpEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    PreviewKeyDownEvent = property(get_PreviewKeyDownEvent, None)
    CharacterReceivedEvent = property(get_CharacterReceivedEvent, None)
    PreviewKeyUpEvent = property(get_PreviewKeyUpEvent, None)
class IUIElementStatics8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics8'
    _iid_ = Guid('{17be3487-4875-4915-b0b1-a4c0f851df3f}')
    @winrt_commethod(6)
    def get_BringIntoViewRequestedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(7)
    def get_ContextRequestedEvent(self) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_commethod(8)
    def get_KeyTipTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_KeyboardAcceleratorPlacementTargetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_KeyboardAcceleratorPlacementModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def RegisterAsScrollPort(self, element: Windows.UI.Xaml.UIElement) -> Void: ...
    BringIntoViewRequestedEvent = property(get_BringIntoViewRequestedEvent, None)
    ContextRequestedEvent = property(get_ContextRequestedEvent, None)
    KeyTipTargetProperty = property(get_KeyTipTargetProperty, None)
    KeyboardAcceleratorPlacementTargetProperty = property(get_KeyboardAcceleratorPlacementTargetProperty, None)
    KeyboardAcceleratorPlacementModeProperty = property(get_KeyboardAcceleratorPlacementModeProperty, None)
class IUIElementStatics9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementStatics9'
    _iid_ = Guid('{71467e77-8ca3-5ed7-95db-d51cdad77f81}')
    @winrt_commethod(6)
    def get_CanBeScrollAnchorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CanBeScrollAnchorProperty = property(get_CanBeScrollAnchorProperty, None)
class IUIElementWeakCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementWeakCollection'
    _iid_ = Guid('{10341223-e66d-519e-acf8-556bd244eac3}')
class IUIElementWeakCollectionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUIElementWeakCollectionFactory'
    _iid_ = Guid('{57242561-188a-5304-8792-a43f35d90f99}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.UIElementWeakCollection: ...
class IUnhandledExceptionEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IUnhandledExceptionEventArgs'
    _iid_ = Guid('{7230269c-054e-4cf3-86c5-be90eb6863d5}')
    @winrt_commethod(6)
    def get_Exception(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Exception = property(get_Exception, None)
    Message = property(get_Message, None)
    Handled = property(get_Handled, put_Handled)
class IVector3Transition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVector3Transition'
    _iid_ = Guid('{d2e209dc-c4a2-5101-9a68-fa0150505589}')
    @winrt_commethod(6)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Components(self) -> Windows.UI.Xaml.Vector3TransitionComponents: ...
    @winrt_commethod(9)
    def put_Components(self, value: Windows.UI.Xaml.Vector3TransitionComponents) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    Components = property(get_Components, put_Components)
class IVector3TransitionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVector3TransitionFactory'
    _iid_ = Guid('{c3706699-ee9b-50dc-8807-f51d5a759495}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Vector3Transition: ...
class IVisualState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualState'
    _iid_ = Guid('{6320affc-c31a-4450-afde-f6ea7bd1f586}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Storyboard(self) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(8)
    def put_Storyboard(self, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    Name = property(get_Name, None)
    Storyboard = property(get_Storyboard, put_Storyboard)
class IVisualState2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualState2'
    _iid_ = Guid('{0fa0f896-64c0-45fb-8d24-fb83298c0d93}')
    @winrt_commethod(6)
    def get_Setters(self) -> Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_commethod(7)
    def get_StateTriggers(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.StateTriggerBase]: ...
    Setters = property(get_Setters, None)
    StateTriggers = property(get_StateTriggers, None)
class IVisualStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateChangedEventArgs'
    _iid_ = Guid('{fe216ab1-f31f-4791-8989-c70e1d9b59ff}')
    @winrt_commethod(6)
    def get_OldState(self) -> Windows.UI.Xaml.VisualState: ...
    @winrt_commethod(7)
    def put_OldState(self, value: Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_commethod(8)
    def get_NewState(self) -> Windows.UI.Xaml.VisualState: ...
    @winrt_commethod(9)
    def put_NewState(self, value: Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_commethod(10)
    def get_Control(self) -> Windows.UI.Xaml.Controls.Control: ...
    @winrt_commethod(11)
    def put_Control(self, value: Windows.UI.Xaml.Controls.Control) -> Void: ...
    OldState = property(get_OldState, put_OldState)
    NewState = property(get_NewState, put_NewState)
    Control = property(get_Control, put_Control)
class IVisualStateGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateGroup'
    _iid_ = Guid('{e4f9d9a4-e028-44de-9b15-4929ae0a26c2}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Transitions(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.VisualTransition]: ...
    @winrt_commethod(8)
    def get_States(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.VisualState]: ...
    @winrt_commethod(9)
    def get_CurrentState(self) -> Windows.UI.Xaml.VisualState: ...
    @winrt_commethod(10)
    def add_CurrentStateChanged(self, handler: Windows.UI.Xaml.VisualStateChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CurrentStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CurrentStateChanging(self, handler: Windows.UI.Xaml.VisualStateChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CurrentStateChanging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Name = property(get_Name, None)
    Transitions = property(get_Transitions, None)
    States = property(get_States, None)
    CurrentState = property(get_CurrentState, None)
class IVisualStateManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManager'
    _iid_ = Guid('{6fda9f9a-6fab-4112-9258-1006a3c3476e}')
class IVisualStateManagerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerFactory'
    _iid_ = Guid('{85e598fd-a575-47b6-9e30-383cd08585f2}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.VisualStateManager: ...
class IVisualStateManagerOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerOverrides'
    _iid_ = Guid('{4a66910e-7979-43c8-8ff4-ec6122750006}')
    @winrt_commethod(6)
    def GoToStateCore(self, control: Windows.UI.Xaml.Controls.Control, templateRoot: Windows.UI.Xaml.FrameworkElement, stateName: WinRT_String, group: Windows.UI.Xaml.VisualStateGroup, state: Windows.UI.Xaml.VisualState, useTransitions: Boolean) -> Boolean: ...
class IVisualStateManagerProtected(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerProtected'
    _iid_ = Guid('{4b3b8640-b0b7-404c-9ef4-d949640e245d}')
    @winrt_commethod(6)
    def RaiseCurrentStateChanging(self, stateGroup: Windows.UI.Xaml.VisualStateGroup, oldState: Windows.UI.Xaml.VisualState, newState: Windows.UI.Xaml.VisualState, control: Windows.UI.Xaml.Controls.Control) -> Void: ...
    @winrt_commethod(7)
    def RaiseCurrentStateChanged(self, stateGroup: Windows.UI.Xaml.VisualStateGroup, oldState: Windows.UI.Xaml.VisualState, newState: Windows.UI.Xaml.VisualState, control: Windows.UI.Xaml.Controls.Control) -> Void: ...
class IVisualStateManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualStateManagerStatics'
    _iid_ = Guid('{01d0e9e0-d713-414e-a74e-e63ec7ac8c3d}')
    @winrt_commethod(6)
    def GetVisualStateGroups(self, obj: Windows.UI.Xaml.FrameworkElement) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.VisualStateGroup]: ...
    @winrt_commethod(7)
    def get_CustomVisualStateManagerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetCustomVisualStateManager(self, obj: Windows.UI.Xaml.FrameworkElement) -> Windows.UI.Xaml.VisualStateManager: ...
    @winrt_commethod(9)
    def SetCustomVisualStateManager(self, obj: Windows.UI.Xaml.FrameworkElement, value: Windows.UI.Xaml.VisualStateManager) -> Void: ...
    @winrt_commethod(10)
    def GoToState(self, control: Windows.UI.Xaml.Controls.Control, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
    CustomVisualStateManagerProperty = property(get_CustomVisualStateManagerProperty, None)
class IVisualTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualTransition'
    _iid_ = Guid('{55c5905e-2bc7-400d-aaa4-1a2981491ee0}')
    @winrt_commethod(6)
    def get_GeneratedDuration(self) -> Windows.UI.Xaml.Duration: ...
    @winrt_commethod(7)
    def put_GeneratedDuration(self, value: Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_commethod(8)
    def get_GeneratedEasingFunction(self) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_commethod(9)
    def put_GeneratedEasingFunction(self, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_commethod(10)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_From(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Storyboard(self) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_commethod(15)
    def put_Storyboard(self, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    GeneratedDuration = property(get_GeneratedDuration, put_GeneratedDuration)
    GeneratedEasingFunction = property(get_GeneratedEasingFunction, put_GeneratedEasingFunction)
    To = property(get_To, put_To)
    From = property(get_From, put_From)
    Storyboard = property(get_Storyboard, put_Storyboard)
class IVisualTransitionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IVisualTransitionFactory'
    _iid_ = Guid('{ea75864f-d1e0-4dae-b429-89fc322724f4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.VisualTransition: ...
class IWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow'
    _iid_ = Guid('{3276167d-c9f6-462d-9de2-ae4c1fd8c2e5}')
    @winrt_commethod(6)
    def get_Bounds(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Content(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Content(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def get_CoreWindow(self) -> Windows.UI.Core.CoreWindow: ...
    @winrt_commethod(11)
    def get_Dispatcher(self) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_commethod(12)
    def add_Activated(self, handler: Windows.UI.Xaml.WindowActivatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Activated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Closed(self, handler: Windows.UI.Xaml.WindowClosedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_SizeChanged(self, handler: Windows.UI.Xaml.WindowSizeChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SizeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_VisibilityChanged(self, handler: Windows.UI.Xaml.WindowVisibilityChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_VisibilityChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def Activate(self) -> Void: ...
    @winrt_commethod(21)
    def Close(self) -> Void: ...
    Bounds = property(get_Bounds, None)
    Visible = property(get_Visible, None)
    Content = property(get_Content, put_Content)
    CoreWindow = property(get_CoreWindow, None)
    Dispatcher = property(get_Dispatcher, None)
class IWindow2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow2'
    _iid_ = Guid('{d384759f-34f6-4482-8435-f552f9b24cc8}')
    @winrt_commethod(6)
    def SetTitleBar(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
class IWindow3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow3'
    _iid_ = Guid('{b70bdc9d-1c35-462a-9b97-808d5af9f28e}')
    @winrt_commethod(6)
    def get_Compositor(self) -> Windows.UI.Composition.Compositor: ...
    Compositor = property(get_Compositor, None)
class IWindow4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindow4'
    _iid_ = Guid('{bfe1b8ce-6c40-50f9-854c-7021d2bc9de6}')
    @winrt_commethod(6)
    def get_UIContext(self) -> Windows.UI.UIContext: ...
    UIContext = property(get_UIContext, None)
class IWindowCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindowCreatedEventArgs'
    _iid_ = Guid('{31b71470-feff-4654-af48-9b398ab5772b}')
    @winrt_commethod(6)
    def get_Window(self) -> Windows.UI.Xaml.Window: ...
    Window = property(get_Window, None)
class IWindowStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IWindowStatics'
    _iid_ = Guid('{93328409-4ea1-4afa-83dc-0c4e73e88bb1}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.UI.Xaml.Window: ...
    Current = property(get_Current, None)
class IXamlRoot(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IXamlRoot'
    _iid_ = Guid('{34b50756-1696-5b6d-8e9b-c71464ccad5a}')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def get_Size(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_RasterizationScale(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsHostVisible(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_UIContext(self) -> Windows.UI.UIContext: ...
    @winrt_commethod(11)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.XamlRoot, Windows.UI.Xaml.XamlRootChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Content = property(get_Content, None)
    Size = property(get_Size, None)
    RasterizationScale = property(get_RasterizationScale, None)
    IsHostVisible = property(get_IsHostVisible, None)
    UIContext = property(get_UIContext, None)
class IXamlRootChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.IXamlRootChangedEventArgs'
    _iid_ = Guid('{92d71c21-d23c-5a17-bcb8-001504b6bb19}')
class LeavingBackgroundEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.LeavingBackgroundEventHandler'
    _iid_ = Guid('{aaad5dad-4fc6-4aa4-b7cf-877e36ada4f6}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.ApplicationModel.LeavingBackgroundEventArgs) -> Void: ...
LineStackingStrategy = Int32
LineStackingStrategy_MaxHeight: LineStackingStrategy = 0
LineStackingStrategy_BlockLineHeight: LineStackingStrategy = 1
LineStackingStrategy_BaselineToBaseline: LineStackingStrategy = 2
class MediaFailedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.ExceptionRoutedEventArgs
    default_interface: Windows.UI.Xaml.IMediaFailedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.MediaFailedRoutedEventArgs'
    @winrt_mixinmethod
    def get_ErrorTrace(self: Windows.UI.Xaml.IMediaFailedRoutedEventArgs) -> WinRT_String: ...
    ErrorTrace = property(get_ErrorTrace, None)
OpticalMarginAlignment = Int32
OpticalMarginAlignment_None: OpticalMarginAlignment = 0
OpticalMarginAlignment_TrimSideBearings: OpticalMarginAlignment = 1
class PointHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IPointHelper
    _classid_ = 'Windows.UI.Xaml.PointHelper'
    @winrt_classmethod
    def FromCoordinates(cls: Windows.UI.Xaml.IPointHelperStatics, x: Single, y: Single) -> Windows.Foundation.Point: ...
class PropertyChangedCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.PropertyChangedCallback'
    _iid_ = Guid('{5a9f8a25-d142-44a4-8231-fd676724f29b}')
    @winrt_commethod(3)
    def Invoke(self, d: Windows.UI.Xaml.DependencyObject, e: Windows.UI.Xaml.DependencyPropertyChangedEventArgs) -> Void: ...
class PropertyMetadata(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IPropertyMetadata
    _classid_ = 'Windows.UI.Xaml.PropertyMetadata'
    @winrt_factorymethod
    def CreateInstanceWithDefaultValue(cls: Windows.UI.Xaml.IPropertyMetadataFactory, defaultValue: Windows.Win32.System.WinRT.IInspectable_head, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_factorymethod
    def CreateInstanceWithDefaultValueAndCallback(cls: Windows.UI.Xaml.IPropertyMetadataFactory, defaultValue: Windows.Win32.System.WinRT.IInspectable_head, propertyChangedCallback: Windows.UI.Xaml.PropertyChangedCallback, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_mixinmethod
    def get_DefaultValue(self: Windows.UI.Xaml.IPropertyMetadata) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_CreateDefaultValueCallback(self: Windows.UI.Xaml.IPropertyMetadata) -> Windows.UI.Xaml.CreateDefaultValueCallback: ...
    @winrt_classmethod
    def CreateWithDefaultValue(cls: Windows.UI.Xaml.IPropertyMetadataStatics, defaultValue: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def CreateWithDefaultValueAndCallback(cls: Windows.UI.Xaml.IPropertyMetadataStatics, defaultValue: Windows.Win32.System.WinRT.IInspectable_head, propertyChangedCallback: Windows.UI.Xaml.PropertyChangedCallback) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def CreateWithFactory(cls: Windows.UI.Xaml.IPropertyMetadataStatics, createDefaultValueCallback: Windows.UI.Xaml.CreateDefaultValueCallback) -> Windows.UI.Xaml.PropertyMetadata: ...
    @winrt_classmethod
    def CreateWithFactoryAndCallback(cls: Windows.UI.Xaml.IPropertyMetadataStatics, createDefaultValueCallback: Windows.UI.Xaml.CreateDefaultValueCallback, propertyChangedCallback: Windows.UI.Xaml.PropertyChangedCallback) -> Windows.UI.Xaml.PropertyMetadata: ...
    DefaultValue = property(get_DefaultValue, None)
    CreateDefaultValueCallback = property(get_CreateDefaultValueCallback, None)
class PropertyPath(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IPropertyPath
    _classid_ = 'Windows.UI.Xaml.PropertyPath'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IPropertyPathFactory, path: WinRT_String) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.UI.Xaml.IPropertyPath) -> WinRT_String: ...
    Path = property(get_Path, None)
class _RectHelper_Meta_(ComPtr.__class__):
    pass
class RectHelper(ComPtr, metaclass=_RectHelper_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IRectHelper
    _classid_ = 'Windows.UI.Xaml.RectHelper'
    @winrt_classmethod
    def get_Empty(cls: Windows.UI.Xaml.IRectHelperStatics) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def FromCoordinatesAndDimensions(cls: Windows.UI.Xaml.IRectHelperStatics, x: Single, y: Single, width: Single, height: Single) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def FromPoints(cls: Windows.UI.Xaml.IRectHelperStatics, point1: Windows.Foundation.Point, point2: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def FromLocationAndSize(cls: Windows.UI.Xaml.IRectHelperStatics, location: Windows.Foundation.Point, size: Windows.Foundation.Size) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def GetIsEmpty(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect) -> Boolean: ...
    @winrt_classmethod
    def GetBottom(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def GetLeft(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def GetRight(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def GetTop(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect) -> Single: ...
    @winrt_classmethod
    def Contains(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect, point: Windows.Foundation.Point) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect, value: Windows.Foundation.Rect) -> Boolean: ...
    @winrt_classmethod
    def Intersect(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def UnionWithPoint(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect, point: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def UnionWithRect(cls: Windows.UI.Xaml.IRectHelperStatics, target: Windows.Foundation.Rect, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    _RectHelper_Meta_.Empty = property(get_Empty.__wrapped__, None)
class ResourceDictionary(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IResourceDictionary
    _classid_ = 'Windows.UI.Xaml.ResourceDictionary'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IResourceDictionaryFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ResourceDictionary: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Xaml.IResourceDictionary) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.UI.Xaml.IResourceDictionary, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_MergedDictionaries(self: Windows.UI.Xaml.IResourceDictionary) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.ResourceDictionary]: ...
    @winrt_mixinmethod
    def get_ThemeDictionaries(self: Windows.UI.Xaml.IResourceDictionary) -> Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head], key: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head], key: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head], key: Windows.Win32.System.WinRT.IInspectable_head, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head], key: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[Windows.Win32.System.WinRT.IInspectable_head, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Source = property(get_Source, put_Source)
    MergedDictionaries = property(get_MergedDictionaries, None)
    ThemeDictionaries = property(get_ThemeDictionaries, None)
    Size = property(get_Size, None)
class RoutedEvent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IRoutedEvent
    _classid_ = 'Windows.UI.Xaml.RoutedEvent'
class RoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.RoutedEventArgs'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IRoutedEventArgsFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.RoutedEventArgs: ...
    @winrt_mixinmethod
    def get_OriginalSource(self: Windows.UI.Xaml.IRoutedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    OriginalSource = property(get_OriginalSource, None)
class RoutedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.RoutedEventHandler'
    _iid_ = Guid('{a856e674-b0b6-4bc3-bba8-1ba06e40d4b5}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.RoutedEventArgs) -> Void: ...
class ScalarTransition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IScalarTransition
    _classid_ = 'Windows.UI.Xaml.ScalarTransition'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IScalarTransitionFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.ScalarTransition: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.UI.Xaml.IScalarTransition) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.UI.Xaml.IScalarTransition, value: Windows.Foundation.TimeSpan) -> Void: ...
    Duration = property(get_Duration, put_Duration)
class Setter(ComPtr):
    extends: Windows.UI.Xaml.SetterBase
    default_interface: Windows.UI.Xaml.ISetter
    _classid_ = 'Windows.UI.Xaml.Setter'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.ISetterFactory, targetProperty: Windows.UI.Xaml.DependencyProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Setter: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Setter: ...
    @winrt_mixinmethod
    def get_Property(self: Windows.UI.Xaml.ISetter) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_mixinmethod
    def put_Property(self: Windows.UI.Xaml.ISetter, value: Windows.UI.Xaml.DependencyProperty) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.ISetter) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.UI.Xaml.ISetter, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: Windows.UI.Xaml.ISetter2) -> Windows.UI.Xaml.TargetPropertyPath: ...
    @winrt_mixinmethod
    def put_Target(self: Windows.UI.Xaml.ISetter2, value: Windows.UI.Xaml.TargetPropertyPath) -> Void: ...
    Property = property(get_Property, put_Property)
    Value = property(get_Value, put_Value)
    Target = property(get_Target, put_Target)
class SetterBase(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.ISetterBase
    _classid_ = 'Windows.UI.Xaml.SetterBase'
    @winrt_mixinmethod
    def get_IsSealed(self: Windows.UI.Xaml.ISetterBase) -> Boolean: ...
    IsSealed = property(get_IsSealed, None)
class SetterBaseCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.ISetterBaseCollection
    _classid_ = 'Windows.UI.Xaml.SetterBaseCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_mixinmethod
    def get_IsSealed(self: Windows.UI.Xaml.ISetterBaseCollection) -> Boolean: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], index: UInt32) -> Windows.UI.Xaml.SetterBase: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.SetterBase]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], value: Windows.UI.Xaml.SetterBase, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], index: UInt32, value: Windows.UI.Xaml.SetterBase) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], index: UInt32, value: Windows.UI.Xaml.SetterBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], value: Windows.UI.Xaml.SetterBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.SetterBase)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.SetterBase], items: POINTER(Windows.UI.Xaml.SetterBase)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.SetterBase]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.SetterBase]: ...
    IsSealed = property(get_IsSealed, None)
    Size = property(get_Size, None)
class SizeChangedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.ISizeChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.SizeChangedEventArgs'
    @winrt_mixinmethod
    def get_PreviousSize(self: Windows.UI.Xaml.ISizeChangedEventArgs) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_NewSize(self: Windows.UI.Xaml.ISizeChangedEventArgs) -> Windows.Foundation.Size: ...
    PreviousSize = property(get_PreviousSize, None)
    NewSize = property(get_NewSize, None)
class SizeChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.SizeChangedEventHandler'
    _iid_ = Guid('{1115b13c-25d2-480b-89dc-eb3dcbd6b7fa}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.SizeChangedEventArgs) -> Void: ...
class _SizeHelper_Meta_(ComPtr.__class__):
    pass
class SizeHelper(ComPtr, metaclass=_SizeHelper_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.ISizeHelper
    _classid_ = 'Windows.UI.Xaml.SizeHelper'
    @winrt_classmethod
    def get_Empty(cls: Windows.UI.Xaml.ISizeHelperStatics) -> Windows.Foundation.Size: ...
    @winrt_classmethod
    def FromDimensions(cls: Windows.UI.Xaml.ISizeHelperStatics, width: Single, height: Single) -> Windows.Foundation.Size: ...
    @winrt_classmethod
    def GetIsEmpty(cls: Windows.UI.Xaml.ISizeHelperStatics, target: Windows.Foundation.Size) -> Boolean: ...
    @winrt_classmethod
    def Equals(cls: Windows.UI.Xaml.ISizeHelperStatics, target: Windows.Foundation.Size, value: Windows.Foundation.Size) -> Boolean: ...
    _SizeHelper_Meta_.Empty = property(get_Empty.__wrapped__, None)
class _StateTrigger_Meta_(ComPtr.__class__):
    pass
class StateTrigger(ComPtr, metaclass=_StateTrigger_Meta_):
    extends: Windows.UI.Xaml.StateTriggerBase
    default_interface: Windows.UI.Xaml.IStateTrigger
    _classid_ = 'Windows.UI.Xaml.StateTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.StateTrigger: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.UI.Xaml.IStateTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsActive(self: Windows.UI.Xaml.IStateTrigger, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsActiveProperty(cls: Windows.UI.Xaml.IStateTriggerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    IsActive = property(get_IsActive, put_IsActive)
    _StateTrigger_Meta_.IsActiveProperty = property(get_IsActiveProperty.__wrapped__, None)
class StateTriggerBase(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IStateTriggerBase
    _classid_ = 'Windows.UI.Xaml.StateTriggerBase'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IStateTriggerBaseFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.StateTriggerBase: ...
    @winrt_mixinmethod
    def SetActive(self: Windows.UI.Xaml.IStateTriggerBaseProtected, IsActive: Boolean) -> Void: ...
class Style(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IStyle
    _classid_ = 'Windows.UI.Xaml.Style'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Style: ...
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IStyleFactory, targetType: Windows.UI.Xaml.Interop.TypeName) -> Windows.UI.Xaml.Style: ...
    @winrt_mixinmethod
    def get_IsSealed(self: Windows.UI.Xaml.IStyle) -> Boolean: ...
    @winrt_mixinmethod
    def get_Setters(self: Windows.UI.Xaml.IStyle) -> Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_mixinmethod
    def get_TargetType(self: Windows.UI.Xaml.IStyle) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def put_TargetType(self: Windows.UI.Xaml.IStyle, value: Windows.UI.Xaml.Interop.TypeName) -> Void: ...
    @winrt_mixinmethod
    def get_BasedOn(self: Windows.UI.Xaml.IStyle) -> Windows.UI.Xaml.Style: ...
    @winrt_mixinmethod
    def put_BasedOn(self: Windows.UI.Xaml.IStyle, value: Windows.UI.Xaml.Style) -> Void: ...
    @winrt_mixinmethod
    def Seal(self: Windows.UI.Xaml.IStyle) -> Void: ...
    IsSealed = property(get_IsSealed, None)
    Setters = property(get_Setters, None)
    TargetType = property(get_TargetType, put_TargetType)
    BasedOn = property(get_BasedOn, put_BasedOn)
class SuspendingEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.SuspendingEventHandler'
    _iid_ = Guid('{23429465-e36a-40e2-b139-a4704602a6e1}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.ApplicationModel.SuspendingEventArgs) -> Void: ...
class TargetPropertyPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.ITargetPropertyPath
    _classid_ = 'Windows.UI.Xaml.TargetPropertyPath'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.ITargetPropertyPathFactory, targetProperty: Windows.UI.Xaml.DependencyProperty) -> Windows.UI.Xaml.TargetPropertyPath: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.TargetPropertyPath: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.UI.Xaml.ITargetPropertyPath) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_Path(self: Windows.UI.Xaml.ITargetPropertyPath, value: Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: Windows.UI.Xaml.ITargetPropertyPath) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Target(self: Windows.UI.Xaml.ITargetPropertyPath, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Path = property(get_Path, put_Path)
    Target = property(get_Target, put_Target)
TextAlignment = Int32
TextAlignment_Center: TextAlignment = 0
TextAlignment_Left: TextAlignment = 1
TextAlignment_Start: TextAlignment = 1
TextAlignment_Right: TextAlignment = 2
TextAlignment_End: TextAlignment = 2
TextAlignment_Justify: TextAlignment = 3
TextAlignment_DetectFromContent: TextAlignment = 4
TextLineBounds = Int32
TextLineBounds_Full: TextLineBounds = 0
TextLineBounds_TrimToCapHeight: TextLineBounds = 1
TextLineBounds_TrimToBaseline: TextLineBounds = 2
TextLineBounds_Tight: TextLineBounds = 3
TextReadingOrder = Int32
TextReadingOrder_Default: TextReadingOrder = 0
TextReadingOrder_UseFlowDirection: TextReadingOrder = 0
TextReadingOrder_DetectFromContent: TextReadingOrder = 1
TextTrimming = Int32
TextTrimming_None: TextTrimming = 0
TextTrimming_CharacterEllipsis: TextTrimming = 1
TextTrimming_WordEllipsis: TextTrimming = 2
TextTrimming_Clip: TextTrimming = 3
TextWrapping = Int32
TextWrapping_NoWrap: TextWrapping = 1
TextWrapping_Wrap: TextWrapping = 2
TextWrapping_WrapWholeWords: TextWrapping = 3
class Thickness(EasyCastStructure):
    Left: Double
    Top: Double
    Right: Double
    Bottom: Double
class ThicknessHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IThicknessHelper
    _classid_ = 'Windows.UI.Xaml.ThicknessHelper'
    @winrt_classmethod
    def FromLengths(cls: Windows.UI.Xaml.IThicknessHelperStatics, left: Double, top: Double, right: Double, bottom: Double) -> Windows.UI.Xaml.Thickness: ...
    @winrt_classmethod
    def FromUniformLength(cls: Windows.UI.Xaml.IThicknessHelperStatics, uniformLength: Double) -> Windows.UI.Xaml.Thickness: ...
class TriggerAction(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.ITriggerAction
    _classid_ = 'Windows.UI.Xaml.TriggerAction'
class TriggerActionCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction]
    _classid_ = 'Windows.UI.Xaml.TriggerActionCollection'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.TriggerActionCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], index: UInt32) -> Windows.UI.Xaml.TriggerAction: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.TriggerAction]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], value: Windows.UI.Xaml.TriggerAction, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], index: UInt32, value: Windows.UI.Xaml.TriggerAction) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], index: UInt32, value: Windows.UI.Xaml.TriggerAction) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], value: Windows.UI.Xaml.TriggerAction) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.TriggerAction)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerAction], items: POINTER(Windows.UI.Xaml.TriggerAction)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.TriggerAction]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.TriggerAction]: ...
    Size = property(get_Size, None)
class TriggerBase(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.ITriggerBase
    _classid_ = 'Windows.UI.Xaml.TriggerBase'
class TriggerCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase]
    _classid_ = 'Windows.UI.Xaml.TriggerCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], index: UInt32) -> Windows.UI.Xaml.TriggerBase: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.TriggerBase]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], value: Windows.UI.Xaml.TriggerBase, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], index: UInt32, value: Windows.UI.Xaml.TriggerBase) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], index: UInt32, value: Windows.UI.Xaml.TriggerBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], value: Windows.UI.Xaml.TriggerBase) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.TriggerBase)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.TriggerBase], items: POINTER(Windows.UI.Xaml.TriggerBase)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.TriggerBase]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.TriggerBase]: ...
    Size = property(get_Size, None)
class _UIElement_Meta_(ComPtr.__class__):
    pass
class UIElement(ComPtr, metaclass=_UIElement_Meta_):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IUIElement
    _classid_ = 'Windows.UI.Xaml.UIElement'
    @winrt_mixinmethod
    def get_DesiredSize(self: Windows.UI.Xaml.IUIElement) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_AllowDrop(self: Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowDrop(self: Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: Windows.UI.Xaml.IUIElement) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: Windows.UI.Xaml.IUIElement, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Clip(self: Windows.UI.Xaml.IUIElement) -> Windows.UI.Xaml.Media.RectangleGeometry: ...
    @winrt_mixinmethod
    def put_Clip(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Media.RectangleGeometry) -> Void: ...
    @winrt_mixinmethod
    def get_RenderTransform(self: Windows.UI.Xaml.IUIElement) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_RenderTransform(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def get_Projection(self: Windows.UI.Xaml.IUIElement) -> Windows.UI.Xaml.Media.Projection: ...
    @winrt_mixinmethod
    def put_Projection(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Media.Projection) -> Void: ...
    @winrt_mixinmethod
    def get_RenderTransformOrigin(self: Windows.UI.Xaml.IUIElement) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_RenderTransformOrigin(self: Windows.UI.Xaml.IUIElement, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_IsHitTestVisible(self: Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHitTestVisible(self: Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Visibility(self: Windows.UI.Xaml.IUIElement) -> Windows.UI.Xaml.Visibility: ...
    @winrt_mixinmethod
    def put_Visibility(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Visibility) -> Void: ...
    @winrt_mixinmethod
    def get_RenderSize(self: Windows.UI.Xaml.IUIElement) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_UseLayoutRounding(self: Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseLayoutRounding(self: Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Transitions(self: Windows.UI.Xaml.IUIElement) -> Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_mixinmethod
    def put_Transitions(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_mixinmethod
    def get_CacheMode(self: Windows.UI.Xaml.IUIElement) -> Windows.UI.Xaml.Media.CacheMode: ...
    @winrt_mixinmethod
    def put_CacheMode(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Media.CacheMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsTapEnabled(self: Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTapEnabled(self: Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDoubleTapEnabled(self: Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDoubleTapEnabled(self: Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRightTapEnabled(self: Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRightTapEnabled(self: Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsHoldingEnabled(self: Windows.UI.Xaml.IUIElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHoldingEnabled(self: Windows.UI.Xaml.IUIElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ManipulationMode(self: Windows.UI.Xaml.IUIElement) -> Windows.UI.Xaml.Input.ManipulationModes: ...
    @winrt_mixinmethod
    def put_ManipulationMode(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Input.ManipulationModes) -> Void: ...
    @winrt_mixinmethod
    def get_PointerCaptures(self: Windows.UI.Xaml.IUIElement) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Input.Pointer]: ...
    @winrt_mixinmethod
    def add_KeyUp(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyUp(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyDown(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyDown(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LostFocus(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LostFocus(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragEnter(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragEnter(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragLeave(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragLeave(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragOver(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragOver(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Drop(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.DragEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Drop(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerEntered(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerCaptureLost(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCaptureLost(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerCanceled(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCanceled(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerWheelChanged(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.PointerEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerWheelChanged(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.TappedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DoubleTapped(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.DoubleTappedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DoubleTapped(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Holding(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.HoldingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Holding(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RightTapped(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.RightTappedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RightTapped(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarting(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.ManipulationStartingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarting(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationInertiaStarting(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.ManipulationInertiaStartingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationInertiaStarting(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.ManipulationStartedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationDelta(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.ManipulationDeltaEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationDelta(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: Windows.UI.Xaml.IUIElement, handler: Windows.UI.Xaml.Input.ManipulationCompletedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: Windows.UI.Xaml.IUIElement, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Measure(self: Windows.UI.Xaml.IUIElement, availableSize: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def Arrange(self: Windows.UI.Xaml.IUIElement, finalRect: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def CapturePointer(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    @winrt_mixinmethod
    def ReleasePointerCapture(self: Windows.UI.Xaml.IUIElement, value: Windows.UI.Xaml.Input.Pointer) -> Void: ...
    @winrt_mixinmethod
    def ReleasePointerCaptures(self: Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def AddHandler(self: Windows.UI.Xaml.IUIElement, routedEvent: Windows.UI.Xaml.RoutedEvent, handler: Windows.Win32.System.WinRT.IInspectable_head, handledEventsToo: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RemoveHandler(self: Windows.UI.Xaml.IUIElement, routedEvent: Windows.UI.Xaml.RoutedEvent, handler: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def TransformToVisual(self: Windows.UI.Xaml.IUIElement, visual: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def InvalidateMeasure(self: Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def InvalidateArrange(self: Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def UpdateLayout(self: Windows.UI.Xaml.IUIElement) -> Void: ...
    @winrt_mixinmethod
    def get_CompositeMode(self: Windows.UI.Xaml.IUIElement2) -> Windows.UI.Xaml.Media.ElementCompositeMode: ...
    @winrt_mixinmethod
    def put_CompositeMode(self: Windows.UI.Xaml.IUIElement2, value: Windows.UI.Xaml.Media.ElementCompositeMode) -> Void: ...
    @winrt_mixinmethod
    def CancelDirectManipulations(self: Windows.UI.Xaml.IUIElement2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Transform3D(self: Windows.UI.Xaml.IUIElement3) -> Windows.UI.Xaml.Media.Media3D.Transform3D: ...
    @winrt_mixinmethod
    def put_Transform3D(self: Windows.UI.Xaml.IUIElement3, value: Windows.UI.Xaml.Media.Media3D.Transform3D) -> Void: ...
    @winrt_mixinmethod
    def get_CanDrag(self: Windows.UI.Xaml.IUIElement3) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanDrag(self: Windows.UI.Xaml.IUIElement3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_DragStarting(self: Windows.UI.Xaml.IUIElement3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.DragStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragStarting(self: Windows.UI.Xaml.IUIElement3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DropCompleted(self: Windows.UI.Xaml.IUIElement3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.DropCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DropCompleted(self: Windows.UI.Xaml.IUIElement3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartDragAsync(self: Windows.UI.Xaml.IUIElement3, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_mixinmethod
    def get_ContextFlyout(self: Windows.UI.Xaml.IUIElement4) -> Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_mixinmethod
    def put_ContextFlyout(self: Windows.UI.Xaml.IUIElement4, value: Windows.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_mixinmethod
    def get_ExitDisplayModeOnAccessKeyInvoked(self: Windows.UI.Xaml.IUIElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExitDisplayModeOnAccessKeyInvoked(self: Windows.UI.Xaml.IUIElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAccessKeyScope(self: Windows.UI.Xaml.IUIElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAccessKeyScope(self: Windows.UI.Xaml.IUIElement4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AccessKeyScopeOwner(self: Windows.UI.Xaml.IUIElement4) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_AccessKeyScopeOwner(self: Windows.UI.Xaml.IUIElement4, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_AccessKey(self: Windows.UI.Xaml.IUIElement4) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AccessKey(self: Windows.UI.Xaml.IUIElement4, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_ContextRequested(self: Windows.UI.Xaml.IUIElement4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.ContextRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContextRequested(self: Windows.UI.Xaml.IUIElement4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContextCanceled(self: Windows.UI.Xaml.IUIElement4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.RoutedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContextCanceled(self: Windows.UI.Xaml.IUIElement4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccessKeyDisplayRequested(self: Windows.UI.Xaml.IUIElement4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.AccessKeyDisplayRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessKeyDisplayRequested(self: Windows.UI.Xaml.IUIElement4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccessKeyDisplayDismissed(self: Windows.UI.Xaml.IUIElement4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.AccessKeyDisplayDismissedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessKeyDisplayDismissed(self: Windows.UI.Xaml.IUIElement4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccessKeyInvoked(self: Windows.UI.Xaml.IUIElement4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.AccessKeyInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessKeyInvoked(self: Windows.UI.Xaml.IUIElement4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Lights(self: Windows.UI.Xaml.IUIElement5) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.XamlLight]: ...
    @winrt_mixinmethod
    def get_KeyTipPlacementMode(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.Input.KeyTipPlacementMode: ...
    @winrt_mixinmethod
    def put_KeyTipPlacementMode(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.Input.KeyTipPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTipHorizontalOffset(self: Windows.UI.Xaml.IUIElement5) -> Double: ...
    @winrt_mixinmethod
    def put_KeyTipHorizontalOffset(self: Windows.UI.Xaml.IUIElement5, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTipVerticalOffset(self: Windows.UI.Xaml.IUIElement5) -> Double: ...
    @winrt_mixinmethod
    def put_KeyTipVerticalOffset(self: Windows.UI.Xaml.IUIElement5, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusKeyboardNavigation(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode: ...
    @winrt_mixinmethod
    def put_XYFocusKeyboardNavigation(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusUpNavigationStrategy(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusUpNavigationStrategy(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusDownNavigationStrategy(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusDownNavigationStrategy(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusLeftNavigationStrategy(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusLeftNavigationStrategy(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_XYFocusRightNavigationStrategy(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.Input.XYFocusNavigationStrategy: ...
    @winrt_mixinmethod
    def put_XYFocusRightNavigationStrategy(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.Input.XYFocusNavigationStrategy) -> Void: ...
    @winrt_mixinmethod
    def get_HighContrastAdjustment(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.ElementHighContrastAdjustment: ...
    @winrt_mixinmethod
    def put_HighContrastAdjustment(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.ElementHighContrastAdjustment) -> Void: ...
    @winrt_mixinmethod
    def get_TabFocusNavigation(self: Windows.UI.Xaml.IUIElement5) -> Windows.UI.Xaml.Input.KeyboardNavigationMode: ...
    @winrt_mixinmethod
    def put_TabFocusNavigation(self: Windows.UI.Xaml.IUIElement5, value: Windows.UI.Xaml.Input.KeyboardNavigationMode) -> Void: ...
    @winrt_mixinmethod
    def add_GettingFocus(self: Windows.UI.Xaml.IUIElement5, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.GettingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GettingFocus(self: Windows.UI.Xaml.IUIElement5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LosingFocus(self: Windows.UI.Xaml.IUIElement5, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.LosingFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LosingFocus(self: Windows.UI.Xaml.IUIElement5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NoFocusCandidateFound(self: Windows.UI.Xaml.IUIElement5, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.NoFocusCandidateFoundEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NoFocusCandidateFound(self: Windows.UI.Xaml.IUIElement5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartBringIntoView(self: Windows.UI.Xaml.IUIElement5) -> Void: ...
    @winrt_mixinmethod
    def StartBringIntoViewWithOptions(self: Windows.UI.Xaml.IUIElement5, options: Windows.UI.Xaml.BringIntoViewOptions) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAccelerators(self: Windows.UI.Xaml.IUIElement7) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Input.KeyboardAccelerator]: ...
    @winrt_mixinmethod
    def add_CharacterReceived(self: Windows.UI.Xaml.IUIElement7, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.CharacterReceivedRoutedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CharacterReceived(self: Windows.UI.Xaml.IUIElement7, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProcessKeyboardAccelerators(self: Windows.UI.Xaml.IUIElement7, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProcessKeyboardAccelerators(self: Windows.UI.Xaml.IUIElement7, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PreviewKeyDown(self: Windows.UI.Xaml.IUIElement7, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PreviewKeyDown(self: Windows.UI.Xaml.IUIElement7, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PreviewKeyUp(self: Windows.UI.Xaml.IUIElement7, handler: Windows.UI.Xaml.Input.KeyEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PreviewKeyUp(self: Windows.UI.Xaml.IUIElement7, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryInvokeKeyboardAccelerator(self: Windows.UI.Xaml.IUIElement7, args: Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_mixinmethod
    def get_KeyTipTarget(self: Windows.UI.Xaml.IUIElement8) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_KeyTipTarget(self: Windows.UI.Xaml.IUIElement8, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAcceleratorPlacementTarget(self: Windows.UI.Xaml.IUIElement8) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_KeyboardAcceleratorPlacementTarget(self: Windows.UI.Xaml.IUIElement8, value: Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_KeyboardAcceleratorPlacementMode(self: Windows.UI.Xaml.IUIElement8) -> Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode: ...
    @winrt_mixinmethod
    def put_KeyboardAcceleratorPlacementMode(self: Windows.UI.Xaml.IUIElement8, value: Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def add_BringIntoViewRequested(self: Windows.UI.Xaml.IUIElement8, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.UIElement, Windows.UI.Xaml.BringIntoViewRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BringIntoViewRequested(self: Windows.UI.Xaml.IUIElement8, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CanBeScrollAnchor(self: Windows.UI.Xaml.IUIElement9) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanBeScrollAnchor(self: Windows.UI.Xaml.IUIElement9, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OpacityTransition(self: Windows.UI.Xaml.IUIElement9) -> Windows.UI.Xaml.ScalarTransition: ...
    @winrt_mixinmethod
    def put_OpacityTransition(self: Windows.UI.Xaml.IUIElement9, value: Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_mixinmethod
    def get_Translation(self: Windows.UI.Xaml.IUIElement9) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Translation(self: Windows.UI.Xaml.IUIElement9, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_TranslationTransition(self: Windows.UI.Xaml.IUIElement9) -> Windows.UI.Xaml.Vector3Transition: ...
    @winrt_mixinmethod
    def put_TranslationTransition(self: Windows.UI.Xaml.IUIElement9, value: Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: Windows.UI.Xaml.IUIElement9) -> Single: ...
    @winrt_mixinmethod
    def put_Rotation(self: Windows.UI.Xaml.IUIElement9, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationTransition(self: Windows.UI.Xaml.IUIElement9) -> Windows.UI.Xaml.ScalarTransition: ...
    @winrt_mixinmethod
    def put_RotationTransition(self: Windows.UI.Xaml.IUIElement9, value: Windows.UI.Xaml.ScalarTransition) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Xaml.IUIElement9) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Xaml.IUIElement9, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleTransition(self: Windows.UI.Xaml.IUIElement9) -> Windows.UI.Xaml.Vector3Transition: ...
    @winrt_mixinmethod
    def put_ScaleTransition(self: Windows.UI.Xaml.IUIElement9, value: Windows.UI.Xaml.Vector3Transition) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: Windows.UI.Xaml.IUIElement9) -> Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: Windows.UI.Xaml.IUIElement9, value: Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: Windows.UI.Xaml.IUIElement9) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: Windows.UI.Xaml.IUIElement9, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAxis(self: Windows.UI.Xaml.IUIElement9) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RotationAxis(self: Windows.UI.Xaml.IUIElement9, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def StartAnimation(self: Windows.UI.Xaml.IUIElement9, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def StopAnimation(self: Windows.UI.Xaml.IUIElement9, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def get_ActualOffset(self: Windows.UI.Xaml.IUIElement10) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ActualSize(self: Windows.UI.Xaml.IUIElement10) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_XamlRoot(self: Windows.UI.Xaml.IUIElement10) -> Windows.UI.Xaml.XamlRoot: ...
    @winrt_mixinmethod
    def put_XamlRoot(self: Windows.UI.Xaml.IUIElement10, value: Windows.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_mixinmethod
    def get_UIContext(self: Windows.UI.Xaml.IUIElement10) -> Windows.UI.UIContext: ...
    @winrt_mixinmethod
    def get_Shadow(self: Windows.UI.Xaml.IUIElement10) -> Windows.UI.Xaml.Media.Shadow: ...
    @winrt_mixinmethod
    def put_Shadow(self: Windows.UI.Xaml.IUIElement10, value: Windows.UI.Xaml.Media.Shadow) -> Void: ...
    @winrt_mixinmethod
    def OnCreateAutomationPeer(self: Windows.UI.Xaml.IUIElementOverrides) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def OnDisconnectVisualChildren(self: Windows.UI.Xaml.IUIElementOverrides) -> Void: ...
    @winrt_mixinmethod
    def FindSubElementsForTouchTargeting(self: Windows.UI.Xaml.IUIElementOverrides, point: Windows.Foundation.Point, boundingRect: Windows.Foundation.Rect) -> Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]]: ...
    @winrt_mixinmethod
    def GetChildrenInTabFocusOrder(self: Windows.UI.Xaml.IUIElementOverrides7) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def OnProcessKeyboardAccelerators(self: Windows.UI.Xaml.IUIElementOverrides7, args: Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnKeyboardAcceleratorInvoked(self: Windows.UI.Xaml.IUIElementOverrides8, args: Windows.UI.Xaml.Input.KeyboardAcceleratorInvokedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def OnBringIntoViewRequested(self: Windows.UI.Xaml.IUIElementOverrides8, e: Windows.UI.Xaml.BringIntoViewRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfoOverride(self: Windows.UI.Xaml.IUIElementOverrides9, propertyName: WinRT_String, animationPropertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfo(self: Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, propertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_classmethod
    def get_ShadowProperty(cls: Windows.UI.Xaml.IUIElementStatics10) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanBeScrollAnchorProperty(cls: Windows.UI.Xaml.IUIElementStatics9) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BringIntoViewRequestedEvent(cls: Windows.UI.Xaml.IUIElementStatics8) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ContextRequestedEvent(cls: Windows.UI.Xaml.IUIElementStatics8) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_KeyTipTargetProperty(cls: Windows.UI.Xaml.IUIElementStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyboardAcceleratorPlacementTargetProperty(cls: Windows.UI.Xaml.IUIElementStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyboardAcceleratorPlacementModeProperty(cls: Windows.UI.Xaml.IUIElementStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def RegisterAsScrollPort(cls: Windows.UI.Xaml.IUIElementStatics8, element: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_PreviewKeyDownEvent(cls: Windows.UI.Xaml.IUIElementStatics7) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_CharacterReceivedEvent(cls: Windows.UI.Xaml.IUIElementStatics7) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PreviewKeyUpEvent(cls: Windows.UI.Xaml.IUIElementStatics7) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_GettingFocusEvent(cls: Windows.UI.Xaml.IUIElementStatics6) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_LosingFocusEvent(cls: Windows.UI.Xaml.IUIElementStatics6) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_NoFocusCandidateFoundEvent(cls: Windows.UI.Xaml.IUIElementStatics6) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_LightsProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTipPlacementModeProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTipHorizontalOffsetProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyTipVerticalOffsetProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusKeyboardNavigationProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusUpNavigationStrategyProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusDownNavigationStrategyProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusLeftNavigationStrategyProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_XYFocusRightNavigationStrategyProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HighContrastAdjustmentProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TabFocusNavigationProperty(cls: Windows.UI.Xaml.IUIElementStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContextFlyoutProperty(cls: Windows.UI.Xaml.IUIElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ExitDisplayModeOnAccessKeyInvokedProperty(cls: Windows.UI.Xaml.IUIElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsAccessKeyScopeProperty(cls: Windows.UI.Xaml.IUIElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AccessKeyScopeOwnerProperty(cls: Windows.UI.Xaml.IUIElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: Windows.UI.Xaml.IUIElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Transform3DProperty(cls: Windows.UI.Xaml.IUIElementStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanDragProperty(cls: Windows.UI.Xaml.IUIElementStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def TryStartDirectManipulation(cls: Windows.UI.Xaml.IUIElementStatics3, value: Windows.UI.Xaml.Input.Pointer) -> Boolean: ...
    @winrt_classmethod
    def get_CompositeModeProperty(cls: Windows.UI.Xaml.IUIElementStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_KeyDownEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_KeyUpEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerEnteredEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerPressedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerMovedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerReleasedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerExitedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerCaptureLostEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerCanceledEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_PointerWheelChangedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_TappedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DoubleTappedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_HoldingEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_RightTappedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationStartingEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationInertiaStartingEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationStartedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationDeltaEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_ManipulationCompletedEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DragEnterEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DragLeaveEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DragOverEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_DropEvent(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.RoutedEvent: ...
    @winrt_classmethod
    def get_AllowDropProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OpacityProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ClipProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RenderTransformProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ProjectionProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RenderTransformOriginProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsHitTestVisibleProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibilityProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_UseLayoutRoundingProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransitionsProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CacheModeProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsTapEnabledProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsDoubleTapEnabledProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsRightTapEnabledProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsHoldingEnabledProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ManipulationModeProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerCapturesProperty(cls: Windows.UI.Xaml.IUIElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    DesiredSize = property(get_DesiredSize, None)
    AllowDrop = property(get_AllowDrop, put_AllowDrop)
    Opacity = property(get_Opacity, put_Opacity)
    Clip = property(get_Clip, put_Clip)
    RenderTransform = property(get_RenderTransform, put_RenderTransform)
    Projection = property(get_Projection, put_Projection)
    RenderTransformOrigin = property(get_RenderTransformOrigin, put_RenderTransformOrigin)
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
    Visibility = property(get_Visibility, put_Visibility)
    RenderSize = property(get_RenderSize, None)
    UseLayoutRounding = property(get_UseLayoutRounding, put_UseLayoutRounding)
    Transitions = property(get_Transitions, put_Transitions)
    CacheMode = property(get_CacheMode, put_CacheMode)
    IsTapEnabled = property(get_IsTapEnabled, put_IsTapEnabled)
    IsDoubleTapEnabled = property(get_IsDoubleTapEnabled, put_IsDoubleTapEnabled)
    IsRightTapEnabled = property(get_IsRightTapEnabled, put_IsRightTapEnabled)
    IsHoldingEnabled = property(get_IsHoldingEnabled, put_IsHoldingEnabled)
    ManipulationMode = property(get_ManipulationMode, put_ManipulationMode)
    PointerCaptures = property(get_PointerCaptures, None)
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
    Transform3D = property(get_Transform3D, put_Transform3D)
    CanDrag = property(get_CanDrag, put_CanDrag)
    ContextFlyout = property(get_ContextFlyout, put_ContextFlyout)
    ExitDisplayModeOnAccessKeyInvoked = property(get_ExitDisplayModeOnAccessKeyInvoked, put_ExitDisplayModeOnAccessKeyInvoked)
    IsAccessKeyScope = property(get_IsAccessKeyScope, put_IsAccessKeyScope)
    AccessKeyScopeOwner = property(get_AccessKeyScopeOwner, put_AccessKeyScopeOwner)
    AccessKey = property(get_AccessKey, put_AccessKey)
    Lights = property(get_Lights, None)
    KeyTipPlacementMode = property(get_KeyTipPlacementMode, put_KeyTipPlacementMode)
    KeyTipHorizontalOffset = property(get_KeyTipHorizontalOffset, put_KeyTipHorizontalOffset)
    KeyTipVerticalOffset = property(get_KeyTipVerticalOffset, put_KeyTipVerticalOffset)
    XYFocusKeyboardNavigation = property(get_XYFocusKeyboardNavigation, put_XYFocusKeyboardNavigation)
    XYFocusUpNavigationStrategy = property(get_XYFocusUpNavigationStrategy, put_XYFocusUpNavigationStrategy)
    XYFocusDownNavigationStrategy = property(get_XYFocusDownNavigationStrategy, put_XYFocusDownNavigationStrategy)
    XYFocusLeftNavigationStrategy = property(get_XYFocusLeftNavigationStrategy, put_XYFocusLeftNavigationStrategy)
    XYFocusRightNavigationStrategy = property(get_XYFocusRightNavigationStrategy, put_XYFocusRightNavigationStrategy)
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    TabFocusNavigation = property(get_TabFocusNavigation, put_TabFocusNavigation)
    KeyboardAccelerators = property(get_KeyboardAccelerators, None)
    KeyTipTarget = property(get_KeyTipTarget, put_KeyTipTarget)
    KeyboardAcceleratorPlacementTarget = property(get_KeyboardAcceleratorPlacementTarget, put_KeyboardAcceleratorPlacementTarget)
    KeyboardAcceleratorPlacementMode = property(get_KeyboardAcceleratorPlacementMode, put_KeyboardAcceleratorPlacementMode)
    CanBeScrollAnchor = property(get_CanBeScrollAnchor, put_CanBeScrollAnchor)
    OpacityTransition = property(get_OpacityTransition, put_OpacityTransition)
    Translation = property(get_Translation, put_Translation)
    TranslationTransition = property(get_TranslationTransition, put_TranslationTransition)
    Rotation = property(get_Rotation, put_Rotation)
    RotationTransition = property(get_RotationTransition, put_RotationTransition)
    Scale = property(get_Scale, put_Scale)
    ScaleTransition = property(get_ScaleTransition, put_ScaleTransition)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    ActualOffset = property(get_ActualOffset, None)
    ActualSize = property(get_ActualSize, None)
    XamlRoot = property(get_XamlRoot, put_XamlRoot)
    UIContext = property(get_UIContext, None)
    Shadow = property(get_Shadow, put_Shadow)
    _UIElement_Meta_.ShadowProperty = property(get_ShadowProperty.__wrapped__, None)
    _UIElement_Meta_.CanBeScrollAnchorProperty = property(get_CanBeScrollAnchorProperty.__wrapped__, None)
    _UIElement_Meta_.BringIntoViewRequestedEvent = property(get_BringIntoViewRequestedEvent.__wrapped__, None)
    _UIElement_Meta_.ContextRequestedEvent = property(get_ContextRequestedEvent.__wrapped__, None)
    _UIElement_Meta_.KeyTipTargetProperty = property(get_KeyTipTargetProperty.__wrapped__, None)
    _UIElement_Meta_.KeyboardAcceleratorPlacementTargetProperty = property(get_KeyboardAcceleratorPlacementTargetProperty.__wrapped__, None)
    _UIElement_Meta_.KeyboardAcceleratorPlacementModeProperty = property(get_KeyboardAcceleratorPlacementModeProperty.__wrapped__, None)
    _UIElement_Meta_.PreviewKeyDownEvent = property(get_PreviewKeyDownEvent.__wrapped__, None)
    _UIElement_Meta_.CharacterReceivedEvent = property(get_CharacterReceivedEvent.__wrapped__, None)
    _UIElement_Meta_.PreviewKeyUpEvent = property(get_PreviewKeyUpEvent.__wrapped__, None)
    _UIElement_Meta_.GettingFocusEvent = property(get_GettingFocusEvent.__wrapped__, None)
    _UIElement_Meta_.LosingFocusEvent = property(get_LosingFocusEvent.__wrapped__, None)
    _UIElement_Meta_.NoFocusCandidateFoundEvent = property(get_NoFocusCandidateFoundEvent.__wrapped__, None)
    _UIElement_Meta_.LightsProperty = property(get_LightsProperty.__wrapped__, None)
    _UIElement_Meta_.KeyTipPlacementModeProperty = property(get_KeyTipPlacementModeProperty.__wrapped__, None)
    _UIElement_Meta_.KeyTipHorizontalOffsetProperty = property(get_KeyTipHorizontalOffsetProperty.__wrapped__, None)
    _UIElement_Meta_.KeyTipVerticalOffsetProperty = property(get_KeyTipVerticalOffsetProperty.__wrapped__, None)
    _UIElement_Meta_.XYFocusKeyboardNavigationProperty = property(get_XYFocusKeyboardNavigationProperty.__wrapped__, None)
    _UIElement_Meta_.XYFocusUpNavigationStrategyProperty = property(get_XYFocusUpNavigationStrategyProperty.__wrapped__, None)
    _UIElement_Meta_.XYFocusDownNavigationStrategyProperty = property(get_XYFocusDownNavigationStrategyProperty.__wrapped__, None)
    _UIElement_Meta_.XYFocusLeftNavigationStrategyProperty = property(get_XYFocusLeftNavigationStrategyProperty.__wrapped__, None)
    _UIElement_Meta_.XYFocusRightNavigationStrategyProperty = property(get_XYFocusRightNavigationStrategyProperty.__wrapped__, None)
    _UIElement_Meta_.HighContrastAdjustmentProperty = property(get_HighContrastAdjustmentProperty.__wrapped__, None)
    _UIElement_Meta_.TabFocusNavigationProperty = property(get_TabFocusNavigationProperty.__wrapped__, None)
    _UIElement_Meta_.ContextFlyoutProperty = property(get_ContextFlyoutProperty.__wrapped__, None)
    _UIElement_Meta_.ExitDisplayModeOnAccessKeyInvokedProperty = property(get_ExitDisplayModeOnAccessKeyInvokedProperty.__wrapped__, None)
    _UIElement_Meta_.IsAccessKeyScopeProperty = property(get_IsAccessKeyScopeProperty.__wrapped__, None)
    _UIElement_Meta_.AccessKeyScopeOwnerProperty = property(get_AccessKeyScopeOwnerProperty.__wrapped__, None)
    _UIElement_Meta_.AccessKeyProperty = property(get_AccessKeyProperty.__wrapped__, None)
    _UIElement_Meta_.Transform3DProperty = property(get_Transform3DProperty.__wrapped__, None)
    _UIElement_Meta_.CanDragProperty = property(get_CanDragProperty.__wrapped__, None)
    _UIElement_Meta_.CompositeModeProperty = property(get_CompositeModeProperty.__wrapped__, None)
    _UIElement_Meta_.KeyDownEvent = property(get_KeyDownEvent.__wrapped__, None)
    _UIElement_Meta_.KeyUpEvent = property(get_KeyUpEvent.__wrapped__, None)
    _UIElement_Meta_.PointerEnteredEvent = property(get_PointerEnteredEvent.__wrapped__, None)
    _UIElement_Meta_.PointerPressedEvent = property(get_PointerPressedEvent.__wrapped__, None)
    _UIElement_Meta_.PointerMovedEvent = property(get_PointerMovedEvent.__wrapped__, None)
    _UIElement_Meta_.PointerReleasedEvent = property(get_PointerReleasedEvent.__wrapped__, None)
    _UIElement_Meta_.PointerExitedEvent = property(get_PointerExitedEvent.__wrapped__, None)
    _UIElement_Meta_.PointerCaptureLostEvent = property(get_PointerCaptureLostEvent.__wrapped__, None)
    _UIElement_Meta_.PointerCanceledEvent = property(get_PointerCanceledEvent.__wrapped__, None)
    _UIElement_Meta_.PointerWheelChangedEvent = property(get_PointerWheelChangedEvent.__wrapped__, None)
    _UIElement_Meta_.TappedEvent = property(get_TappedEvent.__wrapped__, None)
    _UIElement_Meta_.DoubleTappedEvent = property(get_DoubleTappedEvent.__wrapped__, None)
    _UIElement_Meta_.HoldingEvent = property(get_HoldingEvent.__wrapped__, None)
    _UIElement_Meta_.RightTappedEvent = property(get_RightTappedEvent.__wrapped__, None)
    _UIElement_Meta_.ManipulationStartingEvent = property(get_ManipulationStartingEvent.__wrapped__, None)
    _UIElement_Meta_.ManipulationInertiaStartingEvent = property(get_ManipulationInertiaStartingEvent.__wrapped__, None)
    _UIElement_Meta_.ManipulationStartedEvent = property(get_ManipulationStartedEvent.__wrapped__, None)
    _UIElement_Meta_.ManipulationDeltaEvent = property(get_ManipulationDeltaEvent.__wrapped__, None)
    _UIElement_Meta_.ManipulationCompletedEvent = property(get_ManipulationCompletedEvent.__wrapped__, None)
    _UIElement_Meta_.DragEnterEvent = property(get_DragEnterEvent.__wrapped__, None)
    _UIElement_Meta_.DragLeaveEvent = property(get_DragLeaveEvent.__wrapped__, None)
    _UIElement_Meta_.DragOverEvent = property(get_DragOverEvent.__wrapped__, None)
    _UIElement_Meta_.DropEvent = property(get_DropEvent.__wrapped__, None)
    _UIElement_Meta_.AllowDropProperty = property(get_AllowDropProperty.__wrapped__, None)
    _UIElement_Meta_.OpacityProperty = property(get_OpacityProperty.__wrapped__, None)
    _UIElement_Meta_.ClipProperty = property(get_ClipProperty.__wrapped__, None)
    _UIElement_Meta_.RenderTransformProperty = property(get_RenderTransformProperty.__wrapped__, None)
    _UIElement_Meta_.ProjectionProperty = property(get_ProjectionProperty.__wrapped__, None)
    _UIElement_Meta_.RenderTransformOriginProperty = property(get_RenderTransformOriginProperty.__wrapped__, None)
    _UIElement_Meta_.IsHitTestVisibleProperty = property(get_IsHitTestVisibleProperty.__wrapped__, None)
    _UIElement_Meta_.VisibilityProperty = property(get_VisibilityProperty.__wrapped__, None)
    _UIElement_Meta_.UseLayoutRoundingProperty = property(get_UseLayoutRoundingProperty.__wrapped__, None)
    _UIElement_Meta_.TransitionsProperty = property(get_TransitionsProperty.__wrapped__, None)
    _UIElement_Meta_.CacheModeProperty = property(get_CacheModeProperty.__wrapped__, None)
    _UIElement_Meta_.IsTapEnabledProperty = property(get_IsTapEnabledProperty.__wrapped__, None)
    _UIElement_Meta_.IsDoubleTapEnabledProperty = property(get_IsDoubleTapEnabledProperty.__wrapped__, None)
    _UIElement_Meta_.IsRightTapEnabledProperty = property(get_IsRightTapEnabledProperty.__wrapped__, None)
    _UIElement_Meta_.IsHoldingEnabledProperty = property(get_IsHoldingEnabledProperty.__wrapped__, None)
    _UIElement_Meta_.ManipulationModeProperty = property(get_ManipulationModeProperty.__wrapped__, None)
    _UIElement_Meta_.PointerCapturesProperty = property(get_PointerCapturesProperty.__wrapped__, None)
class UIElementWeakCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IUIElementWeakCollection
    _classid_ = 'Windows.UI.Xaml.UIElementWeakCollection'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IUIElementWeakCollectionFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.UIElementWeakCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], index: UInt32) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.UIElement]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], value: Windows.UI.Xaml.UIElement, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], index: UInt32, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], index: UInt32, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.UIElement)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement], items: POINTER(Windows.UI.Xaml.UIElement)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.UIElement]: ...
    Size = property(get_Size, None)
class UnhandledExceptionEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IUnhandledExceptionEventArgs
    _classid_ = 'Windows.UI.Xaml.UnhandledExceptionEventArgs'
    @winrt_mixinmethod
    def get_Exception(self: Windows.UI.Xaml.IUnhandledExceptionEventArgs) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.UI.Xaml.IUnhandledExceptionEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.IUnhandledExceptionEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.IUnhandledExceptionEventArgs, value: Boolean) -> Void: ...
    Exception = property(get_Exception, None)
    Message = property(get_Message, None)
    Handled = property(get_Handled, put_Handled)
class UnhandledExceptionEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.UnhandledExceptionEventHandler'
    _iid_ = Guid('{9274e6bd-49a1-4958-beee-d0e19587b6e3}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.UnhandledExceptionEventArgs) -> Void: ...
class Vector3Transition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IVector3Transition
    _classid_ = 'Windows.UI.Xaml.Vector3Transition'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IVector3TransitionFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Vector3Transition: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.UI.Xaml.IVector3Transition) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.UI.Xaml.IVector3Transition, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Components(self: Windows.UI.Xaml.IVector3Transition) -> Windows.UI.Xaml.Vector3TransitionComponents: ...
    @winrt_mixinmethod
    def put_Components(self: Windows.UI.Xaml.IVector3Transition, value: Windows.UI.Xaml.Vector3TransitionComponents) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    Components = property(get_Components, put_Components)
Vector3TransitionComponents = UInt32
X: Vector3TransitionComponents = 1
Y: Vector3TransitionComponents = 2
Z: Vector3TransitionComponents = 4
VerticalAlignment = Int32
VerticalAlignment_Top: VerticalAlignment = 0
VerticalAlignment_Center: VerticalAlignment = 1
VerticalAlignment_Bottom: VerticalAlignment = 2
VerticalAlignment_Stretch: VerticalAlignment = 3
Visibility = Int32
Visibility_Visible: Visibility = 0
Visibility_Collapsed: Visibility = 1
class VisualState(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IVisualState
    _classid_ = 'Windows.UI.Xaml.VisualState'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.UI.Xaml.IVisualState) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Storyboard(self: Windows.UI.Xaml.IVisualState) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: Windows.UI.Xaml.IVisualState, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    @winrt_mixinmethod
    def get_Setters(self: Windows.UI.Xaml.IVisualState2) -> Windows.UI.Xaml.SetterBaseCollection: ...
    @winrt_mixinmethod
    def get_StateTriggers(self: Windows.UI.Xaml.IVisualState2) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.StateTriggerBase]: ...
    Name = property(get_Name, None)
    Storyboard = property(get_Storyboard, put_Storyboard)
    Setters = property(get_Setters, None)
    StateTriggers = property(get_StateTriggers, None)
class VisualStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IVisualStateChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.VisualStateChangedEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.VisualStateChangedEventArgs: ...
    @winrt_mixinmethod
    def get_OldState(self: Windows.UI.Xaml.IVisualStateChangedEventArgs) -> Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def put_OldState(self: Windows.UI.Xaml.IVisualStateChangedEventArgs, value: Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_mixinmethod
    def get_NewState(self: Windows.UI.Xaml.IVisualStateChangedEventArgs) -> Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def put_NewState(self: Windows.UI.Xaml.IVisualStateChangedEventArgs, value: Windows.UI.Xaml.VisualState) -> Void: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.UI.Xaml.IVisualStateChangedEventArgs) -> Windows.UI.Xaml.Controls.Control: ...
    @winrt_mixinmethod
    def put_Control(self: Windows.UI.Xaml.IVisualStateChangedEventArgs, value: Windows.UI.Xaml.Controls.Control) -> Void: ...
    OldState = property(get_OldState, put_OldState)
    NewState = property(get_NewState, put_NewState)
    Control = property(get_Control, put_Control)
class VisualStateChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.VisualStateChangedEventHandler'
    _iid_ = Guid('{e6d5bbd5-e029-43a6-b36d-84a81042d774}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.VisualStateChangedEventArgs) -> Void: ...
class VisualStateGroup(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IVisualStateGroup
    _classid_ = 'Windows.UI.Xaml.VisualStateGroup'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.VisualStateGroup: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.UI.Xaml.IVisualStateGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Transitions(self: Windows.UI.Xaml.IVisualStateGroup) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.VisualTransition]: ...
    @winrt_mixinmethod
    def get_States(self: Windows.UI.Xaml.IVisualStateGroup) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.VisualState]: ...
    @winrt_mixinmethod
    def get_CurrentState(self: Windows.UI.Xaml.IVisualStateGroup) -> Windows.UI.Xaml.VisualState: ...
    @winrt_mixinmethod
    def add_CurrentStateChanged(self: Windows.UI.Xaml.IVisualStateGroup, handler: Windows.UI.Xaml.VisualStateChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentStateChanged(self: Windows.UI.Xaml.IVisualStateGroup, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CurrentStateChanging(self: Windows.UI.Xaml.IVisualStateGroup, handler: Windows.UI.Xaml.VisualStateChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentStateChanging(self: Windows.UI.Xaml.IVisualStateGroup, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Name = property(get_Name, None)
    Transitions = property(get_Transitions, None)
    States = property(get_States, None)
    CurrentState = property(get_CurrentState, None)
class _VisualStateManager_Meta_(ComPtr.__class__):
    pass
class VisualStateManager(ComPtr, metaclass=_VisualStateManager_Meta_):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IVisualStateManager
    _classid_ = 'Windows.UI.Xaml.VisualStateManager'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IVisualStateManagerFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.VisualStateManager: ...
    @winrt_mixinmethod
    def RaiseCurrentStateChanging(self: Windows.UI.Xaml.IVisualStateManagerProtected, stateGroup: Windows.UI.Xaml.VisualStateGroup, oldState: Windows.UI.Xaml.VisualState, newState: Windows.UI.Xaml.VisualState, control: Windows.UI.Xaml.Controls.Control) -> Void: ...
    @winrt_mixinmethod
    def RaiseCurrentStateChanged(self: Windows.UI.Xaml.IVisualStateManagerProtected, stateGroup: Windows.UI.Xaml.VisualStateGroup, oldState: Windows.UI.Xaml.VisualState, newState: Windows.UI.Xaml.VisualState, control: Windows.UI.Xaml.Controls.Control) -> Void: ...
    @winrt_mixinmethod
    def GoToStateCore(self: Windows.UI.Xaml.IVisualStateManagerOverrides, control: Windows.UI.Xaml.Controls.Control, templateRoot: Windows.UI.Xaml.FrameworkElement, stateName: WinRT_String, group: Windows.UI.Xaml.VisualStateGroup, state: Windows.UI.Xaml.VisualState, useTransitions: Boolean) -> Boolean: ...
    @winrt_classmethod
    def GetVisualStateGroups(cls: Windows.UI.Xaml.IVisualStateManagerStatics, obj: Windows.UI.Xaml.FrameworkElement) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.VisualStateGroup]: ...
    @winrt_classmethod
    def get_CustomVisualStateManagerProperty(cls: Windows.UI.Xaml.IVisualStateManagerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetCustomVisualStateManager(cls: Windows.UI.Xaml.IVisualStateManagerStatics, obj: Windows.UI.Xaml.FrameworkElement) -> Windows.UI.Xaml.VisualStateManager: ...
    @winrt_classmethod
    def SetCustomVisualStateManager(cls: Windows.UI.Xaml.IVisualStateManagerStatics, obj: Windows.UI.Xaml.FrameworkElement, value: Windows.UI.Xaml.VisualStateManager) -> Void: ...
    @winrt_classmethod
    def GoToState(cls: Windows.UI.Xaml.IVisualStateManagerStatics, control: Windows.UI.Xaml.Controls.Control, stateName: WinRT_String, useTransitions: Boolean) -> Boolean: ...
    _VisualStateManager_Meta_.CustomVisualStateManagerProperty = property(get_CustomVisualStateManagerProperty.__wrapped__, None)
class VisualTransition(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.IVisualTransition
    _classid_ = 'Windows.UI.Xaml.VisualTransition'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.IVisualTransitionFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.VisualTransition: ...
    @winrt_mixinmethod
    def get_GeneratedDuration(self: Windows.UI.Xaml.IVisualTransition) -> Windows.UI.Xaml.Duration: ...
    @winrt_mixinmethod
    def put_GeneratedDuration(self: Windows.UI.Xaml.IVisualTransition, value: Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_mixinmethod
    def get_GeneratedEasingFunction(self: Windows.UI.Xaml.IVisualTransition) -> Windows.UI.Xaml.Media.Animation.EasingFunctionBase: ...
    @winrt_mixinmethod
    def put_GeneratedEasingFunction(self: Windows.UI.Xaml.IVisualTransition, value: Windows.UI.Xaml.Media.Animation.EasingFunctionBase) -> Void: ...
    @winrt_mixinmethod
    def get_To(self: Windows.UI.Xaml.IVisualTransition) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: Windows.UI.Xaml.IVisualTransition, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: Windows.UI.Xaml.IVisualTransition) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_From(self: Windows.UI.Xaml.IVisualTransition, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Storyboard(self: Windows.UI.Xaml.IVisualTransition) -> Windows.UI.Xaml.Media.Animation.Storyboard: ...
    @winrt_mixinmethod
    def put_Storyboard(self: Windows.UI.Xaml.IVisualTransition, value: Windows.UI.Xaml.Media.Animation.Storyboard) -> Void: ...
    GeneratedDuration = property(get_GeneratedDuration, put_GeneratedDuration)
    GeneratedEasingFunction = property(get_GeneratedEasingFunction, put_GeneratedEasingFunction)
    To = property(get_To, put_To)
    From = property(get_From, put_From)
    Storyboard = property(get_Storyboard, put_Storyboard)
class _Window_Meta_(ComPtr.__class__):
    pass
class Window(ComPtr, metaclass=_Window_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IWindow
    _classid_ = 'Windows.UI.Xaml.Window'
    @winrt_mixinmethod
    def get_Bounds(self: Windows.UI.Xaml.IWindow) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Visible(self: Windows.UI.Xaml.IWindow) -> Boolean: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Xaml.IWindow) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Content(self: Windows.UI.Xaml.IWindow, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_CoreWindow(self: Windows.UI.Xaml.IWindow) -> Windows.UI.Core.CoreWindow: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.UI.Xaml.IWindow) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def add_Activated(self: Windows.UI.Xaml.IWindow, handler: Windows.UI.Xaml.WindowActivatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: Windows.UI.Xaml.IWindow, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.UI.Xaml.IWindow, handler: Windows.UI.Xaml.WindowClosedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.UI.Xaml.IWindow, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SizeChanged(self: Windows.UI.Xaml.IWindow, handler: Windows.UI.Xaml.WindowSizeChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SizeChanged(self: Windows.UI.Xaml.IWindow, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VisibilityChanged(self: Windows.UI.Xaml.IWindow, handler: Windows.UI.Xaml.WindowVisibilityChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisibilityChanged(self: Windows.UI.Xaml.IWindow, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Activate(self: Windows.UI.Xaml.IWindow) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.UI.Xaml.IWindow) -> Void: ...
    @winrt_mixinmethod
    def SetTitleBar(self: Windows.UI.Xaml.IWindow2, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_Compositor(self: Windows.UI.Xaml.IWindow3) -> Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def get_UIContext(self: Windows.UI.Xaml.IWindow4) -> Windows.UI.UIContext: ...
    @winrt_classmethod
    def get_Current(cls: Windows.UI.Xaml.IWindowStatics) -> Windows.UI.Xaml.Window: ...
    Bounds = property(get_Bounds, None)
    Visible = property(get_Visible, None)
    Content = property(get_Content, put_Content)
    CoreWindow = property(get_CoreWindow, None)
    Dispatcher = property(get_Dispatcher, None)
    Compositor = property(get_Compositor, None)
    UIContext = property(get_UIContext, None)
    _Window_Meta_.Current = property(get_Current.__wrapped__, None)
class WindowActivatedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.WindowActivatedEventHandler'
    _iid_ = Guid('{18026348-8619-4c7b-b534-ced45d9de219}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Core.WindowActivatedEventArgs) -> Void: ...
class WindowClosedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.WindowClosedEventHandler'
    _iid_ = Guid('{0db89161-20d7-45df-9122-ba89576703ba}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Core.CoreWindowEventArgs) -> Void: ...
class WindowCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IWindowCreatedEventArgs
    _classid_ = 'Windows.UI.Xaml.WindowCreatedEventArgs'
    @winrt_mixinmethod
    def get_Window(self: Windows.UI.Xaml.IWindowCreatedEventArgs) -> Windows.UI.Xaml.Window: ...
    Window = property(get_Window, None)
class WindowSizeChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.WindowSizeChangedEventHandler'
    _iid_ = Guid('{5c21c742-2ced-4fd9-ba38-7118d40e966b}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Core.WindowSizeChangedEventArgs) -> Void: ...
class WindowVisibilityChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.WindowVisibilityChangedEventHandler'
    _iid_ = Guid('{10406ad6-b090-4a4a-b2ad-d682df27130f}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Core.VisibilityChangedEventArgs) -> Void: ...
class XamlRoot(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IXamlRoot
    _classid_ = 'Windows.UI.Xaml.XamlRoot'
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Xaml.IXamlRoot) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Xaml.IXamlRoot) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_RasterizationScale(self: Windows.UI.Xaml.IXamlRoot) -> Double: ...
    @winrt_mixinmethod
    def get_IsHostVisible(self: Windows.UI.Xaml.IXamlRoot) -> Boolean: ...
    @winrt_mixinmethod
    def get_UIContext(self: Windows.UI.Xaml.IXamlRoot) -> Windows.UI.UIContext: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.UI.Xaml.IXamlRoot, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.XamlRoot, Windows.UI.Xaml.XamlRootChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.UI.Xaml.IXamlRoot, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Content = property(get_Content, None)
    Size = property(get_Size, None)
    RasterizationScale = property(get_RasterizationScale, None)
    IsHostVisible = property(get_IsHostVisible, None)
    UIContext = property(get_UIContext, None)
class XamlRootChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.IXamlRootChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.XamlRootChangedEventArgs'
make_head(_module, 'AdaptiveTrigger')
make_head(_module, 'Application')
make_head(_module, 'ApplicationInitializationCallback')
make_head(_module, 'ApplicationInitializationCallbackParams')
make_head(_module, 'BindingFailedEventArgs')
make_head(_module, 'BindingFailedEventHandler')
make_head(_module, 'BringIntoViewOptions')
make_head(_module, 'BringIntoViewRequestedEventArgs')
make_head(_module, 'BrushTransition')
make_head(_module, 'ColorPaletteResources')
make_head(_module, 'CornerRadius')
make_head(_module, 'CornerRadiusHelper')
make_head(_module, 'CreateDefaultValueCallback')
make_head(_module, 'DataContextChangedEventArgs')
make_head(_module, 'DataTemplate')
make_head(_module, 'DataTemplateKey')
make_head(_module, 'DebugSettings')
make_head(_module, 'DependencyObject')
make_head(_module, 'DependencyObjectCollection')
make_head(_module, 'DependencyProperty')
make_head(_module, 'DependencyPropertyChangedCallback')
make_head(_module, 'DependencyPropertyChangedEventArgs')
make_head(_module, 'DependencyPropertyChangedEventHandler')
make_head(_module, 'DispatcherTimer')
make_head(_module, 'DragEventArgs')
make_head(_module, 'DragEventHandler')
make_head(_module, 'DragOperationDeferral')
make_head(_module, 'DragStartingEventArgs')
make_head(_module, 'DragUI')
make_head(_module, 'DragUIOverride')
make_head(_module, 'DropCompletedEventArgs')
make_head(_module, 'Duration')
make_head(_module, 'DurationHelper')
make_head(_module, 'EffectiveViewportChangedEventArgs')
make_head(_module, 'ElementFactoryGetArgs')
make_head(_module, 'ElementFactoryRecycleArgs')
make_head(_module, 'ElementSoundPlayer')
make_head(_module, 'EnteredBackgroundEventHandler')
make_head(_module, 'EventTrigger')
make_head(_module, 'ExceptionRoutedEventArgs')
make_head(_module, 'ExceptionRoutedEventHandler')
make_head(_module, 'FrameworkElement')
make_head(_module, 'FrameworkTemplate')
make_head(_module, 'FrameworkView')
make_head(_module, 'FrameworkViewSource')
make_head(_module, 'GridLength')
make_head(_module, 'GridLengthHelper')
make_head(_module, 'IAdaptiveTrigger')
make_head(_module, 'IAdaptiveTriggerFactory')
make_head(_module, 'IAdaptiveTriggerStatics')
make_head(_module, 'IApplication')
make_head(_module, 'IApplication2')
make_head(_module, 'IApplication3')
make_head(_module, 'IApplicationFactory')
make_head(_module, 'IApplicationInitializationCallbackParams')
make_head(_module, 'IApplicationOverrides')
make_head(_module, 'IApplicationOverrides2')
make_head(_module, 'IApplicationStatics')
make_head(_module, 'IBindingFailedEventArgs')
make_head(_module, 'IBringIntoViewOptions')
make_head(_module, 'IBringIntoViewOptions2')
make_head(_module, 'IBringIntoViewRequestedEventArgs')
make_head(_module, 'IBrushTransition')
make_head(_module, 'IBrushTransitionFactory')
make_head(_module, 'IColorPaletteResources')
make_head(_module, 'IColorPaletteResourcesFactory')
make_head(_module, 'ICornerRadiusHelper')
make_head(_module, 'ICornerRadiusHelperStatics')
make_head(_module, 'IDataContextChangedEventArgs')
make_head(_module, 'IDataTemplate')
make_head(_module, 'IDataTemplateExtension')
make_head(_module, 'IDataTemplateFactory')
make_head(_module, 'IDataTemplateKey')
make_head(_module, 'IDataTemplateKeyFactory')
make_head(_module, 'IDataTemplateStatics2')
make_head(_module, 'IDebugSettings')
make_head(_module, 'IDebugSettings2')
make_head(_module, 'IDebugSettings3')
make_head(_module, 'IDebugSettings4')
make_head(_module, 'IDependencyObject')
make_head(_module, 'IDependencyObject2')
make_head(_module, 'IDependencyObjectCollectionFactory')
make_head(_module, 'IDependencyObjectFactory')
make_head(_module, 'IDependencyProperty')
make_head(_module, 'IDependencyPropertyChangedEventArgs')
make_head(_module, 'IDependencyPropertyStatics')
make_head(_module, 'IDispatcherTimer')
make_head(_module, 'IDispatcherTimerFactory')
make_head(_module, 'IDragEventArgs')
make_head(_module, 'IDragEventArgs2')
make_head(_module, 'IDragEventArgs3')
make_head(_module, 'IDragOperationDeferral')
make_head(_module, 'IDragStartingEventArgs')
make_head(_module, 'IDragStartingEventArgs2')
make_head(_module, 'IDragUI')
make_head(_module, 'IDragUIOverride')
make_head(_module, 'IDropCompletedEventArgs')
make_head(_module, 'IDurationHelper')
make_head(_module, 'IDurationHelperStatics')
make_head(_module, 'IEffectiveViewportChangedEventArgs')
make_head(_module, 'IElementFactory')
make_head(_module, 'IElementFactoryGetArgs')
make_head(_module, 'IElementFactoryGetArgsFactory')
make_head(_module, 'IElementFactoryRecycleArgs')
make_head(_module, 'IElementFactoryRecycleArgsFactory')
make_head(_module, 'IElementSoundPlayer')
make_head(_module, 'IElementSoundPlayerStatics')
make_head(_module, 'IElementSoundPlayerStatics2')
make_head(_module, 'IEventTrigger')
make_head(_module, 'IExceptionRoutedEventArgs')
make_head(_module, 'IExceptionRoutedEventArgsFactory')
make_head(_module, 'IFrameworkElement')
make_head(_module, 'IFrameworkElement2')
make_head(_module, 'IFrameworkElement3')
make_head(_module, 'IFrameworkElement4')
make_head(_module, 'IFrameworkElement6')
make_head(_module, 'IFrameworkElement7')
make_head(_module, 'IFrameworkElementFactory')
make_head(_module, 'IFrameworkElementOverrides')
make_head(_module, 'IFrameworkElementOverrides2')
make_head(_module, 'IFrameworkElementProtected7')
make_head(_module, 'IFrameworkElementStatics')
make_head(_module, 'IFrameworkElementStatics2')
make_head(_module, 'IFrameworkElementStatics4')
make_head(_module, 'IFrameworkElementStatics5')
make_head(_module, 'IFrameworkElementStatics6')
make_head(_module, 'IFrameworkTemplate')
make_head(_module, 'IFrameworkTemplateFactory')
make_head(_module, 'IFrameworkView')
make_head(_module, 'IFrameworkViewSource')
make_head(_module, 'IGridLengthHelper')
make_head(_module, 'IGridLengthHelperStatics')
make_head(_module, 'IMediaFailedRoutedEventArgs')
make_head(_module, 'IPointHelper')
make_head(_module, 'IPointHelperStatics')
make_head(_module, 'IPropertyMetadata')
make_head(_module, 'IPropertyMetadataFactory')
make_head(_module, 'IPropertyMetadataStatics')
make_head(_module, 'IPropertyPath')
make_head(_module, 'IPropertyPathFactory')
make_head(_module, 'IRectHelper')
make_head(_module, 'IRectHelperStatics')
make_head(_module, 'IResourceDictionary')
make_head(_module, 'IResourceDictionaryFactory')
make_head(_module, 'IRoutedEvent')
make_head(_module, 'IRoutedEventArgs')
make_head(_module, 'IRoutedEventArgsFactory')
make_head(_module, 'IScalarTransition')
make_head(_module, 'IScalarTransitionFactory')
make_head(_module, 'ISetter')
make_head(_module, 'ISetter2')
make_head(_module, 'ISetterBase')
make_head(_module, 'ISetterBaseCollection')
make_head(_module, 'ISetterBaseFactory')
make_head(_module, 'ISetterFactory')
make_head(_module, 'ISizeChangedEventArgs')
make_head(_module, 'ISizeHelper')
make_head(_module, 'ISizeHelperStatics')
make_head(_module, 'IStateTrigger')
make_head(_module, 'IStateTriggerBase')
make_head(_module, 'IStateTriggerBaseFactory')
make_head(_module, 'IStateTriggerBaseProtected')
make_head(_module, 'IStateTriggerStatics')
make_head(_module, 'IStyle')
make_head(_module, 'IStyleFactory')
make_head(_module, 'ITargetPropertyPath')
make_head(_module, 'ITargetPropertyPathFactory')
make_head(_module, 'IThicknessHelper')
make_head(_module, 'IThicknessHelperStatics')
make_head(_module, 'ITriggerAction')
make_head(_module, 'ITriggerActionFactory')
make_head(_module, 'ITriggerBase')
make_head(_module, 'ITriggerBaseFactory')
make_head(_module, 'IUIElement')
make_head(_module, 'IUIElement10')
make_head(_module, 'IUIElement2')
make_head(_module, 'IUIElement3')
make_head(_module, 'IUIElement4')
make_head(_module, 'IUIElement5')
make_head(_module, 'IUIElement7')
make_head(_module, 'IUIElement8')
make_head(_module, 'IUIElement9')
make_head(_module, 'IUIElementFactory')
make_head(_module, 'IUIElementOverrides')
make_head(_module, 'IUIElementOverrides7')
make_head(_module, 'IUIElementOverrides8')
make_head(_module, 'IUIElementOverrides9')
make_head(_module, 'IUIElementStatics')
make_head(_module, 'IUIElementStatics10')
make_head(_module, 'IUIElementStatics2')
make_head(_module, 'IUIElementStatics3')
make_head(_module, 'IUIElementStatics4')
make_head(_module, 'IUIElementStatics5')
make_head(_module, 'IUIElementStatics6')
make_head(_module, 'IUIElementStatics7')
make_head(_module, 'IUIElementStatics8')
make_head(_module, 'IUIElementStatics9')
make_head(_module, 'IUIElementWeakCollection')
make_head(_module, 'IUIElementWeakCollectionFactory')
make_head(_module, 'IUnhandledExceptionEventArgs')
make_head(_module, 'IVector3Transition')
make_head(_module, 'IVector3TransitionFactory')
make_head(_module, 'IVisualState')
make_head(_module, 'IVisualState2')
make_head(_module, 'IVisualStateChangedEventArgs')
make_head(_module, 'IVisualStateGroup')
make_head(_module, 'IVisualStateManager')
make_head(_module, 'IVisualStateManagerFactory')
make_head(_module, 'IVisualStateManagerOverrides')
make_head(_module, 'IVisualStateManagerProtected')
make_head(_module, 'IVisualStateManagerStatics')
make_head(_module, 'IVisualTransition')
make_head(_module, 'IVisualTransitionFactory')
make_head(_module, 'IWindow')
make_head(_module, 'IWindow2')
make_head(_module, 'IWindow3')
make_head(_module, 'IWindow4')
make_head(_module, 'IWindowCreatedEventArgs')
make_head(_module, 'IWindowStatics')
make_head(_module, 'IXamlRoot')
make_head(_module, 'IXamlRootChangedEventArgs')
make_head(_module, 'LeavingBackgroundEventHandler')
make_head(_module, 'MediaFailedRoutedEventArgs')
make_head(_module, 'PointHelper')
make_head(_module, 'PropertyChangedCallback')
make_head(_module, 'PropertyMetadata')
make_head(_module, 'PropertyPath')
make_head(_module, 'RectHelper')
make_head(_module, 'ResourceDictionary')
make_head(_module, 'RoutedEvent')
make_head(_module, 'RoutedEventArgs')
make_head(_module, 'RoutedEventHandler')
make_head(_module, 'ScalarTransition')
make_head(_module, 'Setter')
make_head(_module, 'SetterBase')
make_head(_module, 'SetterBaseCollection')
make_head(_module, 'SizeChangedEventArgs')
make_head(_module, 'SizeChangedEventHandler')
make_head(_module, 'SizeHelper')
make_head(_module, 'StateTrigger')
make_head(_module, 'StateTriggerBase')
make_head(_module, 'Style')
make_head(_module, 'SuspendingEventHandler')
make_head(_module, 'TargetPropertyPath')
make_head(_module, 'Thickness')
make_head(_module, 'ThicknessHelper')
make_head(_module, 'TriggerAction')
make_head(_module, 'TriggerActionCollection')
make_head(_module, 'TriggerBase')
make_head(_module, 'TriggerCollection')
make_head(_module, 'UIElement')
make_head(_module, 'UIElementWeakCollection')
make_head(_module, 'UnhandledExceptionEventArgs')
make_head(_module, 'UnhandledExceptionEventHandler')
make_head(_module, 'Vector3Transition')
make_head(_module, 'VisualState')
make_head(_module, 'VisualStateChangedEventArgs')
make_head(_module, 'VisualStateChangedEventHandler')
make_head(_module, 'VisualStateGroup')
make_head(_module, 'VisualStateManager')
make_head(_module, 'VisualTransition')
make_head(_module, 'Window')
make_head(_module, 'WindowActivatedEventHandler')
make_head(_module, 'WindowClosedEventHandler')
make_head(_module, 'WindowCreatedEventArgs')
make_head(_module, 'WindowSizeChangedEventHandler')
make_head(_module, 'WindowVisibilityChangedEventHandler')
make_head(_module, 'XamlRoot')
make_head(_module, 'XamlRootChangedEventArgs')
