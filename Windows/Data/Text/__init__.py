from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Data.Text
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.UI.Text.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AlternateNormalizationFormat = Int32
AlternateNormalizationFormat_NotNormalized: AlternateNormalizationFormat = 0
AlternateNormalizationFormat_Number: AlternateNormalizationFormat = 1
AlternateNormalizationFormat_Currency: AlternateNormalizationFormat = 3
AlternateNormalizationFormat_Date: AlternateNormalizationFormat = 4
AlternateNormalizationFormat_Time: AlternateNormalizationFormat = 5
class AlternateWordForm(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.AlternateWordForm'
    @winrt_mixinmethod
    def get_SourceTextSegment(self: Windows.Data.Text.IAlternateWordForm) -> Windows.Data.Text.TextSegment: ...
    @winrt_mixinmethod
    def get_AlternateText(self: Windows.Data.Text.IAlternateWordForm) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NormalizationFormat(self: Windows.Data.Text.IAlternateWordForm) -> Windows.Data.Text.AlternateNormalizationFormat: ...
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateText = property(get_AlternateText, None)
    NormalizationFormat = property(get_NormalizationFormat, None)
class IAlternateWordForm(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('47396c1e-51b9-4207-91-46-24-8e-63-6a-1d-1d')
    @winrt_commethod(6)
    def get_SourceTextSegment(self) -> Windows.Data.Text.TextSegment: ...
    @winrt_commethod(7)
    def get_AlternateText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NormalizationFormat(self) -> Windows.Data.Text.AlternateNormalizationFormat: ...
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateText = property(get_AlternateText, None)
    NormalizationFormat = property(get_NormalizationFormat, None)
class ISelectableWordSegment(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('916a4cb7-8aa7-4c78-b3-74-5d-ed-b7-52-e6-0b')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SourceTextSegment(self) -> Windows.Data.Text.TextSegment: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
class ISelectableWordsSegmenter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f6dc31e7-4b13-45c5-88-97-7d-71-26-9e-08-5d')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetTokenAt(self, text: WinRT_String, startIndex: UInt32) -> Windows.Data.Text.SelectableWordSegment: ...
    @winrt_commethod(8)
    def GetTokens(self, text: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.SelectableWordSegment]: ...
    @winrt_commethod(9)
    def Tokenize(self, text: WinRT_String, startIndex: UInt32, handler: Windows.Data.Text.SelectableWordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class ISelectableWordsSegmenterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8c7a7648-6057-4339-bc-70-f2-10-01-0a-41-50')
    @winrt_commethod(6)
    def CreateWithLanguage(self, language: WinRT_String) -> Windows.Data.Text.SelectableWordsSegmenter: ...
class ISemanticTextQuery(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6a1cab51-1fb2-4909-80-b8-35-73-1a-2b-3e-7f')
    @winrt_commethod(6)
    def Find(self, content: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
    @winrt_commethod(7)
    def FindInProperty(self, propertyContent: WinRT_String, propertyName: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
class ISemanticTextQueryFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('238c0503-f995-4587-87-77-a2-b7-d8-0a-cf-ef')
    @winrt_commethod(6)
    def Create(self, aqsFilter: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
    @winrt_commethod(7)
    def CreateWithLanguage(self, aqsFilter: WinRT_String, filterLanguage: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
class ITextConversionGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('03606a5e-2aa9-4ab6-af-8b-a5-62-b6-3a-89-92')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LanguageAvailableButNotInstalled(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetCandidatesAsync(self, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(9)
    def GetCandidatesWithMaxCountAsync(self, input: WinRT_String, maxCandidates: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
class ITextConversionGeneratorFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fcaa3781-3083-49ab-be-15-56-df-bb-b7-4d-6f')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> Windows.Data.Text.TextConversionGenerator: ...
class ITextPhoneme(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9362a40a-9b7a-4569-94-cf-d8-4f-2f-38-cf-9b')
    @winrt_commethod(6)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ReadingText(self) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, None)
    ReadingText = property(get_ReadingText, None)
class ITextPredictionGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5eacab07-abf1-4cb6-9d-9e-32-6f-2b-46-87-56')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LanguageAvailableButNotInstalled(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetCandidatesAsync(self, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(9)
    def GetCandidatesWithMaxCountAsync(self, input: WinRT_String, maxCandidates: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
class ITextPredictionGenerator2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b84723b8-2c77-486a-90-0a-a3-45-3e-ed-c1-5d')
    @winrt_commethod(6)
    def GetCandidatesWithParametersAsync(self, input: WinRT_String, maxCandidates: UInt32, predictionOptions: Windows.Data.Text.TextPredictionOptions, previousStrings: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(7)
    def GetNextWordCandidatesAsync(self, maxCandidates: UInt32, previousStrings: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(8)
    def get_InputScope(self) -> Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_commethod(9)
    def put_InputScope(self, value: Windows.UI.Text.Core.CoreTextInputScope) -> Void: ...
    InputScope = property(get_InputScope, put_InputScope)
class ITextPredictionGeneratorFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7257b416-8ba2-4751-9d-30-9d-85-43-56-53-a2')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> Windows.Data.Text.TextPredictionGenerator: ...
class ITextReverseConversionGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('51e7f514-9c51-4d86-ae-1b-b4-98-fb-ad-83-13')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LanguageAvailableButNotInstalled(self) -> Boolean: ...
    @winrt_commethod(8)
    def ConvertBackAsync(self, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
class ITextReverseConversionGenerator2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1aafd2ec-85d6-46fd-82-8a-3a-48-30-fa-6e-18')
    @winrt_commethod(6)
    def GetPhonemesAsync(self, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextPhoneme]]: ...
class ITextReverseConversionGeneratorFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63bed326-1fda-41f6-89-d5-23-dd-ea-3c-72-9a')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> Windows.Data.Text.TextReverseConversionGenerator: ...
class IUnicodeCharactersStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('97909e87-9291-4f91-b6-c8-b6-e3-59-d7-a7-fb')
    @winrt_commethod(6)
    def GetCodepointFromSurrogatePair(self, highSurrogate: UInt32, lowSurrogate: UInt32) -> UInt32: ...
    @winrt_commethod(7)
    def GetSurrogatePairFromCodepoint(self, codepoint: UInt32, highSurrogate: c_wchar_p_no, lowSurrogate: c_wchar_p_no) -> Void: ...
    @winrt_commethod(8)
    def IsHighSurrogate(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(9)
    def IsLowSurrogate(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(10)
    def IsSupplementary(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(11)
    def IsNoncharacter(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(12)
    def IsWhitespace(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(13)
    def IsAlphabetic(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(14)
    def IsCased(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(15)
    def IsUppercase(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(16)
    def IsLowercase(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(17)
    def IsIdStart(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(18)
    def IsIdContinue(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(19)
    def IsGraphemeBase(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(20)
    def IsGraphemeExtend(self, codepoint: UInt32) -> Boolean: ...
    @winrt_commethod(21)
    def GetNumericType(self, codepoint: UInt32) -> Windows.Data.Text.UnicodeNumericType: ...
    @winrt_commethod(22)
    def GetGeneralCategory(self, codepoint: UInt32) -> Windows.Data.Text.UnicodeGeneralCategory: ...
class IWordSegment(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d2d4ba6d-987c-4cc0-b6-bd-d4-9a-11-b3-8f-9a')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SourceTextSegment(self) -> Windows.Data.Text.TextSegment: ...
    @winrt_commethod(8)
    def get_AlternateForms(self) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.AlternateWordForm]: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateForms = property(get_AlternateForms, None)
class IWordsSegmenter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('86b4d4d1-b2fe-4e34-a8-1d-66-64-03-00-45-4f')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetTokenAt(self, text: WinRT_String, startIndex: UInt32) -> Windows.Data.Text.WordSegment: ...
    @winrt_commethod(8)
    def GetTokens(self, text: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.WordSegment]: ...
    @winrt_commethod(9)
    def Tokenize(self, text: WinRT_String, startIndex: UInt32, handler: Windows.Data.Text.WordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class IWordsSegmenterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e6977274-fc35-455c-8b-fb-6d-7f-46-53-ca-97')
    @winrt_commethod(6)
    def CreateWithLanguage(self, language: WinRT_String) -> Windows.Data.Text.WordsSegmenter: ...
class SelectableWordSegment(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.SelectableWordSegment'
    @winrt_mixinmethod
    def get_Text(self: Windows.Data.Text.ISelectableWordSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceTextSegment(self: Windows.Data.Text.ISelectableWordSegment) -> Windows.Data.Text.TextSegment: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
class SelectableWordSegmentsTokenizingHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3a3dfc9c-aede-4dc7-9e-6c-41-c0-44-bd-35-92')
    ClassId = 'Windows.Data.Text.SelectableWordSegmentsTokenizingHandler'
    @winrt_commethod(3)
    def Invoke(self, precedingWords: Windows.Foundation.Collections.IIterable[Windows.Data.Text.SelectableWordSegment], words: Windows.Foundation.Collections.IIterable[Windows.Data.Text.SelectableWordSegment]) -> Void: ...
class SelectableWordsSegmenter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.SelectableWordsSegmenter'
    @winrt_factorymethod
    def CreateWithLanguage(cls: Windows.Data.Text.ISelectableWordsSegmenterFactory, language: WinRT_String) -> Windows.Data.Text.SelectableWordsSegmenter: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: Windows.Data.Text.ISelectableWordsSegmenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetTokenAt(self: Windows.Data.Text.ISelectableWordsSegmenter, text: WinRT_String, startIndex: UInt32) -> Windows.Data.Text.SelectableWordSegment: ...
    @winrt_mixinmethod
    def GetTokens(self: Windows.Data.Text.ISelectableWordsSegmenter, text: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.SelectableWordSegment]: ...
    @winrt_mixinmethod
    def Tokenize(self: Windows.Data.Text.ISelectableWordsSegmenter, text: WinRT_String, startIndex: UInt32, handler: Windows.Data.Text.SelectableWordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class SemanticTextQuery(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.SemanticTextQuery'
    @winrt_factorymethod
    def Create(cls: Windows.Data.Text.ISemanticTextQueryFactory, aqsFilter: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
    @winrt_factorymethod
    def CreateWithLanguage(cls: Windows.Data.Text.ISemanticTextQueryFactory, aqsFilter: WinRT_String, filterLanguage: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
    @winrt_mixinmethod
    def Find(self: Windows.Data.Text.ISemanticTextQuery, content: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
    @winrt_mixinmethod
    def FindInProperty(self: Windows.Data.Text.ISemanticTextQuery, propertyContent: WinRT_String, propertyName: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
class TextConversionGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.TextConversionGenerator'
    @winrt_factorymethod
    def Create(cls: Windows.Data.Text.ITextConversionGeneratorFactory, languageTag: WinRT_String) -> Windows.Data.Text.TextConversionGenerator: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: Windows.Data.Text.ITextConversionGenerator) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LanguageAvailableButNotInstalled(self: Windows.Data.Text.ITextConversionGenerator) -> Boolean: ...
    @winrt_mixinmethod
    def GetCandidatesAsync(self: Windows.Data.Text.ITextConversionGenerator, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetCandidatesWithMaxCountAsync(self: Windows.Data.Text.ITextConversionGenerator, input: WinRT_String, maxCandidates: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
class TextPhoneme(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.TextPhoneme'
    @winrt_mixinmethod
    def get_DisplayText(self: Windows.Data.Text.ITextPhoneme) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReadingText(self: Windows.Data.Text.ITextPhoneme) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, None)
    ReadingText = property(get_ReadingText, None)
class TextPredictionGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.TextPredictionGenerator'
    @winrt_factorymethod
    def Create(cls: Windows.Data.Text.ITextPredictionGeneratorFactory, languageTag: WinRT_String) -> Windows.Data.Text.TextPredictionGenerator: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: Windows.Data.Text.ITextPredictionGenerator) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LanguageAvailableButNotInstalled(self: Windows.Data.Text.ITextPredictionGenerator) -> Boolean: ...
    @winrt_mixinmethod
    def GetCandidatesAsync(self: Windows.Data.Text.ITextPredictionGenerator, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetCandidatesWithMaxCountAsync(self: Windows.Data.Text.ITextPredictionGenerator, input: WinRT_String, maxCandidates: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetCandidatesWithParametersAsync(self: Windows.Data.Text.ITextPredictionGenerator2, input: WinRT_String, maxCandidates: UInt32, predictionOptions: Windows.Data.Text.TextPredictionOptions, previousStrings: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetNextWordCandidatesAsync(self: Windows.Data.Text.ITextPredictionGenerator2, maxCandidates: UInt32, previousStrings: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def get_InputScope(self: Windows.Data.Text.ITextPredictionGenerator2) -> Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_mixinmethod
    def put_InputScope(self: Windows.Data.Text.ITextPredictionGenerator2, value: Windows.UI.Text.Core.CoreTextInputScope) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
    InputScope = property(get_InputScope, put_InputScope)
TextPredictionOptions = UInt32
TextPredictionOptions_None: TextPredictionOptions = 0
TextPredictionOptions_Predictions: TextPredictionOptions = 1
TextPredictionOptions_Corrections: TextPredictionOptions = 2
class TextReverseConversionGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.TextReverseConversionGenerator'
    @winrt_factorymethod
    def Create(cls: Windows.Data.Text.ITextReverseConversionGeneratorFactory, languageTag: WinRT_String) -> Windows.Data.Text.TextReverseConversionGenerator: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: Windows.Data.Text.ITextReverseConversionGenerator) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LanguageAvailableButNotInstalled(self: Windows.Data.Text.ITextReverseConversionGenerator) -> Boolean: ...
    @winrt_mixinmethod
    def ConvertBackAsync(self: Windows.Data.Text.ITextReverseConversionGenerator, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetPhonemesAsync(self: Windows.Data.Text.ITextReverseConversionGenerator2, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextPhoneme]]: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
class TextSegment(EasyCastStructure):
    StartPosition: UInt32
    Length: UInt32
class UnicodeCharacters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.UnicodeCharacters'
    @winrt_classmethod
    def GetCodepointFromSurrogatePair(cls: Windows.Data.Text.IUnicodeCharactersStatics, highSurrogate: UInt32, lowSurrogate: UInt32) -> UInt32: ...
    @winrt_classmethod
    def GetSurrogatePairFromCodepoint(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32, highSurrogate: c_wchar_p_no, lowSurrogate: c_wchar_p_no) -> Void: ...
    @winrt_classmethod
    def IsHighSurrogate(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsLowSurrogate(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsSupplementary(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsNoncharacter(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsWhitespace(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsAlphabetic(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsCased(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsUppercase(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsLowercase(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsIdStart(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsIdContinue(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsGraphemeBase(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsGraphemeExtend(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def GetNumericType(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Windows.Data.Text.UnicodeNumericType: ...
    @winrt_classmethod
    def GetGeneralCategory(cls: Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Windows.Data.Text.UnicodeGeneralCategory: ...
UnicodeGeneralCategory = Int32
UnicodeGeneralCategory_UppercaseLetter: UnicodeGeneralCategory = 0
UnicodeGeneralCategory_LowercaseLetter: UnicodeGeneralCategory = 1
UnicodeGeneralCategory_TitlecaseLetter: UnicodeGeneralCategory = 2
UnicodeGeneralCategory_ModifierLetter: UnicodeGeneralCategory = 3
UnicodeGeneralCategory_OtherLetter: UnicodeGeneralCategory = 4
UnicodeGeneralCategory_NonspacingMark: UnicodeGeneralCategory = 5
UnicodeGeneralCategory_SpacingCombiningMark: UnicodeGeneralCategory = 6
UnicodeGeneralCategory_EnclosingMark: UnicodeGeneralCategory = 7
UnicodeGeneralCategory_DecimalDigitNumber: UnicodeGeneralCategory = 8
UnicodeGeneralCategory_LetterNumber: UnicodeGeneralCategory = 9
UnicodeGeneralCategory_OtherNumber: UnicodeGeneralCategory = 10
UnicodeGeneralCategory_SpaceSeparator: UnicodeGeneralCategory = 11
UnicodeGeneralCategory_LineSeparator: UnicodeGeneralCategory = 12
UnicodeGeneralCategory_ParagraphSeparator: UnicodeGeneralCategory = 13
UnicodeGeneralCategory_Control: UnicodeGeneralCategory = 14
UnicodeGeneralCategory_Format: UnicodeGeneralCategory = 15
UnicodeGeneralCategory_Surrogate: UnicodeGeneralCategory = 16
UnicodeGeneralCategory_PrivateUse: UnicodeGeneralCategory = 17
UnicodeGeneralCategory_ConnectorPunctuation: UnicodeGeneralCategory = 18
UnicodeGeneralCategory_DashPunctuation: UnicodeGeneralCategory = 19
UnicodeGeneralCategory_OpenPunctuation: UnicodeGeneralCategory = 20
UnicodeGeneralCategory_ClosePunctuation: UnicodeGeneralCategory = 21
UnicodeGeneralCategory_InitialQuotePunctuation: UnicodeGeneralCategory = 22
UnicodeGeneralCategory_FinalQuotePunctuation: UnicodeGeneralCategory = 23
UnicodeGeneralCategory_OtherPunctuation: UnicodeGeneralCategory = 24
UnicodeGeneralCategory_MathSymbol: UnicodeGeneralCategory = 25
UnicodeGeneralCategory_CurrencySymbol: UnicodeGeneralCategory = 26
UnicodeGeneralCategory_ModifierSymbol: UnicodeGeneralCategory = 27
UnicodeGeneralCategory_OtherSymbol: UnicodeGeneralCategory = 28
UnicodeGeneralCategory_NotAssigned: UnicodeGeneralCategory = 29
UnicodeNumericType = Int32
UnicodeNumericType_None: UnicodeNumericType = 0
UnicodeNumericType_Decimal: UnicodeNumericType = 1
UnicodeNumericType_Digit: UnicodeNumericType = 2
UnicodeNumericType_Numeric: UnicodeNumericType = 3
class WordSegment(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.WordSegment'
    @winrt_mixinmethod
    def get_Text(self: Windows.Data.Text.IWordSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceTextSegment(self: Windows.Data.Text.IWordSegment) -> Windows.Data.Text.TextSegment: ...
    @winrt_mixinmethod
    def get_AlternateForms(self: Windows.Data.Text.IWordSegment) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.AlternateWordForm]: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateForms = property(get_AlternateForms, None)
class WordSegmentsTokenizingHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a5dd6357-bf2a-4c4f-a3-1f-29-e7-1c-6f-8b-35')
    ClassId = 'Windows.Data.Text.WordSegmentsTokenizingHandler'
    @winrt_commethod(3)
    def Invoke(self, precedingWords: Windows.Foundation.Collections.IIterable[Windows.Data.Text.WordSegment], words: Windows.Foundation.Collections.IIterable[Windows.Data.Text.WordSegment]) -> Void: ...
class WordsSegmenter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Text.WordsSegmenter'
    @winrt_factorymethod
    def CreateWithLanguage(cls: Windows.Data.Text.IWordsSegmenterFactory, language: WinRT_String) -> Windows.Data.Text.WordsSegmenter: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: Windows.Data.Text.IWordsSegmenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetTokenAt(self: Windows.Data.Text.IWordsSegmenter, text: WinRT_String, startIndex: UInt32) -> Windows.Data.Text.WordSegment: ...
    @winrt_mixinmethod
    def GetTokens(self: Windows.Data.Text.IWordsSegmenter, text: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.WordSegment]: ...
    @winrt_mixinmethod
    def Tokenize(self: Windows.Data.Text.IWordsSegmenter, text: WinRT_String, startIndex: UInt32, handler: Windows.Data.Text.WordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
make_head(_module, 'AlternateWordForm')
make_head(_module, 'IAlternateWordForm')
make_head(_module, 'ISelectableWordSegment')
make_head(_module, 'ISelectableWordsSegmenter')
make_head(_module, 'ISelectableWordsSegmenterFactory')
make_head(_module, 'ISemanticTextQuery')
make_head(_module, 'ISemanticTextQueryFactory')
make_head(_module, 'ITextConversionGenerator')
make_head(_module, 'ITextConversionGeneratorFactory')
make_head(_module, 'ITextPhoneme')
make_head(_module, 'ITextPredictionGenerator')
make_head(_module, 'ITextPredictionGenerator2')
make_head(_module, 'ITextPredictionGeneratorFactory')
make_head(_module, 'ITextReverseConversionGenerator')
make_head(_module, 'ITextReverseConversionGenerator2')
make_head(_module, 'ITextReverseConversionGeneratorFactory')
make_head(_module, 'IUnicodeCharactersStatics')
make_head(_module, 'IWordSegment')
make_head(_module, 'IWordsSegmenter')
make_head(_module, 'IWordsSegmenterFactory')
make_head(_module, 'SelectableWordSegment')
make_head(_module, 'SelectableWordSegmentsTokenizingHandler')
make_head(_module, 'SelectableWordsSegmenter')
make_head(_module, 'SemanticTextQuery')
make_head(_module, 'TextConversionGenerator')
make_head(_module, 'TextPhoneme')
make_head(_module, 'TextPredictionGenerator')
make_head(_module, 'TextReverseConversionGenerator')
make_head(_module, 'TextSegment')
make_head(_module, 'UnicodeCharacters')
make_head(_module, 'WordSegment')
make_head(_module, 'WordSegmentsTokenizingHandler')
make_head(_module, 'WordsSegmenter')
