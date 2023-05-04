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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Globalization
import Windows.Media.SpeechRecognition
import Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISpeechContinuousRecognitionCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e3d069bb-e30c-5e18-424b-7fbe81f8fbd0}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
class ISpeechContinuousRecognitionResultGeneratedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{19091e1e-6e7e-5a46-40fb-76594f786504}')
    @winrt_commethod(6)
    def get_Result(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    Result = property(get_Result, None)
class ISpeechContinuousRecognitionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6a213c04-6614-49f8-99a2-b5e9b3a085c8}')
    @winrt_commethod(6)
    def get_AutoStopSilenceTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_AutoStopSilenceTimeout(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def StartAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def StartWithModeAsync(self, mode: Windows.Media.SpeechRecognition.SpeechContinuousRecognitionMode) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def CancelAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def PauseAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def Resume(self) -> Void: ...
    @winrt_commethod(14)
    def add_Completed(self, value: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, Windows.Media.SpeechRecognition.SpeechContinuousRecognitionCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Completed(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_ResultGenerated(self, value: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, Windows.Media.SpeechRecognition.SpeechContinuousRecognitionResultGeneratedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ResultGenerated(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoStopSilenceTimeout = property(get_AutoStopSilenceTimeout, put_AutoStopSilenceTimeout)
class ISpeechRecognitionCompilationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{407e6c5d-6ac7-4da4-9cc1-2fce32cf7489}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
class ISpeechRecognitionConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_Type(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_commethod(11)
    def get_Probability(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_commethod(12)
    def put_Probability(self, value: Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
    Probability = property(get_Probability, put_Probability)
class ISpeechRecognitionGrammarFileConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b5031a8f-85ca-4fa4-b11a-474fc41b3835}')
    @winrt_commethod(6)
    def get_GrammarFile(self) -> Windows.Storage.StorageFile: ...
    GrammarFile = property(get_GrammarFile, None)
class ISpeechRecognitionGrammarFileConstraintFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3da770eb-c479-4c27-9f19-89974ef392d1}')
    @winrt_commethod(6)
    def Create(self, file: Windows.Storage.StorageFile) -> Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
    @winrt_commethod(7)
    def CreateWithTag(self, file: Windows.Storage.StorageFile, tag: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
class ISpeechRecognitionHypothesis(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7a7b25b0-99c5-4f7d-bf84-10aa1302b634}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    Text = property(get_Text, None)
class ISpeechRecognitionHypothesisGeneratedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{55161a7a-8023-5866-411d-1213bb271476}')
    @winrt_commethod(6)
    def get_Hypothesis(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionHypothesis: ...
    Hypothesis = property(get_Hypothesis, None)
class ISpeechRecognitionListConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{09c487e9-e4ad-4526-81f2-4946fb481d98}')
    @winrt_commethod(6)
    def get_Commands(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Commands = property(get_Commands, None)
class ISpeechRecognitionListConstraintFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{40f3cdc7-562a-426a-9f3b-3b4e282be1d5}')
    @winrt_commethod(6)
    def Create(self, commands: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
    @winrt_commethod(7)
    def CreateWithTag(self, commands: Windows.Foundation.Collections.IIterable[WinRT_String], tag: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
class ISpeechRecognitionQualityDegradingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4fe24105-8c3a-4c7e-8d0a-5bd4f5b14ad8}')
    @winrt_commethod(6)
    def get_Problem(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionAudioProblem: ...
    Problem = property(get_Problem, None)
class ISpeechRecognitionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4e303157-034e-4652-857e-d0454cc4beec}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Confidence(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionConfidence: ...
    @winrt_commethod(9)
    def get_SemanticInterpretation(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation: ...
    @winrt_commethod(10)
    def GetAlternates(self, maxAlternates: UInt32) -> Windows.Foundation.Collections.IVectorView[Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_commethod(11)
    def get_Constraint(self) -> Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint: ...
    @winrt_commethod(12)
    def get_RulePath(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_RawConfidence(self) -> Double: ...
    Status = property(get_Status, None)
    Text = property(get_Text, None)
    Confidence = property(get_Confidence, None)
    SemanticInterpretation = property(get_SemanticInterpretation, None)
    Constraint = property(get_Constraint, None)
    RulePath = property(get_RulePath, None)
    RawConfidence = property(get_RawConfidence, None)
class ISpeechRecognitionResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{af7ed1ba-451b-4166-a0c1-1ffe84032d03}')
    @winrt_commethod(6)
    def get_PhraseStartTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PhraseDuration(self) -> Windows.Foundation.TimeSpan: ...
    PhraseStartTime = property(get_PhraseStartTime, None)
    PhraseDuration = property(get_PhraseDuration, None)
class ISpeechRecognitionSemanticInterpretation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{aae1da9b-7e32-4c1f-89fe-0c65f486f52e}')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    Properties = property(get_Properties, None)
class ISpeechRecognitionTopicConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bf6fdf19-825d-4e69-a681-36e48cf1c93e}')
    @winrt_commethod(6)
    def get_Scenario(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionScenario: ...
    @winrt_commethod(7)
    def get_TopicHint(self) -> WinRT_String: ...
    Scenario = property(get_Scenario, None)
    TopicHint = property(get_TopicHint, None)
class ISpeechRecognitionTopicConstraintFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6e6863df-ec05-47d7-a5df-56a3431e58d2}')
    @winrt_commethod(6)
    def Create(self, scenario: Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
    @winrt_commethod(7)
    def CreateWithTag(self, scenario: Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String, tag: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
class ISpeechRecognitionVoiceCommandDefinitionConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f2791c2b-1ef4-4ae7-9d77-b6ff10b8a3c2}')
class ISpeechRecognizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0bc3c9cb-c26a-40f2-aeb5-8096b2e48073}')
    @winrt_commethod(6)
    def get_CurrentLanguage(self) -> Windows.Globalization.Language: ...
    @winrt_commethod(7)
    def get_Constraints(self) -> Windows.Foundation.Collections.IVector[Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint]: ...
    @winrt_commethod(8)
    def get_Timeouts(self) -> Windows.Media.SpeechRecognition.SpeechRecognizerTimeouts: ...
    @winrt_commethod(9)
    def get_UIOptions(self) -> Windows.Media.SpeechRecognition.SpeechRecognizerUIOptions: ...
    @winrt_commethod(10)
    def CompileConstraintsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechRecognition.SpeechRecognitionCompilationResult]: ...
    @winrt_commethod(11)
    def RecognizeAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_commethod(12)
    def RecognizeWithUIAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_commethod(13)
    def add_RecognitionQualityDegrading(self, speechRecognitionQualityDegradingHandler: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechRecognizer, Windows.Media.SpeechRecognition.SpeechRecognitionQualityDegradingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_RecognitionQualityDegrading(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_StateChanged(self, stateChangedHandler: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechRecognizer, Windows.Media.SpeechRecognition.SpeechRecognizerStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_StateChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentLanguage = property(get_CurrentLanguage, None)
    Constraints = property(get_Constraints, None)
    Timeouts = property(get_Timeouts, None)
    UIOptions = property(get_UIOptions, None)
class ISpeechRecognizer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{63c9baf1-91e3-4ea4-86a1-7c3867d084a6}')
    @winrt_commethod(6)
    def get_ContinuousRecognitionSession(self) -> Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession: ...
    @winrt_commethod(7)
    def get_State(self) -> Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    @winrt_commethod(8)
    def StopRecognitionAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_HypothesisGenerated(self, value: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechRecognizer, Windows.Media.SpeechRecognition.SpeechRecognitionHypothesisGeneratedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_HypothesisGenerated(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ContinuousRecognitionSession = property(get_ContinuousRecognitionSession, None)
    State = property(get_State, None)
class ISpeechRecognizerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{60c488dd-7fb8-4033-ac70-d046f64818e1}')
    @winrt_commethod(6)
    def Create(self, language: Windows.Globalization.Language) -> Windows.Media.SpeechRecognition.SpeechRecognizer: ...
class ISpeechRecognizerStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{563d4f09-ba03-4bad-ad81-ddc6c4dab0c3}')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    State = property(get_State, None)
class ISpeechRecognizerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{87a35eac-a7dc-4b0b-bcc9-24f47c0b7ebf}')
    @winrt_commethod(6)
    def get_SystemSpeechLanguage(self) -> Windows.Globalization.Language: ...
    @winrt_commethod(7)
    def get_SupportedTopicLanguages(self) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    @winrt_commethod(8)
    def get_SupportedGrammarLanguages(self) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    SystemSpeechLanguage = property(get_SystemSpeechLanguage, None)
    SupportedTopicLanguages = property(get_SupportedTopicLanguages, None)
    SupportedGrammarLanguages = property(get_SupportedGrammarLanguages, None)
class ISpeechRecognizerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1d1b0d95-7565-4ef9-a2f3-ba15162a96cf}')
    @winrt_commethod(6)
    def TrySetSystemSpeechLanguageAsync(self, speechLanguage: Windows.Globalization.Language) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISpeechRecognizerTimeouts(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2ef76fca-6a3c-4dca-a153-df1bc88a79af}')
    @winrt_commethod(6)
    def get_InitialSilenceTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_InitialSilenceTimeout(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_EndSilenceTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_EndSilenceTimeout(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_BabbleTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_BabbleTimeout(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    InitialSilenceTimeout = property(get_InitialSilenceTimeout, put_InitialSilenceTimeout)
    EndSilenceTimeout = property(get_EndSilenceTimeout, put_EndSilenceTimeout)
    BabbleTimeout = property(get_BabbleTimeout, put_BabbleTimeout)
class ISpeechRecognizerUIOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    ExampleText = property(get_ExampleText, put_ExampleText)
    AudiblePrompt = property(get_AudiblePrompt, put_AudiblePrompt)
    IsReadBackEnabled = property(get_IsReadBackEnabled, put_IsReadBackEnabled)
    ShowConfirmation = property(get_ShowConfirmation, put_ShowConfirmation)
class IVoiceCommandManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{aa3a8dd5-b6e7-4ee2-baa9-dd6baced0a2b}')
    @winrt_commethod(6)
    def InstallCommandSetsFromStorageFileAsync(self, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def get_InstalledCommandSets(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Media.SpeechRecognition.VoiceCommandSet]: ...
    InstalledCommandSets = property(get_InstalledCommandSets, None)
class IVoiceCommandSet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0bedda75-46e6-4b11-a088-5c68632899b5}')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetPhraseListAsync(self, phraseListName: WinRT_String, phraseList: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)
class SpeechContinuousRecognitionCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechContinuousRecognitionCompletedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionCompletedEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
SpeechContinuousRecognitionMode = Int32
SpeechContinuousRecognitionMode_Default: SpeechContinuousRecognitionMode = 0
SpeechContinuousRecognitionMode_PauseOnRecognition: SpeechContinuousRecognitionMode = 1
class SpeechContinuousRecognitionResultGeneratedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechContinuousRecognitionResultGeneratedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionResultGeneratedEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    Result = property(get_Result, None)
class SpeechContinuousRecognitionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession'
    @winrt_mixinmethod
    def get_AutoStopSilenceTimeout(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_AutoStopSilenceTimeout(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartWithModeAsync(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, mode: Windows.Media.SpeechRecognition.SpeechContinuousRecognitionMode) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelAsync(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseAsync(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Resume(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, Windows.Media.SpeechRecognition.SpeechContinuousRecognitionCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResultGenerated(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession, Windows.Media.SpeechRecognition.SpeechContinuousRecognitionResultGeneratedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResultGenerated(self: Windows.Media.SpeechRecognition.ISpeechContinuousRecognitionSession, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoStopSilenceTimeout = property(get_AutoStopSilenceTimeout, put_AutoStopSilenceTimeout)
SpeechRecognitionAudioProblem = Int32
SpeechRecognitionAudioProblem_None: SpeechRecognitionAudioProblem = 0
SpeechRecognitionAudioProblem_TooNoisy: SpeechRecognitionAudioProblem = 1
SpeechRecognitionAudioProblem_NoSignal: SpeechRecognitionAudioProblem = 2
SpeechRecognitionAudioProblem_TooLoud: SpeechRecognitionAudioProblem = 3
SpeechRecognitionAudioProblem_TooQuiet: SpeechRecognitionAudioProblem = 4
SpeechRecognitionAudioProblem_TooFast: SpeechRecognitionAudioProblem = 5
SpeechRecognitionAudioProblem_TooSlow: SpeechRecognitionAudioProblem = 6
class SpeechRecognitionCompilationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionCompilationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.SpeechRecognition.ISpeechRecognitionCompilationResult) -> Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    Status = property(get_Status, None)
SpeechRecognitionConfidence = Int32
SpeechRecognitionConfidence_High: SpeechRecognitionConfidence = 0
SpeechRecognitionConfidence_Medium: SpeechRecognitionConfidence = 1
SpeechRecognitionConfidence_Low: SpeechRecognitionConfidence = 2
SpeechRecognitionConfidence_Rejected: SpeechRecognitionConfidence = 3
SpeechRecognitionConstraintProbability = Int32
SpeechRecognitionConstraintProbability_Default: SpeechRecognitionConstraintProbability = 0
SpeechRecognitionConstraintProbability_Min: SpeechRecognitionConstraintProbability = 1
SpeechRecognitionConstraintProbability_Max: SpeechRecognitionConstraintProbability = 2
SpeechRecognitionConstraintType = Int32
SpeechRecognitionConstraintType_Topic: SpeechRecognitionConstraintType = 0
SpeechRecognitionConstraintType_List: SpeechRecognitionConstraintType = 1
SpeechRecognitionConstraintType_Grammar: SpeechRecognitionConstraintType = 2
SpeechRecognitionConstraintType_VoiceCommandDefinition: SpeechRecognitionConstraintType = 3
class SpeechRecognitionGrammarFileConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint'
    @winrt_factorymethod
    def Create(cls: Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraintFactory, file: Windows.Storage.StorageFile) -> Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
    @winrt_factorymethod
    def CreateWithTag(cls: Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraintFactory, file: Windows.Storage.StorageFile, tag: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionGrammarFileConstraint: ...
    @winrt_mixinmethod
    def get_GrammarFile(self: Windows.Media.SpeechRecognition.ISpeechRecognitionGrammarFileConstraint) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    GrammarFile = property(get_GrammarFile, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
    Probability = property(get_Probability, put_Probability)
class SpeechRecognitionHypothesis(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionHypothesis'
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesis) -> WinRT_String: ...
    Text = property(get_Text, None)
class SpeechRecognitionHypothesisGeneratedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionHypothesisGeneratedEventArgs'
    @winrt_mixinmethod
    def get_Hypothesis(self: Windows.Media.SpeechRecognition.ISpeechRecognitionHypothesisGeneratedEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognitionHypothesis: ...
    Hypothesis = property(get_Hypothesis, None)
class SpeechRecognitionListConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint'
    @winrt_factorymethod
    def Create(cls: Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraintFactory, commands: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
    @winrt_factorymethod
    def CreateWithTag(cls: Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraintFactory, commands: Windows.Foundation.Collections.IIterable[WinRT_String], tag: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionListConstraint: ...
    @winrt_mixinmethod
    def get_Commands(self: Windows.Media.SpeechRecognition.ISpeechRecognitionListConstraint) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    Commands = property(get_Commands, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
    Probability = property(get_Probability, put_Probability)
class SpeechRecognitionQualityDegradingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionQualityDegradingEventArgs'
    @winrt_mixinmethod
    def get_Problem(self: Windows.Media.SpeechRecognition.ISpeechRecognitionQualityDegradingEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognitionAudioProblem: ...
    Problem = property(get_Problem, None)
class SpeechRecognitionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Confidence(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> Windows.Media.SpeechRecognition.SpeechRecognitionConfidence: ...
    @winrt_mixinmethod
    def get_SemanticInterpretation(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation: ...
    @winrt_mixinmethod
    def GetAlternates(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult, maxAlternates: UInt32) -> Windows.Foundation.Collections.IVectorView[Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_mixinmethod
    def get_Constraint(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint: ...
    @winrt_mixinmethod
    def get_RulePath(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RawConfidence(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult) -> Double: ...
    @winrt_mixinmethod
    def get_PhraseStartTime(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult2) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PhraseDuration(self: Windows.Media.SpeechRecognition.ISpeechRecognitionResult2) -> Windows.Foundation.TimeSpan: ...
    Status = property(get_Status, None)
    Text = property(get_Text, None)
    Confidence = property(get_Confidence, None)
    SemanticInterpretation = property(get_SemanticInterpretation, None)
    Constraint = property(get_Constraint, None)
    RulePath = property(get_RulePath, None)
    RawConfidence = property(get_RawConfidence, None)
    PhraseStartTime = property(get_PhraseStartTime, None)
    PhraseDuration = property(get_PhraseDuration, None)
SpeechRecognitionResultStatus = Int32
SpeechRecognitionResultStatus_Success: SpeechRecognitionResultStatus = 0
SpeechRecognitionResultStatus_TopicLanguageNotSupported: SpeechRecognitionResultStatus = 1
SpeechRecognitionResultStatus_GrammarLanguageMismatch: SpeechRecognitionResultStatus = 2
SpeechRecognitionResultStatus_GrammarCompilationFailure: SpeechRecognitionResultStatus = 3
SpeechRecognitionResultStatus_AudioQualityFailure: SpeechRecognitionResultStatus = 4
SpeechRecognitionResultStatus_UserCanceled: SpeechRecognitionResultStatus = 5
SpeechRecognitionResultStatus_Unknown: SpeechRecognitionResultStatus = 6
SpeechRecognitionResultStatus_TimeoutExceeded: SpeechRecognitionResultStatus = 7
SpeechRecognitionResultStatus_PauseLimitExceeded: SpeechRecognitionResultStatus = 8
SpeechRecognitionResultStatus_NetworkFailure: SpeechRecognitionResultStatus = 9
SpeechRecognitionResultStatus_MicrophoneUnavailable: SpeechRecognitionResultStatus = 10
SpeechRecognitionScenario = Int32
SpeechRecognitionScenario_WebSearch: SpeechRecognitionScenario = 0
SpeechRecognitionScenario_Dictation: SpeechRecognitionScenario = 1
SpeechRecognitionScenario_FormFilling: SpeechRecognitionScenario = 2
class SpeechRecognitionSemanticInterpretation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionSemanticInterpretation'
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.SpeechRecognition.ISpeechRecognitionSemanticInterpretation) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    Properties = property(get_Properties, None)
class SpeechRecognitionTopicConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint'
    @winrt_factorymethod
    def Create(cls: Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraintFactory, scenario: Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
    @winrt_factorymethod
    def CreateWithTag(cls: Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraintFactory, scenario: Windows.Media.SpeechRecognition.SpeechRecognitionScenario, topicHint: WinRT_String, tag: WinRT_String) -> Windows.Media.SpeechRecognition.SpeechRecognitionTopicConstraint: ...
    @winrt_mixinmethod
    def get_Scenario(self: Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionScenario: ...
    @winrt_mixinmethod
    def get_TopicHint(self: Windows.Media.SpeechRecognition.ISpeechRecognitionTopicConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    Scenario = property(get_Scenario, None)
    TopicHint = property(get_TopicHint, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
    Probability = property(get_Probability, put_Probability)
class SpeechRecognitionVoiceCommandDefinitionConstraint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognitionVoiceCommandDefinitionConstraint'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType: ...
    @winrt_mixinmethod
    def get_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint) -> Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability: ...
    @winrt_mixinmethod
    def put_Probability(self: Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint, value: Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Tag = property(get_Tag, put_Tag)
    Type = property(get_Type, None)
    Probability = property(get_Probability, put_Probability)
class SpeechRecognizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizer'
    @winrt_factorymethod
    def Create(cls: Windows.Media.SpeechRecognition.ISpeechRecognizerFactory, language: Windows.Globalization.Language) -> Windows.Media.SpeechRecognition.SpeechRecognizer: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Media.SpeechRecognition.SpeechRecognizer: ...
    @winrt_mixinmethod
    def get_CurrentLanguage(self: Windows.Media.SpeechRecognition.ISpeechRecognizer) -> Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def get_Constraints(self: Windows.Media.SpeechRecognition.ISpeechRecognizer) -> Windows.Foundation.Collections.IVector[Windows.Media.SpeechRecognition.ISpeechRecognitionConstraint]: ...
    @winrt_mixinmethod
    def get_Timeouts(self: Windows.Media.SpeechRecognition.ISpeechRecognizer) -> Windows.Media.SpeechRecognition.SpeechRecognizerTimeouts: ...
    @winrt_mixinmethod
    def get_UIOptions(self: Windows.Media.SpeechRecognition.ISpeechRecognizer) -> Windows.Media.SpeechRecognition.SpeechRecognizerUIOptions: ...
    @winrt_mixinmethod
    def CompileConstraintsAsync(self: Windows.Media.SpeechRecognition.ISpeechRecognizer) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechRecognition.SpeechRecognitionCompilationResult]: ...
    @winrt_mixinmethod
    def RecognizeAsync(self: Windows.Media.SpeechRecognition.ISpeechRecognizer) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_mixinmethod
    def RecognizeWithUIAsync(self: Windows.Media.SpeechRecognition.ISpeechRecognizer) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechRecognition.SpeechRecognitionResult]: ...
    @winrt_mixinmethod
    def add_RecognitionQualityDegrading(self: Windows.Media.SpeechRecognition.ISpeechRecognizer, speechRecognitionQualityDegradingHandler: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechRecognizer, Windows.Media.SpeechRecognition.SpeechRecognitionQualityDegradingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecognitionQualityDegrading(self: Windows.Media.SpeechRecognition.ISpeechRecognizer, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Media.SpeechRecognition.ISpeechRecognizer, stateChangedHandler: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechRecognizer, Windows.Media.SpeechRecognition.SpeechRecognizerStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Media.SpeechRecognition.ISpeechRecognizer, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_ContinuousRecognitionSession(self: Windows.Media.SpeechRecognition.ISpeechRecognizer2) -> Windows.Media.SpeechRecognition.SpeechContinuousRecognitionSession: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Media.SpeechRecognition.ISpeechRecognizer2) -> Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    @winrt_mixinmethod
    def StopRecognitionAsync(self: Windows.Media.SpeechRecognition.ISpeechRecognizer2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_HypothesisGenerated(self: Windows.Media.SpeechRecognition.ISpeechRecognizer2, value: Windows.Foundation.TypedEventHandler[Windows.Media.SpeechRecognition.SpeechRecognizer, Windows.Media.SpeechRecognition.SpeechRecognitionHypothesisGeneratedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HypothesisGenerated(self: Windows.Media.SpeechRecognition.ISpeechRecognizer2, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TrySetSystemSpeechLanguageAsync(cls: Windows.Media.SpeechRecognition.ISpeechRecognizerStatics2, speechLanguage: Windows.Globalization.Language) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_SystemSpeechLanguage(cls: Windows.Media.SpeechRecognition.ISpeechRecognizerStatics) -> Windows.Globalization.Language: ...
    @winrt_classmethod
    def get_SupportedTopicLanguages(cls: Windows.Media.SpeechRecognition.ISpeechRecognizerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    @winrt_classmethod
    def get_SupportedGrammarLanguages(cls: Windows.Media.SpeechRecognition.ISpeechRecognizerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    CurrentLanguage = property(get_CurrentLanguage, None)
    Constraints = property(get_Constraints, None)
    Timeouts = property(get_Timeouts, None)
    UIOptions = property(get_UIOptions, None)
    ContinuousRecognitionSession = property(get_ContinuousRecognitionSession, None)
    State = property(get_State, None)
    SystemSpeechLanguage = property(get_SystemSpeechLanguage, None)
    SupportedTopicLanguages = property(get_SupportedTopicLanguages, None)
    SupportedGrammarLanguages = property(get_SupportedGrammarLanguages, None)
SpeechRecognizerState = Int32
SpeechRecognizerState_Idle: SpeechRecognizerState = 0
SpeechRecognizerState_Capturing: SpeechRecognizerState = 1
SpeechRecognizerState_Processing: SpeechRecognizerState = 2
SpeechRecognizerState_SoundStarted: SpeechRecognizerState = 3
SpeechRecognizerState_SoundEnded: SpeechRecognizerState = 4
SpeechRecognizerState_SpeechDetected: SpeechRecognizerState = 5
SpeechRecognizerState_Paused: SpeechRecognizerState = 6
class SpeechRecognizerStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizerStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: Windows.Media.SpeechRecognition.ISpeechRecognizerStateChangedEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognizerState: ...
    State = property(get_State, None)
class SpeechRecognizerTimeouts(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizerTimeouts'
    @winrt_mixinmethod
    def get_InitialSilenceTimeout(self: Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_InitialSilenceTimeout(self: Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_EndSilenceTimeout(self: Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_EndSilenceTimeout(self: Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_BabbleTimeout(self: Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_BabbleTimeout(self: Windows.Media.SpeechRecognition.ISpeechRecognizerTimeouts, value: Windows.Foundation.TimeSpan) -> Void: ...
    InitialSilenceTimeout = property(get_InitialSilenceTimeout, put_InitialSilenceTimeout)
    EndSilenceTimeout = property(get_EndSilenceTimeout, put_EndSilenceTimeout)
    BabbleTimeout = property(get_BabbleTimeout, put_BabbleTimeout)
class SpeechRecognizerUIOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.SpeechRecognizerUIOptions'
    @winrt_mixinmethod
    def get_ExampleText(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExampleText(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AudiblePrompt(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AudiblePrompt(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsReadBackEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsReadBackEnabled(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowConfirmation(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowConfirmation(self: Windows.Media.SpeechRecognition.ISpeechRecognizerUIOptions, value: Boolean) -> Void: ...
    ExampleText = property(get_ExampleText, put_ExampleText)
    AudiblePrompt = property(get_AudiblePrompt, put_AudiblePrompt)
    IsReadBackEnabled = property(get_IsReadBackEnabled, put_IsReadBackEnabled)
    ShowConfirmation = property(get_ShowConfirmation, put_ShowConfirmation)
class VoiceCommandManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.VoiceCommandManager'
    @winrt_classmethod
    def InstallCommandSetsFromStorageFileAsync(cls: Windows.Media.SpeechRecognition.IVoiceCommandManager, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_InstalledCommandSets(cls: Windows.Media.SpeechRecognition.IVoiceCommandManager) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Media.SpeechRecognition.VoiceCommandSet]: ...
    InstalledCommandSets = property(get_InstalledCommandSets, None)
class VoiceCommandSet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechRecognition.VoiceCommandSet'
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.SpeechRecognition.IVoiceCommandSet) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.SpeechRecognition.IVoiceCommandSet) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetPhraseListAsync(self: Windows.Media.SpeechRecognition.IVoiceCommandSet, phraseListName: WinRT_String, phraseList: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)
make_head(_module, 'ISpeechContinuousRecognitionCompletedEventArgs')
make_head(_module, 'ISpeechContinuousRecognitionResultGeneratedEventArgs')
make_head(_module, 'ISpeechContinuousRecognitionSession')
make_head(_module, 'ISpeechRecognitionCompilationResult')
make_head(_module, 'ISpeechRecognitionConstraint')
make_head(_module, 'ISpeechRecognitionGrammarFileConstraint')
make_head(_module, 'ISpeechRecognitionGrammarFileConstraintFactory')
make_head(_module, 'ISpeechRecognitionHypothesis')
make_head(_module, 'ISpeechRecognitionHypothesisGeneratedEventArgs')
make_head(_module, 'ISpeechRecognitionListConstraint')
make_head(_module, 'ISpeechRecognitionListConstraintFactory')
make_head(_module, 'ISpeechRecognitionQualityDegradingEventArgs')
make_head(_module, 'ISpeechRecognitionResult')
make_head(_module, 'ISpeechRecognitionResult2')
make_head(_module, 'ISpeechRecognitionSemanticInterpretation')
make_head(_module, 'ISpeechRecognitionTopicConstraint')
make_head(_module, 'ISpeechRecognitionTopicConstraintFactory')
make_head(_module, 'ISpeechRecognitionVoiceCommandDefinitionConstraint')
make_head(_module, 'ISpeechRecognizer')
make_head(_module, 'ISpeechRecognizer2')
make_head(_module, 'ISpeechRecognizerFactory')
make_head(_module, 'ISpeechRecognizerStateChangedEventArgs')
make_head(_module, 'ISpeechRecognizerStatics')
make_head(_module, 'ISpeechRecognizerStatics2')
make_head(_module, 'ISpeechRecognizerTimeouts')
make_head(_module, 'ISpeechRecognizerUIOptions')
make_head(_module, 'IVoiceCommandManager')
make_head(_module, 'IVoiceCommandSet')
make_head(_module, 'SpeechContinuousRecognitionCompletedEventArgs')
make_head(_module, 'SpeechContinuousRecognitionResultGeneratedEventArgs')
make_head(_module, 'SpeechContinuousRecognitionSession')
make_head(_module, 'SpeechRecognitionCompilationResult')
make_head(_module, 'SpeechRecognitionGrammarFileConstraint')
make_head(_module, 'SpeechRecognitionHypothesis')
make_head(_module, 'SpeechRecognitionHypothesisGeneratedEventArgs')
make_head(_module, 'SpeechRecognitionListConstraint')
make_head(_module, 'SpeechRecognitionQualityDegradingEventArgs')
make_head(_module, 'SpeechRecognitionResult')
make_head(_module, 'SpeechRecognitionSemanticInterpretation')
make_head(_module, 'SpeechRecognitionTopicConstraint')
make_head(_module, 'SpeechRecognitionVoiceCommandDefinitionConstraint')
make_head(_module, 'SpeechRecognizer')
make_head(_module, 'SpeechRecognizerStateChangedEventArgs')
make_head(_module, 'SpeechRecognizerTimeouts')
make_head(_module, 'SpeechRecognizerUIOptions')
make_head(_module, 'VoiceCommandManager')
make_head(_module, 'VoiceCommandSet')
