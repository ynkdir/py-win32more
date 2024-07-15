from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.UI
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Controls
import win32more.Windows.UI.Xaml.Controls.Primitives
import win32more.Windows.UI.Xaml.Data
import win32more.Windows.UI.Xaml.Input
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.UI.Xaml.Media
import win32more.Windows.UI.Xaml.Media.Animation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AnimationDirection(Enum, Int32):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
class AppBarButtonTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarButtonTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.AppBarButtonTemplateSettings'
    @winrt_mixinmethod
    def get_KeyboardAcceleratorTextMinWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarButtonTemplateSettings) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class AppBarTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.AppBarTemplateSettings'
    @winrt_mixinmethod
    def get_ClipRect(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CompactVerticalDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CompactRootMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_MinimalVerticalDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_MinimalRootMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_HiddenVerticalDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_HiddenRootMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_NegativeCompactVerticalDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings2) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeMinimalVerticalDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings2) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeHiddenVerticalDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings2) -> Double: ...
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
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarToggleButtonTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.AppBarToggleButtonTemplateSettings'
    @winrt_mixinmethod
    def get_KeyboardAcceleratorTextMinWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.IAppBarToggleButtonTemplateSettings) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class _ButtonBase_Meta_(ComPtr.__class__):
    pass
class ButtonBase(ComPtr, metaclass=_ButtonBase_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ButtonBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.ButtonBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ButtonBase: ...
    @winrt_mixinmethod
    def get_ClickMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase) -> win32more.Windows.UI.Xaml.Controls.ClickMode: ...
    @winrt_mixinmethod
    def put_ClickMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase, value: win32more.Windows.UI.Xaml.Controls.ClickMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsPointerOver(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPressed(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase) -> Boolean: ...
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase) -> win32more.Windows.UI.Xaml.Input.ICommand: ...
    @winrt_mixinmethod
    def put_Command(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase, value: win32more.Windows.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_mixinmethod
    def get_CommandParameter(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_CommandParameter(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def add_Click(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Click(self: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ClickModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsPointerOverProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsPressedProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CommandProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CommandParameterProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.Controls.Panel
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarPanel
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.CalendarPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.CalendarPanel.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.CalendarPanel: ...
class CalendarViewTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.CalendarViewTemplateSettings'
    @winrt_mixinmethod
    def get_MinViewWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_HeaderText(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay1(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay2(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay3(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay4(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay5(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay6(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekDay7(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasMoreContentAfter(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasMoreContentBefore(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasMoreViews(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_ClipRect(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings) -> Double: ...
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
    extends: win32more.Windows.UI.Xaml.Controls.VirtualizingPanel
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.CarouselPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.CarouselPanel.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanelFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.CarouselPanel: ...
    @winrt_mixinmethod
    def get_CanVerticallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanVerticallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanHorizontallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanHorizontallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExtentWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ExtentHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollOwner(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_ScrollOwner(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def LineUp(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def LineDown(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def LineLeft(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def LineRight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageUp(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageDown(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageLeft(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def PageRight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelUp(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelDown(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelLeft(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelRight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel) -> Void: ...
    @winrt_mixinmethod
    def SetHorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def SetVerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def MakeVisible(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICarouselPanel, visual: win32more.Windows.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
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
    extends: win32more.Windows.UI.Xaml.Controls.Slider
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IColorPickerSlider
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ColorPickerSlider'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.ColorPickerSlider.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorPickerSliderFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ColorPickerSlider: ...
    @winrt_mixinmethod
    def get_ColorChannel(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorPickerSlider) -> win32more.Windows.UI.Xaml.Controls.ColorPickerHsvChannel: ...
    @winrt_mixinmethod
    def put_ColorChannel(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorPickerSlider, value: win32more.Windows.UI.Xaml.Controls.ColorPickerHsvChannel) -> Void: ...
    @winrt_classmethod
    def get_ColorChannelProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorPickerSliderStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ColorChannel = property(get_ColorChannel, put_ColorChannel)
    _ColorPickerSlider_Meta_.ColorChannelProperty = property(get_ColorChannelProperty, None)
class _ColorSpectrum_Meta_(ComPtr.__class__):
    pass
class ColorSpectrum(ComPtr, metaclass=_ColorSpectrum_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Control
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ColorSpectrum'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.ColorSpectrum.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ColorSpectrum: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_HsvColor(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Windows.Foundation.Numerics.Vector4: ...
    @winrt_mixinmethod
    def put_HsvColor(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def get_MinHue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MinHue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxHue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxHue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinSaturation(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MinSaturation(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSaturation(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxSaturation(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MinValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Windows.UI.Xaml.Controls.ColorSpectrumShape: ...
    @winrt_mixinmethod
    def put_Shape(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Windows.UI.Xaml.Controls.ColorSpectrumShape) -> Void: ...
    @winrt_mixinmethod
    def get_Components(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum) -> win32more.Windows.UI.Xaml.Controls.ColorSpectrumComponents: ...
    @winrt_mixinmethod
    def put_Components(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, value: win32more.Windows.UI.Xaml.Controls.ColorSpectrumComponents) -> Void: ...
    @winrt_mixinmethod
    def add_ColorChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Primitives.ColorSpectrum, win32more.Windows.UI.Xaml.Controls.ColorChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ColorChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrum, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HsvColorProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinHueProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxHueProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinSaturationProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxSaturationProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MinValueProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaxValueProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ShapeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ComponentsProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
class ComboBoxTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ComboBoxTemplateSettings'
    @winrt_mixinmethod
    def get_DropDownOpenedHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_DropDownClosedHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_DropDownOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_SelectedItemDirection(self: win32more.Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    @winrt_mixinmethod
    def get_DropDownContentMinWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings2) -> Double: ...
    DropDownClosedHeight = property(get_DropDownClosedHeight, None)
    DropDownContentMinWidth = property(get_DropDownContentMinWidth, None)
    DropDownOffset = property(get_DropDownOffset, None)
    DropDownOpenedHeight = property(get_DropDownOpenedHeight, None)
    SelectedItemDirection = property(get_SelectedItemDirection, None)
class CommandBarFlyoutCommandBar(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.CommandBar
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar: ...
    @winrt_mixinmethod
    def get_FlyoutTemplateSettings(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar) -> win32more.Windows.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBarTemplateSettings: ...
    FlyoutTemplateSettings = property(get_FlyoutTemplateSettings, None)
class CommandBarFlyoutCommandBarTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBarTemplateSettings'
    @winrt_mixinmethod
    def get_OpenAnimationStartPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OpenAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CloseAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurrentWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandedWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionAnimationStartPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionMoreButtonAnimationStartPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_WidthExpansionMoreButtonAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpOverflowVerticalPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownOverflowVerticalPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpAnimationStartPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandUpAnimationHoldPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownAnimationStartPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ExpandDownAnimationHoldPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ContentClipRect(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_OverflowContentClipRect(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
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
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.CommandBarTemplateSettings'
    @winrt_mixinmethod
    def get_ContentHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentClipRect(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_OverflowContentMinWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentMaxHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentHorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeOverflowContentHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentMaxWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings2) -> Double: ...
    @winrt_mixinmethod
    def get_EffectiveOverflowButtonVisibility(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings3) -> win32more.Windows.UI.Xaml.Visibility: ...
    @winrt_mixinmethod
    def get_OverflowContentCompactYTranslation(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings4) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentMinimalYTranslation(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings4) -> Double: ...
    @winrt_mixinmethod
    def get_OverflowContentHiddenYTranslation(self: win32more.Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings4) -> Double: ...
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
class DragCompletedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.DragCompletedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.DragCompletedEventArgs.CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IDragCompletedEventArgsFactory, horizontalChange: Double, verticalChange: Double, canceled: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.DragCompletedEventArgs: ...
    @winrt_mixinmethod
    def get_HorizontalChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_Canceled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs) -> Boolean: ...
    Canceled = property(get_Canceled, None)
    HorizontalChange = property(get_HorizontalChange, None)
    VerticalChange = property(get_VerticalChange, None)
class DragCompletedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36b28888-19ac-4b4e-9137-a6cf2b023883}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Controls.Primitives.DragCompletedEventArgs) -> Void: ...
class DragDeltaEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.DragDeltaEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.DragDeltaEventArgs.CreateInstanceWithHorizontalChangeAndVerticalChange(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithHorizontalChangeAndVerticalChange(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IDragDeltaEventArgsFactory, horizontalChange: Double, verticalChange: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.DragDeltaEventArgs: ...
    @winrt_mixinmethod
    def get_HorizontalChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs) -> Double: ...
    HorizontalChange = property(get_HorizontalChange, None)
    VerticalChange = property(get_VerticalChange, None)
class DragDeltaEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ac24f9f-ac28-49e9-9189-dccffeb66472}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Controls.Primitives.DragDeltaEventArgs) -> Void: ...
class DragStartedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IDragStartedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.DragStartedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.DragStartedEventArgs.CreateInstanceWithHorizontalOffsetAndVerticalOffset(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithHorizontalOffsetAndVerticalOffset(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IDragStartedEventArgsFactory, horizontalOffset: Double, verticalOffset: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.DragStartedEventArgs: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IDragStartedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IDragStartedEventArgs) -> Double: ...
    HorizontalOffset = property(get_HorizontalOffset, None)
    VerticalOffset = property(get_VerticalOffset, None)
class DragStartedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2eea48a-c65a-495d-a2f1-72c66989142d}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Controls.Primitives.DragStartedEventArgs) -> Void: ...
class EdgeTransitionLocation(Enum, Int32):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
class _FlyoutBase_Meta_(ComPtr.__class__):
    pass
class FlyoutBase(ComPtr, metaclass=_FlyoutBase_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.FlyoutBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_mixinmethod
    def get_Placement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_mixinmethod
    def put_Placement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def add_Opened(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Opening(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opening(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_overload
    @winrt_mixinmethod
    def ShowAt(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, placementTarget: win32more.Windows.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_mixinmethod
    def Hide(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2) -> win32more.Windows.UI.Xaml.FrameworkElement: ...
    @winrt_mixinmethod
    def get_AllowFocusOnInteraction(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusOnInteraction(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LightDismissOverlayMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2) -> win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_mixinmethod
    def put_LightDismissOverlayMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2, value: win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    @winrt_mixinmethod
    def get_AllowFocusWhenDisabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowFocusWhenDisabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ElementSoundMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2) -> win32more.Windows.UI.Xaml.ElementSoundMode: ...
    @winrt_mixinmethod
    def put_ElementSoundMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2, value: win32more.Windows.UI.Xaml.ElementSoundMode) -> Void: ...
    @winrt_mixinmethod
    def add_Closing(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase, win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBaseClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closing(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OverlayInputPassThroughElement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_mixinmethod
    def put_OverlayInputPassThroughElement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    @winrt_mixinmethod
    def TryInvokeKeyboardAccelerator(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase4, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_mixinmethod
    def get_ShowMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_mixinmethod
    def put_ShowMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_mixinmethod
    def get_InputDevicePrefersPrimaryCommands(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreOpenCloseAnimationsEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreOpenCloseAnimationsEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsOpen(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5) -> Boolean: ...
    @ShowAt.register
    @winrt_mixinmethod
    def ShowAt(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5, placementTarget: win32more.Windows.UI.Xaml.DependencyObject, showOptions: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowOptions) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldConstrainToRootBounds(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldConstrainToRootBounds(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsConstrainedToRootBounds(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6) -> Boolean: ...
    @winrt_mixinmethod
    def get_XamlRoot(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6) -> win32more.Windows.UI.Xaml.XamlRoot: ...
    @winrt_mixinmethod
    def put_XamlRoot(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6, value: win32more.Windows.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_mixinmethod
    def CreatePresenter(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides) -> win32more.Windows.UI.Xaml.Controls.Control: ...
    @winrt_mixinmethod
    def OnProcessKeyboardAccelerators(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides4, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
    @winrt_classmethod
    def get_ShouldConstrainToRootBoundsProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics6) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TargetProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ShowModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_InputDevicePrefersPrimaryCommandsProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AreOpenCloseAnimationsEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsOpenProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OverlayInputPassThroughElementProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowFocusOnInteractionProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LightDismissOverlayModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowFocusWhenDisabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ElementSoundModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PlacementProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AttachedFlyoutProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAttachedFlyout(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics, element: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_classmethod
    def SetAttachedFlyout(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics, element: win32more.Windows.UI.Xaml.FrameworkElement, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_classmethod
    def ShowAttachedFlyout(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics, flyoutOwner: win32more.Windows.UI.Xaml.FrameworkElement) -> Void: ...
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
    _FlyoutBase_Meta_.TargetProperty = property(get_TargetProperty, None)
    Opened = event()
    Closed = event()
    Opening = event()
    Closing = event()
class FlyoutBaseClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.FlyoutBaseClosingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs, value: Boolean) -> Void: ...
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
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.FlyoutShowOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowOptions.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptionsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowOptions: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_ExclusionRect(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_ExclusionRect(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    @winrt_mixinmethod
    def get_ShowMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_mixinmethod
    def put_ShowMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_mixinmethod
    def get_Placement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_mixinmethod
    def put_Placement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
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
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IGeneratorPositionHelper
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.GeneratorPositionHelper'
    @winrt_classmethod
    def FromIndexAndOffset(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGeneratorPositionHelperStatics, index: Int32, offset: Int32) -> win32more.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
class _GridViewItemPresenter_Meta_(ComPtr.__class__):
    pass
class GridViewItemPresenter(ComPtr, metaclass=_GridViewItemPresenter_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.ContentPresenter
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.GridViewItemPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.GridViewItemPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.GridViewItemPresenter: ...
    @winrt_mixinmethod
    def get_SelectionCheckMarkVisualEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SelectionCheckMarkVisualEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CheckHintBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckHintBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckSelectingBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckSelectingBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PlaceholderBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBorderThickness(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_SelectedBorderThickness(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_DisabledOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DisabledOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DragOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DragOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReorderHintOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_ReorderHintOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GridViewItemPresenterHorizontalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_mixinmethod
    def put_GridViewItemPresenterHorizontalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_GridViewItemPresenterVerticalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_mixinmethod
    def put_GridViewItemPresenterVerticalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_GridViewItemPresenterPadding(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_GridViewItemPresenterPadding(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackgroundMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_PointerOverBackgroundMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_ContentMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ContentMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_classmethod
    def get_SelectionCheckMarkVisualEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckHintBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckSelectingBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragForegroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PlaceholderBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedForegroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBorderThicknessProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledOpacityProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragOpacityProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ReorderHintOffsetProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GridViewItemPresenterHorizontalContentAlignmentProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GridViewItemPresenterVerticalContentAlignmentProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GridViewItemPresenterPaddingProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundMarginProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentMarginProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.GridViewItemTemplateSettings'
    @winrt_mixinmethod
    def get_DragItemsCount(self: win32more.Windows.UI.Xaml.Controls.Primitives.IGridViewItemTemplateSettings) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class GroupHeaderPlacement(Enum, Int32):
    Top = 0
    Left = 1
class IAppBarButtonTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IAppBarButtonTemplateSettings'
    _iid_ = Guid('{cbc9b39d-0c95-4951-bff2-13963691c366}')
    @winrt_commethod(6)
    def get_KeyboardAcceleratorTextMinWidth(self) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class IAppBarTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings'
    _iid_ = Guid('{bcc2a863-eb35-423c-8389-d7827be3bf67}')
    @winrt_commethod(6)
    def get_ClipRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_CompactVerticalDelta(self) -> Double: ...
    @winrt_commethod(8)
    def get_CompactRootMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(9)
    def get_MinimalVerticalDelta(self) -> Double: ...
    @winrt_commethod(10)
    def get_MinimalRootMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(11)
    def get_HiddenVerticalDelta(self) -> Double: ...
    @winrt_commethod(12)
    def get_HiddenRootMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    ClipRect = property(get_ClipRect, None)
    CompactRootMargin = property(get_CompactRootMargin, None)
    CompactVerticalDelta = property(get_CompactVerticalDelta, None)
    HiddenRootMargin = property(get_HiddenRootMargin, None)
    HiddenVerticalDelta = property(get_HiddenVerticalDelta, None)
    MinimalRootMargin = property(get_MinimalRootMargin, None)
    MinimalVerticalDelta = property(get_MinimalVerticalDelta, None)
class IAppBarTemplateSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IAppBarTemplateSettings2'
    _iid_ = Guid('{cbe66259-0399-5bcc-b925-4d5f5c9a4568}')
    @winrt_commethod(6)
    def get_NegativeCompactVerticalDelta(self) -> Double: ...
    @winrt_commethod(7)
    def get_NegativeMinimalVerticalDelta(self) -> Double: ...
    @winrt_commethod(8)
    def get_NegativeHiddenVerticalDelta(self) -> Double: ...
    NegativeCompactVerticalDelta = property(get_NegativeCompactVerticalDelta, None)
    NegativeHiddenVerticalDelta = property(get_NegativeHiddenVerticalDelta, None)
    NegativeMinimalVerticalDelta = property(get_NegativeMinimalVerticalDelta, None)
class IAppBarToggleButtonTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IAppBarToggleButtonTemplateSettings'
    _iid_ = Guid('{aaf99c48-d8f4-40d9-9fa3-3a64f0fec5d8}')
    @winrt_commethod(6)
    def get_KeyboardAcceleratorTextMinWidth(self) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class IButtonBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IButtonBase'
    _iid_ = Guid('{fa002c1a-494e-46cf-91d4-e14a8d798674}')
    @winrt_commethod(6)
    def get_ClickMode(self) -> win32more.Windows.UI.Xaml.Controls.ClickMode: ...
    @winrt_commethod(7)
    def put_ClickMode(self, value: win32more.Windows.UI.Xaml.Controls.ClickMode) -> Void: ...
    @winrt_commethod(8)
    def get_IsPointerOver(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsPressed(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Command(self) -> win32more.Windows.UI.Xaml.Input.ICommand: ...
    @winrt_commethod(11)
    def put_Command(self, value: win32more.Windows.UI.Xaml.Input.ICommand) -> Void: ...
    @winrt_commethod(12)
    def get_CommandParameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(13)
    def put_CommandParameter(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(14)
    def add_Click(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IButtonBaseFactory'
    _iid_ = Guid('{389b7c71-5220-42b2-9992-2690c1a6702f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ButtonBase: ...
class IButtonBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics'
    _iid_ = Guid('{67ef17e1-fe37-474f-9e97-3b5e0b30f2df}')
    @winrt_commethod(6)
    def get_ClickModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsPointerOverProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsPressedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CommandProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_CommandParameterProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ClickModeProperty = property(get_ClickModeProperty, None)
    CommandParameterProperty = property(get_CommandParameterProperty, None)
    CommandProperty = property(get_CommandProperty, None)
    IsPointerOverProperty = property(get_IsPointerOverProperty, None)
    IsPressedProperty = property(get_IsPressedProperty, None)
class ICalendarPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICalendarPanel'
    _iid_ = Guid('{fcd55a2d-02d3-4ee6-9a90-9df3ead00994}')
class ICalendarViewTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICalendarViewTemplateSettings'
    _iid_ = Guid('{56c71483-64e1-477c-8a0b-cb2f3334b9b0}')
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICarouselPanel'
    _iid_ = Guid('{deab78b2-373b-4151-8785-e544d0d9362b}')
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
    def MakeVisible(self, visual: win32more.Windows.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICarouselPanelFactory'
    _iid_ = Guid('{c1109404-9ae1-440e-a0dd-bbb6e2293cbe}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.CarouselPanel: ...
class IColorPickerSlider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IColorPickerSlider'
    _iid_ = Guid('{94394d83-e0df-4c5f-bbcd-8155f4020440}')
    @winrt_commethod(6)
    def get_ColorChannel(self) -> win32more.Windows.UI.Xaml.Controls.ColorPickerHsvChannel: ...
    @winrt_commethod(7)
    def put_ColorChannel(self, value: win32more.Windows.UI.Xaml.Controls.ColorPickerHsvChannel) -> Void: ...
    ColorChannel = property(get_ColorChannel, put_ColorChannel)
class IColorPickerSliderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IColorPickerSliderFactory'
    _iid_ = Guid('{06d879a2-8c07-4b1e-a940-9fbce8f49639}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ColorPickerSlider: ...
class IColorPickerSliderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IColorPickerSliderStatics'
    _iid_ = Guid('{22eafc6a-9fe3-4eee-8734-a1398ec4413a}')
    @winrt_commethod(6)
    def get_ColorChannelProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ColorChannelProperty = property(get_ColorChannelProperty, None)
class IColorSpectrum(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IColorSpectrum'
    _iid_ = Guid('{ce46f271-f509-4f98-8288-e4942fb385df}')
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
    def get_Shape(self) -> win32more.Windows.UI.Xaml.Controls.ColorSpectrumShape: ...
    @winrt_commethod(23)
    def put_Shape(self, value: win32more.Windows.UI.Xaml.Controls.ColorSpectrumShape) -> Void: ...
    @winrt_commethod(24)
    def get_Components(self) -> win32more.Windows.UI.Xaml.Controls.ColorSpectrumComponents: ...
    @winrt_commethod(25)
    def put_Components(self, value: win32more.Windows.UI.Xaml.Controls.ColorSpectrumComponents) -> Void: ...
    @winrt_commethod(26)
    def add_ColorChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Primitives.ColorSpectrum, win32more.Windows.UI.Xaml.Controls.ColorChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IColorSpectrumFactory'
    _iid_ = Guid('{90c7e61e-904d-42ab-b44f-e68dbf0cdee9}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ColorSpectrum: ...
class IColorSpectrumStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IColorSpectrumStatics'
    _iid_ = Guid('{906bee7c-2cee-4e90-968b-f0a5bd691b4a}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_HsvColorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_MinHueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_MaxHueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_MinSaturationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_MaxSaturationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_MinValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_MaxValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ShapeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_ComponentsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
class IComboBoxTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings'
    _iid_ = Guid('{83285c4e-17f6-4aa3-b61b-e87c718604ea}')
    @winrt_commethod(6)
    def get_DropDownOpenedHeight(self) -> Double: ...
    @winrt_commethod(7)
    def get_DropDownClosedHeight(self) -> Double: ...
    @winrt_commethod(8)
    def get_DropDownOffset(self) -> Double: ...
    @winrt_commethod(9)
    def get_SelectedItemDirection(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.AnimationDirection: ...
    DropDownClosedHeight = property(get_DropDownClosedHeight, None)
    DropDownOffset = property(get_DropDownOffset, None)
    DropDownOpenedHeight = property(get_DropDownOpenedHeight, None)
    SelectedItemDirection = property(get_SelectedItemDirection, None)
class IComboBoxTemplateSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IComboBoxTemplateSettings2'
    _iid_ = Guid('{00e90cd7-68be-449d-b5a7-76e26f703e9b}')
    @winrt_commethod(6)
    def get_DropDownContentMinWidth(self) -> Double: ...
    DropDownContentMinWidth = property(get_DropDownContentMinWidth, None)
class ICommandBarFlyoutCommandBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBar'
    _iid_ = Guid('{14146e7c-38c4-55c4-b706-ce18f6061e7e}')
    @winrt_commethod(6)
    def get_FlyoutTemplateSettings(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBarTemplateSettings: ...
    FlyoutTemplateSettings = property(get_FlyoutTemplateSettings, None)
class ICommandBarFlyoutCommandBarFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarFactory'
    _iid_ = Guid('{f8236f9f-5559-5697-8e6f-20d70ca17dd0}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar: ...
class ICommandBarFlyoutCommandBarTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICommandBarFlyoutCommandBarTemplateSettings'
    _iid_ = Guid('{47642c44-26ff-5d14-9cfc-77dc64f3a447}')
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings'
    _iid_ = Guid('{61c8f92c-05aa-414a-a2ae-482c5a46c08e}')
    @winrt_commethod(6)
    def get_ContentHeight(self) -> Double: ...
    @winrt_commethod(7)
    def get_OverflowContentClipRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_OverflowContentMinWidth(self) -> Double: ...
    @winrt_commethod(9)
    def get_OverflowContentMaxHeight(self) -> Double: ...
    @winrt_commethod(10)
    def get_OverflowContentHorizontalOffset(self) -> Double: ...
    @winrt_commethod(11)
    def get_OverflowContentHeight(self) -> Double: ...
    @winrt_commethod(12)
    def get_NegativeOverflowContentHeight(self) -> Double: ...
    ContentHeight = property(get_ContentHeight, None)
    NegativeOverflowContentHeight = property(get_NegativeOverflowContentHeight, None)
    OverflowContentClipRect = property(get_OverflowContentClipRect, None)
    OverflowContentHeight = property(get_OverflowContentHeight, None)
    OverflowContentHorizontalOffset = property(get_OverflowContentHorizontalOffset, None)
    OverflowContentMaxHeight = property(get_OverflowContentMaxHeight, None)
    OverflowContentMinWidth = property(get_OverflowContentMinWidth, None)
class ICommandBarTemplateSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings2'
    _iid_ = Guid('{fbb24f93-c2e2-4177-a2b6-3cd705073cf6}')
    @winrt_commethod(6)
    def get_OverflowContentMaxWidth(self) -> Double: ...
    OverflowContentMaxWidth = property(get_OverflowContentMaxWidth, None)
class ICommandBarTemplateSettings3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings3'
    _iid_ = Guid('{3bd71eba-3403-4bfe-842d-2ce8c511d245}')
    @winrt_commethod(6)
    def get_EffectiveOverflowButtonVisibility(self) -> win32more.Windows.UI.Xaml.Visibility: ...
    EffectiveOverflowButtonVisibility = property(get_EffectiveOverflowButtonVisibility, None)
class ICommandBarTemplateSettings4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ICommandBarTemplateSettings4'
    _iid_ = Guid('{f2562dd3-aa58-59c5-853b-828a19d1214e}')
    @winrt_commethod(6)
    def get_OverflowContentCompactYTranslation(self) -> Double: ...
    @winrt_commethod(7)
    def get_OverflowContentMinimalYTranslation(self) -> Double: ...
    @winrt_commethod(8)
    def get_OverflowContentHiddenYTranslation(self) -> Double: ...
    OverflowContentCompactYTranslation = property(get_OverflowContentCompactYTranslation, None)
    OverflowContentHiddenYTranslation = property(get_OverflowContentHiddenYTranslation, None)
    OverflowContentMinimalYTranslation = property(get_OverflowContentMinimalYTranslation, None)
class IDragCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IDragCompletedEventArgs'
    _iid_ = Guid('{b04f29a1-bd16-48f6-a511-9c2763641331}')
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IDragCompletedEventArgsFactory'
    _iid_ = Guid('{36a7d99d-148c-495f-a0fc-afc871d62f33}')
    @winrt_commethod(6)
    def CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled(self, horizontalChange: Double, verticalChange: Double, canceled: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.DragCompletedEventArgs: ...
class IDragDeltaEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IDragDeltaEventArgs'
    _iid_ = Guid('{2c2dd73c-2806-49fc-aae9-6d792b572b6a}')
    @winrt_commethod(6)
    def get_HorizontalChange(self) -> Double: ...
    @winrt_commethod(7)
    def get_VerticalChange(self) -> Double: ...
    HorizontalChange = property(get_HorizontalChange, None)
    VerticalChange = property(get_VerticalChange, None)
class IDragDeltaEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IDragDeltaEventArgsFactory'
    _iid_ = Guid('{46e7a1ef-ae15-44a6-8a04-95b0bf9ab876}')
    @winrt_commethod(6)
    def CreateInstanceWithHorizontalChangeAndVerticalChange(self, horizontalChange: Double, verticalChange: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.DragDeltaEventArgs: ...
class IDragStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IDragStartedEventArgs'
    _iid_ = Guid('{9f915dd0-a124-4366-bd85-2408214aeed4}')
    @winrt_commethod(6)
    def get_HorizontalOffset(self) -> Double: ...
    @winrt_commethod(7)
    def get_VerticalOffset(self) -> Double: ...
    HorizontalOffset = property(get_HorizontalOffset, None)
    VerticalOffset = property(get_VerticalOffset, None)
class IDragStartedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IDragStartedEventArgsFactory'
    _iid_ = Guid('{5eefe579-c706-4781-a308-c9e7f4c6a1d7}')
    @winrt_commethod(6)
    def CreateInstanceWithHorizontalOffsetAndVerticalOffset(self, horizontalOffset: Double, verticalOffset: Double, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.DragStartedEventArgs: ...
class IFlyoutBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBase'
    _iid_ = Guid('{723eea0b-d12e-430d-a9f0-9bb32bbf9913}')
    @winrt_commethod(6)
    def get_Placement(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_commethod(7)
    def put_Placement(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
    @winrt_commethod(8)
    def add_Opened(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Opened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Closed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Opening(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Opening(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def ShowAt(self, placementTarget: win32more.Windows.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_commethod(15)
    def Hide(self) -> Void: ...
    Placement = property(get_Placement, put_Placement)
    Opened = event()
    Closed = event()
    Opening = event()
class IFlyoutBase2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2'
    _iid_ = Guid('{f82b435e-65b3-41c6-a9e2-77b67bc4c00c}')
    @winrt_commethod(6)
    def get_Target(self) -> win32more.Windows.UI.Xaml.FrameworkElement: ...
    @winrt_commethod(7)
    def get_AllowFocusOnInteraction(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowFocusOnInteraction(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_LightDismissOverlayMode(self) -> win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_commethod(10)
    def put_LightDismissOverlayMode(self, value: win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    @winrt_commethod(11)
    def get_AllowFocusWhenDisabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_AllowFocusWhenDisabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_ElementSoundMode(self) -> win32more.Windows.UI.Xaml.ElementSoundMode: ...
    @winrt_commethod(14)
    def put_ElementSoundMode(self, value: win32more.Windows.UI.Xaml.ElementSoundMode) -> Void: ...
    @winrt_commethod(15)
    def add_Closing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase, win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBaseClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Closing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AllowFocusOnInteraction = property(get_AllowFocusOnInteraction, put_AllowFocusOnInteraction)
    AllowFocusWhenDisabled = property(get_AllowFocusWhenDisabled, put_AllowFocusWhenDisabled)
    ElementSoundMode = property(get_ElementSoundMode, put_ElementSoundMode)
    LightDismissOverlayMode = property(get_LightDismissOverlayMode, put_LightDismissOverlayMode)
    Target = property(get_Target, None)
    Closing = event()
class IFlyoutBase3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3'
    _iid_ = Guid('{a89c9712-48e0-4240-95b9-0dfd0826a8d3}')
    @winrt_commethod(6)
    def get_OverlayInputPassThroughElement(self) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(7)
    def put_OverlayInputPassThroughElement(self, value: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
    OverlayInputPassThroughElement = property(get_OverlayInputPassThroughElement, put_OverlayInputPassThroughElement)
class IFlyoutBase4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBase4'
    _iid_ = Guid('{e3897d69-a37f-4828-9b70-0ef67c03b5f8}')
    @winrt_commethod(6)
    def TryInvokeKeyboardAccelerator(self, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
class IFlyoutBase5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5'
    _iid_ = Guid('{ad3ec0c7-12bb-5a73-b78e-105192ca73d6}')
    @winrt_commethod(6)
    def get_ShowMode(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_commethod(7)
    def put_ShowMode(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_commethod(8)
    def get_InputDevicePrefersPrimaryCommands(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_AreOpenCloseAnimationsEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_AreOpenCloseAnimationsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsOpen(self) -> Boolean: ...
    @winrt_commethod(12)
    def ShowAt(self, placementTarget: win32more.Windows.UI.Xaml.DependencyObject, showOptions: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowOptions) -> Void: ...
    AreOpenCloseAnimationsEnabled = property(get_AreOpenCloseAnimationsEnabled, put_AreOpenCloseAnimationsEnabled)
    InputDevicePrefersPrimaryCommands = property(get_InputDevicePrefersPrimaryCommands, None)
    IsOpen = property(get_IsOpen, None)
    ShowMode = property(get_ShowMode, put_ShowMode)
class IFlyoutBase6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6'
    _iid_ = Guid('{5399de8c-06cc-5b52-b65a-ff9322d1c940}')
    @winrt_commethod(6)
    def get_ShouldConstrainToRootBounds(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ShouldConstrainToRootBounds(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsConstrainedToRootBounds(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_XamlRoot(self) -> win32more.Windows.UI.Xaml.XamlRoot: ...
    @winrt_commethod(10)
    def put_XamlRoot(self, value: win32more.Windows.UI.Xaml.XamlRoot) -> Void: ...
    IsConstrainedToRootBounds = property(get_IsConstrainedToRootBounds, None)
    ShouldConstrainToRootBounds = property(get_ShouldConstrainToRootBounds, put_ShouldConstrainToRootBounds)
    XamlRoot = property(get_XamlRoot, put_XamlRoot)
class IFlyoutBaseClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs'
    _iid_ = Guid('{d075852d-b09a-4fd1-b005-db2ba01206fb}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    Cancel = property(get_Cancel, put_Cancel)
class IFlyoutBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseFactory'
    _iid_ = Guid('{1c3363d7-fca7-407e-920e-70e15e9f0bf1}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
class IFlyoutBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides'
    _iid_ = Guid('{101dec86-6f4d-45a4-9d0e-3ece6f16977e}')
    @winrt_commethod(6)
    def CreatePresenter(self) -> win32more.Windows.UI.Xaml.Controls.Control: ...
class IFlyoutBaseOverrides4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides4'
    _iid_ = Guid('{a6bfd04d-5ff3-4418-add8-4042a88d2da5}')
    @winrt_commethod(6)
    def OnProcessKeyboardAccelerators(self, args: win32more.Windows.UI.Xaml.Input.ProcessKeyboardAcceleratorEventArgs) -> Void: ...
class IFlyoutBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics'
    _iid_ = Guid('{e2d795e3-85c0-4de2-bac1-5294ca011a78}')
    @winrt_commethod(6)
    def get_PlacementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_AttachedFlyoutProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def GetAttachedFlyout(self, element: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase: ...
    @winrt_commethod(9)
    def SetAttachedFlyout(self, element: win32more.Windows.UI.Xaml.FrameworkElement, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase) -> Void: ...
    @winrt_commethod(10)
    def ShowAttachedFlyout(self, flyoutOwner: win32more.Windows.UI.Xaml.FrameworkElement) -> Void: ...
    AttachedFlyoutProperty = property(get_AttachedFlyoutProperty, None)
    PlacementProperty = property(get_PlacementProperty, None)
class IFlyoutBaseStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2'
    _iid_ = Guid('{a8e913fe-2d60-4307-aad9-56b450121b58}')
    @winrt_commethod(6)
    def get_AllowFocusOnInteractionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LightDismissOverlayModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AllowFocusWhenDisabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ElementSoundModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AllowFocusOnInteractionProperty = property(get_AllowFocusOnInteractionProperty, None)
    AllowFocusWhenDisabledProperty = property(get_AllowFocusWhenDisabledProperty, None)
    ElementSoundModeProperty = property(get_ElementSoundModeProperty, None)
    LightDismissOverlayModeProperty = property(get_LightDismissOverlayModeProperty, None)
class IFlyoutBaseStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics3'
    _iid_ = Guid('{7ba92e4f-dd16-4be4-99db-bd9d4406c0f8}')
    @winrt_commethod(6)
    def get_OverlayInputPassThroughElementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    OverlayInputPassThroughElementProperty = property(get_OverlayInputPassThroughElementProperty, None)
class IFlyoutBaseStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5'
    _iid_ = Guid('{69edb25c-992a-542b-bcff-2f7f855523bd}')
    @winrt_commethod(6)
    def get_TargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ShowModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_InputDevicePrefersPrimaryCommandsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AreOpenCloseAnimationsEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_IsOpenProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AreOpenCloseAnimationsEnabledProperty = property(get_AreOpenCloseAnimationsEnabledProperty, None)
    InputDevicePrefersPrimaryCommandsProperty = property(get_InputDevicePrefersPrimaryCommandsProperty, None)
    IsOpenProperty = property(get_IsOpenProperty, None)
    ShowModeProperty = property(get_ShowModeProperty, None)
    TargetProperty = property(get_TargetProperty, None)
class IFlyoutBaseStatics6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics6'
    _iid_ = Guid('{96d49254-c91b-5246-8b39-afc2a2c50cf8}')
    @winrt_commethod(6)
    def get_ShouldConstrainToRootBoundsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ShouldConstrainToRootBoundsProperty = property(get_ShouldConstrainToRootBoundsProperty, None)
class IFlyoutShowOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions'
    _iid_ = Guid('{57d693ad-0c74-54dd-b110-1ee43fabadd9}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(7)
    def put_Position(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(8)
    def get_ExclusionRect(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_ExclusionRect(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    @winrt_commethod(10)
    def get_ShowMode(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode: ...
    @winrt_commethod(11)
    def put_ShowMode(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode) -> Void: ...
    @winrt_commethod(12)
    def get_Placement(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode: ...
    @winrt_commethod(13)
    def put_Placement(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode) -> Void: ...
    ExclusionRect = property(get_ExclusionRect, put_ExclusionRect)
    Placement = property(get_Placement, put_Placement)
    Position = property(get_Position, put_Position)
    ShowMode = property(get_ShowMode, put_ShowMode)
class IFlyoutShowOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptionsFactory'
    _iid_ = Guid('{ce596f61-2eb4-5b4e-af69-f9af42320eee}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutShowOptions: ...
class IGeneratorPositionHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IGeneratorPositionHelper'
    _iid_ = Guid('{cd40318d-7745-40d9-ab9d-abbda4a7ffea}')
class IGeneratorPositionHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IGeneratorPositionHelperStatics'
    _iid_ = Guid('{ad4095cd-60ec-4588-8d60-39d29097a4df}')
    @winrt_commethod(6)
    def FromIndexAndOffset(self, index: Int32, offset: Int32) -> win32more.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
class IGridViewItemPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenter'
    _iid_ = Guid('{214f9010-56e2-4821-8a1c-2305709af94b}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SelectionCheckMarkVisualEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CheckHintBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_CheckHintBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_CheckSelectingBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(11)
    def put_CheckSelectingBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(12)
    def get_CheckBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(13)
    def put_CheckBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(14)
    def get_DragBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(15)
    def put_DragBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(16)
    def get_DragForeground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_DragForeground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(18)
    def get_FocusBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(19)
    def put_FocusBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(20)
    def get_PlaceholderBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(21)
    def put_PlaceholderBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(22)
    def get_PointerOverBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(23)
    def put_PointerOverBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(24)
    def get_SelectedBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(25)
    def put_SelectedBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(26)
    def get_SelectedForeground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(27)
    def put_SelectedForeground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(28)
    def get_SelectedPointerOverBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(29)
    def put_SelectedPointerOverBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(30)
    def get_SelectedPointerOverBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(31)
    def put_SelectedPointerOverBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(32)
    def get_SelectedBorderThickness(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(33)
    def put_SelectedBorderThickness(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
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
    def get_GridViewItemPresenterHorizontalContentAlignment(self) -> win32more.Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_commethod(41)
    def put_GridViewItemPresenterHorizontalContentAlignment(self, value: win32more.Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_commethod(42)
    def get_GridViewItemPresenterVerticalContentAlignment(self) -> win32more.Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_commethod(43)
    def put_GridViewItemPresenterVerticalContentAlignment(self, value: win32more.Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_commethod(44)
    def get_GridViewItemPresenterPadding(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(45)
    def put_GridViewItemPresenterPadding(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(46)
    def get_PointerOverBackgroundMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(47)
    def put_PointerOverBackgroundMargin(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(48)
    def get_ContentMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(49)
    def put_ContentMargin(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterFactory'
    _iid_ = Guid('{53c12178-63bb-4a65-a3f1-ab114cfc6ffe}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.GridViewItemPresenter: ...
class IGridViewItemPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IGridViewItemPresenterStatics'
    _iid_ = Guid('{e958f8c4-277e-4a72-a01e-9e1688980178}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CheckHintBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CheckSelectingBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CheckBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DragBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_DragForegroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_FocusBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_PlaceholderBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_PointerOverBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_SelectedBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_SelectedForegroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_SelectedPointerOverBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_SelectedPointerOverBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_SelectedBorderThicknessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_DisabledOpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_DragOpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_ReorderHintOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_GridViewItemPresenterHorizontalContentAlignmentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(24)
    def get_GridViewItemPresenterVerticalContentAlignmentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def get_GridViewItemPresenterPaddingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(26)
    def get_PointerOverBackgroundMarginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(27)
    def get_ContentMarginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IGridViewItemTemplateSettings'
    _iid_ = Guid('{9e30baaf-165d-4267-a45e-1a43a75706ac}')
    @winrt_commethod(6)
    def get_DragItemsCount(self) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class IItemsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs'
    _iid_ = Guid('{e8b45568-7d10-421e-be29-81839a91de20}')
    @winrt_commethod(6)
    def get_Action(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
    @winrt_commethod(8)
    def get_OldPosition(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter'
    _iid_ = Guid('{81177858-d224-410c-b16c-c5b6bb6188b2}')
    @winrt_commethod(6)
    def get_Enabled(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Enabled(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Disabled(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_Disabled(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
class IJumpListItemBackgroundConverterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverterStatics'
    _iid_ = Guid('{20e7c3dd-6f27-4808-b0be-83e0e9b5cc45}')
    @winrt_commethod(6)
    def get_EnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_DisabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DisabledProperty = property(get_DisabledProperty, None)
    EnabledProperty = property(get_EnabledProperty, None)
class IJumpListItemForegroundConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter'
    _iid_ = Guid('{1590ed38-c504-4796-a63a-5bfc9eefaae8}')
    @winrt_commethod(6)
    def get_Enabled(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Enabled(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Disabled(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_Disabled(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
class IJumpListItemForegroundConverterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverterStatics'
    _iid_ = Guid('{474e7352-210c-4673-ac6a-413f0e2c7750}')
    @winrt_commethod(6)
    def get_EnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_DisabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DisabledProperty = property(get_DisabledProperty, None)
    EnabledProperty = property(get_EnabledProperty, None)
class ILayoutInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ILayoutInformation'
    _iid_ = Guid('{b5384c9b-c8cf-41b3-bf16-18c8420e72c9}')
class ILayoutInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ILayoutInformationStatics'
    _iid_ = Guid('{cf06cf99-58e9-4682-8326-50caab65ed7c}')
    @winrt_commethod(6)
    def GetLayoutExceptionElement(self, dispatcher: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def GetLayoutSlot(self, element: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.Foundation.Rect: ...
class ILayoutInformationStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ILayoutInformationStatics2'
    _iid_ = Guid('{760315b5-6d4e-4939-ac61-639863cea36b}')
    @winrt_commethod(6)
    def GetAvailableSize(self, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Size: ...
class IListViewItemPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter'
    _iid_ = Guid('{fc8946bd-a3a2-4969-8174-25b5d3c28033}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SelectionCheckMarkVisualEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CheckHintBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_CheckHintBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_CheckSelectingBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(11)
    def put_CheckSelectingBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(12)
    def get_CheckBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(13)
    def put_CheckBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(14)
    def get_DragBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(15)
    def put_DragBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(16)
    def get_DragForeground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_DragForeground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(18)
    def get_FocusBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(19)
    def put_FocusBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(20)
    def get_PlaceholderBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(21)
    def put_PlaceholderBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(22)
    def get_PointerOverBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(23)
    def put_PointerOverBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(24)
    def get_SelectedBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(25)
    def put_SelectedBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(26)
    def get_SelectedForeground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(27)
    def put_SelectedForeground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(28)
    def get_SelectedPointerOverBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(29)
    def put_SelectedPointerOverBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(30)
    def get_SelectedPointerOverBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(31)
    def put_SelectedPointerOverBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(32)
    def get_SelectedBorderThickness(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(33)
    def put_SelectedBorderThickness(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
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
    def get_ListViewItemPresenterHorizontalContentAlignment(self) -> win32more.Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_commethod(41)
    def put_ListViewItemPresenterHorizontalContentAlignment(self, value: win32more.Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_commethod(42)
    def get_ListViewItemPresenterVerticalContentAlignment(self) -> win32more.Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_commethod(43)
    def put_ListViewItemPresenterVerticalContentAlignment(self, value: win32more.Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_commethod(44)
    def get_ListViewItemPresenterPadding(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(45)
    def put_ListViewItemPresenterPadding(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(46)
    def get_PointerOverBackgroundMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(47)
    def put_PointerOverBackgroundMargin(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(48)
    def get_ContentMargin(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(49)
    def put_ContentMargin(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    CheckBrush = property(get_CheckBrush, put_CheckBrush)
    CheckHintBrush = property(get_CheckHintBrush, put_CheckHintBrush)
    CheckSelectingBrush = property(get_CheckSelectingBrush, put_CheckSelectingBrush)
    ContentMargin = property(get_ContentMargin, put_ContentMargin)
    DisabledOpacity = property(get_DisabledOpacity, put_DisabledOpacity)
    DragBackground = property(get_DragBackground, put_DragBackground)
    DragForeground = property(get_DragForeground, put_DragForeground)
    DragOpacity = property(get_DragOpacity, put_DragOpacity)
    FocusBorderBrush = property(get_FocusBorderBrush, put_FocusBorderBrush)
    ListViewItemPresenterHorizontalContentAlignment = property(get_ListViewItemPresenterHorizontalContentAlignment, put_ListViewItemPresenterHorizontalContentAlignment)
    ListViewItemPresenterPadding = property(get_ListViewItemPresenterPadding, put_ListViewItemPresenterPadding)
    ListViewItemPresenterVerticalContentAlignment = property(get_ListViewItemPresenterVerticalContentAlignment, put_ListViewItemPresenterVerticalContentAlignment)
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
class IListViewItemPresenter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2'
    _iid_ = Guid('{f5dc5496-e122-4c57-a625-ac4b08fb2d4c}')
    @winrt_commethod(6)
    def get_SelectedPressedBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_SelectedPressedBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_PressedBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_PressedBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_CheckBoxBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(11)
    def put_CheckBoxBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(12)
    def get_FocusSecondaryBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(13)
    def put_FocusSecondaryBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(14)
    def get_CheckMode(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode: ...
    @winrt_commethod(15)
    def put_CheckMode(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode) -> Void: ...
    @winrt_commethod(16)
    def get_PointerOverForeground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_PointerOverForeground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    CheckBoxBrush = property(get_CheckBoxBrush, put_CheckBoxBrush)
    CheckMode = property(get_CheckMode, put_CheckMode)
    FocusSecondaryBorderBrush = property(get_FocusSecondaryBorderBrush, put_FocusSecondaryBorderBrush)
    PointerOverForeground = property(get_PointerOverForeground, put_PointerOverForeground)
    PressedBackground = property(get_PressedBackground, put_PressedBackground)
    SelectedPressedBackground = property(get_SelectedPressedBackground, put_SelectedPressedBackground)
class IListViewItemPresenter3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3'
    _iid_ = Guid('{36620013-0390-4e30-ad97-8744404f7010}')
    @winrt_commethod(6)
    def get_RevealBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_RevealBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_RevealBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_RevealBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_RevealBorderThickness(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(11)
    def put_RevealBorderThickness(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(12)
    def get_RevealBackgroundShowsAboveContent(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_RevealBackgroundShowsAboveContent(self, value: Boolean) -> Void: ...
    RevealBackground = property(get_RevealBackground, put_RevealBackground)
    RevealBackgroundShowsAboveContent = property(get_RevealBackgroundShowsAboveContent, put_RevealBackgroundShowsAboveContent)
    RevealBorderBrush = property(get_RevealBorderBrush, put_RevealBorderBrush)
    RevealBorderThickness = property(get_RevealBorderThickness, put_RevealBorderThickness)
class IListViewItemPresenter4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4'
    _iid_ = Guid('{da600ac1-adea-5940-a18f-57582f96d99a}')
    @winrt_commethod(6)
    def get_SelectedDisabledBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_SelectedDisabledBackground(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_CheckPressedBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_CheckPressedBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_CheckDisabledBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(11)
    def put_CheckDisabledBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(12)
    def get_CheckBoxPointerOverBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(13)
    def put_CheckBoxPointerOverBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(14)
    def get_CheckBoxPressedBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(15)
    def put_CheckBoxPressedBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(16)
    def get_CheckBoxDisabledBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(17)
    def put_CheckBoxDisabledBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(18)
    def get_CheckBoxSelectedBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(19)
    def put_CheckBoxSelectedBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(20)
    def get_CheckBoxSelectedPointerOverBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(21)
    def put_CheckBoxSelectedPointerOverBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(22)
    def get_CheckBoxSelectedPressedBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(23)
    def put_CheckBoxSelectedPressedBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(24)
    def get_CheckBoxSelectedDisabledBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(25)
    def put_CheckBoxSelectedDisabledBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(26)
    def get_CheckBoxBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(27)
    def put_CheckBoxBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(28)
    def get_CheckBoxPointerOverBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(29)
    def put_CheckBoxPointerOverBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(30)
    def get_CheckBoxPressedBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(31)
    def put_CheckBoxPressedBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(32)
    def get_CheckBoxDisabledBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(33)
    def put_CheckBoxDisabledBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(34)
    def get_CheckBoxCornerRadius(self) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_commethod(35)
    def put_CheckBoxCornerRadius(self, value: win32more.Windows.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_commethod(36)
    def get_SelectionIndicatorCornerRadius(self) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_commethod(37)
    def put_SelectionIndicatorCornerRadius(self, value: win32more.Windows.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_commethod(38)
    def get_SelectionIndicatorVisualEnabled(self) -> Boolean: ...
    @winrt_commethod(39)
    def put_SelectionIndicatorVisualEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(40)
    def get_SelectionIndicatorMode(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode: ...
    @winrt_commethod(41)
    def put_SelectionIndicatorMode(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode) -> Void: ...
    @winrt_commethod(42)
    def get_SelectionIndicatorBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(43)
    def put_SelectionIndicatorBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(44)
    def get_SelectionIndicatorPointerOverBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(45)
    def put_SelectionIndicatorPointerOverBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(46)
    def get_SelectionIndicatorPressedBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(47)
    def put_SelectionIndicatorPressedBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(48)
    def get_SelectionIndicatorDisabledBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(49)
    def put_SelectionIndicatorDisabledBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(50)
    def get_SelectedBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(51)
    def put_SelectedBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(52)
    def get_SelectedPressedBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(53)
    def put_SelectedPressedBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(54)
    def get_SelectedDisabledBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(55)
    def put_SelectedDisabledBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(56)
    def get_SelectedInnerBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(57)
    def put_SelectedInnerBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(58)
    def get_PointerOverBorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(59)
    def put_PointerOverBorderBrush(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    CheckBoxBorderBrush = property(get_CheckBoxBorderBrush, put_CheckBoxBorderBrush)
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
    CheckDisabledBrush = property(get_CheckDisabledBrush, put_CheckDisabledBrush)
    CheckPressedBrush = property(get_CheckPressedBrush, put_CheckPressedBrush)
    PointerOverBorderBrush = property(get_PointerOverBorderBrush, put_PointerOverBorderBrush)
    SelectedBorderBrush = property(get_SelectedBorderBrush, put_SelectedBorderBrush)
    SelectedDisabledBackground = property(get_SelectedDisabledBackground, put_SelectedDisabledBackground)
    SelectedDisabledBorderBrush = property(get_SelectedDisabledBorderBrush, put_SelectedDisabledBorderBrush)
    SelectedInnerBorderBrush = property(get_SelectedInnerBorderBrush, put_SelectedInnerBorderBrush)
    SelectedPressedBorderBrush = property(get_SelectedPressedBorderBrush, put_SelectedPressedBorderBrush)
    SelectionIndicatorBrush = property(get_SelectionIndicatorBrush, put_SelectionIndicatorBrush)
    SelectionIndicatorCornerRadius = property(get_SelectionIndicatorCornerRadius, put_SelectionIndicatorCornerRadius)
    SelectionIndicatorDisabledBrush = property(get_SelectionIndicatorDisabledBrush, put_SelectionIndicatorDisabledBrush)
    SelectionIndicatorMode = property(get_SelectionIndicatorMode, put_SelectionIndicatorMode)
    SelectionIndicatorPointerOverBrush = property(get_SelectionIndicatorPointerOverBrush, put_SelectionIndicatorPointerOverBrush)
    SelectionIndicatorPressedBrush = property(get_SelectionIndicatorPressedBrush, put_SelectionIndicatorPressedBrush)
    SelectionIndicatorVisualEnabled = property(get_SelectionIndicatorVisualEnabled, put_SelectionIndicatorVisualEnabled)
class IListViewItemPresenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterFactory'
    _iid_ = Guid('{e0777cfd-f7e4-4a67-9ac0-a994fcacd020}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter: ...
class IListViewItemPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics'
    _iid_ = Guid('{6504a55a-15dd-42fb-aa5d-2d8ce2e9c294}')
    @winrt_commethod(6)
    def get_SelectionCheckMarkVisualEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CheckHintBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CheckSelectingBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CheckBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DragBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_DragForegroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_FocusBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_PlaceholderBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_PointerOverBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_SelectedBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_SelectedForegroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_SelectedPointerOverBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_SelectedPointerOverBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_SelectedBorderThicknessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_DisabledOpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_DragOpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_ReorderHintOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_ListViewItemPresenterHorizontalContentAlignmentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(24)
    def get_ListViewItemPresenterVerticalContentAlignmentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def get_ListViewItemPresenterPaddingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(26)
    def get_PointerOverBackgroundMarginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(27)
    def get_ContentMarginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CheckBrushProperty = property(get_CheckBrushProperty, None)
    CheckHintBrushProperty = property(get_CheckHintBrushProperty, None)
    CheckSelectingBrushProperty = property(get_CheckSelectingBrushProperty, None)
    ContentMarginProperty = property(get_ContentMarginProperty, None)
    DisabledOpacityProperty = property(get_DisabledOpacityProperty, None)
    DragBackgroundProperty = property(get_DragBackgroundProperty, None)
    DragForegroundProperty = property(get_DragForegroundProperty, None)
    DragOpacityProperty = property(get_DragOpacityProperty, None)
    FocusBorderBrushProperty = property(get_FocusBorderBrushProperty, None)
    ListViewItemPresenterHorizontalContentAlignmentProperty = property(get_ListViewItemPresenterHorizontalContentAlignmentProperty, None)
    ListViewItemPresenterPaddingProperty = property(get_ListViewItemPresenterPaddingProperty, None)
    ListViewItemPresenterVerticalContentAlignmentProperty = property(get_ListViewItemPresenterVerticalContentAlignmentProperty, None)
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
class IListViewItemPresenterStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics2'
    _iid_ = Guid('{4cb3b945-d24d-42a3-9e83-a86d0618bf1b}')
    @winrt_commethod(6)
    def get_SelectedPressedBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PressedBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CheckBoxBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_FocusSecondaryBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_CheckModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_PointerOverForegroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CheckBoxBrushProperty = property(get_CheckBoxBrushProperty, None)
    CheckModeProperty = property(get_CheckModeProperty, None)
    FocusSecondaryBorderBrushProperty = property(get_FocusSecondaryBorderBrushProperty, None)
    PointerOverForegroundProperty = property(get_PointerOverForegroundProperty, None)
    PressedBackgroundProperty = property(get_PressedBackgroundProperty, None)
    SelectedPressedBackgroundProperty = property(get_SelectedPressedBackgroundProperty, None)
class IListViewItemPresenterStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics3'
    _iid_ = Guid('{c3d3d11e-fa26-4ce7-a4ed-ff948f01b7c0}')
    @winrt_commethod(6)
    def get_RevealBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RevealBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RevealBorderThicknessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RevealBackgroundShowsAboveContentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RevealBackgroundProperty = property(get_RevealBackgroundProperty, None)
    RevealBackgroundShowsAboveContentProperty = property(get_RevealBackgroundShowsAboveContentProperty, None)
    RevealBorderBrushProperty = property(get_RevealBorderBrushProperty, None)
    RevealBorderThicknessProperty = property(get_RevealBorderThicknessProperty, None)
class IListViewItemPresenterStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4'
    _iid_ = Guid('{3917159e-74a1-5e7e-a743-e45be9fb919b}')
    @winrt_commethod(6)
    def get_SelectedDisabledBackgroundProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CheckPressedBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CheckDisabledBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CheckBoxPointerOverBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_CheckBoxPressedBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_CheckBoxDisabledBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_CheckBoxSelectedBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_CheckBoxSelectedPointerOverBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_CheckBoxSelectedPressedBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_CheckBoxSelectedDisabledBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_CheckBoxBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_CheckBoxPointerOverBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_CheckBoxPressedBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_CheckBoxDisabledBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_CheckBoxCornerRadiusProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_SelectionIndicatorCornerRadiusProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_SelectionIndicatorVisualEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_SelectionIndicatorModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(24)
    def get_SelectionIndicatorBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def get_SelectionIndicatorPointerOverBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(26)
    def get_SelectionIndicatorPressedBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(27)
    def get_SelectionIndicatorDisabledBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(28)
    def get_SelectedBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(29)
    def get_SelectedPressedBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(30)
    def get_SelectedDisabledBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(31)
    def get_SelectedInnerBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(32)
    def get_PointerOverBorderBrushProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CheckBoxBorderBrushProperty = property(get_CheckBoxBorderBrushProperty, None)
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
    CheckDisabledBrushProperty = property(get_CheckDisabledBrushProperty, None)
    CheckPressedBrushProperty = property(get_CheckPressedBrushProperty, None)
    PointerOverBorderBrushProperty = property(get_PointerOverBorderBrushProperty, None)
    SelectedBorderBrushProperty = property(get_SelectedBorderBrushProperty, None)
    SelectedDisabledBackgroundProperty = property(get_SelectedDisabledBackgroundProperty, None)
    SelectedDisabledBorderBrushProperty = property(get_SelectedDisabledBorderBrushProperty, None)
    SelectedInnerBorderBrushProperty = property(get_SelectedInnerBorderBrushProperty, None)
    SelectedPressedBorderBrushProperty = property(get_SelectedPressedBorderBrushProperty, None)
    SelectionIndicatorBrushProperty = property(get_SelectionIndicatorBrushProperty, None)
    SelectionIndicatorCornerRadiusProperty = property(get_SelectionIndicatorCornerRadiusProperty, None)
    SelectionIndicatorDisabledBrushProperty = property(get_SelectionIndicatorDisabledBrushProperty, None)
    SelectionIndicatorModeProperty = property(get_SelectionIndicatorModeProperty, None)
    SelectionIndicatorPointerOverBrushProperty = property(get_SelectionIndicatorPointerOverBrushProperty, None)
    SelectionIndicatorPressedBrushProperty = property(get_SelectionIndicatorPressedBrushProperty, None)
    SelectionIndicatorVisualEnabledProperty = property(get_SelectionIndicatorVisualEnabledProperty, None)
class IListViewItemTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IListViewItemTemplateSettings'
    _iid_ = Guid('{67af84bf-8279-4686-9326-cd189f27575d}')
    @winrt_commethod(6)
    def get_DragItemsCount(self) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class ILoopingSelector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ILoopingSelector'
    _iid_ = Guid('{4c9a3e04-4827-49d9-8806-093957b0fd21}')
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
    def get_ItemTemplate(self) -> win32more.Windows.UI.Xaml.DataTemplate: ...
    @winrt_commethod(19)
    def put_ItemTemplate(self, value: win32more.Windows.UI.Xaml.DataTemplate) -> Void: ...
    @winrt_commethod(20)
    def add_SelectionChanged(self, handler: win32more.Windows.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorItem'
    _iid_ = Guid('{c69714b9-27c6-4433-9d7c-0dbfb2f4344f}')
class ILoopingSelectorPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorPanel'
    _iid_ = Guid('{40a9ba70-1011-4778-87f7-6bfd20d6377d}')
class ILoopingSelectorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics'
    _iid_ = Guid('{03e8bafa-8c7d-4fc5-b92a-f049fb933cc5}')
    @winrt_commethod(6)
    def get_ShouldLoopProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ItemsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_SelectedIndexProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_SelectedItemProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ItemWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ItemHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_ItemTemplateProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ItemHeightProperty = property(get_ItemHeightProperty, None)
    ItemTemplateProperty = property(get_ItemTemplateProperty, None)
    ItemWidthProperty = property(get_ItemWidthProperty, None)
    ItemsProperty = property(get_ItemsProperty, None)
    SelectedIndexProperty = property(get_SelectedIndexProperty, None)
    SelectedItemProperty = property(get_SelectedItemProperty, None)
    ShouldLoopProperty = property(get_ShouldLoopProperty, None)
class IMenuFlyoutItemTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutItemTemplateSettings'
    _iid_ = Guid('{56ad1809-3a16-4147-81cb-d0b35c834e0f}')
    @winrt_commethod(6)
    def get_KeyboardAcceleratorTextMinWidth(self) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class IMenuFlyoutPresenterTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings'
    _iid_ = Guid('{d68fd00d-629d-4349-ac51-b877c80983b8}')
    @winrt_commethod(6)
    def get_FlyoutContentMinWidth(self) -> Double: ...
    FlyoutContentMinWidth = property(get_FlyoutContentMinWidth, None)
class INavigationViewItemPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter'
    _iid_ = Guid('{9956d3fc-4693-59cb-b6bf-37249058be96}')
    @winrt_commethod(6)
    def get_Icon(self) -> win32more.Windows.UI.Xaml.Controls.IconElement: ...
    @winrt_commethod(7)
    def put_Icon(self, value: win32more.Windows.UI.Xaml.Controls.IconElement) -> Void: ...
    Icon = property(get_Icon, put_Icon)
class INavigationViewItemPresenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterFactory'
    _iid_ = Guid('{bb062c50-4a36-52e7-9459-e89d02f3fc42}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter: ...
class INavigationViewItemPresenterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterStatics'
    _iid_ = Guid('{52814604-cfc1-5ad5-a3aa-fa355be6bd76}')
    @winrt_commethod(6)
    def get_IconProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IconProperty = property(get_IconProperty, None)
class IOrientedVirtualizingPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel'
    _iid_ = Guid('{f077b577-39bd-46ee-bdd7-0826beed71b8}')
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
    def MakeVisible(self, visual: win32more.Windows.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanelFactory'
    _iid_ = Guid('{7b8eaeaf-f92f-439d-9ebf-e9919f56c94d}')
class IPickerFlyoutBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBase'
    _iid_ = Guid('{e33574ea-1076-44d1-9383-dc24ac5cff2a}')
class IPickerFlyoutBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseFactory'
    _iid_ = Guid('{7ec27a53-9502-4beb-b342-00566c8f16b0}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.PickerFlyoutBase: ...
class IPickerFlyoutBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseOverrides'
    _iid_ = Guid('{5bfc4f4a-4822-47b4-a958-77c20ba120d3}')
    @winrt_commethod(6)
    def OnConfirmed(self) -> Void: ...
    @winrt_commethod(7)
    def ShouldShowConfirmationButtons(self) -> Boolean: ...
class IPickerFlyoutBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics'
    _iid_ = Guid('{5a4d0ac5-89ae-40e5-a7f1-bb702355adf3}')
    @winrt_commethod(6)
    def get_TitleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetTitle(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetTitle(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    TitleProperty = property(get_TitleProperty, None)
class IPivotHeaderItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPivotHeaderItem'
    _iid_ = Guid('{594572c2-82aa-410b-9e55-fd8e2c98862d}')
class IPivotHeaderItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPivotHeaderItemFactory'
    _iid_ = Guid('{14308b37-185b-4117-bc77-dda2eb261b99}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.PivotHeaderItem: ...
class IPivotHeaderPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPivotHeaderPanel'
    _iid_ = Guid('{21484ebc-9241-4203-bd37-6c08fb096612}')
class IPivotPanel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPivotPanel'
    _iid_ = Guid('{ad4ebe80-22a9-4ca3-9212-2773b6359ff3}')
class IPopup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopup'
    _iid_ = Guid('{62418240-e6d3-4705-a1dc-39156456ee29}')
    @winrt_commethod(6)
    def get_Child(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(7)
    def put_Child(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
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
    def get_ChildTransitions(self) -> win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_commethod(15)
    def put_ChildTransitions(self, value: win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_commethod(16)
    def get_IsLightDismissEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsLightDismissEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def add_Opened(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_Opened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_Closed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Child = property(get_Child, put_Child)
    ChildTransitions = property(get_ChildTransitions, put_ChildTransitions)
    HorizontalOffset = property(get_HorizontalOffset, put_HorizontalOffset)
    IsLightDismissEnabled = property(get_IsLightDismissEnabled, put_IsLightDismissEnabled)
    IsOpen = property(get_IsOpen, put_IsOpen)
    VerticalOffset = property(get_VerticalOffset, put_VerticalOffset)
    Opened = event()
    Closed = event()
class IPopup2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopup2'
    _iid_ = Guid('{376a8c4c-aac0-4b20-966a-0b9364feb4b5}')
    @winrt_commethod(6)
    def get_LightDismissOverlayMode(self) -> win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_commethod(7)
    def put_LightDismissOverlayMode(self, value: win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    LightDismissOverlayMode = property(get_LightDismissOverlayMode, put_LightDismissOverlayMode)
class IPopup3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopup3'
    _iid_ = Guid('{f9c46915-a65c-5f68-9f54-310a1b51095f}')
    @winrt_commethod(6)
    def get_ShouldConstrainToRootBounds(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ShouldConstrainToRootBounds(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsConstrainedToRootBounds(self) -> Boolean: ...
    IsConstrainedToRootBounds = property(get_IsConstrainedToRootBounds, None)
    ShouldConstrainToRootBounds = property(get_ShouldConstrainToRootBounds, put_ShouldConstrainToRootBounds)
class IPopup4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopup4'
    _iid_ = Guid('{1870b836-df2f-5fc6-a5f2-748ed6ce7321}')
    @winrt_commethod(6)
    def get_PlacementTarget(self) -> win32more.Windows.UI.Xaml.FrameworkElement: ...
    @winrt_commethod(7)
    def put_PlacementTarget(self, value: win32more.Windows.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredPlacement(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_commethod(9)
    def put_DesiredPlacement(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode) -> Void: ...
    @winrt_commethod(10)
    def get_ActualPlacement(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_commethod(11)
    def add_ActualPlacementChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ActualPlacementChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ActualPlacement = property(get_ActualPlacement, None)
    DesiredPlacement = property(get_DesiredPlacement, put_DesiredPlacement)
    PlacementTarget = property(get_PlacementTarget, put_PlacementTarget)
    ActualPlacementChanged = event()
class IPopupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopupStatics'
    _iid_ = Guid('{5ae3bf1a-6e34-40d6-8a7f-ca822aaf59e3}')
    @winrt_commethod(6)
    def get_ChildProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsOpenProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_HorizontalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_VerticalOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ChildTransitionsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_IsLightDismissEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ChildProperty = property(get_ChildProperty, None)
    ChildTransitionsProperty = property(get_ChildTransitionsProperty, None)
    HorizontalOffsetProperty = property(get_HorizontalOffsetProperty, None)
    IsLightDismissEnabledProperty = property(get_IsLightDismissEnabledProperty, None)
    IsOpenProperty = property(get_IsOpenProperty, None)
    VerticalOffsetProperty = property(get_VerticalOffsetProperty, None)
class IPopupStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopupStatics2'
    _iid_ = Guid('{2b9ae9ec-55ef-43b6-b459-12e40ffa4302}')
    @winrt_commethod(6)
    def get_LightDismissOverlayModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    LightDismissOverlayModeProperty = property(get_LightDismissOverlayModeProperty, None)
class IPopupStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopupStatics3'
    _iid_ = Guid('{00789589-c580-558f-945a-7d02ee004d3e}')
    @winrt_commethod(6)
    def get_ShouldConstrainToRootBoundsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ShouldConstrainToRootBoundsProperty = property(get_ShouldConstrainToRootBoundsProperty, None)
class IPopupStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IPopupStatics4'
    _iid_ = Guid('{d1a42c06-8bfa-5164-8554-48bfe6bd4cc6}')
    @winrt_commethod(6)
    def get_PlacementTargetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_DesiredPlacementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DesiredPlacementProperty = property(get_DesiredPlacementProperty, None)
    PlacementTargetProperty = property(get_PlacementTargetProperty, None)
class IProgressBarTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings'
    _iid_ = Guid('{3fe2ea2a-e3f2-4c2b-9488-918d77d2bbe4}')
    @winrt_commethod(6)
    def get_EllipseDiameter(self) -> Double: ...
    @winrt_commethod(7)
    def get_EllipseOffset(self) -> Double: ...
    @winrt_commethod(8)
    def get_EllipseAnimationWellPosition(self) -> Double: ...
    @winrt_commethod(9)
    def get_EllipseAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(10)
    def get_ContainerAnimationStartPosition(self) -> Double: ...
    @winrt_commethod(11)
    def get_ContainerAnimationEndPosition(self) -> Double: ...
    @winrt_commethod(12)
    def get_IndicatorLengthDelta(self) -> Double: ...
    ContainerAnimationEndPosition = property(get_ContainerAnimationEndPosition, None)
    ContainerAnimationStartPosition = property(get_ContainerAnimationStartPosition, None)
    EllipseAnimationEndPosition = property(get_EllipseAnimationEndPosition, None)
    EllipseAnimationWellPosition = property(get_EllipseAnimationWellPosition, None)
    EllipseDiameter = property(get_EllipseDiameter, None)
    EllipseOffset = property(get_EllipseOffset, None)
    IndicatorLengthDelta = property(get_IndicatorLengthDelta, None)
class IProgressRingTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IProgressRingTemplateSettings'
    _iid_ = Guid('{b9b675ec-c723-42e6-83e9-9826272bdc0e}')
    @winrt_commethod(6)
    def get_EllipseDiameter(self) -> Double: ...
    @winrt_commethod(7)
    def get_EllipseOffset(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(8)
    def get_MaxSideLength(self) -> Double: ...
    EllipseDiameter = property(get_EllipseDiameter, None)
    EllipseOffset = property(get_EllipseOffset, None)
    MaxSideLength = property(get_MaxSideLength, None)
class IRangeBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IRangeBase'
    _iid_ = Guid('{fa002c1a-494e-46cf-91d4-e14a8d798675}')
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
    def add_ValueChanged(self, handler: win32more.Windows.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IRangeBaseFactory'
    _iid_ = Guid('{389b7c71-5220-42b2-9992-2690c1a67030}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.RangeBase: ...
class IRangeBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IRangeBaseOverrides'
    _iid_ = Guid('{4291af39-7f0b-4bc2-99c4-06e7062682d8}')
    @winrt_commethod(6)
    def OnMinimumChanged(self, oldMinimum: Double, newMinimum: Double) -> Void: ...
    @winrt_commethod(7)
    def OnMaximumChanged(self, oldMaximum: Double, newMaximum: Double) -> Void: ...
    @winrt_commethod(8)
    def OnValueChanged(self, oldValue: Double, newValue: Double) -> Void: ...
class IRangeBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IRangeBaseStatics'
    _iid_ = Guid('{67ef17e1-fe37-474f-9e97-3b5e0b30f2e0}')
    @winrt_commethod(6)
    def get_MinimumProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MaximumProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_SmallChangeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_LargeChangeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    LargeChangeProperty = property(get_LargeChangeProperty, None)
    MaximumProperty = property(get_MaximumProperty, None)
    MinimumProperty = property(get_MinimumProperty, None)
    SmallChangeProperty = property(get_SmallChangeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IRangeBaseValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs'
    _iid_ = Guid('{a1921777-d5c1-4f9c-a7b0-0401b7e6dc5c}')
    @winrt_commethod(6)
    def get_OldValue(self) -> Double: ...
    @winrt_commethod(7)
    def get_NewValue(self) -> Double: ...
    NewValue = property(get_NewValue, None)
    OldValue = property(get_OldValue, None)
class IRepeatButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IRepeatButton'
    _iid_ = Guid('{02200df9-021a-484a-a93b-0f31020314e5}')
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IRepeatButtonStatics'
    _iid_ = Guid('{3914ac4e-f462-4f73-8197-e8846639c682}')
    @winrt_commethod(6)
    def get_DelayProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IntervalProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DelayProperty = property(get_DelayProperty, None)
    IntervalProperty = property(get_IntervalProperty, None)
class IScrollBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IScrollBar'
    _iid_ = Guid('{f57ae6ca-d1a6-4b90-a4e9-54df1ba8d2ec}')
    @winrt_commethod(6)
    def get_Orientation(self) -> win32more.Windows.UI.Xaml.Controls.Orientation: ...
    @winrt_commethod(7)
    def put_Orientation(self, value: win32more.Windows.UI.Xaml.Controls.Orientation) -> Void: ...
    @winrt_commethod(8)
    def get_ViewportSize(self) -> Double: ...
    @winrt_commethod(9)
    def put_ViewportSize(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_IndicatorMode(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode: ...
    @winrt_commethod(11)
    def put_IndicatorMode(self, value: win32more.Windows.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode) -> Void: ...
    @winrt_commethod(12)
    def add_Scroll(self, handler: win32more.Windows.UI.Xaml.Controls.Primitives.ScrollEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Scroll(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IndicatorMode = property(get_IndicatorMode, put_IndicatorMode)
    Orientation = property(get_Orientation, put_Orientation)
    ViewportSize = property(get_ViewportSize, put_ViewportSize)
    Scroll = event()
class IScrollBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IScrollBarStatics'
    _iid_ = Guid('{45eaf38d-b814-48cf-97f2-539eb16dfd4d}')
    @winrt_commethod(6)
    def get_OrientationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ViewportSizeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IndicatorModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IndicatorModeProperty = property(get_IndicatorModeProperty, None)
    OrientationProperty = property(get_OrientationProperty, None)
    ViewportSizeProperty = property(get_ViewportSizeProperty, None)
class IScrollEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IScrollEventArgs'
    _iid_ = Guid('{c57e5168-3afe-448d-b752-2f364c75d743}')
    @winrt_commethod(6)
    def get_NewValue(self) -> Double: ...
    @winrt_commethod(7)
    def get_ScrollEventType(self) -> win32more.Windows.UI.Xaml.Controls.Primitives.ScrollEventType: ...
    NewValue = property(get_NewValue, None)
    ScrollEventType = property(get_ScrollEventType, None)
class IScrollSnapPointsInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo'
    _iid_ = Guid('{1b5d1336-e61b-4d51-be41-fd8ddc55c58c}')
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
    def GetIrregularSnapPoints(self, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_commethod(13)
    def GetRegularSnapPoints(self, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    AreHorizontalSnapPointsRegular = property(get_AreHorizontalSnapPointsRegular, None)
    AreVerticalSnapPointsRegular = property(get_AreVerticalSnapPointsRegular, None)
    HorizontalSnapPointsChanged = event()
    VerticalSnapPointsChanged = event()
class ISelector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISelector'
    _iid_ = Guid('{e30eb3a5-b36b-42dc-8527-cd25136c083c}')
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
    def add_SelectionChanged(self, handler: win32more.Windows.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISelectorFactory'
    _iid_ = Guid('{c9be2995-d136-4600-b187-8ad56079b48a}')
class ISelectorItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISelectorItem'
    _iid_ = Guid('{541c8d6c-0283-4581-b945-2a64c28a0646}')
    @winrt_commethod(6)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsSelected(self, value: Boolean) -> Void: ...
    IsSelected = property(get_IsSelected, put_IsSelected)
class ISelectorItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISelectorItemFactory'
    _iid_ = Guid('{b9363945-c86a-4b1e-9440-1879378d5313}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.SelectorItem: ...
class ISelectorItemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISelectorItemStatics'
    _iid_ = Guid('{2a353ab8-cbe9-4303-92e7-c8906e218392}')
    @winrt_commethod(6)
    def get_IsSelectedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsSelectedProperty = property(get_IsSelectedProperty, None)
class ISelectorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISelectorStatics'
    _iid_ = Guid('{13300b06-bd10-4e09-bff7-71efb8bbb42b}')
    @winrt_commethod(6)
    def get_SelectedIndexProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SelectedItemProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_SelectedValueProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_SelectedValuePathProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_IsSynchronizedWithCurrentItemProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def GetIsSelectionActive(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    IsSynchronizedWithCurrentItemProperty = property(get_IsSynchronizedWithCurrentItemProperty, None)
    SelectedIndexProperty = property(get_SelectedIndexProperty, None)
    SelectedItemProperty = property(get_SelectedItemProperty, None)
    SelectedValuePathProperty = property(get_SelectedValuePathProperty, None)
    SelectedValueProperty = property(get_SelectedValueProperty, None)
class ISettingsFlyoutTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings'
    _iid_ = Guid('{bcf14c10-cea7-43f1-9d68-57605ded69d4}')
    @winrt_commethod(6)
    def get_HeaderBackground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def get_HeaderForeground(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(8)
    def get_BorderBrush(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def get_BorderThickness(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(10)
    def get_IconSource(self) -> win32more.Windows.UI.Xaml.Media.ImageSource: ...
    @winrt_commethod(11)
    def get_ContentTransitions(self) -> win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    BorderBrush = property(get_BorderBrush, None)
    BorderThickness = property(get_BorderThickness, None)
    ContentTransitions = property(get_ContentTransitions, None)
    HeaderBackground = property(get_HeaderBackground, None)
    HeaderForeground = property(get_HeaderForeground, None)
    IconSource = property(get_IconSource, None)
class ISplitViewTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings'
    _iid_ = Guid('{c16ab5a7-4996-4443-b199-6b6b89124eab}')
    @winrt_commethod(6)
    def get_OpenPaneLength(self) -> Double: ...
    @winrt_commethod(7)
    def get_NegativeOpenPaneLength(self) -> Double: ...
    @winrt_commethod(8)
    def get_OpenPaneLengthMinusCompactLength(self) -> Double: ...
    @winrt_commethod(9)
    def get_NegativeOpenPaneLengthMinusCompactLength(self) -> Double: ...
    @winrt_commethod(10)
    def get_OpenPaneGridLength(self) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(11)
    def get_CompactPaneGridLength(self) -> win32more.Windows.UI.Xaml.GridLength: ...
    CompactPaneGridLength = property(get_CompactPaneGridLength, None)
    NegativeOpenPaneLength = property(get_NegativeOpenPaneLength, None)
    NegativeOpenPaneLengthMinusCompactLength = property(get_NegativeOpenPaneLengthMinusCompactLength, None)
    OpenPaneGridLength = property(get_OpenPaneGridLength, None)
    OpenPaneLength = property(get_OpenPaneLength, None)
    OpenPaneLengthMinusCompactLength = property(get_OpenPaneLengthMinusCompactLength, None)
class IThumb(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IThumb'
    _iid_ = Guid('{e8b2b281-0d6a-45cf-b333-2402b037f099}')
    @winrt_commethod(6)
    def get_IsDragging(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_DragStarted(self, handler: win32more.Windows.UI.Xaml.Controls.Primitives.DragStartedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_DragStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_DragDelta(self, handler: win32more.Windows.UI.Xaml.Controls.Primitives.DragDeltaEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_DragDelta(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_DragCompleted(self, handler: win32more.Windows.UI.Xaml.Controls.Primitives.DragCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IThumbStatics'
    _iid_ = Guid('{955024eb-36f3-4672-a186-baaf626ac4ad}')
    @winrt_commethod(6)
    def get_IsDraggingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsDraggingProperty = property(get_IsDraggingProperty, None)
class ITickBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ITickBar'
    _iid_ = Guid('{994683fa-f1f6-487d-a5ac-c15921bfa995}')
    @winrt_commethod(6)
    def get_Fill(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Fill(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    Fill = property(get_Fill, put_Fill)
class ITickBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ITickBarStatics'
    _iid_ = Guid('{2c6d7e40-799d-4a54-be09-1fefc61d018e}')
    @winrt_commethod(6)
    def get_FillProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FillProperty = property(get_FillProperty, None)
class IToggleButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IToggleButton'
    _iid_ = Guid('{589877fb-0fc7-4036-9d8b-127dfa75c16d}')
    @winrt_commethod(6)
    def get_IsChecked(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(7)
    def put_IsChecked(self, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(8)
    def get_IsThreeState(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsThreeState(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def add_Checked(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Checked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Unchecked(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Unchecked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Indeterminate(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Indeterminate(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsChecked = property(get_IsChecked, put_IsChecked)
    IsThreeState = property(get_IsThreeState, put_IsThreeState)
    Checked = event()
    Unchecked = event()
    Indeterminate = event()
class IToggleButtonFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IToggleButtonFactory'
    _iid_ = Guid('{d56aa2fc-fc7f-449c-9855-7a1055d668a8}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ToggleButton: ...
class IToggleButtonOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IToggleButtonOverrides'
    _iid_ = Guid('{d20e4c28-f18b-491a-9a45-f1a04a9369a4}')
    @winrt_commethod(6)
    def OnToggle(self) -> Void: ...
class IToggleButtonStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IToggleButtonStatics'
    _iid_ = Guid('{af1eab12-0128-4f67-9c5a-82320c445d19}')
    @winrt_commethod(6)
    def get_IsCheckedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsThreeStateProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsCheckedProperty = property(get_IsCheckedProperty, None)
    IsThreeStateProperty = property(get_IsThreeStateProperty, None)
class IToggleSwitchTemplateSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings'
    _iid_ = Guid('{02b7bdcd-628a-4363-86e0-51d6e2e89e58}')
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
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings'
    _iid_ = Guid('{d4388247-0ec4-4506-affd-afac2225b48c}')
    @winrt_commethod(6)
    def get_FromHorizontalOffset(self) -> Double: ...
    @winrt_commethod(7)
    def get_FromVerticalOffset(self) -> Double: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, None)
    FromVerticalOffset = property(get_FromVerticalOffset, None)
class ItemsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ItemsChangedEventArgs'
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
    @winrt_mixinmethod
    def get_OldPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition: ...
    @winrt_mixinmethod
    def get_ItemCount(self: win32more.Windows.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ItemUICount(self: win32more.Windows.UI.Xaml.Controls.Primitives.IItemsChangedEventArgs) -> Int32: ...
    Action = property(get_Action, None)
    ItemCount = property(get_ItemCount, None)
    ItemUICount = property(get_ItemUICount, None)
    OldPosition = property(get_OldPosition, None)
    Position = property(get_Position, None)
class ItemsChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{178257be-a304-482f-8bf0-b9d2e39612a3}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Controls.Primitives.ItemsChangedEventArgs) -> Void: ...
class _JumpListItemBackgroundConverter_Meta_(ComPtr.__class__):
    pass
class JumpListItemBackgroundConverter(ComPtr, metaclass=_JumpListItemBackgroundConverter_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.JumpListItemBackgroundConverter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.JumpListItemBackgroundConverter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.JumpListItemBackgroundConverter: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_Disabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Disabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def Convert(self: win32more.Windows.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def ConvertBack(self: win32more.Windows.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_EnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemBackgroundConverterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
    _JumpListItemBackgroundConverter_Meta_.DisabledProperty = property(get_DisabledProperty, None)
    _JumpListItemBackgroundConverter_Meta_.EnabledProperty = property(get_EnabledProperty, None)
class _JumpListItemForegroundConverter_Meta_(ComPtr.__class__):
    pass
class JumpListItemForegroundConverter(ComPtr, metaclass=_JumpListItemForegroundConverter_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.JumpListItemForegroundConverter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.JumpListItemForegroundConverter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.JumpListItemForegroundConverter: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_Disabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Disabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def Convert(self: win32more.Windows.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def ConvertBack(self: win32more.Windows.UI.Xaml.Data.IValueConverter, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_EnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IJumpListItemForegroundConverterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Disabled = property(get_Disabled, put_Disabled)
    Enabled = property(get_Enabled, put_Enabled)
    _JumpListItemForegroundConverter_Meta_.DisabledProperty = property(get_DisabledProperty, None)
    _JumpListItemForegroundConverter_Meta_.EnabledProperty = property(get_EnabledProperty, None)
class LayoutInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ILayoutInformation
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.LayoutInformation'
    @winrt_classmethod
    def GetAvailableSize(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILayoutInformationStatics2, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Size: ...
    @winrt_classmethod
    def GetLayoutExceptionElement(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILayoutInformationStatics, dispatcher: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def GetLayoutSlot(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILayoutInformationStatics, element: win32more.Windows.UI.Xaml.FrameworkElement) -> win32more.Windows.Foundation.Rect: ...
class _ListViewItemPresenter_Meta_(ComPtr.__class__):
    pass
class ListViewItemPresenter(ComPtr, metaclass=_ListViewItemPresenter_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.ContentPresenter
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter: ...
    @winrt_mixinmethod
    def get_SelectionCheckMarkVisualEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_SelectionCheckMarkVisualEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CheckHintBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckHintBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckSelectingBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckSelectingBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_DragForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_DragForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PlaceholderBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBorderThickness(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_SelectedBorderThickness(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_DisabledOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DisabledOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DragOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_DragOpacity(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReorderHintOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> Double: ...
    @winrt_mixinmethod
    def put_ReorderHintOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ListViewItemPresenterHorizontalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.HorizontalAlignment: ...
    @winrt_mixinmethod
    def put_ListViewItemPresenterHorizontalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.HorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_ListViewItemPresenterVerticalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.VerticalAlignment: ...
    @winrt_mixinmethod
    def put_ListViewItemPresenterVerticalContentAlignment(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.VerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_ListViewItemPresenterPadding(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ListViewItemPresenterPadding(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBackgroundMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_PointerOverBackgroundMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_ContentMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ContentMargin(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPressedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPressedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PressedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PressedBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_FocusSecondaryBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_FocusSecondaryBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2) -> win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode: ...
    @winrt_mixinmethod
    def put_CheckMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2, value: win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter2, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_RevealBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_RevealBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBorderThickness(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_RevealBorderThickness(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def get_RevealBackgroundShowsAboveContent(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3) -> Boolean: ...
    @winrt_mixinmethod
    def put_RevealBackgroundShowsAboveContent(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedDisabledBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedDisabledBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPointerOverBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPointerOverBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedPointerOverBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedPointerOverBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxSelectedDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxSelectedDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxPressedBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxPressedBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxDisabledBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_CheckBoxDisabledBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_CheckBoxCornerRadius(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_mixinmethod
    def put_CheckBoxCornerRadius(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorCornerRadius(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorCornerRadius(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorVisualEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> Boolean: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorVisualEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorPointerOverBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorPointerOverBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorPressedBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionIndicatorDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectionIndicatorDisabledBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedPressedBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedPressedBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedDisabledBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedDisabledBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedInnerBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_SelectedInnerBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_PointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_PointerOverBorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenter4, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_classmethod
    def get_SelectedDisabledBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckPressedBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckDisabledBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPointerOverBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPressedBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxDisabledBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedPointerOverBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedPressedBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxSelectedDisabledBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPointerOverBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxPressedBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxDisabledBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxCornerRadiusProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorCornerRadiusProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorVisualEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorPointerOverBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorPressedBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionIndicatorDisabledBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPressedBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedDisabledBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedInnerBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBorderThicknessProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RevealBackgroundShowsAboveContentProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPressedBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PressedBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBoxBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusSecondaryBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverForegroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectionCheckMarkVisualEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckHintBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckSelectingBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CheckBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragForegroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FocusBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PlaceholderBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedForegroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBackgroundProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedPointerOverBorderBrushProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedBorderThicknessProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DisabledOpacityProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DragOpacityProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ReorderHintOffsetProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ListViewItemPresenterHorizontalContentAlignmentProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ListViewItemPresenterVerticalContentAlignmentProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ListViewItemPresenterPaddingProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointerOverBackgroundMarginProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ContentMarginProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ListViewItemTemplateSettings'
    @winrt_mixinmethod
    def get_DragItemsCount(self: win32more.Windows.UI.Xaml.Controls.Primitives.IListViewItemTemplateSettings) -> Int32: ...
    DragItemsCount = property(get_DragItemsCount, None)
class _LoopingSelector_Meta_(ComPtr.__class__):
    pass
class LoopingSelector(ComPtr, metaclass=_LoopingSelector_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Control
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.LoopingSelector'
    @winrt_mixinmethod
    def get_ShouldLoop(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldLoop(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def put_Items(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedIndex(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Int32: ...
    @winrt_mixinmethod
    def put_SelectedIndex(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedItem(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_SelectedItem(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_ItemWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Int32: ...
    @winrt_mixinmethod
    def put_ItemWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ItemHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector) -> Int32: ...
    @winrt_mixinmethod
    def put_ItemHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ItemTemplate(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector) -> win32more.Windows.UI.Xaml.DataTemplate: ...
    @winrt_mixinmethod
    def put_ItemTemplate(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, value: win32more.Windows.UI.Xaml.DataTemplate) -> Void: ...
    @winrt_mixinmethod
    def add_SelectionChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, handler: win32more.Windows.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelector, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ShouldLoopProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemsProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedIndexProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedItemProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemWidthProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemHeightProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemTemplateProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorItem
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.LoopingSelectorItem'
class LoopingSelectorPanel(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.Canvas
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ILoopingSelectorPanel
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.LoopingSelectorPanel'
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    AreHorizontalSnapPointsRegular = property(get_AreHorizontalSnapPointsRegular, None)
    AreVerticalSnapPointsRegular = property(get_AreVerticalSnapPointsRegular, None)
    HorizontalSnapPointsChanged = event()
    VerticalSnapPointsChanged = event()
class MenuFlyoutItemTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutItemTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.MenuFlyoutItemTemplateSettings'
    @winrt_mixinmethod
    def get_KeyboardAcceleratorTextMinWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutItemTemplateSettings) -> Double: ...
    KeyboardAcceleratorTextMinWidth = property(get_KeyboardAcceleratorTextMinWidth, None)
class MenuFlyoutPresenterTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.MenuFlyoutPresenterTemplateSettings'
    @winrt_mixinmethod
    def get_FlyoutContentMinWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings) -> Double: ...
    FlyoutContentMinWidth = property(get_FlyoutContentMinWidth, None)
class _NavigationViewItemPresenter_Meta_(ComPtr.__class__):
    pass
class NavigationViewItemPresenter(ComPtr, metaclass=_NavigationViewItemPresenter_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.NavigationViewItemPresenter: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter) -> win32more.Windows.UI.Xaml.Controls.IconElement: ...
    @winrt_mixinmethod
    def put_Icon(self: win32more.Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenter, value: win32more.Windows.UI.Xaml.Controls.IconElement) -> Void: ...
    @winrt_classmethod
    def get_IconProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.INavigationViewItemPresenterStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Icon = property(get_Icon, put_Icon)
    _NavigationViewItemPresenter_Meta_.IconProperty = property(get_IconProperty, None)
class OrientedVirtualizingPanel(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.VirtualizingPanel
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.OrientedVirtualizingPanel'
    @winrt_mixinmethod
    def get_CanVerticallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanVerticallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanHorizontallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanHorizontallyScroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExtentWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ExtentHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportWidth(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ViewportHeight(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollOwner(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_ScrollOwner(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def LineUp(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def LineDown(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def LineLeft(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def LineRight(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageUp(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageDown(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageLeft(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def PageRight(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelUp(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelDown(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelLeft(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def MouseWheelRight(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel) -> Void: ...
    @winrt_mixinmethod
    def SetHorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def SetVerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, offset: Double) -> Void: ...
    @winrt_mixinmethod
    def MakeVisible(self: win32more.Windows.UI.Xaml.Controls.Primitives.IOrientedVirtualizingPanel, visual: win32more.Windows.UI.Xaml.UIElement, rectangle: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
    @winrt_mixinmethod
    def GetInsertionIndexes(self: win32more.Windows.UI.Xaml.Controls.IInsertionPanel, position: win32more.Windows.Foundation.Point, first: POINTER(Int32), second: POINTER(Int32)) -> Void: ...
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
    extends: win32more.Windows.UI.Xaml.Controls.Primitives.FlyoutBase
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBase
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.PickerFlyoutBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.PickerFlyoutBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.PickerFlyoutBase: ...
    @winrt_mixinmethod
    def OnConfirmed(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseOverrides) -> Void: ...
    @winrt_mixinmethod
    def ShouldShowConfirmationButtons(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseOverrides) -> Boolean: ...
    @winrt_classmethod
    def get_TitleProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetTitle(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetTitle(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPickerFlyoutBaseStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    _PickerFlyoutBase_Meta_.TitleProperty = property(get_TitleProperty, None)
class PivotHeaderItem(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IPivotHeaderItem
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.PivotHeaderItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.PivotHeaderItem.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPivotHeaderItemFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.PivotHeaderItem: ...
class PivotHeaderPanel(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.Canvas
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IPivotHeaderPanel
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.PivotHeaderPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.PivotHeaderPanel.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.PivotHeaderPanel: ...
class PivotPanel(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.Panel
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IPivotPanel
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.PivotPanel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.PivotPanel.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.PivotPanel: ...
    @winrt_mixinmethod
    def get_AreHorizontalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreVerticalSnapPointsRegular(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo) -> Boolean: ...
    @winrt_mixinmethod
    def add_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HorizontalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VerticalSnapPointsChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetIrregularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def GetRegularSnapPoints(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo, orientation: win32more.Windows.UI.Xaml.Controls.Orientation, alignment: win32more.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment, offset: POINTER(Single)) -> Single: ...
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
    extends: win32more.Windows.UI.Xaml.FrameworkElement
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.Popup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.Popup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.Popup: ...
    @winrt_mixinmethod
    def get_Child(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Child(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def get_IsOpen(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOpen(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup) -> Double: ...
    @winrt_mixinmethod
    def put_VerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ChildTransitions(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup) -> win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    @winrt_mixinmethod
    def put_ChildTransitions(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, value: win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection) -> Void: ...
    @winrt_mixinmethod
    def get_IsLightDismissEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLightDismissEnabled(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_Opened(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_LightDismissOverlayMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup2) -> win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode: ...
    @winrt_mixinmethod
    def put_LightDismissOverlayMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup2, value: win32more.Windows.UI.Xaml.Controls.LightDismissOverlayMode) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldConstrainToRootBounds(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup3) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldConstrainToRootBounds(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsConstrainedToRootBounds(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup3) -> Boolean: ...
    @winrt_mixinmethod
    def get_PlacementTarget(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup4) -> win32more.Windows.UI.Xaml.FrameworkElement: ...
    @winrt_mixinmethod
    def put_PlacementTarget(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup4, value: win32more.Windows.UI.Xaml.FrameworkElement) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredPlacement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup4) -> win32more.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_mixinmethod
    def put_DesiredPlacement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup4, value: win32more.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode) -> Void: ...
    @winrt_mixinmethod
    def get_ActualPlacement(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup4) -> win32more.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode: ...
    @winrt_mixinmethod
    def add_ActualPlacementChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup4, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualPlacementChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IPopup4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_PlacementTargetProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DesiredPlacementProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ShouldConstrainToRootBoundsProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LightDismissOverlayModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsOpenProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HorizontalOffsetProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VerticalOffsetProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildTransitionsProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsLightDismissEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IPopupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
class ProgressBarTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ProgressBarTemplateSettings'
    @winrt_mixinmethod
    def get_EllipseDiameter(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_EllipseOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_EllipseAnimationWellPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_EllipseAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ContainerAnimationStartPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_ContainerAnimationEndPosition(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_IndicatorLengthDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressBarTemplateSettings) -> Double: ...
    ContainerAnimationEndPosition = property(get_ContainerAnimationEndPosition, None)
    ContainerAnimationStartPosition = property(get_ContainerAnimationStartPosition, None)
    EllipseAnimationEndPosition = property(get_EllipseAnimationEndPosition, None)
    EllipseAnimationWellPosition = property(get_EllipseAnimationWellPosition, None)
    EllipseDiameter = property(get_EllipseDiameter, None)
    EllipseOffset = property(get_EllipseOffset, None)
    IndicatorLengthDelta = property(get_IndicatorLengthDelta, None)
class ProgressRingTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressRingTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ProgressRingTemplateSettings'
    @winrt_mixinmethod
    def get_EllipseDiameter(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressRingTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_EllipseOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressRingTemplateSettings) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_MaxSideLength(self: win32more.Windows.UI.Xaml.Controls.Primitives.IProgressRingTemplateSettings) -> Double: ...
    EllipseDiameter = property(get_EllipseDiameter, None)
    EllipseOffset = property(get_EllipseOffset, None)
    MaxSideLength = property(get_MaxSideLength, None)
class _RangeBase_Meta_(ComPtr.__class__):
    pass
class RangeBase(ComPtr, metaclass=_RangeBase_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Control
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.RangeBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.RangeBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.RangeBase: ...
    @winrt_mixinmethod
    def get_Minimum(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_Minimum(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Maximum(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_Maximum(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SmallChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_SmallChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LargeChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_LargeChange(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase) -> Double: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase, value: Double) -> Void: ...
    @winrt_mixinmethod
    def add_ValueChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase, handler: win32more.Windows.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBase, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OnMinimumChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseOverrides, oldMinimum: Double, newMinimum: Double) -> Void: ...
    @winrt_mixinmethod
    def OnMaximumChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseOverrides, oldMaximum: Double, newMaximum: Double) -> Void: ...
    @winrt_mixinmethod
    def OnValueChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseOverrides, oldValue: Double, newValue: Double) -> Void: ...
    @winrt_classmethod
    def get_MinimumProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MaximumProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SmallChangeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LargeChangeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventArgs'
    @winrt_mixinmethod
    def get_OldValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_NewValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRangeBaseValueChangedEventArgs) -> Double: ...
    NewValue = property(get_NewValue, None)
    OldValue = property(get_OldValue, None)
class RangeBaseValueChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e3906fd9-4d1b-4ac8-a43c-c3b908742799}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Controls.Primitives.RangeBaseValueChangedEventArgs) -> Void: ...
class _RepeatButton_Meta_(ComPtr.__class__):
    pass
class RepeatButton(ComPtr, metaclass=_RepeatButton_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Primitives.ButtonBase
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IRepeatButton
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.RepeatButton'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.RepeatButton.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.RepeatButton: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRepeatButton) -> Int32: ...
    @winrt_mixinmethod
    def put_Delay(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRepeatButton, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRepeatButton) -> Int32: ...
    @winrt_mixinmethod
    def put_Interval(self: win32more.Windows.UI.Xaml.Controls.Primitives.IRepeatButton, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_DelayProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRepeatButtonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IntervalProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IRepeatButtonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Delay = property(get_Delay, put_Delay)
    Interval = property(get_Interval, put_Interval)
    _RepeatButton_Meta_.DelayProperty = property(get_DelayProperty, None)
    _RepeatButton_Meta_.IntervalProperty = property(get_IntervalProperty, None)
class _ScrollBar_Meta_(ComPtr.__class__):
    pass
class ScrollBar(ComPtr, metaclass=_ScrollBar_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Primitives.RangeBase
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ScrollBar'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.ScrollBar.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.ScrollBar: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar) -> win32more.Windows.UI.Xaml.Controls.Orientation: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar, value: win32more.Windows.UI.Xaml.Controls.Orientation) -> Void: ...
    @winrt_mixinmethod
    def get_ViewportSize(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar) -> Double: ...
    @winrt_mixinmethod
    def put_ViewportSize(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IndicatorMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar) -> win32more.Windows.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode: ...
    @winrt_mixinmethod
    def put_IndicatorMode(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar, value: win32more.Windows.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode) -> Void: ...
    @winrt_mixinmethod
    def add_Scroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar, handler: win32more.Windows.UI.Xaml.Controls.Primitives.ScrollEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Scroll(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBar, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_OrientationProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBarStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ViewportSizeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBarStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IndicatorModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollBarStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IndicatorMode = property(get_IndicatorMode, put_IndicatorMode)
    Orientation = property(get_Orientation, put_Orientation)
    ViewportSize = property(get_ViewportSize, put_ViewportSize)
    _ScrollBar_Meta_.IndicatorModeProperty = property(get_IndicatorModeProperty, None)
    _ScrollBar_Meta_.OrientationProperty = property(get_OrientationProperty, None)
    _ScrollBar_Meta_.ViewportSizeProperty = property(get_ViewportSizeProperty, None)
    Scroll = event()
class ScrollEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ScrollEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.ScrollEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.ScrollEventArgs: ...
    @winrt_mixinmethod
    def get_NewValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_ScrollEventType(self: win32more.Windows.UI.Xaml.Controls.Primitives.IScrollEventArgs) -> win32more.Windows.UI.Xaml.Controls.Primitives.ScrollEventType: ...
    NewValue = property(get_NewValue, None)
    ScrollEventType = property(get_ScrollEventType, None)
class ScrollEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8860b0a4-a383-4c83-b306-a1c39d7db87f}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Controls.Primitives.ScrollEventArgs) -> Void: ...
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
class ScrollingIndicatorMode(Enum, Int32):
    None_ = 0
    TouchIndicator = 1
    MouseIndicator = 2
class _Selector_Meta_(ComPtr.__class__):
    pass
class Selector(ComPtr, metaclass=_Selector_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.ItemsControl
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.Selector'
    @winrt_mixinmethod
    def get_SelectedIndex(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector) -> Int32: ...
    @winrt_mixinmethod
    def put_SelectedIndex(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedItem(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_SelectedItem(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_SelectedValue(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedValuePath(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SelectedValuePath(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsSynchronizedWithCurrentItem(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_IsSynchronizedWithCurrentItem(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def add_SelectionChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector, handler: win32more.Windows.UI.Xaml.Controls.SelectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionChanged(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelector, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_SelectedIndexProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedItemProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedValueProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SelectedValuePathProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsSynchronizedWithCurrentItemProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsSelectionActive(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
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
    extends: win32more.Windows.UI.Xaml.Controls.ContentControl
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorItem
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.SelectorItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.SelectorItem.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorItemFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.SelectorItem: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSelected(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorItem, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsSelectedProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ISelectorItemStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsSelected = property(get_IsSelected, put_IsSelected)
    _SelectorItem_Meta_.IsSelectedProperty = property(get_IsSelectedProperty, None)
class SettingsFlyoutTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.SettingsFlyoutTemplateSettings'
    @winrt_mixinmethod
    def get_HeaderBackground(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_HeaderForeground(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_BorderBrush(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_BorderThickness(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def get_IconSource(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings) -> win32more.Windows.UI.Xaml.Media.ImageSource: ...
    @winrt_mixinmethod
    def get_ContentTransitions(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISettingsFlyoutTemplateSettings) -> win32more.Windows.UI.Xaml.Media.Animation.TransitionCollection: ...
    BorderBrush = property(get_BorderBrush, None)
    BorderThickness = property(get_BorderThickness, None)
    ContentTransitions = property(get_ContentTransitions, None)
    HeaderBackground = property(get_HeaderBackground, None)
    HeaderForeground = property(get_HeaderForeground, None)
    IconSource = property(get_IconSource, None)
class SliderSnapsTo(Enum, Int32):
    StepValues = 0
    Ticks = 1
class SnapPointsAlignment(Enum, Int32):
    Near = 0
    Center = 1
    Far = 2
class SplitViewTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.SplitViewTemplateSettings'
    @winrt_mixinmethod
    def get_OpenPaneLength(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeOpenPaneLength(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OpenPaneLengthMinusCompactLength(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_NegativeOpenPaneLengthMinusCompactLength(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_OpenPaneGridLength(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_mixinmethod
    def get_CompactPaneGridLength(self: win32more.Windows.UI.Xaml.Controls.Primitives.ISplitViewTemplateSettings) -> win32more.Windows.UI.Xaml.GridLength: ...
    CompactPaneGridLength = property(get_CompactPaneGridLength, None)
    NegativeOpenPaneLength = property(get_NegativeOpenPaneLength, None)
    NegativeOpenPaneLengthMinusCompactLength = property(get_NegativeOpenPaneLengthMinusCompactLength, None)
    OpenPaneGridLength = property(get_OpenPaneGridLength, None)
    OpenPaneLength = property(get_OpenPaneLength, None)
    OpenPaneLengthMinusCompactLength = property(get_OpenPaneLengthMinusCompactLength, None)
class _Thumb_Meta_(ComPtr.__class__):
    pass
class Thumb(ComPtr, metaclass=_Thumb_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Control
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.Thumb'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.Thumb.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.Thumb: ...
    @winrt_mixinmethod
    def get_IsDragging(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb) -> Boolean: ...
    @winrt_mixinmethod
    def add_DragStarted(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb, handler: win32more.Windows.UI.Xaml.Controls.Primitives.DragStartedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragStarted(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb, handler: win32more.Windows.UI.Xaml.Controls.Primitives.DragDeltaEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragDelta(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DragCompleted(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb, handler: win32more.Windows.UI.Xaml.Controls.Primitives.DragCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DragCompleted(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CancelDrag(self: win32more.Windows.UI.Xaml.Controls.Primitives.IThumb) -> Void: ...
    @winrt_classmethod
    def get_IsDraggingProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IThumbStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsDragging = property(get_IsDragging, None)
    _Thumb_Meta_.IsDraggingProperty = property(get_IsDraggingProperty, None)
    DragStarted = event()
    DragDelta = event()
    DragCompleted = event()
class _TickBar_Meta_(ComPtr.__class__):
    pass
class TickBar(ComPtr, metaclass=_TickBar_Meta_):
    extends: win32more.Windows.UI.Xaml.FrameworkElement
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.ITickBar
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.TickBar'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.TickBar.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Primitives.TickBar: ...
    @winrt_mixinmethod
    def get_Fill(self: win32more.Windows.UI.Xaml.Controls.Primitives.ITickBar) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Fill(self: win32more.Windows.UI.Xaml.Controls.Primitives.ITickBar, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_classmethod
    def get_FillProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.ITickBarStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.Controls.Primitives.ButtonBase
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ToggleButton'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Primitives.ToggleButton.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButtonFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Primitives.ToggleButton: ...
    @winrt_mixinmethod
    def get_IsChecked(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_IsChecked(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_IsThreeState(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsThreeState(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_Checked(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Checked(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Unchecked(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Unchecked(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Indeterminate(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Indeterminate(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OnToggle(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButtonOverrides) -> Void: ...
    @winrt_classmethod
    def get_IsCheckedProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButtonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsThreeStateProperty(cls: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleButtonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsChecked = property(get_IsChecked, put_IsChecked)
    IsThreeState = property(get_IsThreeState, put_IsThreeState)
    _ToggleButton_Meta_.IsCheckedProperty = property(get_IsCheckedProperty, None)
    _ToggleButton_Meta_.IsThreeStateProperty = property(get_IsThreeStateProperty, None)
    Checked = event()
    Unchecked = event()
    Indeterminate = event()
class ToggleSwitchTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ToggleSwitchTemplateSettings'
    @winrt_mixinmethod
    def get_KnobCurrentToOnOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_KnobCurrentToOffOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_KnobOnToOffOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_KnobOffToOnOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainCurrentToOnOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainCurrentToOffOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainOnToOffOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_CurtainOffToOnOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToggleSwitchTemplateSettings) -> Double: ...
    CurtainCurrentToOffOffset = property(get_CurtainCurrentToOffOffset, None)
    CurtainCurrentToOnOffset = property(get_CurtainCurrentToOnOffset, None)
    CurtainOffToOnOffset = property(get_CurtainOffToOnOffset, None)
    CurtainOnToOffOffset = property(get_CurtainOnToOffOffset, None)
    KnobCurrentToOffOffset = property(get_KnobCurrentToOffOffset, None)
    KnobCurrentToOnOffset = property(get_KnobCurrentToOnOffset, None)
    KnobOffToOnOffset = property(get_KnobOffToOnOffset, None)
    KnobOnToOffOffset = property(get_KnobOnToOffOffset, None)
class ToolTipTemplateSettings(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings
    _classid_ = 'Windows.UI.Xaml.Controls.Primitives.ToolTipTemplateSettings'
    @winrt_mixinmethod
    def get_FromHorizontalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings) -> Double: ...
    @winrt_mixinmethod
    def get_FromVerticalOffset(self: win32more.Windows.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings) -> Double: ...
    FromHorizontalOffset = property(get_FromHorizontalOffset, None)
    FromVerticalOffset = property(get_FromVerticalOffset, None)


make_ready(__name__)
