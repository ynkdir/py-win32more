from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.AI
import win32more.Microsoft.Windows.AI.ContentSafety
import win32more.Microsoft.Windows.AI.Foundation
import win32more.Microsoft.Windows.AI.Text
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class ConversationItem(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.IConversationItem
    _classid_ = 'Microsoft.Windows.AI.Text.ConversationItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.AI.Text.ConversationItem.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.AI.Text.ConversationItem: ...
    @winrt_mixinmethod
    def get_Participant(self: win32more.Microsoft.Windows.AI.Text.IConversationItem) -> hstr: ...
    @winrt_mixinmethod
    def put_Participant(self: win32more.Microsoft.Windows.AI.Text.IConversationItem, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Microsoft.Windows.AI.Text.IConversationItem) -> hstr: ...
    @winrt_mixinmethod
    def put_Message(self: win32more.Microsoft.Windows.AI.Text.IConversationItem, value: hstr) -> Void: ...
    Message = property(get_Message, put_Message)
    Participant = property(get_Participant, put_Participant)
class ConversationSummaryOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions
    _classid_ = 'Microsoft.Windows.AI.Text.ConversationSummaryOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.AI.Text.ConversationSummaryOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.AI.Text.ConversationSummaryOptions: ...
    @winrt_mixinmethod
    def get_InputKind(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions) -> win32more.Microsoft.Windows.AI.Text.InputKind: ...
    @winrt_mixinmethod
    def put_InputKind(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions, value: win32more.Microsoft.Windows.AI.Text.InputKind) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeMessageCitations(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeMessageCitations(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeParticipantAttribution(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeParticipantAttribution(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxKeyPoints(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxKeyPoints(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Microsoft.Windows.AI.Text.IConversationSummaryOptions, value: hstr) -> Void: ...
    IncludeMessageCitations = property(get_IncludeMessageCitations, put_IncludeMessageCitations)
    IncludeParticipantAttribution = property(get_IncludeParticipantAttribution, put_IncludeParticipantAttribution)
    InputKind = property(get_InputKind, put_InputKind)
    Language = property(get_Language, put_Language)
    MaxKeyPoints = property(get_MaxKeyPoints, put_MaxKeyPoints)
class IConversationItem(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.IConversationItem'
    _iid_ = Guid('{957b0b85-4d7e-5788-baae-af7cf256bb8e}')
    @winrt_commethod(6)
    def get_Participant(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Participant(self, value: hstr) -> Void: ...
    @winrt_commethod(8)
    def get_Message(self) -> hstr: ...
    @winrt_commethod(9)
    def put_Message(self, value: hstr) -> Void: ...
    Message = property(get_Message, put_Message)
    Participant = property(get_Participant, put_Participant)
class IConversationSummaryOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.IConversationSummaryOptions'
    _iid_ = Guid('{360bce9f-fd14-5d0e-bd24-fd78ed3038e6}')
    @winrt_commethod(6)
    def get_InputKind(self) -> win32more.Microsoft.Windows.AI.Text.InputKind: ...
    @winrt_commethod(7)
    def put_InputKind(self, value: win32more.Microsoft.Windows.AI.Text.InputKind) -> Void: ...
    @winrt_commethod(8)
    def get_IncludeMessageCitations(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IncludeMessageCitations(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IncludeParticipantAttribution(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IncludeParticipantAttribution(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_MaxKeyPoints(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_MaxKeyPoints(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_Language(self) -> hstr: ...
    @winrt_commethod(15)
    def put_Language(self, value: hstr) -> Void: ...
    IncludeMessageCitations = property(get_IncludeMessageCitations, put_IncludeMessageCitations)
    IncludeParticipantAttribution = property(get_IncludeParticipantAttribution, put_IncludeParticipantAttribution)
    InputKind = property(get_InputKind, put_InputKind)
    Language = property(get_Language, put_Language)
    MaxKeyPoints = property(get_MaxKeyPoints, put_MaxKeyPoints)
class ILanguageModel(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModel'
    _iid_ = Guid('{6331c629-8c86-5bfe-8c4e-9ca5573cc14b}')
class ILanguageModel2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModel2'
    _iid_ = Guid('{653b714e-f9b3-51cb-954f-5ea58f63ab89}')
    @winrt_commethod(6)
    def GenerateResponseAsync(self, prompt: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_commethod(7)
    def GenerateResponseAsync2(self, prompt: hstr, options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_commethod(8)
    def GenerateResponseAsync3(self, context: win32more.Microsoft.Windows.AI.Text.LanguageModelContext, prompt: hstr, options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_commethod(9)
    def GenerateResponseFromEmbeddingsAsync(self, promptEmbedding: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_commethod(10)
    def GenerateResponseFromEmbeddingsAsync2(self, promptEmbedding: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector], options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_commethod(11)
    def GenerateResponseFromEmbeddingsAsync3(self, context: win32more.Microsoft.Windows.AI.Text.LanguageModelContext, promptEmbedding: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector], options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_commethod(12)
    def GenerateEmbeddingVectors(self, prompt: hstr) -> win32more.Microsoft.Windows.AI.Text.LanguageModelEmbeddingVectorResult: ...
    @winrt_commethod(13)
    def GenerateEmbeddingVectors2(self, prompt: hstr, contentFilterOptions: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> win32more.Microsoft.Windows.AI.Text.LanguageModelEmbeddingVectorResult: ...
    @winrt_commethod(14)
    def GetUsablePromptLength(self, prompt: hstr) -> UInt64: ...
    @winrt_commethod(15)
    def GetUsablePromptLength2(self, context: win32more.Microsoft.Windows.AI.Text.LanguageModelContext, prompt: hstr) -> UInt64: ...
    @winrt_commethod(16)
    def GetVectorSpaceId(self) -> Guid: ...
    @winrt_commethod(17)
    def CreateContext(self) -> win32more.Microsoft.Windows.AI.Text.LanguageModelContext: ...
    @winrt_commethod(18)
    def CreateContext2(self, systemPrompt: hstr) -> win32more.Microsoft.Windows.AI.Text.LanguageModelContext: ...
    @winrt_commethod(19)
    def CreateContext3(self, systemPrompt: hstr, contentFilterOptions: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> win32more.Microsoft.Windows.AI.Text.LanguageModelContext: ...
class ILanguageModelContext(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModelContext'
    _iid_ = Guid('{518b305c-7b69-5a33-8129-d47d6b8eec4e}')
class ILanguageModelEmbeddingVectorResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ILanguageModelEmbeddingVectorResult'
    _iid_ = Guid('{4dbdb154-ee3c-56f6-a40b-413e95bd5acb}')
    @winrt_commethod(6)
    def get_EmbeddingVectors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.Text.LanguageModelResponseStatus: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    EmbeddingVectors = property(get_EmbeddingVectors, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
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
    def get_Text(self) -> hstr: ...
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
    def RewriteAsync(self, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
class ITextRewriter2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextRewriter2'
    _iid_ = Guid('{7937d261-13ce-5b24-b17c-fe5cd0be23b6}')
    @winrt_commethod(6)
    def RewriteAsync(self, text: hstr, tone: win32more.Microsoft.Windows.AI.Text.TextRewriteTone) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
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
    def SummarizeAsync(self, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_commethod(7)
    def SummarizeParagraphAsync(self, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
class ITextSummarizer2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextSummarizer2'
    _iid_ = Guid('{9e20797d-1ff6-5295-8cb6-d48fb8ba483b}')
    @winrt_commethod(6)
    def SummarizeConversationAsync(self, messages: win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.AI.Text.ConversationItem], options: win32more.Microsoft.Windows.AI.Text.ConversationSummaryOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
class ITextSummarizer3(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextSummarizer3'
    _iid_ = Guid('{493d32b9-dbc9-5d4b-802f-90473850500e}')
    @winrt_commethod(6)
    def IsPromptLargerThanContext(self, messages: PassArray[win32more.Microsoft.Windows.AI.Text.ConversationItem], options: win32more.Microsoft.Windows.AI.Text.ConversationSummaryOptions, cutoffPosition: POINTER(UInt64)) -> Boolean: ...
class ITextSummarizer4(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Text.ITextSummarizer4'
    _iid_ = Guid('{5b7a28c0-7777-52e5-9934-b95b514cf535}')
    @winrt_commethod(6)
    def IsPromptLargerThanContext(self, text: hstr, cutoffPosition: POINTER(UInt64)) -> Boolean: ...
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
    def ConvertAsync(self, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.TextToTableResponseResult, hstr]: ...
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
    def GetColumns(self) -> ReceiveArray[hstr]: ...
class InputKind(Enum, Int32):
    GeneralConversation = 0
    Email = 1
class LanguageModel(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Text.ILanguageModel
    _classid_ = 'Microsoft.Windows.AI.Text.LanguageModel'
    @winrt_mixinmethod
    def GenerateResponseAsync(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, prompt: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def GenerateResponseAsync2(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, prompt: hstr, options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def GenerateResponseAsync3(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, context: win32more.Microsoft.Windows.AI.Text.LanguageModelContext, prompt: hstr, options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def GenerateResponseFromEmbeddingsAsync(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, promptEmbedding: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def GenerateResponseFromEmbeddingsAsync2(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, promptEmbedding: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector], options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def GenerateResponseFromEmbeddingsAsync3(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, context: win32more.Microsoft.Windows.AI.Text.LanguageModelContext, promptEmbedding: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector], options: win32more.Microsoft.Windows.AI.Text.LanguageModelOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def GenerateEmbeddingVectors(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, prompt: hstr) -> win32more.Microsoft.Windows.AI.Text.LanguageModelEmbeddingVectorResult: ...
    @winrt_mixinmethod
    def GenerateEmbeddingVectors2(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, prompt: hstr, contentFilterOptions: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> win32more.Microsoft.Windows.AI.Text.LanguageModelEmbeddingVectorResult: ...
    @winrt_mixinmethod
    def GetUsablePromptLength(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, prompt: hstr) -> UInt64: ...
    @winrt_mixinmethod
    def GetUsablePromptLength2(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, context: win32more.Microsoft.Windows.AI.Text.LanguageModelContext, prompt: hstr) -> UInt64: ...
    @winrt_mixinmethod
    def GetVectorSpaceId(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2) -> Guid: ...
    @winrt_mixinmethod
    def CreateContext(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2) -> win32more.Microsoft.Windows.AI.Text.LanguageModelContext: ...
    @winrt_mixinmethod
    def CreateContext2(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, systemPrompt: hstr) -> win32more.Microsoft.Windows.AI.Text.LanguageModelContext: ...
    @winrt_mixinmethod
    def CreateContext3(self: win32more.Microsoft.Windows.AI.Text.ILanguageModel2, systemPrompt: hstr, contentFilterOptions: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> win32more.Microsoft.Windows.AI.Text.LanguageModelContext: ...
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
class LanguageModelEmbeddingVectorResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Text.ILanguageModelEmbeddingVectorResult
    _classid_ = 'Microsoft.Windows.AI.Text.LanguageModelEmbeddingVectorResult'
    @winrt_mixinmethod
    def get_EmbeddingVectors(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelEmbeddingVectorResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelEmbeddingVectorResult) -> win32more.Microsoft.Windows.AI.Text.LanguageModelResponseStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelEmbeddingVectorResult) -> win32more.Windows.Foundation.HResult: ...
    EmbeddingVectors = property(get_EmbeddingVectors, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
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
    def get_Text(self: win32more.Microsoft.Windows.AI.Text.ILanguageModelResponseResult) -> hstr: ...
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
TextIntelligenceContract: UInt32 = 393216
class TextRewriteTone(Enum, Int32):
    Default = 0
    General = 1
    Casual = 2
    Concise = 3
    Formal = 4
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
    @winrt_overload
    @winrt_mixinmethod
    def RewriteAsync(self: win32more.Microsoft.Windows.AI.Text.ITextRewriter, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @RewriteAsync.register
    @winrt_mixinmethod
    def RewriteAsync(self: win32more.Microsoft.Windows.AI.Text.ITextRewriter2, text: hstr, tone: win32more.Microsoft.Windows.AI.Text.TextRewriteTone) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
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
    def SummarizeAsync(self: win32more.Microsoft.Windows.AI.Text.ITextSummarizer, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def SummarizeParagraphAsync(self: win32more.Microsoft.Windows.AI.Text.ITextSummarizer, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_mixinmethod
    def SummarizeConversationAsync(self: win32more.Microsoft.Windows.AI.Text.ITextSummarizer2, messages: win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.AI.Text.ConversationItem], options: win32more.Microsoft.Windows.AI.Text.ConversationSummaryOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.LanguageModelResponseResult, hstr]: ...
    @winrt_overload
    @winrt_mixinmethod
    def IsPromptLargerThanContext(self: win32more.Microsoft.Windows.AI.Text.ITextSummarizer3, messages: PassArray[win32more.Microsoft.Windows.AI.Text.ConversationItem], options: win32more.Microsoft.Windows.AI.Text.ConversationSummaryOptions, cutoffPosition: POINTER(UInt64)) -> Boolean: ...
    @IsPromptLargerThanContext.register
    @winrt_mixinmethod
    def IsPromptLargerThanContext(self: win32more.Microsoft.Windows.AI.Text.ITextSummarizer4, text: hstr, cutoffPosition: POINTER(UInt64)) -> Boolean: ...
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
    def ConvertAsync(self: win32more.Microsoft.Windows.AI.Text.ITextToTableConverter, text: hstr) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Text.TextToTableResponseResult, hstr]: ...
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
    def GetColumns(self: win32more.Microsoft.Windows.AI.Text.ITextToTableRow) -> ReceiveArray[hstr]: ...


make_ready(__name__)
