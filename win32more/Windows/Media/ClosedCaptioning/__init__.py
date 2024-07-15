from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Media.ClosedCaptioning
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class ClosedCaptionColor(Enum, Int32):
    Default = 0
    White = 1
    Black = 2
    Red = 3
    Green = 4
    Blue = 5
    Yellow = 6
    Magenta = 7
    Cyan = 8
class ClosedCaptionEdgeEffect(Enum, Int32):
    Default = 0
    None_ = 1
    Raised = 2
    Depressed = 3
    Uniform = 4
    DropShadow = 5
class ClosedCaptionOpacity(Enum, Int32):
    Default = 0
    OneHundredPercent = 1
    SeventyFivePercent = 2
    TwentyFivePercent = 3
    ZeroPercent = 4
class _ClosedCaptionProperties_Meta_(ComPtr.__class__):
    pass
class ClosedCaptionProperties(ComPtr, metaclass=_ClosedCaptionProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ClosedCaptioning.ClosedCaptionProperties'
    @winrt_classmethod
    def add_PropertiesChanged(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PropertiesChanged(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_FontColor(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_classmethod
    def get_ComputedFontColor(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.UI.Color: ...
    @winrt_classmethod
    def get_FontOpacity(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_classmethod
    def get_FontSize(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionSize: ...
    @winrt_classmethod
    def get_FontStyle(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionStyle: ...
    @winrt_classmethod
    def get_FontEffect(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionEdgeEffect: ...
    @winrt_classmethod
    def get_BackgroundColor(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_classmethod
    def get_ComputedBackgroundColor(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.UI.Color: ...
    @winrt_classmethod
    def get_BackgroundOpacity(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_classmethod
    def get_RegionColor(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_classmethod
    def get_ComputedRegionColor(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.UI.Color: ...
    @winrt_classmethod
    def get_RegionOpacity(cls: win32more.Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    _ClosedCaptionProperties_Meta_.BackgroundColor = property(get_BackgroundColor, None)
    _ClosedCaptionProperties_Meta_.BackgroundOpacity = property(get_BackgroundOpacity, None)
    _ClosedCaptionProperties_Meta_.ComputedBackgroundColor = property(get_ComputedBackgroundColor, None)
    _ClosedCaptionProperties_Meta_.ComputedFontColor = property(get_ComputedFontColor, None)
    _ClosedCaptionProperties_Meta_.ComputedRegionColor = property(get_ComputedRegionColor, None)
    _ClosedCaptionProperties_Meta_.FontColor = property(get_FontColor, None)
    _ClosedCaptionProperties_Meta_.FontEffect = property(get_FontEffect, None)
    _ClosedCaptionProperties_Meta_.FontOpacity = property(get_FontOpacity, None)
    _ClosedCaptionProperties_Meta_.FontSize = property(get_FontSize, None)
    _ClosedCaptionProperties_Meta_.FontStyle = property(get_FontStyle, None)
    _ClosedCaptionProperties_Meta_.RegionColor = property(get_RegionColor, None)
    _ClosedCaptionProperties_Meta_.RegionOpacity = property(get_RegionOpacity, None)
class ClosedCaptionSize(Enum, Int32):
    Default = 0
    FiftyPercent = 1
    OneHundredPercent = 2
    OneHundredFiftyPercent = 3
    TwoHundredPercent = 4
class ClosedCaptionStyle(Enum, Int32):
    Default = 0
    MonospacedWithSerifs = 1
    ProportionalWithSerifs = 2
    MonospacedWithoutSerifs = 3
    ProportionalWithoutSerifs = 4
    Casual = 5
    Cursive = 6
    SmallCapitals = 7
class IClosedCaptionPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics'
    _iid_ = Guid('{10aa1f84-cc30-4141-b503-5272289e0c20}')
    @winrt_commethod(6)
    def get_FontColor(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_commethod(7)
    def get_ComputedFontColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(8)
    def get_FontOpacity(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_commethod(9)
    def get_FontSize(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionSize: ...
    @winrt_commethod(10)
    def get_FontStyle(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionStyle: ...
    @winrt_commethod(11)
    def get_FontEffect(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionEdgeEffect: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_commethod(13)
    def get_ComputedBackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(14)
    def get_BackgroundOpacity(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_commethod(15)
    def get_RegionColor(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_commethod(16)
    def get_ComputedRegionColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(17)
    def get_RegionOpacity(self) -> win32more.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    BackgroundColor = property(get_BackgroundColor, None)
    BackgroundOpacity = property(get_BackgroundOpacity, None)
    ComputedBackgroundColor = property(get_ComputedBackgroundColor, None)
    ComputedFontColor = property(get_ComputedFontColor, None)
    ComputedRegionColor = property(get_ComputedRegionColor, None)
    FontColor = property(get_FontColor, None)
    FontEffect = property(get_FontEffect, None)
    FontOpacity = property(get_FontOpacity, None)
    FontSize = property(get_FontSize, None)
    FontStyle = property(get_FontStyle, None)
    RegionColor = property(get_RegionColor, None)
    RegionOpacity = property(get_RegionOpacity, None)
class IClosedCaptionPropertiesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics2'
    _iid_ = Guid('{9de26870-37de-4197-8845-9a48dc5ac317}')
    @winrt_commethod(6)
    def add_PropertiesChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PropertiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PropertiesChanged = event()


make_ready(__name__)
