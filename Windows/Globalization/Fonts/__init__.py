from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Globalization.Fonts
import Windows.UI.Text
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILanguageFont(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Fonts.ILanguageFont'
    _iid_ = Guid('{b12e5c3a-b76d-459b-beeb-901151cd77d1}')
    @winrt_commethod(6)
    def get_FontFamily(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FontWeight(self) -> Windows.UI.Text.FontWeight: ...
    @winrt_commethod(8)
    def get_FontStretch(self) -> Windows.UI.Text.FontStretch: ...
    @winrt_commethod(9)
    def get_FontStyle(self) -> Windows.UI.Text.FontStyle: ...
    @winrt_commethod(10)
    def get_ScaleFactor(self) -> Double: ...
    FontFamily = property(get_FontFamily, None)
    FontWeight = property(get_FontWeight, None)
    FontStretch = property(get_FontStretch, None)
    FontStyle = property(get_FontStyle, None)
    ScaleFactor = property(get_ScaleFactor, None)
class ILanguageFontGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Fonts.ILanguageFontGroup'
    _iid_ = Guid('{f33a7fc3-3a5c-4aea-b9ff-b39fb242f7f6}')
    @winrt_commethod(6)
    def get_UITextFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(7)
    def get_UIHeadingFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(8)
    def get_UITitleFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(9)
    def get_UICaptionFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(10)
    def get_UINotificationHeadingFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(11)
    def get_TraditionalDocumentFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(12)
    def get_ModernDocumentFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(13)
    def get_DocumentHeadingFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(14)
    def get_FixedWidthTextFont(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(15)
    def get_DocumentAlternate1Font(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(16)
    def get_DocumentAlternate2Font(self) -> Windows.Globalization.Fonts.LanguageFont: ...
    UITextFont = property(get_UITextFont, None)
    UIHeadingFont = property(get_UIHeadingFont, None)
    UITitleFont = property(get_UITitleFont, None)
    UICaptionFont = property(get_UICaptionFont, None)
    UINotificationHeadingFont = property(get_UINotificationHeadingFont, None)
    TraditionalDocumentFont = property(get_TraditionalDocumentFont, None)
    ModernDocumentFont = property(get_ModernDocumentFont, None)
    DocumentHeadingFont = property(get_DocumentHeadingFont, None)
    FixedWidthTextFont = property(get_FixedWidthTextFont, None)
    DocumentAlternate1Font = property(get_DocumentAlternate1Font, None)
    DocumentAlternate2Font = property(get_DocumentAlternate2Font, None)
class ILanguageFontGroupFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Fonts.ILanguageFontGroupFactory'
    _iid_ = Guid('{fcaeac67-4e77-49c7-b856-dde934fc735b}')
    @winrt_commethod(6)
    def CreateLanguageFontGroup(self, languageTag: WinRT_String) -> Windows.Globalization.Fonts.LanguageFontGroup: ...
class LanguageFont(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Globalization.Fonts.ILanguageFont
    _classid_ = 'Windows.Globalization.Fonts.LanguageFont'
    @winrt_mixinmethod
    def get_FontFamily(self: Windows.Globalization.Fonts.ILanguageFont) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FontWeight(self: Windows.Globalization.Fonts.ILanguageFont) -> Windows.UI.Text.FontWeight: ...
    @winrt_mixinmethod
    def get_FontStretch(self: Windows.Globalization.Fonts.ILanguageFont) -> Windows.UI.Text.FontStretch: ...
    @winrt_mixinmethod
    def get_FontStyle(self: Windows.Globalization.Fonts.ILanguageFont) -> Windows.UI.Text.FontStyle: ...
    @winrt_mixinmethod
    def get_ScaleFactor(self: Windows.Globalization.Fonts.ILanguageFont) -> Double: ...
    FontFamily = property(get_FontFamily, None)
    FontWeight = property(get_FontWeight, None)
    FontStretch = property(get_FontStretch, None)
    FontStyle = property(get_FontStyle, None)
    ScaleFactor = property(get_ScaleFactor, None)
class LanguageFontGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Globalization.Fonts.ILanguageFontGroup
    _classid_ = 'Windows.Globalization.Fonts.LanguageFontGroup'
    @winrt_factorymethod
    def CreateLanguageFontGroup(cls: Windows.Globalization.Fonts.ILanguageFontGroupFactory, languageTag: WinRT_String) -> Windows.Globalization.Fonts.LanguageFontGroup: ...
    @winrt_mixinmethod
    def get_UITextFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UIHeadingFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UITitleFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UICaptionFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UINotificationHeadingFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_TraditionalDocumentFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_ModernDocumentFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_DocumentHeadingFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_FixedWidthTextFont(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_DocumentAlternate1Font(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_DocumentAlternate2Font(self: Windows.Globalization.Fonts.ILanguageFontGroup) -> Windows.Globalization.Fonts.LanguageFont: ...
    UITextFont = property(get_UITextFont, None)
    UIHeadingFont = property(get_UIHeadingFont, None)
    UITitleFont = property(get_UITitleFont, None)
    UICaptionFont = property(get_UICaptionFont, None)
    UINotificationHeadingFont = property(get_UINotificationHeadingFont, None)
    TraditionalDocumentFont = property(get_TraditionalDocumentFont, None)
    ModernDocumentFont = property(get_ModernDocumentFont, None)
    DocumentHeadingFont = property(get_DocumentHeadingFont, None)
    FixedWidthTextFont = property(get_FixedWidthTextFont, None)
    DocumentAlternate1Font = property(get_DocumentAlternate1Font, None)
    DocumentAlternate2Font = property(get_DocumentAlternate2Font, None)
make_head(_module, 'ILanguageFont')
make_head(_module, 'ILanguageFontGroup')
make_head(_module, 'ILanguageFontGroupFactory')
make_head(_module, 'LanguageFont')
make_head(_module, 'LanguageFontGroup')
