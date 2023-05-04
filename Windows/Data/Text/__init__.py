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
class AlternateWordForm(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.IAlternateWordForm
    _classid_ = 'Windows.Data.Text.AlternateWordForm'
    @winrt_mixinmethod
    def get_SourceTextSegment(self: Windows.Data.Text.IAlternateWordForm) -> Windows.Data.Text.TextSegment: ...
    @winrt_mixinmethod
    def get_AlternateText(self: Windows.Data.Text.IAlternateWordForm) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NormalizationFormat(self: Windows.Data.Text.IAlternateWordForm) -> Windows.Data.Text.AlternateNormalizationFormat: ...
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateText = property(get_AlternateText, None)
    NormalizationFormat = property(get_NormalizationFormat, None)
class IAlternateWordForm(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{47396c1e-51b9-4207-9146-248e636a1d1d}')
    @winrt_commethod(6)
    def get_SourceTextSegment(self) -> Windows.Data.Text.TextSegment: ...
    @winrt_commethod(7)
    def get_AlternateText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NormalizationFormat(self) -> Windows.Data.Text.AlternateNormalizationFormat: ...
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateText = property(get_AlternateText, None)
    NormalizationFormat = property(get_NormalizationFormat, None)
class ISelectableWordSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{916a4cb7-8aa7-4c78-b374-5dedb752e60b}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SourceTextSegment(self) -> Windows.Data.Text.TextSegment: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
class ISelectableWordsSegmenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f6dc31e7-4b13-45c5-8897-7d71269e085d}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetTokenAt(self, text: WinRT_String, startIndex: UInt32) -> Windows.Data.Text.SelectableWordSegment: ...
    @winrt_commethod(8)
    def GetTokens(self, text: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.SelectableWordSegment]: ...
    @winrt_commethod(9)
    def Tokenize(self, text: WinRT_String, startIndex: UInt32, handler: Windows.Data.Text.SelectableWordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class ISelectableWordsSegmenterFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8c7a7648-6057-4339-bc70-f210010a4150}')
    @winrt_commethod(6)
    def CreateWithLanguage(self, language: WinRT_String) -> Windows.Data.Text.SelectableWordsSegmenter: ...
class ISemanticTextQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6a1cab51-1fb2-4909-80b8-35731a2b3e7f}')
    @winrt_commethod(6)
    def Find(self, content: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
    @winrt_commethod(7)
    def FindInProperty(self, propertyContent: WinRT_String, propertyName: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
class ISemanticTextQueryFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{238c0503-f995-4587-8777-a2b7d80acfef}')
    @winrt_commethod(6)
    def Create(self, aqsFilter: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
    @winrt_commethod(7)
    def CreateWithLanguage(self, aqsFilter: WinRT_String, filterLanguage: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
class ITextConversionGenerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{03606a5e-2aa9-4ab6-af8b-a562b63a8992}')
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
class ITextConversionGeneratorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fcaa3781-3083-49ab-be15-56dfbbb74d6f}')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> Windows.Data.Text.TextConversionGenerator: ...
class ITextPhoneme(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9362a40a-9b7a-4569-94cf-d84f2f38cf9b}')
    @winrt_commethod(6)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ReadingText(self) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, None)
    ReadingText = property(get_ReadingText, None)
class ITextPredictionGenerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5eacab07-abf1-4cb6-9d9e-326f2b468756}')
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
class ITextPredictionGenerator2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b84723b8-2c77-486a-900a-a3453eedc15d}')
    @winrt_commethod(6)
    def GetCandidatesWithParametersAsync(self, input: WinRT_String, maxCandidates: UInt32, predictionOptions: Windows.Data.Text.TextPredictionOptions, previousStrings: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(7)
    def GetNextWordCandidatesAsync(self, maxCandidates: UInt32, previousStrings: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(8)
    def get_InputScope(self) -> Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_commethod(9)
    def put_InputScope(self, value: Windows.UI.Text.Core.CoreTextInputScope) -> Void: ...
    InputScope = property(get_InputScope, put_InputScope)
class ITextPredictionGeneratorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7257b416-8ba2-4751-9d30-9d85435653a2}')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> Windows.Data.Text.TextPredictionGenerator: ...
class ITextReverseConversionGenerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{51e7f514-9c51-4d86-ae1b-b498fbad8313}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LanguageAvailableButNotInstalled(self) -> Boolean: ...
    @winrt_commethod(8)
    def ConvertBackAsync(self, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
class ITextReverseConversionGenerator2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1aafd2ec-85d6-46fd-828a-3a4830fa6e18}')
    @winrt_commethod(6)
    def GetPhonemesAsync(self, input: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextPhoneme]]: ...
class ITextReverseConversionGeneratorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{63bed326-1fda-41f6-89d5-23ddea3c729a}')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> Windows.Data.Text.TextReverseConversionGenerator: ...
class IUnicodeCharactersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{97909e87-9291-4f91-b6c8-b6e359d7a7fb}')
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
class IWordSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d2d4ba6d-987c-4cc0-b6bd-d49a11b38f9a}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SourceTextSegment(self) -> Windows.Data.Text.TextSegment: ...
    @winrt_commethod(8)
    def get_AlternateForms(self) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.AlternateWordForm]: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateForms = property(get_AlternateForms, None)
class IWordsSegmenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{86b4d4d1-b2fe-4e34-a81d-66640300454f}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetTokenAt(self, text: WinRT_String, startIndex: UInt32) -> Windows.Data.Text.WordSegment: ...
    @winrt_commethod(8)
    def GetTokens(self, text: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.WordSegment]: ...
    @winrt_commethod(9)
    def Tokenize(self, text: WinRT_String, startIndex: UInt32, handler: Windows.Data.Text.WordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class IWordsSegmenterFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e6977274-fc35-455c-8bfb-6d7f4653ca97}')
    @winrt_commethod(6)
    def CreateWithLanguage(self, language: WinRT_String) -> Windows.Data.Text.WordsSegmenter: ...
class SelectableWordSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.ISelectableWordSegment
    _classid_ = 'Windows.Data.Text.SelectableWordSegment'
    @winrt_mixinmethod
    def get_Text(self: Windows.Data.Text.ISelectableWordSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceTextSegment(self: Windows.Data.Text.ISelectableWordSegment) -> Windows.Data.Text.TextSegment: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
class SelectableWordSegmentsTokenizingHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a3dfc9c-aede-4dc7-9e6c-41c044bd3592}')
    _classid_ = 'Windows.Data.Text.SelectableWordSegmentsTokenizingHandler'
    @winrt_commethod(3)
    def Invoke(self, precedingWords: Windows.Foundation.Collections.IIterable[Windows.Data.Text.SelectableWordSegment], words: Windows.Foundation.Collections.IIterable[Windows.Data.Text.SelectableWordSegment]) -> Void: ...
class SelectableWordsSegmenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.ISelectableWordsSegmenter
    _classid_ = 'Windows.Data.Text.SelectableWordsSegmenter'
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
class SemanticTextQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.ISemanticTextQuery
    _classid_ = 'Windows.Data.Text.SemanticTextQuery'
    @winrt_factorymethod
    def Create(cls: Windows.Data.Text.ISemanticTextQueryFactory, aqsFilter: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
    @winrt_factorymethod
    def CreateWithLanguage(cls: Windows.Data.Text.ISemanticTextQueryFactory, aqsFilter: WinRT_String, filterLanguage: WinRT_String) -> Windows.Data.Text.SemanticTextQuery: ...
    @winrt_mixinmethod
    def Find(self: Windows.Data.Text.ISemanticTextQuery, content: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
    @winrt_mixinmethod
    def FindInProperty(self: Windows.Data.Text.ISemanticTextQuery, propertyContent: WinRT_String, propertyName: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]: ...
class TextConversionGenerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.ITextConversionGenerator
    _classid_ = 'Windows.Data.Text.TextConversionGenerator'
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
class TextPhoneme(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.ITextPhoneme
    _classid_ = 'Windows.Data.Text.TextPhoneme'
    @winrt_mixinmethod
    def get_DisplayText(self: Windows.Data.Text.ITextPhoneme) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReadingText(self: Windows.Data.Text.ITextPhoneme) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, None)
    ReadingText = property(get_ReadingText, None)
class TextPredictionGenerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.ITextPredictionGenerator
    _classid_ = 'Windows.Data.Text.TextPredictionGenerator'
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
class TextReverseConversionGenerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.ITextReverseConversionGenerator
    _classid_ = 'Windows.Data.Text.TextReverseConversionGenerator'
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
class UnicodeCharacters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
class WordSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.IWordSegment
    _classid_ = 'Windows.Data.Text.WordSegment'
    @winrt_mixinmethod
    def get_Text(self: Windows.Data.Text.IWordSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceTextSegment(self: Windows.Data.Text.IWordSegment) -> Windows.Data.Text.TextSegment: ...
    @winrt_mixinmethod
    def get_AlternateForms(self: Windows.Data.Text.IWordSegment) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Text.AlternateWordForm]: ...
    Text = property(get_Text, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
    AlternateForms = property(get_AlternateForms, None)
class WordSegmentsTokenizingHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5dd6357-bf2a-4c4f-a31f-29e71c6f8b35}')
    _classid_ = 'Windows.Data.Text.WordSegmentsTokenizingHandler'
    @winrt_commethod(3)
    def Invoke(self, precedingWords: Windows.Foundation.Collections.IIterable[Windows.Data.Text.WordSegment], words: Windows.Foundation.Collections.IIterable[Windows.Data.Text.WordSegment]) -> Void: ...
class WordsSegmenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Text.IWordsSegmenter
    _classid_ = 'Windows.Data.Text.WordsSegmenter'
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
