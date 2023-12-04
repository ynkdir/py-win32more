from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Globalization.Fonts
import win32more.Windows.UI.Text
class ILanguageFont(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Fonts.ILanguageFont'
    _iid_ = Guid('{b12e5c3a-b76d-459b-beeb-901151cd77d1}')
    @winrt_commethod(6)
    def get_FontFamily(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FontWeight(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(8)
    def get_FontStretch(self) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_commethod(9)
    def get_FontStyle(self) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_commethod(10)
    def get_ScaleFactor(self) -> Double: ...
    FontFamily = property(get_FontFamily, None)
    FontWeight = property(get_FontWeight, None)
    FontStretch = property(get_FontStretch, None)
    FontStyle = property(get_FontStyle, None)
    ScaleFactor = property(get_ScaleFactor, None)
class ILanguageFontGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Fonts.ILanguageFontGroup'
    _iid_ = Guid('{f33a7fc3-3a5c-4aea-b9ff-b39fb242f7f6}')
    @winrt_commethod(6)
    def get_UITextFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(7)
    def get_UIHeadingFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(8)
    def get_UITitleFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(9)
    def get_UICaptionFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(10)
    def get_UINotificationHeadingFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(11)
    def get_TraditionalDocumentFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(12)
    def get_ModernDocumentFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(13)
    def get_DocumentHeadingFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(14)
    def get_FixedWidthTextFont(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(15)
    def get_DocumentAlternate1Font(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_commethod(16)
    def get_DocumentAlternate2Font(self) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Fonts.ILanguageFontGroupFactory'
    _iid_ = Guid('{fcaeac67-4e77-49c7-b856-dde934fc735b}')
    @winrt_commethod(6)
    def CreateLanguageFontGroup(self, languageTag: WinRT_String) -> win32more.Windows.Globalization.Fonts.LanguageFontGroup: ...
class LanguageFont(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.Fonts.ILanguageFont
    _classid_ = 'Windows.Globalization.Fonts.LanguageFont'
    @winrt_mixinmethod
    def get_FontFamily(self: win32more.Windows.Globalization.Fonts.ILanguageFont) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FontWeight(self: win32more.Windows.Globalization.Fonts.ILanguageFont) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_mixinmethod
    def get_FontStretch(self: win32more.Windows.Globalization.Fonts.ILanguageFont) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_mixinmethod
    def get_FontStyle(self: win32more.Windows.Globalization.Fonts.ILanguageFont) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_mixinmethod
    def get_ScaleFactor(self: win32more.Windows.Globalization.Fonts.ILanguageFont) -> Double: ...
    FontFamily = property(get_FontFamily, None)
    FontWeight = property(get_FontWeight, None)
    FontStretch = property(get_FontStretch, None)
    FontStyle = property(get_FontStyle, None)
    ScaleFactor = property(get_ScaleFactor, None)
class LanguageFontGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.Fonts.ILanguageFontGroup
    _classid_ = 'Windows.Globalization.Fonts.LanguageFontGroup'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Globalization.Fonts.LanguageFontGroup.CreateLanguageFontGroup(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateLanguageFontGroup(cls: win32more.Windows.Globalization.Fonts.ILanguageFontGroupFactory, languageTag: WinRT_String) -> win32more.Windows.Globalization.Fonts.LanguageFontGroup: ...
    @winrt_mixinmethod
    def get_UITextFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UIHeadingFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UITitleFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UICaptionFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_UINotificationHeadingFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_TraditionalDocumentFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_ModernDocumentFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_DocumentHeadingFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_FixedWidthTextFont(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_DocumentAlternate1Font(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
    @winrt_mixinmethod
    def get_DocumentAlternate2Font(self: win32more.Windows.Globalization.Fonts.ILanguageFontGroup) -> win32more.Windows.Globalization.Fonts.LanguageFont: ...
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
make_ready(__name__)
