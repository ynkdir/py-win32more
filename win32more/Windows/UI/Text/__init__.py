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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Text
CaretType = Int32
CaretType_Normal: CaretType = 0
CaretType_Null: CaretType = 1
class ContentLinkInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.IContentLinkInfo
    _classid_ = 'Windows.UI.Text.ContentLinkInfo'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Text.ContentLinkInfo.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Text.ContentLinkInfo: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Text.IContentLinkInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Text.IContentLinkInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayText(self: win32more.Windows.UI.Text.IContentLinkInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayText(self: win32more.Windows.UI.Text.IContentLinkInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SecondaryText(self: win32more.Windows.UI.Text.IContentLinkInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SecondaryText(self: win32more.Windows.UI.Text.IContentLinkInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.UI.Text.IContentLinkInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.UI.Text.IContentLinkInfo, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_LinkContentKind(self: win32more.Windows.UI.Text.IContentLinkInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LinkContentKind(self: win32more.Windows.UI.Text.IContentLinkInfo, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    DisplayText = property(get_DisplayText, put_DisplayText)
    SecondaryText = property(get_SecondaryText, put_SecondaryText)
    Uri = property(get_Uri, put_Uri)
    LinkContentKind = property(get_LinkContentKind, put_LinkContentKind)
FindOptions = UInt32
FindOptions_None: FindOptions = 0
FindOptions_Word: FindOptions = 2
FindOptions_Case: FindOptions = 4
FontStretch = Int32
FontStretch_Undefined: FontStretch = 0
FontStretch_UltraCondensed: FontStretch = 1
FontStretch_ExtraCondensed: FontStretch = 2
FontStretch_Condensed: FontStretch = 3
FontStretch_SemiCondensed: FontStretch = 4
FontStretch_Normal: FontStretch = 5
FontStretch_SemiExpanded: FontStretch = 6
FontStretch_Expanded: FontStretch = 7
FontStretch_ExtraExpanded: FontStretch = 8
FontStretch_UltraExpanded: FontStretch = 9
FontStyle = Int32
FontStyle_Normal: FontStyle = 0
FontStyle_Oblique: FontStyle = 1
FontStyle_Italic: FontStyle = 2
class FontWeight(EasyCastStructure):
    Weight: UInt16
class _FontWeights_Meta_(ComPtr.__class__):
    pass
class FontWeights(ComPtr, metaclass=_FontWeights_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.IFontWeights
    _classid_ = 'Windows.UI.Text.FontWeights'
    @winrt_classmethod
    def get_Black(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_Bold(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_ExtraBlack(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_ExtraBold(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_ExtraLight(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_Light(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_Medium(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_Normal(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_SemiBold(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_SemiLight(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_classmethod
    def get_Thin(cls: win32more.Windows.UI.Text.IFontWeightsStatics) -> win32more.Windows.UI.Text.FontWeight: ...
    _FontWeights_Meta_.Black = property(get_Black.__wrapped__, None)
    _FontWeights_Meta_.Bold = property(get_Bold.__wrapped__, None)
    _FontWeights_Meta_.ExtraBlack = property(get_ExtraBlack.__wrapped__, None)
    _FontWeights_Meta_.ExtraBold = property(get_ExtraBold.__wrapped__, None)
    _FontWeights_Meta_.ExtraLight = property(get_ExtraLight.__wrapped__, None)
    _FontWeights_Meta_.Light = property(get_Light.__wrapped__, None)
    _FontWeights_Meta_.Medium = property(get_Medium.__wrapped__, None)
    _FontWeights_Meta_.Normal = property(get_Normal.__wrapped__, None)
    _FontWeights_Meta_.SemiBold = property(get_SemiBold.__wrapped__, None)
    _FontWeights_Meta_.SemiLight = property(get_SemiLight.__wrapped__, None)
    _FontWeights_Meta_.Thin = property(get_Thin.__wrapped__, None)
FormatEffect = Int32
FormatEffect_Off: FormatEffect = 0
FormatEffect_On: FormatEffect = 1
FormatEffect_Toggle: FormatEffect = 2
FormatEffect_Undefined: FormatEffect = 3
HorizontalCharacterAlignment = Int32
HorizontalCharacterAlignment_Left: HorizontalCharacterAlignment = 0
HorizontalCharacterAlignment_Right: HorizontalCharacterAlignment = 1
HorizontalCharacterAlignment_Center: HorizontalCharacterAlignment = 2
class IContentLinkInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.IContentLinkInfo'
    _iid_ = Guid('{1ed52525-1c5f-48cb-b335-78b50a2ee642}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_Id(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SecondaryText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_SecondaryText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(13)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(14)
    def get_LinkContentKind(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_LinkContentKind(self, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    DisplayText = property(get_DisplayText, put_DisplayText)
    SecondaryText = property(get_SecondaryText, put_SecondaryText)
    Uri = property(get_Uri, put_Uri)
    LinkContentKind = property(get_LinkContentKind, put_LinkContentKind)
class IFontWeights(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.IFontWeights'
    _iid_ = Guid('{7880a444-01ab-4997-8517-df822a0c45f1}')
class IFontWeightsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.IFontWeightsStatics'
    _iid_ = Guid('{b3b579d5-1ba9-48eb-9dad-c095e8c23ba3}')
    @winrt_commethod(6)
    def get_Black(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(7)
    def get_Bold(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(8)
    def get_ExtraBlack(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(9)
    def get_ExtraBold(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(10)
    def get_ExtraLight(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(11)
    def get_Light(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(12)
    def get_Medium(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(13)
    def get_Normal(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(14)
    def get_SemiBold(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(15)
    def get_SemiLight(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(16)
    def get_Thin(self) -> win32more.Windows.UI.Text.FontWeight: ...
    Black = property(get_Black, None)
    Bold = property(get_Bold, None)
    ExtraBlack = property(get_ExtraBlack, None)
    ExtraBold = property(get_ExtraBold, None)
    ExtraLight = property(get_ExtraLight, None)
    Light = property(get_Light, None)
    Medium = property(get_Medium, None)
    Normal = property(get_Normal, None)
    SemiBold = property(get_SemiBold, None)
    SemiLight = property(get_SemiLight, None)
    Thin = property(get_Thin, None)
class IRichEditTextRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.IRichEditTextRange'
    _iid_ = Guid('{374e3515-ba8a-4a6e-8c59-0dde3d0cf5cd}')
    @winrt_commethod(6)
    def get_ContentLinkInfo(self) -> win32more.Windows.UI.Text.ContentLinkInfo: ...
    @winrt_commethod(7)
    def put_ContentLinkInfo(self, value: win32more.Windows.UI.Text.ContentLinkInfo) -> Void: ...
    ContentLinkInfo = property(get_ContentLinkInfo, put_ContentLinkInfo)
class ITextCharacterFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextCharacterFormat'
    _iid_ = Guid('{5adef3db-05fb-442d-8065-642afea02ced}')
    @winrt_commethod(6)
    def get_AllCaps(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(7)
    def put_AllCaps(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(8)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_Bold(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(11)
    def put_Bold(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(12)
    def get_FontStretch(self) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_commethod(13)
    def put_FontStretch(self, value: win32more.Windows.UI.Text.FontStretch) -> Void: ...
    @winrt_commethod(14)
    def get_FontStyle(self) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_commethod(15)
    def put_FontStyle(self, value: win32more.Windows.UI.Text.FontStyle) -> Void: ...
    @winrt_commethod(16)
    def get_ForegroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(17)
    def put_ForegroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(18)
    def get_Hidden(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(19)
    def put_Hidden(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(20)
    def get_Italic(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(21)
    def put_Italic(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(22)
    def get_Kerning(self) -> Single: ...
    @winrt_commethod(23)
    def put_Kerning(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_LanguageTag(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def put_LanguageTag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(26)
    def get_LinkType(self) -> win32more.Windows.UI.Text.LinkType: ...
    @winrt_commethod(27)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(29)
    def get_Outline(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(30)
    def put_Outline(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(31)
    def get_Position(self) -> Single: ...
    @winrt_commethod(32)
    def put_Position(self, value: Single) -> Void: ...
    @winrt_commethod(33)
    def get_ProtectedText(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(34)
    def put_ProtectedText(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(35)
    def get_Size(self) -> Single: ...
    @winrt_commethod(36)
    def put_Size(self, value: Single) -> Void: ...
    @winrt_commethod(37)
    def get_SmallCaps(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(38)
    def put_SmallCaps(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(39)
    def get_Spacing(self) -> Single: ...
    @winrt_commethod(40)
    def put_Spacing(self, value: Single) -> Void: ...
    @winrt_commethod(41)
    def get_Strikethrough(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(42)
    def put_Strikethrough(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(43)
    def get_Subscript(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(44)
    def put_Subscript(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(45)
    def get_Superscript(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(46)
    def put_Superscript(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(47)
    def get_TextScript(self) -> win32more.Windows.UI.Text.TextScript: ...
    @winrt_commethod(48)
    def put_TextScript(self, value: win32more.Windows.UI.Text.TextScript) -> Void: ...
    @winrt_commethod(49)
    def get_Underline(self) -> win32more.Windows.UI.Text.UnderlineType: ...
    @winrt_commethod(50)
    def put_Underline(self, value: win32more.Windows.UI.Text.UnderlineType) -> Void: ...
    @winrt_commethod(51)
    def get_Weight(self) -> Int32: ...
    @winrt_commethod(52)
    def put_Weight(self, value: Int32) -> Void: ...
    @winrt_commethod(53)
    def SetClone(self, value: win32more.Windows.UI.Text.ITextCharacterFormat) -> Void: ...
    @winrt_commethod(54)
    def GetClone(self) -> win32more.Windows.UI.Text.ITextCharacterFormat: ...
    @winrt_commethod(55)
    def IsEqual(self, format: win32more.Windows.UI.Text.ITextCharacterFormat) -> Boolean: ...
    AllCaps = property(get_AllCaps, put_AllCaps)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    Bold = property(get_Bold, put_Bold)
    FontStretch = property(get_FontStretch, put_FontStretch)
    FontStyle = property(get_FontStyle, put_FontStyle)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    Hidden = property(get_Hidden, put_Hidden)
    Italic = property(get_Italic, put_Italic)
    Kerning = property(get_Kerning, put_Kerning)
    LanguageTag = property(get_LanguageTag, put_LanguageTag)
    LinkType = property(get_LinkType, None)
    Name = property(get_Name, put_Name)
    Outline = property(get_Outline, put_Outline)
    Position = property(get_Position, put_Position)
    ProtectedText = property(get_ProtectedText, put_ProtectedText)
    Size = property(get_Size, put_Size)
    SmallCaps = property(get_SmallCaps, put_SmallCaps)
    Spacing = property(get_Spacing, put_Spacing)
    Strikethrough = property(get_Strikethrough, put_Strikethrough)
    Subscript = property(get_Subscript, put_Subscript)
    Superscript = property(get_Superscript, put_Superscript)
    TextScript = property(get_TextScript, put_TextScript)
    Underline = property(get_Underline, put_Underline)
    Weight = property(get_Weight, put_Weight)
class ITextConstantsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextConstantsStatics'
    _iid_ = Guid('{779e7c33-189d-4bfa-97c8-10db135d976e}')
    @winrt_commethod(6)
    def get_AutoColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def get_MinUnitCount(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MaxUnitCount(self) -> Int32: ...
    @winrt_commethod(9)
    def get_UndefinedColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(10)
    def get_UndefinedFloatValue(self) -> Single: ...
    @winrt_commethod(11)
    def get_UndefinedInt32Value(self) -> Int32: ...
    @winrt_commethod(12)
    def get_UndefinedFontStretch(self) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_commethod(13)
    def get_UndefinedFontStyle(self) -> win32more.Windows.UI.Text.FontStyle: ...
    AutoColor = property(get_AutoColor, None)
    MinUnitCount = property(get_MinUnitCount, None)
    MaxUnitCount = property(get_MaxUnitCount, None)
    UndefinedColor = property(get_UndefinedColor, None)
    UndefinedFloatValue = property(get_UndefinedFloatValue, None)
    UndefinedInt32Value = property(get_UndefinedInt32Value, None)
    UndefinedFontStretch = property(get_UndefinedFontStretch, None)
    UndefinedFontStyle = property(get_UndefinedFontStyle, None)
class ITextDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextDocument'
    _iid_ = Guid('{beee4ddb-90b2-408c-a2f6-0a0ac31e33e4}')
    @winrt_commethod(6)
    def get_CaretType(self) -> win32more.Windows.UI.Text.CaretType: ...
    @winrt_commethod(7)
    def put_CaretType(self, value: win32more.Windows.UI.Text.CaretType) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultTabStop(self) -> Single: ...
    @winrt_commethod(9)
    def put_DefaultTabStop(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_Selection(self) -> win32more.Windows.UI.Text.ITextSelection: ...
    @winrt_commethod(11)
    def get_UndoLimit(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_UndoLimit(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def CanCopy(self) -> Boolean: ...
    @winrt_commethod(14)
    def CanPaste(self) -> Boolean: ...
    @winrt_commethod(15)
    def CanRedo(self) -> Boolean: ...
    @winrt_commethod(16)
    def CanUndo(self) -> Boolean: ...
    @winrt_commethod(17)
    def ApplyDisplayUpdates(self) -> Int32: ...
    @winrt_commethod(18)
    def BatchDisplayUpdates(self) -> Int32: ...
    @winrt_commethod(19)
    def BeginUndoGroup(self) -> Void: ...
    @winrt_commethod(20)
    def EndUndoGroup(self) -> Void: ...
    @winrt_commethod(21)
    def GetDefaultCharacterFormat(self) -> win32more.Windows.UI.Text.ITextCharacterFormat: ...
    @winrt_commethod(22)
    def GetDefaultParagraphFormat(self) -> win32more.Windows.UI.Text.ITextParagraphFormat: ...
    @winrt_commethod(23)
    def GetRange(self, startPosition: Int32, endPosition: Int32) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_commethod(24)
    def GetRangeFromPoint(self, point: win32more.Windows.Foundation.Point, options: win32more.Windows.UI.Text.PointOptions) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_commethod(25)
    def GetText(self, options: win32more.Windows.UI.Text.TextGetOptions, value: POINTER(WinRT_String)) -> Void: ...
    @winrt_commethod(26)
    def LoadFromStream(self, options: win32more.Windows.UI.Text.TextSetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(27)
    def Redo(self) -> Void: ...
    @winrt_commethod(28)
    def SaveToStream(self, options: win32more.Windows.UI.Text.TextGetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(29)
    def SetDefaultCharacterFormat(self, value: win32more.Windows.UI.Text.ITextCharacterFormat) -> Void: ...
    @winrt_commethod(30)
    def SetDefaultParagraphFormat(self, value: win32more.Windows.UI.Text.ITextParagraphFormat) -> Void: ...
    @winrt_commethod(31)
    def SetText(self, options: win32more.Windows.UI.Text.TextSetOptions, value: WinRT_String) -> Void: ...
    @winrt_commethod(32)
    def Undo(self) -> Void: ...
    CaretType = property(get_CaretType, put_CaretType)
    DefaultTabStop = property(get_DefaultTabStop, put_DefaultTabStop)
    Selection = property(get_Selection, None)
    UndoLimit = property(get_UndoLimit, put_UndoLimit)
class ITextDocument2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextDocument2'
    _iid_ = Guid('{f2311112-8c89-49c9-9118-f057cbb814ee}')
    @winrt_commethod(6)
    def get_AlignmentIncludesTrailingWhitespace(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AlignmentIncludesTrailingWhitespace(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IgnoreTrailingCharacterSpacing(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IgnoreTrailingCharacterSpacing(self, value: Boolean) -> Void: ...
    AlignmentIncludesTrailingWhitespace = property(get_AlignmentIncludesTrailingWhitespace, put_AlignmentIncludesTrailingWhitespace)
    IgnoreTrailingCharacterSpacing = property(get_IgnoreTrailingCharacterSpacing, put_IgnoreTrailingCharacterSpacing)
class ITextDocument3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextDocument3'
    _iid_ = Guid('{75ab03a1-a6f8-441d-aa18-0a851d6e5e3c}')
    @winrt_commethod(6)
    def ClearUndoRedoHistory(self) -> Void: ...
class ITextDocument4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextDocument4'
    _iid_ = Guid('{619c20f2-cb3b-4521-981f-2865b1b93f04}')
    @winrt_commethod(6)
    def SetMath(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def GetMath(self, value: POINTER(WinRT_String)) -> Void: ...
    @winrt_commethod(8)
    def SetMathMode(self, mode: win32more.Windows.UI.Text.RichEditMathMode) -> Void: ...
class ITextParagraphFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextParagraphFormat'
    _iid_ = Guid('{2cf8cfa6-4676-498a-93f5-bbdbfc0bd883}')
    @winrt_commethod(6)
    def get_Alignment(self) -> win32more.Windows.UI.Text.ParagraphAlignment: ...
    @winrt_commethod(7)
    def put_Alignment(self, value: win32more.Windows.UI.Text.ParagraphAlignment) -> Void: ...
    @winrt_commethod(8)
    def get_FirstLineIndent(self) -> Single: ...
    @winrt_commethod(9)
    def get_KeepTogether(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(10)
    def put_KeepTogether(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(11)
    def get_KeepWithNext(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(12)
    def put_KeepWithNext(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(13)
    def get_LeftIndent(self) -> Single: ...
    @winrt_commethod(14)
    def get_LineSpacing(self) -> Single: ...
    @winrt_commethod(15)
    def get_LineSpacingRule(self) -> win32more.Windows.UI.Text.LineSpacingRule: ...
    @winrt_commethod(16)
    def get_ListAlignment(self) -> win32more.Windows.UI.Text.MarkerAlignment: ...
    @winrt_commethod(17)
    def put_ListAlignment(self, value: win32more.Windows.UI.Text.MarkerAlignment) -> Void: ...
    @winrt_commethod(18)
    def get_ListLevelIndex(self) -> Int32: ...
    @winrt_commethod(19)
    def put_ListLevelIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_ListStart(self) -> Int32: ...
    @winrt_commethod(21)
    def put_ListStart(self, value: Int32) -> Void: ...
    @winrt_commethod(22)
    def get_ListStyle(self) -> win32more.Windows.UI.Text.MarkerStyle: ...
    @winrt_commethod(23)
    def put_ListStyle(self, value: win32more.Windows.UI.Text.MarkerStyle) -> Void: ...
    @winrt_commethod(24)
    def get_ListTab(self) -> Single: ...
    @winrt_commethod(25)
    def put_ListTab(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def get_ListType(self) -> win32more.Windows.UI.Text.MarkerType: ...
    @winrt_commethod(27)
    def put_ListType(self, value: win32more.Windows.UI.Text.MarkerType) -> Void: ...
    @winrt_commethod(28)
    def get_NoLineNumber(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(29)
    def put_NoLineNumber(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(30)
    def get_PageBreakBefore(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(31)
    def put_PageBreakBefore(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(32)
    def get_RightIndent(self) -> Single: ...
    @winrt_commethod(33)
    def put_RightIndent(self, value: Single) -> Void: ...
    @winrt_commethod(34)
    def get_RightToLeft(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(35)
    def put_RightToLeft(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(36)
    def get_Style(self) -> win32more.Windows.UI.Text.ParagraphStyle: ...
    @winrt_commethod(37)
    def put_Style(self, value: win32more.Windows.UI.Text.ParagraphStyle) -> Void: ...
    @winrt_commethod(38)
    def get_SpaceAfter(self) -> Single: ...
    @winrt_commethod(39)
    def put_SpaceAfter(self, value: Single) -> Void: ...
    @winrt_commethod(40)
    def get_SpaceBefore(self) -> Single: ...
    @winrt_commethod(41)
    def put_SpaceBefore(self, value: Single) -> Void: ...
    @winrt_commethod(42)
    def get_WidowControl(self) -> win32more.Windows.UI.Text.FormatEffect: ...
    @winrt_commethod(43)
    def put_WidowControl(self, value: win32more.Windows.UI.Text.FormatEffect) -> Void: ...
    @winrt_commethod(44)
    def get_TabCount(self) -> Int32: ...
    @winrt_commethod(45)
    def AddTab(self, position: Single, align: win32more.Windows.UI.Text.TabAlignment, leader: win32more.Windows.UI.Text.TabLeader) -> Void: ...
    @winrt_commethod(46)
    def ClearAllTabs(self) -> Void: ...
    @winrt_commethod(47)
    def DeleteTab(self, position: Single) -> Void: ...
    @winrt_commethod(48)
    def GetClone(self) -> win32more.Windows.UI.Text.ITextParagraphFormat: ...
    @winrt_commethod(49)
    def GetTab(self, index: Int32, position: POINTER(Single), align: POINTER(win32more.Windows.UI.Text.TabAlignment), leader: POINTER(win32more.Windows.UI.Text.TabLeader)) -> Void: ...
    @winrt_commethod(50)
    def IsEqual(self, format: win32more.Windows.UI.Text.ITextParagraphFormat) -> Boolean: ...
    @winrt_commethod(51)
    def SetClone(self, format: win32more.Windows.UI.Text.ITextParagraphFormat) -> Void: ...
    @winrt_commethod(52)
    def SetIndents(self, start: Single, left: Single, right: Single) -> Void: ...
    @winrt_commethod(53)
    def SetLineSpacing(self, rule: win32more.Windows.UI.Text.LineSpacingRule, spacing: Single) -> Void: ...
    Alignment = property(get_Alignment, put_Alignment)
    FirstLineIndent = property(get_FirstLineIndent, None)
    KeepTogether = property(get_KeepTogether, put_KeepTogether)
    KeepWithNext = property(get_KeepWithNext, put_KeepWithNext)
    LeftIndent = property(get_LeftIndent, None)
    LineSpacing = property(get_LineSpacing, None)
    LineSpacingRule = property(get_LineSpacingRule, None)
    ListAlignment = property(get_ListAlignment, put_ListAlignment)
    ListLevelIndex = property(get_ListLevelIndex, put_ListLevelIndex)
    ListStart = property(get_ListStart, put_ListStart)
    ListStyle = property(get_ListStyle, put_ListStyle)
    ListTab = property(get_ListTab, put_ListTab)
    ListType = property(get_ListType, put_ListType)
    NoLineNumber = property(get_NoLineNumber, put_NoLineNumber)
    PageBreakBefore = property(get_PageBreakBefore, put_PageBreakBefore)
    RightIndent = property(get_RightIndent, put_RightIndent)
    RightToLeft = property(get_RightToLeft, put_RightToLeft)
    Style = property(get_Style, put_Style)
    SpaceAfter = property(get_SpaceAfter, put_SpaceAfter)
    SpaceBefore = property(get_SpaceBefore, put_SpaceBefore)
    WidowControl = property(get_WidowControl, put_WidowControl)
    TabCount = property(get_TabCount, None)
class ITextRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextRange'
    _iid_ = Guid('{5b9e4e57-c072-42a0-8945-af503ee54768}')
    @winrt_commethod(6)
    def get_Character(self) -> Char: ...
    @winrt_commethod(7)
    def put_Character(self, value: Char) -> Void: ...
    @winrt_commethod(8)
    def get_CharacterFormat(self) -> win32more.Windows.UI.Text.ITextCharacterFormat: ...
    @winrt_commethod(9)
    def put_CharacterFormat(self, value: win32more.Windows.UI.Text.ITextCharacterFormat) -> Void: ...
    @winrt_commethod(10)
    def get_FormattedText(self) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_commethod(11)
    def put_FormattedText(self, value: win32more.Windows.UI.Text.ITextRange) -> Void: ...
    @winrt_commethod(12)
    def get_EndPosition(self) -> Int32: ...
    @winrt_commethod(13)
    def put_EndPosition(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_Gravity(self) -> win32more.Windows.UI.Text.RangeGravity: ...
    @winrt_commethod(15)
    def put_Gravity(self, value: win32more.Windows.UI.Text.RangeGravity) -> Void: ...
    @winrt_commethod(16)
    def get_Length(self) -> Int32: ...
    @winrt_commethod(17)
    def get_Link(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_Link(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(19)
    def get_ParagraphFormat(self) -> win32more.Windows.UI.Text.ITextParagraphFormat: ...
    @winrt_commethod(20)
    def put_ParagraphFormat(self, value: win32more.Windows.UI.Text.ITextParagraphFormat) -> Void: ...
    @winrt_commethod(21)
    def get_StartPosition(self) -> Int32: ...
    @winrt_commethod(22)
    def put_StartPosition(self, value: Int32) -> Void: ...
    @winrt_commethod(23)
    def get_StoryLength(self) -> Int32: ...
    @winrt_commethod(24)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(26)
    def CanPaste(self, format: Int32) -> Boolean: ...
    @winrt_commethod(27)
    def ChangeCase(self, value: win32more.Windows.UI.Text.LetterCase) -> Void: ...
    @winrt_commethod(28)
    def Collapse(self, value: Boolean) -> Void: ...
    @winrt_commethod(29)
    def Copy(self) -> Void: ...
    @winrt_commethod(30)
    def Cut(self) -> Void: ...
    @winrt_commethod(31)
    def Delete(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_commethod(32)
    def EndOf(self, unit: win32more.Windows.UI.Text.TextRangeUnit, extend: Boolean) -> Int32: ...
    @winrt_commethod(33)
    def Expand(self, unit: win32more.Windows.UI.Text.TextRangeUnit) -> Int32: ...
    @winrt_commethod(34)
    def FindText(self, value: WinRT_String, scanLength: Int32, options: win32more.Windows.UI.Text.FindOptions) -> Int32: ...
    @winrt_commethod(35)
    def GetCharacterUtf32(self, value: POINTER(UInt32), offset: Int32) -> Void: ...
    @winrt_commethod(36)
    def GetClone(self) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_commethod(37)
    def GetIndex(self, unit: win32more.Windows.UI.Text.TextRangeUnit) -> Int32: ...
    @winrt_commethod(38)
    def GetPoint(self, horizontalAlign: win32more.Windows.UI.Text.HorizontalCharacterAlignment, verticalAlign: win32more.Windows.UI.Text.VerticalCharacterAlignment, options: win32more.Windows.UI.Text.PointOptions, point: POINTER(win32more.Windows.Foundation.Point)) -> Void: ...
    @winrt_commethod(39)
    def GetRect(self, options: win32more.Windows.UI.Text.PointOptions, rect: POINTER(win32more.Windows.Foundation.Rect), hit: POINTER(Int32)) -> Void: ...
    @winrt_commethod(40)
    def GetText(self, options: win32more.Windows.UI.Text.TextGetOptions, value: POINTER(WinRT_String)) -> Void: ...
    @winrt_commethod(41)
    def GetTextViaStream(self, options: win32more.Windows.UI.Text.TextGetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(42)
    def InRange(self, range: win32more.Windows.UI.Text.ITextRange) -> Boolean: ...
    @winrt_commethod(43)
    def InsertImage(self, width: Int32, height: Int32, ascent: Int32, verticalAlign: win32more.Windows.UI.Text.VerticalCharacterAlignment, alternateText: WinRT_String, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(44)
    def InStory(self, range: win32more.Windows.UI.Text.ITextRange) -> Boolean: ...
    @winrt_commethod(45)
    def IsEqual(self, range: win32more.Windows.UI.Text.ITextRange) -> Boolean: ...
    @winrt_commethod(46)
    def Move(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_commethod(47)
    def MoveEnd(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_commethod(48)
    def MoveStart(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_commethod(49)
    def Paste(self, format: Int32) -> Void: ...
    @winrt_commethod(50)
    def ScrollIntoView(self, value: win32more.Windows.UI.Text.PointOptions) -> Void: ...
    @winrt_commethod(51)
    def MatchSelection(self) -> Void: ...
    @winrt_commethod(52)
    def SetIndex(self, unit: win32more.Windows.UI.Text.TextRangeUnit, index: Int32, extend: Boolean) -> Void: ...
    @winrt_commethod(53)
    def SetPoint(self, point: win32more.Windows.Foundation.Point, options: win32more.Windows.UI.Text.PointOptions, extend: Boolean) -> Void: ...
    @winrt_commethod(54)
    def SetRange(self, startPosition: Int32, endPosition: Int32) -> Void: ...
    @winrt_commethod(55)
    def SetText(self, options: win32more.Windows.UI.Text.TextSetOptions, value: WinRT_String) -> Void: ...
    @winrt_commethod(56)
    def SetTextViaStream(self, options: win32more.Windows.UI.Text.TextSetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(57)
    def StartOf(self, unit: win32more.Windows.UI.Text.TextRangeUnit, extend: Boolean) -> Int32: ...
    Character = property(get_Character, put_Character)
    CharacterFormat = property(get_CharacterFormat, put_CharacterFormat)
    FormattedText = property(get_FormattedText, put_FormattedText)
    EndPosition = property(get_EndPosition, put_EndPosition)
    Gravity = property(get_Gravity, put_Gravity)
    Length = property(get_Length, None)
    Link = property(get_Link, put_Link)
    ParagraphFormat = property(get_ParagraphFormat, put_ParagraphFormat)
    StartPosition = property(get_StartPosition, put_StartPosition)
    StoryLength = property(get_StoryLength, None)
    Text = property(get_Text, put_Text)
class ITextSelection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.ITextSelection'
    _iid_ = Guid('{a6d36724-f28f-430a-b2cf-c343671ec0e9}')
    @winrt_commethod(6)
    def get_Options(self) -> win32more.Windows.UI.Text.SelectionOptions: ...
    @winrt_commethod(7)
    def put_Options(self, value: win32more.Windows.UI.Text.SelectionOptions) -> Void: ...
    @winrt_commethod(8)
    def get_Type(self) -> win32more.Windows.UI.Text.SelectionType: ...
    @winrt_commethod(9)
    def EndKey(self, unit: win32more.Windows.UI.Text.TextRangeUnit, extend: Boolean) -> Int32: ...
    @winrt_commethod(10)
    def HomeKey(self, unit: win32more.Windows.UI.Text.TextRangeUnit, extend: Boolean) -> Int32: ...
    @winrt_commethod(11)
    def MoveDown(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32, extend: Boolean) -> Int32: ...
    @winrt_commethod(12)
    def MoveLeft(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32, extend: Boolean) -> Int32: ...
    @winrt_commethod(13)
    def MoveRight(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32, extend: Boolean) -> Int32: ...
    @winrt_commethod(14)
    def MoveUp(self, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32, extend: Boolean) -> Int32: ...
    @winrt_commethod(15)
    def TypeText(self, value: WinRT_String) -> Void: ...
    Options = property(get_Options, put_Options)
    Type = property(get_Type, None)
LetterCase = Int32
LetterCase_Lower: LetterCase = 0
LetterCase_Upper: LetterCase = 1
LineSpacingRule = Int32
LineSpacingRule_Undefined: LineSpacingRule = 0
LineSpacingRule_Single: LineSpacingRule = 1
LineSpacingRule_OneAndHalf: LineSpacingRule = 2
LineSpacingRule_Double: LineSpacingRule = 3
LineSpacingRule_AtLeast: LineSpacingRule = 4
LineSpacingRule_Exactly: LineSpacingRule = 5
LineSpacingRule_Multiple: LineSpacingRule = 6
LineSpacingRule_Percent: LineSpacingRule = 7
LinkType = Int32
LinkType_Undefined: LinkType = 0
LinkType_NotALink: LinkType = 1
LinkType_ClientLink: LinkType = 2
LinkType_FriendlyLinkName: LinkType = 3
LinkType_FriendlyLinkAddress: LinkType = 4
LinkType_AutoLink: LinkType = 5
LinkType_AutoLinkEmail: LinkType = 6
LinkType_AutoLinkPhone: LinkType = 7
LinkType_AutoLinkPath: LinkType = 8
MarkerAlignment = Int32
MarkerAlignment_Undefined: MarkerAlignment = 0
MarkerAlignment_Left: MarkerAlignment = 1
MarkerAlignment_Center: MarkerAlignment = 2
MarkerAlignment_Right: MarkerAlignment = 3
MarkerStyle = Int32
MarkerStyle_Undefined: MarkerStyle = 0
MarkerStyle_Parenthesis: MarkerStyle = 1
MarkerStyle_Parentheses: MarkerStyle = 2
MarkerStyle_Period: MarkerStyle = 3
MarkerStyle_Plain: MarkerStyle = 4
MarkerStyle_Minus: MarkerStyle = 5
MarkerStyle_NoNumber: MarkerStyle = 6
MarkerType = Int32
MarkerType_Undefined: MarkerType = 0
MarkerType_None: MarkerType = 1
MarkerType_Bullet: MarkerType = 2
MarkerType_Arabic: MarkerType = 3
MarkerType_LowercaseEnglishLetter: MarkerType = 4
MarkerType_UppercaseEnglishLetter: MarkerType = 5
MarkerType_LowercaseRoman: MarkerType = 6
MarkerType_UppercaseRoman: MarkerType = 7
MarkerType_UnicodeSequence: MarkerType = 8
MarkerType_CircledNumber: MarkerType = 9
MarkerType_BlackCircleWingding: MarkerType = 10
MarkerType_WhiteCircleWingding: MarkerType = 11
MarkerType_ArabicWide: MarkerType = 12
MarkerType_SimplifiedChinese: MarkerType = 13
MarkerType_TraditionalChinese: MarkerType = 14
MarkerType_JapanSimplifiedChinese: MarkerType = 15
MarkerType_JapanKorea: MarkerType = 16
MarkerType_ArabicDictionary: MarkerType = 17
MarkerType_ArabicAbjad: MarkerType = 18
MarkerType_Hebrew: MarkerType = 19
MarkerType_ThaiAlphabetic: MarkerType = 20
MarkerType_ThaiNumeric: MarkerType = 21
MarkerType_DevanagariVowel: MarkerType = 22
MarkerType_DevanagariConsonant: MarkerType = 23
MarkerType_DevanagariNumeric: MarkerType = 24
ParagraphAlignment = Int32
ParagraphAlignment_Undefined: ParagraphAlignment = 0
ParagraphAlignment_Left: ParagraphAlignment = 1
ParagraphAlignment_Center: ParagraphAlignment = 2
ParagraphAlignment_Right: ParagraphAlignment = 3
ParagraphAlignment_Justify: ParagraphAlignment = 4
ParagraphStyle = Int32
ParagraphStyle_Undefined: ParagraphStyle = 0
ParagraphStyle_None: ParagraphStyle = 1
ParagraphStyle_Normal: ParagraphStyle = 2
ParagraphStyle_Heading1: ParagraphStyle = 3
ParagraphStyle_Heading2: ParagraphStyle = 4
ParagraphStyle_Heading3: ParagraphStyle = 5
ParagraphStyle_Heading4: ParagraphStyle = 6
ParagraphStyle_Heading5: ParagraphStyle = 7
ParagraphStyle_Heading6: ParagraphStyle = 8
ParagraphStyle_Heading7: ParagraphStyle = 9
ParagraphStyle_Heading8: ParagraphStyle = 10
ParagraphStyle_Heading9: ParagraphStyle = 11
PointOptions = UInt32
PointOptions_None: PointOptions = 0
PointOptions_IncludeInset: PointOptions = 1
PointOptions_Start: PointOptions = 32
PointOptions_ClientCoordinates: PointOptions = 256
PointOptions_AllowOffClient: PointOptions = 512
PointOptions_Transform: PointOptions = 1024
PointOptions_NoHorizontalScroll: PointOptions = 65536
PointOptions_NoVerticalScroll: PointOptions = 262144
RangeGravity = Int32
RangeGravity_UIBehavior: RangeGravity = 0
RangeGravity_Backward: RangeGravity = 1
RangeGravity_Forward: RangeGravity = 2
RangeGravity_Inward: RangeGravity = 3
RangeGravity_Outward: RangeGravity = 4
RichEditMathMode = Int32
RichEditMathMode_NoMath: RichEditMathMode = 0
RichEditMathMode_MathOnly: RichEditMathMode = 1
class RichEditTextDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.ITextDocument
    _classid_ = 'Windows.UI.Text.RichEditTextDocument'
    @winrt_mixinmethod
    def get_AlignmentIncludesTrailingWhitespace(self: win32more.Windows.UI.Text.ITextDocument2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlignmentIncludesTrailingWhitespace(self: win32more.Windows.UI.Text.ITextDocument2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoreTrailingCharacterSpacing(self: win32more.Windows.UI.Text.ITextDocument2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreTrailingCharacterSpacing(self: win32more.Windows.UI.Text.ITextDocument2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def ClearUndoRedoHistory(self: win32more.Windows.UI.Text.ITextDocument3) -> Void: ...
    @winrt_mixinmethod
    def SetMath(self: win32more.Windows.UI.Text.ITextDocument4, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetMath(self: win32more.Windows.UI.Text.ITextDocument4, value: POINTER(WinRT_String)) -> Void: ...
    @winrt_mixinmethod
    def SetMathMode(self: win32more.Windows.UI.Text.ITextDocument4, mode: win32more.Windows.UI.Text.RichEditMathMode) -> Void: ...
    @winrt_mixinmethod
    def get_CaretType(self: win32more.Windows.UI.Text.ITextDocument) -> win32more.Windows.UI.Text.CaretType: ...
    @winrt_mixinmethod
    def put_CaretType(self: win32more.Windows.UI.Text.ITextDocument, value: win32more.Windows.UI.Text.CaretType) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultTabStop(self: win32more.Windows.UI.Text.ITextDocument) -> Single: ...
    @winrt_mixinmethod
    def put_DefaultTabStop(self: win32more.Windows.UI.Text.ITextDocument, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Selection(self: win32more.Windows.UI.Text.ITextDocument) -> win32more.Windows.UI.Text.ITextSelection: ...
    @winrt_mixinmethod
    def get_UndoLimit(self: win32more.Windows.UI.Text.ITextDocument) -> UInt32: ...
    @winrt_mixinmethod
    def put_UndoLimit(self: win32more.Windows.UI.Text.ITextDocument, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def CanCopy(self: win32more.Windows.UI.Text.ITextDocument) -> Boolean: ...
    @winrt_mixinmethod
    def CanPaste(self: win32more.Windows.UI.Text.ITextDocument) -> Boolean: ...
    @winrt_mixinmethod
    def CanRedo(self: win32more.Windows.UI.Text.ITextDocument) -> Boolean: ...
    @winrt_mixinmethod
    def CanUndo(self: win32more.Windows.UI.Text.ITextDocument) -> Boolean: ...
    @winrt_mixinmethod
    def ApplyDisplayUpdates(self: win32more.Windows.UI.Text.ITextDocument) -> Int32: ...
    @winrt_mixinmethod
    def BatchDisplayUpdates(self: win32more.Windows.UI.Text.ITextDocument) -> Int32: ...
    @winrt_mixinmethod
    def BeginUndoGroup(self: win32more.Windows.UI.Text.ITextDocument) -> Void: ...
    @winrt_mixinmethod
    def EndUndoGroup(self: win32more.Windows.UI.Text.ITextDocument) -> Void: ...
    @winrt_mixinmethod
    def GetDefaultCharacterFormat(self: win32more.Windows.UI.Text.ITextDocument) -> win32more.Windows.UI.Text.ITextCharacterFormat: ...
    @winrt_mixinmethod
    def GetDefaultParagraphFormat(self: win32more.Windows.UI.Text.ITextDocument) -> win32more.Windows.UI.Text.ITextParagraphFormat: ...
    @winrt_mixinmethod
    def GetRange(self: win32more.Windows.UI.Text.ITextDocument, startPosition: Int32, endPosition: Int32) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_mixinmethod
    def GetRangeFromPoint(self: win32more.Windows.UI.Text.ITextDocument, point: win32more.Windows.Foundation.Point, options: win32more.Windows.UI.Text.PointOptions) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_mixinmethod
    def GetText(self: win32more.Windows.UI.Text.ITextDocument, options: win32more.Windows.UI.Text.TextGetOptions, value: POINTER(WinRT_String)) -> Void: ...
    @winrt_mixinmethod
    def LoadFromStream(self: win32more.Windows.UI.Text.ITextDocument, options: win32more.Windows.UI.Text.TextSetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def Redo(self: win32more.Windows.UI.Text.ITextDocument) -> Void: ...
    @winrt_mixinmethod
    def SaveToStream(self: win32more.Windows.UI.Text.ITextDocument, options: win32more.Windows.UI.Text.TextGetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def SetDefaultCharacterFormat(self: win32more.Windows.UI.Text.ITextDocument, value: win32more.Windows.UI.Text.ITextCharacterFormat) -> Void: ...
    @winrt_mixinmethod
    def SetDefaultParagraphFormat(self: win32more.Windows.UI.Text.ITextDocument, value: win32more.Windows.UI.Text.ITextParagraphFormat) -> Void: ...
    @winrt_mixinmethod
    def SetText(self: win32more.Windows.UI.Text.ITextDocument, options: win32more.Windows.UI.Text.TextSetOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Undo(self: win32more.Windows.UI.Text.ITextDocument) -> Void: ...
    AlignmentIncludesTrailingWhitespace = property(get_AlignmentIncludesTrailingWhitespace, put_AlignmentIncludesTrailingWhitespace)
    IgnoreTrailingCharacterSpacing = property(get_IgnoreTrailingCharacterSpacing, put_IgnoreTrailingCharacterSpacing)
    CaretType = property(get_CaretType, put_CaretType)
    DefaultTabStop = property(get_DefaultTabStop, put_DefaultTabStop)
    Selection = property(get_Selection, None)
    UndoLimit = property(get_UndoLimit, put_UndoLimit)
class RichEditTextRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.ITextRange
    _classid_ = 'Windows.UI.Text.RichEditTextRange'
    @winrt_mixinmethod
    def get_ContentLinkInfo(self: win32more.Windows.UI.Text.IRichEditTextRange) -> win32more.Windows.UI.Text.ContentLinkInfo: ...
    @winrt_mixinmethod
    def put_ContentLinkInfo(self: win32more.Windows.UI.Text.IRichEditTextRange, value: win32more.Windows.UI.Text.ContentLinkInfo) -> Void: ...
    @winrt_mixinmethod
    def get_Character(self: win32more.Windows.UI.Text.ITextRange) -> Char: ...
    @winrt_mixinmethod
    def put_Character(self: win32more.Windows.UI.Text.ITextRange, value: Char) -> Void: ...
    @winrt_mixinmethod
    def get_CharacterFormat(self: win32more.Windows.UI.Text.ITextRange) -> win32more.Windows.UI.Text.ITextCharacterFormat: ...
    @winrt_mixinmethod
    def put_CharacterFormat(self: win32more.Windows.UI.Text.ITextRange, value: win32more.Windows.UI.Text.ITextCharacterFormat) -> Void: ...
    @winrt_mixinmethod
    def get_FormattedText(self: win32more.Windows.UI.Text.ITextRange) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_mixinmethod
    def put_FormattedText(self: win32more.Windows.UI.Text.ITextRange, value: win32more.Windows.UI.Text.ITextRange) -> Void: ...
    @winrt_mixinmethod
    def get_EndPosition(self: win32more.Windows.UI.Text.ITextRange) -> Int32: ...
    @winrt_mixinmethod
    def put_EndPosition(self: win32more.Windows.UI.Text.ITextRange, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Gravity(self: win32more.Windows.UI.Text.ITextRange) -> win32more.Windows.UI.Text.RangeGravity: ...
    @winrt_mixinmethod
    def put_Gravity(self: win32more.Windows.UI.Text.ITextRange, value: win32more.Windows.UI.Text.RangeGravity) -> Void: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.UI.Text.ITextRange) -> Int32: ...
    @winrt_mixinmethod
    def get_Link(self: win32more.Windows.UI.Text.ITextRange) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Link(self: win32more.Windows.UI.Text.ITextRange, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ParagraphFormat(self: win32more.Windows.UI.Text.ITextRange) -> win32more.Windows.UI.Text.ITextParagraphFormat: ...
    @winrt_mixinmethod
    def put_ParagraphFormat(self: win32more.Windows.UI.Text.ITextRange, value: win32more.Windows.UI.Text.ITextParagraphFormat) -> Void: ...
    @winrt_mixinmethod
    def get_StartPosition(self: win32more.Windows.UI.Text.ITextRange) -> Int32: ...
    @winrt_mixinmethod
    def put_StartPosition(self: win32more.Windows.UI.Text.ITextRange, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_StoryLength(self: win32more.Windows.UI.Text.ITextRange) -> Int32: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.Text.ITextRange) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.UI.Text.ITextRange, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def CanPaste(self: win32more.Windows.UI.Text.ITextRange, format: Int32) -> Boolean: ...
    @winrt_mixinmethod
    def ChangeCase(self: win32more.Windows.UI.Text.ITextRange, value: win32more.Windows.UI.Text.LetterCase) -> Void: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Windows.UI.Text.ITextRange, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Copy(self: win32more.Windows.UI.Text.ITextRange) -> Void: ...
    @winrt_mixinmethod
    def Cut(self: win32more.Windows.UI.Text.ITextRange) -> Void: ...
    @winrt_mixinmethod
    def Delete(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_mixinmethod
    def EndOf(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit, extend: Boolean) -> Int32: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit) -> Int32: ...
    @winrt_mixinmethod
    def FindText(self: win32more.Windows.UI.Text.ITextRange, value: WinRT_String, scanLength: Int32, options: win32more.Windows.UI.Text.FindOptions) -> Int32: ...
    @winrt_mixinmethod
    def GetCharacterUtf32(self: win32more.Windows.UI.Text.ITextRange, value: POINTER(UInt32), offset: Int32) -> Void: ...
    @winrt_mixinmethod
    def GetClone(self: win32more.Windows.UI.Text.ITextRange) -> win32more.Windows.UI.Text.ITextRange: ...
    @winrt_mixinmethod
    def GetIndex(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit) -> Int32: ...
    @winrt_mixinmethod
    def GetPoint(self: win32more.Windows.UI.Text.ITextRange, horizontalAlign: win32more.Windows.UI.Text.HorizontalCharacterAlignment, verticalAlign: win32more.Windows.UI.Text.VerticalCharacterAlignment, options: win32more.Windows.UI.Text.PointOptions, point: POINTER(win32more.Windows.Foundation.Point)) -> Void: ...
    @winrt_mixinmethod
    def GetRect(self: win32more.Windows.UI.Text.ITextRange, options: win32more.Windows.UI.Text.PointOptions, rect: POINTER(win32more.Windows.Foundation.Rect), hit: POINTER(Int32)) -> Void: ...
    @winrt_mixinmethod
    def GetText(self: win32more.Windows.UI.Text.ITextRange, options: win32more.Windows.UI.Text.TextGetOptions, value: POINTER(WinRT_String)) -> Void: ...
    @winrt_mixinmethod
    def GetTextViaStream(self: win32more.Windows.UI.Text.ITextRange, options: win32more.Windows.UI.Text.TextGetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def InRange(self: win32more.Windows.UI.Text.ITextRange, range: win32more.Windows.UI.Text.ITextRange) -> Boolean: ...
    @winrt_mixinmethod
    def InsertImage(self: win32more.Windows.UI.Text.ITextRange, width: Int32, height: Int32, ascent: Int32, verticalAlign: win32more.Windows.UI.Text.VerticalCharacterAlignment, alternateText: WinRT_String, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def InStory(self: win32more.Windows.UI.Text.ITextRange, range: win32more.Windows.UI.Text.ITextRange) -> Boolean: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.UI.Text.ITextRange, range: win32more.Windows.UI.Text.ITextRange) -> Boolean: ...
    @winrt_mixinmethod
    def Move(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_mixinmethod
    def MoveEnd(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_mixinmethod
    def MoveStart(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit, count: Int32) -> Int32: ...
    @winrt_mixinmethod
    def Paste(self: win32more.Windows.UI.Text.ITextRange, format: Int32) -> Void: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Windows.UI.Text.ITextRange, value: win32more.Windows.UI.Text.PointOptions) -> Void: ...
    @winrt_mixinmethod
    def MatchSelection(self: win32more.Windows.UI.Text.ITextRange) -> Void: ...
    @winrt_mixinmethod
    def SetIndex(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit, index: Int32, extend: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetPoint(self: win32more.Windows.UI.Text.ITextRange, point: win32more.Windows.Foundation.Point, options: win32more.Windows.UI.Text.PointOptions, extend: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetRange(self: win32more.Windows.UI.Text.ITextRange, startPosition: Int32, endPosition: Int32) -> Void: ...
    @winrt_mixinmethod
    def SetText(self: win32more.Windows.UI.Text.ITextRange, options: win32more.Windows.UI.Text.TextSetOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetTextViaStream(self: win32more.Windows.UI.Text.ITextRange, options: win32more.Windows.UI.Text.TextSetOptions, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def StartOf(self: win32more.Windows.UI.Text.ITextRange, unit: win32more.Windows.UI.Text.TextRangeUnit, extend: Boolean) -> Int32: ...
    ContentLinkInfo = property(get_ContentLinkInfo, put_ContentLinkInfo)
    Character = property(get_Character, put_Character)
    CharacterFormat = property(get_CharacterFormat, put_CharacterFormat)
    FormattedText = property(get_FormattedText, put_FormattedText)
    EndPosition = property(get_EndPosition, put_EndPosition)
    Gravity = property(get_Gravity, put_Gravity)
    Length = property(get_Length, None)
    Link = property(get_Link, put_Link)
    ParagraphFormat = property(get_ParagraphFormat, put_ParagraphFormat)
    StartPosition = property(get_StartPosition, put_StartPosition)
    StoryLength = property(get_StoryLength, None)
    Text = property(get_Text, put_Text)
SelectionOptions = UInt32
SelectionOptions_StartActive: SelectionOptions = 1
SelectionOptions_AtEndOfLine: SelectionOptions = 2
SelectionOptions_Overtype: SelectionOptions = 4
SelectionOptions_Active: SelectionOptions = 8
SelectionOptions_Replace: SelectionOptions = 16
SelectionType = Int32
SelectionType_None: SelectionType = 0
SelectionType_InsertionPoint: SelectionType = 1
SelectionType_Normal: SelectionType = 2
SelectionType_InlineShape: SelectionType = 7
SelectionType_Shape: SelectionType = 8
TabAlignment = Int32
TabAlignment_Left: TabAlignment = 0
TabAlignment_Center: TabAlignment = 1
TabAlignment_Right: TabAlignment = 2
TabAlignment_Decimal: TabAlignment = 3
TabAlignment_Bar: TabAlignment = 4
TabLeader = Int32
TabLeader_Spaces: TabLeader = 0
TabLeader_Dots: TabLeader = 1
TabLeader_Dashes: TabLeader = 2
TabLeader_Lines: TabLeader = 3
TabLeader_ThickLines: TabLeader = 4
TabLeader_Equals: TabLeader = 5
class _TextConstants_Meta_(ComPtr.__class__):
    pass
class TextConstants(ComPtr, metaclass=_TextConstants_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.TextConstants'
    @winrt_classmethod
    def get_AutoColor(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> win32more.Windows.UI.Color: ...
    @winrt_classmethod
    def get_MinUnitCount(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> Int32: ...
    @winrt_classmethod
    def get_MaxUnitCount(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> Int32: ...
    @winrt_classmethod
    def get_UndefinedColor(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> win32more.Windows.UI.Color: ...
    @winrt_classmethod
    def get_UndefinedFloatValue(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> Single: ...
    @winrt_classmethod
    def get_UndefinedInt32Value(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> Int32: ...
    @winrt_classmethod
    def get_UndefinedFontStretch(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_classmethod
    def get_UndefinedFontStyle(cls: win32more.Windows.UI.Text.ITextConstantsStatics) -> win32more.Windows.UI.Text.FontStyle: ...
    _TextConstants_Meta_.AutoColor = property(get_AutoColor.__wrapped__, None)
    _TextConstants_Meta_.MinUnitCount = property(get_MinUnitCount.__wrapped__, None)
    _TextConstants_Meta_.MaxUnitCount = property(get_MaxUnitCount.__wrapped__, None)
    _TextConstants_Meta_.UndefinedColor = property(get_UndefinedColor.__wrapped__, None)
    _TextConstants_Meta_.UndefinedFloatValue = property(get_UndefinedFloatValue.__wrapped__, None)
    _TextConstants_Meta_.UndefinedInt32Value = property(get_UndefinedInt32Value.__wrapped__, None)
    _TextConstants_Meta_.UndefinedFontStretch = property(get_UndefinedFontStretch.__wrapped__, None)
    _TextConstants_Meta_.UndefinedFontStyle = property(get_UndefinedFontStyle.__wrapped__, None)
TextDecorations = UInt32
TextDecorations_None: TextDecorations = 0
TextDecorations_Underline: TextDecorations = 1
TextDecorations_Strikethrough: TextDecorations = 2
TextGetOptions = UInt32
TextGetOptions_None: TextGetOptions = 0
TextGetOptions_AdjustCrlf: TextGetOptions = 1
TextGetOptions_UseCrlf: TextGetOptions = 2
TextGetOptions_UseObjectText: TextGetOptions = 4
TextGetOptions_AllowFinalEop: TextGetOptions = 8
TextGetOptions_NoHidden: TextGetOptions = 32
TextGetOptions_IncludeNumbering: TextGetOptions = 64
TextGetOptions_FormatRtf: TextGetOptions = 8192
TextGetOptions_UseLf: TextGetOptions = 16777216
TextRangeUnit = Int32
TextRangeUnit_Character: TextRangeUnit = 0
TextRangeUnit_Word: TextRangeUnit = 1
TextRangeUnit_Sentence: TextRangeUnit = 2
TextRangeUnit_Paragraph: TextRangeUnit = 3
TextRangeUnit_Line: TextRangeUnit = 4
TextRangeUnit_Story: TextRangeUnit = 5
TextRangeUnit_Screen: TextRangeUnit = 6
TextRangeUnit_Section: TextRangeUnit = 7
TextRangeUnit_Window: TextRangeUnit = 8
TextRangeUnit_CharacterFormat: TextRangeUnit = 9
TextRangeUnit_ParagraphFormat: TextRangeUnit = 10
TextRangeUnit_Object: TextRangeUnit = 11
TextRangeUnit_HardParagraph: TextRangeUnit = 12
TextRangeUnit_Cluster: TextRangeUnit = 13
TextRangeUnit_Bold: TextRangeUnit = 14
TextRangeUnit_Italic: TextRangeUnit = 15
TextRangeUnit_Underline: TextRangeUnit = 16
TextRangeUnit_Strikethrough: TextRangeUnit = 17
TextRangeUnit_ProtectedText: TextRangeUnit = 18
TextRangeUnit_Link: TextRangeUnit = 19
TextRangeUnit_SmallCaps: TextRangeUnit = 20
TextRangeUnit_AllCaps: TextRangeUnit = 21
TextRangeUnit_Hidden: TextRangeUnit = 22
TextRangeUnit_Outline: TextRangeUnit = 23
TextRangeUnit_Shadow: TextRangeUnit = 24
TextRangeUnit_Imprint: TextRangeUnit = 25
TextRangeUnit_Disabled: TextRangeUnit = 26
TextRangeUnit_Revised: TextRangeUnit = 27
TextRangeUnit_Subscript: TextRangeUnit = 28
TextRangeUnit_Superscript: TextRangeUnit = 29
TextRangeUnit_FontBound: TextRangeUnit = 30
TextRangeUnit_LinkProtected: TextRangeUnit = 31
TextRangeUnit_ContentLink: TextRangeUnit = 32
TextScript = Int32
TextScript_Undefined: TextScript = 0
TextScript_Ansi: TextScript = 1
TextScript_EastEurope: TextScript = 2
TextScript_Cyrillic: TextScript = 3
TextScript_Greek: TextScript = 4
TextScript_Turkish: TextScript = 5
TextScript_Hebrew: TextScript = 6
TextScript_Arabic: TextScript = 7
TextScript_Baltic: TextScript = 8
TextScript_Vietnamese: TextScript = 9
TextScript_Default: TextScript = 10
TextScript_Symbol: TextScript = 11
TextScript_Thai: TextScript = 12
TextScript_ShiftJis: TextScript = 13
TextScript_GB2312: TextScript = 14
TextScript_Hangul: TextScript = 15
TextScript_Big5: TextScript = 16
TextScript_PC437: TextScript = 17
TextScript_Oem: TextScript = 18
TextScript_Mac: TextScript = 19
TextScript_Armenian: TextScript = 20
TextScript_Syriac: TextScript = 21
TextScript_Thaana: TextScript = 22
TextScript_Devanagari: TextScript = 23
TextScript_Bengali: TextScript = 24
TextScript_Gurmukhi: TextScript = 25
TextScript_Gujarati: TextScript = 26
TextScript_Oriya: TextScript = 27
TextScript_Tamil: TextScript = 28
TextScript_Telugu: TextScript = 29
TextScript_Kannada: TextScript = 30
TextScript_Malayalam: TextScript = 31
TextScript_Sinhala: TextScript = 32
TextScript_Lao: TextScript = 33
TextScript_Tibetan: TextScript = 34
TextScript_Myanmar: TextScript = 35
TextScript_Georgian: TextScript = 36
TextScript_Jamo: TextScript = 37
TextScript_Ethiopic: TextScript = 38
TextScript_Cherokee: TextScript = 39
TextScript_Aboriginal: TextScript = 40
TextScript_Ogham: TextScript = 41
TextScript_Runic: TextScript = 42
TextScript_Khmer: TextScript = 43
TextScript_Mongolian: TextScript = 44
TextScript_Braille: TextScript = 45
TextScript_Yi: TextScript = 46
TextScript_Limbu: TextScript = 47
TextScript_TaiLe: TextScript = 48
TextScript_NewTaiLue: TextScript = 49
TextScript_SylotiNagri: TextScript = 50
TextScript_Kharoshthi: TextScript = 51
TextScript_Kayahli: TextScript = 52
TextScript_UnicodeSymbol: TextScript = 53
TextScript_Emoji: TextScript = 54
TextScript_Glagolitic: TextScript = 55
TextScript_Lisu: TextScript = 56
TextScript_Vai: TextScript = 57
TextScript_NKo: TextScript = 58
TextScript_Osmanya: TextScript = 59
TextScript_PhagsPa: TextScript = 60
TextScript_Gothic: TextScript = 61
TextScript_Deseret: TextScript = 62
TextScript_Tifinagh: TextScript = 63
TextSetOptions = UInt32
TextSetOptions_None: TextSetOptions = 0
TextSetOptions_UnicodeBidi: TextSetOptions = 1
TextSetOptions_Unlink: TextSetOptions = 8
TextSetOptions_Unhide: TextSetOptions = 16
TextSetOptions_CheckTextLimit: TextSetOptions = 32
TextSetOptions_FormatRtf: TextSetOptions = 8192
TextSetOptions_ApplyRtfDocumentDefaults: TextSetOptions = 16384
UnderlineType = Int32
UnderlineType_Undefined: UnderlineType = 0
UnderlineType_None: UnderlineType = 1
UnderlineType_Single: UnderlineType = 2
UnderlineType_Words: UnderlineType = 3
UnderlineType_Double: UnderlineType = 4
UnderlineType_Dotted: UnderlineType = 5
UnderlineType_Dash: UnderlineType = 6
UnderlineType_DashDot: UnderlineType = 7
UnderlineType_DashDotDot: UnderlineType = 8
UnderlineType_Wave: UnderlineType = 9
UnderlineType_Thick: UnderlineType = 10
UnderlineType_Thin: UnderlineType = 11
UnderlineType_DoubleWave: UnderlineType = 12
UnderlineType_HeavyWave: UnderlineType = 13
UnderlineType_LongDash: UnderlineType = 14
UnderlineType_ThickDash: UnderlineType = 15
UnderlineType_ThickDashDot: UnderlineType = 16
UnderlineType_ThickDashDotDot: UnderlineType = 17
UnderlineType_ThickDotted: UnderlineType = 18
UnderlineType_ThickLongDash: UnderlineType = 19
VerticalCharacterAlignment = Int32
VerticalCharacterAlignment_Top: VerticalCharacterAlignment = 0
VerticalCharacterAlignment_Baseline: VerticalCharacterAlignment = 1
VerticalCharacterAlignment_Bottom: VerticalCharacterAlignment = 2
make_ready(__name__)
