from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Graphics.Canvas
import win32more.Microsoft.Graphics.Canvas.Brushes
import win32more.Microsoft.Graphics.Canvas.Text
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.UI
import win32more.Windows.UI.Text
import win32more.Windows.Win32.System.WinRT
class CanvasAnalyzedBidi(Structure):
    ExplicitLevel: UInt32
    ResolvedLevel: UInt32
class CanvasAnalyzedBreakpoint(Structure):
    BreakBefore: win32more.Microsoft.Graphics.Canvas.Text.CanvasLineBreakCondition
    BreakAfter: win32more.Microsoft.Graphics.Canvas.Text.CanvasLineBreakCondition
    IsWhitespace: Boolean
    IsSoftHyphen: Boolean
class CanvasAnalyzedGlyphOrientation(Structure):
    GlyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphOrientation
    AdjustedBidiLevel: UInt32
    IsSideways: Boolean
    IsRightToLeft: Boolean
class CanvasAnalyzedScript(Structure):
    ScriptIdentifier: Int32
    Shape: win32more.Microsoft.Graphics.Canvas.Text.CanvasScriptShape
class CanvasCharacterRange(Structure):
    CharacterIndex: Int32
    CharacterCount: Int32
class CanvasClusterMetrics(Structure):
    CharacterCount: Int32
    Width: Single
    Properties: win32more.Microsoft.Graphics.Canvas.Text.CanvasClusterProperties
class CanvasClusterProperties(Enum, UInt32):
    None_ = 0
    CanWrapLineAfter = 1
    Whitespace = 2
    Newline = 4
    SoftHyphen = 8
    RightToLeft = 16
class CanvasDrawTextOptions(Enum, UInt32):
    Default = 0
    NoPixelSnap = 1
    Clip = 2
    EnableColorFont = 4
class CanvasFontFace(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasFontFace'
    @winrt_mixinmethod
    def GetRecommendedRenderingMode(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, fontSize: Single, dpi: Single, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, renderingParameters: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode: ...
    @winrt_mixinmethod
    def GetRecommendedRenderingModeWithAllOptions(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, fontSize: Single, dpi: Single, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, renderingParameters: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters, transform: win32more.Windows.Foundation.Numerics.Matrix3x2, isSideways: Boolean, outlineThreshold: win32more.Microsoft.Graphics.Canvas.CanvasAntialiasing) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode: ...
    @winrt_mixinmethod
    def GetRecommendedGridFit(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, fontSize: Single, dpi: Single, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, renderingParameters: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters, transform: win32more.Windows.Foundation.Numerics.Matrix3x2, isSideways: Boolean, outlineThreshold: win32more.Microsoft.Graphics.Canvas.CanvasAntialiasing) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextGridFit: ...
    @winrt_mixinmethod
    def get_GlyphBox(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_SubscriptPosition(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_SubscriptSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SuperscriptPosition(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_SuperscriptSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_HasTypographicMetrics(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Boolean: ...
    @winrt_mixinmethod
    def get_Ascent(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_Descent(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_LineGap(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_CapHeight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_LowercaseLetterHeight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_UnderlinePosition(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_UnderlineThickness(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_StrikethroughPosition(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_StrikethroughThickness(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_CaretSlopeRise(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_CaretSlopeRun(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_CaretOffset(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Single: ...
    @winrt_mixinmethod
    def get_UnicodeRanges(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasUnicodeRange]: ...
    @winrt_mixinmethod
    def get_IsMonospaced(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Boolean: ...
    @winrt_mixinmethod
    def GetVerticalGlyphVariants(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, inputElements: PassArray[Int32]) -> ReceiveArray[Int32]: ...
    @winrt_mixinmethod
    def get_HasVerticalGlyphVariants(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Boolean: ...
    @winrt_mixinmethod
    def get_FileFormatType(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFileFormatType: ...
    @winrt_mixinmethod
    def get_Simulations(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSimulations: ...
    @winrt_mixinmethod
    def get_IsSymbolFont(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> Boolean: ...
    @winrt_mixinmethod
    def get_GlyphCount(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> UInt32: ...
    @winrt_mixinmethod
    def GetGlyphIndices(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, inputElements: PassArray[UInt32]) -> ReceiveArray[Int32]: ...
    @winrt_mixinmethod
    def GetGlyphMetrics(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, inputElements: PassArray[Int32], isSideways: Boolean) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphMetrics]: ...
    @winrt_mixinmethod
    def GetGdiCompatibleGlyphMetrics(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, fontSize: Single, dpi: Single, transform: win32more.Windows.Foundation.Numerics.Matrix3x2, useGdiNatural: Boolean, inputElements: PassArray[Int32], isSideways: Boolean) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphMetrics]: ...
    @winrt_mixinmethod
    def get_Weight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_mixinmethod
    def get_Stretch(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_mixinmethod
    def get_Style(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_mixinmethod
    def get_FamilyNames(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_FaceNames(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def GetInformationalStrings(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, fontInformation: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontInformation) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def HasCharacter(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, unicodeValue: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def GetGlyphRunBounds(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, drawingSession: win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession, point: win32more.Windows.Foundation.Numerics.Vector2, fontSize: Single, glyphs: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], isSideways: Boolean, bidiLevel: UInt32) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetGlyphRunBoundsWithMeasuringMode(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, drawingSession: win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession, point: win32more.Windows.Foundation.Numerics.Vector2, fontSize: Single, glyphs: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], isSideways: Boolean, bidiLevel: UInt32, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Panose(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def GetSupportedTypographicFeatureNames(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName]: ...
    @winrt_mixinmethod
    def GetSupportedTypographicFeatureNamesWithLocale(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, locale: WinRT_String) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName]: ...
    @winrt_mixinmethod
    def GetTypographicFeatureGlyphSupport(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, typographicFeatureName: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName, glyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]) -> ReceiveArray[Boolean]: ...
    @winrt_mixinmethod
    def GetTypographicFeatureGlyphSupportWithLocale(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontFace, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, typographicFeatureName: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName, glyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], locale: WinRT_String) -> ReceiveArray[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Ascent = property(get_Ascent, None)
    CapHeight = property(get_CapHeight, None)
    CaretOffset = property(get_CaretOffset, None)
    CaretSlopeRise = property(get_CaretSlopeRise, None)
    CaretSlopeRun = property(get_CaretSlopeRun, None)
    Descent = property(get_Descent, None)
    FaceNames = property(get_FaceNames, None)
    FamilyNames = property(get_FamilyNames, None)
    FileFormatType = property(get_FileFormatType, None)
    GlyphBox = property(get_GlyphBox, None)
    GlyphCount = property(get_GlyphCount, None)
    HasTypographicMetrics = property(get_HasTypographicMetrics, None)
    HasVerticalGlyphVariants = property(get_HasVerticalGlyphVariants, None)
    IsMonospaced = property(get_IsMonospaced, None)
    IsSymbolFont = property(get_IsSymbolFont, None)
    LineGap = property(get_LineGap, None)
    LowercaseLetterHeight = property(get_LowercaseLetterHeight, None)
    Panose = property(get_Panose, None)
    Simulations = property(get_Simulations, None)
    Stretch = property(get_Stretch, None)
    StrikethroughPosition = property(get_StrikethroughPosition, None)
    StrikethroughThickness = property(get_StrikethroughThickness, None)
    Style = property(get_Style, None)
    SubscriptPosition = property(get_SubscriptPosition, None)
    SubscriptSize = property(get_SubscriptSize, None)
    SuperscriptPosition = property(get_SuperscriptPosition, None)
    SuperscriptSize = property(get_SuperscriptSize, None)
    UnderlinePosition = property(get_UnderlinePosition, None)
    UnderlineThickness = property(get_UnderlineThickness, None)
    UnicodeRanges = property(get_UnicodeRanges, None)
    Weight = property(get_Weight, None)
class CanvasFontFileFormatType(Enum, Int32):
    Cff = 0
    TrueType = 1
    TrueTypeCollection = 2
    Type1 = 3
    Vector = 4
    Bitmap = 5
    Unknown = 6
    RawCff = 7
class CanvasFontInformation(Enum, Int32):
    None_ = 0
    CopyrightNotice = 1
    VersionStrings = 2
    Trademark = 3
    Manufacturer = 4
    Designer = 5
    DesignerUrl = 6
    Description = 7
    FontVendorUrl = 8
    LicenseDescription = 9
    LicenseInfoUrl = 10
    Win32FamilyNames = 11
    Win32SubfamilyNames = 12
    PreferredFamilyNames = 13
    PreferredSubfamilyNames = 14
    SampleText = 15
    FullName = 16
    PostscriptName = 17
    PostscriptCidName = 18
    WwsFamilyName = 19
    DesignScriptLanguageTag = 20
    SupportedScriptLanguageTag = 21
class CanvasFontProperty(Structure):
    Identifier: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontPropertyIdentifier
    Value: WinRT_String
    Locale: WinRT_String
class CanvasFontPropertyIdentifier(Enum, Int32):
    None_ = 0
    FamilyName = 1
    PreferredFamilyName = 2
    FaceName = 3
    FullName = 4
    Win32FamilyName = 5
    PostscriptName = 6
    DesignScriptLanguageTag = 7
    SupportedScriptLanguageTag = 8
    SemanticTag = 9
    Weight = 10
    Stretch = 11
    Style = 12
    Total = 13
class CanvasFontSet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasFontSet'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSetFactory, uri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
    @winrt_mixinmethod
    def get_Fonts(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace]: ...
    @winrt_mixinmethod
    def TryFindFontFace(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, index: POINTER(Int32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMatchingFontsFromProperties(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet, propertyElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty]) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
    @winrt_mixinmethod
    def GetMatchingFontsFromWwsFamily(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet, familyName: WinRT_String, weight: win32more.Windows.UI.Text.FontWeight, stretch: win32more.Windows.UI.Text.FontStretch, style: win32more.Windows.UI.Text.FontStyle) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
    @winrt_mixinmethod
    def CountFontsMatchingProperty(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet, property: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty) -> UInt32: ...
    @winrt_mixinmethod
    def GetPropertyValuesFromIndex(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet, fontIndex: UInt32, propertyIdentifier: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontPropertyIdentifier) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def GetPropertyValuesFromIdentifier(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet, propertyIdentifier: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontPropertyIdentifier, preferredLocaleNames: WinRT_String) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty]: ...
    @winrt_mixinmethod
    def GetPropertyValues(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSet, propertyIdentifier: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontPropertyIdentifier) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetSystemFontSet(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasFontSetStatics) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
    Fonts = property(get_Fonts, None)
class CanvasFontSimulations(Enum, UInt32):
    None_ = 0
    Bold = 1
    Oblique = 2
class CanvasGlyph(Structure):
    Index: Int32
    Advance: Single
    AdvanceOffset: Single
    AscenderOffset: Single
class CanvasGlyphJustification(Enum, Int32):
    None_ = 0
    ArabicBlank = 1
    Character = 2
    Blank = 4
    ArabicNormal = 7
    ArabicKashida = 8
    ArabicAlef = 9
    ArabicHa = 10
    ArabicRa = 11
    ArabicBa = 12
    ArabicBara = 13
    ArabicSeen = 14
    ArabicSeenM = 15
class CanvasGlyphMetrics(Structure):
    LeftSideBearing: Single
    AdvanceWidth: Single
    RightSideBearing: Single
    TopSideBearing: Single
    AdvanceHeight: Single
    BottomSideBearing: Single
    VerticalOrigin: Single
    DrawBounds: win32more.Windows.Foundation.Rect
class CanvasGlyphOrientation(Enum, Int32):
    Upright = 0
    Clockwise90Degrees = 1
    Clockwise180Degrees = 2
    Clockwise270Degrees = 3
class CanvasGlyphShaping(Structure):
    Justification: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphJustification
    IsClusterStart: Boolean
    IsDiacritic: Boolean
    IsZeroWidthSpace: Boolean
class CanvasHorizontalAlignment(Enum, Int32):
    Left = 0
    Right = 1
    Center = 2
    Justified = 3
class CanvasJustificationOpportunity(Structure):
    ExpansionMinimum: Single
    ExpansionMaximum: Single
    CompressionMaximum: Single
    ExpansionPriority: Byte
    CompressionPriority: Byte
    AllowResidualExpansion: Boolean
    AllowResidualCompression: Boolean
    ApplyToLeadingEdge: Boolean
    ApplyToTrailingEdge: Boolean
class CanvasLineBreakCondition(Enum, Int32):
    Neutral = 0
    CanBreak = 1
    CannotBreak = 2
    MustBreak = 3
class CanvasLineMetrics(Structure):
    CharacterCount: Int32
    TrailingWhitespaceCount: Int32
    TerminalNewlineCount: Int32
    Height: Single
    Baseline: Single
    IsTrimmed: Boolean
    LeadingWhitespaceBefore: Single
    LeadingWhitespaceAfter: Single
class CanvasLineSpacingMode(Enum, Int32):
    Default = 0
    Uniform = 1
    Proportional = 2
class CanvasNumberSubstitution(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasNumberSubstitution
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution.CreateWithLocaleAndIgnoreOverrides(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasNumberSubstitutionFactory, method: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitutionMethod) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution: ...
    @winrt_factorymethod
    def CreateWithLocaleAndIgnoreOverrides(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasNumberSubstitutionFactory, method: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitutionMethod, localeName: WinRT_String, ignoreEnvironmentOverrides: Boolean) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class CanvasNumberSubstitutionMethod(Enum, Int32):
    FromCulture = 0
    Contextual = 1
    Disabled = 2
    National = 3
    Traditional = 4
class CanvasOpticalAlignment(Enum, Int32):
    Default = 0
    NoSideBearings = 1
class CanvasScaledFont(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasScaledFont
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasScaledFont'
    @winrt_mixinmethod
    def get_FontFace(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasScaledFont) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace: ...
    @winrt_mixinmethod
    def get_ScaleFactor(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasScaledFont) -> Single: ...
    FontFace = property(get_FontFace, None)
    ScaleFactor = property(get_ScaleFactor, None)
class CanvasScriptProperties(Structure):
    IsoScriptCode: WinRT_String
    IsoScriptNumber: Int32
    ClusterLookahead: Int32
    JustificationCharacter: WinRT_String
    RestrictCaretToClusters: Boolean
    UsesWordDividers: Boolean
    IsDiscreteWriting: Boolean
    IsBlockWriting: Boolean
    IsDistributedWithinCluster: Boolean
    IsConnectedWriting: Boolean
    IsCursiveWriting: Boolean
class CanvasScriptShape(Enum, Int32):
    Default = 0
    NoVisual = 1
class CanvasTextAnalyzer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer.CreateWithOptions(*args))
        elif len(args) == 5:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer.CreateWithNumberSubstitutionAndVerticalGlyphOrientationAndBidiLevel(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzerFactory, text: WinRT_String, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer: ...
    @winrt_factorymethod
    def CreateWithOptions(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzerFactory, text: WinRT_String, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection, options: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzerOptions) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer: ...
    @winrt_factorymethod
    def CreateWithNumberSubstitutionAndVerticalGlyphOrientationAndBidiLevel(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzerFactory, text: WinRT_String, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection, numberSubstitution: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution, verticalGlyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation, bidiLevel: UInt32) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer: ...
    @winrt_mixinmethod
    def GetFontsUsingSystemFontSet(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, textFormat: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasScaledFont]]: ...
    @winrt_mixinmethod
    def GetFonts(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, textFormat: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat, fontSet: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasScaledFont]]: ...
    @winrt_mixinmethod
    def GetBidi(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBidi]]: ...
    @winrt_mixinmethod
    def GetBidiWithLocale(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, locale: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBidi]]: ...
    @winrt_mixinmethod
    def GetBreakpoints(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBreakpoint]: ...
    @winrt_mixinmethod
    def GetBreakpointsWithLocale(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, locale: WinRT_String) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBreakpoint]: ...
    @winrt_mixinmethod
    def GetNumberSubstitutions(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution]]: ...
    @winrt_mixinmethod
    def GetScript(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript]]: ...
    @winrt_mixinmethod
    def GetScriptWithLocale(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, locale: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript]]: ...
    @winrt_mixinmethod
    def GetGlyphOrientations(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedGlyphOrientation]]: ...
    @winrt_mixinmethod
    def GetGlyphOrientationsWithLocale(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, locale: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedGlyphOrientation]]: ...
    @winrt_mixinmethod
    def GetScriptProperties(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, analyzedScript: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasScriptProperties: ...
    @winrt_mixinmethod
    def GetGlyphs(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, characterRange: win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, isSideways: Boolean, isRightToLeft: Boolean, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_mixinmethod
    def GetGlyphsWithAllOptions(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, characterRange: win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, isSideways: Boolean, isRightToLeft: Boolean, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, locale: WinRT_String, numberSubstitution: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution, typographyRanges: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography]], clusterMapIndicesElements: ReceiveArray[Int32], isShapedAloneGlyphsElements: ReceiveArray[Boolean], glyphShapingResultsElements: ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_mixinmethod
    def GetJustificationOpportunities(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, characterRange: win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, clusterMapIndicesElements: PassArray[Int32], glyphShapingResultsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasJustificationOpportunity]: ...
    @winrt_mixinmethod
    def ApplyJustificationOpportunities(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, lineWidth: Single, justificationOpportunitiesElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasJustificationOpportunity], sourceGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_mixinmethod
    def AddGlyphsAfterJustification(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, clusterMapIndicesElements: PassArray[Int32], originalGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], justifiedGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], glyphShapingResultsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_mixinmethod
    def AddGlyphsAfterJustificationWithClusterMap(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, clusterMapIndicesElements: PassArray[Int32], originalGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], justifiedGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], glyphShapingResultsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping], outputClusterMapIndicesElements: ReceiveArray[Int32]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class CanvasTextAntialiasing(Enum, Int32):
    Auto = 0
    ClearType = 1
    Grayscale = 2
    Aliased = 3
class CanvasTextDirection(Enum, Int32):
    LeftToRightThenTopToBottom = 0
    RightToLeftThenTopToBottom = 1
    LeftToRightThenBottomToTop = 2
    RightToLeftThenBottomToTop = 3
    TopToBottomThenLeftToRight = 4
    BottomToTopThenLeftToRight = 5
    TopToBottomThenRightToLeft = 6
    BottomToTopThenRightToLeft = 7
class CanvasTextFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasTextFormat'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection) -> Void: ...
    @winrt_mixinmethod
    def get_FontFamily(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FontFamily(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FontSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> Single: ...
    @winrt_mixinmethod
    def put_FontSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_FontStretch(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_mixinmethod
    def put_FontStretch(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Windows.UI.Text.FontStretch) -> Void: ...
    @winrt_mixinmethod
    def get_FontStyle(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_mixinmethod
    def put_FontStyle(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Windows.UI.Text.FontStyle) -> Void: ...
    @winrt_mixinmethod
    def get_FontWeight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_mixinmethod
    def put_FontWeight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Windows.UI.Text.FontWeight) -> Void: ...
    @winrt_mixinmethod
    def get_IncrementalTabStop(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> Single: ...
    @winrt_mixinmethod
    def put_IncrementalTabStop(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacing(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> Single: ...
    @winrt_mixinmethod
    def put_LineSpacing(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacingBaseline(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> Single: ...
    @winrt_mixinmethod
    def put_LineSpacingBaseline(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LocaleName(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LocaleName(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment: ...
    @winrt_mixinmethod
    def put_VerticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment: ...
    @winrt_mixinmethod
    def put_HorizontalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingGranularity(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity: ...
    @winrt_mixinmethod
    def put_TrimmingGranularity(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingDelimiter(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TrimmingDelimiter(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingDelimiterCount(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> Int32: ...
    @winrt_mixinmethod
    def put_TrimmingDelimiterCount(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_WordWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping: ...
    @winrt_mixinmethod
    def put_WordWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping) -> Void: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions: ...
    @winrt_mixinmethod
    def put_Options(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalGlyphOrientation(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation: ...
    @winrt_mixinmethod
    def put_VerticalGlyphOrientation(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_OpticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment: ...
    @winrt_mixinmethod
    def put_OpticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_LastLineWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> Boolean: ...
    @winrt_mixinmethod
    def put_LastLineWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacingMode(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode: ...
    @winrt_mixinmethod
    def put_LineSpacingMode(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign: ...
    @winrt_mixinmethod
    def put_TrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign) -> Void: ...
    @winrt_mixinmethod
    def get_CustomTrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat) -> win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject: ...
    @winrt_mixinmethod
    def put_CustomTrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormat, value: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetSystemFontFamilies(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormatStatics) -> ReceiveArray[WinRT_String]: ...
    @winrt_classmethod
    def GetSystemFontFamiliesFromLocaleList(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextFormatStatics, localeList: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> ReceiveArray[WinRT_String]: ...
    CustomTrimmingSign = property(get_CustomTrimmingSign, put_CustomTrimmingSign)
    Direction = property(get_Direction, put_Direction)
    FontFamily = property(get_FontFamily, put_FontFamily)
    FontSize = property(get_FontSize, put_FontSize)
    FontStretch = property(get_FontStretch, put_FontStretch)
    FontStyle = property(get_FontStyle, put_FontStyle)
    FontWeight = property(get_FontWeight, put_FontWeight)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    IncrementalTabStop = property(get_IncrementalTabStop, put_IncrementalTabStop)
    LastLineWrapping = property(get_LastLineWrapping, put_LastLineWrapping)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineSpacingBaseline = property(get_LineSpacingBaseline, put_LineSpacingBaseline)
    LineSpacingMode = property(get_LineSpacingMode, put_LineSpacingMode)
    LocaleName = property(get_LocaleName, put_LocaleName)
    OpticalAlignment = property(get_OpticalAlignment, put_OpticalAlignment)
    Options = property(get_Options, put_Options)
    TrimmingDelimiter = property(get_TrimmingDelimiter, put_TrimmingDelimiter)
    TrimmingDelimiterCount = property(get_TrimmingDelimiterCount, put_TrimmingDelimiterCount)
    TrimmingGranularity = property(get_TrimmingGranularity, put_TrimmingGranularity)
    TrimmingSign = property(get_TrimmingSign, put_TrimmingSign)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    VerticalGlyphOrientation = property(get_VerticalGlyphOrientation, put_VerticalGlyphOrientation)
    WordWrapping = property(get_WordWrapping, put_WordWrapping)
class CanvasTextGridFit(Enum, Int32):
    Default = 0
    Disable = 1
    Enable = 2
class CanvasTextLayout(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasTextLayout'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 5:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayout.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayoutFactory, resourceCreator: win32more.Microsoft.Graphics.Canvas.ICanvasResourceCreator, textString: WinRT_String, textFormat: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat, requestedWidth: Single, requestedHeight: Single) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayout: ...
    @winrt_mixinmethod
    def GetFormatChangeIndices(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> ReceiveArray[Int32]: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultFontFamily(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefaultFontSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Single: ...
    @winrt_mixinmethod
    def get_DefaultFontStretch(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_mixinmethod
    def get_DefaultFontStyle(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_mixinmethod
    def get_DefaultFontWeight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_mixinmethod
    def get_IncrementalTabStop(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Single: ...
    @winrt_mixinmethod
    def put_IncrementalTabStop(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacing(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Single: ...
    @winrt_mixinmethod
    def put_LineSpacing(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacingBaseline(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Single: ...
    @winrt_mixinmethod
    def put_LineSpacingBaseline(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultLocaleName(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VerticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment: ...
    @winrt_mixinmethod
    def put_VerticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment: ...
    @winrt_mixinmethod
    def put_HorizontalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingGranularity(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity: ...
    @winrt_mixinmethod
    def put_TrimmingGranularity(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingDelimiter(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TrimmingDelimiter(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingDelimiterCount(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Int32: ...
    @winrt_mixinmethod
    def put_TrimmingDelimiterCount(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_WordWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping: ...
    @winrt_mixinmethod
    def put_WordWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping) -> Void: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions: ...
    @winrt_mixinmethod
    def put_Options(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacingMode(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode: ...
    @winrt_mixinmethod
    def put_LineSpacingMode(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode) -> Void: ...
    @winrt_mixinmethod
    def get_TrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign: ...
    @winrt_mixinmethod
    def put_TrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign) -> Void: ...
    @winrt_mixinmethod
    def get_CustomTrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject: ...
    @winrt_mixinmethod
    def put_CustomTrimmingSign(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject) -> Void: ...
    @winrt_mixinmethod
    def get_RequestedSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_RequestedSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def GetMinimumLineLength(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Single: ...
    @winrt_mixinmethod
    def GetBrush(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> win32more.Microsoft.Graphics.Canvas.Brushes.ICanvasBrush: ...
    @winrt_mixinmethod
    def GetCustomBrush(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetFontFamily(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetFontSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> Single: ...
    @winrt_mixinmethod
    def GetFontStretch(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_mixinmethod
    def GetFontStyle(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_mixinmethod
    def GetFontWeight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_mixinmethod
    def GetLocaleName(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetStrikethrough(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> Boolean: ...
    @winrt_mixinmethod
    def GetUnderline(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> Boolean: ...
    @winrt_mixinmethod
    def GetInlineObject(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject: ...
    @winrt_mixinmethod
    def SetColor(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, color: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetBrush(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, brush: win32more.Microsoft.Graphics.Canvas.Brushes.ICanvasBrush) -> Void: ...
    @winrt_mixinmethod
    def SetCustomBrush(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, brush: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def SetFontFamily(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, fontFamily: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetFontSize(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, fontSize: Single) -> Void: ...
    @winrt_mixinmethod
    def SetFontStretch(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, fontStretch: win32more.Windows.UI.Text.FontStretch) -> Void: ...
    @winrt_mixinmethod
    def SetFontStyle(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, fontStyle: win32more.Windows.UI.Text.FontStyle) -> Void: ...
    @winrt_mixinmethod
    def SetFontWeight(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, fontWeight: win32more.Windows.UI.Text.FontWeight) -> Void: ...
    @winrt_mixinmethod
    def SetLocaleName(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetStrikethrough(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, hasStrikethrough: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetUnderline(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, hasUnderline: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetInlineObject(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, inlineObject: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject) -> Void: ...
    @winrt_mixinmethod
    def DrawToTextRenderer(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, textRenderer: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderer, position: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def DrawToTextRendererWithCoords(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, textRenderer: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderer, x: Single, y: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LineMetrics(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasLineMetrics]: ...
    @winrt_mixinmethod
    def get_ClusterMetrics(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasClusterMetrics]: ...
    @winrt_mixinmethod
    def SetTypography(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, typography: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography) -> Void: ...
    @winrt_mixinmethod
    def GetTypography(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography: ...
    @winrt_mixinmethod
    def get_LayoutBounds(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_LayoutBoundsIncludingTrailingWhitespace(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_LineCount(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Int32: ...
    @winrt_mixinmethod
    def get_MaximumBidiReorderingDepth(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Int32: ...
    @winrt_mixinmethod
    def get_DrawBounds(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def HitTest(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, point: win32more.Windows.Foundation.Numerics.Vector2) -> Boolean: ...
    @winrt_mixinmethod
    def HitTestWithCoords(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, x: Single, y: Single) -> Boolean: ...
    @winrt_mixinmethod
    def HitTestWithDescription(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, point: win32more.Windows.Foundation.Numerics.Vector2, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion)) -> Boolean: ...
    @winrt_mixinmethod
    def HitTestWithDescriptionAndCoords(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, x: Single, y: Single, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion)) -> Boolean: ...
    @winrt_mixinmethod
    def HitTestWithDescriptionAndTrailingSide(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, point: win32more.Windows.Foundation.Numerics.Vector2, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion), trailingSideOfCharacter: POINTER(Boolean)) -> Boolean: ...
    @winrt_mixinmethod
    def HitTestWithDescriptionAndCoordsAndTrailingSide(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, x: Single, y: Single, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion), trailingSideOfCharacter: POINTER(Boolean)) -> Boolean: ...
    @winrt_mixinmethod
    def GetCaretPosition(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, trailingSideOfCharacter: Boolean) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def GetCaretPositionWithDescription(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, trailingSideOfCharacter: Boolean, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion)) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def GetCharacterRegions(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion]: ...
    @winrt_mixinmethod
    def GetPairKerning(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> Boolean: ...
    @winrt_mixinmethod
    def SetPairKerning(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, hasPairKerning: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetLeadingCharacterSpacing(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> Single: ...
    @winrt_mixinmethod
    def GetTrailingCharacterSpacing(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> Single: ...
    @winrt_mixinmethod
    def GetMinimumCharacterAdvance(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32) -> Single: ...
    @winrt_mixinmethod
    def SetCharacterSpacing(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, characterIndex: Int32, characterCount: Int32, leadingSpacing: Single, trailingSpacing: Single, minimumAdvance: Single) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalGlyphOrientation(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation: ...
    @winrt_mixinmethod
    def put_VerticalGlyphOrientation(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_OpticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment: ...
    @winrt_mixinmethod
    def put_OpticalAlignment(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_LastLineWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> Boolean: ...
    @winrt_mixinmethod
    def put_LastLineWrapping(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Device(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayout) -> win32more.Microsoft.Graphics.Canvas.CanvasDevice: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetGlyphOrientationTransform(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextLayoutStatics, glyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphOrientation, isSideways: Boolean, position: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    ClusterMetrics = property(get_ClusterMetrics, None)
    CustomTrimmingSign = property(get_CustomTrimmingSign, put_CustomTrimmingSign)
    DefaultFontFamily = property(get_DefaultFontFamily, None)
    DefaultFontSize = property(get_DefaultFontSize, None)
    DefaultFontStretch = property(get_DefaultFontStretch, None)
    DefaultFontStyle = property(get_DefaultFontStyle, None)
    DefaultFontWeight = property(get_DefaultFontWeight, None)
    DefaultLocaleName = property(get_DefaultLocaleName, None)
    Device = property(get_Device, None)
    Direction = property(get_Direction, put_Direction)
    DrawBounds = property(get_DrawBounds, None)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    IncrementalTabStop = property(get_IncrementalTabStop, put_IncrementalTabStop)
    LastLineWrapping = property(get_LastLineWrapping, put_LastLineWrapping)
    LayoutBounds = property(get_LayoutBounds, None)
    LayoutBoundsIncludingTrailingWhitespace = property(get_LayoutBoundsIncludingTrailingWhitespace, None)
    LineCount = property(get_LineCount, None)
    LineMetrics = property(get_LineMetrics, None)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineSpacingBaseline = property(get_LineSpacingBaseline, put_LineSpacingBaseline)
    LineSpacingMode = property(get_LineSpacingMode, put_LineSpacingMode)
    MaximumBidiReorderingDepth = property(get_MaximumBidiReorderingDepth, None)
    OpticalAlignment = property(get_OpticalAlignment, put_OpticalAlignment)
    Options = property(get_Options, put_Options)
    RequestedSize = property(get_RequestedSize, put_RequestedSize)
    TrimmingDelimiter = property(get_TrimmingDelimiter, put_TrimmingDelimiter)
    TrimmingDelimiterCount = property(get_TrimmingDelimiterCount, put_TrimmingDelimiterCount)
    TrimmingGranularity = property(get_TrimmingGranularity, put_TrimmingGranularity)
    TrimmingSign = property(get_TrimmingSign, put_TrimmingSign)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    VerticalGlyphOrientation = property(get_VerticalGlyphOrientation, put_VerticalGlyphOrientation)
    WordWrapping = property(get_WordWrapping, put_WordWrapping)
class CanvasTextLayoutRegion(Structure):
    CharacterIndex: Int32
    CharacterCount: Int32
    LayoutBounds: win32more.Windows.Foundation.Rect
class CanvasTextMeasuringMode(Enum, Int32):
    Natural = 0
    GdiClassic = 1
    GdiNatural = 2
class CanvasTextRenderingMode(Enum, Int32):
    Default = 0
    Aliased = 1
    GdiClassic = 2
    GdiNatural = 3
    Natural = 4
    NaturalSymmetric = 5
    Outline = 6
    NaturalSymmetricDownsampled = 7
class CanvasTextRenderingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderingParameters
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderingParametersFactory, textRenderingMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode, gridFit: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextGridFit) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters: ...
    @winrt_mixinmethod
    def get_RenderingMode(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderingParameters) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode: ...
    @winrt_mixinmethod
    def get_GridFit(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderingParameters) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextGridFit: ...
    GridFit = property(get_GridFit, None)
    RenderingMode = property(get_RenderingMode, None)
class CanvasTextTrimmingGranularity(Enum, Int32):
    None_ = 0
    Character = 1
    Word = 2
class CanvasTrimmingSign(Enum, Int32):
    None_ = 0
    Ellipsis = 1
class CanvasTypography(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTypography
    _classid_ = 'Microsoft.Graphics.Canvas.Text.CanvasTypography'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography: ...
    @winrt_mixinmethod
    def AddFeature(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTypography, feature: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeature) -> Void: ...
    @winrt_mixinmethod
    def AddFeatureWithNameAndParameter(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTypography, name: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName, parameter: UInt32) -> Void: ...
    @winrt_mixinmethod
    def GetFeatures(self: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTypography) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeature]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class CanvasTypographyFeature(Structure):
    Name: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName
    Parameter: UInt32
class CanvasTypographyFeatureName(Enum, Int32):
    None_ = 0
    Default = 1953261156
    VerticalWriting = 1953654134
    VerticalAlternatesAndRotation = 846492278
    AlternativeFractions = 1668441697
    PetiteCapitalsFromCapitals = 1668297315
    SmallCapitalsFromCapitals = 1668493923
    ContextualAlternates = 1953259875
    CaseSensitiveForms = 1702060387
    GlyphCompositionDecomposition = 1886217059
    ContextualLigatures = 1734962275
    CapitalSpacing = 1886613603
    ContextualSwash = 1752658787
    CursivePositioning = 1936880995
    DiscretionaryLigatures = 1734962276
    ExpertForms = 1953527909
    Fractions = 1667330662
    FullWidth = 1684633446
    HalfForms = 1718378856
    HalantForms = 1852596584
    AlternateHalfWidth = 1953259880
    HistoricalForms = 1953720680
    HorizontalKanaAlternates = 1634626408
    HistoricalLigatures = 1734962280
    HalfWidth = 1684633448
    HojoKanjiForms = 1869246312
    Jis04Forms = 875589738
    Jis78Forms = 943157354
    Jis83Forms = 859336810
    Jis90Forms = 809070698
    Kerning = 1852990827
    StandardLigatures = 1634167148
    LiningFigures = 1836412524
    LocalizedForms = 1818455916
    MarkPositioning = 1802658157
    MathematicalGreek = 1802659693
    MarkToMarkPositioning = 1802333037
    AlternateAnnotationForms = 1953259886
    NlcKanjiForms = 1801677934
    OldStyleFigures = 1836412527
    Ordinals = 1852076655
    ProportionalAlternateWidth = 1953259888
    PetiteCapitals = 1885430640
    ProportionalFigures = 1836412528
    ProportionalWidths = 1684633456
    QuarterWidths = 1684633457
    RequiredLigatures = 1734962290
    RubyNotationForms = 2036495730
    StylisticAlternates = 1953259891
    ScientificInferiors = 1718511987
    SmallCapitals = 1885564275
    SimplifiedForms = 1819307379
    StylisticSet1 = 825258867
    StylisticSet2 = 842036083
    StylisticSet3 = 858813299
    StylisticSet4 = 875590515
    StylisticSet5 = 892367731
    StylisticSet6 = 909144947
    StylisticSet7 = 925922163
    StylisticSet8 = 942699379
    StylisticSet9 = 959476595
    StylisticSet10 = 808547187
    StylisticSet11 = 825324403
    StylisticSet12 = 842101619
    StylisticSet13 = 858878835
    StylisticSet14 = 875656051
    StylisticSet15 = 892433267
    StylisticSet16 = 909210483
    StylisticSet17 = 925987699
    StylisticSet18 = 942764915
    StylisticSet19 = 959542131
    StylisticSet20 = 808612723
    Subscript = 1935832435
    Superscript = 1936749939
    Swash = 1752397683
    Titling = 1819568500
    TraditionalNameForms = 1835101812
    TabularFigures = 1836412532
    TraditionalForms = 1684107892
    ThirdWidths = 1684633460
    Unicase = 1667853941
    SlashedZero = 1869768058
class CanvasUnicodeRange(Structure):
    First: UInt32
    Last: UInt32
class CanvasVerticalAlignment(Enum, Int32):
    Top = 0
    Bottom = 1
    Center = 2
class CanvasVerticalGlyphOrientation(Enum, Int32):
    Default = 0
    Stacked = 1
class CanvasWordWrapping(Enum, Int32):
    Wrap = 0
    NoWrap = 1
    EmergencyBreak = 2
    WholeWord = 3
    Character = 4
class ICanvasFontFace(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasFontFace'
    _iid_ = Guid('{5199d129-4ef9-4dee-b74c-4dc910201a7f}')
    @winrt_commethod(6)
    def GetRecommendedRenderingMode(self, fontSize: Single, dpi: Single, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, renderingParameters: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode: ...
    @winrt_commethod(7)
    def GetRecommendedRenderingModeWithAllOptions(self, fontSize: Single, dpi: Single, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, renderingParameters: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters, transform: win32more.Windows.Foundation.Numerics.Matrix3x2, isSideways: Boolean, outlineThreshold: win32more.Microsoft.Graphics.Canvas.CanvasAntialiasing) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode: ...
    @winrt_commethod(8)
    def GetRecommendedGridFit(self, fontSize: Single, dpi: Single, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, renderingParameters: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters, transform: win32more.Windows.Foundation.Numerics.Matrix3x2, isSideways: Boolean, outlineThreshold: win32more.Microsoft.Graphics.Canvas.CanvasAntialiasing) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextGridFit: ...
    @winrt_commethod(9)
    def get_GlyphBox(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def get_SubscriptPosition(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def get_SubscriptSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(12)
    def get_SuperscriptPosition(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(13)
    def get_SuperscriptSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(14)
    def get_HasTypographicMetrics(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_Ascent(self) -> Single: ...
    @winrt_commethod(16)
    def get_Descent(self) -> Single: ...
    @winrt_commethod(17)
    def get_LineGap(self) -> Single: ...
    @winrt_commethod(18)
    def get_CapHeight(self) -> Single: ...
    @winrt_commethod(19)
    def get_LowercaseLetterHeight(self) -> Single: ...
    @winrt_commethod(20)
    def get_UnderlinePosition(self) -> Single: ...
    @winrt_commethod(21)
    def get_UnderlineThickness(self) -> Single: ...
    @winrt_commethod(22)
    def get_StrikethroughPosition(self) -> Single: ...
    @winrt_commethod(23)
    def get_StrikethroughThickness(self) -> Single: ...
    @winrt_commethod(24)
    def get_CaretSlopeRise(self) -> Single: ...
    @winrt_commethod(25)
    def get_CaretSlopeRun(self) -> Single: ...
    @winrt_commethod(26)
    def get_CaretOffset(self) -> Single: ...
    @winrt_commethod(27)
    def get_UnicodeRanges(self) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasUnicodeRange]: ...
    @winrt_commethod(28)
    def get_IsMonospaced(self) -> Boolean: ...
    @winrt_commethod(29)
    def GetVerticalGlyphVariants(self, inputElements: PassArray[Int32]) -> ReceiveArray[Int32]: ...
    @winrt_commethod(30)
    def get_HasVerticalGlyphVariants(self) -> Boolean: ...
    @winrt_commethod(31)
    def get_FileFormatType(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFileFormatType: ...
    @winrt_commethod(32)
    def get_Simulations(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSimulations: ...
    @winrt_commethod(33)
    def get_IsSymbolFont(self) -> Boolean: ...
    @winrt_commethod(34)
    def get_GlyphCount(self) -> UInt32: ...
    @winrt_commethod(35)
    def GetGlyphIndices(self, inputElements: PassArray[UInt32]) -> ReceiveArray[Int32]: ...
    @winrt_commethod(36)
    def GetGlyphMetrics(self, inputElements: PassArray[Int32], isSideways: Boolean) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphMetrics]: ...
    @winrt_commethod(37)
    def GetGdiCompatibleGlyphMetrics(self, fontSize: Single, dpi: Single, transform: win32more.Windows.Foundation.Numerics.Matrix3x2, useGdiNatural: Boolean, inputElements: PassArray[Int32], isSideways: Boolean) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphMetrics]: ...
    @winrt_commethod(38)
    def get_Weight(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(39)
    def get_Stretch(self) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_commethod(40)
    def get_Style(self) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_commethod(41)
    def get_FamilyNames(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(42)
    def get_FaceNames(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(43)
    def GetInformationalStrings(self, fontInformation: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontInformation) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(44)
    def HasCharacter(self, unicodeValue: UInt32) -> Boolean: ...
    @winrt_commethod(45)
    def GetGlyphRunBounds(self, drawingSession: win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession, point: win32more.Windows.Foundation.Numerics.Vector2, fontSize: Single, glyphs: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], isSideways: Boolean, bidiLevel: UInt32) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(46)
    def GetGlyphRunBoundsWithMeasuringMode(self, drawingSession: win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession, point: win32more.Windows.Foundation.Numerics.Vector2, fontSize: Single, glyphs: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], isSideways: Boolean, bidiLevel: UInt32, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(47)
    def get_Panose(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(48)
    def GetSupportedTypographicFeatureNames(self, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName]: ...
    @winrt_commethod(49)
    def GetSupportedTypographicFeatureNamesWithLocale(self, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, locale: WinRT_String) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName]: ...
    @winrt_commethod(50)
    def GetTypographicFeatureGlyphSupport(self, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, typographicFeatureName: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName, glyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]) -> ReceiveArray[Boolean]: ...
    @winrt_commethod(51)
    def GetTypographicFeatureGlyphSupportWithLocale(self, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, typographicFeatureName: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName, glyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], locale: WinRT_String) -> ReceiveArray[Boolean]: ...
    Ascent = property(get_Ascent, None)
    CapHeight = property(get_CapHeight, None)
    CaretOffset = property(get_CaretOffset, None)
    CaretSlopeRise = property(get_CaretSlopeRise, None)
    CaretSlopeRun = property(get_CaretSlopeRun, None)
    Descent = property(get_Descent, None)
    FaceNames = property(get_FaceNames, None)
    FamilyNames = property(get_FamilyNames, None)
    FileFormatType = property(get_FileFormatType, None)
    GlyphBox = property(get_GlyphBox, None)
    GlyphCount = property(get_GlyphCount, None)
    HasTypographicMetrics = property(get_HasTypographicMetrics, None)
    HasVerticalGlyphVariants = property(get_HasVerticalGlyphVariants, None)
    IsMonospaced = property(get_IsMonospaced, None)
    IsSymbolFont = property(get_IsSymbolFont, None)
    LineGap = property(get_LineGap, None)
    LowercaseLetterHeight = property(get_LowercaseLetterHeight, None)
    Panose = property(get_Panose, None)
    Simulations = property(get_Simulations, None)
    Stretch = property(get_Stretch, None)
    StrikethroughPosition = property(get_StrikethroughPosition, None)
    StrikethroughThickness = property(get_StrikethroughThickness, None)
    Style = property(get_Style, None)
    SubscriptPosition = property(get_SubscriptPosition, None)
    SubscriptSize = property(get_SubscriptSize, None)
    SuperscriptPosition = property(get_SuperscriptPosition, None)
    SuperscriptSize = property(get_SuperscriptSize, None)
    UnderlinePosition = property(get_UnderlinePosition, None)
    UnderlineThickness = property(get_UnderlineThickness, None)
    UnicodeRanges = property(get_UnicodeRanges, None)
    Weight = property(get_Weight, None)
class ICanvasFontSet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasFontSet'
    _iid_ = Guid('{0a5bfb92-1f3c-459f-9d7e-a6289dd093c0}')
    @winrt_commethod(6)
    def get_Fonts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace]: ...
    @winrt_commethod(7)
    def TryFindFontFace(self, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, index: POINTER(Int32)) -> Boolean: ...
    @winrt_commethod(8)
    def GetMatchingFontsFromProperties(self, propertyElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty]) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
    @winrt_commethod(9)
    def GetMatchingFontsFromWwsFamily(self, familyName: WinRT_String, weight: win32more.Windows.UI.Text.FontWeight, stretch: win32more.Windows.UI.Text.FontStretch, style: win32more.Windows.UI.Text.FontStyle) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
    @winrt_commethod(10)
    def CountFontsMatchingProperty(self, property: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty) -> UInt32: ...
    @winrt_commethod(11)
    def GetPropertyValuesFromIndex(self, fontIndex: UInt32, propertyIdentifier: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontPropertyIdentifier) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(12)
    def GetPropertyValuesFromIdentifier(self, propertyIdentifier: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontPropertyIdentifier, preferredLocaleNames: WinRT_String) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty]: ...
    @winrt_commethod(13)
    def GetPropertyValues(self, propertyIdentifier: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontPropertyIdentifier) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasFontProperty]: ...
    Fonts = property(get_Fonts, None)
class ICanvasFontSetFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasFontSetFactory'
    _iid_ = Guid('{3c9c9bda-70f9-4ff9-aab2-3b42923286ee}')
    @winrt_commethod(6)
    def Create(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
class ICanvasFontSetStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasFontSetStatics'
    _iid_ = Guid('{5f4275ce-bcfa-48c5-9e67-fbe9866d4924}')
    @winrt_commethod(6)
    def GetSystemFontSet(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet: ...
class ICanvasNumberSubstitution(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasNumberSubstitution'
    _iid_ = Guid('{c81a67ad-0639-4f8f-878b-d937f8a14293}')
class ICanvasNumberSubstitutionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasNumberSubstitutionFactory'
    _iid_ = Guid('{7496a822-c781-4eb0-aafb-c078e7fa8e24}')
    @winrt_commethod(6)
    def Create(self, method: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitutionMethod) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution: ...
    @winrt_commethod(7)
    def CreateWithLocaleAndIgnoreOverrides(self, method: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitutionMethod, localeName: WinRT_String, ignoreEnvironmentOverrides: Boolean) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution: ...
class ICanvasScaledFont(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasScaledFont'
    _iid_ = Guid('{bbc4f8d2-eb2b-45f1-ac2a-cfc1f598bae3}')
    @winrt_commethod(6)
    def get_FontFace(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace: ...
    @winrt_commethod(7)
    def get_ScaleFactor(self) -> Single: ...
    FontFace = property(get_FontFace, None)
    ScaleFactor = property(get_ScaleFactor, None)
class ICanvasTextAnalyzer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzer'
    _iid_ = Guid('{4298f3d1-645b-40e3-b91b-81986d767fc0}')
    @winrt_commethod(6)
    def GetFontsUsingSystemFontSet(self, textFormat: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasScaledFont]]: ...
    @winrt_commethod(7)
    def GetFonts(self, textFormat: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat, fontSet: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontSet) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasScaledFont]]: ...
    @winrt_commethod(8)
    def GetBidi(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBidi]]: ...
    @winrt_commethod(9)
    def GetBidiWithLocale(self, locale: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBidi]]: ...
    @winrt_commethod(10)
    def GetBreakpoints(self) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBreakpoint]: ...
    @winrt_commethod(11)
    def GetBreakpointsWithLocale(self, locale: WinRT_String) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedBreakpoint]: ...
    @winrt_commethod(12)
    def GetNumberSubstitutions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution]]: ...
    @winrt_commethod(13)
    def GetScript(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript]]: ...
    @winrt_commethod(14)
    def GetScriptWithLocale(self, locale: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript]]: ...
    @winrt_commethod(15)
    def GetGlyphOrientations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedGlyphOrientation]]: ...
    @winrt_commethod(16)
    def GetGlyphOrientationsWithLocale(self, locale: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedGlyphOrientation]]: ...
    @winrt_commethod(17)
    def GetScriptProperties(self, analyzedScript: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasScriptProperties: ...
    @winrt_commethod(18)
    def GetGlyphs(self, characterRange: win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, isSideways: Boolean, isRightToLeft: Boolean, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_commethod(19)
    def GetGlyphsWithAllOptions(self, characterRange: win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, isSideways: Boolean, isRightToLeft: Boolean, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, locale: WinRT_String, numberSubstitution: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution, typographyRanges: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IKeyValuePair[win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography]], clusterMapIndicesElements: ReceiveArray[Int32], isShapedAloneGlyphsElements: ReceiveArray[Boolean], glyphShapingResultsElements: ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_commethod(20)
    def GetJustificationOpportunities(self, characterRange: win32more.Microsoft.Graphics.Canvas.Text.CanvasCharacterRange, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, clusterMapIndicesElements: PassArray[Int32], glyphShapingResultsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasJustificationOpportunity]: ...
    @winrt_commethod(21)
    def ApplyJustificationOpportunities(self, lineWidth: Single, justificationOpportunitiesElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasJustificationOpportunity], sourceGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_commethod(22)
    def AddGlyphsAfterJustification(self, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, clusterMapIndicesElements: PassArray[Int32], originalGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], justifiedGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], glyphShapingResultsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
    @winrt_commethod(23)
    def AddGlyphsAfterJustificationWithClusterMap(self, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, script: win32more.Microsoft.Graphics.Canvas.Text.CanvasAnalyzedScript, clusterMapIndicesElements: PassArray[Int32], originalGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], justifiedGlyphsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], glyphShapingResultsElements: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphShaping], outputClusterMapIndicesElements: ReceiveArray[Int32]) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph]: ...
class ICanvasTextAnalyzerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzerFactory'
    _iid_ = Guid('{521e433f-f698-44c0-8d7f-fe374fe539e1}')
    @winrt_commethod(6)
    def Create(self, text: WinRT_String, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer: ...
    @winrt_commethod(7)
    def CreateWithNumberSubstitutionAndVerticalGlyphOrientationAndBidiLevel(self, text: WinRT_String, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection, numberSubstitution: win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution, verticalGlyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation, bidiLevel: UInt32) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer: ...
    @winrt_commethod(8)
    def CreateWithOptions(self, text: WinRT_String, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection, options: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzerOptions) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextAnalyzer: ...
class ICanvasTextAnalyzerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextAnalyzerOptions'
    _iid_ = Guid('{31f2406a-8c5f-4e12-8bd6-cfbbc7214d02}')
    @winrt_commethod(6)
    def GetLocaleName(self, characterIndex: Int32, characterCount: POINTER(Int32)) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetNumberSubstitution(self, characterIndex: Int32, characterCount: POINTER(Int32)) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasNumberSubstitution: ...
    @winrt_commethod(8)
    def GetVerticalGlyphOrientation(self, characterIndex: Int32, characterCount: POINTER(Int32)) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation: ...
    @winrt_commethod(9)
    def GetBidiLevel(self, characterIndex: Int32, characterCount: POINTER(Int32)) -> UInt32: ...
class ICanvasTextFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextFormat'
    _iid_ = Guid('{af61bfdc-eabb-4d38-ba1b-afb340612d33}')
    @winrt_commethod(6)
    def get_Direction(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection: ...
    @winrt_commethod(7)
    def put_Direction(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection) -> Void: ...
    @winrt_commethod(8)
    def get_FontFamily(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_FontFamily(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_FontSize(self) -> Single: ...
    @winrt_commethod(11)
    def put_FontSize(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_FontStretch(self) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_commethod(13)
    def put_FontStretch(self, value: win32more.Windows.UI.Text.FontStretch) -> Void: ...
    @winrt_commethod(14)
    def get_FontStyle(self) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_commethod(15)
    def put_FontStyle(self, value: win32more.Windows.UI.Text.FontStyle) -> Void: ...
    @winrt_commethod(16)
    def get_FontWeight(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(17)
    def put_FontWeight(self, value: win32more.Windows.UI.Text.FontWeight) -> Void: ...
    @winrt_commethod(18)
    def get_IncrementalTabStop(self) -> Single: ...
    @winrt_commethod(19)
    def put_IncrementalTabStop(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_LineSpacing(self) -> Single: ...
    @winrt_commethod(21)
    def put_LineSpacing(self, value: Single) -> Void: ...
    @winrt_commethod(22)
    def get_LineSpacingBaseline(self) -> Single: ...
    @winrt_commethod(23)
    def put_LineSpacingBaseline(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_LocaleName(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def put_LocaleName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(26)
    def get_VerticalAlignment(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment: ...
    @winrt_commethod(27)
    def put_VerticalAlignment(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment) -> Void: ...
    @winrt_commethod(28)
    def get_HorizontalAlignment(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment: ...
    @winrt_commethod(29)
    def put_HorizontalAlignment(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment) -> Void: ...
    @winrt_commethod(30)
    def get_TrimmingGranularity(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity: ...
    @winrt_commethod(31)
    def put_TrimmingGranularity(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity) -> Void: ...
    @winrt_commethod(32)
    def get_TrimmingDelimiter(self) -> WinRT_String: ...
    @winrt_commethod(33)
    def put_TrimmingDelimiter(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(34)
    def get_TrimmingDelimiterCount(self) -> Int32: ...
    @winrt_commethod(35)
    def put_TrimmingDelimiterCount(self, value: Int32) -> Void: ...
    @winrt_commethod(36)
    def get_WordWrapping(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping: ...
    @winrt_commethod(37)
    def put_WordWrapping(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping) -> Void: ...
    @winrt_commethod(38)
    def get_Options(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions: ...
    @winrt_commethod(39)
    def put_Options(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions) -> Void: ...
    @winrt_commethod(40)
    def get_VerticalGlyphOrientation(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation: ...
    @winrt_commethod(41)
    def put_VerticalGlyphOrientation(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation) -> Void: ...
    @winrt_commethod(42)
    def get_OpticalAlignment(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment: ...
    @winrt_commethod(43)
    def put_OpticalAlignment(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment) -> Void: ...
    @winrt_commethod(44)
    def get_LastLineWrapping(self) -> Boolean: ...
    @winrt_commethod(45)
    def put_LastLineWrapping(self, value: Boolean) -> Void: ...
    @winrt_commethod(46)
    def get_LineSpacingMode(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode: ...
    @winrt_commethod(47)
    def put_LineSpacingMode(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode) -> Void: ...
    @winrt_commethod(48)
    def get_TrimmingSign(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign: ...
    @winrt_commethod(49)
    def put_TrimmingSign(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign) -> Void: ...
    @winrt_commethod(50)
    def get_CustomTrimmingSign(self) -> win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject: ...
    @winrt_commethod(51)
    def put_CustomTrimmingSign(self, value: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject) -> Void: ...
    CustomTrimmingSign = property(get_CustomTrimmingSign, put_CustomTrimmingSign)
    Direction = property(get_Direction, put_Direction)
    FontFamily = property(get_FontFamily, put_FontFamily)
    FontSize = property(get_FontSize, put_FontSize)
    FontStretch = property(get_FontStretch, put_FontStretch)
    FontStyle = property(get_FontStyle, put_FontStyle)
    FontWeight = property(get_FontWeight, put_FontWeight)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    IncrementalTabStop = property(get_IncrementalTabStop, put_IncrementalTabStop)
    LastLineWrapping = property(get_LastLineWrapping, put_LastLineWrapping)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineSpacingBaseline = property(get_LineSpacingBaseline, put_LineSpacingBaseline)
    LineSpacingMode = property(get_LineSpacingMode, put_LineSpacingMode)
    LocaleName = property(get_LocaleName, put_LocaleName)
    OpticalAlignment = property(get_OpticalAlignment, put_OpticalAlignment)
    Options = property(get_Options, put_Options)
    TrimmingDelimiter = property(get_TrimmingDelimiter, put_TrimmingDelimiter)
    TrimmingDelimiterCount = property(get_TrimmingDelimiterCount, put_TrimmingDelimiterCount)
    TrimmingGranularity = property(get_TrimmingGranularity, put_TrimmingGranularity)
    TrimmingSign = property(get_TrimmingSign, put_TrimmingSign)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    VerticalGlyphOrientation = property(get_VerticalGlyphOrientation, put_VerticalGlyphOrientation)
    WordWrapping = property(get_WordWrapping, put_WordWrapping)
class ICanvasTextFormatStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextFormatStatics'
    _iid_ = Guid('{8a927515-33fc-4c92-a6aa-94a8f29c140b}')
    @winrt_commethod(6)
    def GetSystemFontFamilies(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(7)
    def GetSystemFontFamiliesFromLocaleList(self, localeList: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> ReceiveArray[WinRT_String]: ...
class ICanvasTextInlineObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject'
    _iid_ = Guid('{7a89ee99-ce2a-47fa-9dd2-0a6825f6053f}')
    @winrt_commethod(6)
    def Draw(self, textRenderer: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderer, point: win32more.Windows.Foundation.Numerics.Vector2, isSideways: Boolean, isRightToLeft: Boolean, brush: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_Baseline(self) -> Single: ...
    @winrt_commethod(9)
    def get_SupportsSideways(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_DrawBounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def get_BreakBefore(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasLineBreakCondition: ...
    @winrt_commethod(12)
    def get_BreakAfter(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasLineBreakCondition: ...
    Baseline = property(get_Baseline, None)
    BreakAfter = property(get_BreakAfter, None)
    BreakBefore = property(get_BreakBefore, None)
    DrawBounds = property(get_DrawBounds, None)
    Size = property(get_Size, None)
    SupportsSideways = property(get_SupportsSideways, None)
class ICanvasTextLayout(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextLayout'
    _iid_ = Guid('{bae63e54-48ae-4446-a2c7-b6ef93806c20}')
    @winrt_commethod(6)
    def GetFormatChangeIndices(self) -> ReceiveArray[Int32]: ...
    @winrt_commethod(7)
    def get_Direction(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection: ...
    @winrt_commethod(8)
    def put_Direction(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection) -> Void: ...
    @winrt_commethod(9)
    def get_DefaultFontFamily(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DefaultFontSize(self) -> Single: ...
    @winrt_commethod(11)
    def get_DefaultFontStretch(self) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_commethod(12)
    def get_DefaultFontStyle(self) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_commethod(13)
    def get_DefaultFontWeight(self) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(14)
    def get_IncrementalTabStop(self) -> Single: ...
    @winrt_commethod(15)
    def put_IncrementalTabStop(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_LineSpacing(self) -> Single: ...
    @winrt_commethod(17)
    def put_LineSpacing(self, value: Single) -> Void: ...
    @winrt_commethod(18)
    def get_LineSpacingBaseline(self) -> Single: ...
    @winrt_commethod(19)
    def put_LineSpacingBaseline(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_DefaultLocaleName(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_VerticalAlignment(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment: ...
    @winrt_commethod(22)
    def put_VerticalAlignment(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalAlignment) -> Void: ...
    @winrt_commethod(23)
    def get_HorizontalAlignment(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment: ...
    @winrt_commethod(24)
    def put_HorizontalAlignment(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasHorizontalAlignment) -> Void: ...
    @winrt_commethod(25)
    def get_TrimmingGranularity(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity: ...
    @winrt_commethod(26)
    def put_TrimmingGranularity(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextTrimmingGranularity) -> Void: ...
    @winrt_commethod(27)
    def get_TrimmingDelimiter(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def put_TrimmingDelimiter(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(29)
    def get_TrimmingDelimiterCount(self) -> Int32: ...
    @winrt_commethod(30)
    def put_TrimmingDelimiterCount(self, value: Int32) -> Void: ...
    @winrt_commethod(31)
    def get_WordWrapping(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping: ...
    @winrt_commethod(32)
    def put_WordWrapping(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasWordWrapping) -> Void: ...
    @winrt_commethod(33)
    def get_Options(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions: ...
    @winrt_commethod(34)
    def put_Options(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasDrawTextOptions) -> Void: ...
    @winrt_commethod(35)
    def get_LineSpacingMode(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode: ...
    @winrt_commethod(36)
    def put_LineSpacingMode(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasLineSpacingMode) -> Void: ...
    @winrt_commethod(37)
    def get_TrimmingSign(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign: ...
    @winrt_commethod(38)
    def put_TrimmingSign(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasTrimmingSign) -> Void: ...
    @winrt_commethod(39)
    def get_CustomTrimmingSign(self) -> win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject: ...
    @winrt_commethod(40)
    def put_CustomTrimmingSign(self, value: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject) -> Void: ...
    @winrt_commethod(41)
    def get_RequestedSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(42)
    def put_RequestedSize(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(43)
    def GetMinimumLineLength(self) -> Single: ...
    @winrt_commethod(44)
    def GetBrush(self, characterIndex: Int32) -> win32more.Microsoft.Graphics.Canvas.Brushes.ICanvasBrush: ...
    @winrt_commethod(45)
    def GetCustomBrush(self, characterIndex: Int32) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(46)
    def GetFontFamily(self, characterIndex: Int32) -> WinRT_String: ...
    @winrt_commethod(47)
    def GetFontSize(self, characterIndex: Int32) -> Single: ...
    @winrt_commethod(48)
    def GetFontStretch(self, characterIndex: Int32) -> win32more.Windows.UI.Text.FontStretch: ...
    @winrt_commethod(49)
    def GetFontStyle(self, characterIndex: Int32) -> win32more.Windows.UI.Text.FontStyle: ...
    @winrt_commethod(50)
    def GetFontWeight(self, characterIndex: Int32) -> win32more.Windows.UI.Text.FontWeight: ...
    @winrt_commethod(51)
    def GetLocaleName(self, characterIndex: Int32) -> WinRT_String: ...
    @winrt_commethod(52)
    def GetStrikethrough(self, characterIndex: Int32) -> Boolean: ...
    @winrt_commethod(53)
    def GetUnderline(self, characterIndex: Int32) -> Boolean: ...
    @winrt_commethod(54)
    def GetInlineObject(self, characterIndex: Int32) -> win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject: ...
    @winrt_commethod(55)
    def SetColor(self, characterIndex: Int32, characterCount: Int32, color: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(56)
    def SetBrush(self, characterIndex: Int32, characterCount: Int32, brush: win32more.Microsoft.Graphics.Canvas.Brushes.ICanvasBrush) -> Void: ...
    @winrt_commethod(57)
    def SetCustomBrush(self, characterIndex: Int32, characterCount: Int32, brush: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(58)
    def SetFontFamily(self, characterIndex: Int32, characterCount: Int32, fontFamily: WinRT_String) -> Void: ...
    @winrt_commethod(59)
    def SetFontSize(self, characterIndex: Int32, characterCount: Int32, fontSize: Single) -> Void: ...
    @winrt_commethod(60)
    def SetFontStretch(self, characterIndex: Int32, characterCount: Int32, fontStretch: win32more.Windows.UI.Text.FontStretch) -> Void: ...
    @winrt_commethod(61)
    def SetFontStyle(self, characterIndex: Int32, characterCount: Int32, fontStyle: win32more.Windows.UI.Text.FontStyle) -> Void: ...
    @winrt_commethod(62)
    def SetFontWeight(self, characterIndex: Int32, characterCount: Int32, fontWeight: win32more.Windows.UI.Text.FontWeight) -> Void: ...
    @winrt_commethod(63)
    def SetLocaleName(self, characterIndex: Int32, characterCount: Int32, name: WinRT_String) -> Void: ...
    @winrt_commethod(64)
    def SetStrikethrough(self, characterIndex: Int32, characterCount: Int32, hasStrikethrough: Boolean) -> Void: ...
    @winrt_commethod(65)
    def SetUnderline(self, characterIndex: Int32, characterCount: Int32, hasUnderline: Boolean) -> Void: ...
    @winrt_commethod(66)
    def SetInlineObject(self, characterIndex: Int32, characterCount: Int32, inlineObject: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject) -> Void: ...
    @winrt_commethod(67)
    def DrawToTextRenderer(self, textRenderer: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderer, position: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(68)
    def DrawToTextRendererWithCoords(self, textRenderer: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextRenderer, x: Single, y: Single) -> Void: ...
    @winrt_commethod(69)
    def get_LineMetrics(self) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasLineMetrics]: ...
    @winrt_commethod(70)
    def get_ClusterMetrics(self) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasClusterMetrics]: ...
    @winrt_commethod(71)
    def SetTypography(self, characterIndex: Int32, characterCount: Int32, typography: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography) -> Void: ...
    @winrt_commethod(72)
    def GetTypography(self, characterIndex: Int32) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTypography: ...
    @winrt_commethod(73)
    def get_LayoutBounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(74)
    def get_LayoutBoundsIncludingTrailingWhitespace(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(75)
    def get_LineCount(self) -> Int32: ...
    @winrt_commethod(76)
    def get_MaximumBidiReorderingDepth(self) -> Int32: ...
    @winrt_commethod(77)
    def get_DrawBounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(78)
    def HitTest(self, point: win32more.Windows.Foundation.Numerics.Vector2) -> Boolean: ...
    @winrt_commethod(79)
    def HitTestWithCoords(self, x: Single, y: Single) -> Boolean: ...
    @winrt_commethod(80)
    def HitTestWithDescription(self, point: win32more.Windows.Foundation.Numerics.Vector2, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion)) -> Boolean: ...
    @winrt_commethod(81)
    def HitTestWithDescriptionAndCoords(self, x: Single, y: Single, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion)) -> Boolean: ...
    @winrt_commethod(82)
    def HitTestWithDescriptionAndTrailingSide(self, point: win32more.Windows.Foundation.Numerics.Vector2, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion), trailingSideOfCharacter: POINTER(Boolean)) -> Boolean: ...
    @winrt_commethod(83)
    def HitTestWithDescriptionAndCoordsAndTrailingSide(self, x: Single, y: Single, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion), trailingSideOfCharacter: POINTER(Boolean)) -> Boolean: ...
    @winrt_commethod(84)
    def GetCaretPosition(self, characterIndex: Int32, trailingSideOfCharacter: Boolean) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(85)
    def GetCaretPositionWithDescription(self, characterIndex: Int32, trailingSideOfCharacter: Boolean, textLayoutRegion: POINTER(win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion)) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(86)
    def GetCharacterRegions(self, characterIndex: Int32, characterCount: Int32) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayoutRegion]: ...
    @winrt_commethod(87)
    def GetPairKerning(self, characterIndex: Int32) -> Boolean: ...
    @winrt_commethod(88)
    def SetPairKerning(self, characterIndex: Int32, characterCount: Int32, hasPairKerning: Boolean) -> Void: ...
    @winrt_commethod(89)
    def GetLeadingCharacterSpacing(self, characterIndex: Int32) -> Single: ...
    @winrt_commethod(90)
    def GetTrailingCharacterSpacing(self, characterIndex: Int32) -> Single: ...
    @winrt_commethod(91)
    def GetMinimumCharacterAdvance(self, characterIndex: Int32) -> Single: ...
    @winrt_commethod(92)
    def SetCharacterSpacing(self, characterIndex: Int32, characterCount: Int32, leadingSpacing: Single, trailingSpacing: Single, minimumAdvance: Single) -> Void: ...
    @winrt_commethod(93)
    def get_VerticalGlyphOrientation(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation: ...
    @winrt_commethod(94)
    def put_VerticalGlyphOrientation(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasVerticalGlyphOrientation) -> Void: ...
    @winrt_commethod(95)
    def get_OpticalAlignment(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment: ...
    @winrt_commethod(96)
    def put_OpticalAlignment(self, value: win32more.Microsoft.Graphics.Canvas.Text.CanvasOpticalAlignment) -> Void: ...
    @winrt_commethod(97)
    def get_LastLineWrapping(self) -> Boolean: ...
    @winrt_commethod(98)
    def put_LastLineWrapping(self, value: Boolean) -> Void: ...
    @winrt_commethod(99)
    def get_Device(self) -> win32more.Microsoft.Graphics.Canvas.CanvasDevice: ...
    ClusterMetrics = property(get_ClusterMetrics, None)
    CustomTrimmingSign = property(get_CustomTrimmingSign, put_CustomTrimmingSign)
    DefaultFontFamily = property(get_DefaultFontFamily, None)
    DefaultFontSize = property(get_DefaultFontSize, None)
    DefaultFontStretch = property(get_DefaultFontStretch, None)
    DefaultFontStyle = property(get_DefaultFontStyle, None)
    DefaultFontWeight = property(get_DefaultFontWeight, None)
    DefaultLocaleName = property(get_DefaultLocaleName, None)
    Device = property(get_Device, None)
    Direction = property(get_Direction, put_Direction)
    DrawBounds = property(get_DrawBounds, None)
    HorizontalAlignment = property(get_HorizontalAlignment, put_HorizontalAlignment)
    IncrementalTabStop = property(get_IncrementalTabStop, put_IncrementalTabStop)
    LastLineWrapping = property(get_LastLineWrapping, put_LastLineWrapping)
    LayoutBounds = property(get_LayoutBounds, None)
    LayoutBoundsIncludingTrailingWhitespace = property(get_LayoutBoundsIncludingTrailingWhitespace, None)
    LineCount = property(get_LineCount, None)
    LineMetrics = property(get_LineMetrics, None)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineSpacingBaseline = property(get_LineSpacingBaseline, put_LineSpacingBaseline)
    LineSpacingMode = property(get_LineSpacingMode, put_LineSpacingMode)
    MaximumBidiReorderingDepth = property(get_MaximumBidiReorderingDepth, None)
    OpticalAlignment = property(get_OpticalAlignment, put_OpticalAlignment)
    Options = property(get_Options, put_Options)
    RequestedSize = property(get_RequestedSize, put_RequestedSize)
    TrimmingDelimiter = property(get_TrimmingDelimiter, put_TrimmingDelimiter)
    TrimmingDelimiterCount = property(get_TrimmingDelimiterCount, put_TrimmingDelimiterCount)
    TrimmingGranularity = property(get_TrimmingGranularity, put_TrimmingGranularity)
    TrimmingSign = property(get_TrimmingSign, put_TrimmingSign)
    VerticalAlignment = property(get_VerticalAlignment, put_VerticalAlignment)
    VerticalGlyphOrientation = property(get_VerticalGlyphOrientation, put_VerticalGlyphOrientation)
    WordWrapping = property(get_WordWrapping, put_WordWrapping)
class ICanvasTextLayoutFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextLayoutFactory'
    _iid_ = Guid('{9c1f7179-acd0-4680-93d5-95a6247e8f6b}')
    @winrt_commethod(6)
    def Create(self, resourceCreator: win32more.Microsoft.Graphics.Canvas.ICanvasResourceCreator, textString: WinRT_String, textFormat: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextFormat, requestedWidth: Single, requestedHeight: Single) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextLayout: ...
class ICanvasTextLayoutStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextLayoutStatics'
    _iid_ = Guid('{7f2b8ffd-6935-4f60-b409-6394a19c5ebc}')
    @winrt_commethod(6)
    def GetGlyphOrientationTransform(self, glyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphOrientation, isSideways: Boolean, position: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
class ICanvasTextRenderer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextRenderer'
    _iid_ = Guid('{9aaeece5-8d09-4a64-b322-af030421b2e4}')
    @winrt_commethod(6)
    def DrawGlyphRun(self, point: win32more.Windows.Foundation.Numerics.Vector2, fontFace: win32more.Microsoft.Graphics.Canvas.Text.CanvasFontFace, fontSize: Single, glyphs: PassArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyph], isSideways: Boolean, bidiLevel: UInt32, brush: win32more.Windows.Win32.System.WinRT.IInspectable, measuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, localeName: WinRT_String, textString: WinRT_String, clusterMapIndices: PassArray[Int32], characterIndex: UInt32, glyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphOrientation) -> Void: ...
    @winrt_commethod(7)
    def DrawStrikethrough(self, point: win32more.Windows.Foundation.Numerics.Vector2, strikethroughWidth: Single, strikethroughThickness: Single, strikethroughOffset: Single, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection, brush: win32more.Windows.Win32.System.WinRT.IInspectable, textMeasuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, localeName: WinRT_String, glyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphOrientation) -> Void: ...
    @winrt_commethod(8)
    def DrawUnderline(self, point: win32more.Windows.Foundation.Numerics.Vector2, underlineWidth: Single, underlineThickness: Single, underlineOffset: Single, runHeight: Single, textDirection: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextDirection, brush: win32more.Windows.Win32.System.WinRT.IInspectable, textMeasuringMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextMeasuringMode, localeName: WinRT_String, glyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphOrientation) -> Void: ...
    @winrt_commethod(9)
    def DrawInlineObject(self, point: win32more.Windows.Foundation.Numerics.Vector2, inlineObject: win32more.Microsoft.Graphics.Canvas.Text.ICanvasTextInlineObject, isSideways: Boolean, isRightToLeft: Boolean, brush: win32more.Windows.Win32.System.WinRT.IInspectable, glyphOrientation: win32more.Microsoft.Graphics.Canvas.Text.CanvasGlyphOrientation) -> Void: ...
    @winrt_commethod(10)
    def get_PixelSnappingDisabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_Transform(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(12)
    def get_Dpi(self) -> Single: ...
    Dpi = property(get_Dpi, None)
    PixelSnappingDisabled = property(get_PixelSnappingDisabled, None)
    Transform = property(get_Transform, None)
class ICanvasTextRenderingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextRenderingParameters'
    _iid_ = Guid('{b20bf738-edb9-4eec-a12f-b6ae32e8ace6}')
    @winrt_commethod(6)
    def get_RenderingMode(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode: ...
    @winrt_commethod(7)
    def get_GridFit(self) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextGridFit: ...
    GridFit = property(get_GridFit, None)
    RenderingMode = property(get_RenderingMode, None)
class ICanvasTextRenderingParametersFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTextRenderingParametersFactory'
    _iid_ = Guid('{d240ac25-4d23-4964-9d9a-db2fc8af185d}')
    @winrt_commethod(6)
    def Create(self, textRenderingMode: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingMode, gridFit: win32more.Microsoft.Graphics.Canvas.Text.CanvasTextGridFit) -> win32more.Microsoft.Graphics.Canvas.Text.CanvasTextRenderingParameters: ...
class ICanvasTypography(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Text.ICanvasTypography'
    _iid_ = Guid('{f15bc312-447f-44ed-8bec-7e40f4a4dfc8}')
    @winrt_commethod(6)
    def AddFeature(self, feature: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeature) -> Void: ...
    @winrt_commethod(7)
    def AddFeatureWithNameAndParameter(self, name: win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeatureName, parameter: UInt32) -> Void: ...
    @winrt_commethod(8)
    def GetFeatures(self) -> ReceiveArray[win32more.Microsoft.Graphics.Canvas.Text.CanvasTypographyFeature]: ...


make_ready(__name__)
