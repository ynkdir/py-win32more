from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.AI
import win32more.Microsoft.Windows.AI.ContentSafety
import win32more.Microsoft.Windows.AI.Text
import win32more.Windows.Foundation
class ILanguageModel(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModel'
    _iid_ = Guid('{6331c629-8c86-5bfe-8c4e-9ca5573cc14b}')
class ILanguageModelContext(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModelContext'
    _iid_ = Guid('{518b305c-7b69-5a33-8129-d47d6b8eec4e}')
class ILanguageModelOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModelOptions'
    _iid_ = Guid('{7f380003-5a09-5f1f-afb0-aa483e3670cc}')
    @winrt_commethod(6)
    def get_Temperature(self) -> Single: ...
    @winrt_commethod(7)
    def put_Temperature(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_TopP(self) -> Single: ...
    @winrt_commethod(9)
    def put_TopP(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_TopK(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_TopK(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_ContentFilterOptions(self) -> win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions: ...
    @winrt_commethod(13)
    def put_ContentFilterOptions(self, value: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> Void: ...
    ContentFilterOptions = property(get_ContentFilterOptions, put_ContentFilterOptions)
    Temperature = property(get_Temperature, put_Temperature)
    TopK = property(get_TopK, put_TopK)
    TopP = property(get_TopP, put_TopP)
class ILanguageModelResponseResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModelResponseResult'
    _iid_ = Guid('{3a256fff-a426-5d3b-8e4b-3ac84162471e}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.Text.LanguageModelResponseStatus: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
    Text = property(get_Text, None)
class ILanguageModelStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModelStatics'
    _iid_ = Guid('{8f18f9af-6095-553b-8d9d-6bcc98026546}')
    @winrt_commethod(6)
    def GetReadyState(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_commethod(7)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_commethod(8)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Text.LanguageModel]: ...
class ITextRewriter(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextRewriter'
    _iid_ = Guid('{eb1e7cf0-e110-506c-b0ea-7a288d8e7778}')
    @winrt_commethod(6)
    def RewriteAsync(self, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, WinRT_String]: ...
class ITextRewriterFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextRewriterFactory'
    _iid_ = Guid('{f452e60d-ef50-5bc9-b483-217d5b4e7151}')
    @winrt_commethod(6)
    def CreateInstance(self, languageModel: win32more.Microsoft.Windows.AI.Text.LanguageModel) -> win32more.Microsoft.Windows.AI.Text.TextRewriter: ...
class ITextSummarizer(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextSummarizer'
    _iid_ = Guid('{eef548c5-d7bc-50be-a8ab-29e241b78bd1}')
    @winrt_commethod(6)
    def SummarizeAsync(self, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, WinRT_String]: ...
    @winrt_commethod(7)
    def SummarizeParagraphAsync(self, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, WinRT_String]: ...
class ITextSummarizerFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextSummarizerFactory'
    _iid_ = Guid('{b6a75913-4a1e-59e7-856a-ae7ab2383864}')
    @winrt_commethod(6)
    def CreateInstance(self, languageModel: win32more.Microsoft.Windows.AI.Text.LanguageModel) -> win32more.Microsoft.Windows.AI.Text.TextSummarizer: ...
class ITextToTableConverter(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextToTableConverter'
    _iid_ = Guid('{a008d9ad-25ce-5a6b-9ceb-d8e95d04e10b}')
    @winrt_commethod(6)
    def ConvertAsync(self, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.TextToTableResponseResult, WinRT_String]: ...
class ITextToTableConverterFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextToTableConverterFactory'
    _iid_ = Guid('{bb84cbb5-19c8-5857-b65d-705aa1486404}')
    @winrt_commethod(6)
    def CreateInstance(self, languageModel: win32more.Microsoft.Windows.AI.Text.LanguageModel) -> win32more.Microsoft.Windows.AI.Text.TextToTableConverter: ...
class ITextToTableResponseResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextToTableResponseResult'
    _iid_ = Guid('{391fbf11-59cd-575d-834a-9ef823116f98}')
    @winrt_commethod(6)
    def GetRows(self) -> ReceiveArray[win32more.Microsoft.Windows.AI.Text.TextToTableRow]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.Text.LanguageModelResponseStatus: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class ITextToTableRow(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextToTableRow'
    _iid_ = Guid('{036294fe-e53c-5e66-93d2-7c92338db881}')
    @winrt_commethod(6)
    def GetColumns(self) -> ReceiveArray[WinRT_String]: ...
class LanguageModel(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Text.ILanguageModel
    _classid_ = 'Microsoft.Windows.AI.Text.LanguageModel'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetReadyState(cls: win32more.Microsoft.Windows.AI.Text.ILanguageModelStatics) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_classmethod
    def EnsureReadyAsync(cls: win32more.Microsoft.Windows.AI.Text.ILanguageModelStatics) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Microsoft.Windows.AI.Text.ILanguageModelStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Text.LanguageModel]: ...
class LanguageModelContext(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Text.ILanguageModelContext
    _classid_ = 'Microsoft.Windows.AI.Text.LanguageModelContext'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
LanguageModelContract: UInt32 = 131072
class LanguageModelOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions
    _classid_ = 'Microsoft.Windows.AI.Text.LanguageModelOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.AI.Text.LanguageModelOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.AI.Text.LanguageModelOptions: ...
    @winrt_mixinmethod
    def get_Temperature(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions) -> Single: ...
    @winrt_mixinmethod
    def put_Temperature(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopP(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions) -> Single: ...
    @winrt_mixinmethod
    def put_TopP(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopK(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_TopK(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ContentFilterOptions(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions) -> win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions: ...
    @winrt_mixinmethod
    def put_ContentFilterOptions(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelOptions, value: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> Void: ...
    ContentFilterOptions = property(get_ContentFilterOptions, put_ContentFilterOptions)
    Temperature = property(get_Temperature, put_Temperature)
    TopK = property(get_TopK, put_TopK)
    TopP = property(get_TopP, put_TopP)
class LanguageModelResponseResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ILanguageModelResponseResult
    _classid_ = 'Microsoft.Windows.AI.Text.LanguageModelResponseResult'
    @winrt_mixinmethod
    def get_Text(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelResponseResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelResponseResult) -> win32more.Microsoft.Windows.AI.Text.LanguageModelResponseStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelResponseResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
    Text = property(get_Text, None)
class LanguageModelResponseStatus(Enum, Int32):
    Complete = 0
    InProgress = 1
    BlockedByPolicy = 2
    PromptLargerThanContext = 3
    PromptBlockedByContentModeration = 4
    ResponseBlockedByContentModeration = 5
    Error = 6
TextIntelligenceContract: UInt32 = 131072
class TextRewriter(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ITextRewriter
    _classid_ = 'Microsoft.Windows.AI.Text.TextRewriter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AI.Text.TextRewriter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.Text.ITextRewriterFactory, languageModel: win32more.Microsoft.Windows.AI.Text.LanguageModel) -> win32more.Microsoft.Windows.AI.Text.TextRewriter: ...
    @winrt_mixinmethod
    def RewriteAsync(self: win32more.Microsoft.Windows.AI.Text.ITextRewriter, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, WinRT_String]: ...
class TextSummarizer(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ITextSummarizer
    _classid_ = 'Microsoft.Windows.AI.Text.TextSummarizer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AI.Text.TextSummarizer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.Text.ITextSummarizerFactory, languageModel: win32more.Microsoft.Windows.AI.Text.LanguageModel) -> win32more.Microsoft.Windows.AI.Text.TextSummarizer: ...
    @winrt_mixinmethod
    def SummarizeAsync(self: win32more.Microsoft.Windows.AI.Text.ITextSummarizer, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, WinRT_String]: ...
    @winrt_mixinmethod
    def SummarizeParagraphAsync(self: win32more.Microsoft.Windows.AI.Text.ITextSummarizer, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, WinRT_String]: ...
class TextToTableConverter(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ITextToTableConverter
    _classid_ = 'Microsoft.Windows.AI.Text.TextToTableConverter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AI.Text.TextToTableConverter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.Text.ITextToTableConverterFactory, languageModel: win32more.Microsoft.Windows.AI.Text.LanguageModel) -> win32more.Microsoft.Windows.AI.Text.TextToTableConverter: ...
    @winrt_mixinmethod
    def ConvertAsync(self: win32more.Microsoft.Windows.AI.Text.ITextToTableConverter, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.TextToTableResponseResult, WinRT_String]: ...
class TextToTableResponseResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ITextToTableResponseResult
    _classid_ = 'Microsoft.Windows.AI.Text.TextToTableResponseResult'
    @winrt_mixinmethod
    def GetRows(self: win32more.Microsoft.Windows.AI.Text.ITextToTableResponseResult) -> ReceiveArray[win32more.Microsoft.Windows.AI.Text.TextToTableRow]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.Text.ITextToTableResponseResult) -> win32more.Microsoft.Windows.AI.Text.LanguageModelResponseStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.AI.Text.ITextToTableResponseResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class TextToTableRow(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ITextToTableRow
    _classid_ = 'Microsoft.Windows.AI.Text.TextToTableRow'
    @winrt_mixinmethod
    def GetColumns(self: win32more.Microsoft.Windows.AI.Text.ITextToTableRow) -> ReceiveArray[WinRT_String]: ...


make_ready(__name__)
