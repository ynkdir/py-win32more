from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Data.Text
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Text.Core
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AlternateNormalizationFormat(Enum, Int32):
    NotNormalized = 0
    Number = 1
    Currency = 3
    Date = 4
    Time = 5
class AlternateWordForm(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.IAlternateWordForm
    _classid_ = 'Windows.Data.Text.AlternateWordForm'
    @winrt_mixinmethod
    def get_SourceTextSegment(self: win32more.Windows.Data.Text.IAlternateWordForm) -> win32more.Windows.Data.Text.TextSegment: ...
    @winrt_mixinmethod
    def get_AlternateText(self: win32more.Windows.Data.Text.IAlternateWordForm) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NormalizationFormat(self: win32more.Windows.Data.Text.IAlternateWordForm) -> win32more.Windows.Data.Text.AlternateNormalizationFormat: ...
    AlternateText = property(get_AlternateText, None)
    NormalizationFormat = property(get_NormalizationFormat, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
class IAlternateWordForm(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.IAlternateWordForm'
    _iid_ = Guid('{47396c1e-51b9-4207-9146-248e636a1d1d}')
    @winrt_commethod(6)
    def get_SourceTextSegment(self) -> win32more.Windows.Data.Text.TextSegment: ...
    @winrt_commethod(7)
    def get_AlternateText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NormalizationFormat(self) -> win32more.Windows.Data.Text.AlternateNormalizationFormat: ...
    AlternateText = property(get_AlternateText, None)
    NormalizationFormat = property(get_NormalizationFormat, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
class ISelectableWordSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ISelectableWordSegment'
    _iid_ = Guid('{916a4cb7-8aa7-4c78-b374-5dedb752e60b}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SourceTextSegment(self) -> win32more.Windows.Data.Text.TextSegment: ...
    SourceTextSegment = property(get_SourceTextSegment, None)
    Text = property(get_Text, None)
class ISelectableWordsSegmenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ISelectableWordsSegmenter'
    _iid_ = Guid('{f6dc31e7-4b13-45c5-8897-7d71269e085d}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetTokenAt(self, text: WinRT_String, startIndex: UInt32) -> win32more.Windows.Data.Text.SelectableWordSegment: ...
    @winrt_commethod(8)
    def GetTokens(self, text: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.SelectableWordSegment]: ...
    @winrt_commethod(9)
    def Tokenize(self, text: WinRT_String, startIndex: UInt32, handler: win32more.Windows.Data.Text.SelectableWordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class ISelectableWordsSegmenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ISelectableWordsSegmenterFactory'
    _iid_ = Guid('{8c7a7648-6057-4339-bc70-f210010a4150}')
    @winrt_commethod(6)
    def CreateWithLanguage(self, language: WinRT_String) -> win32more.Windows.Data.Text.SelectableWordsSegmenter: ...
class ISemanticTextQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ISemanticTextQuery'
    _iid_ = Guid('{6a1cab51-1fb2-4909-80b8-35731a2b3e7f}')
    @winrt_commethod(6)
    def Find(self, content: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]: ...
    @winrt_commethod(7)
    def FindInProperty(self, propertyContent: WinRT_String, propertyName: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]: ...
class ISemanticTextQueryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ISemanticTextQueryFactory'
    _iid_ = Guid('{238c0503-f995-4587-8777-a2b7d80acfef}')
    @winrt_commethod(6)
    def Create(self, aqsFilter: WinRT_String) -> win32more.Windows.Data.Text.SemanticTextQuery: ...
    @winrt_commethod(7)
    def CreateWithLanguage(self, aqsFilter: WinRT_String, filterLanguage: WinRT_String) -> win32more.Windows.Data.Text.SemanticTextQuery: ...
class ITextConversionGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextConversionGenerator'
    _iid_ = Guid('{03606a5e-2aa9-4ab6-af8b-a562b63a8992}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LanguageAvailableButNotInstalled(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetCandidatesAsync(self, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(9)
    def GetCandidatesWithMaxCountAsync(self, input: WinRT_String, maxCandidates: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class ITextConversionGeneratorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextConversionGeneratorFactory'
    _iid_ = Guid('{fcaa3781-3083-49ab-be15-56dfbbb74d6f}')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> win32more.Windows.Data.Text.TextConversionGenerator: ...
class ITextPhoneme(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextPhoneme'
    _iid_ = Guid('{9362a40a-9b7a-4569-94cf-d84f2f38cf9b}')
    @winrt_commethod(6)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ReadingText(self) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, None)
    ReadingText = property(get_ReadingText, None)
class ITextPredictionGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextPredictionGenerator'
    _iid_ = Guid('{5eacab07-abf1-4cb6-9d9e-326f2b468756}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LanguageAvailableButNotInstalled(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetCandidatesAsync(self, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(9)
    def GetCandidatesWithMaxCountAsync(self, input: WinRT_String, maxCandidates: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class ITextPredictionGenerator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextPredictionGenerator2'
    _iid_ = Guid('{b84723b8-2c77-486a-900a-a3453eedc15d}')
    @winrt_commethod(6)
    def GetCandidatesWithParametersAsync(self, input: WinRT_String, maxCandidates: UInt32, predictionOptions: win32more.Windows.Data.Text.TextPredictionOptions, previousStrings: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(7)
    def GetNextWordCandidatesAsync(self, maxCandidates: UInt32, previousStrings: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(8)
    def get_InputScope(self) -> win32more.Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_commethod(9)
    def put_InputScope(self, value: win32more.Windows.UI.Text.Core.CoreTextInputScope) -> Void: ...
    InputScope = property(get_InputScope, put_InputScope)
class ITextPredictionGeneratorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextPredictionGeneratorFactory'
    _iid_ = Guid('{7257b416-8ba2-4751-9d30-9d85435653a2}')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> win32more.Windows.Data.Text.TextPredictionGenerator: ...
class ITextReverseConversionGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextReverseConversionGenerator'
    _iid_ = Guid('{51e7f514-9c51-4d86-ae1b-b498fbad8313}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LanguageAvailableButNotInstalled(self) -> Boolean: ...
    @winrt_commethod(8)
    def ConvertBackAsync(self, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class ITextReverseConversionGenerator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextReverseConversionGenerator2'
    _iid_ = Guid('{1aafd2ec-85d6-46fd-828a-3a4830fa6e18}')
    @winrt_commethod(6)
    def GetPhonemesAsync(self, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextPhoneme]]: ...
class ITextReverseConversionGeneratorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.ITextReverseConversionGeneratorFactory'
    _iid_ = Guid('{63bed326-1fda-41f6-89d5-23ddea3c729a}')
    @winrt_commethod(6)
    def Create(self, languageTag: WinRT_String) -> win32more.Windows.Data.Text.TextReverseConversionGenerator: ...
class IUnicodeCharactersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.IUnicodeCharactersStatics'
    _iid_ = Guid('{97909e87-9291-4f91-b6c8-b6e359d7a7fb}')
    @winrt_commethod(6)
    def GetCodepointFromSurrogatePair(self, highSurrogate: UInt32, lowSurrogate: UInt32) -> UInt32: ...
    @winrt_commethod(7)
    def GetSurrogatePairFromCodepoint(self, codepoint: UInt32, highSurrogate: POINTER(Char), lowSurrogate: POINTER(Char)) -> Void: ...
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
    def GetNumericType(self, codepoint: UInt32) -> win32more.Windows.Data.Text.UnicodeNumericType: ...
    @winrt_commethod(22)
    def GetGeneralCategory(self, codepoint: UInt32) -> win32more.Windows.Data.Text.UnicodeGeneralCategory: ...
class IWordSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.IWordSegment'
    _iid_ = Guid('{d2d4ba6d-987c-4cc0-b6bd-d49a11b38f9a}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SourceTextSegment(self) -> win32more.Windows.Data.Text.TextSegment: ...
    @winrt_commethod(8)
    def get_AlternateForms(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.AlternateWordForm]: ...
    AlternateForms = property(get_AlternateForms, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
    Text = property(get_Text, None)
class IWordsSegmenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.IWordsSegmenter'
    _iid_ = Guid('{86b4d4d1-b2fe-4e34-a81d-66640300454f}')
    @winrt_commethod(6)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetTokenAt(self, text: WinRT_String, startIndex: UInt32) -> win32more.Windows.Data.Text.WordSegment: ...
    @winrt_commethod(8)
    def GetTokens(self, text: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.WordSegment]: ...
    @winrt_commethod(9)
    def Tokenize(self, text: WinRT_String, startIndex: UInt32, handler: win32more.Windows.Data.Text.WordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class IWordsSegmenterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.IWordsSegmenterFactory'
    _iid_ = Guid('{e6977274-fc35-455c-8bfb-6d7f4653ca97}')
    @winrt_commethod(6)
    def CreateWithLanguage(self, language: WinRT_String) -> win32more.Windows.Data.Text.WordsSegmenter: ...
class SelectableWordSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.ISelectableWordSegment
    _classid_ = 'Windows.Data.Text.SelectableWordSegment'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Data.Text.ISelectableWordSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceTextSegment(self: win32more.Windows.Data.Text.ISelectableWordSegment) -> win32more.Windows.Data.Text.TextSegment: ...
    SourceTextSegment = property(get_SourceTextSegment, None)
    Text = property(get_Text, None)
class SelectableWordSegmentsTokenizingHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a3dfc9c-aede-4dc7-9e6c-41c044bd3592}')
    @winrt_commethod(3)
    def Invoke(self, precedingWords: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Data.Text.SelectableWordSegment], words: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Data.Text.SelectableWordSegment]) -> Void: ...
class SelectableWordsSegmenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.ISelectableWordsSegmenter
    _classid_ = 'Windows.Data.Text.SelectableWordsSegmenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Data.Text.SelectableWordsSegmenter.CreateWithLanguage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithLanguage(cls: win32more.Windows.Data.Text.ISelectableWordsSegmenterFactory, language: WinRT_String) -> win32more.Windows.Data.Text.SelectableWordsSegmenter: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Data.Text.ISelectableWordsSegmenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetTokenAt(self: win32more.Windows.Data.Text.ISelectableWordsSegmenter, text: WinRT_String, startIndex: UInt32) -> win32more.Windows.Data.Text.SelectableWordSegment: ...
    @winrt_mixinmethod
    def GetTokens(self: win32more.Windows.Data.Text.ISelectableWordsSegmenter, text: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.SelectableWordSegment]: ...
    @winrt_mixinmethod
    def Tokenize(self: win32more.Windows.Data.Text.ISelectableWordsSegmenter, text: WinRT_String, startIndex: UInt32, handler: win32more.Windows.Data.Text.SelectableWordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class SemanticTextQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.ISemanticTextQuery
    _classid_ = 'Windows.Data.Text.SemanticTextQuery'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Data.Text.SemanticTextQuery.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Data.Text.SemanticTextQuery.CreateWithLanguage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Data.Text.ISemanticTextQueryFactory, aqsFilter: WinRT_String) -> win32more.Windows.Data.Text.SemanticTextQuery: ...
    @winrt_factorymethod
    def CreateWithLanguage(cls: win32more.Windows.Data.Text.ISemanticTextQueryFactory, aqsFilter: WinRT_String, filterLanguage: WinRT_String) -> win32more.Windows.Data.Text.SemanticTextQuery: ...
    @winrt_mixinmethod
    def Find(self: win32more.Windows.Data.Text.ISemanticTextQuery, content: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]: ...
    @winrt_mixinmethod
    def FindInProperty(self: win32more.Windows.Data.Text.ISemanticTextQuery, propertyContent: WinRT_String, propertyName: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]: ...
class TextConversionGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.ITextConversionGenerator
    _classid_ = 'Windows.Data.Text.TextConversionGenerator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Data.Text.TextConversionGenerator.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Data.Text.ITextConversionGeneratorFactory, languageTag: WinRT_String) -> win32more.Windows.Data.Text.TextConversionGenerator: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Data.Text.ITextConversionGenerator) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LanguageAvailableButNotInstalled(self: win32more.Windows.Data.Text.ITextConversionGenerator) -> Boolean: ...
    @winrt_mixinmethod
    def GetCandidatesAsync(self: win32more.Windows.Data.Text.ITextConversionGenerator, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetCandidatesWithMaxCountAsync(self: win32more.Windows.Data.Text.ITextConversionGenerator, input: WinRT_String, maxCandidates: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class TextPhoneme(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.ITextPhoneme
    _classid_ = 'Windows.Data.Text.TextPhoneme'
    @winrt_mixinmethod
    def get_DisplayText(self: win32more.Windows.Data.Text.ITextPhoneme) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReadingText(self: win32more.Windows.Data.Text.ITextPhoneme) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, None)
    ReadingText = property(get_ReadingText, None)
class TextPredictionGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.ITextPredictionGenerator
    _classid_ = 'Windows.Data.Text.TextPredictionGenerator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Data.Text.TextPredictionGenerator.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Data.Text.ITextPredictionGeneratorFactory, languageTag: WinRT_String) -> win32more.Windows.Data.Text.TextPredictionGenerator: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Data.Text.ITextPredictionGenerator) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LanguageAvailableButNotInstalled(self: win32more.Windows.Data.Text.ITextPredictionGenerator) -> Boolean: ...
    @winrt_mixinmethod
    def GetCandidatesAsync(self: win32more.Windows.Data.Text.ITextPredictionGenerator, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetCandidatesWithMaxCountAsync(self: win32more.Windows.Data.Text.ITextPredictionGenerator, input: WinRT_String, maxCandidates: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetCandidatesWithParametersAsync(self: win32more.Windows.Data.Text.ITextPredictionGenerator2, input: WinRT_String, maxCandidates: UInt32, predictionOptions: win32more.Windows.Data.Text.TextPredictionOptions, previousStrings: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetNextWordCandidatesAsync(self: win32more.Windows.Data.Text.ITextPredictionGenerator2, maxCandidates: UInt32, previousStrings: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def get_InputScope(self: win32more.Windows.Data.Text.ITextPredictionGenerator2) -> win32more.Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_mixinmethod
    def put_InputScope(self: win32more.Windows.Data.Text.ITextPredictionGenerator2, value: win32more.Windows.UI.Text.Core.CoreTextInputScope) -> Void: ...
    InputScope = property(get_InputScope, put_InputScope)
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class TextPredictionOptions(Enum, UInt32):
    None_ = 0
    Predictions = 1
    Corrections = 2
class TextReverseConversionGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.ITextReverseConversionGenerator
    _classid_ = 'Windows.Data.Text.TextReverseConversionGenerator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Data.Text.TextReverseConversionGenerator.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Data.Text.ITextReverseConversionGeneratorFactory, languageTag: WinRT_String) -> win32more.Windows.Data.Text.TextReverseConversionGenerator: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Data.Text.ITextReverseConversionGenerator) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LanguageAvailableButNotInstalled(self: win32more.Windows.Data.Text.ITextReverseConversionGenerator) -> Boolean: ...
    @winrt_mixinmethod
    def ConvertBackAsync(self: win32more.Windows.Data.Text.ITextReverseConversionGenerator, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetPhonemesAsync(self: win32more.Windows.Data.Text.ITextReverseConversionGenerator2, input: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextPhoneme]]: ...
    LanguageAvailableButNotInstalled = property(get_LanguageAvailableButNotInstalled, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
class TextSegment(Structure):
    StartPosition: UInt32
    Length: UInt32
class UnicodeCharacters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Text.UnicodeCharacters'
    @winrt_classmethod
    def GetCodepointFromSurrogatePair(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, highSurrogate: UInt32, lowSurrogate: UInt32) -> UInt32: ...
    @winrt_classmethod
    def GetSurrogatePairFromCodepoint(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32, highSurrogate: POINTER(Char), lowSurrogate: POINTER(Char)) -> Void: ...
    @winrt_classmethod
    def IsHighSurrogate(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsLowSurrogate(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsSupplementary(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsNoncharacter(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsWhitespace(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsAlphabetic(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsCased(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsUppercase(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsLowercase(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsIdStart(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsIdContinue(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsGraphemeBase(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsGraphemeExtend(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> Boolean: ...
    @winrt_classmethod
    def GetNumericType(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> win32more.Windows.Data.Text.UnicodeNumericType: ...
    @winrt_classmethod
    def GetGeneralCategory(cls: win32more.Windows.Data.Text.IUnicodeCharactersStatics, codepoint: UInt32) -> win32more.Windows.Data.Text.UnicodeGeneralCategory: ...
class UnicodeGeneralCategory(Enum, Int32):
    UppercaseLetter = 0
    LowercaseLetter = 1
    TitlecaseLetter = 2
    ModifierLetter = 3
    OtherLetter = 4
    NonspacingMark = 5
    SpacingCombiningMark = 6
    EnclosingMark = 7
    DecimalDigitNumber = 8
    LetterNumber = 9
    OtherNumber = 10
    SpaceSeparator = 11
    LineSeparator = 12
    ParagraphSeparator = 13
    Control = 14
    Format = 15
    Surrogate = 16
    PrivateUse = 17
    ConnectorPunctuation = 18
    DashPunctuation = 19
    OpenPunctuation = 20
    ClosePunctuation = 21
    InitialQuotePunctuation = 22
    FinalQuotePunctuation = 23
    OtherPunctuation = 24
    MathSymbol = 25
    CurrencySymbol = 26
    ModifierSymbol = 27
    OtherSymbol = 28
    NotAssigned = 29
class UnicodeNumericType(Enum, Int32):
    None_ = 0
    Decimal = 1
    Digit = 2
    Numeric = 3
class WordSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.IWordSegment
    _classid_ = 'Windows.Data.Text.WordSegment'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Data.Text.IWordSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceTextSegment(self: win32more.Windows.Data.Text.IWordSegment) -> win32more.Windows.Data.Text.TextSegment: ...
    @winrt_mixinmethod
    def get_AlternateForms(self: win32more.Windows.Data.Text.IWordSegment) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.AlternateWordForm]: ...
    AlternateForms = property(get_AlternateForms, None)
    SourceTextSegment = property(get_SourceTextSegment, None)
    Text = property(get_Text, None)
class WordSegmentsTokenizingHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5dd6357-bf2a-4c4f-a31f-29e71c6f8b35}')
    @winrt_commethod(3)
    def Invoke(self, precedingWords: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Data.Text.WordSegment], words: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Data.Text.WordSegment]) -> Void: ...
class WordsSegmenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Text.IWordsSegmenter
    _classid_ = 'Windows.Data.Text.WordsSegmenter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Data.Text.WordsSegmenter.CreateWithLanguage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithLanguage(cls: win32more.Windows.Data.Text.IWordsSegmenterFactory, language: WinRT_String) -> win32more.Windows.Data.Text.WordsSegmenter: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Data.Text.IWordsSegmenter) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetTokenAt(self: win32more.Windows.Data.Text.IWordsSegmenter, text: WinRT_String, startIndex: UInt32) -> win32more.Windows.Data.Text.WordSegment: ...
    @winrt_mixinmethod
    def GetTokens(self: win32more.Windows.Data.Text.IWordsSegmenter, text: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.WordSegment]: ...
    @winrt_mixinmethod
    def Tokenize(self: win32more.Windows.Data.Text.IWordsSegmenter, text: WinRT_String, startIndex: UInt32, handler: win32more.Windows.Data.Text.WordSegmentsTokenizingHandler) -> Void: ...
    ResolvedLanguage = property(get_ResolvedLanguage, None)


make_ready(__name__)
