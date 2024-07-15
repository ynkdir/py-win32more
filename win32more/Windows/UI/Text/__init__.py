from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Text
import win32more.Windows.Win32.System.WinRT
class CaretType(Enum, Int32):
    Normal = 0
    Null = 1
class ContentLinkInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.IContentLinkInfo
    _classid_ = 'Windows.UI.Text.ContentLinkInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Text.ContentLinkInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    DisplayText = property(get_DisplayText, put_DisplayText)
    Id = property(get_Id, put_Id)
    LinkContentKind = property(get_LinkContentKind, put_LinkContentKind)
    SecondaryText = property(get_SecondaryText, put_SecondaryText)
    Uri = property(get_Uri, put_Uri)
class FindOptions(Enum, UInt32):
    None_ = 0
    Word = 2
    Case = 4
class FontStretch(Enum, Int32):
    Undefined = 0
    UltraCondensed = 1
    ExtraCondensed = 2
    Condensed = 3
    SemiCondensed = 4
    Normal = 5
    SemiExpanded = 6
    Expanded = 7
    ExtraExpanded = 8
    UltraExpanded = 9
class FontStyle(Enum, Int32):
    Normal = 0
    Oblique = 1
    Italic = 2
class FontWeight(Structure):
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
    _FontWeights_Meta_.Black = property(get_Black, None)
    _FontWeights_Meta_.Bold = property(get_Bold, None)
    _FontWeights_Meta_.ExtraBlack = property(get_ExtraBlack, None)
    _FontWeights_Meta_.ExtraBold = property(get_ExtraBold, None)
    _FontWeights_Meta_.ExtraLight = property(get_ExtraLight, None)
    _FontWeights_Meta_.Light = property(get_Light, None)
    _FontWeights_Meta_.Medium = property(get_Medium, None)
    _FontWeights_Meta_.Normal = property(get_Normal, None)
    _FontWeights_Meta_.SemiBold = property(get_SemiBold, None)
    _FontWeights_Meta_.SemiLight = property(get_SemiLight, None)
    _FontWeights_Meta_.Thin = property(get_Thin, None)
class FormatEffect(Enum, Int32):
    Off = 0
    On = 1
    Toggle = 2
    Undefined = 3
class HorizontalCharacterAlignment(Enum, Int32):
    Left = 0
    Right = 1
    Center = 2
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
    DisplayText = property(get_DisplayText, put_DisplayText)
    Id = property(get_Id, put_Id)
    LinkContentKind = property(get_LinkContentKind, put_LinkContentKind)
    SecondaryText = property(get_SecondaryText, put_SecondaryText)
    Uri = property(get_Uri, put_Uri)
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
    MaxUnitCount = property(get_MaxUnitCount, None)
    MinUnitCount = property(get_MinUnitCount, None)
    UndefinedColor = property(get_UndefinedColor, None)
    UndefinedFloatValue = property(get_UndefinedFloatValue, None)
    UndefinedFontStretch = property(get_UndefinedFontStretch, None)
    UndefinedFontStyle = property(get_UndefinedFontStyle, None)
    UndefinedInt32Value = property(get_UndefinedInt32Value, None)
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
    SpaceAfter = property(get_SpaceAfter, put_SpaceAfter)
    SpaceBefore = property(get_SpaceBefore, put_SpaceBefore)
    Style = property(get_Style, put_Style)
    TabCount = property(get_TabCount, None)
    WidowControl = property(get_WidowControl, put_WidowControl)
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
    EndPosition = property(get_EndPosition, put_EndPosition)
    FormattedText = property(get_FormattedText, put_FormattedText)
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
class LetterCase(Enum, Int32):
    Lower = 0
    Upper = 1
class LineSpacingRule(Enum, Int32):
    Undefined = 0
    Single = 1
    OneAndHalf = 2
    Double = 3
    AtLeast = 4
    Exactly = 5
    Multiple = 6
    Percent = 7
class LinkType(Enum, Int32):
    Undefined = 0
    NotALink = 1
    ClientLink = 2
    FriendlyLinkName = 3
    FriendlyLinkAddress = 4
    AutoLink = 5
    AutoLinkEmail = 6
    AutoLinkPhone = 7
    AutoLinkPath = 8
class MarkerAlignment(Enum, Int32):
    Undefined = 0
    Left = 1
    Center = 2
    Right = 3
class MarkerStyle(Enum, Int32):
    Undefined = 0
    Parenthesis = 1
    Parentheses = 2
    Period = 3
    Plain = 4
    Minus = 5
    NoNumber = 6
class MarkerType(Enum, Int32):
    Undefined = 0
    None_ = 1
    Bullet = 2
    Arabic = 3
    LowercaseEnglishLetter = 4
    UppercaseEnglishLetter = 5
    LowercaseRoman = 6
    UppercaseRoman = 7
    UnicodeSequence = 8
    CircledNumber = 9
    BlackCircleWingding = 10
    WhiteCircleWingding = 11
    ArabicWide = 12
    SimplifiedChinese = 13
    TraditionalChinese = 14
    JapanSimplifiedChinese = 15
    JapanKorea = 16
    ArabicDictionary = 17
    ArabicAbjad = 18
    Hebrew = 19
    ThaiAlphabetic = 20
    ThaiNumeric = 21
    DevanagariVowel = 22
    DevanagariConsonant = 23
    DevanagariNumeric = 24
class ParagraphAlignment(Enum, Int32):
    Undefined = 0
    Left = 1
    Center = 2
    Right = 3
    Justify = 4
class ParagraphStyle(Enum, Int32):
    Undefined = 0
    None_ = 1
    Normal = 2
    Heading1 = 3
    Heading2 = 4
    Heading3 = 5
    Heading4 = 6
    Heading5 = 7
    Heading6 = 8
    Heading7 = 9
    Heading8 = 10
    Heading9 = 11
class PointOptions(Enum, UInt32):
    None_ = 0
    IncludeInset = 1
    Start = 32
    ClientCoordinates = 256
    AllowOffClient = 512
    Transform = 1024
    NoHorizontalScroll = 65536
    NoVerticalScroll = 262144
class RangeGravity(Enum, Int32):
    UIBehavior = 0
    Backward = 1
    Forward = 2
    Inward = 3
    Outward = 4
class RichEditMathMode(Enum, Int32):
    NoMath = 0
    MathOnly = 1
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
    CaretType = property(get_CaretType, put_CaretType)
    DefaultTabStop = property(get_DefaultTabStop, put_DefaultTabStop)
    IgnoreTrailingCharacterSpacing = property(get_IgnoreTrailingCharacterSpacing, put_IgnoreTrailingCharacterSpacing)
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
    Character = property(get_Character, put_Character)
    CharacterFormat = property(get_CharacterFormat, put_CharacterFormat)
    ContentLinkInfo = property(get_ContentLinkInfo, put_ContentLinkInfo)
    EndPosition = property(get_EndPosition, put_EndPosition)
    FormattedText = property(get_FormattedText, put_FormattedText)
    Gravity = property(get_Gravity, put_Gravity)
    Length = property(get_Length, None)
    Link = property(get_Link, put_Link)
    ParagraphFormat = property(get_ParagraphFormat, put_ParagraphFormat)
    StartPosition = property(get_StartPosition, put_StartPosition)
    StoryLength = property(get_StoryLength, None)
    Text = property(get_Text, put_Text)
class SelectionOptions(Enum, UInt32):
    StartActive = 1
    AtEndOfLine = 2
    Overtype = 4
    Active = 8
    Replace = 16
class SelectionType(Enum, Int32):
    None_ = 0
    InsertionPoint = 1
    Normal = 2
    InlineShape = 7
    Shape = 8
class TabAlignment(Enum, Int32):
    Left = 0
    Center = 1
    Right = 2
    Decimal = 3
    Bar = 4
class TabLeader(Enum, Int32):
    Spaces = 0
    Dots = 1
    Dashes = 2
    Lines = 3
    ThickLines = 4
    Equals = 5
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
    _TextConstants_Meta_.AutoColor = property(get_AutoColor, None)
    _TextConstants_Meta_.MaxUnitCount = property(get_MaxUnitCount, None)
    _TextConstants_Meta_.MinUnitCount = property(get_MinUnitCount, None)
    _TextConstants_Meta_.UndefinedColor = property(get_UndefinedColor, None)
    _TextConstants_Meta_.UndefinedFloatValue = property(get_UndefinedFloatValue, None)
    _TextConstants_Meta_.UndefinedFontStretch = property(get_UndefinedFontStretch, None)
    _TextConstants_Meta_.UndefinedFontStyle = property(get_UndefinedFontStyle, None)
    _TextConstants_Meta_.UndefinedInt32Value = property(get_UndefinedInt32Value, None)
class TextDecorations(Enum, UInt32):
    None_ = 0
    Underline = 1
    Strikethrough = 2
class TextGetOptions(Enum, UInt32):
    None_ = 0
    AdjustCrlf = 1
    UseCrlf = 2
    UseObjectText = 4
    AllowFinalEop = 8
    NoHidden = 32
    IncludeNumbering = 64
    FormatRtf = 8192
    UseLf = 16777216
class TextRangeUnit(Enum, Int32):
    Character = 0
    Word = 1
    Sentence = 2
    Paragraph = 3
    Line = 4
    Story = 5
    Screen = 6
    Section = 7
    Window = 8
    CharacterFormat = 9
    ParagraphFormat = 10
    Object = 11
    HardParagraph = 12
    Cluster = 13
    Bold = 14
    Italic = 15
    Underline = 16
    Strikethrough = 17
    ProtectedText = 18
    Link = 19
    SmallCaps = 20
    AllCaps = 21
    Hidden = 22
    Outline = 23
    Shadow = 24
    Imprint = 25
    Disabled = 26
    Revised = 27
    Subscript = 28
    Superscript = 29
    FontBound = 30
    LinkProtected = 31
    ContentLink = 32
class TextScript(Enum, Int32):
    Undefined = 0
    Ansi = 1
    EastEurope = 2
    Cyrillic = 3
    Greek = 4
    Turkish = 5
    Hebrew = 6
    Arabic = 7
    Baltic = 8
    Vietnamese = 9
    Default = 10
    Symbol = 11
    Thai = 12
    ShiftJis = 13
    GB2312 = 14
    Hangul = 15
    Big5 = 16
    PC437 = 17
    Oem = 18
    Mac = 19
    Armenian = 20
    Syriac = 21
    Thaana = 22
    Devanagari = 23
    Bengali = 24
    Gurmukhi = 25
    Gujarati = 26
    Oriya = 27
    Tamil = 28
    Telugu = 29
    Kannada = 30
    Malayalam = 31
    Sinhala = 32
    Lao = 33
    Tibetan = 34
    Myanmar = 35
    Georgian = 36
    Jamo = 37
    Ethiopic = 38
    Cherokee = 39
    Aboriginal = 40
    Ogham = 41
    Runic = 42
    Khmer = 43
    Mongolian = 44
    Braille = 45
    Yi = 46
    Limbu = 47
    TaiLe = 48
    NewTaiLue = 49
    SylotiNagri = 50
    Kharoshthi = 51
    Kayahli = 52
    UnicodeSymbol = 53
    Emoji = 54
    Glagolitic = 55
    Lisu = 56
    Vai = 57
    NKo = 58
    Osmanya = 59
    PhagsPa = 60
    Gothic = 61
    Deseret = 62
    Tifinagh = 63
class TextSetOptions(Enum, UInt32):
    None_ = 0
    UnicodeBidi = 1
    Unlink = 8
    Unhide = 16
    CheckTextLimit = 32
    FormatRtf = 8192
    ApplyRtfDocumentDefaults = 16384
class UnderlineType(Enum, Int32):
    Undefined = 0
    None_ = 1
    Single = 2
    Words = 3
    Double = 4
    Dotted = 5
    Dash = 6
    DashDot = 7
    DashDotDot = 8
    Wave = 9
    Thick = 10
    Thin = 11
    DoubleWave = 12
    HeavyWave = 13
    LongDash = 14
    ThickDash = 15
    ThickDashDot = 16
    ThickDashDotDot = 17
    ThickDotted = 18
    ThickLongDash = 19
class VerticalCharacterAlignment(Enum, Int32):
    Top = 0
    Baseline = 1
    Bottom = 2


make_ready(__name__)
