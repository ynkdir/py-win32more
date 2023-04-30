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
import Windows.Media.ClosedCaptioning
import Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ClosedCaptionColor = Int32
ClosedCaptionColor_Default: ClosedCaptionColor = 0
ClosedCaptionColor_White: ClosedCaptionColor = 1
ClosedCaptionColor_Black: ClosedCaptionColor = 2
ClosedCaptionColor_Red: ClosedCaptionColor = 3
ClosedCaptionColor_Green: ClosedCaptionColor = 4
ClosedCaptionColor_Blue: ClosedCaptionColor = 5
ClosedCaptionColor_Yellow: ClosedCaptionColor = 6
ClosedCaptionColor_Magenta: ClosedCaptionColor = 7
ClosedCaptionColor_Cyan: ClosedCaptionColor = 8
ClosedCaptionEdgeEffect = Int32
ClosedCaptionEdgeEffect_Default: ClosedCaptionEdgeEffect = 0
ClosedCaptionEdgeEffect_None: ClosedCaptionEdgeEffect = 1
ClosedCaptionEdgeEffect_Raised: ClosedCaptionEdgeEffect = 2
ClosedCaptionEdgeEffect_Depressed: ClosedCaptionEdgeEffect = 3
ClosedCaptionEdgeEffect_Uniform: ClosedCaptionEdgeEffect = 4
ClosedCaptionEdgeEffect_DropShadow: ClosedCaptionEdgeEffect = 5
ClosedCaptionOpacity = Int32
ClosedCaptionOpacity_Default: ClosedCaptionOpacity = 0
ClosedCaptionOpacity_OneHundredPercent: ClosedCaptionOpacity = 1
ClosedCaptionOpacity_SeventyFivePercent: ClosedCaptionOpacity = 2
ClosedCaptionOpacity_TwentyFivePercent: ClosedCaptionOpacity = 3
ClosedCaptionOpacity_ZeroPercent: ClosedCaptionOpacity = 4
class ClosedCaptionProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ClosedCaptioning.ClosedCaptionProperties'
    @winrt_classmethod
    def get_FontColor(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_classmethod
    def get_ComputedFontColor(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.UI.Color: ...
    @winrt_classmethod
    def get_FontOpacity(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_classmethod
    def get_FontSize(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionSize: ...
    @winrt_classmethod
    def get_FontStyle(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionStyle: ...
    @winrt_classmethod
    def get_FontEffect(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionEdgeEffect: ...
    @winrt_classmethod
    def get_BackgroundColor(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_classmethod
    def get_ComputedBackgroundColor(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.UI.Color: ...
    @winrt_classmethod
    def get_BackgroundOpacity(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_classmethod
    def get_RegionColor(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_classmethod
    def get_ComputedRegionColor(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.UI.Color: ...
    @winrt_classmethod
    def get_RegionOpacity(cls: Windows.Media.ClosedCaptioning.IClosedCaptionPropertiesStatics) -> Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    FontColor = property(get_FontColor, None)
    ComputedFontColor = property(get_ComputedFontColor, None)
    FontOpacity = property(get_FontOpacity, None)
    FontSize = property(get_FontSize, None)
    FontStyle = property(get_FontStyle, None)
    FontEffect = property(get_FontEffect, None)
    BackgroundColor = property(get_BackgroundColor, None)
    ComputedBackgroundColor = property(get_ComputedBackgroundColor, None)
    BackgroundOpacity = property(get_BackgroundOpacity, None)
    RegionColor = property(get_RegionColor, None)
    ComputedRegionColor = property(get_ComputedRegionColor, None)
    RegionOpacity = property(get_RegionOpacity, None)
ClosedCaptionSize = Int32
ClosedCaptionSize_Default: ClosedCaptionSize = 0
ClosedCaptionSize_FiftyPercent: ClosedCaptionSize = 1
ClosedCaptionSize_OneHundredPercent: ClosedCaptionSize = 2
ClosedCaptionSize_OneHundredFiftyPercent: ClosedCaptionSize = 3
ClosedCaptionSize_TwoHundredPercent: ClosedCaptionSize = 4
ClosedCaptionStyle = Int32
ClosedCaptionStyle_Default: ClosedCaptionStyle = 0
ClosedCaptionStyle_MonospacedWithSerifs: ClosedCaptionStyle = 1
ClosedCaptionStyle_ProportionalWithSerifs: ClosedCaptionStyle = 2
ClosedCaptionStyle_MonospacedWithoutSerifs: ClosedCaptionStyle = 3
ClosedCaptionStyle_ProportionalWithoutSerifs: ClosedCaptionStyle = 4
ClosedCaptionStyle_Casual: ClosedCaptionStyle = 5
ClosedCaptionStyle_Cursive: ClosedCaptionStyle = 6
ClosedCaptionStyle_SmallCapitals: ClosedCaptionStyle = 7
class IClosedCaptionPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('10aa1f84-cc30-4141-b5-03-52-72-28-9e-0c-20')
    @winrt_commethod(6)
    def get_FontColor(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_commethod(7)
    def get_ComputedFontColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(8)
    def get_FontOpacity(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_commethod(9)
    def get_FontSize(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionSize: ...
    @winrt_commethod(10)
    def get_FontStyle(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionStyle: ...
    @winrt_commethod(11)
    def get_FontEffect(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionEdgeEffect: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_commethod(13)
    def get_ComputedBackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(14)
    def get_BackgroundOpacity(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    @winrt_commethod(15)
    def get_RegionColor(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionColor: ...
    @winrt_commethod(16)
    def get_ComputedRegionColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(17)
    def get_RegionOpacity(self) -> Windows.Media.ClosedCaptioning.ClosedCaptionOpacity: ...
    FontColor = property(get_FontColor, None)
    ComputedFontColor = property(get_ComputedFontColor, None)
    FontOpacity = property(get_FontOpacity, None)
    FontSize = property(get_FontSize, None)
    FontStyle = property(get_FontStyle, None)
    FontEffect = property(get_FontEffect, None)
    BackgroundColor = property(get_BackgroundColor, None)
    ComputedBackgroundColor = property(get_ComputedBackgroundColor, None)
    BackgroundOpacity = property(get_BackgroundOpacity, None)
    RegionColor = property(get_RegionColor, None)
    ComputedRegionColor = property(get_ComputedRegionColor, None)
    RegionOpacity = property(get_RegionOpacity, None)
make_head(_module, 'ClosedCaptionProperties')
make_head(_module, 'IClosedCaptionPropertiesStatics')
