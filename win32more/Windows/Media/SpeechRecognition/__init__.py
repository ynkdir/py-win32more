from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.Media.SpeechRecognition
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
class ISpeechContinuousRecognitionCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionCompletedEventArgs'
    _iid_ = Guid('{e3d069bb-e30c-5e18-424b-7fbe81f8fbd0}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
class ISpeechContinuousRecognitionResultGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionResultGeneratedEventArgs'
    _iid_ = Guid('{19091e1e-6e7e-5a46-40fb-76594f786504}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    Result = property(get_Result, None)
class ISpeechContinuousRecognitionSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession'
    _iid_ = Guid('{6a213c04-6614-49f8-99a2-b5e9b3a085c8}')
    @winrt_commethod(6)
    def get_AutoStopSilenceTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_AutoStopSilenceTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def StartWithModeAsync(self, mode: win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionMode) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def CancelAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def PauseAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def Resume(self) -> Void: ...
    @winrt_commethod(14)
    def add_Completed(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Completed(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_ResultGenerated(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionResultGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ResultGenerated(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoStopSilenceTimeout = property(get_AutoStopSilenceTimeout, put_AutoStopSilenceTimeout)
    Completed = event()
    ResultGenerated = event()
class ISpeechRecognitionCompilationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionCompilationResult'
    _iid_ = Guid('{407e6c5d-6ac7-4da4-9cc1-2fce32cf7489}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
class ISpeechRecognitionConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint'
    _iid_ = Guid('{79ac1628-4d68-43c4-8911-40dc4101b55b}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Type(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_commethod(11)
    def get_Probability(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_commethod(12)
    def put_Probability(self, value: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Probability = property(get_Probability, put_Probability)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
class ISpeechRecognitionGrammarFileConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraint'
    _iid_ = Guid('{b5031a8f-85ca-4fa4-b11a-474fc41b3835}')
    @winrt_commethod(6)
    def get_GrammarFile(self) -> win32more.Windows.Storage.StorageFile: ...
    GrammarFile = property(get_GrammarFile, None)
class ISpeechRecognitionGrammarFileConstraintFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraintFactory'
    _iid_ = Guid('{3da770eb-c479-4c27-9f19-89974ef392d1}')
    @winrt_commethod(6)
    def Create(self, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
    @winrt_commethod(7)
    def CreateWithTag(self, file: win32more.Windows.Storage.StorageFile, tag: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
class ISpeechRecognitionHypothesis(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesis'
    _iid_ = Guid('{7a7b25b0-99c5-4f7d-bf84-10aa1302b634}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    Text = property(get_Text, None)
class ISpeechRecognitionHypothesisGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesisGeneratedEventArgs'
    _iid_ = Guid('{55161a7a-8023-5866-411d-1213bb271476}')
    @winrt_commethod(6)
    def get_Hypothesis(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionHypothesis: ...
    Hypothesis = property(get_Hypothesis, None)
class ISpeechRecognitionListConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraint'
    _iid_ = Guid('{09c487e9-e4ad-4526-81f2-4946fb481d98}')
    @winrt_commethod(6)
    def get_Commands(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Commands = property(get_Commands, None)
class ISpeechRecognitionListConstraintFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraintFactory'
    _iid_ = Guid('{40f3cdc7-562a-426a-9f3b-3b4e282be1d5}')
    @winrt_commethod(6)
    def Create(self, commands: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
    @winrt_commethod(7)
    def CreateWithTag(self, commands: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], tag: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
class ISpeechRecognitionQualityDegradingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionQualityDegradingEventArgs'
    _iid_ = Guid('{4fe24105-8c3a-4c7e-8d0a-5bd4f5b14ad8}')
    @winrt_commethod(6)
    def get_Problem(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionAudioProblem: ...
    Problem = property(get_Problem, None)
class ISpeechRecognitionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionResult'
    _iid_ = Guid('{4e303157-034e-4652-857e-d0454cc4beec}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Confidence(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConfidence: ...
    @winrt_commethod(9)
    def get_SemanticInterpretation(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation: ...
    @winrt_commethod(10)
    def GetAlternates(self, maxAlternates: UInt32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_commethod(11)
    def get_Constraint(self) -> win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint: ...
    @winrt_commethod(12)
    def get_RulePath(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_RawConfidence(self) -> Double: ...
    Confidence = property(get_Confidence, None)
    Constraint = property(get_Constraint, None)
    RawConfidence = property(get_RawConfidence, None)
    RulePath = property(get_RulePath, None)
    SemanticInterpretation = property(get_SemanticInterpretation, None)
    Status = property(get_Status, None)
    Text = property(get_Text, None)
class ISpeechRecognitionResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionResult2'
    _iid_ = Guid('{af7ed1ba-451b-4166-a0c1-1ffe84032d03}')
    @winrt_commethod(6)
    def get_PhraseStartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PhraseDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    PhraseDuration = property(get_PhraseDuration, None)
    PhraseStartTime = property(get_PhraseStartTime, None)
class ISpeechRecognitionSemanticInterpretation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionSemanticInterpretation'
    _iid_ = Guid('{aae1da9b-7e32-4c1f-89fe-0c65f486f52e}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    Properties = property(get_Properties, None)
class ISpeechRecognitionTopicConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraint'
    _iid_ = Guid('{bf6fdf19-825d-4e69-a681-36e48cf1c93e}')
    @winrt_commethod(6)
    def get_Scenario(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionScenario: ...
    @winrt_commethod(7)
    def get_TopicHint(self) -> WinRT_String: ...
    Scenario = property(get_Scenario, None)
    TopicHint = property(get_TopicHint, None)
class ISpeechRecognitionTopicConstraintFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraintFactory'
    _iid_ = Guid('{6e6863df-ec05-47d7-a5df-56a3431e58d2}')
    @winrt_commethod(6)
    def Create(self, scenario: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
    @winrt_commethod(7)
    def CreateWithTag(self, scenario: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String, tag: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
class ISpeechRecognitionVoiceCommandDefinitionConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognitionVoiceCommandDefinitionConstraint'
    _iid_ = Guid('{f2791c2b-1ef4-4ae7-9d77-b6ff10b8a3c2}')
class ISpeechRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizer'
    _iid_ = Guid('{0bc3c9cb-c26a-40f2-aeb5-8096b2e48073}')
    @winrt_commethod(6)
    def get_CurrentLanguage(self) -> win32more.Windows.Globalization.Language: ...
    @winrt_commethod(7)
    def get_Constraints(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint]: ...
    @winrt_commethod(8)
    def get_Timeouts(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerTimeouts: ...
    @winrt_commethod(9)
    def get_UIOptions(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerUIOptions: ...
    @winrt_commethod(10)
    def CompileConstraintsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionCompilationResult]: ...
    @winrt_commethod(11)
    def RecognizeAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_commethod(12)
    def RecognizeWithUIAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_commethod(13)
    def add_RecognitionQualityDegrading(self, speechRecognitionQualityDegradingHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechRecognizer, win32more.Windows.Media.SpeechRecognition.SpeechRecognitionQualityDegradingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_RecognitionQualityDegrading(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_StateChanged(self, stateChangedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechRecognizer, win32more.Windows.Media.SpeechRecognition.SpeechRecognizerStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_StateChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Constraints = property(get_Constraints, None)
    CurrentLanguage = property(get_CurrentLanguage, None)
    Timeouts = property(get_Timeouts, None)
    UIOptions = property(get_UIOptions, None)
    RecognitionQualityDegrading = event()
    StateChanged = event()
class ISpeechRecognizer2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizer2'
    _iid_ = Guid('{63c9baf1-91e3-4ea4-86a1-7c3867d084a6}')
    @winrt_commethod(6)
    def get_ContinuousRecognitionSession(self) -> win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession: ...
    @winrt_commethod(7)
    def get_State(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    @winrt_commethod(8)
    def StopRecognitionAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_HypothesisGenerated(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechRecognizer, win32more.Windows.Media.SpeechRecognition.SpeechRecognitionHypothesisGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_HypothesisGenerated(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ContinuousRecognitionSession = property(get_ContinuousRecognitionSession, None)
    State = property(get_State, None)
    HypothesisGenerated = event()
class ISpeechRecognizerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizerFactory'
    _iid_ = Guid('{60c488dd-7fb8-4033-ac70-d046f64818e1}')
    @winrt_commethod(6)
    def Create(self, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizer: ...
class ISpeechRecognizerStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizerStateChangedEventArgs'
    _iid_ = Guid('{563d4f09-ba03-4bad-ad81-ddc6c4dab0c3}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    State = property(get_State, None)
class ISpeechRecognizerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizerStatics'
    _iid_ = Guid('{87a35eac-a7dc-4b0b-bcc9-24f47c0b7ebf}')
    @winrt_commethod(6)
    def get_SystemSpeechLanguage(self) -> win32more.Windows.Globalization.Language: ...
    @winrt_commethod(7)
    def get_SupportedTopicLanguages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    @winrt_commethod(8)
    def get_SupportedGrammarLanguages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    SupportedGrammarLanguages = property(get_SupportedGrammarLanguages, None)
    SupportedTopicLanguages = property(get_SupportedTopicLanguages, None)
    SystemSpeechLanguage = property(get_SystemSpeechLanguage, None)
class ISpeechRecognizerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizerStatics2'
    _iid_ = Guid('{1d1b0d95-7565-4ef9-a2f3-ba15162a96cf}')
    @winrt_commethod(6)
    def TrySetSystemSpeechLanguageAsync(self, speechLanguage: win32more.Windows.Globalization.Language) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISpeechRecognizerTimeouts(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts'
    _iid_ = Guid('{2ef76fca-6a3c-4dca-a153-df1bc88a79af}')
    @winrt_commethod(6)
    def get_InitialSilenceTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_InitialSilenceTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_EndSilenceTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_EndSilenceTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_BabbleTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_BabbleTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    BabbleTimeout = property(get_BabbleTimeout, put_BabbleTimeout)
    EndSilenceTimeout = property(get_EndSilenceTimeout, put_EndSilenceTimeout)
    InitialSilenceTimeout = property(get_InitialSilenceTimeout, put_InitialSilenceTimeout)
class ISpeechRecognizerUIOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions'
    _iid_ = Guid('{7888d641-b92b-44ba-a25f-d1864630641f}')
    @winrt_commethod(6)
    def get_ExampleText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ExampleText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AudiblePrompt(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_AudiblePrompt(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_IsReadBackEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsReadBackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_ShowConfirmation(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_ShowConfirmation(self, value: Boolean) -> Void: ...
    AudiblePrompt = property(get_AudiblePrompt, put_AudiblePrompt)
    ExampleText = property(get_ExampleText, put_ExampleText)
    IsReadBackEnabled = property(get_IsReadBackEnabled, put_IsReadBackEnabled)
    ShowConfirmation = property(get_ShowConfirmation, put_ShowConfirmation)
class IVoiceCommandManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.IVoiceCommandManager'
    _iid_ = Guid('{aa3a8dd5-b6e7-4ee2-baa9-dd6baced0a2b}')
    @winrt_commethod(6)
    def InstallCommandSetsFromStorageFileAsync(self, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def get_InstalledCommandSets(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Media.SpeechRecognition.VoiceCommandSet]: ...
    InstalledCommandSets = property(get_InstalledCommandSets, None)
class IVoiceCommandSet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.IVoiceCommandSet'
    _iid_ = Guid('{0bedda75-46e6-4b11-a088-5c68632899b5}')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetPhraseListAsync(self, phraseListName: WinRT_String, phraseList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)
class SpeechContinuousRecognitionCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionCompletedEventArgs
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechContinuousRecognitionCompletedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionCompletedEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
class SpeechContinuousRecognitionMode(Enum, Int32):
    Default = 0
    PauseOnRecognition = 1
class SpeechContinuousRecognitionResultGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionResultGeneratedEventArgs
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechContinuousRecognitionResultGeneratedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionResultGeneratedEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    Result = property(get_Result, None)
class SpeechContinuousRecognitionSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession'
    @winrt_mixinmethod
    def get_AutoStopSilenceTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_AutoStopSilenceTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartWithModeAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, mode: win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionMode) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResultGenerated(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionResultGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResultGenerated(self: win32more.Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoStopSilenceTimeout = property(get_AutoStopSilenceTimeout, put_AutoStopSilenceTimeout)
    Completed = event()
    ResultGenerated = event()
class SpeechRecognitionAudioProblem(Enum, Int32):
    None_ = 0
    TooNoisy = 1
    NoSignal = 2
    TooLoud = 3
    TooQuiet = 4
    TooFast = 5
    TooSlow = 6
class SpeechRecognitionCompilationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionCompilationResult
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionCompilationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionCompilationResult) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
class SpeechRecognitionConfidence(Enum, Int32):
    High = 0
    Medium = 1
    Low = 2
    Rejected = 3
class SpeechRecognitionConstraintProbability(Enum, Int32):
    Default = 0
    Min = 1
    Max = 2
class SpeechRecognitionConstraintType(Enum, Int32):
    Topic = 0
    List = 1
    Grammar = 2
    VoiceCommandDefinition = 3
class SpeechRecognitionGrammarFileConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraint
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint.CreateWithTag(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraintFactory, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
    @winrt_factorymethod
    def CreateWithTag(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraintFactory, file: win32more.Windows.Storage.StorageFile, tag: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
    @winrt_mixinmethod
    def get_GrammarFile(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraint) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    GrammarFile = property(get_GrammarFile, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Probability = property(get_Probability, put_Probability)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
class SpeechRecognitionHypothesis(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesis
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionHypothesis'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesis) -> WinRT_String: ...
    Text = property(get_Text, None)
class SpeechRecognitionHypothesisGeneratedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesisGeneratedEventArgs
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionHypothesisGeneratedEventArgs'
    @winrt_mixinmethod
    def get_Hypothesis(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesisGeneratedEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionHypothesis: ...
    Hypothesis = property(get_Hypothesis, None)
class SpeechRecognitionListConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraint
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint.CreateWithTag(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraintFactory, commands: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
    @winrt_factorymethod
    def CreateWithTag(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraintFactory, commands: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], tag: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
    @winrt_mixinmethod
    def get_Commands(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraint) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    Commands = property(get_Commands, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Probability = property(get_Probability, put_Probability)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
class SpeechRecognitionQualityDegradingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionQualityDegradingEventArgs
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionQualityDegradingEventArgs'
    @winrt_mixinmethod
    def get_Problem(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionQualityDegradingEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionAudioProblem: ...
    Problem = property(get_Problem, None)
class SpeechRecognitionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Confidence(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConfidence: ...
    @winrt_mixinmethod
    def get_SemanticInterpretation(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation: ...
    @winrt_mixinmethod
    def GetAlternates(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult, maxAlternates: UInt32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_mixinmethod
    def get_Constraint(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint: ...
    @winrt_mixinmethod
    def get_RulePath(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RawConfidence(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> Double: ...
    @winrt_mixinmethod
    def get_PhraseStartTime(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult2) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PhraseDuration(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionResult2) -> win32more.Windows.Foundation.TimeSpan: ...
    Confidence = property(get_Confidence, None)
    Constraint = property(get_Constraint, None)
    PhraseDuration = property(get_PhraseDuration, None)
    PhraseStartTime = property(get_PhraseStartTime, None)
    RawConfidence = property(get_RawConfidence, None)
    RulePath = property(get_RulePath, None)
    SemanticInterpretation = property(get_SemanticInterpretation, None)
    Status = property(get_Status, None)
    Text = property(get_Text, None)
class SpeechRecognitionResultStatus(Enum, Int32):
    Success = 0
    TopicLanguageNotSupported = 1
    GrammarLanguageMismatch = 2
    GrammarCompilationFailure = 3
    AudioQualityFailure = 4
    UserCanceled = 5
    Unknown = 6
    TimeoutExceeded = 7
    PauseLimitExceeded = 8
    NetworkFailure = 9
    MicrophoneUnavailable = 10
class SpeechRecognitionScenario(Enum, Int32):
    WebSearch = 0
    Dictation = 1
    FormFilling = 2
class SpeechRecognitionSemanticInterpretation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionSemanticInterpretation
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation'
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionSemanticInterpretation) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    Properties = property(get_Properties, None)
class SpeechRecognitionTopicConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraint
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint.CreateWithTag(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraintFactory, scenario: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
    @winrt_factorymethod
    def CreateWithTag(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraintFactory, scenario: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String, tag: WinRT_String) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
    @winrt_mixinmethod
    def get_Scenario(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionScenario: ...
    @winrt_mixinmethod
    def get_TopicHint(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Probability = property(get_Probability, put_Probability)
    Scenario = property(get_Scenario, None)
    Tag = property(get_Tag, put_Tag)
    TopicHint = property(get_TopicHint, None)
    Type = property(get_Type, None)
class SpeechRecognitionVoiceCommandDefinitionConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionVoiceCommandDefinitionConstraint
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionVoiceCommandDefinitionConstraint'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: win32more.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Probability = property(get_Probability, put_Probability)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
class _SpeechRecognizer_Meta_(ComPtr.__class__):
    pass
class SpeechRecognizer(ComPtr, metaclass=_SpeechRecognizer_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognizer.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.SpeechRecognition.SpeechRecognizer.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizer: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerFactory, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizer: ...
    @winrt_mixinmethod
    def get_CurrentLanguage(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer) -> win32more.Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def get_Constraints(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint]: ...
    @winrt_mixinmethod
    def get_Timeouts(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerTimeouts: ...
    @winrt_mixinmethod
    def get_UIOptions(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerUIOptions: ...
    @winrt_mixinmethod
    def CompileConstraintsAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionCompilationResult]: ...
    @winrt_mixinmethod
    def RecognizeAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_mixinmethod
    def RecognizeWithUIAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_mixinmethod
    def add_RecognitionQualityDegrading(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer, speechRecognitionQualityDegradingHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechRecognizer, win32more.Windows.Media.SpeechRecognition.SpeechRecognitionQualityDegradingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecognitionQualityDegrading(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer, stateChangedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechRecognizer, win32more.Windows.Media.SpeechRecognition.SpeechRecognizerStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_ContinuousRecognitionSession(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer2) -> win32more.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer2) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    @winrt_mixinmethod
    def StopRecognitionAsync(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_HypothesisGenerated(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.SpeechRecognition.SpeechRecognizer, win32more.Windows.Media.SpeechRecognition.SpeechRecognitionHypothesisGeneratedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HypothesisGenerated(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizer2, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TrySetSystemSpeechLanguageAsync(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerStatics2, speechLanguage: win32more.Windows.Globalization.Language) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_SystemSpeechLanguage(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerStatics) -> win32more.Windows.Globalization.Language: ...
    @winrt_classmethod
    def get_SupportedTopicLanguages(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    @winrt_classmethod
    def get_SupportedGrammarLanguages(cls: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    Constraints = property(get_Constraints, None)
    ContinuousRecognitionSession = property(get_ContinuousRecognitionSession, None)
    CurrentLanguage = property(get_CurrentLanguage, None)
    State = property(get_State, None)
    Timeouts = property(get_Timeouts, None)
    UIOptions = property(get_UIOptions, None)
    _SpeechRecognizer_Meta_.SupportedGrammarLanguages = property(get_SupportedGrammarLanguages, None)
    _SpeechRecognizer_Meta_.SupportedTopicLanguages = property(get_SupportedTopicLanguages, None)
    _SpeechRecognizer_Meta_.SystemSpeechLanguage = property(get_SystemSpeechLanguage, None)
    RecognitionQualityDegrading = event()
    StateChanged = event()
    HypothesisGenerated = event()
class SpeechRecognizerState(Enum, Int32):
    Idle = 0
    Capturing = 1
    Processing = 2
    SoundStarted = 3
    SoundEnded = 4
    SpeechDetected = 5
    Paused = 6
class SpeechRecognizerStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerStateChangedEventArgs
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizerStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerStateChangedEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    State = property(get_State, None)
class SpeechRecognizerTimeouts(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizerTimeouts'
    @winrt_mixinmethod
    def get_InitialSilenceTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_InitialSilenceTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_EndSilenceTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_EndSilenceTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_BabbleTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_BabbleTimeout(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    BabbleTimeout = property(get_BabbleTimeout, put_BabbleTimeout)
    EndSilenceTimeout = property(get_EndSilenceTimeout, put_EndSilenceTimeout)
    InitialSilenceTimeout = property(get_InitialSilenceTimeout, put_InitialSilenceTimeout)
class SpeechRecognizerUIOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizerUIOptions'
    @winrt_mixinmethod
    def get_ExampleText(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExampleText(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AudiblePrompt(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AudiblePrompt(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsReadBackEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsReadBackEnabled(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowConfirmation(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowConfirmation(self: win32more.Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: Boolean) -> Void: ...
    AudiblePrompt = property(get_AudiblePrompt, put_AudiblePrompt)
    ExampleText = property(get_ExampleText, put_ExampleText)
    IsReadBackEnabled = property(get_IsReadBackEnabled, put_IsReadBackEnabled)
    ShowConfirmation = property(get_ShowConfirmation, put_ShowConfirmation)
class _VoiceCommandManager_Meta_(ComPtr.__class__):
    pass
class VoiceCommandManager(ComPtr, metaclass=_VoiceCommandManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.VoiceCommandManager'
    @winrt_classmethod
    def InstallCommandSetsFromStorageFileAsync(cls: win32more.Windows.Media.SpeechRecognition.IVoiceCommandManager, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_InstalledCommandSets(cls: win32more.Windows.Media.SpeechRecognition.IVoiceCommandManager) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Media.SpeechRecognition.VoiceCommandSet]: ...
    _VoiceCommandManager_Meta_.InstalledCommandSets = property(get_InstalledCommandSets, None)
class VoiceCommandSet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechRecognition.IVoiceCommandSet
    _classid_ = 'Windows.Media.SpeechRecognition.VoiceCommandSet'
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.SpeechRecognition.IVoiceCommandSet) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.SpeechRecognition.IVoiceCommandSet) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetPhraseListAsync(self: win32more.Windows.Media.SpeechRecognition.IVoiceCommandSet, phraseListName: WinRT_String, phraseList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)


make_ready(__name__)
