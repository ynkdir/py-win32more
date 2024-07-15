from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Input
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Automation.Peers
import win32more.Microsoft.UI.Xaml.Controls
import win32more.Microsoft.UI.Xaml.Controls.Primitives
import win32more.Microsoft.UI.Xaml.Data
import win32more.Microsoft.UI.Xaml.Input
import win32more.Microsoft.UI.Xaml.Media
import win32more.Microsoft.UI.Xaml.Media.Animation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.UI
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AnimationDirection(Enum, Int32):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
class AppBarButtonTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarButtonTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.AppBarButtonTemplateSettings'
    @winrt_mixinmethod
    def get_KeyboardAcceleratorTextMinWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarButtonTemplateSettings) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class AppBarTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.AppBarTemplateSettings'
    @winrt_mixinmethod
    def get_ClipRect(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CompactVerticalDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CompactRootMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_MinimalVerticalDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_MinimalRootMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_HiddenVerticalDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_HiddenRootMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_NegativeCompactVerticalDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeMinimalVerticalDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeHiddenVerticalDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    ClipRect = property(get_ClipRect, None)
    CompactRootMargin = property(get_CompactRootMargin, None)
    CompactVerticalDelta = property(get_CompactVerticalDelta, None)
    HiddenRootMargin = property(get_HiddenRootMargin, None)
    HiddenVerticalDelta = property(get_HiddenVerticalDelta, None)
    MinimalRootMargin = property(get_MinimalRootMargin, None)
    MinimalVerticalDelta = property(get_MinimalVerticalDelta, None)
    NegativeCompactVerticalDelta = property(get_NegativeCompactVerticalDelta, None)
    NegativeHiddenVerticalDelta = property(get_NegativeHiddenVerticalDelta, None)
    NegativeMinimalVerticalDelta = property(get_NegativeMinimalVerticalDelta, None)
class AppBarToggleButtonTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarToggleButtonTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.AppBarToggleButtonTemplateSettings'
    @winrt_mixinmethod
    def get_KeyboardAcceleratorTextMinWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAppBarToggleButtonTemplateSettings) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class _AutoSuggestBoxHelper_Meta_(ComPtr.__class__):
    pass
class AutoSuggestBoxHelper(ComPtr, metaclass=_AutoSuggestBoxHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAutoSuggestBoxHelper
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.AutoSuggestBoxHelper'
    @winrt_classmethod
    def get_KeepInteriorCornersSquareProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAutoSuggestBoxHelperStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def SetKeepInteriorCornersSquare(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAutoSuggestBoxHelperStatics, autoSuggestBox: win32more.Microsoft.UI.Xaml.Controls.AutoSuggestBox, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetKeepInteriorCornersSquare(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IAutoSuggestBoxHelperStatics, autoSuggestBox: win32more.Microsoft.UI.Xaml.Controls.AutoSuggestBox) -> Boolean: ...
    _AutoSuggestBoxHelper_Meta_.KeepInteriorCornersSquareProperty = property(get_KeepInteriorCornersSquareProperty, None)
class _ButtonBase_Meta_(ComPtr.__class__):
    pass
class ButtonBase(ComPtr, metaclass=_ButtonBase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ButtonBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ButtonBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ButtonBase: ...
    @winrt_mixinmethod
    def get_ClickMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase) -> win32more.Microsoft.UI.Xaml.Controls.ClickMode: ...
    @winrt_mixinmethod
    def put_ClickMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase, value: win32more.Microsoft.UI.Xaml.Controls.ClickMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsPointerOver(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPressed(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase) -> Boolean: ...
    @winrt_mixinmethod
    def get_Command(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase) -> win32more.Microsoft.UI.Xaml.Input.ICommand: ...
    @winrt_mixinmethod
    def put_Command(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase, value: win32more.Microsoft.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_mixinmethod
    def get_CommandParameter(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_CommandParameter(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def add_Click(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Click(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ClickModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsPointerOverProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsPressedProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CommandProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CommandParameterProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ClickMode = property(get_ClickMode, put_ClickMode)
    Command = property(get_Command, put_Command)
    CommandParameter = property(get_CommandParameter, put_CommandParameter)
    IsPointerOver = property(get_IsPointerOver, None)
    IsPressed = property(get_IsPressed, None)
    _ButtonBase_Meta_.ClickModeProperty = property(get_ClickModeProperty, None)
    _ButtonBase_Meta_.CommandParameterProperty = property(get_CommandParameterProperty, None)
    _ButtonBase_Meta_.CommandProperty = property(get_CommandProperty, None)
    _ButtonBase_Meta_.IsPointerOverProperty = property(get_IsPointerOverProperty, None)
    _ButtonBase_Meta_.IsPressedProperty = property(get_IsPressedProperty, None)
    Click = event()
class CalendarPanel(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Panel
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarPanel
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CalendarPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.CalendarPanel.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CalendarPanel: ...
class CalendarViewTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CalendarViewTemplateSettings'
    @winrt_mixinmethod
    def get_MinViewWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_HeaderText(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay1(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay2(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay3(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay4(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay5(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay6(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay7(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasMoreContentAfter(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasMoreContentBefore(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasMoreViews(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_ClipRect(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Double: ...
    CenterX = property(get_CenterX, None)
    CenterY = property(get_CenterY, None)
    ClipRect = property(get_ClipRect, None)
    HasMoreContentAfter = property(get_HasMoreContentAfter, None)
    HasMoreContentBefore = property(get_HasMoreContentBefore, None)
    HasMoreViews = property(get_HasMoreViews, None)
    HeaderText = property(get_HeaderText, None)
    MinViewWidth = property(get_MinViewWidth, None)
    WeekDay1 = property(get_WeekDay1, None)
    WeekDay2 = property(get_WeekDay2, None)
    WeekDay3 = property(get_WeekDay3, None)
    WeekDay4 = property(get_WeekDay4, None)
    WeekDay5 = property(get_WeekDay5, None)
    WeekDay6 = property(get_WeekDay6, None)
    WeekDay7 = property(get_WeekDay7, None)
class CarouselPanel(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.VirtualizingPanel
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CarouselPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.CarouselPanel.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanelFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CarouselPanel: ...
    @winrt_mixinmethod
    def get_CanVerticallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanVerticallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanHorizontallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanHorizontallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExtentWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ExtentHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollOwner(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_ScrollOwner(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def LineUp(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def LineDown(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def LineLeft(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def LineRight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageUp(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageDown(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageLeft(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageRight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelUp(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelDown(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelLeft(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelRight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def SetHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def SetVerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def MakeVisible(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel, visual: win32more.Microsoft.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    AreHorizontalSnapPointsRegular = property(get_AreHorizontalSnapPointsRegular, None)
    AreVerticalSnapPointsRegular = property(get_AreVerticalSnapPointsRegular, None)
    CanHorizontallyScroll = property(get_CanHorizontallyScroll, put_CanHorizontallyScroll)
    CanVerticallyScroll = property(get_CanVerticallyScroll, put_CanVerticallyScroll)
    ExtentHeight = property(get_ExtentHeight, None)
    ExtentWidth = property(get_ExtentWidth, None)
    HorizontalOffset = property(get_HorizontalOffset, None)
    ScrollOwner = property(get_ScrollOwner, put_ScrollOwner)
    VerticalOffset = property(get_VerticalOffset, None)
    ViewportHeight = property(get_ViewportHeight, None)
    ViewportWidth = property(get_ViewportWidth, None)
    HorizontalSnapPointsChanged = event()
    VerticalSnapPointsChanged = event()
class _ColorPickerSlider_Meta_(ComPtr.__class__):
    pass
class ColorPickerSlider(ComPtr, metaclass=_ColorPickerSlider_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Slider
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSlider
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ColorPickerSlider'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorPickerSlider.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSliderFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorPickerSlider: ...
    @winrt_mixinmethod
    def get_ColorChannel(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSlider) -> win32more.Microsoft.UI.Xaml.Controls.ColorPickerHsvChannel: ...
    @winrt_mixinmethod
    def put_ColorChannel(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSlider, value: win32more.Microsoft.UI.Xaml.Controls.ColorPickerHsvChannel) -> Void: ...
    @winrt_classmethod
    def get_ColorChannelProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSliderStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColorChannel = property(get_ColorChannel, put_ColorChannel)
    _ColorPickerSlider_Meta_.ColorChannelProperty = property(get_ColorChannelProperty, None)
class _ColorSpectrum_Meta_(ComPtr.__class__):
    pass
class ColorSpectrum(ComPtr, metaclass=_ColorSpectrum_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Control
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_HsvColor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Windows.Foundation.Numerics.Vector4: ...
    @winrt_mixinmethod
    def put_HsvColor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def get_MinHue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MinHue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxHue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxHue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinSaturation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MinSaturation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSaturation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxSaturation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MinValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumShape: ...
    @winrt_mixinmethod
    def put_Shape(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumShape) -> Void: ...
    @winrt_mixinmethod
    def get_Components(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumComponents: ...
    @winrt_mixinmethod
    def put_Components(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumComponents) -> Void: ...
    @winrt_mixinmethod
    def add_ColorChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum, win32more.Microsoft.UI.Xaml.Controls.ColorChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ColorChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HsvColorProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinHueProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxHueProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinSaturationProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxSaturationProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinValueProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxValueProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ShapeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ComponentsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Color = property(get_Color, put_Color)
    Components = property(get_Components, put_Components)
    HsvColor = property(get_HsvColor, put_HsvColor)
    MaxHue = property(get_MaxHue, put_MaxHue)
    MaxSaturation = property(get_MaxSaturation, put_MaxSaturation)
    MaxValue = property(get_MaxValue, put_MaxValue)
    MinHue = property(get_MinHue, put_MinHue)
    MinSaturation = property(get_MinSaturation, put_MinSaturation)
    MinValue = property(get_MinValue, put_MinValue)
    Shape = property(get_Shape, put_Shape)
    _ColorSpectrum_Meta_.ColorProperty = property(get_ColorProperty, None)
    _ColorSpectrum_Meta_.ComponentsProperty = property(get_ComponentsProperty, None)
    _ColorSpectrum_Meta_.HsvColorProperty = property(get_HsvColorProperty, None)
    _ColorSpectrum_Meta_.MaxHueProperty = property(get_MaxHueProperty, None)
    _ColorSpectrum_Meta_.MaxSaturationProperty = property(get_MaxSaturationProperty, None)
    _ColorSpectrum_Meta_.MaxValueProperty = property(get_MaxValueProperty, None)
    _ColorSpectrum_Meta_.MinHueProperty = property(get_MinHueProperty, None)
    _ColorSpectrum_Meta_.MinSaturationProperty = property(get_MinSaturationProperty, None)
    _ColorSpectrum_Meta_.MinValueProperty = property(get_MinValueProperty, None)
    _ColorSpectrum_Meta_.ShapeProperty = property(get_ShapeProperty, None)
    ColorChanged = event()
class _ColumnMajorUniformToLargestGridLayout_Meta_(ComPtr.__class__):
    pass
class ColumnMajorUniformToLargestGridLayout(ComPtr, metaclass=_ColumnMajorUniformToLargestGridLayout_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.NonVirtualizingLayout
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ColumnMajorUniformToLargestGridLayout'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ColumnMajorUniformToLargestGridLayout.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayoutFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ColumnMajorUniformToLargestGridLayout: ...
    @winrt_mixinmethod
    def get_MaxColumns(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxColumns(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ColumnSpacing(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout) -> Double: ...
    @winrt_mixinmethod
    def put_ColumnSpacing(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RowSpacing(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout) -> Double: ...
    @winrt_mixinmethod
    def put_RowSpacing(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout, value: Double) -> Void: ...
    @winrt_classmethod
    def get_MaxColumnsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayoutStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ColumnSpacingProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayoutStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RowSpacingProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayoutStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColumnSpacing = property(get_ColumnSpacing, put_ColumnSpacing)
    MaxColumns = property(get_MaxColumns, put_MaxColumns)
    RowSpacing = property(get_RowSpacing, put_RowSpacing)
    _ColumnMajorUniformToLargestGridLayout_Meta_.ColumnSpacingProperty = property(get_ColumnSpacingProperty, None)
    _ColumnMajorUniformToLargestGridLayout_Meta_.MaxColumnsProperty = property(get_MaxColumnsProperty, None)
    _ColumnMajorUniformToLargestGridLayout_Meta_.RowSpacingProperty = property(get_RowSpacingProperty, None)
class _ComboBoxHelper_Meta_(ComPtr.__class__):
    pass
class ComboBoxHelper(ComPtr, metaclass=_ComboBoxHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxHelper
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ComboBoxHelper'
    @winrt_classmethod
    def get_KeepInteriorCornersSquareProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxHelperStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def SetKeepInteriorCornersSquare(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxHelperStatics, comboBox: win32more.Microsoft.UI.Xaml.Controls.ComboBox, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetKeepInteriorCornersSquare(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxHelperStatics, comboBox: win32more.Microsoft.UI.Xaml.Controls.ComboBox) -> Boolean: ...
    _ComboBoxHelper_Meta_.KeepInteriorCornersSquareProperty = property(get_KeepInteriorCornersSquareProperty, None)
class ComboBoxTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ComboBoxTemplateSettings'
    @winrt_mixinmethod
    def get_DropDownOpenedHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_DropDownClosedHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_DropDownOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_SelectedItemDirection(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def get_DropDownContentMinWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> Double: ...
    DropDownClosedHeight = property(get_DropDownClosedHeight, None)
    DropDownContentMinWidth = property(get_DropDownContentMinWidth, None)
    DropDownOffset = property(get_DropDownOffset, None)
    DropDownOpenedHeight = property(get_DropDownOpenedHeight, None)
    SelectedItemDirection = property(get_SelectedItemDirection, None)
class _CommandBarFlyoutCommandBar_Meta_(ComPtr.__class__):
    pass
class CommandBarFlyoutCommandBar(ComPtr, metaclass=_CommandBarFlyoutCommandBar_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.CommandBar
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar: ...
    @winrt_mixinmethod
    def get_FlyoutTemplateSettings(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBarTemplateSettings: ...
    @winrt_mixinmethod
    def get_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar2) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_mixinmethod
    def put_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar2, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    @winrt_classmethod
    def get_SystemBackdropProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FlyoutTemplateSettings = property(get_FlyoutTemplateSettings, None)
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
    _CommandBarFlyoutCommandBar_Meta_.SystemBackdropProperty = property(get_SystemBackdropProperty, None)
class _CommandBarFlyoutCommandBarAutomationProperties_Meta_(ComPtr.__class__):
    pass
class CommandBarFlyoutCommandBarAutomationProperties(ComPtr, metaclass=_CommandBarFlyoutCommandBarAutomationProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBarAutomationProperties'
    @winrt_classmethod
    def get_ControlTypeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetControlType(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_classmethod
    def SetControlType(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.UIElement, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    _CommandBarFlyoutCommandBarAutomationProperties_Meta_.ControlTypeProperty = property(get_ControlTypeProperty, None)
class CommandBarFlyoutCommandBarTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBarTemplateSettings'
    @winrt_mixinmethod
    def get_OpenAnimationStartPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OpenAnimationEndPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CloseAnimationEndPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurrentWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandedWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionAnimationStartPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionAnimationEndPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionMoreButtonAnimationStartPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionMoreButtonAnimationEndPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpOverflowVerticalPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownOverflowVerticalPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpAnimationStartPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpAnimationEndPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpAnimationHoldPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownAnimationStartPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownAnimationEndPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownAnimationHoldPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ContentClipRect(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_OverflowContentClipRect(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    CloseAnimationEndPosition = property(get_CloseAnimationEndPosition, None)
    ContentClipRect = property(get_ContentClipRect, None)
    CurrentWidth = property(get_CurrentWidth, None)
    ExpandDownAnimationEndPosition = property(get_ExpandDownAnimationEndPosition, None)
    ExpandDownAnimationHoldPosition = property(get_ExpandDownAnimationHoldPosition, None)
    ExpandDownAnimationStartPosition = property(get_ExpandDownAnimationStartPosition, None)
    ExpandDownOverflowVerticalPosition = property(get_ExpandDownOverflowVerticalPosition, None)
    ExpandUpAnimationEndPosition = property(get_ExpandUpAnimationEndPosition, None)
    ExpandUpAnimationHoldPosition = property(get_ExpandUpAnimationHoldPosition, None)
    ExpandUpAnimationStartPosition = property(get_ExpandUpAnimationStartPosition, None)
    ExpandUpOverflowVerticalPosition = property(get_ExpandUpOverflowVerticalPosition, None)
    ExpandedWidth = property(get_ExpandedWidth, None)
    OpenAnimationEndPosition = property(get_OpenAnimationEndPosition, None)
    OpenAnimationStartPosition = property(get_OpenAnimationStartPosition, None)
    OverflowContentClipRect = property(get_OverflowContentClipRect, None)
    WidthExpansionAnimationEndPosition = property(get_WidthExpansionAnimationEndPosition, None)
    WidthExpansionAnimationStartPosition = property(get_WidthExpansionAnimationStartPosition, None)
    WidthExpansionDelta = property(get_WidthExpansionDelta, None)
    WidthExpansionMoreButtonAnimationEndPosition = property(get_WidthExpansionMoreButtonAnimationEndPosition, None)
    WidthExpansionMoreButtonAnimationStartPosition = property(get_WidthExpansionMoreButtonAnimationStartPosition, None)
class CommandBarTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CommandBarTemplateSettings'
    @winrt_mixinmethod
    def get_ContentHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentClipRect(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_OverflowContentMinWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentMaxWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentMaxHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeOverflowContentHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_EffectiveOverflowButtonVisibility(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> win32more.Microsoft.UI.Xaml.Visibility: ...
    @winrt_mixinmethod
    def get_OverflowContentCompactYTranslation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentMinimalYTranslation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentHiddenYTranslation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    ContentHeight = property(get_ContentHeight, None)
    EffectiveOverflowButtonVisibility = property(get_EffectiveOverflowButtonVisibility, None)
    NegativeOverflowContentHeight = property(get_NegativeOverflowContentHeight, None)
    OverflowContentClipRect = property(get_OverflowContentClipRect, None)
    OverflowContentCompactYTranslation = property(get_OverflowContentCompactYTranslation, None)
    OverflowContentHeight = property(get_OverflowContentHeight, None)
    OverflowContentHiddenYTranslation = property(get_OverflowContentHiddenYTranslation, None)
    OverflowContentHorizontalOffset = property(get_OverflowContentHorizontalOffset, None)
    OverflowContentMaxHeight = property(get_OverflowContentMaxHeight, None)
    OverflowContentMaxWidth = property(get_OverflowContentMaxWidth, None)
    OverflowContentMinWidth = property(get_OverflowContentMinWidth, None)
    OverflowContentMinimalYTranslation = property(get_OverflowContentMinimalYTranslation, None)
class ComponentResourceLocation(Enum, Int32):
    Application = 0
    Nested = 1
class _CornerRadiusFilterConverter_Meta_(ComPtr.__class__):
    pass
class CornerRadiusFilterConverter(ComPtr, metaclass=_CornerRadiusFilterConverter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterConverter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterConverter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterConverter: ...
    @winrt_mixinmethod
    def get_Filter(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverter) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterKind: ...
    @winrt_mixinmethod
    def put_Filter(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverter, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterKind) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverter) -> Double: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def Convert(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def ConvertBack(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_FilterProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Filter = property(get_Filter, put_Filter)
    Scale = property(get_Scale, put_Scale)
    _CornerRadiusFilterConverter_Meta_.FilterProperty = property(get_FilterProperty, None)
    _CornerRadiusFilterConverter_Meta_.ScaleProperty = property(get_ScaleProperty, None)
class CornerRadiusFilterKind(Enum, Int32):
    None_ = 0
    Top = 1
    Right = 2
    Bottom = 3
    Left = 4
    TopLeftValue = 5
    BottomRightValue = 6
class _CornerRadiusToThicknessConverter_Meta_(ComPtr.__class__):
    pass
class CornerRadiusToThicknessConverter(ComPtr, metaclass=_CornerRadiusToThicknessConverter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverter: ...
    @winrt_mixinmethod
    def get_ConversionKind(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverter) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverterKind: ...
    @winrt_mixinmethod
    def put_ConversionKind(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverter, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverterKind) -> Void: ...
    @winrt_mixinmethod
    def get_Multiplier(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverter) -> Double: ...
    @winrt_mixinmethod
    def put_Multiplier(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def Convert(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def ConvertBack(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_ConversionKindProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MultiplierProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ConversionKind = property(get_ConversionKind, put_ConversionKind)
    Multiplier = property(get_Multiplier, put_Multiplier)
    _CornerRadiusToThicknessConverter_Meta_.ConversionKindProperty = property(get_ConversionKindProperty, None)
    _CornerRadiusToThicknessConverter_Meta_.MultiplierProperty = property(get_MultiplierProperty, None)
class CornerRadiusToThicknessConverterKind(Enum, Int32):
    FilterTopAndBottomFromLeft = 0
    FilterTopAndBottomFromRight = 1
    FilterLeftAndRightFromTop = 2
    FilterLeftAndRightFromBottom = 3
    FilterTopFromTopLeft = 4
    FilterTopFromTopRight = 5
    FilterRightFromTopRight = 6
    FilterRightFromBottomRight = 7
    FilterBottomFromBottomRight = 8
    FilterBottomFromBottomLeft = 9
    FilterLeftFromBottomLeft = 10
    FilterLeftFromTopLeft = 11
class DragCompletedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.DragCompletedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.DragCompletedEventArgs.CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragCompletedEventArgsFactory, horizontalChange: Double, verticalChange: Double, canceled: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.DragCompletedEventArgs: ...
    @winrt_mixinmethod
    def get_HorizontalChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_Canceled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs) -> Boolean: ...
    Canceled = property(get_Canceled, None)
    HorizontalChange = property(get_HorizontalChange, None)
    VerticalChange = property(get_VerticalChange, None)
class DragCompletedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a27012cb-923f-5992-ade2-878f7c794ef5}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragCompletedEventArgs) -> Void: ...
class DragDeltaEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.DragDeltaEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.DragDeltaEventArgs.CreateInstanceWithHorizontalChangeAndVerticalChange(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithHorizontalChangeAndVerticalChange(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragDeltaEventArgsFactory, horizontalChange: Double, verticalChange: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.DragDeltaEventArgs: ...
    @winrt_mixinmethod
    def get_HorizontalChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs) -> Double: ...
    HorizontalChange = property(get_HorizontalChange, None)
    VerticalChange = property(get_VerticalChange, None)
class DragDeltaEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{49ca91d0-fc43-56b1-98bd-68e2e1e24de9}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragDeltaEventArgs) -> Void: ...
class DragStartedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragStartedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.DragStartedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.DragStartedEventArgs.CreateInstanceWithHorizontalOffsetAndVerticalOffset(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithHorizontalOffsetAndVerticalOffset(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragStartedEventArgsFactory, horizontalOffset: Double, verticalOffset: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.DragStartedEventArgs: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragStartedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IDragStartedEventArgs) -> Double: ...
    HorizontalOffset = property(get_HorizontalOffset, None)
    VerticalOffset = property(get_VerticalOffset, None)
class DragStartedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{13191f6d-a651-5870-b3a1-221550003512}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragStartedEventArgs) -> Void: ...
class EdgeTransitionLocation(Enum, Int32):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
class _FlyoutBase_Meta_(ComPtr.__class__):
    pass
class FlyoutBase(ComPtr, metaclass=_FlyoutBase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_mixinmethod
    def get_Placement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_mixinmethod
    def put_Placement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Microsoft.UI.Xaml.FrameworkElement: ...
    @winrt_mixinmethod
    def get_AllowFocusOnInteraction(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusOnInteraction(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LightDismissOverlayMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_mixinmethod
    def put_LightDismissOverlayMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    @winrt_mixinmethod
    def get_AllowFocusWhenDisabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusWhenDisabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_mixinmethod
    def put_ShowMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevicePrefersPrimaryCommands(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreOpenCloseAnimationsEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreOpenCloseAnimationsEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldConstrainToRootBounds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldConstrainToRootBounds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsConstrainedToRootBounds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Boolean: ...
    @winrt_mixinmethod
    def get_ElementSoundMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Microsoft.UI.Xaml.ElementSoundMode: ...
    @winrt_mixinmethod
    def put_ElementSoundMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: win32more.Microsoft.UI.Xaml.ElementSoundMode) -> Void: ...
    @winrt_mixinmethod
    def get_OverlayInputPassThroughElement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OverlayInputPassThroughElement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def get_IsOpen(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Boolean: ...
    @winrt_mixinmethod
    def get_XamlRoot(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Microsoft.UI.Xaml.XamlRoot: ...
    @winrt_mixinmethod
    def put_XamlRoot(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, value: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_mixinmethod
    def add_Opened(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Opening(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opening(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closing(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase, win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBaseClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closing(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ShowAt(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, placementTarget: win32more.Microsoft.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_mixinmethod
    def ShowAtWithOptions(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, placementTarget: win32more.Microsoft.UI.Xaml.DependencyObject, showOptions: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowOptions) -> Void: ...
    @winrt_mixinmethod
    def Hide(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Void: ...
    @winrt_mixinmethod
    def TryInvokeKeyboardAccelerator(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase, args: win32more.Microsoft.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_mixinmethod
    def get_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase2) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_mixinmethod
    def put_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase2, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    @winrt_mixinmethod
    def CreatePresenter(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides) -> win32more.Microsoft.UI.Xaml.Controls.Control: ...
    @winrt_mixinmethod
    def OnProcessKeyboardAccelerators(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides, args: win32more.Microsoft.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_classmethod
    def get_SystemBackdropProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TargetProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PlacementProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowFocusOnInteractionProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LightDismissOverlayModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowFocusWhenDisabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ShowModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_InputDevicePrefersPrimaryCommandsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AreOpenCloseAnimationsEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ShouldConstrainToRootBoundsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ElementSoundModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OverlayInputPassThroughElementProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsOpenProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AttachedFlyoutProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAttachedFlyout(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics, element: win32more.Microsoft.UI.Xaml.FrameworkElement) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_classmethod
    def SetAttachedFlyout(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics, element: win32more.Microsoft.UI.Xaml.FrameworkElement, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_classmethod
    def ShowAttachedFlyout(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics, flyoutOwner: win32more.Microsoft.UI.Xaml.FrameworkElement) -> Void: ...
    AllowFocusOnInteraction = property(get_AllowFocusOnInteraction, put_AllowFocusOnInteraction)
    AllowFocusWhenDisabled = property(get_AllowFocusWhenDisabled, put_AllowFocusWhenDisabled)
    AreOpenCloseAnimationsEnabled = property(get_AreOpenCloseAnimationsEnabled, put_AreOpenCloseAnimationsEnabled)
    ElementSoundMode = property(get_ElementSoundMode, put_ElementSoundMode)
    InputDevicePrefersPrimaryCommands = property(get_InputDevicePrefersPrimaryCommands, None)
    IsConstrainedToRootBounds = property(get_IsConstrainedToRootBounds, None)
    IsOpen = property(get_IsOpen, None)
    LightDismissOverlayMode = property(get_LightDismissOverlayMode, put_LightDismissOverlayMode)
    OverlayInputPassThroughElement = property(get_OverlayInputPassThroughElement, put_OverlayInputPassThroughElement)
    Placement = property(get_Placement, put_Placement)
    ShouldConstrainToRootBounds = property(get_ShouldConstrainToRootBounds, put_ShouldConstrainToRootBounds)
    ShowMode = property(get_ShowMode, put_ShowMode)
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
    Target = property(get_Target, None)
    XamlRoot = property(get_XamlRoot, put_XamlRoot)
    _FlyoutBase_Meta_.AllowFocusOnInteractionProperty = property(get_AllowFocusOnInteractionProperty, None)
    _FlyoutBase_Meta_.AllowFocusWhenDisabledProperty = property(get_AllowFocusWhenDisabledProperty, None)
    _FlyoutBase_Meta_.AreOpenCloseAnimationsEnabledProperty = property(get_AreOpenCloseAnimationsEnabledProperty, None)
    _FlyoutBase_Meta_.AttachedFlyoutProperty = property(get_AttachedFlyoutProperty, None)
    _FlyoutBase_Meta_.ElementSoundModeProperty = property(get_ElementSoundModeProperty, None)
    _FlyoutBase_Meta_.InputDevicePrefersPrimaryCommandsProperty = property(get_InputDevicePrefersPrimaryCommandsProperty, None)
    _FlyoutBase_Meta_.IsOpenProperty = property(get_IsOpenProperty, None)
    _FlyoutBase_Meta_.LightDismissOverlayModeProperty = property(get_LightDismissOverlayModeProperty, None)
    _FlyoutBase_Meta_.OverlayInputPassThroughElementProperty = property(get_OverlayInputPassThroughElementProperty, None)
    _FlyoutBase_Meta_.PlacementProperty = property(get_PlacementProperty, None)
    _FlyoutBase_Meta_.ShouldConstrainToRootBoundsProperty = property(get_ShouldConstrainToRootBoundsProperty, None)
    _FlyoutBase_Meta_.ShowModeProperty = property(get_ShowModeProperty, None)
    _FlyoutBase_Meta_.SystemBackdropProperty = property(get_SystemBackdropProperty, None)
    _FlyoutBase_Meta_.TargetProperty = property(get_TargetProperty, None)
    Opened = event()
    Closed = event()
    Opening = event()
    Closing = event()
class FlyoutBaseClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.FlyoutBaseClosingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs, value: Boolean) -> Void: ...
    Cancel = property(get_Cancel, put_Cancel)
class FlyoutPlacementMode(Enum, Int32):
    Top = 0
    Bottom = 1
    Left = 2
    Right = 3
    Full = 4
    TopEdgeAlignedLeft = 5
    TopEdgeAlignedRight = 6
    BottomEdgeAlignedLeft = 7
    BottomEdgeAlignedRight = 8
    LeftEdgeAlignedTop = 9
    LeftEdgeAlignedBottom = 10
    RightEdgeAlignedTop = 11
    RightEdgeAlignedBottom = 12
    Auto = 13
class FlyoutShowMode(Enum, Int32):
    Auto = 0
    Standard = 1
    Transient = 2
    TransientWithDismissOnPointerMoveAway = 3
class FlyoutShowOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowOptions.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptionsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowOptions: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_ExclusionRect(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_ExclusionRect(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    @winrt_mixinmethod
    def get_ShowMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_mixinmethod
    def put_ShowMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_mixinmethod
    def get_Placement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_mixinmethod
    def put_Placement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    Placement = property(get_Placement, put_Placement)
    Position = property(get_Position, put_Position)
    ShowMode = property(get_ShowMode, put_ShowMode)
class GeneratorDirection(Enum, Int32):
    Forward = 0
    Backward = 1
class GeneratorPosition(Structure):
    Index: Int32
    Offset: Int32
class GeneratorPositionHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGeneratorPositionHelper
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.GeneratorPositionHelper'
    @winrt_classmethod
    def FromIndexAndOffset(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGeneratorPositionHelperStatics, index: Int32, offset: Int32) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
class _GridViewItemPresenter_Meta_(ComPtr.__class__):
    pass
class GridViewItemPresenter(ComPtr, metaclass=_GridViewItemPresenter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.ContentPresenter
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.GridViewItemPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.GridViewItemPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GridViewItemPresenter: ...
    @winrt_mixinmethod
    def get_SelectionCheckMarkVisualEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SelectionCheckMarkVisualEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CheckHintBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckHintBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckSelectingBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckSelectingBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PlaceholderBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBorderThickness(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_SelectedBorderThickness(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_DisabledOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DisabledOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DragOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DragOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReorderHintOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_ReorderHintOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GridViewItemPresenterHorizontalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.HorizontalAlignment: ...
    @winrt_mixinmethod
    def put_GridViewItemPresenterHorizontalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_GridViewItemPresenterVerticalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.VerticalAlignment: ...
    @winrt_mixinmethod
    def put_GridViewItemPresenterVerticalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_GridViewItemPresenterPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_GridViewItemPresenterPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackgroundMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_PointerOverBackgroundMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_ContentMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ContentMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_classmethod
    def get_SelectionCheckMarkVisualEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckHintBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckSelectingBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragForegroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PlaceholderBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedForegroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBorderThicknessProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledOpacityProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragOpacityProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ReorderHintOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GridViewItemPresenterHorizontalContentAlignmentProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GridViewItemPresenterVerticalContentAlignmentProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GridViewItemPresenterPaddingProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundMarginProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentMarginProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CheckBrush = property(get_CheckBrush, put_CheckBrush)
    CheckHintBrush = property(get_CheckHintBrush, put_CheckHintBrush)
    CheckSelectingBrush = property(get_CheckSelectingBrush, put_CheckSelectingBrush)
    ContentMargin = property(get_ContentMargin, put_ContentMargin)
    DisabledOpacity = property(get_DisabledOpacity, put_DisabledOpacity)
    DragBackground = property(get_DragBackground, put_DragBackground)
    DragForeground = property(get_DragForeground, put_DragForeground)
    DragOpacity = property(get_DragOpacity, put_DragOpacity)
    FocusBorderBrush = property(get_FocusBorderBrush, put_FocusBorderBrush)
    GridViewItemPresenterHorizontalContentAlignment = property(get_GridViewItemPresenterHorizontalContentAlignment, put_GridViewItemPresenterHorizontalContentAlignment)
    GridViewItemPresenterPadding = property(get_GridViewItemPresenterPadding, put_GridViewItemPresenterPadding)
    GridViewItemPresenterVerticalContentAlignment = property(get_GridViewItemPresenterVerticalContentAlignment, put_GridViewItemPresenterVerticalContentAlignment)
    PlaceholderBackground = property(get_PlaceholderBackground, put_PlaceholderBackground)
    PointerOverBackground = property(get_PointerOverBackground, put_PointerOverBackground)
    PointerOverBackgroundMargin = property(get_PointerOverBackgroundMargin, put_PointerOverBackgroundMargin)
    ReorderHintOffset = property(get_ReorderHintOffset, put_ReorderHintOffset)
    SelectedBackground = property(get_SelectedBackground, put_SelectedBackground)
    SelectedBorderThickness = property(get_SelectedBorderThickness, put_SelectedBorderThickness)
    SelectedForeground = property(get_SelectedForeground, put_SelectedForeground)
    SelectedPointerOverBackground = property(get_SelectedPointerOverBackground, put_SelectedPointerOverBackground)
    SelectedPointerOverBorderBrush = property(get_SelectedPointerOverBorderBrush, put_SelectedPointerOverBorderBrush)
    SelectionCheckMarkVisualEnabled = property(get_SelectionCheckMarkVisualEnabled, put_SelectionCheckMarkVisualEnabled)
    _GridViewItemPresenter_Meta_.CheckBrushProperty = property(get_CheckBrushProperty, None)
    _GridViewItemPresenter_Meta_.CheckHintBrushProperty = property(get_CheckHintBrushProperty, None)
    _GridViewItemPresenter_Meta_.CheckSelectingBrushProperty = property(get_CheckSelectingBrushProperty, None)
    _GridViewItemPresenter_Meta_.ContentMarginProperty = property(get_ContentMarginProperty, None)
    _GridViewItemPresenter_Meta_.DisabledOpacityProperty = property(get_DisabledOpacityProperty, None)
    _GridViewItemPresenter_Meta_.DragBackgroundProperty = property(get_DragBackgroundProperty, None)
    _GridViewItemPresenter_Meta_.DragForegroundProperty = property(get_DragForegroundProperty, None)
    _GridViewItemPresenter_Meta_.DragOpacityProperty = property(get_DragOpacityProperty, None)
    _GridViewItemPresenter_Meta_.FocusBorderBrushProperty = property(get_FocusBorderBrushProperty, None)
    _GridViewItemPresenter_Meta_.GridViewItemPresenterHorizontalContentAlignmentProperty = property(get_GridViewItemPresenterHorizontalContentAlignmentProperty, None)
    _GridViewItemPresenter_Meta_.GridViewItemPresenterPaddingProperty = property(get_GridViewItemPresenterPaddingProperty, None)
    _GridViewItemPresenter_Meta_.GridViewItemPresenterVerticalContentAlignmentProperty = property(get_GridViewItemPresenterVerticalContentAlignmentProperty, None)
    _GridViewItemPresenter_Meta_.PlaceholderBackgroundProperty = property(get_PlaceholderBackgroundProperty, None)
    _GridViewItemPresenter_Meta_.PointerOverBackgroundMarginProperty = property(get_PointerOverBackgroundMarginProperty, None)
    _GridViewItemPresenter_Meta_.PointerOverBackgroundProperty = property(get_PointerOverBackgroundProperty, None)
    _GridViewItemPresenter_Meta_.ReorderHintOffsetProperty = property(get_ReorderHintOffsetProperty, None)
    _GridViewItemPresenter_Meta_.SelectedBackgroundProperty = property(get_SelectedBackgroundProperty, None)
    _GridViewItemPresenter_Meta_.SelectedBorderThicknessProperty = property(get_SelectedBorderThicknessProperty, None)
    _GridViewItemPresenter_Meta_.SelectedForegroundProperty = property(get_SelectedForegroundProperty, None)
    _GridViewItemPresenter_Meta_.SelectedPointerOverBackgroundProperty = property(get_SelectedPointerOverBackgroundProperty, None)
    _GridViewItemPresenter_Meta_.SelectedPointerOverBorderBrushProperty = property(get_SelectedPointerOverBorderBrushProperty, None)
    _GridViewItemPresenter_Meta_.SelectionCheckMarkVisualEnabledProperty = property(get_SelectionCheckMarkVisualEnabledProperty, None)
class GridViewItemTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.GridViewItemTemplateSettings'
    @winrt_mixinmethod
    def get_DragItemsCount(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemTemplateSettings) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class GroupHeaderPlacement(Enum, Int32):
    Top = 0
    Left = 1
class IAppBarButtonTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IAppBarButtonTemplateSettings'
    _iid_ = Guid('{6fc13525-bf03-5190-a1d5-ebd6a1bcb6b4}')
    @winrt_commethod(6)
    def get_KeyboardAcceleratorTextMinWidth(self) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class IAppBarTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings'
    _iid_ = Guid('{fe60e73f-9a52-5e0a-b738-426f97d09768}')
    @winrt_commethod(6)
    def get_ClipRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_CompactVerticalDelta(self) -> Double: ...
    @winrt_commethod(8)
    def get_CompactRootMargin(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(9)
    def get_MinimalVerticalDelta(self) -> Double: ...
    @winrt_commethod(10)
    def get_MinimalRootMargin(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(11)
    def get_HiddenVerticalDelta(self) -> Double: ...
    @winrt_commethod(12)
    def get_HiddenRootMargin(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(13)
    def get_NegativeCompactVerticalDelta(self) -> Double: ...
    @winrt_commethod(14)
    def get_NegativeMinimalVerticalDelta(self) -> Double: ...
    @winrt_commethod(15)
    def get_NegativeHiddenVerticalDelta(self) -> Double: ...
    ClipRect = property(get_ClipRect, None)
    CompactRootMargin = property(get_CompactRootMargin, None)
    CompactVerticalDelta = property(get_CompactVerticalDelta, None)
    HiddenRootMargin = property(get_HiddenRootMargin, None)
    HiddenVerticalDelta = property(get_HiddenVerticalDelta, None)
    MinimalRootMargin = property(get_MinimalRootMargin, None)
    MinimalVerticalDelta = property(get_MinimalVerticalDelta, None)
    NegativeCompactVerticalDelta = property(get_NegativeCompactVerticalDelta, None)
    NegativeHiddenVerticalDelta = property(get_NegativeHiddenVerticalDelta, None)
    NegativeMinimalVerticalDelta = property(get_NegativeMinimalVerticalDelta, None)
class IAppBarToggleButtonTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IAppBarToggleButtonTemplateSettings'
    _iid_ = Guid('{32aa9f11-2f5e-57ab-a570-b03bceee835d}')
    @winrt_commethod(6)
    def get_KeyboardAcceleratorTextMinWidth(self) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class IAutoSuggestBoxHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IAutoSuggestBoxHelper'
    _iid_ = Guid('{1e56736c-8248-57d9-ac04-e4e7dcc3f9e1}')
class IAutoSuggestBoxHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IAutoSuggestBoxHelperStatics'
    _iid_ = Guid('{a8c05752-b160-5710-a009-2ad0fc4ed111}')
    @winrt_commethod(6)
    def get_KeepInteriorCornersSquareProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def SetKeepInteriorCornersSquare(self, autoSuggestBox: win32more.Microsoft.UI.Xaml.Controls.AutoSuggestBox, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetKeepInteriorCornersSquare(self, autoSuggestBox: win32more.Microsoft.UI.Xaml.Controls.AutoSuggestBox) -> Boolean: ...
    KeepInteriorCornersSquareProperty = property(get_KeepInteriorCornersSquareProperty, None)
class IButtonBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IButtonBase'
    _iid_ = Guid('{65714269-2473-5327-a652-0ea6bce7f403}')
    @winrt_commethod(6)
    def get_ClickMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ClickMode: ...
    @winrt_commethod(7)
    def put_ClickMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ClickMode) -> Void: ...
    @winrt_commethod(8)
    def get_IsPointerOver(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsPressed(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Command(self) -> win32more.Microsoft.UI.Xaml.Input.ICommand: ...
    @winrt_commethod(11)
    def put_Command(self, value: win32more.Microsoft.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_commethod(12)
    def get_CommandParameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(13)
    def put_CommandParameter(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(14)
    def add_Click(self, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Click(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ClickMode = property(get_ClickMode, put_ClickMode)
    Command = property(get_Command, put_Command)
    CommandParameter = property(get_CommandParameter, put_CommandParameter)
    IsPointerOver = property(get_IsPointerOver, None)
    IsPressed = property(get_IsPressed, None)
    Click = event()
class IButtonBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseFactory'
    _iid_ = Guid('{21251aa9-6fd1-5e51-ab3b-e6fcaf3395ed}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ButtonBase: ...
class IButtonBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IButtonBaseStatics'
    _iid_ = Guid('{dbe812f6-adf8-51d3-8137-a8fbf6445b3c}')
    @winrt_commethod(6)
    def get_ClickModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsPointerOverProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsPressedProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CommandProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_CommandParameterProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ClickModeProperty = property(get_ClickModeProperty, None)
    CommandParameterProperty = property(get_CommandParameterProperty, None)
    CommandProperty = property(get_CommandProperty, None)
    IsPointerOverProperty = property(get_IsPointerOverProperty, None)
    IsPressedProperty = property(get_IsPressedProperty, None)
class ICalendarPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICalendarPanel'
    _iid_ = Guid('{a4b26c3a-3825-5da4-a9e0-dd9b1e405e53}')
class ICalendarViewTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings'
    _iid_ = Guid('{23b0facb-0083-5109-87d3-dbeb13e331a0}')
    @winrt_commethod(6)
    def get_MinViewWidth(self) -> Double: ...
    @winrt_commethod(7)
    def get_HeaderText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_WeekDay1(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_WeekDay2(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_WeekDay3(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_WeekDay4(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_WeekDay5(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_WeekDay6(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_WeekDay7(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_HasMoreContentAfter(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_HasMoreContentBefore(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_HasMoreViews(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_ClipRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(19)
    def get_CenterX(self) -> Double: ...
    @winrt_commethod(20)
    def get_CenterY(self) -> Double: ...
    CenterX = property(get_CenterX, None)
    CenterY = property(get_CenterY, None)
    ClipRect = property(get_ClipRect, None)
    HasMoreContentAfter = property(get_HasMoreContentAfter, None)
    HasMoreContentBefore = property(get_HasMoreContentBefore, None)
    HasMoreViews = property(get_HasMoreViews, None)
    HeaderText = property(get_HeaderText, None)
    MinViewWidth = property(get_MinViewWidth, None)
    WeekDay1 = property(get_WeekDay1, None)
    WeekDay2 = property(get_WeekDay2, None)
    WeekDay3 = property(get_WeekDay3, None)
    WeekDay4 = property(get_WeekDay4, None)
    WeekDay5 = property(get_WeekDay5, None)
    WeekDay6 = property(get_WeekDay6, None)
    WeekDay7 = property(get_WeekDay7, None)
class ICarouselPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanel'
    _iid_ = Guid('{298d3800-e5c9-5003-b84c-a6538866e2d5}')
    @winrt_commethod(6)
    def get_CanVerticallyScroll(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanVerticallyScroll(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CanHorizontallyScroll(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CanHorizontallyScroll(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ExtentWidth(self) -> Double: ...
    @winrt_commethod(11)
    def get_ExtentHeight(self) -> Double: ...
    @winrt_commethod(12)
    def get_ViewportWidth(self) -> Double: ...
    @winrt_commethod(13)
    def get_ViewportHeight(self) -> Double: ...
    @winrt_commethod(14)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(15)
    def get_VerticalOffset(self) -> Double: ...
    @winrt_commethod(16)
    def get_ScrollOwner(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(17)
    def put_ScrollOwner(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(18)
    def LineUp(self) -> Void: ...
    @winrt_commethod(19)
    def LineDown(self) -> Void: ...
    @winrt_commethod(20)
    def LineLeft(self) -> Void: ...
    @winrt_commethod(21)
    def LineRight(self) -> Void: ...
    @winrt_commethod(22)
    def PageUp(self) -> Void: ...
    @winrt_commethod(23)
    def PageDown(self) -> Void: ...
    @winrt_commethod(24)
    def PageLeft(self) -> Void: ...
    @winrt_commethod(25)
    def PageRight(self) -> Void: ...
    @winrt_commethod(26)
    def MouseWheelUp(self) -> Void: ...
    @winrt_commethod(27)
    def MouseWheelDown(self) -> Void: ...
    @winrt_commethod(28)
    def MouseWheelLeft(self) -> Void: ...
    @winrt_commethod(29)
    def MouseWheelRight(self) -> Void: ...
    @winrt_commethod(30)
    def SetHorizontalOffset(self, offset: Double) -> Void: ...
    @winrt_commethod(31)
    def SetVerticalOffset(self, offset: Double) -> Void: ...
    @winrt_commethod(32)
    def MakeVisible(self, visual: win32more.Microsoft.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    CanHorizontallyScroll = property(get_CanHorizontallyScroll, put_CanHorizontallyScroll)
    CanVerticallyScroll = property(get_CanVerticallyScroll, put_CanVerticallyScroll)
    ExtentHeight = property(get_ExtentHeight, None)
    ExtentWidth = property(get_ExtentWidth, None)
    HorizontalOffset = property(get_HorizontalOffset, None)
    ScrollOwner = property(get_ScrollOwner, put_ScrollOwner)
    VerticalOffset = property(get_VerticalOffset, None)
    ViewportHeight = property(get_ViewportHeight, None)
    ViewportWidth = property(get_ViewportWidth, None)
class ICarouselPanelFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICarouselPanelFactory'
    _iid_ = Guid('{161d3fc2-d1ec-5d1d-ac8a-cf4577f06c3c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CarouselPanel: ...
class IColorPickerSlider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSlider'
    _iid_ = Guid('{456231bb-5a4c-564b-9b3d-2f157061a0f8}')
    @winrt_commethod(6)
    def get_ColorChannel(self) -> win32more.Microsoft.UI.Xaml.Controls.ColorPickerHsvChannel: ...
    @winrt_commethod(7)
    def put_ColorChannel(self, value: win32more.Microsoft.UI.Xaml.Controls.ColorPickerHsvChannel) -> Void: ...
    ColorChannel = property(get_ColorChannel, put_ColorChannel)
class IColorPickerSliderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSliderFactory'
    _iid_ = Guid('{d0cb1f0e-0771-5c7d-ba14-aa431179b2ac}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorPickerSlider: ...
class IColorPickerSliderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColorPickerSliderStatics'
    _iid_ = Guid('{82f72b75-e986-587f-9701-8ac6801da932}')
    @winrt_commethod(6)
    def get_ColorChannelProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColorChannelProperty = property(get_ColorChannelProperty, None)
class IColorSpectrum(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrum'
    _iid_ = Guid('{75305916-882d-5667-bfd0-0af72d502d72}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_HsvColor(self) -> win32more.Windows.Foundation.Numerics.Vector4: ...
    @winrt_commethod(9)
    def put_HsvColor(self, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(10)
    def get_MinHue(self) -> Int32: ...
    @winrt_commethod(11)
    def put_MinHue(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_MaxHue(self) -> Int32: ...
    @winrt_commethod(13)
    def put_MaxHue(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_MinSaturation(self) -> Int32: ...
    @winrt_commethod(15)
    def put_MinSaturation(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def get_MaxSaturation(self) -> Int32: ...
    @winrt_commethod(17)
    def put_MaxSaturation(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_MinValue(self) -> Int32: ...
    @winrt_commethod(19)
    def put_MinValue(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_MaxValue(self) -> Int32: ...
    @winrt_commethod(21)
    def put_MaxValue(self, value: Int32) -> Void: ...
    @winrt_commethod(22)
    def get_Shape(self) -> win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumShape: ...
    @winrt_commethod(23)
    def put_Shape(self, value: win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumShape) -> Void: ...
    @winrt_commethod(24)
    def get_Components(self) -> win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumComponents: ...
    @winrt_commethod(25)
    def put_Components(self, value: win32more.Microsoft.UI.Xaml.Controls.ColorSpectrumComponents) -> Void: ...
    @winrt_commethod(26)
    def add_ColorChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum, win32more.Microsoft.UI.Xaml.Controls.ColorChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_ColorChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Color = property(get_Color, put_Color)
    Components = property(get_Components, put_Components)
    HsvColor = property(get_HsvColor, put_HsvColor)
    MaxHue = property(get_MaxHue, put_MaxHue)
    MaxSaturation = property(get_MaxSaturation, put_MaxSaturation)
    MaxValue = property(get_MaxValue, put_MaxValue)
    MinHue = property(get_MinHue, put_MinHue)
    MinSaturation = property(get_MinSaturation, put_MinSaturation)
    MinValue = property(get_MinValue, put_MinValue)
    Shape = property(get_Shape, put_Shape)
    ColorChanged = event()
class IColorSpectrumFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumFactory'
    _iid_ = Guid('{efecd442-8c2a-50a6-88a3-3999ea01f096}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum: ...
class IColorSpectrumStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColorSpectrumStatics'
    _iid_ = Guid('{a2b43dba-1616-527d-9d32-039573b7fce7}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_HsvColorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_MinHueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_MaxHueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_MinSaturationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_MaxSaturationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_MinValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_MaxValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ShapeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ComponentsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColorProperty = property(get_ColorProperty, None)
    ComponentsProperty = property(get_ComponentsProperty, None)
    HsvColorProperty = property(get_HsvColorProperty, None)
    MaxHueProperty = property(get_MaxHueProperty, None)
    MaxSaturationProperty = property(get_MaxSaturationProperty, None)
    MaxValueProperty = property(get_MaxValueProperty, None)
    MinHueProperty = property(get_MinHueProperty, None)
    MinSaturationProperty = property(get_MinSaturationProperty, None)
    MinValueProperty = property(get_MinValueProperty, None)
    ShapeProperty = property(get_ShapeProperty, None)
class IColumnMajorUniformToLargestGridLayout(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayout'
    _iid_ = Guid('{ee10a6aa-efeb-51ac-b791-71913ae8c235}')
    @winrt_commethod(6)
    def get_MaxColumns(self) -> Int32: ...
    @winrt_commethod(7)
    def put_MaxColumns(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_ColumnSpacing(self) -> Double: ...
    @winrt_commethod(9)
    def put_ColumnSpacing(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_RowSpacing(self) -> Double: ...
    @winrt_commethod(11)
    def put_RowSpacing(self, value: Double) -> Void: ...
    ColumnSpacing = property(get_ColumnSpacing, put_ColumnSpacing)
    MaxColumns = property(get_MaxColumns, put_MaxColumns)
    RowSpacing = property(get_RowSpacing, put_RowSpacing)
class IColumnMajorUniformToLargestGridLayoutFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayoutFactory'
    _iid_ = Guid('{2f21af59-1585-5325-8412-2b83bf05d345}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ColumnMajorUniformToLargestGridLayout: ...
class IColumnMajorUniformToLargestGridLayoutStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IColumnMajorUniformToLargestGridLayoutStatics'
    _iid_ = Guid('{7b2f0ec6-2345-5986-a5b9-b1beb5a74350}')
    @winrt_commethod(6)
    def get_MaxColumnsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ColumnSpacingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RowSpacingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColumnSpacingProperty = property(get_ColumnSpacingProperty, None)
    MaxColumnsProperty = property(get_MaxColumnsProperty, None)
    RowSpacingProperty = property(get_RowSpacingProperty, None)
class IComboBoxHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IComboBoxHelper'
    _iid_ = Guid('{5a3c87ac-c399-5e5f-873f-b9d0e8bcceb7}')
class IComboBoxHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IComboBoxHelperStatics'
    _iid_ = Guid('{ec21be42-ed02-5c10-9fbe-af1881cd877b}')
    @winrt_commethod(6)
    def get_KeepInteriorCornersSquareProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def SetKeepInteriorCornersSquare(self, comboBox: win32more.Microsoft.UI.Xaml.Controls.ComboBox, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetKeepInteriorCornersSquare(self, comboBox: win32more.Microsoft.UI.Xaml.Controls.ComboBox) -> Boolean: ...
    KeepInteriorCornersSquareProperty = property(get_KeepInteriorCornersSquareProperty, None)
class IComboBoxTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings'
    _iid_ = Guid('{f2dc5e7f-8d3f-5c20-b356-af6f1ff8242a}')
    @winrt_commethod(6)
    def get_DropDownOpenedHeight(self) -> Double: ...
    @winrt_commethod(7)
    def get_DropDownClosedHeight(self) -> Double: ...
    @winrt_commethod(8)
    def get_DropDownOffset(self) -> Double: ...
    @winrt_commethod(9)
    def get_SelectedItemDirection(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_commethod(10)
    def get_DropDownContentMinWidth(self) -> Double: ...
    DropDownClosedHeight = property(get_DropDownClosedHeight, None)
    DropDownContentMinWidth = property(get_DropDownContentMinWidth, None)
    DropDownOffset = property(get_DropDownOffset, None)
    DropDownOpenedHeight = property(get_DropDownOpenedHeight, None)
    SelectedItemDirection = property(get_SelectedItemDirection, None)
class ICommandBarFlyoutCommandBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar'
    _iid_ = Guid('{0f7120c5-6d00-5489-9171-bedd2d4ef677}')
    @winrt_commethod(6)
    def get_FlyoutTemplateSettings(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBarTemplateSettings: ...
    FlyoutTemplateSettings = property(get_FlyoutTemplateSettings, None)
class ICommandBarFlyoutCommandBar2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar2'
    _iid_ = Guid('{6aca769f-1119-5355-af7f-bcd5aa751229}')
    @winrt_commethod(6)
    def get_SystemBackdrop(self) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_commethod(7)
    def put_SystemBackdrop(self, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
class ICommandBarFlyoutCommandBarAutomationPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarAutomationPropertiesStatics'
    _iid_ = Guid('{c9957f75-c57f-5ba3-b867-f9d86b1d90b9}')
    @winrt_commethod(6)
    def get_ControlTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetControlType(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(8)
    def SetControlType(self, element: win32more.Microsoft.UI.Xaml.UIElement, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    ControlTypeProperty = property(get_ControlTypeProperty, None)
class ICommandBarFlyoutCommandBarFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarFactory'
    _iid_ = Guid('{58dbcda9-38e4-5efc-b740-26fda3d0a3c6}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar: ...
class ICommandBarFlyoutCommandBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarStatics'
    _iid_ = Guid('{5f7fb950-7c7d-5f5c-8fc5-91344f3b034c}')
    @winrt_commethod(6)
    def get_SystemBackdropProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    SystemBackdropProperty = property(get_SystemBackdropProperty, None)
class ICommandBarFlyoutCommandBarTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings'
    _iid_ = Guid('{533cc5ca-dcf7-5f9d-a460-934a883acdc1}')
    @winrt_commethod(6)
    def get_OpenAnimationStartPosition(self) -> Double: ...
    @winrt_commethod(7)
    def get_OpenAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(8)
    def get_CloseAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(9)
    def get_CurrentWidth(self) -> Double: ...
    @winrt_commethod(10)
    def get_ExpandedWidth(self) -> Double: ...
    @winrt_commethod(11)
    def get_WidthExpansionDelta(self) -> Double: ...
    @winrt_commethod(12)
    def get_WidthExpansionAnimationStartPosition(self) -> Double: ...
    @winrt_commethod(13)
    def get_WidthExpansionAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(14)
    def get_WidthExpansionMoreButtonAnimationStartPosition(self) -> Double: ...
    @winrt_commethod(15)
    def get_WidthExpansionMoreButtonAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(16)
    def get_ExpandUpOverflowVerticalPosition(self) -> Double: ...
    @winrt_commethod(17)
    def get_ExpandDownOverflowVerticalPosition(self) -> Double: ...
    @winrt_commethod(18)
    def get_ExpandUpAnimationStartPosition(self) -> Double: ...
    @winrt_commethod(19)
    def get_ExpandUpAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(20)
    def get_ExpandUpAnimationHoldPosition(self) -> Double: ...
    @winrt_commethod(21)
    def get_ExpandDownAnimationStartPosition(self) -> Double: ...
    @winrt_commethod(22)
    def get_ExpandDownAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(23)
    def get_ExpandDownAnimationHoldPosition(self) -> Double: ...
    @winrt_commethod(24)
    def get_ContentClipRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(25)
    def get_OverflowContentClipRect(self) -> win32more.Windows.Foundation.Rect: ...
    CloseAnimationEndPosition = property(get_CloseAnimationEndPosition, None)
    ContentClipRect = property(get_ContentClipRect, None)
    CurrentWidth = property(get_CurrentWidth, None)
    ExpandDownAnimationEndPosition = property(get_ExpandDownAnimationEndPosition, None)
    ExpandDownAnimationHoldPosition = property(get_ExpandDownAnimationHoldPosition, None)
    ExpandDownAnimationStartPosition = property(get_ExpandDownAnimationStartPosition, None)
    ExpandDownOverflowVerticalPosition = property(get_ExpandDownOverflowVerticalPosition, None)
    ExpandUpAnimationEndPosition = property(get_ExpandUpAnimationEndPosition, None)
    ExpandUpAnimationHoldPosition = property(get_ExpandUpAnimationHoldPosition, None)
    ExpandUpAnimationStartPosition = property(get_ExpandUpAnimationStartPosition, None)
    ExpandUpOverflowVerticalPosition = property(get_ExpandUpOverflowVerticalPosition, None)
    ExpandedWidth = property(get_ExpandedWidth, None)
    OpenAnimationEndPosition = property(get_OpenAnimationEndPosition, None)
    OpenAnimationStartPosition = property(get_OpenAnimationStartPosition, None)
    OverflowContentClipRect = property(get_OverflowContentClipRect, None)
    WidthExpansionAnimationEndPosition = property(get_WidthExpansionAnimationEndPosition, None)
    WidthExpansionAnimationStartPosition = property(get_WidthExpansionAnimationStartPosition, None)
    WidthExpansionDelta = property(get_WidthExpansionDelta, None)
    WidthExpansionMoreButtonAnimationEndPosition = property(get_WidthExpansionMoreButtonAnimationEndPosition, None)
    WidthExpansionMoreButtonAnimationStartPosition = property(get_WidthExpansionMoreButtonAnimationStartPosition, None)
class ICommandBarTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings'
    _iid_ = Guid('{ae9535f6-1678-5066-90bf-147aa610c5dd}')
    @winrt_commethod(6)
    def get_ContentHeight(self) -> Double: ...
    @winrt_commethod(7)
    def get_OverflowContentClipRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_OverflowContentMinWidth(self) -> Double: ...
    @winrt_commethod(9)
    def get_OverflowContentMaxWidth(self) -> Double: ...
    @winrt_commethod(10)
    def get_OverflowContentMaxHeight(self) -> Double: ...
    @winrt_commethod(11)
    def get_OverflowContentHorizontalOffset(self) -> Double: ...
    @winrt_commethod(12)
    def get_OverflowContentHeight(self) -> Double: ...
    @winrt_commethod(13)
    def get_NegativeOverflowContentHeight(self) -> Double: ...
    @winrt_commethod(14)
    def get_EffectiveOverflowButtonVisibility(self) -> win32more.Microsoft.UI.Xaml.Visibility: ...
    @winrt_commethod(15)
    def get_OverflowContentCompactYTranslation(self) -> Double: ...
    @winrt_commethod(16)
    def get_OverflowContentMinimalYTranslation(self) -> Double: ...
    @winrt_commethod(17)
    def get_OverflowContentHiddenYTranslation(self) -> Double: ...
    ContentHeight = property(get_ContentHeight, None)
    EffectiveOverflowButtonVisibility = property(get_EffectiveOverflowButtonVisibility, None)
    NegativeOverflowContentHeight = property(get_NegativeOverflowContentHeight, None)
    OverflowContentClipRect = property(get_OverflowContentClipRect, None)
    OverflowContentCompactYTranslation = property(get_OverflowContentCompactYTranslation, None)
    OverflowContentHeight = property(get_OverflowContentHeight, None)
    OverflowContentHiddenYTranslation = property(get_OverflowContentHiddenYTranslation, None)
    OverflowContentHorizontalOffset = property(get_OverflowContentHorizontalOffset, None)
    OverflowContentMaxHeight = property(get_OverflowContentMaxHeight, None)
    OverflowContentMaxWidth = property(get_OverflowContentMaxWidth, None)
    OverflowContentMinWidth = property(get_OverflowContentMinWidth, None)
    OverflowContentMinimalYTranslation = property(get_OverflowContentMinimalYTranslation, None)
class ICornerRadiusFilterConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverter'
    _iid_ = Guid('{6f1a3ed2-f965-545e-bd44-441db1794f5f}')
    @winrt_commethod(6)
    def get_Filter(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterKind: ...
    @winrt_commethod(7)
    def put_Filter(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterKind) -> Void: ...
    @winrt_commethod(8)
    def get_Scale(self) -> Double: ...
    @winrt_commethod(9)
    def put_Scale(self, value: Double) -> Void: ...
    Filter = property(get_Filter, put_Filter)
    Scale = property(get_Scale, put_Scale)
class ICornerRadiusFilterConverterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusFilterConverterStatics'
    _iid_ = Guid('{2d9574f9-cc9e-535e-a70e-d55c4ca27f49}')
    @winrt_commethod(6)
    def get_FilterProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ScaleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FilterProperty = property(get_FilterProperty, None)
    ScaleProperty = property(get_ScaleProperty, None)
class ICornerRadiusToThicknessConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverter'
    _iid_ = Guid('{b36aa8ae-166e-5ca5-93d2-95e9907c1222}')
    @winrt_commethod(6)
    def get_ConversionKind(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverterKind: ...
    @winrt_commethod(7)
    def put_ConversionKind(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverterKind) -> Void: ...
    @winrt_commethod(8)
    def get_Multiplier(self) -> Double: ...
    @winrt_commethod(9)
    def put_Multiplier(self, value: Double) -> Void: ...
    ConversionKind = property(get_ConversionKind, put_ConversionKind)
    Multiplier = property(get_Multiplier, put_Multiplier)
class ICornerRadiusToThicknessConverterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ICornerRadiusToThicknessConverterStatics'
    _iid_ = Guid('{92ad9d36-5483-5258-a43b-4356443087f1}')
    @winrt_commethod(6)
    def get_ConversionKindProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MultiplierProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ConversionKindProperty = property(get_ConversionKindProperty, None)
    MultiplierProperty = property(get_MultiplierProperty, None)
class IDragCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs'
    _iid_ = Guid('{acd47547-3784-51ff-8eeb-7b212439974b}')
    @winrt_commethod(6)
    def get_HorizontalChange(self) -> Double: ...
    @winrt_commethod(7)
    def get_VerticalChange(self) -> Double: ...
    @winrt_commethod(8)
    def get_Canceled(self) -> Boolean: ...
    Canceled = property(get_Canceled, None)
    HorizontalChange = property(get_HorizontalChange, None)
    VerticalChange = property(get_VerticalChange, None)
class IDragCompletedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IDragCompletedEventArgsFactory'
    _iid_ = Guid('{5767c408-454b-55cf-b74e-229642aed108}')
    @winrt_commethod(6)
    def CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled(self, horizontalChange: Double, verticalChange: Double, canceled: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.DragCompletedEventArgs: ...
class IDragDeltaEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs'
    _iid_ = Guid('{bc405765-ed94-5697-8506-a8f3d15272f9}')
    @winrt_commethod(6)
    def get_HorizontalChange(self) -> Double: ...
    @winrt_commethod(7)
    def get_VerticalChange(self) -> Double: ...
    HorizontalChange = property(get_HorizontalChange, None)
    VerticalChange = property(get_VerticalChange, None)
class IDragDeltaEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IDragDeltaEventArgsFactory'
    _iid_ = Guid('{4adba280-e1f9-5dab-87ff-5903b419ef9d}')
    @winrt_commethod(6)
    def CreateInstanceWithHorizontalChangeAndVerticalChange(self, horizontalChange: Double, verticalChange: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.DragDeltaEventArgs: ...
class IDragStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IDragStartedEventArgs'
    _iid_ = Guid('{aa27aee4-2bdd-5d9a-8a1c-b37480a2012b}')
    @winrt_commethod(6)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(7)
    def get_VerticalOffset(self) -> Double: ...
    HorizontalOffset = property(get_HorizontalOffset, None)
    VerticalOffset = property(get_VerticalOffset, None)
class IDragStartedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IDragStartedEventArgsFactory'
    _iid_ = Guid('{36078aa3-906c-5ef0-9d24-30c09f79c18f}')
    @winrt_commethod(6)
    def CreateInstanceWithHorizontalOffsetAndVerticalOffset(self, horizontalOffset: Double, verticalOffset: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.DragStartedEventArgs: ...
class IFlyoutBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase'
    _iid_ = Guid('{bb6603bf-744d-5c31-a87d-744394634d77}')
    @winrt_commethod(6)
    def get_Placement(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_commethod(7)
    def put_Placement(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
    @winrt_commethod(8)
    def get_Target(self) -> win32more.Microsoft.UI.Xaml.FrameworkElement: ...
    @winrt_commethod(9)
    def get_AllowFocusOnInteraction(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_AllowFocusOnInteraction(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_LightDismissOverlayMode(self) -> win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_commethod(12)
    def put_LightDismissOverlayMode(self, value: win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    @winrt_commethod(13)
    def get_AllowFocusWhenDisabled(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_AllowFocusWhenDisabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_ShowMode(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_commethod(16)
    def put_ShowMode(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_commethod(17)
    def get_InputDevicePrefersPrimaryCommands(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_AreOpenCloseAnimationsEnabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_AreOpenCloseAnimationsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_ShouldConstrainToRootBounds(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_ShouldConstrainToRootBounds(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_IsConstrainedToRootBounds(self) -> Boolean: ...
    @winrt_commethod(23)
    def get_ElementSoundMode(self) -> win32more.Microsoft.UI.Xaml.ElementSoundMode: ...
    @winrt_commethod(24)
    def put_ElementSoundMode(self, value: win32more.Microsoft.UI.Xaml.ElementSoundMode) -> Void: ...
    @winrt_commethod(25)
    def get_OverlayInputPassThroughElement(self) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(26)
    def put_OverlayInputPassThroughElement(self, value: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_commethod(27)
    def get_IsOpen(self) -> Boolean: ...
    @winrt_commethod(28)
    def get_XamlRoot(self) -> win32more.Microsoft.UI.Xaml.XamlRoot: ...
    @winrt_commethod(29)
    def put_XamlRoot(self, value: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_commethod(30)
    def add_Opened(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_Opened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_Closed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_Opening(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_Opening(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def add_Closing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase, win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBaseClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(37)
    def remove_Closing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(38)
    def ShowAt(self, placementTarget: win32more.Microsoft.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_commethod(39)
    def ShowAtWithOptions(self, placementTarget: win32more.Microsoft.UI.Xaml.DependencyObject, showOptions: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowOptions) -> Void: ...
    @winrt_commethod(40)
    def Hide(self) -> Void: ...
    @winrt_commethod(41)
    def TryInvokeKeyboardAccelerator(self, args: win32more.Microsoft.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    AllowFocusOnInteraction = property(get_AllowFocusOnInteraction, put_AllowFocusOnInteraction)
    AllowFocusWhenDisabled = property(get_AllowFocusWhenDisabled, put_AllowFocusWhenDisabled)
    AreOpenCloseAnimationsEnabled = property(get_AreOpenCloseAnimationsEnabled, put_AreOpenCloseAnimationsEnabled)
    ElementSoundMode = property(get_ElementSoundMode, put_ElementSoundMode)
    InputDevicePrefersPrimaryCommands = property(get_InputDevicePrefersPrimaryCommands, None)
    IsConstrainedToRootBounds = property(get_IsConstrainedToRootBounds, None)
    IsOpen = property(get_IsOpen, None)
    LightDismissOverlayMode = property(get_LightDismissOverlayMode, put_LightDismissOverlayMode)
    OverlayInputPassThroughElement = property(get_OverlayInputPassThroughElement, put_OverlayInputPassThroughElement)
    Placement = property(get_Placement, put_Placement)
    ShouldConstrainToRootBounds = property(get_ShouldConstrainToRootBounds, put_ShouldConstrainToRootBounds)
    ShowMode = property(get_ShowMode, put_ShowMode)
    Target = property(get_Target, None)
    XamlRoot = property(get_XamlRoot, put_XamlRoot)
    Opened = event()
    Closed = event()
    Opening = event()
    Closing = event()
class IFlyoutBase2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBase2'
    _iid_ = Guid('{54592f97-e40e-5cad-864b-32307d047020}')
    @winrt_commethod(6)
    def get_SystemBackdrop(self) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_commethod(7)
    def put_SystemBackdrop(self, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
class IFlyoutBaseClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs'
    _iid_ = Guid('{7cb280b4-1cca-5a5a-8ea4-191a2bbc8b32}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    Cancel = property(get_Cancel, put_Cancel)
class IFlyoutBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseFactory'
    _iid_ = Guid('{006d738f-7c91-5ef3-8a80-a548108dab8b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase: ...
class IFlyoutBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides'
    _iid_ = Guid('{5bb19ed8-08de-5eec-91cb-5fc59974e894}')
    @winrt_commethod(6)
    def CreatePresenter(self) -> win32more.Microsoft.UI.Xaml.Controls.Control: ...
    @winrt_commethod(7)
    def OnProcessKeyboardAccelerators(self, args: win32more.Microsoft.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
class IFlyoutBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics'
    _iid_ = Guid('{63ee628e-d2e3-5515-aea4-e461088c0c4e}')
    @winrt_commethod(6)
    def get_TargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PlacementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AllowFocusOnInteractionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_LightDismissOverlayModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_AllowFocusWhenDisabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ShowModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_InputDevicePrefersPrimaryCommandsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_AreOpenCloseAnimationsEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ShouldConstrainToRootBoundsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ElementSoundModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_OverlayInputPassThroughElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_IsOpenProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_AttachedFlyoutProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def GetAttachedFlyout(self, element: win32more.Microsoft.UI.Xaml.FrameworkElement) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_commethod(20)
    def SetAttachedFlyout(self, element: win32more.Microsoft.UI.Xaml.FrameworkElement, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_commethod(21)
    def ShowAttachedFlyout(self, flyoutOwner: win32more.Microsoft.UI.Xaml.FrameworkElement) -> Void: ...
    AllowFocusOnInteractionProperty = property(get_AllowFocusOnInteractionProperty, None)
    AllowFocusWhenDisabledProperty = property(get_AllowFocusWhenDisabledProperty, None)
    AreOpenCloseAnimationsEnabledProperty = property(get_AreOpenCloseAnimationsEnabledProperty, None)
    AttachedFlyoutProperty = property(get_AttachedFlyoutProperty, None)
    ElementSoundModeProperty = property(get_ElementSoundModeProperty, None)
    InputDevicePrefersPrimaryCommandsProperty = property(get_InputDevicePrefersPrimaryCommandsProperty, None)
    IsOpenProperty = property(get_IsOpenProperty, None)
    LightDismissOverlayModeProperty = property(get_LightDismissOverlayModeProperty, None)
    OverlayInputPassThroughElementProperty = property(get_OverlayInputPassThroughElementProperty, None)
    PlacementProperty = property(get_PlacementProperty, None)
    ShouldConstrainToRootBoundsProperty = property(get_ShouldConstrainToRootBoundsProperty, None)
    ShowModeProperty = property(get_ShowModeProperty, None)
    TargetProperty = property(get_TargetProperty, None)
class IFlyoutBaseStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2'
    _iid_ = Guid('{2403cd2c-a6b8-5dc2-be3b-2a4bdd072ef1}')
    @winrt_commethod(6)
    def get_SystemBackdropProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    SystemBackdropProperty = property(get_SystemBackdropProperty, None)
class IFlyoutShowOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptions'
    _iid_ = Guid('{30774a93-2803-50d3-b406-904aec3e175d}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(7)
    def put_Position(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(8)
    def get_ExclusionRect(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_ExclusionRect(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    @winrt_commethod(10)
    def get_ShowMode(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_commethod(11)
    def put_ShowMode(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_commethod(12)
    def get_Placement(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_commethod(13)
    def put_Placement(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    Placement = property(get_Placement, put_Placement)
    Position = property(get_Position, put_Position)
    ShowMode = property(get_ShowMode, put_ShowMode)
class IFlyoutShowOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IFlyoutShowOptionsFactory'
    _iid_ = Guid('{17426d30-70d9-54d7-bd39-e7c4c940c0f4}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowOptions: ...
class IGeneratorPositionHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IGeneratorPositionHelper'
    _iid_ = Guid('{872a9f8f-0e0e-5089-92a9-dbced99ca86d}')
class IGeneratorPositionHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IGeneratorPositionHelperStatics'
    _iid_ = Guid('{3113605a-3feb-54f9-a256-f373250281d4}')
    @winrt_commethod(6)
    def FromIndexAndOffset(self, index: Int32, offset: Int32) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
class IGridViewItemPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenter'
    _iid_ = Guid('{22772fd8-fe30-5b6f-9b17-5eea5d70d860}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SelectionCheckMarkVisualEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CheckHintBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_CheckHintBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_CheckSelectingBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(11)
    def put_CheckSelectingBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(12)
    def get_CheckBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(13)
    def put_CheckBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(14)
    def get_DragBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(15)
    def put_DragBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(16)
    def get_DragForeground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_DragForeground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(18)
    def get_FocusBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(19)
    def put_FocusBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(20)
    def get_PlaceholderBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(21)
    def put_PlaceholderBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(22)
    def get_PointerOverBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(23)
    def put_PointerOverBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(24)
    def get_SelectedBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(25)
    def put_SelectedBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(26)
    def get_SelectedForeground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(27)
    def put_SelectedForeground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(28)
    def get_SelectedPointerOverBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(29)
    def put_SelectedPointerOverBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(30)
    def get_SelectedPointerOverBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(31)
    def put_SelectedPointerOverBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(32)
    def get_SelectedBorderThickness(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(33)
    def put_SelectedBorderThickness(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(34)
    def get_DisabledOpacity(self) -> Double: ...
    @winrt_commethod(35)
    def put_DisabledOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(36)
    def get_DragOpacity(self) -> Double: ...
    @winrt_commethod(37)
    def put_DragOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(38)
    def get_ReorderHintOffset(self) -> Double: ...
    @winrt_commethod(39)
    def put_ReorderHintOffset(self, value: Double) -> Void: ...
    @winrt_commethod(40)
    def get_GridViewItemPresenterHorizontalContentAlignment(self) -> win32more.Microsoft.UI.Xaml.HorizontalAlignment: ...
    @winrt_commethod(41)
    def put_GridViewItemPresenterHorizontalContentAlignment(self, value: win32more.Microsoft.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_commethod(42)
    def get_GridViewItemPresenterVerticalContentAlignment(self) -> win32more.Microsoft.UI.Xaml.VerticalAlignment: ...
    @winrt_commethod(43)
    def put_GridViewItemPresenterVerticalContentAlignment(self, value: win32more.Microsoft.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_commethod(44)
    def get_GridViewItemPresenterPadding(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(45)
    def put_GridViewItemPresenterPadding(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(46)
    def get_PointerOverBackgroundMargin(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(47)
    def put_PointerOverBackgroundMargin(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(48)
    def get_ContentMargin(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(49)
    def put_ContentMargin(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    CheckBrush = property(get_CheckBrush, put_CheckBrush)
    CheckHintBrush = property(get_CheckHintBrush, put_CheckHintBrush)
    CheckSelectingBrush = property(get_CheckSelectingBrush, put_CheckSelectingBrush)
    ContentMargin = property(get_ContentMargin, put_ContentMargin)
    DisabledOpacity = property(get_DisabledOpacity, put_DisabledOpacity)
    DragBackground = property(get_DragBackground, put_DragBackground)
    DragForeground = property(get_DragForeground, put_DragForeground)
    DragOpacity = property(get_DragOpacity, put_DragOpacity)
    FocusBorderBrush = property(get_FocusBorderBrush, put_FocusBorderBrush)
    GridViewItemPresenterHorizontalContentAlignment = property(get_GridViewItemPresenterHorizontalContentAlignment, put_GridViewItemPresenterHorizontalContentAlignment)
    GridViewItemPresenterPadding = property(get_GridViewItemPresenterPadding, put_GridViewItemPresenterPadding)
    GridViewItemPresenterVerticalContentAlignment = property(get_GridViewItemPresenterVerticalContentAlignment, put_GridViewItemPresenterVerticalContentAlignment)
    PlaceholderBackground = property(get_PlaceholderBackground, put_PlaceholderBackground)
    PointerOverBackground = property(get_PointerOverBackground, put_PointerOverBackground)
    PointerOverBackgroundMargin = property(get_PointerOverBackgroundMargin, put_PointerOverBackgroundMargin)
    ReorderHintOffset = property(get_ReorderHintOffset, put_ReorderHintOffset)
    SelectedBackground = property(get_SelectedBackground, put_SelectedBackground)
    SelectedBorderThickness = property(get_SelectedBorderThickness, put_SelectedBorderThickness)
    SelectedForeground = property(get_SelectedForeground, put_SelectedForeground)
    SelectedPointerOverBackground = property(get_SelectedPointerOverBackground, put_SelectedPointerOverBackground)
    SelectedPointerOverBorderBrush = property(get_SelectedPointerOverBorderBrush, put_SelectedPointerOverBorderBrush)
    SelectionCheckMarkVisualEnabled = property(get_SelectionCheckMarkVisualEnabled, put_SelectionCheckMarkVisualEnabled)
class IGridViewItemPresenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterFactory'
    _iid_ = Guid('{d1f47760-c353-5a10-8a6b-9a1e3b52f934}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GridViewItemPresenter: ...
class IGridViewItemPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics'
    _iid_ = Guid('{31a58ed1-901c-5753-944e-4dd9f22d2447}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CheckHintBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CheckSelectingBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CheckBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DragBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_DragForegroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_FocusBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_PlaceholderBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_PointerOverBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_SelectedBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_SelectedForegroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_SelectedPointerOverBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_SelectedPointerOverBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_SelectedBorderThicknessProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_DisabledOpacityProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_DragOpacityProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_ReorderHintOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_GridViewItemPresenterHorizontalContentAlignmentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(24)
    def get_GridViewItemPresenterVerticalContentAlignmentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def get_GridViewItemPresenterPaddingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(26)
    def get_PointerOverBackgroundMarginProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(27)
    def get_ContentMarginProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CheckBrushProperty = property(get_CheckBrushProperty, None)
    CheckHintBrushProperty = property(get_CheckHintBrushProperty, None)
    CheckSelectingBrushProperty = property(get_CheckSelectingBrushProperty, None)
    ContentMarginProperty = property(get_ContentMarginProperty, None)
    DisabledOpacityProperty = property(get_DisabledOpacityProperty, None)
    DragBackgroundProperty = property(get_DragBackgroundProperty, None)
    DragForegroundProperty = property(get_DragForegroundProperty, None)
    DragOpacityProperty = property(get_DragOpacityProperty, None)
    FocusBorderBrushProperty = property(get_FocusBorderBrushProperty, None)
    GridViewItemPresenterHorizontalContentAlignmentProperty = property(get_GridViewItemPresenterHorizontalContentAlignmentProperty, None)
    GridViewItemPresenterPaddingProperty = property(get_GridViewItemPresenterPaddingProperty, None)
    GridViewItemPresenterVerticalContentAlignmentProperty = property(get_GridViewItemPresenterVerticalContentAlignmentProperty, None)
    PlaceholderBackgroundProperty = property(get_PlaceholderBackgroundProperty, None)
    PointerOverBackgroundMarginProperty = property(get_PointerOverBackgroundMarginProperty, None)
    PointerOverBackgroundProperty = property(get_PointerOverBackgroundProperty, None)
    ReorderHintOffsetProperty = property(get_ReorderHintOffsetProperty, None)
    SelectedBackgroundProperty = property(get_SelectedBackgroundProperty, None)
    SelectedBorderThicknessProperty = property(get_SelectedBorderThicknessProperty, None)
    SelectedForegroundProperty = property(get_SelectedForegroundProperty, None)
    SelectedPointerOverBackgroundProperty = property(get_SelectedPointerOverBackgroundProperty, None)
    SelectedPointerOverBorderBrushProperty = property(get_SelectedPointerOverBorderBrushProperty, None)
    SelectionCheckMarkVisualEnabledProperty = property(get_SelectionCheckMarkVisualEnabledProperty, None)
class IGridViewItemTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IGridViewItemTemplateSettings'
    _iid_ = Guid('{7033e884-2117-56e7-afb8-b7f5b8b64c70}')
    @winrt_commethod(6)
    def get_DragItemsCount(self) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class IInfoBarPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanel'
    _iid_ = Guid('{4d2fd5fe-cb75-52ff-b57f-a992912383cc}')
    @winrt_commethod(6)
    def get_HorizontalOrientationPadding(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(7)
    def put_HorizontalOrientationPadding(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(8)
    def get_VerticalOrientationPadding(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(9)
    def put_VerticalOrientationPadding(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    HorizontalOrientationPadding = property(get_HorizontalOrientationPadding, put_HorizontalOrientationPadding)
    VerticalOrientationPadding = property(get_VerticalOrientationPadding, put_VerticalOrientationPadding)
class IInfoBarPanelFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelFactory'
    _iid_ = Guid('{00d1a8c5-f631-564a-8e9c-7c5ccad238de}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.InfoBarPanel: ...
class IInfoBarPanelStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics'
    _iid_ = Guid('{e0f19305-b392-5fa6-9670-895895a067ff}')
    @winrt_commethod(6)
    def get_HorizontalOrientationPaddingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VerticalOrientationPaddingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def SetHorizontalOrientationMargin(self, object: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(9)
    def GetHorizontalOrientationMargin(self, object: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(10)
    def get_HorizontalOrientationMarginProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def SetVerticalOrientationMargin(self, object: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(12)
    def GetVerticalOrientationMargin(self, object: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(13)
    def get_VerticalOrientationMarginProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    HorizontalOrientationMarginProperty = property(get_HorizontalOrientationMarginProperty, None)
    HorizontalOrientationPaddingProperty = property(get_HorizontalOrientationPaddingProperty, None)
    VerticalOrientationMarginProperty = property(get_VerticalOrientationMarginProperty, None)
    VerticalOrientationPaddingProperty = property(get_VerticalOrientationPaddingProperty, None)
class IItemsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs'
    _iid_ = Guid('{b2ba1610-0e96-538a-978f-ec0b37193228}')
    @winrt_commethod(6)
    def get_Action(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
    @winrt_commethod(8)
    def get_OldPosition(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
    @winrt_commethod(9)
    def get_ItemCount(self) -> Int32: ...
    @winrt_commethod(10)
    def get_ItemUICount(self) -> Int32: ...
    Action = property(get_Action, None)
    ItemCount = property(get_ItemCount, None)
    ItemUICount = property(get_ItemUICount, None)
    OldPosition = property(get_OldPosition, None)
    Position = property(get_Position, None)
class IJumpListItemBackgroundConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter'
    _iid_ = Guid('{c475bb52-ea34-5cde-9851-7841febd3d1d}')
    @winrt_commethod(6)
    def get_Enabled(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Enabled(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Disabled(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_Disabled(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
class IJumpListItemBackgroundConverterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverterStatics'
    _iid_ = Guid('{b03cb261-71ec-540e-83ac-e1a9fdd335e6}')
    @winrt_commethod(6)
    def get_EnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_DisabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DisabledProperty = property(get_DisabledProperty, None)
    EnabledProperty = property(get_EnabledProperty, None)
class IJumpListItemForegroundConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter'
    _iid_ = Guid('{7308e0e4-102f-571a-bfdc-c8f411f07400}')
    @winrt_commethod(6)
    def get_Enabled(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Enabled(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Disabled(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_Disabled(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
class IJumpListItemForegroundConverterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverterStatics'
    _iid_ = Guid('{9ab3b95d-4061-59b4-9ce9-f45e2c05add7}')
    @winrt_commethod(6)
    def get_EnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_DisabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DisabledProperty = property(get_DisabledProperty, None)
    EnabledProperty = property(get_EnabledProperty, None)
class ILayoutInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ILayoutInformation'
    _iid_ = Guid('{ceea0a8c-5a4f-5d7a-8fea-77b5e0e0230c}')
class ILayoutInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ILayoutInformationStatics'
    _iid_ = Guid('{8ddb192d-b7ff-5307-acf4-d4e547da5815}')
    @winrt_commethod(6)
    def GetLayoutExceptionElement(self, dispatcher: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def GetLayoutSlot(self, element: win32more.Microsoft.UI.Xaml.FrameworkElement) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def GetAvailableSize(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Size: ...
class IListViewItemPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter'
    _iid_ = Guid('{81012623-d987-5582-bc28-755a95caaf1c}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SelectionCheckMarkVisualEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CheckHintBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_CheckHintBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_CheckSelectingBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(11)
    def put_CheckSelectingBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(12)
    def get_CheckBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(13)
    def put_CheckBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(14)
    def get_DragBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(15)
    def put_DragBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(16)
    def get_DragForeground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_DragForeground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(18)
    def get_FocusBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(19)
    def put_FocusBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(20)
    def get_PlaceholderBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(21)
    def put_PlaceholderBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(22)
    def get_PointerOverBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(23)
    def put_PointerOverBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(24)
    def get_SelectedBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(25)
    def put_SelectedBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(26)
    def get_SelectedForeground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(27)
    def put_SelectedForeground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(28)
    def get_SelectedPointerOverBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(29)
    def put_SelectedPointerOverBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(30)
    def get_SelectedPointerOverBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(31)
    def put_SelectedPointerOverBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(32)
    def get_SelectedBorderThickness(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(33)
    def put_SelectedBorderThickness(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(34)
    def get_DisabledOpacity(self) -> Double: ...
    @winrt_commethod(35)
    def put_DisabledOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(36)
    def get_DragOpacity(self) -> Double: ...
    @winrt_commethod(37)
    def put_DragOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(38)
    def get_ReorderHintOffset(self) -> Double: ...
    @winrt_commethod(39)
    def put_ReorderHintOffset(self, value: Double) -> Void: ...
    @winrt_commethod(40)
    def get_ListViewItemPresenterHorizontalContentAlignment(self) -> win32more.Microsoft.UI.Xaml.HorizontalAlignment: ...
    @winrt_commethod(41)
    def put_ListViewItemPresenterHorizontalContentAlignment(self, value: win32more.Microsoft.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_commethod(42)
    def get_ListViewItemPresenterVerticalContentAlignment(self) -> win32more.Microsoft.UI.Xaml.VerticalAlignment: ...
    @winrt_commethod(43)
    def put_ListViewItemPresenterVerticalContentAlignment(self, value: win32more.Microsoft.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_commethod(44)
    def get_ListViewItemPresenterPadding(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(45)
    def put_ListViewItemPresenterPadding(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(46)
    def get_PointerOverBackgroundMargin(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(47)
    def put_PointerOverBackgroundMargin(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(48)
    def get_ContentMargin(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(49)
    def put_ContentMargin(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(50)
    def get_SelectedPressedBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(51)
    def put_SelectedPressedBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(52)
    def get_PressedBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(53)
    def put_PressedBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(54)
    def get_CheckBoxBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(55)
    def put_CheckBoxBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(56)
    def get_FocusSecondaryBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(57)
    def put_FocusSecondaryBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(58)
    def get_CheckMode(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode: ...
    @winrt_commethod(59)
    def put_CheckMode(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode) -> Void: ...
    @winrt_commethod(60)
    def get_PointerOverForeground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(61)
    def put_PointerOverForeground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(62)
    def get_RevealBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(63)
    def put_RevealBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(64)
    def get_RevealBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(65)
    def put_RevealBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(66)
    def get_RevealBorderThickness(self) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_commethod(67)
    def put_RevealBorderThickness(self, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(68)
    def get_RevealBackgroundShowsAboveContent(self) -> Boolean: ...
    @winrt_commethod(69)
    def put_RevealBackgroundShowsAboveContent(self, value: Boolean) -> Void: ...
    @winrt_commethod(70)
    def get_SelectedDisabledBackground(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(71)
    def put_SelectedDisabledBackground(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(72)
    def get_CheckPressedBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(73)
    def put_CheckPressedBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(74)
    def get_CheckDisabledBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(75)
    def put_CheckDisabledBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(76)
    def get_CheckBoxPointerOverBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(77)
    def put_CheckBoxPointerOverBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(78)
    def get_CheckBoxPressedBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(79)
    def put_CheckBoxPressedBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(80)
    def get_CheckBoxDisabledBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(81)
    def put_CheckBoxDisabledBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(82)
    def get_CheckBoxSelectedBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(83)
    def put_CheckBoxSelectedBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(84)
    def get_CheckBoxSelectedPointerOverBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(85)
    def put_CheckBoxSelectedPointerOverBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(86)
    def get_CheckBoxSelectedPressedBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(87)
    def put_CheckBoxSelectedPressedBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(88)
    def get_CheckBoxSelectedDisabledBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(89)
    def put_CheckBoxSelectedDisabledBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(90)
    def get_CheckBoxBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(91)
    def put_CheckBoxBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(92)
    def get_CheckBoxPointerOverBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(93)
    def put_CheckBoxPointerOverBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(94)
    def get_CheckBoxPressedBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(95)
    def put_CheckBoxPressedBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(96)
    def get_CheckBoxDisabledBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(97)
    def put_CheckBoxDisabledBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(98)
    def get_CheckBoxCornerRadius(self) -> win32more.Microsoft.UI.Xaml.CornerRadius: ...
    @winrt_commethod(99)
    def put_CheckBoxCornerRadius(self, value: win32more.Microsoft.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_commethod(100)
    def get_SelectionIndicatorCornerRadius(self) -> win32more.Microsoft.UI.Xaml.CornerRadius: ...
    @winrt_commethod(101)
    def put_SelectionIndicatorCornerRadius(self, value: win32more.Microsoft.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_commethod(102)
    def get_SelectionIndicatorVisualEnabled(self) -> Boolean: ...
    @winrt_commethod(103)
    def put_SelectionIndicatorVisualEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(104)
    def get_SelectionIndicatorMode(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode: ...
    @winrt_commethod(105)
    def put_SelectionIndicatorMode(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode) -> Void: ...
    @winrt_commethod(106)
    def get_SelectionIndicatorBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(107)
    def put_SelectionIndicatorBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(108)
    def get_SelectionIndicatorPointerOverBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(109)
    def put_SelectionIndicatorPointerOverBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(110)
    def get_SelectionIndicatorPressedBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(111)
    def put_SelectionIndicatorPressedBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(112)
    def get_SelectionIndicatorDisabledBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(113)
    def put_SelectionIndicatorDisabledBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(114)
    def get_SelectedBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(115)
    def put_SelectedBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(116)
    def get_SelectedPressedBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(117)
    def put_SelectedPressedBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(118)
    def get_SelectedDisabledBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(119)
    def put_SelectedDisabledBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(120)
    def get_SelectedInnerBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(121)
    def put_SelectedInnerBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(122)
    def get_PointerOverBorderBrush(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(123)
    def put_PointerOverBorderBrush(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    CheckBoxBorderBrush = property(get_CheckBoxBorderBrush, put_CheckBoxBorderBrush)
    CheckBoxBrush = property(get_CheckBoxBrush, put_CheckBoxBrush)
    CheckBoxCornerRadius = property(get_CheckBoxCornerRadius, put_CheckBoxCornerRadius)
    CheckBoxDisabledBorderBrush = property(get_CheckBoxDisabledBorderBrush, put_CheckBoxDisabledBorderBrush)
    CheckBoxDisabledBrush = property(get_CheckBoxDisabledBrush, put_CheckBoxDisabledBrush)
    CheckBoxPointerOverBorderBrush = property(get_CheckBoxPointerOverBorderBrush, put_CheckBoxPointerOverBorderBrush)
    CheckBoxPointerOverBrush = property(get_CheckBoxPointerOverBrush, put_CheckBoxPointerOverBrush)
    CheckBoxPressedBorderBrush = property(get_CheckBoxPressedBorderBrush, put_CheckBoxPressedBorderBrush)
    CheckBoxPressedBrush = property(get_CheckBoxPressedBrush, put_CheckBoxPressedBrush)
    CheckBoxSelectedBrush = property(get_CheckBoxSelectedBrush, put_CheckBoxSelectedBrush)
    CheckBoxSelectedDisabledBrush = property(get_CheckBoxSelectedDisabledBrush, put_CheckBoxSelectedDisabledBrush)
    CheckBoxSelectedPointerOverBrush = property(get_CheckBoxSelectedPointerOverBrush, put_CheckBoxSelectedPointerOverBrush)
    CheckBoxSelectedPressedBrush = property(get_CheckBoxSelectedPressedBrush, put_CheckBoxSelectedPressedBrush)
    CheckBrush = property(get_CheckBrush, put_CheckBrush)
    CheckDisabledBrush = property(get_CheckDisabledBrush, put_CheckDisabledBrush)
    CheckHintBrush = property(get_CheckHintBrush, put_CheckHintBrush)
    CheckMode = property(get_CheckMode, put_CheckMode)
    CheckPressedBrush = property(get_CheckPressedBrush, put_CheckPressedBrush)
    CheckSelectingBrush = property(get_CheckSelectingBrush, put_CheckSelectingBrush)
    ContentMargin = property(get_ContentMargin, put_ContentMargin)
    DisabledOpacity = property(get_DisabledOpacity, put_DisabledOpacity)
    DragBackground = property(get_DragBackground, put_DragBackground)
    DragForeground = property(get_DragForeground, put_DragForeground)
    DragOpacity = property(get_DragOpacity, put_DragOpacity)
    FocusBorderBrush = property(get_FocusBorderBrush, put_FocusBorderBrush)
    FocusSecondaryBorderBrush = property(get_FocusSecondaryBorderBrush, put_FocusSecondaryBorderBrush)
    ListViewItemPresenterHorizontalContentAlignment = property(get_ListViewItemPresenterHorizontalContentAlignment, put_ListViewItemPresenterHorizontalContentAlignment)
    ListViewItemPresenterPadding = property(get_ListViewItemPresenterPadding, put_ListViewItemPresenterPadding)
    ListViewItemPresenterVerticalContentAlignment = property(get_ListViewItemPresenterVerticalContentAlignment, put_ListViewItemPresenterVerticalContentAlignment)
    PlaceholderBackground = property(get_PlaceholderBackground, put_PlaceholderBackground)
    PointerOverBackground = property(get_PointerOverBackground, put_PointerOverBackground)
    PointerOverBackgroundMargin = property(get_PointerOverBackgroundMargin, put_PointerOverBackgroundMargin)
    PointerOverBorderBrush = property(get_PointerOverBorderBrush, put_PointerOverBorderBrush)
    PointerOverForeground = property(get_PointerOverForeground, put_PointerOverForeground)
    PressedBackground = property(get_PressedBackground, put_PressedBackground)
    ReorderHintOffset = property(get_ReorderHintOffset, put_ReorderHintOffset)
    RevealBackground = property(get_RevealBackground, put_RevealBackground)
    RevealBackgroundShowsAboveContent = property(get_RevealBackgroundShowsAboveContent, put_RevealBackgroundShowsAboveContent)
    RevealBorderBrush = property(get_RevealBorderBrush, put_RevealBorderBrush)
    RevealBorderThickness = property(get_RevealBorderThickness, put_RevealBorderThickness)
    SelectedBackground = property(get_SelectedBackground, put_SelectedBackground)
    SelectedBorderBrush = property(get_SelectedBorderBrush, put_SelectedBorderBrush)
    SelectedBorderThickness = property(get_SelectedBorderThickness, put_SelectedBorderThickness)
    SelectedDisabledBackground = property(get_SelectedDisabledBackground, put_SelectedDisabledBackground)
    SelectedDisabledBorderBrush = property(get_SelectedDisabledBorderBrush, put_SelectedDisabledBorderBrush)
    SelectedForeground = property(get_SelectedForeground, put_SelectedForeground)
    SelectedInnerBorderBrush = property(get_SelectedInnerBorderBrush, put_SelectedInnerBorderBrush)
    SelectedPointerOverBackground = property(get_SelectedPointerOverBackground, put_SelectedPointerOverBackground)
    SelectedPointerOverBorderBrush = property(get_SelectedPointerOverBorderBrush, put_SelectedPointerOverBorderBrush)
    SelectedPressedBackground = property(get_SelectedPressedBackground, put_SelectedPressedBackground)
    SelectedPressedBorderBrush = property(get_SelectedPressedBorderBrush, put_SelectedPressedBorderBrush)
    SelectionCheckMarkVisualEnabled = property(get_SelectionCheckMarkVisualEnabled, put_SelectionCheckMarkVisualEnabled)
    SelectionIndicatorBrush = property(get_SelectionIndicatorBrush, put_SelectionIndicatorBrush)
    SelectionIndicatorCornerRadius = property(get_SelectionIndicatorCornerRadius, put_SelectionIndicatorCornerRadius)
    SelectionIndicatorDisabledBrush = property(get_SelectionIndicatorDisabledBrush, put_SelectionIndicatorDisabledBrush)
    SelectionIndicatorMode = property(get_SelectionIndicatorMode, put_SelectionIndicatorMode)
    SelectionIndicatorPointerOverBrush = property(get_SelectionIndicatorPointerOverBrush, put_SelectionIndicatorPointerOverBrush)
    SelectionIndicatorPressedBrush = property(get_SelectionIndicatorPressedBrush, put_SelectionIndicatorPressedBrush)
    SelectionIndicatorVisualEnabled = property(get_SelectionIndicatorVisualEnabled, put_SelectionIndicatorVisualEnabled)
class IListViewItemPresenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterFactory'
    _iid_ = Guid('{f86ac266-2740-505c-95eb-a7331b53b4a3}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenter: ...
class IListViewItemPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics'
    _iid_ = Guid('{fb0810f9-3475-593a-88a8-edbbf76fa90c}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CheckHintBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CheckSelectingBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CheckBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DragBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_DragForegroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_FocusBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_PlaceholderBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_PointerOverBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_SelectedBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_SelectedForegroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_SelectedPointerOverBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_SelectedPointerOverBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_SelectedBorderThicknessProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_DisabledOpacityProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_DragOpacityProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_ReorderHintOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_ListViewItemPresenterHorizontalContentAlignmentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(24)
    def get_ListViewItemPresenterVerticalContentAlignmentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def get_ListViewItemPresenterPaddingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(26)
    def get_PointerOverBackgroundMarginProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(27)
    def get_ContentMarginProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(28)
    def get_SelectedPressedBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(29)
    def get_PressedBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(30)
    def get_CheckBoxBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(31)
    def get_FocusSecondaryBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(32)
    def get_CheckModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(33)
    def get_PointerOverForegroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(34)
    def get_RevealBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(35)
    def get_RevealBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(36)
    def get_RevealBorderThicknessProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(37)
    def get_RevealBackgroundShowsAboveContentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(38)
    def get_SelectedDisabledBackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(39)
    def get_CheckPressedBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(40)
    def get_CheckDisabledBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(41)
    def get_CheckBoxPointerOverBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(42)
    def get_CheckBoxPressedBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(43)
    def get_CheckBoxDisabledBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(44)
    def get_CheckBoxSelectedBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(45)
    def get_CheckBoxSelectedPointerOverBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(46)
    def get_CheckBoxSelectedPressedBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(47)
    def get_CheckBoxSelectedDisabledBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(48)
    def get_CheckBoxBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(49)
    def get_CheckBoxPointerOverBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(50)
    def get_CheckBoxPressedBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(51)
    def get_CheckBoxDisabledBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(52)
    def get_CheckBoxCornerRadiusProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(53)
    def get_SelectionIndicatorCornerRadiusProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(54)
    def get_SelectionIndicatorVisualEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(55)
    def get_SelectionIndicatorModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(56)
    def get_SelectionIndicatorBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(57)
    def get_SelectionIndicatorPointerOverBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(58)
    def get_SelectionIndicatorPressedBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(59)
    def get_SelectionIndicatorDisabledBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(60)
    def get_SelectedBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(61)
    def get_SelectedPressedBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(62)
    def get_SelectedDisabledBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(63)
    def get_SelectedInnerBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(64)
    def get_PointerOverBorderBrushProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CheckBoxBorderBrushProperty = property(get_CheckBoxBorderBrushProperty, None)
    CheckBoxBrushProperty = property(get_CheckBoxBrushProperty, None)
    CheckBoxCornerRadiusProperty = property(get_CheckBoxCornerRadiusProperty, None)
    CheckBoxDisabledBorderBrushProperty = property(get_CheckBoxDisabledBorderBrushProperty, None)
    CheckBoxDisabledBrushProperty = property(get_CheckBoxDisabledBrushProperty, None)
    CheckBoxPointerOverBorderBrushProperty = property(get_CheckBoxPointerOverBorderBrushProperty, None)
    CheckBoxPointerOverBrushProperty = property(get_CheckBoxPointerOverBrushProperty, None)
    CheckBoxPressedBorderBrushProperty = property(get_CheckBoxPressedBorderBrushProperty, None)
    CheckBoxPressedBrushProperty = property(get_CheckBoxPressedBrushProperty, None)
    CheckBoxSelectedBrushProperty = property(get_CheckBoxSelectedBrushProperty, None)
    CheckBoxSelectedDisabledBrushProperty = property(get_CheckBoxSelectedDisabledBrushProperty, None)
    CheckBoxSelectedPointerOverBrushProperty = property(get_CheckBoxSelectedPointerOverBrushProperty, None)
    CheckBoxSelectedPressedBrushProperty = property(get_CheckBoxSelectedPressedBrushProperty, None)
    CheckBrushProperty = property(get_CheckBrushProperty, None)
    CheckDisabledBrushProperty = property(get_CheckDisabledBrushProperty, None)
    CheckHintBrushProperty = property(get_CheckHintBrushProperty, None)
    CheckModeProperty = property(get_CheckModeProperty, None)
    CheckPressedBrushProperty = property(get_CheckPressedBrushProperty, None)
    CheckSelectingBrushProperty = property(get_CheckSelectingBrushProperty, None)
    ContentMarginProperty = property(get_ContentMarginProperty, None)
    DisabledOpacityProperty = property(get_DisabledOpacityProperty, None)
    DragBackgroundProperty = property(get_DragBackgroundProperty, None)
    DragForegroundProperty = property(get_DragForegroundProperty, None)
    DragOpacityProperty = property(get_DragOpacityProperty, None)
    FocusBorderBrushProperty = property(get_FocusBorderBrushProperty, None)
    FocusSecondaryBorderBrushProperty = property(get_FocusSecondaryBorderBrushProperty, None)
    ListViewItemPresenterHorizontalContentAlignmentProperty = property(get_ListViewItemPresenterHorizontalContentAlignmentProperty, None)
    ListViewItemPresenterPaddingProperty = property(get_ListViewItemPresenterPaddingProperty, None)
    ListViewItemPresenterVerticalContentAlignmentProperty = property(get_ListViewItemPresenterVerticalContentAlignmentProperty, None)
    PlaceholderBackgroundProperty = property(get_PlaceholderBackgroundProperty, None)
    PointerOverBackgroundMarginProperty = property(get_PointerOverBackgroundMarginProperty, None)
    PointerOverBackgroundProperty = property(get_PointerOverBackgroundProperty, None)
    PointerOverBorderBrushProperty = property(get_PointerOverBorderBrushProperty, None)
    PointerOverForegroundProperty = property(get_PointerOverForegroundProperty, None)
    PressedBackgroundProperty = property(get_PressedBackgroundProperty, None)
    ReorderHintOffsetProperty = property(get_ReorderHintOffsetProperty, None)
    RevealBackgroundProperty = property(get_RevealBackgroundProperty, None)
    RevealBackgroundShowsAboveContentProperty = property(get_RevealBackgroundShowsAboveContentProperty, None)
    RevealBorderBrushProperty = property(get_RevealBorderBrushProperty, None)
    RevealBorderThicknessProperty = property(get_RevealBorderThicknessProperty, None)
    SelectedBackgroundProperty = property(get_SelectedBackgroundProperty, None)
    SelectedBorderBrushProperty = property(get_SelectedBorderBrushProperty, None)
    SelectedBorderThicknessProperty = property(get_SelectedBorderThicknessProperty, None)
    SelectedDisabledBackgroundProperty = property(get_SelectedDisabledBackgroundProperty, None)
    SelectedDisabledBorderBrushProperty = property(get_SelectedDisabledBorderBrushProperty, None)
    SelectedForegroundProperty = property(get_SelectedForegroundProperty, None)
    SelectedInnerBorderBrushProperty = property(get_SelectedInnerBorderBrushProperty, None)
    SelectedPointerOverBackgroundProperty = property(get_SelectedPointerOverBackgroundProperty, None)
    SelectedPointerOverBorderBrushProperty = property(get_SelectedPointerOverBorderBrushProperty, None)
    SelectedPressedBackgroundProperty = property(get_SelectedPressedBackgroundProperty, None)
    SelectedPressedBorderBrushProperty = property(get_SelectedPressedBorderBrushProperty, None)
    SelectionCheckMarkVisualEnabledProperty = property(get_SelectionCheckMarkVisualEnabledProperty, None)
    SelectionIndicatorBrushProperty = property(get_SelectionIndicatorBrushProperty, None)
    SelectionIndicatorCornerRadiusProperty = property(get_SelectionIndicatorCornerRadiusProperty, None)
    SelectionIndicatorDisabledBrushProperty = property(get_SelectionIndicatorDisabledBrushProperty, None)
    SelectionIndicatorModeProperty = property(get_SelectionIndicatorModeProperty, None)
    SelectionIndicatorPointerOverBrushProperty = property(get_SelectionIndicatorPointerOverBrushProperty, None)
    SelectionIndicatorPressedBrushProperty = property(get_SelectionIndicatorPressedBrushProperty, None)
    SelectionIndicatorVisualEnabledProperty = property(get_SelectionIndicatorVisualEnabledProperty, None)
class IListViewItemTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IListViewItemTemplateSettings'
    _iid_ = Guid('{6e302714-2955-5961-94ed-5d0c0c1d0b07}')
    @winrt_commethod(6)
    def get_DragItemsCount(self) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class ILoopingSelector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector'
    _iid_ = Guid('{077759ac-6b52-5054-bd49-9eba843cf894}')
    @winrt_commethod(6)
    def get_ShouldLoop(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ShouldLoop(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(9)
    def put_Items(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_commethod(10)
    def get_SelectedIndex(self) -> Int32: ...
    @winrt_commethod(11)
    def put_SelectedIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_SelectedItem(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(13)
    def put_SelectedItem(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(14)
    def get_ItemWidth(self) -> Int32: ...
    @winrt_commethod(15)
    def put_ItemWidth(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def get_ItemHeight(self) -> Int32: ...
    @winrt_commethod(17)
    def put_ItemHeight(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_ItemTemplate(self) -> win32more.Microsoft.UI.Xaml.DataTemplate: ...
    @winrt_commethod(19)
    def put_ItemTemplate(self, value: win32more.Microsoft.UI.Xaml.DataTemplate) -> Void: ...
    @winrt_commethod(20)
    def add_SelectionChanged(self, handler: win32more.Microsoft.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_SelectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ItemHeight = property(get_ItemHeight, put_ItemHeight)
    ItemTemplate = property(get_ItemTemplate, put_ItemTemplate)
    ItemWidth = property(get_ItemWidth, put_ItemWidth)
    Items = property(get_Items, put_Items)
    SelectedIndex = property(get_SelectedIndex, put_SelectedIndex)
    SelectedItem = property(get_SelectedItem, put_SelectedItem)
    ShouldLoop = property(get_ShouldLoop, put_ShouldLoop)
    SelectionChanged = event()
class ILoopingSelectorItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorItem'
    _iid_ = Guid('{75d36595-bf4f-5393-819f-eb1e321ce1dc}')
class ILoopingSelectorPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorPanel'
    _iid_ = Guid('{7479c3a4-c5b1-5112-bea9-beef5cc79f57}')
class ILoopingSelectorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics'
    _iid_ = Guid('{e7f8770e-729b-57aa-9a79-ede3f84253cc}')
    @winrt_commethod(6)
    def get_ShouldLoopProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ItemsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_SelectedIndexProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_SelectedItemProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ItemWidthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ItemHeightProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_ItemTemplateProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ItemHeightProperty = property(get_ItemHeightProperty, None)
    ItemTemplateProperty = property(get_ItemTemplateProperty, None)
    ItemWidthProperty = property(get_ItemWidthProperty, None)
    ItemsProperty = property(get_ItemsProperty, None)
    SelectedIndexProperty = property(get_SelectedIndexProperty, None)
    SelectedItemProperty = property(get_SelectedItemProperty, None)
    ShouldLoopProperty = property(get_ShouldLoopProperty, None)
class IMenuFlyoutItemTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IMenuFlyoutItemTemplateSettings'
    _iid_ = Guid('{fa7b8b1f-020d-58ec-8658-f2ce97310051}')
    @winrt_commethod(6)
    def get_KeyboardAcceleratorTextMinWidth(self) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class IMenuFlyoutPresenterTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings'
    _iid_ = Guid('{2bfcfa7e-483c-5fc9-b070-fbb58e6e974d}')
    @winrt_commethod(6)
    def get_FlyoutContentMinWidth(self) -> Double: ...
    FlyoutContentMinWidth = property(get_FlyoutContentMinWidth, None)
class IMonochromaticOverlayPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenter'
    _iid_ = Guid('{3f0d1e92-5450-5078-8f72-5ac1749976e3}')
    @winrt_commethod(6)
    def get_SourceElement(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_SourceElement(self, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_ReplacementColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_ReplacementColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    ReplacementColor = property(get_ReplacementColor, put_ReplacementColor)
    SourceElement = property(get_SourceElement, put_SourceElement)
class IMonochromaticOverlayPresenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenterFactory'
    _iid_ = Guid('{4997847b-b558-5c8c-8298-be1532e898ec}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.MonochromaticOverlayPresenter: ...
class IMonochromaticOverlayPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenterStatics'
    _iid_ = Guid('{a931bf94-a9c6-5d10-83ac-1492739e11e4}')
    @winrt_commethod(6)
    def get_SourceElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ReplacementColorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ReplacementColorProperty = property(get_ReplacementColorProperty, None)
    SourceElementProperty = property(get_SourceElementProperty, None)
class INavigationViewItemPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter'
    _iid_ = Guid('{64939df5-760c-5b0b-af4d-d8dd4ee50278}')
    @winrt_commethod(6)
    def get_Icon(self) -> win32more.Microsoft.UI.Xaml.Controls.IconElement: ...
    @winrt_commethod(7)
    def put_Icon(self, value: win32more.Microsoft.UI.Xaml.Controls.IconElement) -> Void: ...
    @winrt_commethod(8)
    def get_TemplateSettings(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenterTemplateSettings: ...
    Icon = property(get_Icon, put_Icon)
    TemplateSettings = property(get_TemplateSettings, None)
class INavigationViewItemPresenter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter2'
    _iid_ = Guid('{3f775730-3713-5b3b-9600-53b79fff2e35}')
    @winrt_commethod(6)
    def get_InfoBadge(self) -> win32more.Microsoft.UI.Xaml.Controls.InfoBadge: ...
    @winrt_commethod(7)
    def put_InfoBadge(self, value: win32more.Microsoft.UI.Xaml.Controls.InfoBadge) -> Void: ...
    InfoBadge = property(get_InfoBadge, put_InfoBadge)
class INavigationViewItemPresenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterFactory'
    _iid_ = Guid('{b28b0160-022c-593c-ab9a-7b3ded2c0754}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter: ...
class INavigationViewItemPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterStatics'
    _iid_ = Guid('{3b07f068-a764-549c-b4cf-ebab40ec5dd1}')
    @winrt_commethod(6)
    def get_IconProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TemplateSettingsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IconProperty = property(get_IconProperty, None)
    TemplateSettingsProperty = property(get_TemplateSettingsProperty, None)
class INavigationViewItemPresenterStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterStatics2'
    _iid_ = Guid('{4b473f61-3f17-5e4f-8453-541df947a789}')
    @winrt_commethod(6)
    def get_InfoBadgeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    InfoBadgeProperty = property(get_InfoBadgeProperty, None)
class INavigationViewItemPresenterTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettings'
    _iid_ = Guid('{a5119750-fa71-56f2-bfa4-799d9f304cb8}')
    @winrt_commethod(6)
    def get_IconWidth(self) -> Double: ...
    @winrt_commethod(7)
    def get_SmallerIconWidth(self) -> Double: ...
    IconWidth = property(get_IconWidth, None)
    SmallerIconWidth = property(get_SmallerIconWidth, None)
class INavigationViewItemPresenterTemplateSettingsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettingsFactory'
    _iid_ = Guid('{19ef1328-52c7-55e3-b1bb-923f2f39bd6e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenterTemplateSettings: ...
class INavigationViewItemPresenterTemplateSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettingsStatics'
    _iid_ = Guid('{72f09642-c658-5b06-8c81-1566b737b746}')
    @winrt_commethod(6)
    def get_IconWidthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SmallerIconWidthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IconWidthProperty = property(get_IconWidthProperty, None)
    SmallerIconWidthProperty = property(get_SmallerIconWidthProperty, None)
class IOrientedVirtualizingPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel'
    _iid_ = Guid('{450d2984-1e70-53d8-8269-a27564daa69f}')
    @winrt_commethod(6)
    def get_CanVerticallyScroll(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanVerticallyScroll(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CanHorizontallyScroll(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CanHorizontallyScroll(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ExtentWidth(self) -> Double: ...
    @winrt_commethod(11)
    def get_ExtentHeight(self) -> Double: ...
    @winrt_commethod(12)
    def get_ViewportWidth(self) -> Double: ...
    @winrt_commethod(13)
    def get_ViewportHeight(self) -> Double: ...
    @winrt_commethod(14)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(15)
    def get_VerticalOffset(self) -> Double: ...
    @winrt_commethod(16)
    def get_ScrollOwner(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(17)
    def put_ScrollOwner(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(18)
    def LineUp(self) -> Void: ...
    @winrt_commethod(19)
    def LineDown(self) -> Void: ...
    @winrt_commethod(20)
    def LineLeft(self) -> Void: ...
    @winrt_commethod(21)
    def LineRight(self) -> Void: ...
    @winrt_commethod(22)
    def PageUp(self) -> Void: ...
    @winrt_commethod(23)
    def PageDown(self) -> Void: ...
    @winrt_commethod(24)
    def PageLeft(self) -> Void: ...
    @winrt_commethod(25)
    def PageRight(self) -> Void: ...
    @winrt_commethod(26)
    def MouseWheelUp(self) -> Void: ...
    @winrt_commethod(27)
    def MouseWheelDown(self) -> Void: ...
    @winrt_commethod(28)
    def MouseWheelLeft(self) -> Void: ...
    @winrt_commethod(29)
    def MouseWheelRight(self) -> Void: ...
    @winrt_commethod(30)
    def SetHorizontalOffset(self, offset: Double) -> Void: ...
    @winrt_commethod(31)
    def SetVerticalOffset(self, offset: Double) -> Void: ...
    @winrt_commethod(32)
    def MakeVisible(self, visual: win32more.Microsoft.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    CanHorizontallyScroll = property(get_CanHorizontallyScroll, put_CanHorizontallyScroll)
    CanVerticallyScroll = property(get_CanVerticallyScroll, put_CanVerticallyScroll)
    ExtentHeight = property(get_ExtentHeight, None)
    ExtentWidth = property(get_ExtentWidth, None)
    HorizontalOffset = property(get_HorizontalOffset, None)
    ScrollOwner = property(get_ScrollOwner, put_ScrollOwner)
    VerticalOffset = property(get_VerticalOffset, None)
    ViewportHeight = property(get_ViewportHeight, None)
    ViewportWidth = property(get_ViewportWidth, None)
class IOrientedVirtualizingPanelFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanelFactory'
    _iid_ = Guid('{a70c98f4-d671-5f46-9b01-28b1b5528fc0}')
class IPickerFlyoutBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBase'
    _iid_ = Guid('{8c2cc030-14fe-5fca-8ce3-e11a918632cc}')
class IPickerFlyoutBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseFactory'
    _iid_ = Guid('{8231dab5-4b8b-5674-b273-1c66701c14e1}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PickerFlyoutBase: ...
class IPickerFlyoutBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseOverrides'
    _iid_ = Guid('{5b090ffc-d423-5756-a01c-aa734579d856}')
    @winrt_commethod(6)
    def OnConfirmed(self) -> Void: ...
    @winrt_commethod(7)
    def ShouldShowConfirmationButtons(self) -> Boolean: ...
class IPickerFlyoutBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics'
    _iid_ = Guid('{0e414dc2-38e0-5efe-bae8-a0c6a78514c8}')
    @winrt_commethod(6)
    def get_TitleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetTitle(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetTitle(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    TitleProperty = property(get_TitleProperty, None)
class IPivotHeaderItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPivotHeaderItem'
    _iid_ = Guid('{612d6f77-6c76-5239-8894-efbab0f53e3e}')
class IPivotHeaderItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPivotHeaderItemFactory'
    _iid_ = Guid('{d8db1a66-1384-518d-bc8f-9edc2ca79190}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PivotHeaderItem: ...
class IPivotHeaderPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPivotHeaderPanel'
    _iid_ = Guid('{b5af5bed-5f2f-5af6-bf17-c085531c880f}')
class IPivotPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPivotPanel'
    _iid_ = Guid('{8e66cdcf-3bf5-5fe0-b05b-1125e961f0cc}')
class IPopup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPopup'
    _iid_ = Guid('{4e3ab19d-2f95-579c-9535-906c58629437}')
    @winrt_commethod(6)
    def get_Child(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_Child(self, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def get_IsOpen(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsOpen(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(11)
    def put_HorizontalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_VerticalOffset(self) -> Double: ...
    @winrt_commethod(13)
    def put_VerticalOffset(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_ChildTransitions(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_commethod(15)
    def put_ChildTransitions(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_commethod(16)
    def get_IsLightDismissEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsLightDismissEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_LightDismissOverlayMode(self) -> win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_commethod(19)
    def put_LightDismissOverlayMode(self, value: win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    @winrt_commethod(20)
    def get_ShouldConstrainToRootBounds(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_ShouldConstrainToRootBounds(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_IsConstrainedToRootBounds(self) -> Boolean: ...
    @winrt_commethod(23)
    def add_Opened(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_Opened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_Closed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Child = property(get_Child, put_Child)
    ChildTransitions = property(get_ChildTransitions, put_ChildTransitions)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    IsConstrainedToRootBounds = property(get_IsConstrainedToRootBounds, None)
    IsLightDismissEnabled = property(get_IsLightDismissEnabled, put_IsLightDismissEnabled)
    IsOpen = property(get_IsOpen, put_IsOpen)
    LightDismissOverlayMode = property(get_LightDismissOverlayMode, put_LightDismissOverlayMode)
    ShouldConstrainToRootBounds = property(get_ShouldConstrainToRootBounds, put_ShouldConstrainToRootBounds)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    Opened = event()
    Closed = event()
class IPopup2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPopup2'
    _iid_ = Guid('{ea9c4f43-a937-53d5-b665-6640ad7ec2f4}')
    @winrt_commethod(6)
    def get_PlacementTarget(self) -> win32more.Microsoft.UI.Xaml.FrameworkElement: ...
    @winrt_commethod(7)
    def put_PlacementTarget(self, value: win32more.Microsoft.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredPlacement(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_commethod(9)
    def put_DesiredPlacement(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode) -> Void: ...
    @winrt_commethod(10)
    def get_ActualPlacement(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_commethod(11)
    def add_ActualPlacementChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ActualPlacementChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ActualPlacement = property(get_ActualPlacement, None)
    DesiredPlacement = property(get_DesiredPlacement, put_DesiredPlacement)
    PlacementTarget = property(get_PlacementTarget, put_PlacementTarget)
    ActualPlacementChanged = event()
class IPopup3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPopup3'
    _iid_ = Guid('{03736c25-dd36-5344-9a8d-3f4e8e616cba}')
    @winrt_commethod(6)
    def get_SystemBackdrop(self) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_commethod(7)
    def put_SystemBackdrop(self, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
class IPopupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics'
    _iid_ = Guid('{c1acfaa4-209a-5fb8-8934-8825976769b8}')
    @winrt_commethod(6)
    def get_ChildProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsOpenProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_HorizontalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_VerticalOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ChildTransitionsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_IsLightDismissEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_LightDismissOverlayModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ShouldConstrainToRootBoundsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ChildProperty = property(get_ChildProperty, None)
    ChildTransitionsProperty = property(get_ChildTransitionsProperty, None)
    HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    IsLightDismissEnabledProperty = property(get_IsLightDismissEnabledProperty, None)
    IsOpenProperty = property(get_IsOpenProperty, None)
    LightDismissOverlayModeProperty = property(get_LightDismissOverlayModeProperty, None)
    ShouldConstrainToRootBoundsProperty = property(get_ShouldConstrainToRootBoundsProperty, None)
    VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class IPopupStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics2'
    _iid_ = Guid('{79b3285a-1330-5cfd-af2f-88efa00770a9}')
    @winrt_commethod(6)
    def get_PlacementTargetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_DesiredPlacementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DesiredPlacementProperty = property(get_DesiredPlacementProperty, None)
    PlacementTargetProperty = property(get_PlacementTargetProperty, None)
class IPopupStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics3'
    _iid_ = Guid('{2409656d-84f9-5979-8adf-f3db71530b22}')
    @winrt_commethod(6)
    def get_SystemBackdropProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    SystemBackdropProperty = property(get_SystemBackdropProperty, None)
class IRangeBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRangeBase'
    _iid_ = Guid('{540d6d61-8fac-5d5c-b5b0-e172a7dde103}')
    @winrt_commethod(6)
    def get_Minimum(self) -> Double: ...
    @winrt_commethod(7)
    def put_Minimum(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Maximum(self) -> Double: ...
    @winrt_commethod(9)
    def put_Maximum(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_SmallChange(self) -> Double: ...
    @winrt_commethod(11)
    def put_SmallChange(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_LargeChange(self) -> Double: ...
    @winrt_commethod(13)
    def put_LargeChange(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_Value(self) -> Double: ...
    @winrt_commethod(15)
    def put_Value(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def add_ValueChanged(self, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ValueChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    LargeChange = property(get_LargeChange, put_LargeChange)
    Maximum = property(get_Maximum, put_Maximum)
    Minimum = property(get_Minimum, put_Minimum)
    SmallChange = property(get_SmallChange, put_SmallChange)
    Value = property(get_Value, put_Value)
    ValueChanged = event()
class IRangeBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseFactory'
    _iid_ = Guid('{41c205e2-4422-5dca-9b49-e31210ea396c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBase: ...
class IRangeBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseOverrides'
    _iid_ = Guid('{b3deb76f-68a6-5c14-a824-ab58e8774745}')
    @winrt_commethod(6)
    def OnMinimumChanged(self, oldMinimum: Double, newMinimum: Double) -> Void: ...
    @winrt_commethod(7)
    def OnMaximumChanged(self, oldMaximum: Double, newMaximum: Double) -> Void: ...
    @winrt_commethod(8)
    def OnValueChanged(self, oldValue: Double, newValue: Double) -> Void: ...
class IRangeBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseStatics'
    _iid_ = Guid('{4aed5e49-64ec-56f1-874d-b8c0f83f9ac8}')
    @winrt_commethod(6)
    def get_MinimumProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MaximumProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_SmallChangeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_LargeChangeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    LargeChangeProperty = property(get_LargeChangeProperty, None)
    MaximumProperty = property(get_MaximumProperty, None)
    MinimumProperty = property(get_MinimumProperty, None)
    SmallChangeProperty = property(get_SmallChangeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IRangeBaseValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs'
    _iid_ = Guid('{b0181692-9578-51c7-9d1c-adfcf8945aa9}')
    @winrt_commethod(6)
    def get_OldValue(self) -> Double: ...
    @winrt_commethod(7)
    def get_NewValue(self) -> Double: ...
    NewValue = property(get_NewValue, None)
    OldValue = property(get_OldValue, None)
class IRepeatButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRepeatButton'
    _iid_ = Guid('{97f4c728-4a94-56b5-91e4-e7c6f6a1251a}')
    @winrt_commethod(6)
    def get_Delay(self) -> Int32: ...
    @winrt_commethod(7)
    def put_Delay(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Interval(self) -> Int32: ...
    @winrt_commethod(9)
    def put_Interval(self, value: Int32) -> Void: ...
    Delay = property(get_Delay, put_Delay)
    Interval = property(get_Interval, put_Interval)
class IRepeatButtonStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRepeatButtonStatics'
    _iid_ = Guid('{b57320f6-a58a-589c-9f41-aab02f51e829}')
    @winrt_commethod(6)
    def get_DelayProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IntervalProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DelayProperty = property(get_DelayProperty, None)
    IntervalProperty = property(get_IntervalProperty, None)
class IRepeatedScrollSnapPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPoint'
    _iid_ = Guid('{5828fb51-8ebb-596d-a871-50063479362d}')
    @winrt_commethod(6)
    def get_Offset(self) -> Double: ...
    @winrt_commethod(7)
    def get_Interval(self) -> Double: ...
    @winrt_commethod(8)
    def get_Start(self) -> Double: ...
    @winrt_commethod(9)
    def get_End(self) -> Double: ...
    End = property(get_End, None)
    Interval = property(get_Interval, None)
    Offset = property(get_Offset, None)
    Start = property(get_Start, None)
class IRepeatedScrollSnapPointFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPointFactory'
    _iid_ = Guid('{f2fd8403-679e-5c31-b431-72a0e0014e6a}')
    @winrt_commethod(6)
    def CreateInstance(self, offset: Double, interval: Double, start: Double, end: Double, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatedScrollSnapPoint: ...
class IRepeatedZoomSnapPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPoint'
    _iid_ = Guid('{1fa6dbbe-5e11-5d32-873b-c92b1d171538}')
    @winrt_commethod(6)
    def get_Offset(self) -> Double: ...
    @winrt_commethod(7)
    def get_Interval(self) -> Double: ...
    @winrt_commethod(8)
    def get_Start(self) -> Double: ...
    @winrt_commethod(9)
    def get_End(self) -> Double: ...
    End = property(get_End, None)
    Interval = property(get_Interval, None)
    Offset = property(get_Offset, None)
    Start = property(get_Start, None)
class IRepeatedZoomSnapPointFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPointFactory'
    _iid_ = Guid('{7d032a7c-d91c-5660-b1c2-b36e8810ac65}')
    @winrt_commethod(6)
    def CreateInstance(self, offset: Double, interval: Double, start: Double, end: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatedZoomSnapPoint: ...
class IScrollBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollBar'
    _iid_ = Guid('{568cbf41-f741-5f05-8e08-c0a50ac17c8c}')
    @winrt_commethod(6)
    def get_Orientation(self) -> win32more.Microsoft.UI.Xaml.Controls.Orientation: ...
    @winrt_commethod(7)
    def put_Orientation(self, value: win32more.Microsoft.UI.Xaml.Controls.Orientation) -> Void: ...
    @winrt_commethod(8)
    def get_ViewportSize(self) -> Double: ...
    @winrt_commethod(9)
    def put_ViewportSize(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_IndicatorMode(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode: ...
    @winrt_commethod(11)
    def put_IndicatorMode(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode) -> Void: ...
    @winrt_commethod(12)
    def add_Scroll(self, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Scroll(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IndicatorMode = property(get_IndicatorMode, put_IndicatorMode)
    Orientation = property(get_Orientation, put_Orientation)
    ViewportSize = property(get_ViewportSize, put_ViewportSize)
    Scroll = event()
class IScrollBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollBarStatics'
    _iid_ = Guid('{88b52e18-9528-579f-bd84-eba585a01c7a}')
    @winrt_commethod(6)
    def get_OrientationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ViewportSizeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IndicatorModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IndicatorModeProperty = property(get_IndicatorModeProperty, None)
    OrientationProperty = property(get_OrientationProperty, None)
    ViewportSizeProperty = property(get_ViewportSizeProperty, None)
class IScrollController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollController'
    _iid_ = Guid('{54396786-1726-53d6-97a3-40af0838314c}')
    @winrt_commethod(6)
    def get_PanningInfo(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanningInfo: ...
    @winrt_commethod(7)
    def get_CanScroll(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsScrollingWithMouse(self) -> Boolean: ...
    @winrt_commethod(9)
    def SetIsScrollable(self, isScrollable: Boolean) -> Void: ...
    @winrt_commethod(10)
    def SetValues(self, minOffset: Double, maxOffset: Double, offset: Double, viewportLength: Double) -> Void: ...
    @winrt_commethod(11)
    def GetScrollAnimation(self, correlationId: Int32, startPosition: win32more.Windows.Foundation.Numerics.Vector2, endPosition: win32more.Windows.Foundation.Numerics.Vector2, defaultAnimation: win32more.Microsoft.UI.Composition.CompositionAnimation) -> win32more.Microsoft.UI.Composition.CompositionAnimation: ...
    @winrt_commethod(12)
    def NotifyRequestedScrollCompleted(self, correlationId: Int32) -> Void: ...
    @winrt_commethod(13)
    def add_CanScrollChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_CanScrollChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_IsScrollingWithMouseChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_IsScrollingWithMouseChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_ScrollToRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController, win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollToRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ScrollToRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_ScrollByRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController, win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollByRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_ScrollByRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_AddScrollVelocityRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController, win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerAddScrollVelocityRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_AddScrollVelocityRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CanScroll = property(get_CanScroll, None)
    IsScrollingWithMouse = property(get_IsScrollingWithMouse, None)
    PanningInfo = property(get_PanningInfo, None)
    CanScrollChanged = event()
    IsScrollingWithMouseChanged = event()
    ScrollToRequested = event()
    ScrollByRequested = event()
    AddScrollVelocityRequested = event()
class IScrollControllerAddScrollVelocityRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgs'
    _iid_ = Guid('{317bbc1a-0cf7-5815-a8a7-bd7e6eef966a}')
    @winrt_commethod(6)
    def get_OffsetVelocity(self) -> Single: ...
    @winrt_commethod(7)
    def get_InertiaDecayRate(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(8)
    def get_CorrelationId(self) -> Int32: ...
    @winrt_commethod(9)
    def put_CorrelationId(self, value: Int32) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    InertiaDecayRate = property(get_InertiaDecayRate, None)
    OffsetVelocity = property(get_OffsetVelocity, None)
class IScrollControllerAddScrollVelocityRequestedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgsFactory'
    _iid_ = Guid('{9221d193-6f82-5e21-aacc-0b1460818ab5}')
    @winrt_commethod(6)
    def CreateInstance(self, offsetVelocity: Single, inertiaDecayRate: win32more.Windows.Foundation.IReference[Single]) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerAddScrollVelocityRequestedEventArgs: ...
class IScrollControllerPanRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanRequestedEventArgs'
    _iid_ = Guid('{beee064e-1d4d-5a1a-8781-acf1587a5d6a}')
    @winrt_commethod(6)
    def get_PointerPoint(self) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    PointerPoint = property(get_PointerPoint, None)
class IScrollControllerPanRequestedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanRequestedEventArgsFactory'
    _iid_ = Guid('{c3b0a6c1-6732-5832-be50-4ecade585cbc}')
    @winrt_commethod(6)
    def CreateInstance(self, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerPanRequestedEventArgs: ...
class IScrollControllerPanningInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanningInfo'
    _iid_ = Guid('{53d5b301-9aab-59bc-92cd-42cf21abd590}')
    @winrt_commethod(6)
    def get_IsRailEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_PanOrientation(self) -> win32more.Microsoft.UI.Xaml.Controls.Orientation: ...
    @winrt_commethod(8)
    def get_PanningElementAncestor(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def SetPanningElementExpressionAnimationSources(self, propertySet: win32more.Microsoft.UI.Composition.CompositionPropertySet, minOffsetPropertyName: WinRT_String, maxOffsetPropertyName: WinRT_String, offsetPropertyName: WinRT_String, multiplierPropertyName: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanningInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PanRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanningInfo, win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerPanRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PanRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsRailEnabled = property(get_IsRailEnabled, None)
    PanOrientation = property(get_PanOrientation, None)
    PanningElementAncestor = property(get_PanningElementAncestor, None)
    Changed = event()
    PanRequested = event()
class IScrollControllerScrollByRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgs'
    _iid_ = Guid('{e7f305fa-4073-5d88-8bf1-ae4ecb9208bf}')
    @winrt_commethod(6)
    def get_OffsetDelta(self) -> Double: ...
    @winrt_commethod(7)
    def get_Options(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions: ...
    @winrt_commethod(8)
    def get_CorrelationId(self) -> Int32: ...
    @winrt_commethod(9)
    def put_CorrelationId(self, value: Int32) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    OffsetDelta = property(get_OffsetDelta, None)
    Options = property(get_Options, None)
class IScrollControllerScrollByRequestedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgsFactory'
    _iid_ = Guid('{7ecf01a7-ef3f-5af9-93b4-38bc1bafd335}')
    @winrt_commethod(6)
    def CreateInstance(self, offsetDelta: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollByRequestedEventArgs: ...
class IScrollControllerScrollToRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgs'
    _iid_ = Guid('{73f16b99-7310-5c73-872b-276e5a9d4913}')
    @winrt_commethod(6)
    def get_Offset(self) -> Double: ...
    @winrt_commethod(7)
    def get_Options(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions: ...
    @winrt_commethod(8)
    def get_CorrelationId(self) -> Int32: ...
    @winrt_commethod(9)
    def put_CorrelationId(self, value: Int32) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    Offset = property(get_Offset, None)
    Options = property(get_Options, None)
class IScrollControllerScrollToRequestedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgsFactory'
    _iid_ = Guid('{01675dc4-1074-54e8-bebb-66b03a33da0d}')
    @winrt_commethod(6)
    def CreateInstance(self, offset: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollToRequestedEventArgs: ...
class IScrollEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollEventArgs'
    _iid_ = Guid('{dbd27f11-f937-5ad0-9f75-b962c33254cf}')
    @winrt_commethod(6)
    def get_NewValue(self) -> Double: ...
    @winrt_commethod(7)
    def get_ScrollEventType(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventType: ...
    NewValue = property(get_NewValue, None)
    ScrollEventType = property(get_ScrollEventType, None)
class IScrollPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter'
    _iid_ = Guid('{424b8afd-f7aa-5e5b-9d0b-5f0ea4e1a56e}')
    @winrt_commethod(6)
    def get_Background(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Background(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Content(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Content(self, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def get_ExpressionAnimationSources(self) -> win32more.Microsoft.UI.Composition.CompositionPropertySet: ...
    @winrt_commethod(11)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(12)
    def get_VerticalOffset(self) -> Double: ...
    @winrt_commethod(13)
    def get_ZoomFactor(self) -> Single: ...
    @winrt_commethod(14)
    def get_ExtentWidth(self) -> Double: ...
    @winrt_commethod(15)
    def get_ExtentHeight(self) -> Double: ...
    @winrt_commethod(16)
    def get_ViewportWidth(self) -> Double: ...
    @winrt_commethod(17)
    def get_ViewportHeight(self) -> Double: ...
    @winrt_commethod(18)
    def get_ScrollableWidth(self) -> Double: ...
    @winrt_commethod(19)
    def get_ScrollableHeight(self) -> Double: ...
    @winrt_commethod(20)
    def get_ContentOrientation(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingContentOrientation: ...
    @winrt_commethod(21)
    def put_ContentOrientation(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingContentOrientation) -> Void: ...
    @winrt_commethod(22)
    def get_HorizontalScrollChainMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode: ...
    @winrt_commethod(23)
    def put_HorizontalScrollChainMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode) -> Void: ...
    @winrt_commethod(24)
    def get_VerticalScrollChainMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode: ...
    @winrt_commethod(25)
    def put_VerticalScrollChainMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode) -> Void: ...
    @winrt_commethod(26)
    def get_HorizontalScrollRailMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode: ...
    @winrt_commethod(27)
    def put_HorizontalScrollRailMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode) -> Void: ...
    @winrt_commethod(28)
    def get_VerticalScrollRailMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode: ...
    @winrt_commethod(29)
    def put_VerticalScrollRailMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode) -> Void: ...
    @winrt_commethod(30)
    def get_HorizontalScrollMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_commethod(31)
    def put_HorizontalScrollMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode) -> Void: ...
    @winrt_commethod(32)
    def get_VerticalScrollMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_commethod(33)
    def put_VerticalScrollMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode) -> Void: ...
    @winrt_commethod(34)
    def get_ComputedHorizontalScrollMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_commethod(35)
    def get_ComputedVerticalScrollMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_commethod(36)
    def get_ZoomChainMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode: ...
    @winrt_commethod(37)
    def put_ZoomChainMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode) -> Void: ...
    @winrt_commethod(38)
    def get_ZoomMode(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomMode: ...
    @winrt_commethod(39)
    def put_ZoomMode(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomMode) -> Void: ...
    @winrt_commethod(40)
    def get_IgnoredInputKinds(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingInputKinds: ...
    @winrt_commethod(41)
    def put_IgnoredInputKinds(self, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingInputKinds) -> Void: ...
    @winrt_commethod(42)
    def get_MinZoomFactor(self) -> Double: ...
    @winrt_commethod(43)
    def put_MinZoomFactor(self, value: Double) -> Void: ...
    @winrt_commethod(44)
    def get_MaxZoomFactor(self) -> Double: ...
    @winrt_commethod(45)
    def put_MaxZoomFactor(self, value: Double) -> Void: ...
    @winrt_commethod(46)
    def get_State(self) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingInteractionState: ...
    @winrt_commethod(47)
    def get_HorizontalScrollController(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController: ...
    @winrt_commethod(48)
    def put_HorizontalScrollController(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController) -> Void: ...
    @winrt_commethod(49)
    def get_VerticalScrollController(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController: ...
    @winrt_commethod(50)
    def put_VerticalScrollController(self, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController) -> Void: ...
    @winrt_commethod(51)
    def get_HorizontalAnchorRatio(self) -> Double: ...
    @winrt_commethod(52)
    def put_HorizontalAnchorRatio(self, value: Double) -> Void: ...
    @winrt_commethod(53)
    def get_VerticalAnchorRatio(self) -> Double: ...
    @winrt_commethod(54)
    def put_VerticalAnchorRatio(self, value: Double) -> Void: ...
    @winrt_commethod(55)
    def get_HorizontalSnapPoints(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointBase]: ...
    @winrt_commethod(56)
    def get_VerticalSnapPoints(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointBase]: ...
    @winrt_commethod(57)
    def get_ZoomSnapPoints(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPointBase]: ...
    @winrt_commethod(58)
    def ScrollTo(self, horizontalOffset: Double, verticalOffset: Double) -> Int32: ...
    @winrt_commethod(59)
    def ScrollToWithOptions(self, horizontalOffset: Double, verticalOffset: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> Int32: ...
    @winrt_commethod(60)
    def ScrollBy(self, horizontalOffsetDelta: Double, verticalOffsetDelta: Double) -> Int32: ...
    @winrt_commethod(61)
    def ScrollByWithOptions(self, horizontalOffsetDelta: Double, verticalOffsetDelta: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> Int32: ...
    @winrt_commethod(62)
    def AddScrollVelocity(self, offsetsVelocity: win32more.Windows.Foundation.Numerics.Vector2, inertiaDecayRate: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Int32: ...
    @winrt_commethod(63)
    def ZoomTo(self, zoomFactor: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Int32: ...
    @winrt_commethod(64)
    def ZoomToWithOptions(self, zoomFactor: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2], options: win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomOptions) -> Int32: ...
    @winrt_commethod(65)
    def ZoomBy(self, zoomFactorDelta: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Int32: ...
    @winrt_commethod(66)
    def ZoomByWithOptions(self, zoomFactorDelta: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2], options: win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomOptions) -> Int32: ...
    @winrt_commethod(67)
    def AddZoomVelocity(self, zoomFactorVelocity: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2], inertiaDecayRate: win32more.Windows.Foundation.IReference[Single]) -> Int32: ...
    @winrt_commethod(68)
    def add_ExtentChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(69)
    def remove_ExtentChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(70)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(71)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(72)
    def add_ViewChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(73)
    def remove_ViewChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(74)
    def add_ScrollAnimationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(75)
    def remove_ScrollAnimationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(76)
    def add_ZoomAnimationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(77)
    def remove_ZoomAnimationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(78)
    def add_ScrollCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(79)
    def remove_ScrollCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(80)
    def add_ZoomCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(81)
    def remove_ZoomCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(82)
    def add_BringingIntoView(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingBringingIntoViewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(83)
    def remove_BringingIntoView(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(84)
    def add_AnchorRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingAnchorRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(85)
    def remove_AnchorRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Background = property(get_Background, put_Background)
    ComputedHorizontalScrollMode = property(get_ComputedHorizontalScrollMode, None)
    ComputedVerticalScrollMode = property(get_ComputedVerticalScrollMode, None)
    Content = property(get_Content, put_Content)
    ContentOrientation = property(get_ContentOrientation, put_ContentOrientation)
    ExpressionAnimationSources = property(get_ExpressionAnimationSources, None)
    ExtentHeight = property(get_ExtentHeight, None)
    ExtentWidth = property(get_ExtentWidth, None)
    HorizontalAnchorRatio = property(get_HorizontalAnchorRatio, put_HorizontalAnchorRatio)
    HorizontalOffset = property(get_HorizontalOffset, None)
    HorizontalScrollChainMode = property(get_HorizontalScrollChainMode, put_HorizontalScrollChainMode)
    HorizontalScrollController = property(get_HorizontalScrollController, put_HorizontalScrollController)
    HorizontalScrollMode = property(get_HorizontalScrollMode, put_HorizontalScrollMode)
    HorizontalScrollRailMode = property(get_HorizontalScrollRailMode, put_HorizontalScrollRailMode)
    HorizontalSnapPoints = property(get_HorizontalSnapPoints, None)
    IgnoredInputKinds = property(get_IgnoredInputKinds, put_IgnoredInputKinds)
    MaxZoomFactor = property(get_MaxZoomFactor, put_MaxZoomFactor)
    MinZoomFactor = property(get_MinZoomFactor, put_MinZoomFactor)
    ScrollableHeight = property(get_ScrollableHeight, None)
    ScrollableWidth = property(get_ScrollableWidth, None)
    State = property(get_State, None)
    VerticalAnchorRatio = property(get_VerticalAnchorRatio, put_VerticalAnchorRatio)
    VerticalOffset = property(get_VerticalOffset, None)
    VerticalScrollChainMode = property(get_VerticalScrollChainMode, put_VerticalScrollChainMode)
    VerticalScrollController = property(get_VerticalScrollController, put_VerticalScrollController)
    VerticalScrollMode = property(get_VerticalScrollMode, put_VerticalScrollMode)
    VerticalScrollRailMode = property(get_VerticalScrollRailMode, put_VerticalScrollRailMode)
    VerticalSnapPoints = property(get_VerticalSnapPoints, None)
    ViewportHeight = property(get_ViewportHeight, None)
    ViewportWidth = property(get_ViewportWidth, None)
    ZoomChainMode = property(get_ZoomChainMode, put_ZoomChainMode)
    ZoomFactor = property(get_ZoomFactor, None)
    ZoomMode = property(get_ZoomMode, put_ZoomMode)
    ZoomSnapPoints = property(get_ZoomSnapPoints, None)
    ExtentChanged = event()
    StateChanged = event()
    ViewChanged = event()
    ScrollAnimationStarting = event()
    ZoomAnimationStarting = event()
    ScrollCompleted = event()
    ZoomCompleted = event()
    BringingIntoView = event()
    AnchorRequested = event()
class IScrollPresenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterFactory'
    _iid_ = Guid('{9f5cdc57-d229-52b2-aee4-37c496764ea3}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter: ...
class IScrollPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics'
    _iid_ = Guid('{e27ba947-f8a5-5869-9a71-cd514d41c623}')
    @winrt_commethod(6)
    def get_BackgroundProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ContentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ContentOrientationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_HorizontalScrollChainModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_VerticalScrollChainModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_HorizontalScrollRailModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_VerticalScrollRailModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_HorizontalScrollModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_VerticalScrollModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ComputedHorizontalScrollModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_ComputedVerticalScrollModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_ZoomChainModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_ZoomModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_IgnoredInputKindsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_MinZoomFactorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_MaxZoomFactorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_HorizontalAnchorRatioProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_VerticalAnchorRatioProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    BackgroundProperty = property(get_BackgroundProperty, None)
    ComputedHorizontalScrollModeProperty = property(get_ComputedHorizontalScrollModeProperty, None)
    ComputedVerticalScrollModeProperty = property(get_ComputedVerticalScrollModeProperty, None)
    ContentOrientationProperty = property(get_ContentOrientationProperty, None)
    ContentProperty = property(get_ContentProperty, None)
    HorizontalAnchorRatioProperty = property(get_HorizontalAnchorRatioProperty, None)
    HorizontalScrollChainModeProperty = property(get_HorizontalScrollChainModeProperty, None)
    HorizontalScrollModeProperty = property(get_HorizontalScrollModeProperty, None)
    HorizontalScrollRailModeProperty = property(get_HorizontalScrollRailModeProperty, None)
    IgnoredInputKindsProperty = property(get_IgnoredInputKindsProperty, None)
    MaxZoomFactorProperty = property(get_MaxZoomFactorProperty, None)
    MinZoomFactorProperty = property(get_MinZoomFactorProperty, None)
    VerticalAnchorRatioProperty = property(get_VerticalAnchorRatioProperty, None)
    VerticalScrollChainModeProperty = property(get_VerticalScrollChainModeProperty, None)
    VerticalScrollModeProperty = property(get_VerticalScrollModeProperty, None)
    VerticalScrollRailModeProperty = property(get_VerticalScrollRailModeProperty, None)
    ZoomChainModeProperty = property(get_ZoomChainModeProperty, None)
    ZoomModeProperty = property(get_ZoomModeProperty, None)
class IScrollSnapPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPoint'
    _iid_ = Guid('{73d918ff-d16c-52cd-9657-e392ee08868a}')
    @winrt_commethod(6)
    def get_Value(self) -> Double: ...
    Value = property(get_Value, None)
class IScrollSnapPointBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointBase'
    _iid_ = Guid('{45d7319d-c9eb-5109-9668-ff3fc6ccdf11}')
    @winrt_commethod(6)
    def get_Alignment(self) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment: ...
    Alignment = property(get_Alignment, None)
class IScrollSnapPointBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointBaseFactory'
    _iid_ = Guid('{3fa2e552-1a45-5691-99dc-6400087cbb38}')
class IScrollSnapPointFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointFactory'
    _iid_ = Guid('{39304bc7-0e54-5c06-8920-adcf67e7c466}')
    @winrt_commethod(6)
    def CreateInstance(self, snapPointValue: Double, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPoint: ...
class IScrollSnapPointsInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo'
    _iid_ = Guid('{d3ea6e09-ecf7-51a8-bd54-fc84b9653766}')
    @winrt_commethod(6)
    def get_AreHorizontalSnapPointsRegular(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AreVerticalSnapPointsRegular(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_HorizontalSnapPointsChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HorizontalSnapPointsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_VerticalSnapPointsChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_VerticalSnapPointsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def GetIrregularSnapPoints(self, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_commethod(13)
    def GetRegularSnapPoints(self, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    AreHorizontalSnapPointsRegular = property(get_AreHorizontalSnapPointsRegular, None)
    AreVerticalSnapPointsRegular = property(get_AreVerticalSnapPointsRegular, None)
    HorizontalSnapPointsChanged = event()
    VerticalSnapPointsChanged = event()
class ISelector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISelector'
    _iid_ = Guid('{8f7e2159-e61d-576f-8476-f83fde3d689e}')
    @winrt_commethod(6)
    def get_SelectedIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_SelectedIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_SelectedItem(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(9)
    def put_SelectedItem(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(10)
    def get_SelectedValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def put_SelectedValue(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(12)
    def get_SelectedValuePath(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_SelectedValuePath(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_IsSynchronizedWithCurrentItem(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(15)
    def put_IsSynchronizedWithCurrentItem(self, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(16)
    def add_SelectionChanged(self, handler: win32more.Microsoft.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SelectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsSynchronizedWithCurrentItem = property(get_IsSynchronizedWithCurrentItem, put_IsSynchronizedWithCurrentItem)
    SelectedIndex = property(get_SelectedIndex, put_SelectedIndex)
    SelectedItem = property(get_SelectedItem, put_SelectedItem)
    SelectedValue = property(get_SelectedValue, put_SelectedValue)
    SelectedValuePath = property(get_SelectedValuePath, put_SelectedValuePath)
    SelectionChanged = event()
class ISelectorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISelectorFactory'
    _iid_ = Guid('{21a42024-af07-58f9-8789-848d3324d901}')
class ISelectorItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISelectorItem'
    _iid_ = Guid('{5772c4de-60ea-5492-8c5e-b3323d5a3ca6}')
    @winrt_commethod(6)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsSelected(self, value: Boolean) -> Void: ...
    IsSelected = property(get_IsSelected, put_IsSelected)
class ISelectorItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISelectorItemFactory'
    _iid_ = Guid('{078039f5-76ed-5299-9715-fc8c58173560}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.SelectorItem: ...
class ISelectorItemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISelectorItemStatics'
    _iid_ = Guid('{4b201a54-a414-5e79-9b6b-3da9de442a35}')
    @winrt_commethod(6)
    def get_IsSelectedProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsSelectedProperty = property(get_IsSelectedProperty, None)
class ISelectorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISelectorStatics'
    _iid_ = Guid('{569b2234-1ceb-516e-b64e-0d479452e279}')
    @winrt_commethod(6)
    def get_SelectedIndexProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SelectedItemProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_SelectedValueProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_SelectedValuePathProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_IsSynchronizedWithCurrentItemProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def GetIsSelectionActive(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    IsSynchronizedWithCurrentItemProperty = property(get_IsSynchronizedWithCurrentItemProperty, None)
    SelectedIndexProperty = property(get_SelectedIndexProperty, None)
    SelectedItemProperty = property(get_SelectedItemProperty, None)
    SelectedValuePathProperty = property(get_SelectedValuePathProperty, None)
    SelectedValueProperty = property(get_SelectedValueProperty, None)
class ISnapPointBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISnapPointBase'
    _iid_ = Guid('{14ed1089-fb97-5211-8c45-c352cd8b96a1}')
class ISnapPointBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISnapPointBaseFactory'
    _iid_ = Guid('{50266508-15f8-530a-a213-e976e04e670b}')
class ISplitViewTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings'
    _iid_ = Guid('{44d6f6f7-0058-5eac-8837-f7f16d961f7c}')
    @winrt_commethod(6)
    def get_OpenPaneLength(self) -> Double: ...
    @winrt_commethod(7)
    def get_NegativeOpenPaneLength(self) -> Double: ...
    @winrt_commethod(8)
    def get_OpenPaneLengthMinusCompactLength(self) -> Double: ...
    @winrt_commethod(9)
    def get_NegativeOpenPaneLengthMinusCompactLength(self) -> Double: ...
    @winrt_commethod(10)
    def get_OpenPaneGridLength(self) -> win32more.Microsoft.UI.Xaml.GridLength: ...
    @winrt_commethod(11)
    def get_CompactPaneGridLength(self) -> win32more.Microsoft.UI.Xaml.GridLength: ...
    CompactPaneGridLength = property(get_CompactPaneGridLength, None)
    NegativeOpenPaneLength = property(get_NegativeOpenPaneLength, None)
    NegativeOpenPaneLengthMinusCompactLength = property(get_NegativeOpenPaneLengthMinusCompactLength, None)
    OpenPaneGridLength = property(get_OpenPaneGridLength, None)
    OpenPaneLength = property(get_OpenPaneLength, None)
    OpenPaneLengthMinusCompactLength = property(get_OpenPaneLengthMinusCompactLength, None)
class ITabViewListView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ITabViewListView'
    _iid_ = Guid('{ec48efb5-2cb3-562b-921c-e554923ce1d5}')
class ITabViewListViewFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ITabViewListViewFactory'
    _iid_ = Guid('{8a084fdd-86f0-51ee-98df-5fbd0b5669be}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.TabViewListView: ...
class IThumb(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IThumb'
    _iid_ = Guid('{9b540ae4-98ed-5a19-9512-a56878c52fee}')
    @winrt_commethod(6)
    def get_IsDragging(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_DragStarted(self, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragStartedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_DragStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_DragDelta(self, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragDeltaEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_DragDelta(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_DragCompleted(self, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_DragCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def CancelDrag(self) -> Void: ...
    IsDragging = property(get_IsDragging, None)
    DragStarted = event()
    DragDelta = event()
    DragCompleted = event()
class IThumbStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IThumbStatics'
    _iid_ = Guid('{900c4924-886a-5f24-96d1-1ec3a36e8d66}')
    @winrt_commethod(6)
    def get_IsDraggingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsDraggingProperty = property(get_IsDraggingProperty, None)
class ITickBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ITickBar'
    _iid_ = Guid('{573293bd-3f6a-56c3-bf95-6254c9bbbc89}')
    @winrt_commethod(6)
    def get_Fill(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Fill(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    Fill = property(get_Fill, put_Fill)
class ITickBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ITickBarStatics'
    _iid_ = Guid('{41c210cf-7060-5b7b-83ab-a302aa6eed6b}')
    @winrt_commethod(6)
    def get_FillProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FillProperty = property(get_FillProperty, None)
class IToggleButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IToggleButton'
    _iid_ = Guid('{686fbaa4-c866-568b-8f75-481d8d545291}')
    @winrt_commethod(6)
    def get_IsChecked(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(7)
    def put_IsChecked(self, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(8)
    def get_IsThreeState(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsThreeState(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def add_Checked(self, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Checked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Unchecked(self, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Unchecked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Indeterminate(self, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Indeterminate(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsChecked = property(get_IsChecked, put_IsChecked)
    IsThreeState = property(get_IsThreeState, put_IsThreeState)
    Checked = event()
    Unchecked = event()
    Indeterminate = event()
class IToggleButtonFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IToggleButtonFactory'
    _iid_ = Guid('{519511bb-d35b-5e2d-966c-8369405a4408}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ToggleButton: ...
class IToggleButtonOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IToggleButtonOverrides'
    _iid_ = Guid('{ee55f85d-9061-5d18-b31a-90bc5625cfe9}')
    @winrt_commethod(6)
    def OnToggle(self) -> Void: ...
class IToggleButtonStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IToggleButtonStatics'
    _iid_ = Guid('{4b8397e3-76fd-59df-824f-40ae339fb00b}')
    @winrt_commethod(6)
    def get_IsCheckedProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsThreeStateProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsCheckedProperty = property(get_IsCheckedProperty, None)
    IsThreeStateProperty = property(get_IsThreeStateProperty, None)
class IToggleSwitchTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings'
    _iid_ = Guid('{8f9640a3-aa4e-52da-a2c6-9167c800baba}')
    @winrt_commethod(6)
    def get_KnobCurrentToOnOffset(self) -> Double: ...
    @winrt_commethod(7)
    def get_KnobCurrentToOffOffset(self) -> Double: ...
    @winrt_commethod(8)
    def get_KnobOnToOffOffset(self) -> Double: ...
    @winrt_commethod(9)
    def get_KnobOffToOnOffset(self) -> Double: ...
    @winrt_commethod(10)
    def get_CurtainCurrentToOnOffset(self) -> Double: ...
    @winrt_commethod(11)
    def get_CurtainCurrentToOffOffset(self) -> Double: ...
    @winrt_commethod(12)
    def get_CurtainOnToOffOffset(self) -> Double: ...
    @winrt_commethod(13)
    def get_CurtainOffToOnOffset(self) -> Double: ...
    CurtainCurrentToOffOffset = property(get_CurtainCurrentToOffOffset, None)
    CurtainCurrentToOnOffset = property(get_CurtainCurrentToOnOffset, None)
    CurtainOffToOnOffset = property(get_CurtainOffToOnOffset, None)
    CurtainOnToOffOffset = property(get_CurtainOnToOffOffset, None)
    KnobCurrentToOffOffset = property(get_KnobCurrentToOffOffset, None)
    KnobCurrentToOnOffset = property(get_KnobCurrentToOnOffset, None)
    KnobOffToOnOffset = property(get_KnobOffToOnOffset, None)
    KnobOnToOffOffset = property(get_KnobOnToOffOffset, None)
class IToolTipTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings'
    _iid_ = Guid('{4f725950-ff64-5cf1-9e86-9011fb10e88e}')
    @winrt_commethod(6)
    def get_FromHorizontalOffset(self) -> Double: ...
    @winrt_commethod(7)
    def get_FromVerticalOffset(self) -> Double: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, None)
    FromVerticalOffset = property(get_FromVerticalOffset, None)
class IZoomSnapPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPoint'
    _iid_ = Guid('{8101d353-8db3-5ac6-a7f8-b18eb9c123ac}')
    @winrt_commethod(6)
    def get_Value(self) -> Double: ...
    Value = property(get_Value, None)
class IZoomSnapPointBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPointBase'
    _iid_ = Guid('{c6d08756-0860-5c2d-abec-6eb4aa4b53d7}')
class IZoomSnapPointBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPointBaseFactory'
    _iid_ = Guid('{2c689eea-b6cf-5024-847b-589355d5a2fa}')
class IZoomSnapPointFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPointFactory'
    _iid_ = Guid('{0b3b5418-bff6-5a9e-b734-b68adf49f775}')
    @winrt_commethod(6)
    def CreateInstance(self, snapPointValue: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPoint: ...
class _InfoBarPanel_Meta_(ComPtr.__class__):
    pass
class InfoBarPanel(ComPtr, metaclass=_InfoBarPanel_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Panel
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanel
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.InfoBarPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.InfoBarPanel.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.InfoBarPanel: ...
    @winrt_mixinmethod
    def get_HorizontalOrientationPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanel) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_HorizontalOrientationPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanel, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOrientationPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanel) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_VerticalOrientationPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanel, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_classmethod
    def get_HorizontalOrientationPaddingProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalOrientationPaddingProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def SetHorizontalOrientationMargin(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics, object: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_classmethod
    def GetHorizontalOrientationMargin(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics, object: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_classmethod
    def get_HorizontalOrientationMarginProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def SetVerticalOrientationMargin(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics, object: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_classmethod
    def GetVerticalOrientationMargin(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics, object: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_classmethod
    def get_VerticalOrientationMarginProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IInfoBarPanelStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    HorizontalOrientationPadding = property(get_HorizontalOrientationPadding, put_HorizontalOrientationPadding)
    VerticalOrientationPadding = property(get_VerticalOrientationPadding, put_VerticalOrientationPadding)
    _InfoBarPanel_Meta_.HorizontalOrientationMarginProperty = property(get_HorizontalOrientationMarginProperty, None)
    _InfoBarPanel_Meta_.HorizontalOrientationPaddingProperty = property(get_HorizontalOrientationPaddingProperty, None)
    _InfoBarPanel_Meta_.VerticalOrientationMarginProperty = property(get_VerticalOrientationMarginProperty, None)
    _InfoBarPanel_Meta_.VerticalOrientationPaddingProperty = property(get_VerticalOrientationPaddingProperty, None)
class ItemsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ItemsChangedEventArgs'
    @winrt_mixinmethod
    def get_Action(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
    @winrt_mixinmethod
    def get_OldPosition(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
    @winrt_mixinmethod
    def get_ItemCount(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ItemUICount(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> Int32: ...
    Action = property(get_Action, None)
    ItemCount = property(get_ItemCount, None)
    ItemUICount = property(get_ItemUICount, None)
    OldPosition = property(get_OldPosition, None)
    Position = property(get_Position, None)
class ItemsChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8e15e39e-23f7-5fcf-b04b-d1b7891dccc4}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Controls.Primitives.ItemsChangedEventArgs) -> Void: ...
class _JumpListItemBackgroundConverter_Meta_(ComPtr.__class__):
    pass
class JumpListItemBackgroundConverter(ComPtr, metaclass=_JumpListItemBackgroundConverter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.JumpListItemBackgroundConverter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.JumpListItemBackgroundConverter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.JumpListItemBackgroundConverter: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_Disabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Disabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def Convert(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def ConvertBack(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_EnabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
    _JumpListItemBackgroundConverter_Meta_.DisabledProperty = property(get_DisabledProperty, None)
    _JumpListItemBackgroundConverter_Meta_.EnabledProperty = property(get_EnabledProperty, None)
class _JumpListItemForegroundConverter_Meta_(ComPtr.__class__):
    pass
class JumpListItemForegroundConverter(ComPtr, metaclass=_JumpListItemForegroundConverter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.JumpListItemForegroundConverter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.JumpListItemForegroundConverter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.JumpListItemForegroundConverter: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_Disabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Disabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def Convert(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def ConvertBack(self: win32more.Microsoft.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_EnabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
    _JumpListItemForegroundConverter_Meta_.DisabledProperty = property(get_DisabledProperty, None)
    _JumpListItemForegroundConverter_Meta_.EnabledProperty = property(get_EnabledProperty, None)
class LayoutInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILayoutInformation
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.LayoutInformation'
    @winrt_classmethod
    def GetLayoutExceptionElement(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILayoutInformationStatics, dispatcher: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def GetLayoutSlot(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILayoutInformationStatics, element: win32more.Microsoft.UI.Xaml.FrameworkElement) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def GetAvailableSize(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILayoutInformationStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Size: ...
class _ListViewItemPresenter_Meta_(ComPtr.__class__):
    pass
class ListViewItemPresenter(ComPtr, metaclass=_ListViewItemPresenter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.ContentPresenter
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenter: ...
    @winrt_mixinmethod
    def get_SelectionCheckMarkVisualEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SelectionCheckMarkVisualEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CheckHintBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckHintBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckSelectingBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckSelectingBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PlaceholderBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBorderThickness(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_SelectedBorderThickness(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_DisabledOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DisabledOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DragOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DragOpacity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReorderHintOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_ReorderHintOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ListViewItemPresenterHorizontalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.HorizontalAlignment: ...
    @winrt_mixinmethod
    def put_ListViewItemPresenterHorizontalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_ListViewItemPresenterVerticalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.VerticalAlignment: ...
    @winrt_mixinmethod
    def put_ListViewItemPresenterVerticalContentAlignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_ListViewItemPresenterPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ListViewItemPresenterPadding(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackgroundMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_PointerOverBackgroundMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_ContentMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ContentMargin(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPressedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPressedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PressedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PressedBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusSecondaryBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusSecondaryBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode: ...
    @winrt_mixinmethod
    def put_CheckMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverForeground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_RevealBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_RevealBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBorderThickness(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_RevealBorderThickness(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBackgroundShowsAboveContent(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_RevealBackgroundShowsAboveContent(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedDisabledBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedDisabledBackground(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPointerOverBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPointerOverBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedPointerOverBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedPointerOverBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPressedBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPressedBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxDisabledBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxDisabledBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxCornerRadius(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.CornerRadius: ...
    @winrt_mixinmethod
    def put_CheckBoxCornerRadius(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorCornerRadius(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.CornerRadius: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorCornerRadius(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorVisualEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorVisualEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorPointerOverBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorPointerOverBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorPressedBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorDisabledBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPressedBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPressedBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedDisabledBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedDisabledBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedInnerBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedInnerBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverBorderBrush(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_classmethod
    def get_SelectionCheckMarkVisualEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckHintBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckSelectingBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragForegroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PlaceholderBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedForegroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBorderThicknessProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledOpacityProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragOpacityProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ReorderHintOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ListViewItemPresenterHorizontalContentAlignmentProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ListViewItemPresenterVerticalContentAlignmentProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ListViewItemPresenterPaddingProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundMarginProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentMarginProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPressedBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PressedBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusSecondaryBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverForegroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBorderThicknessProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBackgroundShowsAboveContentProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedDisabledBackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckPressedBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckDisabledBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPointerOverBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPressedBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxDisabledBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedPointerOverBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedPressedBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedDisabledBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPointerOverBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPressedBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxDisabledBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxCornerRadiusProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorCornerRadiusProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorVisualEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorPointerOverBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorPressedBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorDisabledBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPressedBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedDisabledBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedInnerBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBorderBrushProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CheckBoxBorderBrush = property(get_CheckBoxBorderBrush, put_CheckBoxBorderBrush)
    CheckBoxBrush = property(get_CheckBoxBrush, put_CheckBoxBrush)
    CheckBoxCornerRadius = property(get_CheckBoxCornerRadius, put_CheckBoxCornerRadius)
    CheckBoxDisabledBorderBrush = property(get_CheckBoxDisabledBorderBrush, put_CheckBoxDisabledBorderBrush)
    CheckBoxDisabledBrush = property(get_CheckBoxDisabledBrush, put_CheckBoxDisabledBrush)
    CheckBoxPointerOverBorderBrush = property(get_CheckBoxPointerOverBorderBrush, put_CheckBoxPointerOverBorderBrush)
    CheckBoxPointerOverBrush = property(get_CheckBoxPointerOverBrush, put_CheckBoxPointerOverBrush)
    CheckBoxPressedBorderBrush = property(get_CheckBoxPressedBorderBrush, put_CheckBoxPressedBorderBrush)
    CheckBoxPressedBrush = property(get_CheckBoxPressedBrush, put_CheckBoxPressedBrush)
    CheckBoxSelectedBrush = property(get_CheckBoxSelectedBrush, put_CheckBoxSelectedBrush)
    CheckBoxSelectedDisabledBrush = property(get_CheckBoxSelectedDisabledBrush, put_CheckBoxSelectedDisabledBrush)
    CheckBoxSelectedPointerOverBrush = property(get_CheckBoxSelectedPointerOverBrush, put_CheckBoxSelectedPointerOverBrush)
    CheckBoxSelectedPressedBrush = property(get_CheckBoxSelectedPressedBrush, put_CheckBoxSelectedPressedBrush)
    CheckBrush = property(get_CheckBrush, put_CheckBrush)
    CheckDisabledBrush = property(get_CheckDisabledBrush, put_CheckDisabledBrush)
    CheckHintBrush = property(get_CheckHintBrush, put_CheckHintBrush)
    CheckMode = property(get_CheckMode, put_CheckMode)
    CheckPressedBrush = property(get_CheckPressedBrush, put_CheckPressedBrush)
    CheckSelectingBrush = property(get_CheckSelectingBrush, put_CheckSelectingBrush)
    ContentMargin = property(get_ContentMargin, put_ContentMargin)
    DisabledOpacity = property(get_DisabledOpacity, put_DisabledOpacity)
    DragBackground = property(get_DragBackground, put_DragBackground)
    DragForeground = property(get_DragForeground, put_DragForeground)
    DragOpacity = property(get_DragOpacity, put_DragOpacity)
    FocusBorderBrush = property(get_FocusBorderBrush, put_FocusBorderBrush)
    FocusSecondaryBorderBrush = property(get_FocusSecondaryBorderBrush, put_FocusSecondaryBorderBrush)
    ListViewItemPresenterHorizontalContentAlignment = property(get_ListViewItemPresenterHorizontalContentAlignment, put_ListViewItemPresenterHorizontalContentAlignment)
    ListViewItemPresenterPadding = property(get_ListViewItemPresenterPadding, put_ListViewItemPresenterPadding)
    ListViewItemPresenterVerticalContentAlignment = property(get_ListViewItemPresenterVerticalContentAlignment, put_ListViewItemPresenterVerticalContentAlignment)
    PlaceholderBackground = property(get_PlaceholderBackground, put_PlaceholderBackground)
    PointerOverBackground = property(get_PointerOverBackground, put_PointerOverBackground)
    PointerOverBackgroundMargin = property(get_PointerOverBackgroundMargin, put_PointerOverBackgroundMargin)
    PointerOverBorderBrush = property(get_PointerOverBorderBrush, put_PointerOverBorderBrush)
    PointerOverForeground = property(get_PointerOverForeground, put_PointerOverForeground)
    PressedBackground = property(get_PressedBackground, put_PressedBackground)
    ReorderHintOffset = property(get_ReorderHintOffset, put_ReorderHintOffset)
    RevealBackground = property(get_RevealBackground, put_RevealBackground)
    RevealBackgroundShowsAboveContent = property(get_RevealBackgroundShowsAboveContent, put_RevealBackgroundShowsAboveContent)
    RevealBorderBrush = property(get_RevealBorderBrush, put_RevealBorderBrush)
    RevealBorderThickness = property(get_RevealBorderThickness, put_RevealBorderThickness)
    SelectedBackground = property(get_SelectedBackground, put_SelectedBackground)
    SelectedBorderBrush = property(get_SelectedBorderBrush, put_SelectedBorderBrush)
    SelectedBorderThickness = property(get_SelectedBorderThickness, put_SelectedBorderThickness)
    SelectedDisabledBackground = property(get_SelectedDisabledBackground, put_SelectedDisabledBackground)
    SelectedDisabledBorderBrush = property(get_SelectedDisabledBorderBrush, put_SelectedDisabledBorderBrush)
    SelectedForeground = property(get_SelectedForeground, put_SelectedForeground)
    SelectedInnerBorderBrush = property(get_SelectedInnerBorderBrush, put_SelectedInnerBorderBrush)
    SelectedPointerOverBackground = property(get_SelectedPointerOverBackground, put_SelectedPointerOverBackground)
    SelectedPointerOverBorderBrush = property(get_SelectedPointerOverBorderBrush, put_SelectedPointerOverBorderBrush)
    SelectedPressedBackground = property(get_SelectedPressedBackground, put_SelectedPressedBackground)
    SelectedPressedBorderBrush = property(get_SelectedPressedBorderBrush, put_SelectedPressedBorderBrush)
    SelectionCheckMarkVisualEnabled = property(get_SelectionCheckMarkVisualEnabled, put_SelectionCheckMarkVisualEnabled)
    SelectionIndicatorBrush = property(get_SelectionIndicatorBrush, put_SelectionIndicatorBrush)
    SelectionIndicatorCornerRadius = property(get_SelectionIndicatorCornerRadius, put_SelectionIndicatorCornerRadius)
    SelectionIndicatorDisabledBrush = property(get_SelectionIndicatorDisabledBrush, put_SelectionIndicatorDisabledBrush)
    SelectionIndicatorMode = property(get_SelectionIndicatorMode, put_SelectionIndicatorMode)
    SelectionIndicatorPointerOverBrush = property(get_SelectionIndicatorPointerOverBrush, put_SelectionIndicatorPointerOverBrush)
    SelectionIndicatorPressedBrush = property(get_SelectionIndicatorPressedBrush, put_SelectionIndicatorPressedBrush)
    SelectionIndicatorVisualEnabled = property(get_SelectionIndicatorVisualEnabled, put_SelectionIndicatorVisualEnabled)
    _ListViewItemPresenter_Meta_.CheckBoxBorderBrushProperty = property(get_CheckBoxBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxBrushProperty = property(get_CheckBoxBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxCornerRadiusProperty = property(get_CheckBoxCornerRadiusProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxDisabledBorderBrushProperty = property(get_CheckBoxDisabledBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxDisabledBrushProperty = property(get_CheckBoxDisabledBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxPointerOverBorderBrushProperty = property(get_CheckBoxPointerOverBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxPointerOverBrushProperty = property(get_CheckBoxPointerOverBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxPressedBorderBrushProperty = property(get_CheckBoxPressedBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxPressedBrushProperty = property(get_CheckBoxPressedBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxSelectedBrushProperty = property(get_CheckBoxSelectedBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxSelectedDisabledBrushProperty = property(get_CheckBoxSelectedDisabledBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxSelectedPointerOverBrushProperty = property(get_CheckBoxSelectedPointerOverBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBoxSelectedPressedBrushProperty = property(get_CheckBoxSelectedPressedBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckBrushProperty = property(get_CheckBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckDisabledBrushProperty = property(get_CheckDisabledBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckHintBrushProperty = property(get_CheckHintBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckModeProperty = property(get_CheckModeProperty, None)
    _ListViewItemPresenter_Meta_.CheckPressedBrushProperty = property(get_CheckPressedBrushProperty, None)
    _ListViewItemPresenter_Meta_.CheckSelectingBrushProperty = property(get_CheckSelectingBrushProperty, None)
    _ListViewItemPresenter_Meta_.ContentMarginProperty = property(get_ContentMarginProperty, None)
    _ListViewItemPresenter_Meta_.DisabledOpacityProperty = property(get_DisabledOpacityProperty, None)
    _ListViewItemPresenter_Meta_.DragBackgroundProperty = property(get_DragBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.DragForegroundProperty = property(get_DragForegroundProperty, None)
    _ListViewItemPresenter_Meta_.DragOpacityProperty = property(get_DragOpacityProperty, None)
    _ListViewItemPresenter_Meta_.FocusBorderBrushProperty = property(get_FocusBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.FocusSecondaryBorderBrushProperty = property(get_FocusSecondaryBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.ListViewItemPresenterHorizontalContentAlignmentProperty = property(get_ListViewItemPresenterHorizontalContentAlignmentProperty, None)
    _ListViewItemPresenter_Meta_.ListViewItemPresenterPaddingProperty = property(get_ListViewItemPresenterPaddingProperty, None)
    _ListViewItemPresenter_Meta_.ListViewItemPresenterVerticalContentAlignmentProperty = property(get_ListViewItemPresenterVerticalContentAlignmentProperty, None)
    _ListViewItemPresenter_Meta_.PlaceholderBackgroundProperty = property(get_PlaceholderBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.PointerOverBackgroundMarginProperty = property(get_PointerOverBackgroundMarginProperty, None)
    _ListViewItemPresenter_Meta_.PointerOverBackgroundProperty = property(get_PointerOverBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.PointerOverBorderBrushProperty = property(get_PointerOverBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.PointerOverForegroundProperty = property(get_PointerOverForegroundProperty, None)
    _ListViewItemPresenter_Meta_.PressedBackgroundProperty = property(get_PressedBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.ReorderHintOffsetProperty = property(get_ReorderHintOffsetProperty, None)
    _ListViewItemPresenter_Meta_.RevealBackgroundProperty = property(get_RevealBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.RevealBackgroundShowsAboveContentProperty = property(get_RevealBackgroundShowsAboveContentProperty, None)
    _ListViewItemPresenter_Meta_.RevealBorderBrushProperty = property(get_RevealBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.RevealBorderThicknessProperty = property(get_RevealBorderThicknessProperty, None)
    _ListViewItemPresenter_Meta_.SelectedBackgroundProperty = property(get_SelectedBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.SelectedBorderBrushProperty = property(get_SelectedBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectedBorderThicknessProperty = property(get_SelectedBorderThicknessProperty, None)
    _ListViewItemPresenter_Meta_.SelectedDisabledBackgroundProperty = property(get_SelectedDisabledBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.SelectedDisabledBorderBrushProperty = property(get_SelectedDisabledBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectedForegroundProperty = property(get_SelectedForegroundProperty, None)
    _ListViewItemPresenter_Meta_.SelectedInnerBorderBrushProperty = property(get_SelectedInnerBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectedPointerOverBackgroundProperty = property(get_SelectedPointerOverBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.SelectedPointerOverBorderBrushProperty = property(get_SelectedPointerOverBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectedPressedBackgroundProperty = property(get_SelectedPressedBackgroundProperty, None)
    _ListViewItemPresenter_Meta_.SelectedPressedBorderBrushProperty = property(get_SelectedPressedBorderBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectionCheckMarkVisualEnabledProperty = property(get_SelectionCheckMarkVisualEnabledProperty, None)
    _ListViewItemPresenter_Meta_.SelectionIndicatorBrushProperty = property(get_SelectionIndicatorBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectionIndicatorCornerRadiusProperty = property(get_SelectionIndicatorCornerRadiusProperty, None)
    _ListViewItemPresenter_Meta_.SelectionIndicatorDisabledBrushProperty = property(get_SelectionIndicatorDisabledBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectionIndicatorModeProperty = property(get_SelectionIndicatorModeProperty, None)
    _ListViewItemPresenter_Meta_.SelectionIndicatorPointerOverBrushProperty = property(get_SelectionIndicatorPointerOverBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectionIndicatorPressedBrushProperty = property(get_SelectionIndicatorPressedBrushProperty, None)
    _ListViewItemPresenter_Meta_.SelectionIndicatorVisualEnabledProperty = property(get_SelectionIndicatorVisualEnabledProperty, None)
class ListViewItemPresenterCheckMode(Enum, Int32):
    Inline = 0
    Overlay = 1
class ListViewItemPresenterSelectionIndicatorMode(Enum, Int32):
    Inline = 0
    Overlay = 1
class ListViewItemTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ListViewItemTemplateSettings'
    @winrt_mixinmethod
    def get_DragItemsCount(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IListViewItemTemplateSettings) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class _LoopingSelector_Meta_(ComPtr.__class__):
    pass
class LoopingSelector(ComPtr, metaclass=_LoopingSelector_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Control
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.LoopingSelector'
    @winrt_mixinmethod
    def get_ShouldLoop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldLoop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Items(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def put_Items(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedIndex(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Int32: ...
    @winrt_mixinmethod
    def put_SelectedIndex(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedItem(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_SelectedItem(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_ItemWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Int32: ...
    @winrt_mixinmethod
    def put_ItemWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ItemHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Int32: ...
    @winrt_mixinmethod
    def put_ItemHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ItemTemplate(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector) -> win32more.Microsoft.UI.Xaml.DataTemplate: ...
    @winrt_mixinmethod
    def put_ItemTemplate(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, value: win32more.Microsoft.UI.Xaml.DataTemplate) -> Void: ...
    @winrt_mixinmethod
    def add_SelectionChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, handler: win32more.Microsoft.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelector, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ShouldLoopProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedIndexProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedItemProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemWidthProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemHeightProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemTemplateProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ItemHeight = property(get_ItemHeight, put_ItemHeight)
    ItemTemplate = property(get_ItemTemplate, put_ItemTemplate)
    ItemWidth = property(get_ItemWidth, put_ItemWidth)
    Items = property(get_Items, put_Items)
    SelectedIndex = property(get_SelectedIndex, put_SelectedIndex)
    SelectedItem = property(get_SelectedItem, put_SelectedItem)
    ShouldLoop = property(get_ShouldLoop, put_ShouldLoop)
    _LoopingSelector_Meta_.ItemHeightProperty = property(get_ItemHeightProperty, None)
    _LoopingSelector_Meta_.ItemTemplateProperty = property(get_ItemTemplateProperty, None)
    _LoopingSelector_Meta_.ItemWidthProperty = property(get_ItemWidthProperty, None)
    _LoopingSelector_Meta_.ItemsProperty = property(get_ItemsProperty, None)
    _LoopingSelector_Meta_.SelectedIndexProperty = property(get_SelectedIndexProperty, None)
    _LoopingSelector_Meta_.SelectedItemProperty = property(get_SelectedItemProperty, None)
    _LoopingSelector_Meta_.ShouldLoopProperty = property(get_ShouldLoopProperty, None)
    SelectionChanged = event()
class LoopingSelectorItem(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorItem
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.LoopingSelectorItem'
class LoopingSelectorPanel(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Canvas
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ILoopingSelectorPanel
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.LoopingSelectorPanel'
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    AreHorizontalSnapPointsRegular = property(get_AreHorizontalSnapPointsRegular, None)
    AreVerticalSnapPointsRegular = property(get_AreVerticalSnapPointsRegular, None)
    HorizontalSnapPointsChanged = event()
    VerticalSnapPointsChanged = event()
class MenuFlyoutItemTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMenuFlyoutItemTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.MenuFlyoutItemTemplateSettings'
    @winrt_mixinmethod
    def get_KeyboardAcceleratorTextMinWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMenuFlyoutItemTemplateSettings) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class MenuFlyoutPresenterTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.MenuFlyoutPresenterTemplateSettings'
    @winrt_mixinmethod
    def get_FlyoutContentMinWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings) -> Double: ...
    FlyoutContentMinWidth = property(get_FlyoutContentMinWidth, None)
class _MonochromaticOverlayPresenter_Meta_(ComPtr.__class__):
    pass
class MonochromaticOverlayPresenter(ComPtr, metaclass=_MonochromaticOverlayPresenter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Grid
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.MonochromaticOverlayPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.MonochromaticOverlayPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.MonochromaticOverlayPresenter: ...
    @winrt_mixinmethod
    def get_SourceElement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenter) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_SourceElement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenter, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_ReplacementColor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenter) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ReplacementColor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenter, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_classmethod
    def get_SourceElementProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ReplacementColorProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IMonochromaticOverlayPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ReplacementColor = property(get_ReplacementColor, put_ReplacementColor)
    SourceElement = property(get_SourceElement, put_SourceElement)
    _MonochromaticOverlayPresenter_Meta_.ReplacementColorProperty = property(get_ReplacementColorProperty, None)
    _MonochromaticOverlayPresenter_Meta_.SourceElementProperty = property(get_SourceElementProperty, None)
class _NavigationViewItemPresenter_Meta_(ComPtr.__class__):
    pass
class NavigationViewItemPresenter(ComPtr, metaclass=_NavigationViewItemPresenter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Controls.IconElement: ...
    @winrt_mixinmethod
    def put_Icon(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter, value: win32more.Microsoft.UI.Xaml.Controls.IconElement) -> Void: ...
    @winrt_mixinmethod
    def get_TemplateSettings(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenterTemplateSettings: ...
    @winrt_mixinmethod
    def get_InfoBadge(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter2) -> win32more.Microsoft.UI.Xaml.Controls.InfoBadge: ...
    @winrt_mixinmethod
    def put_InfoBadge(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter2, value: win32more.Microsoft.UI.Xaml.Controls.InfoBadge) -> Void: ...
    @winrt_classmethod
    def get_InfoBadgeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterStatics2) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IconProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TemplateSettingsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Icon = property(get_Icon, put_Icon)
    InfoBadge = property(get_InfoBadge, put_InfoBadge)
    TemplateSettings = property(get_TemplateSettings, None)
    _NavigationViewItemPresenter_Meta_.IconProperty = property(get_IconProperty, None)
    _NavigationViewItemPresenter_Meta_.InfoBadgeProperty = property(get_InfoBadgeProperty, None)
    _NavigationViewItemPresenter_Meta_.TemplateSettingsProperty = property(get_TemplateSettingsProperty, None)
class _NavigationViewItemPresenterTemplateSettings_Meta_(ComPtr.__class__):
    pass
class NavigationViewItemPresenterTemplateSettings(ComPtr, metaclass=_NavigationViewItemPresenterTemplateSettings_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenterTemplateSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenterTemplateSettings.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettingsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.NavigationViewItemPresenterTemplateSettings: ...
    @winrt_mixinmethod
    def get_IconWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_SmallerIconWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettings) -> Double: ...
    @winrt_classmethod
    def get_IconWidthProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettingsStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SmallerIconWidthProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterTemplateSettingsStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IconWidth = property(get_IconWidth, None)
    SmallerIconWidth = property(get_SmallerIconWidth, None)
    _NavigationViewItemPresenterTemplateSettings_Meta_.IconWidthProperty = property(get_IconWidthProperty, None)
    _NavigationViewItemPresenterTemplateSettings_Meta_.SmallerIconWidthProperty = property(get_SmallerIconWidthProperty, None)
class OrientedVirtualizingPanel(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.VirtualizingPanel
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.OrientedVirtualizingPanel'
    @winrt_mixinmethod
    def get_CanVerticallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanVerticallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanHorizontallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanHorizontallyScroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExtentWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ExtentHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollOwner(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_ScrollOwner(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def LineUp(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def LineDown(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def LineLeft(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def LineRight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageUp(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageDown(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageLeft(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageRight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelUp(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelDown(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelLeft(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelRight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def SetHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def SetVerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def MakeVisible(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, visual: win32more.Microsoft.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    @winrt_mixinmethod
    def GetInsertionIndexes(self: win32more.Microsoft.UI.Xaml.Controls.IInsertionPanel, position: win32more.Windows.Foundation.Point, first: POINTER(Int32), second: POINTER(Int32)) -> Void: ...
    AreHorizontalSnapPointsRegular = property(get_AreHorizontalSnapPointsRegular, None)
    AreVerticalSnapPointsRegular = property(get_AreVerticalSnapPointsRegular, None)
    CanHorizontallyScroll = property(get_CanHorizontallyScroll, put_CanHorizontallyScroll)
    CanVerticallyScroll = property(get_CanVerticallyScroll, put_CanVerticallyScroll)
    ExtentHeight = property(get_ExtentHeight, None)
    ExtentWidth = property(get_ExtentWidth, None)
    HorizontalOffset = property(get_HorizontalOffset, None)
    ScrollOwner = property(get_ScrollOwner, put_ScrollOwner)
    VerticalOffset = property(get_VerticalOffset, None)
    ViewportHeight = property(get_ViewportHeight, None)
    ViewportWidth = property(get_ViewportWidth, None)
    HorizontalSnapPointsChanged = event()
    VerticalSnapPointsChanged = event()
class _PickerFlyoutBase_Meta_(ComPtr.__class__):
    pass
class PickerFlyoutBase(ComPtr, metaclass=_PickerFlyoutBase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.FlyoutBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBase
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.PickerFlyoutBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.PickerFlyoutBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PickerFlyoutBase: ...
    @winrt_mixinmethod
    def OnConfirmed(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseOverrides) -> Void: ...
    @winrt_mixinmethod
    def ShouldShowConfirmationButtons(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseOverrides) -> Boolean: ...
    @winrt_classmethod
    def get_TitleProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTitle(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetTitle(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    _PickerFlyoutBase_Meta_.TitleProperty = property(get_TitleProperty, None)
class PivotHeaderItem(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPivotHeaderItem
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.PivotHeaderItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.PivotHeaderItem.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPivotHeaderItemFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PivotHeaderItem: ...
class PivotHeaderPanel(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Canvas
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPivotHeaderPanel
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.PivotHeaderPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.PivotHeaderPanel.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PivotHeaderPanel: ...
class PivotPanel(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Panel
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPivotPanel
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.PivotPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.PivotPanel.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PivotPanel: ...
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Microsoft.UI.Xaml.Controls.Orientation, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    AreHorizontalSnapPointsRegular = property(get_AreHorizontalSnapPointsRegular, None)
    AreVerticalSnapPointsRegular = property(get_AreVerticalSnapPointsRegular, None)
    HorizontalSnapPointsChanged = event()
    VerticalSnapPointsChanged = event()
class PlacementMode(Enum, Int32):
    Bottom = 2
    Left = 9
    Mouse = 7
    Right = 4
    Top = 10
class _Popup_Meta_(ComPtr.__class__):
    pass
class Popup(ComPtr, metaclass=_Popup_Meta_):
    extends: win32more.Microsoft.UI.Xaml.FrameworkElement
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.Popup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.Popup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.Popup: ...
    @winrt_mixinmethod
    def get_Child(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Child(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_IsOpen(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOpen(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ChildTransitions(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> win32more.Microsoft.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_mixinmethod
    def put_ChildTransitions(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: win32more.Microsoft.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_mixinmethod
    def get_IsLightDismissEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLightDismissEnabled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LightDismissOverlayMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_mixinmethod
    def put_LightDismissOverlayMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: win32more.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldConstrainToRootBounds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldConstrainToRootBounds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsConstrainedToRootBounds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup) -> Boolean: ...
    @winrt_mixinmethod
    def add_Opened(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_PlacementTarget(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup2) -> win32more.Microsoft.UI.Xaml.FrameworkElement: ...
    @winrt_mixinmethod
    def put_PlacementTarget(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup2, value: win32more.Microsoft.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredPlacement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup2) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_mixinmethod
    def put_DesiredPlacement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup2, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def get_ActualPlacement(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup2) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_mixinmethod
    def add_ActualPlacementChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualPlacementChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup3) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_mixinmethod
    def put_SystemBackdrop(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopup3, value: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop) -> Void: ...
    @winrt_classmethod
    def get_SystemBackdropProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics3) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PlacementTargetProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics2) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DesiredPlacementProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics2) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsOpenProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildTransitionsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsLightDismissEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LightDismissOverlayModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ShouldConstrainToRootBoundsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ActualPlacement = property(get_ActualPlacement, None)
    Child = property(get_Child, put_Child)
    ChildTransitions = property(get_ChildTransitions, put_ChildTransitions)
    DesiredPlacement = property(get_DesiredPlacement, put_DesiredPlacement)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    IsConstrainedToRootBounds = property(get_IsConstrainedToRootBounds, None)
    IsLightDismissEnabled = property(get_IsLightDismissEnabled, put_IsLightDismissEnabled)
    IsOpen = property(get_IsOpen, put_IsOpen)
    LightDismissOverlayMode = property(get_LightDismissOverlayMode, put_LightDismissOverlayMode)
    PlacementTarget = property(get_PlacementTarget, put_PlacementTarget)
    ShouldConstrainToRootBounds = property(get_ShouldConstrainToRootBounds, put_ShouldConstrainToRootBounds)
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    _Popup_Meta_.ChildProperty = property(get_ChildProperty, None)
    _Popup_Meta_.ChildTransitionsProperty = property(get_ChildTransitionsProperty, None)
    _Popup_Meta_.DesiredPlacementProperty = property(get_DesiredPlacementProperty, None)
    _Popup_Meta_.HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    _Popup_Meta_.IsLightDismissEnabledProperty = property(get_IsLightDismissEnabledProperty, None)
    _Popup_Meta_.IsOpenProperty = property(get_IsOpenProperty, None)
    _Popup_Meta_.LightDismissOverlayModeProperty = property(get_LightDismissOverlayModeProperty, None)
    _Popup_Meta_.PlacementTargetProperty = property(get_PlacementTargetProperty, None)
    _Popup_Meta_.ShouldConstrainToRootBoundsProperty = property(get_ShouldConstrainToRootBoundsProperty, None)
    _Popup_Meta_.SystemBackdropProperty = property(get_SystemBackdropProperty, None)
    _Popup_Meta_.VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
    Opened = event()
    Closed = event()
    ActualPlacementChanged = event()
class PopupPlacementMode(Enum, Int32):
    Auto = 0
    Top = 1
    Bottom = 2
    Left = 3
    Right = 4
    TopEdgeAlignedLeft = 5
    TopEdgeAlignedRight = 6
    BottomEdgeAlignedLeft = 7
    BottomEdgeAlignedRight = 8
    LeftEdgeAlignedTop = 9
    LeftEdgeAlignedBottom = 10
    RightEdgeAlignedTop = 11
    RightEdgeAlignedBottom = 12
class _RangeBase_Meta_(ComPtr.__class__):
    pass
class RangeBase(ComPtr, metaclass=_RangeBase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Control
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.RangeBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBase: ...
    @winrt_mixinmethod
    def get_Minimum(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_Minimum(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Maximum(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_Maximum(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SmallChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_SmallChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LargeChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_LargeChange(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def add_ValueChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OnMinimumChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseOverrides, oldMinimum: Double, newMinimum: Double) -> Void: ...
    @winrt_mixinmethod
    def OnMaximumChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseOverrides, oldMaximum: Double, newMaximum: Double) -> Void: ...
    @winrt_mixinmethod
    def OnValueChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseOverrides, oldValue: Double, newValue: Double) -> Void: ...
    @winrt_classmethod
    def get_MinimumProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaximumProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SmallChangeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LargeChangeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    LargeChange = property(get_LargeChange, put_LargeChange)
    Maximum = property(get_Maximum, put_Maximum)
    Minimum = property(get_Minimum, put_Minimum)
    SmallChange = property(get_SmallChange, put_SmallChange)
    Value = property(get_Value, put_Value)
    _RangeBase_Meta_.LargeChangeProperty = property(get_LargeChangeProperty, None)
    _RangeBase_Meta_.MaximumProperty = property(get_MaximumProperty, None)
    _RangeBase_Meta_.MinimumProperty = property(get_MinimumProperty, None)
    _RangeBase_Meta_.SmallChangeProperty = property(get_SmallChangeProperty, None)
    _RangeBase_Meta_.ValueProperty = property(get_ValueProperty, None)
    ValueChanged = event()
class RangeBaseValueChangedEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventArgs'
    @winrt_mixinmethod
    def get_OldValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_NewValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs) -> Double: ...
    NewValue = property(get_NewValue, None)
    OldValue = property(get_OldValue, None)
class RangeBaseValueChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23f0e209-9455-54cb-b8bc-0b49553c7dcc}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventArgs) -> Void: ...
class _RepeatButton_Meta_(ComPtr.__class__):
    pass
class RepeatButton(ComPtr, metaclass=_RepeatButton_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.ButtonBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatButton
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.RepeatButton'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatButton.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatButton: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatButton) -> Int32: ...
    @winrt_mixinmethod
    def put_Delay(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatButton, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatButton) -> Int32: ...
    @winrt_mixinmethod
    def put_Interval(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatButton, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_DelayProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatButtonStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IntervalProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatButtonStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Delay = property(get_Delay, put_Delay)
    Interval = property(get_Interval, put_Interval)
    _RepeatButton_Meta_.DelayProperty = property(get_DelayProperty, None)
    _RepeatButton_Meta_.IntervalProperty = property(get_IntervalProperty, None)
class RepeatedScrollSnapPoint(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPoint
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.RepeatedScrollSnapPoint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 5:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatedScrollSnapPoint.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPointFactory, offset: Double, interval: Double, start: Double, end: Double, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatedScrollSnapPoint: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPoint) -> Double: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPoint) -> Double: ...
    @winrt_mixinmethod
    def get_Start(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPoint) -> Double: ...
    @winrt_mixinmethod
    def get_End(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedScrollSnapPoint) -> Double: ...
    End = property(get_End, None)
    Interval = property(get_Interval, None)
    Offset = property(get_Offset, None)
    Start = property(get_Start, None)
class RepeatedZoomSnapPoint(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPointBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPoint
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.RepeatedZoomSnapPoint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatedZoomSnapPoint.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPointFactory, offset: Double, interval: Double, start: Double, end: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatedZoomSnapPoint: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPoint) -> Double: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPoint) -> Double: ...
    @winrt_mixinmethod
    def get_Start(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPoint) -> Double: ...
    @winrt_mixinmethod
    def get_End(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IRepeatedZoomSnapPoint) -> Double: ...
    End = property(get_End, None)
    Interval = property(get_Interval, None)
    Offset = property(get_Offset, None)
    Start = property(get_Start, None)
class _ScrollBar_Meta_(ComPtr.__class__):
    pass
class ScrollBar(ComPtr, metaclass=_ScrollBar_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollBar'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollBar.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollBar: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar) -> win32more.Microsoft.UI.Xaml.Controls.Orientation: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar, value: win32more.Microsoft.UI.Xaml.Controls.Orientation) -> Void: ...
    @winrt_mixinmethod
    def get_ViewportSize(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar) -> Double: ...
    @winrt_mixinmethod
    def put_ViewportSize(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IndicatorMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode: ...
    @winrt_mixinmethod
    def put_IndicatorMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode) -> Void: ...
    @winrt_mixinmethod
    def add_Scroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Scroll(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBar, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_OrientationProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBarStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ViewportSizeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBarStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IndicatorModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollBarStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IndicatorMode = property(get_IndicatorMode, put_IndicatorMode)
    Orientation = property(get_Orientation, put_Orientation)
    ViewportSize = property(get_ViewportSize, put_ViewportSize)
    _ScrollBar_Meta_.IndicatorModeProperty = property(get_IndicatorModeProperty, None)
    _ScrollBar_Meta_.OrientationProperty = property(get_OrientationProperty, None)
    _ScrollBar_Meta_.ViewportSizeProperty = property(get_ViewportSizeProperty, None)
    Scroll = event()
class ScrollControllerAddScrollVelocityRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerAddScrollVelocityRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerAddScrollVelocityRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgsFactory, offsetVelocity: Single, inertiaDecayRate: win32more.Windows.Foundation.IReference[Single]) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerAddScrollVelocityRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_OffsetVelocity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgs) -> Single: ...
    @winrt_mixinmethod
    def get_InertiaDecayRate(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgs) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def put_CorrelationId(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerAddScrollVelocityRequestedEventArgs, value: Int32) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    InertiaDecayRate = property(get_InertiaDecayRate, None)
    OffsetVelocity = property(get_OffsetVelocity, None)
class ScrollControllerPanRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerPanRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerPanRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanRequestedEventArgsFactory, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerPanRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_PointerPoint(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanRequestedEventArgs) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerPanRequestedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    PointerPoint = property(get_PointerPoint, None)
class ScrollControllerScrollByRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollByRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollByRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgsFactory, offsetDelta: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollByRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_OffsetDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgs) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def put_CorrelationId(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollByRequestedEventArgs, value: Int32) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    OffsetDelta = property(get_OffsetDelta, None)
    Options = property(get_Options, None)
class ScrollControllerScrollToRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollToRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollToRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgsFactory, offset: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollControllerScrollToRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgs) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def put_CorrelationId(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollControllerScrollToRequestedEventArgs, value: Int32) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    Offset = property(get_Offset, None)
    Options = property(get_Options, None)
class ScrollEventArgs(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventArgs: ...
    @winrt_mixinmethod
    def get_NewValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollEventType(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollEventArgs) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventType: ...
    NewValue = property(get_NewValue, None)
    ScrollEventType = property(get_ScrollEventType, None)
class ScrollEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ff661ba9-8c06-5785-a23c-30d6b31631e8}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventArgs) -> Void: ...
class ScrollEventType(Enum, Int32):
    SmallDecrement = 0
    SmallIncrement = 1
    LargeDecrement = 2
    LargeIncrement = 3
    ThumbPosition = 4
    ThumbTrack = 5
    First = 6
    Last = 7
    EndScroll = 8
class _ScrollPresenter_Meta_(ComPtr.__class__):
    pass
class ScrollPresenter(ComPtr, metaclass=_ScrollPresenter_Meta_):
    extends: win32more.Microsoft.UI.Xaml.FrameworkElement
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter: ...
    @winrt_mixinmethod
    def get_Background(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Background(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_ExpressionAnimationSources(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Composition.CompositionPropertySet: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_ZoomFactor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Single: ...
    @winrt_mixinmethod
    def get_ExtentWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_ExtentHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollableWidth(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollableHeight(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def get_ContentOrientation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingContentOrientation: ...
    @winrt_mixinmethod
    def put_ContentOrientation(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingContentOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalScrollChainMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode: ...
    @winrt_mixinmethod
    def put_HorizontalScrollChainMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalScrollChainMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode: ...
    @winrt_mixinmethod
    def put_VerticalScrollChainMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalScrollRailMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode: ...
    @winrt_mixinmethod
    def put_HorizontalScrollRailMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalScrollRailMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode: ...
    @winrt_mixinmethod
    def put_VerticalScrollRailMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingRailMode) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalScrollMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_mixinmethod
    def put_HorizontalScrollMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalScrollMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_mixinmethod
    def put_VerticalScrollMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode) -> Void: ...
    @winrt_mixinmethod
    def get_ComputedHorizontalScrollMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_mixinmethod
    def get_ComputedVerticalScrollMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollMode: ...
    @winrt_mixinmethod
    def get_ZoomChainMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode: ...
    @winrt_mixinmethod
    def put_ZoomChainMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingChainMode) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomMode: ...
    @winrt_mixinmethod
    def put_ZoomMode(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomMode) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoredInputKinds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingInputKinds: ...
    @winrt_mixinmethod
    def put_IgnoredInputKinds(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.ScrollingInputKinds) -> Void: ...
    @winrt_mixinmethod
    def get_MinZoomFactor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_MinZoomFactor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MaxZoomFactor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_MaxZoomFactor(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.ScrollingInteractionState: ...
    @winrt_mixinmethod
    def get_HorizontalScrollController(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController: ...
    @winrt_mixinmethod
    def put_HorizontalScrollController(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalScrollController(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController: ...
    @winrt_mixinmethod
    def put_VerticalScrollController(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollController) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAnchorRatio(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalAnchorRatio(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAnchorRatio(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalAnchorRatio(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointBase]: ...
    @winrt_mixinmethod
    def get_VerticalSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointBase]: ...
    @winrt_mixinmethod
    def get_ZoomSnapPoints(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPointBase]: ...
    @winrt_mixinmethod
    def ScrollTo(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, horizontalOffset: Double, verticalOffset: Double) -> Int32: ...
    @winrt_mixinmethod
    def ScrollToWithOptions(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, horizontalOffset: Double, verticalOffset: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> Int32: ...
    @winrt_mixinmethod
    def ScrollBy(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, horizontalOffsetDelta: Double, verticalOffsetDelta: Double) -> Int32: ...
    @winrt_mixinmethod
    def ScrollByWithOptions(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, horizontalOffsetDelta: Double, verticalOffsetDelta: Double, options: win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollOptions) -> Int32: ...
    @winrt_mixinmethod
    def AddScrollVelocity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, offsetsVelocity: win32more.Windows.Foundation.Numerics.Vector2, inertiaDecayRate: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Int32: ...
    @winrt_mixinmethod
    def ZoomTo(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, zoomFactor: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Int32: ...
    @winrt_mixinmethod
    def ZoomToWithOptions(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, zoomFactor: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2], options: win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomOptions) -> Int32: ...
    @winrt_mixinmethod
    def ZoomBy(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, zoomFactorDelta: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Int32: ...
    @winrt_mixinmethod
    def ZoomByWithOptions(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, zoomFactorDelta: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2], options: win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomOptions) -> Int32: ...
    @winrt_mixinmethod
    def AddZoomVelocity(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, zoomFactorVelocity: Single, centerPoint: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2], inertiaDecayRate: win32more.Windows.Foundation.IReference[Single]) -> Int32: ...
    @winrt_mixinmethod
    def add_ExtentChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ExtentChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ViewChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ViewChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScrollAnimationStarting(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScrollAnimationStarting(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ZoomAnimationStarting(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ZoomAnimationStarting(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScrollCompleted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingScrollCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScrollCompleted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ZoomCompleted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingZoomCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ZoomCompleted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BringingIntoView(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingBringingIntoViewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BringingIntoView(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AnchorRequested(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, win32more.Microsoft.UI.Xaml.Controls.ScrollingAnchorRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AnchorRequested(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentAnchor(self: win32more.Microsoft.UI.Xaml.Controls.IScrollAnchorProvider) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def RegisterAnchorCandidate(self: win32more.Microsoft.UI.Xaml.Controls.IScrollAnchorProvider, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def UnregisterAnchorCandidate(self: win32more.Microsoft.UI.Xaml.Controls.IScrollAnchorProvider, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_BackgroundProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentOrientationProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalScrollChainModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalScrollChainModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalScrollRailModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalScrollRailModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalScrollModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalScrollModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ComputedHorizontalScrollModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ComputedVerticalScrollModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomChainModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomModeProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IgnoredInputKindsProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinZoomFactorProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxZoomFactorProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalAnchorRatioProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalAnchorRatioProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollPresenterStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Background = property(get_Background, put_Background)
    ComputedHorizontalScrollMode = property(get_ComputedHorizontalScrollMode, None)
    ComputedVerticalScrollMode = property(get_ComputedVerticalScrollMode, None)
    Content = property(get_Content, put_Content)
    ContentOrientation = property(get_ContentOrientation, put_ContentOrientation)
    CurrentAnchor = property(get_CurrentAnchor, None)
    ExpressionAnimationSources = property(get_ExpressionAnimationSources, None)
    ExtentHeight = property(get_ExtentHeight, None)
    ExtentWidth = property(get_ExtentWidth, None)
    HorizontalAnchorRatio = property(get_HorizontalAnchorRatio, put_HorizontalAnchorRatio)
    HorizontalOffset = property(get_HorizontalOffset, None)
    HorizontalScrollChainMode = property(get_HorizontalScrollChainMode, put_HorizontalScrollChainMode)
    HorizontalScrollController = property(get_HorizontalScrollController, put_HorizontalScrollController)
    HorizontalScrollMode = property(get_HorizontalScrollMode, put_HorizontalScrollMode)
    HorizontalScrollRailMode = property(get_HorizontalScrollRailMode, put_HorizontalScrollRailMode)
    HorizontalSnapPoints = property(get_HorizontalSnapPoints, None)
    IgnoredInputKinds = property(get_IgnoredInputKinds, put_IgnoredInputKinds)
    MaxZoomFactor = property(get_MaxZoomFactor, put_MaxZoomFactor)
    MinZoomFactor = property(get_MinZoomFactor, put_MinZoomFactor)
    ScrollableHeight = property(get_ScrollableHeight, None)
    ScrollableWidth = property(get_ScrollableWidth, None)
    State = property(get_State, None)
    VerticalAnchorRatio = property(get_VerticalAnchorRatio, put_VerticalAnchorRatio)
    VerticalOffset = property(get_VerticalOffset, None)
    VerticalScrollChainMode = property(get_VerticalScrollChainMode, put_VerticalScrollChainMode)
    VerticalScrollController = property(get_VerticalScrollController, put_VerticalScrollController)
    VerticalScrollMode = property(get_VerticalScrollMode, put_VerticalScrollMode)
    VerticalScrollRailMode = property(get_VerticalScrollRailMode, put_VerticalScrollRailMode)
    VerticalSnapPoints = property(get_VerticalSnapPoints, None)
    ViewportHeight = property(get_ViewportHeight, None)
    ViewportWidth = property(get_ViewportWidth, None)
    ZoomChainMode = property(get_ZoomChainMode, put_ZoomChainMode)
    ZoomFactor = property(get_ZoomFactor, None)
    ZoomMode = property(get_ZoomMode, put_ZoomMode)
    ZoomSnapPoints = property(get_ZoomSnapPoints, None)
    _ScrollPresenter_Meta_.BackgroundProperty = property(get_BackgroundProperty, None)
    _ScrollPresenter_Meta_.ComputedHorizontalScrollModeProperty = property(get_ComputedHorizontalScrollModeProperty, None)
    _ScrollPresenter_Meta_.ComputedVerticalScrollModeProperty = property(get_ComputedVerticalScrollModeProperty, None)
    _ScrollPresenter_Meta_.ContentOrientationProperty = property(get_ContentOrientationProperty, None)
    _ScrollPresenter_Meta_.ContentProperty = property(get_ContentProperty, None)
    _ScrollPresenter_Meta_.HorizontalAnchorRatioProperty = property(get_HorizontalAnchorRatioProperty, None)
    _ScrollPresenter_Meta_.HorizontalScrollChainModeProperty = property(get_HorizontalScrollChainModeProperty, None)
    _ScrollPresenter_Meta_.HorizontalScrollModeProperty = property(get_HorizontalScrollModeProperty, None)
    _ScrollPresenter_Meta_.HorizontalScrollRailModeProperty = property(get_HorizontalScrollRailModeProperty, None)
    _ScrollPresenter_Meta_.IgnoredInputKindsProperty = property(get_IgnoredInputKindsProperty, None)
    _ScrollPresenter_Meta_.MaxZoomFactorProperty = property(get_MaxZoomFactorProperty, None)
    _ScrollPresenter_Meta_.MinZoomFactorProperty = property(get_MinZoomFactorProperty, None)
    _ScrollPresenter_Meta_.VerticalAnchorRatioProperty = property(get_VerticalAnchorRatioProperty, None)
    _ScrollPresenter_Meta_.VerticalScrollChainModeProperty = property(get_VerticalScrollChainModeProperty, None)
    _ScrollPresenter_Meta_.VerticalScrollModeProperty = property(get_VerticalScrollModeProperty, None)
    _ScrollPresenter_Meta_.VerticalScrollRailModeProperty = property(get_VerticalScrollRailModeProperty, None)
    _ScrollPresenter_Meta_.ZoomChainModeProperty = property(get_ZoomChainModeProperty, None)
    _ScrollPresenter_Meta_.ZoomModeProperty = property(get_ZoomModeProperty, None)
    ExtentChanged = event()
    StateChanged = event()
    ViewChanged = event()
    ScrollAnimationStarting = event()
    ZoomAnimationStarting = event()
    ScrollCompleted = event()
    ZoomCompleted = event()
    BringingIntoView = event()
    AnchorRequested = event()
class ScrollSnapPoint(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPoint
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPoint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPoint.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointFactory, snapPointValue: Double, alignment: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPoint: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPoint) -> Double: ...
    Value = property(get_Value, None)
class ScrollSnapPointBase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointBase
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointBase'
    @winrt_mixinmethod
    def get_Alignment(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IScrollSnapPointBase) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment: ...
    Alignment = property(get_Alignment, None)
class ScrollSnapPointsAlignment(Enum, Int32):
    Near = 0
    Center = 1
    Far = 2
class ScrollingIndicatorMode(Enum, Int32):
    None_ = 0
    TouchIndicator = 1
    MouseIndicator = 2
class _Selector_Meta_(ComPtr.__class__):
    pass
class Selector(ComPtr, metaclass=_Selector_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.ItemsControl
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.Selector'
    @winrt_mixinmethod
    def get_SelectedIndex(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector) -> Int32: ...
    @winrt_mixinmethod
    def put_SelectedIndex(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedItem(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_SelectedItem(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_SelectedValue(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedValuePath(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SelectedValuePath(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsSynchronizedWithCurrentItem(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_IsSynchronizedWithCurrentItem(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def add_SelectionChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector, handler: win32more.Microsoft.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionChanged(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelector, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_SelectedIndexProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedItemProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedValueProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedValuePathProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsSynchronizedWithCurrentItemProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsSelectionActive(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    IsSynchronizedWithCurrentItem = property(get_IsSynchronizedWithCurrentItem, put_IsSynchronizedWithCurrentItem)
    SelectedIndex = property(get_SelectedIndex, put_SelectedIndex)
    SelectedItem = property(get_SelectedItem, put_SelectedItem)
    SelectedValue = property(get_SelectedValue, put_SelectedValue)
    SelectedValuePath = property(get_SelectedValuePath, put_SelectedValuePath)
    _Selector_Meta_.IsSynchronizedWithCurrentItemProperty = property(get_IsSynchronizedWithCurrentItemProperty, None)
    _Selector_Meta_.SelectedIndexProperty = property(get_SelectedIndexProperty, None)
    _Selector_Meta_.SelectedItemProperty = property(get_SelectedItemProperty, None)
    _Selector_Meta_.SelectedValuePathProperty = property(get_SelectedValuePathProperty, None)
    _Selector_Meta_.SelectedValueProperty = property(get_SelectedValueProperty, None)
    SelectionChanged = event()
class _SelectorItem_Meta_(ComPtr.__class__):
    pass
class SelectorItem(ComPtr, metaclass=_SelectorItem_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorItem
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.SelectorItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.SelectorItem.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorItemFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.SelectorItem: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSelected(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorItem, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsSelectedProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISelectorItemStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsSelected = property(get_IsSelected, put_IsSelected)
    _SelectorItem_Meta_.IsSelectedProperty = property(get_IsSelectedProperty, None)
class SliderSnapsTo(Enum, Int32):
    StepValues = 0
    Ticks = 1
class SnapPointBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISnapPointBase
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.SnapPointBase'
class SnapPointsAlignment(Enum, Int32):
    Near = 0
    Center = 1
    Far = 2
class SplitViewTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.SplitViewTemplateSettings'
    @winrt_mixinmethod
    def get_OpenPaneLength(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeOpenPaneLength(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OpenPaneLengthMinusCompactLength(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeOpenPaneLengthMinusCompactLength(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OpenPaneGridLength(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> win32more.Microsoft.UI.Xaml.GridLength: ...
    @winrt_mixinmethod
    def get_CompactPaneGridLength(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> win32more.Microsoft.UI.Xaml.GridLength: ...
    CompactPaneGridLength = property(get_CompactPaneGridLength, None)
    NegativeOpenPaneLength = property(get_NegativeOpenPaneLength, None)
    NegativeOpenPaneLengthMinusCompactLength = property(get_NegativeOpenPaneLengthMinusCompactLength, None)
    OpenPaneGridLength = property(get_OpenPaneGridLength, None)
    OpenPaneLength = property(get_OpenPaneLength, None)
    OpenPaneLengthMinusCompactLength = property(get_OpenPaneLengthMinusCompactLength, None)
class TabViewListView(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.ListView
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ITabViewListView
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.TabViewListView'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.TabViewListView.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ITabViewListViewFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.TabViewListView: ...
class _Thumb_Meta_(ComPtr.__class__):
    pass
class Thumb(ComPtr, metaclass=_Thumb_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Control
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.Thumb'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.Thumb.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.Thumb: ...
    @winrt_mixinmethod
    def get_IsDragging(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb) -> Boolean: ...
    @winrt_mixinmethod
    def add_DragStarted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragStartedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragStarted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragDeltaEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragDelta(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragCompleted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb, handler: win32more.Microsoft.UI.Xaml.Controls.Primitives.DragCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragCompleted(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CancelDrag(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumb) -> Void: ...
    @winrt_classmethod
    def get_IsDraggingProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IThumbStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsDragging = property(get_IsDragging, None)
    _Thumb_Meta_.IsDraggingProperty = property(get_IsDraggingProperty, None)
    DragStarted = event()
    DragDelta = event()
    DragCompleted = event()
class _TickBar_Meta_(ComPtr.__class__):
    pass
class TickBar(ComPtr, metaclass=_TickBar_Meta_):
    extends: win32more.Microsoft.UI.Xaml.FrameworkElement
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.ITickBar
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.TickBar'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.TickBar.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.TickBar: ...
    @winrt_mixinmethod
    def get_Fill(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ITickBar) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Fill(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.ITickBar, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_classmethod
    def get_FillProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.ITickBarStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Fill = property(get_Fill, put_Fill)
    _TickBar_Meta_.FillProperty = property(get_FillProperty, None)
class TickPlacement(Enum, Int32):
    None_ = 0
    TopLeft = 1
    BottomRight = 2
    Outside = 3
    Inline = 4
class _ToggleButton_Meta_(ComPtr.__class__):
    pass
class ToggleButton(ComPtr, metaclass=_ToggleButton_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.ButtonBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ToggleButton'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ToggleButton.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButtonFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ToggleButton: ...
    @winrt_mixinmethod
    def get_IsChecked(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_IsChecked(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_IsThreeState(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsThreeState(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_Checked(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Checked(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Unchecked(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Unchecked(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Indeterminate(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Indeterminate(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OnToggle(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButtonOverrides) -> Void: ...
    @winrt_classmethod
    def get_IsCheckedProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButtonStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsThreeStateProperty(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleButtonStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsChecked = property(get_IsChecked, put_IsChecked)
    IsThreeState = property(get_IsThreeState, put_IsThreeState)
    _ToggleButton_Meta_.IsCheckedProperty = property(get_IsCheckedProperty, None)
    _ToggleButton_Meta_.IsThreeStateProperty = property(get_IsThreeStateProperty, None)
    Checked = event()
    Unchecked = event()
    Indeterminate = event()
class ToggleSwitchTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ToggleSwitchTemplateSettings'
    @winrt_mixinmethod
    def get_KnobCurrentToOnOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_KnobCurrentToOffOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_KnobOnToOffOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_KnobOffToOnOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainCurrentToOnOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainCurrentToOffOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainOnToOffOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainOffToOnOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    CurtainCurrentToOffOffset = property(get_CurtainCurrentToOffOffset, None)
    CurtainCurrentToOnOffset = property(get_CurtainCurrentToOnOffset, None)
    CurtainOffToOnOffset = property(get_CurtainOffToOnOffset, None)
    CurtainOnToOffOffset = property(get_CurtainOnToOffOffset, None)
    KnobCurrentToOffOffset = property(get_KnobCurrentToOffOffset, None)
    KnobCurrentToOnOffset = property(get_KnobCurrentToOnOffset, None)
    KnobOffToOnOffset = property(get_KnobOffToOnOffset, None)
    KnobOnToOffOffset = property(get_KnobOnToOffOffset, None)
class ToolTipTemplateSettings(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ToolTipTemplateSettings'
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings) -> Double: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, None)
    FromVerticalOffset = property(get_FromVerticalOffset, None)
class ZoomSnapPoint(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPointBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPoint
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPoint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPoint.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPointFactory, snapPointValue: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPoint: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPoint) -> Double: ...
    Value = property(get_Value, None)
class ZoomSnapPointBase(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Controls.Primitives.SnapPointBase
    default_interface: win32more.Microsoft.UI.Xaml.Controls.Primitives.IZoomSnapPointBase
    _classid_ = 'Microsoft.UI.Xaml.Controls.Primitives.ZoomSnapPointBase'


make_ready(__name__)
