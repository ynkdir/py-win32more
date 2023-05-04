from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Speech
import Windows.Win32.System.Com
import Windows.Win32.System.Com.Urlmon
import Windows.Win32.System.Registry
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
SPDUI_EngineProperties: String = 'EngineProperties'
SPDUI_AddRemoveWord: String = 'AddRemoveWord'
SPDUI_UserTraining: String = 'UserTraining'
SPDUI_MicTraining: String = 'MicTraining'
SPDUI_RecoProfileProperties: String = 'RecoProfileProperties'
SPDUI_AudioProperties: String = 'AudioProperties'
SPDUI_AudioVolume: String = 'AudioVolume'
SPDUI_UserEnrollment: String = 'UserEnrollment'
SPDUI_ShareData: String = 'ShareData'
SPDUI_Tutorial: String = 'Tutorial'
SPREG_USER_ROOT: String = 'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech'
SPREG_LOCAL_MACHINE_ROOT: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech'
SPCAT_AUDIOOUT: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioOutput'
SPCAT_AUDIOIN: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioInput'
SPCAT_VOICES: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices'
SPCAT_RECOGNIZERS: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Recognizers'
SPCAT_APPLEXICONS: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AppLexicons'
SPCAT_PHONECONVERTERS: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\PhoneConverters'
SPCAT_TEXTNORMALIZERS: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\TextNormalizers'
SPCAT_RECOPROFILES: String = 'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech\\RecoProfiles'
SPMMSYS_AUDIO_IN_TOKEN_ID: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioInput\\TokenEnums\\MMAudioIn\\'
SPMMSYS_AUDIO_OUT_TOKEN_ID: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioOutput\\TokenEnums\\MMAudioOut\\'
SPCURRENT_USER_LEXICON_TOKEN_ID: String = 'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech\\CurrentUserLexicon'
SPCURRENT_USER_SHORTCUT_TOKEN_ID: String = 'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech\\CurrentUserShortcut'
SPTOKENVALUE_CLSID: String = 'CLSID'
SPTOKENKEY_FILES: String = 'Files'
SPTOKENKEY_UI: String = 'UI'
SPTOKENKEY_ATTRIBUTES: String = 'Attributes'
SPTOKENKEY_RETAINEDAUDIO: String = 'SecondsPerRetainedAudioEvent'
SPTOKENKEY_AUDIO_LATENCY_WARNING: String = 'LatencyWarningThreshold'
SPTOKENKEY_AUDIO_LATENCY_TRUNCATE: String = 'LatencyTruncateThreshold'
SPTOKENKEY_AUDIO_LATENCY_UPDATE_INTERVAL: String = 'LatencyUpdateInterval'
SPVOICECATEGORY_TTSRATE: String = 'DefaultTTSRate'
SPPROP_RESOURCE_USAGE: String = 'ResourceUsage'
SPPROP_HIGH_CONFIDENCE_THRESHOLD: String = 'HighConfidenceThreshold'
SPPROP_NORMAL_CONFIDENCE_THRESHOLD: String = 'NormalConfidenceThreshold'
SPPROP_LOW_CONFIDENCE_THRESHOLD: String = 'LowConfidenceThreshold'
SPPROP_RESPONSE_SPEED: String = 'ResponseSpeed'
SPPROP_COMPLEX_RESPONSE_SPEED: String = 'ComplexResponseSpeed'
SPPROP_ADAPTATION_ON: String = 'AdaptationOn'
SPPROP_PERSISTED_BACKGROUND_ADAPTATION: String = 'PersistedBackgroundAdaptation'
SPPROP_PERSISTED_LANGUAGE_MODEL_ADAPTATION: String = 'PersistedLanguageModelAdaptation'
SPPROP_UX_IS_LISTENING: String = 'UXIsListening'
SPTOPIC_SPELLING: String = 'Spelling'
SPWILDCARD: String = '...'
SPDICTATION: String = '*'
SPINFDICTATION: String = '*+'
SPREG_SAFE_USER_TOKENS: String = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\UserTokens'
SP_LOW_CONFIDENCE: Int32 = -1
SP_NORMAL_CONFIDENCE: UInt32 = 0
DEFAULT_WEIGHT: UInt32 = 1
SP_MAX_WORD_LENGTH: UInt32 = 128
SP_MAX_PRON_LENGTH: UInt32 = 384
SP_EMULATE_RESULT: UInt32 = 1073741824
SP_STREAMPOS_ASAP: UInt32 = 0
SP_STREAMPOS_REALTIME: Int32 = -1
SPRP_NORMAL: UInt32 = 0
SP_MAX_LANGIDS: UInt32 = 20
SPRECOEXTENSION: String = 'RecoExtension'
SPALTERNATESCLSID: String = 'AlternatesCLSID'
SR_LOCALIZED_DESCRIPTION: String = 'Description'
SAPI_ERROR_BASE: UInt32 = 20480
Speech_Default_Weight: Single = 1
Speech_Max_Word_Length: Int32 = 128
Speech_Max_Pron_Length: Int32 = 384
Speech_StreamPos_Asap: Int32 = 0
Speech_StreamPos_RealTime: Int32 = -1
SpeechAllElements: Int32 = -1
DISPIDSPRG = Int32
DISPID_SRGId: DISPIDSPRG = 1
DISPID_SRGRecoContext: DISPIDSPRG = 2
DISPID_SRGState: DISPIDSPRG = 3
DISPID_SRGRules: DISPIDSPRG = 4
DISPID_SRGReset: DISPIDSPRG = 5
DISPID_SRGCommit: DISPIDSPRG = 6
DISPID_SRGCmdLoadFromFile: DISPIDSPRG = 7
DISPID_SRGCmdLoadFromObject: DISPIDSPRG = 8
DISPID_SRGCmdLoadFromResource: DISPIDSPRG = 9
DISPID_SRGCmdLoadFromMemory: DISPIDSPRG = 10
DISPID_SRGCmdLoadFromProprietaryGrammar: DISPIDSPRG = 11
DISPID_SRGCmdSetRuleState: DISPIDSPRG = 12
DISPID_SRGCmdSetRuleIdState: DISPIDSPRG = 13
DISPID_SRGDictationLoad: DISPIDSPRG = 14
DISPID_SRGDictationUnload: DISPIDSPRG = 15
DISPID_SRGDictationSetState: DISPIDSPRG = 16
DISPID_SRGSetWordSequenceData: DISPIDSPRG = 17
DISPID_SRGSetTextSelection: DISPIDSPRG = 18
DISPID_SRGIsPronounceable: DISPIDSPRG = 19
DISPIDSPTSI = Int32
DISPIDSPTSI_ActiveOffset: DISPIDSPTSI = 1
DISPIDSPTSI_ActiveLength: DISPIDSPTSI = 2
DISPIDSPTSI_SelectionOffset: DISPIDSPTSI = 3
DISPIDSPTSI_SelectionLength: DISPIDSPTSI = 4
DISPID_SpeechAudio = Int32
DISPID_SAStatus: DISPID_SpeechAudio = 200
DISPID_SABufferInfo: DISPID_SpeechAudio = 201
DISPID_SADefaultFormat: DISPID_SpeechAudio = 202
DISPID_SAVolume: DISPID_SpeechAudio = 203
DISPID_SABufferNotifySize: DISPID_SpeechAudio = 204
DISPID_SAEventHandle: DISPID_SpeechAudio = 205
DISPID_SASetState: DISPID_SpeechAudio = 206
DISPID_SpeechAudioBufferInfo = Int32
DISPID_SABIMinNotification: DISPID_SpeechAudioBufferInfo = 1
DISPID_SABIBufferSize: DISPID_SpeechAudioBufferInfo = 2
DISPID_SABIEventBias: DISPID_SpeechAudioBufferInfo = 3
DISPID_SpeechAudioFormat = Int32
DISPID_SAFType: DISPID_SpeechAudioFormat = 1
DISPID_SAFGuid: DISPID_SpeechAudioFormat = 2
DISPID_SAFGetWaveFormatEx: DISPID_SpeechAudioFormat = 3
DISPID_SAFSetWaveFormatEx: DISPID_SpeechAudioFormat = 4
DISPID_SpeechAudioStatus = Int32
DISPID_SASFreeBufferSpace: DISPID_SpeechAudioStatus = 1
DISPID_SASNonBlockingIO: DISPID_SpeechAudioStatus = 2
DISPID_SASState: DISPID_SpeechAudioStatus = 3
DISPID_SASCurrentSeekPosition: DISPID_SpeechAudioStatus = 4
DISPID_SASCurrentDevicePosition: DISPID_SpeechAudioStatus = 5
DISPID_SpeechBaseStream = Int32
DISPID_SBSFormat: DISPID_SpeechBaseStream = 1
DISPID_SBSRead: DISPID_SpeechBaseStream = 2
DISPID_SBSWrite: DISPID_SpeechBaseStream = 3
DISPID_SBSSeek: DISPID_SpeechBaseStream = 4
DISPID_SpeechCustomStream = Int32
DISPID_SCSBaseStream: DISPID_SpeechCustomStream = 100
DISPID_SpeechDataKey = Int32
DISPID_SDKSetBinaryValue: DISPID_SpeechDataKey = 1
DISPID_SDKGetBinaryValue: DISPID_SpeechDataKey = 2
DISPID_SDKSetStringValue: DISPID_SpeechDataKey = 3
DISPID_SDKGetStringValue: DISPID_SpeechDataKey = 4
DISPID_SDKSetLongValue: DISPID_SpeechDataKey = 5
DISPID_SDKGetlongValue: DISPID_SpeechDataKey = 6
DISPID_SDKOpenKey: DISPID_SpeechDataKey = 7
DISPID_SDKCreateKey: DISPID_SpeechDataKey = 8
DISPID_SDKDeleteKey: DISPID_SpeechDataKey = 9
DISPID_SDKDeleteValue: DISPID_SpeechDataKey = 10
DISPID_SDKEnumKeys: DISPID_SpeechDataKey = 11
DISPID_SDKEnumValues: DISPID_SpeechDataKey = 12
DISPID_SpeechFileStream = Int32
DISPID_SFSOpen: DISPID_SpeechFileStream = 100
DISPID_SFSClose: DISPID_SpeechFileStream = 101
DISPID_SpeechGrammarRule = Int32
DISPID_SGRAttributes: DISPID_SpeechGrammarRule = 1
DISPID_SGRInitialState: DISPID_SpeechGrammarRule = 2
DISPID_SGRName: DISPID_SpeechGrammarRule = 3
DISPID_SGRId: DISPID_SpeechGrammarRule = 4
DISPID_SGRClear: DISPID_SpeechGrammarRule = 5
DISPID_SGRAddResource: DISPID_SpeechGrammarRule = 6
DISPID_SGRAddState: DISPID_SpeechGrammarRule = 7
DISPID_SpeechGrammarRuleState = Int32
DISPID_SGRSRule: DISPID_SpeechGrammarRuleState = 1
DISPID_SGRSTransitions: DISPID_SpeechGrammarRuleState = 2
DISPID_SGRSAddWordTransition: DISPID_SpeechGrammarRuleState = 3
DISPID_SGRSAddRuleTransition: DISPID_SpeechGrammarRuleState = 4
DISPID_SGRSAddSpecialTransition: DISPID_SpeechGrammarRuleState = 5
DISPID_SpeechGrammarRuleStateTransition = Int32
DISPID_SGRSTType: DISPID_SpeechGrammarRuleStateTransition = 1
DISPID_SGRSTText: DISPID_SpeechGrammarRuleStateTransition = 2
DISPID_SGRSTRule: DISPID_SpeechGrammarRuleStateTransition = 3
DISPID_SGRSTWeight: DISPID_SpeechGrammarRuleStateTransition = 4
DISPID_SGRSTPropertyName: DISPID_SpeechGrammarRuleStateTransition = 5
DISPID_SGRSTPropertyId: DISPID_SpeechGrammarRuleStateTransition = 6
DISPID_SGRSTPropertyValue: DISPID_SpeechGrammarRuleStateTransition = 7
DISPID_SGRSTNextState: DISPID_SpeechGrammarRuleStateTransition = 8
DISPID_SpeechGrammarRuleStateTransitions = Int32
DISPID_SGRSTsCount: DISPID_SpeechGrammarRuleStateTransitions = 1
DISPID_SGRSTsItem: DISPID_SpeechGrammarRuleStateTransitions = 0
DISPID_SGRSTs_NewEnum: DISPID_SpeechGrammarRuleStateTransitions = -4
DISPID_SpeechGrammarRules = Int32
DISPID_SGRsCount: DISPID_SpeechGrammarRules = 1
DISPID_SGRsDynamic: DISPID_SpeechGrammarRules = 2
DISPID_SGRsAdd: DISPID_SpeechGrammarRules = 3
DISPID_SGRsCommit: DISPID_SpeechGrammarRules = 4
DISPID_SGRsCommitAndSave: DISPID_SpeechGrammarRules = 5
DISPID_SGRsFindRule: DISPID_SpeechGrammarRules = 6
DISPID_SGRsItem: DISPID_SpeechGrammarRules = 0
DISPID_SGRs_NewEnum: DISPID_SpeechGrammarRules = -4
DISPID_SpeechLexicon = Int32
DISPID_SLGenerationId: DISPID_SpeechLexicon = 1
DISPID_SLGetWords: DISPID_SpeechLexicon = 2
DISPID_SLAddPronunciation: DISPID_SpeechLexicon = 3
DISPID_SLAddPronunciationByPhoneIds: DISPID_SpeechLexicon = 4
DISPID_SLRemovePronunciation: DISPID_SpeechLexicon = 5
DISPID_SLRemovePronunciationByPhoneIds: DISPID_SpeechLexicon = 6
DISPID_SLGetPronunciations: DISPID_SpeechLexicon = 7
DISPID_SLGetGenerationChange: DISPID_SpeechLexicon = 8
DISPID_SpeechLexiconProns = Int32
DISPID_SLPsCount: DISPID_SpeechLexiconProns = 1
DISPID_SLPsItem: DISPID_SpeechLexiconProns = 0
DISPID_SLPs_NewEnum: DISPID_SpeechLexiconProns = -4
DISPID_SpeechLexiconPronunciation = Int32
DISPID_SLPType: DISPID_SpeechLexiconPronunciation = 1
DISPID_SLPLangId: DISPID_SpeechLexiconPronunciation = 2
DISPID_SLPPartOfSpeech: DISPID_SpeechLexiconPronunciation = 3
DISPID_SLPPhoneIds: DISPID_SpeechLexiconPronunciation = 4
DISPID_SLPSymbolic: DISPID_SpeechLexiconPronunciation = 5
DISPID_SpeechLexiconWord = Int32
DISPID_SLWLangId: DISPID_SpeechLexiconWord = 1
DISPID_SLWType: DISPID_SpeechLexiconWord = 2
DISPID_SLWWord: DISPID_SpeechLexiconWord = 3
DISPID_SLWPronunciations: DISPID_SpeechLexiconWord = 4
DISPID_SpeechLexiconWords = Int32
DISPID_SLWsCount: DISPID_SpeechLexiconWords = 1
DISPID_SLWsItem: DISPID_SpeechLexiconWords = 0
DISPID_SLWs_NewEnum: DISPID_SpeechLexiconWords = -4
DISPID_SpeechMMSysAudio = Int32
DISPID_SMSADeviceId: DISPID_SpeechMMSysAudio = 300
DISPID_SMSALineId: DISPID_SpeechMMSysAudio = 301
DISPID_SMSAMMHandle: DISPID_SpeechMMSysAudio = 302
DISPID_SpeechMemoryStream = Int32
DISPID_SMSSetData: DISPID_SpeechMemoryStream = 100
DISPID_SMSGetData: DISPID_SpeechMemoryStream = 101
DISPID_SpeechObjectToken = Int32
DISPID_SOTId: DISPID_SpeechObjectToken = 1
DISPID_SOTDataKey: DISPID_SpeechObjectToken = 2
DISPID_SOTCategory: DISPID_SpeechObjectToken = 3
DISPID_SOTGetDescription: DISPID_SpeechObjectToken = 4
DISPID_SOTSetId: DISPID_SpeechObjectToken = 5
DISPID_SOTGetAttribute: DISPID_SpeechObjectToken = 6
DISPID_SOTCreateInstance: DISPID_SpeechObjectToken = 7
DISPID_SOTRemove: DISPID_SpeechObjectToken = 8
DISPID_SOTGetStorageFileName: DISPID_SpeechObjectToken = 9
DISPID_SOTRemoveStorageFileName: DISPID_SpeechObjectToken = 10
DISPID_SOTIsUISupported: DISPID_SpeechObjectToken = 11
DISPID_SOTDisplayUI: DISPID_SpeechObjectToken = 12
DISPID_SOTMatchesAttributes: DISPID_SpeechObjectToken = 13
DISPID_SpeechObjectTokenCategory = Int32
DISPID_SOTCId: DISPID_SpeechObjectTokenCategory = 1
DISPID_SOTCDefault: DISPID_SpeechObjectTokenCategory = 2
DISPID_SOTCSetId: DISPID_SpeechObjectTokenCategory = 3
DISPID_SOTCGetDataKey: DISPID_SpeechObjectTokenCategory = 4
DISPID_SOTCEnumerateTokens: DISPID_SpeechObjectTokenCategory = 5
DISPID_SpeechObjectTokens = Int32
DISPID_SOTsCount: DISPID_SpeechObjectTokens = 1
DISPID_SOTsItem: DISPID_SpeechObjectTokens = 0
DISPID_SOTs_NewEnum: DISPID_SpeechObjectTokens = -4
DISPID_SpeechPhoneConverter = Int32
DISPID_SPCLangId: DISPID_SpeechPhoneConverter = 1
DISPID_SPCPhoneToId: DISPID_SpeechPhoneConverter = 2
DISPID_SPCIdToPhone: DISPID_SpeechPhoneConverter = 3
DISPID_SpeechPhraseAlternate = Int32
DISPID_SPARecoResult: DISPID_SpeechPhraseAlternate = 1
DISPID_SPAStartElementInResult: DISPID_SpeechPhraseAlternate = 2
DISPID_SPANumberOfElementsInResult: DISPID_SpeechPhraseAlternate = 3
DISPID_SPAPhraseInfo: DISPID_SpeechPhraseAlternate = 4
DISPID_SPACommit: DISPID_SpeechPhraseAlternate = 5
DISPID_SpeechPhraseAlternates = Int32
DISPID_SPAsCount: DISPID_SpeechPhraseAlternates = 1
DISPID_SPAsItem: DISPID_SpeechPhraseAlternates = 0
DISPID_SPAs_NewEnum: DISPID_SpeechPhraseAlternates = -4
DISPID_SpeechPhraseBuilder = Int32
DISPID_SPPBRestorePhraseFromMemory: DISPID_SpeechPhraseBuilder = 1
DISPID_SpeechPhraseElement = Int32
DISPID_SPEAudioTimeOffset: DISPID_SpeechPhraseElement = 1
DISPID_SPEAudioSizeTime: DISPID_SpeechPhraseElement = 2
DISPID_SPEAudioStreamOffset: DISPID_SpeechPhraseElement = 3
DISPID_SPEAudioSizeBytes: DISPID_SpeechPhraseElement = 4
DISPID_SPERetainedStreamOffset: DISPID_SpeechPhraseElement = 5
DISPID_SPERetainedSizeBytes: DISPID_SpeechPhraseElement = 6
DISPID_SPEDisplayText: DISPID_SpeechPhraseElement = 7
DISPID_SPELexicalForm: DISPID_SpeechPhraseElement = 8
DISPID_SPEPronunciation: DISPID_SpeechPhraseElement = 9
DISPID_SPEDisplayAttributes: DISPID_SpeechPhraseElement = 10
DISPID_SPERequiredConfidence: DISPID_SpeechPhraseElement = 11
DISPID_SPEActualConfidence: DISPID_SpeechPhraseElement = 12
DISPID_SPEEngineConfidence: DISPID_SpeechPhraseElement = 13
DISPID_SpeechPhraseElements = Int32
DISPID_SPEsCount: DISPID_SpeechPhraseElements = 1
DISPID_SPEsItem: DISPID_SpeechPhraseElements = 0
DISPID_SPEs_NewEnum: DISPID_SpeechPhraseElements = -4
DISPID_SpeechPhraseInfo = Int32
DISPID_SPILanguageId: DISPID_SpeechPhraseInfo = 1
DISPID_SPIGrammarId: DISPID_SpeechPhraseInfo = 2
DISPID_SPIStartTime: DISPID_SpeechPhraseInfo = 3
DISPID_SPIAudioStreamPosition: DISPID_SpeechPhraseInfo = 4
DISPID_SPIAudioSizeBytes: DISPID_SpeechPhraseInfo = 5
DISPID_SPIRetainedSizeBytes: DISPID_SpeechPhraseInfo = 6
DISPID_SPIAudioSizeTime: DISPID_SpeechPhraseInfo = 7
DISPID_SPIRule: DISPID_SpeechPhraseInfo = 8
DISPID_SPIProperties: DISPID_SpeechPhraseInfo = 9
DISPID_SPIElements: DISPID_SpeechPhraseInfo = 10
DISPID_SPIReplacements: DISPID_SpeechPhraseInfo = 11
DISPID_SPIEngineId: DISPID_SpeechPhraseInfo = 12
DISPID_SPIEnginePrivateData: DISPID_SpeechPhraseInfo = 13
DISPID_SPISaveToMemory: DISPID_SpeechPhraseInfo = 14
DISPID_SPIGetText: DISPID_SpeechPhraseInfo = 15
DISPID_SPIGetDisplayAttributes: DISPID_SpeechPhraseInfo = 16
DISPID_SpeechPhraseProperties = Int32
DISPID_SPPsCount: DISPID_SpeechPhraseProperties = 1
DISPID_SPPsItem: DISPID_SpeechPhraseProperties = 0
DISPID_SPPs_NewEnum: DISPID_SpeechPhraseProperties = -4
DISPID_SpeechPhraseProperty = Int32
DISPID_SPPName: DISPID_SpeechPhraseProperty = 1
DISPID_SPPId: DISPID_SpeechPhraseProperty = 2
DISPID_SPPValue: DISPID_SpeechPhraseProperty = 3
DISPID_SPPFirstElement: DISPID_SpeechPhraseProperty = 4
DISPID_SPPNumberOfElements: DISPID_SpeechPhraseProperty = 5
DISPID_SPPEngineConfidence: DISPID_SpeechPhraseProperty = 6
DISPID_SPPConfidence: DISPID_SpeechPhraseProperty = 7
DISPID_SPPParent: DISPID_SpeechPhraseProperty = 8
DISPID_SPPChildren: DISPID_SpeechPhraseProperty = 9
DISPID_SpeechPhraseReplacement = Int32
DISPID_SPRDisplayAttributes: DISPID_SpeechPhraseReplacement = 1
DISPID_SPRText: DISPID_SpeechPhraseReplacement = 2
DISPID_SPRFirstElement: DISPID_SpeechPhraseReplacement = 3
DISPID_SPRNumberOfElements: DISPID_SpeechPhraseReplacement = 4
DISPID_SpeechPhraseReplacements = Int32
DISPID_SPRsCount: DISPID_SpeechPhraseReplacements = 1
DISPID_SPRsItem: DISPID_SpeechPhraseReplacements = 0
DISPID_SPRs_NewEnum: DISPID_SpeechPhraseReplacements = -4
DISPID_SpeechPhraseRule = Int32
DISPID_SPRuleName: DISPID_SpeechPhraseRule = 1
DISPID_SPRuleId: DISPID_SpeechPhraseRule = 2
DISPID_SPRuleFirstElement: DISPID_SpeechPhraseRule = 3
DISPID_SPRuleNumberOfElements: DISPID_SpeechPhraseRule = 4
DISPID_SPRuleParent: DISPID_SpeechPhraseRule = 5
DISPID_SPRuleChildren: DISPID_SpeechPhraseRule = 6
DISPID_SPRuleConfidence: DISPID_SpeechPhraseRule = 7
DISPID_SPRuleEngineConfidence: DISPID_SpeechPhraseRule = 8
DISPID_SpeechPhraseRules = Int32
DISPID_SPRulesCount: DISPID_SpeechPhraseRules = 1
DISPID_SPRulesItem: DISPID_SpeechPhraseRules = 0
DISPID_SPRules_NewEnum: DISPID_SpeechPhraseRules = -4
DISPID_SpeechRecoContext = Int32
DISPID_SRCRecognizer: DISPID_SpeechRecoContext = 1
DISPID_SRCAudioInInterferenceStatus: DISPID_SpeechRecoContext = 2
DISPID_SRCRequestedUIType: DISPID_SpeechRecoContext = 3
DISPID_SRCVoice: DISPID_SpeechRecoContext = 4
DISPID_SRAllowVoiceFormatMatchingOnNextSet: DISPID_SpeechRecoContext = 5
DISPID_SRCVoicePurgeEvent: DISPID_SpeechRecoContext = 6
DISPID_SRCEventInterests: DISPID_SpeechRecoContext = 7
DISPID_SRCCmdMaxAlternates: DISPID_SpeechRecoContext = 8
DISPID_SRCState: DISPID_SpeechRecoContext = 9
DISPID_SRCRetainedAudio: DISPID_SpeechRecoContext = 10
DISPID_SRCRetainedAudioFormat: DISPID_SpeechRecoContext = 11
DISPID_SRCPause: DISPID_SpeechRecoContext = 12
DISPID_SRCResume: DISPID_SpeechRecoContext = 13
DISPID_SRCCreateGrammar: DISPID_SpeechRecoContext = 14
DISPID_SRCCreateResultFromMemory: DISPID_SpeechRecoContext = 15
DISPID_SRCBookmark: DISPID_SpeechRecoContext = 16
DISPID_SRCSetAdaptationData: DISPID_SpeechRecoContext = 17
DISPID_SpeechRecoContextEvents = Int32
DISPID_SRCEStartStream: DISPID_SpeechRecoContextEvents = 1
DISPID_SRCEEndStream: DISPID_SpeechRecoContextEvents = 2
DISPID_SRCEBookmark: DISPID_SpeechRecoContextEvents = 3
DISPID_SRCESoundStart: DISPID_SpeechRecoContextEvents = 4
DISPID_SRCESoundEnd: DISPID_SpeechRecoContextEvents = 5
DISPID_SRCEPhraseStart: DISPID_SpeechRecoContextEvents = 6
DISPID_SRCERecognition: DISPID_SpeechRecoContextEvents = 7
DISPID_SRCEHypothesis: DISPID_SpeechRecoContextEvents = 8
DISPID_SRCEPropertyNumberChange: DISPID_SpeechRecoContextEvents = 9
DISPID_SRCEPropertyStringChange: DISPID_SpeechRecoContextEvents = 10
DISPID_SRCEFalseRecognition: DISPID_SpeechRecoContextEvents = 11
DISPID_SRCEInterference: DISPID_SpeechRecoContextEvents = 12
DISPID_SRCERequestUI: DISPID_SpeechRecoContextEvents = 13
DISPID_SRCERecognizerStateChange: DISPID_SpeechRecoContextEvents = 14
DISPID_SRCEAdaptation: DISPID_SpeechRecoContextEvents = 15
DISPID_SRCERecognitionForOtherContext: DISPID_SpeechRecoContextEvents = 16
DISPID_SRCEAudioLevel: DISPID_SpeechRecoContextEvents = 17
DISPID_SRCEEnginePrivate: DISPID_SpeechRecoContextEvents = 18
DISPID_SpeechRecoResult = Int32
DISPID_SRRRecoContext: DISPID_SpeechRecoResult = 1
DISPID_SRRTimes: DISPID_SpeechRecoResult = 2
DISPID_SRRAudioFormat: DISPID_SpeechRecoResult = 3
DISPID_SRRPhraseInfo: DISPID_SpeechRecoResult = 4
DISPID_SRRAlternates: DISPID_SpeechRecoResult = 5
DISPID_SRRAudio: DISPID_SpeechRecoResult = 6
DISPID_SRRSpeakAudio: DISPID_SpeechRecoResult = 7
DISPID_SRRSaveToMemory: DISPID_SpeechRecoResult = 8
DISPID_SRRDiscardResultInfo: DISPID_SpeechRecoResult = 9
DISPID_SpeechRecoResult2 = Int32
DISPID_SRRSetTextFeedback: DISPID_SpeechRecoResult2 = 12
DISPID_SpeechRecoResultTimes = Int32
DISPID_SRRTStreamTime: DISPID_SpeechRecoResultTimes = 1
DISPID_SRRTLength: DISPID_SpeechRecoResultTimes = 2
DISPID_SRRTTickCount: DISPID_SpeechRecoResultTimes = 3
DISPID_SRRTOffsetFromStart: DISPID_SpeechRecoResultTimes = 4
DISPID_SpeechRecognizer = Int32
DISPID_SRRecognizer: DISPID_SpeechRecognizer = 1
DISPID_SRAllowAudioInputFormatChangesOnNextSet: DISPID_SpeechRecognizer = 2
DISPID_SRAudioInput: DISPID_SpeechRecognizer = 3
DISPID_SRAudioInputStream: DISPID_SpeechRecognizer = 4
DISPID_SRIsShared: DISPID_SpeechRecognizer = 5
DISPID_SRState: DISPID_SpeechRecognizer = 6
DISPID_SRStatus: DISPID_SpeechRecognizer = 7
DISPID_SRProfile: DISPID_SpeechRecognizer = 8
DISPID_SREmulateRecognition: DISPID_SpeechRecognizer = 9
DISPID_SRCreateRecoContext: DISPID_SpeechRecognizer = 10
DISPID_SRGetFormat: DISPID_SpeechRecognizer = 11
DISPID_SRSetPropertyNumber: DISPID_SpeechRecognizer = 12
DISPID_SRGetPropertyNumber: DISPID_SpeechRecognizer = 13
DISPID_SRSetPropertyString: DISPID_SpeechRecognizer = 14
DISPID_SRGetPropertyString: DISPID_SpeechRecognizer = 15
DISPID_SRIsUISupported: DISPID_SpeechRecognizer = 16
DISPID_SRDisplayUI: DISPID_SpeechRecognizer = 17
DISPID_SRGetRecognizers: DISPID_SpeechRecognizer = 18
DISPID_SVGetAudioInputs: DISPID_SpeechRecognizer = 19
DISPID_SVGetProfiles: DISPID_SpeechRecognizer = 20
DISPID_SpeechRecognizerStatus = Int32
DISPID_SRSAudioStatus: DISPID_SpeechRecognizerStatus = 1
DISPID_SRSCurrentStreamPosition: DISPID_SpeechRecognizerStatus = 2
DISPID_SRSCurrentStreamNumber: DISPID_SpeechRecognizerStatus = 3
DISPID_SRSNumberOfActiveRules: DISPID_SpeechRecognizerStatus = 4
DISPID_SRSClsidEngine: DISPID_SpeechRecognizerStatus = 5
DISPID_SRSSupportedLanguages: DISPID_SpeechRecognizerStatus = 6
DISPID_SpeechVoice = Int32
DISPID_SVStatus: DISPID_SpeechVoice = 1
DISPID_SVVoice: DISPID_SpeechVoice = 2
DISPID_SVAudioOutput: DISPID_SpeechVoice = 3
DISPID_SVAudioOutputStream: DISPID_SpeechVoice = 4
DISPID_SVRate: DISPID_SpeechVoice = 5
DISPID_SVVolume: DISPID_SpeechVoice = 6
DISPID_SVAllowAudioOuputFormatChangesOnNextSet: DISPID_SpeechVoice = 7
DISPID_SVEventInterests: DISPID_SpeechVoice = 8
DISPID_SVPriority: DISPID_SpeechVoice = 9
DISPID_SVAlertBoundary: DISPID_SpeechVoice = 10
DISPID_SVSyncronousSpeakTimeout: DISPID_SpeechVoice = 11
DISPID_SVSpeak: DISPID_SpeechVoice = 12
DISPID_SVSpeakStream: DISPID_SpeechVoice = 13
DISPID_SVPause: DISPID_SpeechVoice = 14
DISPID_SVResume: DISPID_SpeechVoice = 15
DISPID_SVSkip: DISPID_SpeechVoice = 16
DISPID_SVGetVoices: DISPID_SpeechVoice = 17
DISPID_SVGetAudioOutputs: DISPID_SpeechVoice = 18
DISPID_SVWaitUntilDone: DISPID_SpeechVoice = 19
DISPID_SVSpeakCompleteEvent: DISPID_SpeechVoice = 20
DISPID_SVIsUISupported: DISPID_SpeechVoice = 21
DISPID_SVDisplayUI: DISPID_SpeechVoice = 22
DISPID_SpeechVoiceEvent = Int32
DISPID_SVEStreamStart: DISPID_SpeechVoiceEvent = 1
DISPID_SVEStreamEnd: DISPID_SpeechVoiceEvent = 2
DISPID_SVEVoiceChange: DISPID_SpeechVoiceEvent = 3
DISPID_SVEBookmark: DISPID_SpeechVoiceEvent = 4
DISPID_SVEWord: DISPID_SpeechVoiceEvent = 5
DISPID_SVEPhoneme: DISPID_SpeechVoiceEvent = 6
DISPID_SVESentenceBoundary: DISPID_SpeechVoiceEvent = 7
DISPID_SVEViseme: DISPID_SpeechVoiceEvent = 8
DISPID_SVEAudioLevel: DISPID_SpeechVoiceEvent = 9
DISPID_SVEEnginePrivate: DISPID_SpeechVoiceEvent = 10
DISPID_SpeechVoiceStatus = Int32
DISPID_SVSCurrentStreamNumber: DISPID_SpeechVoiceStatus = 1
DISPID_SVSLastStreamNumberQueued: DISPID_SpeechVoiceStatus = 2
DISPID_SVSLastResult: DISPID_SpeechVoiceStatus = 3
DISPID_SVSRunningState: DISPID_SpeechVoiceStatus = 4
DISPID_SVSInputWordPosition: DISPID_SpeechVoiceStatus = 5
DISPID_SVSInputWordLength: DISPID_SpeechVoiceStatus = 6
DISPID_SVSInputSentencePosition: DISPID_SpeechVoiceStatus = 7
DISPID_SVSInputSentenceLength: DISPID_SpeechVoiceStatus = 8
DISPID_SVSLastBookmark: DISPID_SpeechVoiceStatus = 9
DISPID_SVSLastBookmarkId: DISPID_SpeechVoiceStatus = 10
DISPID_SVSPhonemeId: DISPID_SpeechVoiceStatus = 11
DISPID_SVSVisemeId: DISPID_SpeechVoiceStatus = 12
DISPID_SpeechWaveFormatEx = Int32
DISPID_SWFEFormatTag: DISPID_SpeechWaveFormatEx = 1
DISPID_SWFEChannels: DISPID_SpeechWaveFormatEx = 2
DISPID_SWFESamplesPerSec: DISPID_SpeechWaveFormatEx = 3
DISPID_SWFEAvgBytesPerSec: DISPID_SpeechWaveFormatEx = 4
DISPID_SWFEBlockAlign: DISPID_SpeechWaveFormatEx = 5
DISPID_SWFEBitsPerSample: DISPID_SpeechWaveFormatEx = 6
DISPID_SWFEExtraData: DISPID_SpeechWaveFormatEx = 7
DISPID_SpeechXMLRecoResult = Int32
DISPID_SRRGetXMLResult: DISPID_SpeechXMLRecoResult = 10
DISPID_SRRGetXMLErrorInfo: DISPID_SpeechXMLRecoResult = 11
class IEnumSpObjectTokens(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{06b64f9e-7fda-11d2-b4f2-00c04f797396}')
    @commethod(3)
    def Next(self, celt: UInt32, pelt: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.Media.Speech.IEnumSpObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Item(self, Index: UInt32, ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpAudio(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpStreamFormat
    _iid_ = Guid('{c05c768f-fae8-4ec2-8e07-338321c12452}')
    @commethod(15)
    def SetState(self, NewState: Windows.Win32.Media.Speech.SPAUDIOSTATE, ullReserved: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetFormat(self, rguidFmtId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStatus(self, pStatus: POINTER(Windows.Win32.Media.Speech.SPAUDIOSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetBufferInfo(self, pBuffInfo: POINTER(Windows.Win32.Media.Speech.SPAUDIOBUFFERINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetBufferInfo(self, pBuffInfo: POINTER(Windows.Win32.Media.Speech.SPAUDIOBUFFERINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultFormat(self, pFormatId: POINTER(Guid), ppCoMemWaveFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EventHandle(self) -> Windows.Win32.Foundation.HANDLE: ...
    @commethod(22)
    def GetVolumeLevel(self, pLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetVolumeLevel(self, Level: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBufferNotifySize(self, pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetBufferNotifySize(self, cbSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpContainerLexicon(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpLexicon
    _iid_ = Guid('{8565572f-c094-41cc-b56e-10bd9c3ff044}')
    @commethod(9)
    def AddLexicon(self, pAddLexicon: Windows.Win32.Media.Speech.ISpLexicon_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpDataKey(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{14056581-e16c-11d2-bb90-00c04f8ee6c0}')
    @commethod(3)
    def SetData(self, pszValueName: Windows.Win32.Foundation.PWSTR, cbData: UInt32, pData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetData(self, pszValueName: Windows.Win32.Foundation.PWSTR, pcbData: POINTER(UInt32), pData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStringValue(self, pszValueName: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringValue(self, pszValueName: Windows.Win32.Foundation.PWSTR, ppszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDWORD(self, pszValueName: Windows.Win32.Foundation.PWSTR, dwValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDWORD(self, pszValueName: Windows.Win32.Foundation.PWSTR, pdwValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OpenKey(self, pszSubKeyName: Windows.Win32.Foundation.PWSTR, ppSubKey: POINTER(Windows.Win32.Media.Speech.ISpDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateKey(self, pszSubKey: Windows.Win32.Foundation.PWSTR, ppSubKey: POINTER(Windows.Win32.Media.Speech.ISpDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteKey(self, pszSubKey: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteValue(self, pszValueName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnumKeys(self, Index: UInt32, ppszSubKeyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumValues(self, Index: UInt32, ppszValueName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpDisplayAlternates(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8d7c7e2-0dde-44b7-afe3-b0c991fbeb5e}')
    @commethod(3)
    def GetDisplayAlternates(self, pPhrase: POINTER(Windows.Win32.Media.Speech.SPDISPLAYPHRASE_head), cRequestCount: UInt32, ppCoMemPhrases: POINTER(POINTER(Windows.Win32.Media.Speech.SPDISPLAYPHRASE_head)), pcPhrasesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFullStopTrailSpace(self, ulTrailSpace: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEnginePronunciation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c360ce4b-76d1-4214-ad68-52657d5083da}')
    @commethod(3)
    def Normalize(self, pszWord: Windows.Win32.Foundation.PWSTR, pszLeftContext: Windows.Win32.Foundation.PWSTR, pszRightContext: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pNormalizationList: POINTER(Windows.Win32.Media.Speech.SPNORMALIZATIONLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPronunciations(self, pszWord: Windows.Win32.Foundation.PWSTR, pszLeftContext: Windows.Win32.Foundation.PWSTR, pszRightContext: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pEnginePronunciationList: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATIONLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEventSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{be7a9cc9-5f9e-11d2-960f-00c04f8ee628}')
    @commethod(3)
    def AddEvents(self, pEventArray: POINTER(Windows.Win32.Media.Speech.SPEVENT_head), ulCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEventInterest(self, pullEventInterest: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEventSource(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpNotifySource
    _iid_ = Guid('{be7a9cce-5f9e-11d2-960f-00c04f8ee628}')
    @commethod(10)
    def SetInterest(self, ullEventInterest: UInt64, ullQueuedInterest: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEvents(self, ulCount: UInt32, pEventArray: POINTER(Windows.Win32.Media.Speech.SPEVENT_head), pulFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInfo(self, pInfo: POINTER(Windows.Win32.Media.Speech.SPEVENTSOURCEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEventSource2(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpEventSource
    _iid_ = Guid('{2373a435-6a4b-429e-a6ac-d4231a61975b}')
    @commethod(13)
    def GetEventsEx(self, ulCount: UInt32, pEventArray: POINTER(Windows.Win32.Media.Speech.SPEVENTEX_head), pulFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpGrammarBuilder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8137828f-591a-4a42-be58-49ea7ebaac68}')
    @commethod(3)
    def ResetGrammar(self, NewLanguage: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRule(self, pszRuleName: Windows.Win32.Foundation.PWSTR, dwRuleId: UInt32, dwAttributes: UInt32, fCreateIfNotExist: Windows.Win32.Foundation.BOOL, phInitialState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearRule(self, hState: Windows.Win32.Media.Speech.SPSTATEHANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateNewState(self, hState: Windows.Win32.Media.Speech.SPSTATEHANDLE, phState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddWordTransition(self, hFromState: Windows.Win32.Media.Speech.SPSTATEHANDLE, hToState: Windows.Win32.Media.Speech.SPSTATEHANDLE, psz: Windows.Win32.Foundation.PWSTR, pszSeparators: Windows.Win32.Foundation.PWSTR, eWordType: Windows.Win32.Media.Speech.SPGRAMMARWORDTYPE, Weight: Single, pPropInfo: POINTER(Windows.Win32.Media.Speech.SPPROPERTYINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddRuleTransition(self, hFromState: Windows.Win32.Media.Speech.SPSTATEHANDLE, hToState: Windows.Win32.Media.Speech.SPSTATEHANDLE, hRule: Windows.Win32.Media.Speech.SPSTATEHANDLE, Weight: Single, pPropInfo: POINTER(Windows.Win32.Media.Speech.SPPROPERTYINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddResource(self, hRuleState: Windows.Win32.Media.Speech.SPSTATEHANDLE, pszResourceName: Windows.Win32.Foundation.PWSTR, pszResourceValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Commit(self, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpGrammarBuilder2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ab10026-20cc-4b20-8c22-a49c9ba78f60}')
    @commethod(3)
    def AddTextSubset(self, hFromState: Windows.Win32.Media.Speech.SPSTATEHANDLE, hToState: Windows.Win32.Media.Speech.SPSTATEHANDLE, psz: Windows.Win32.Foundation.PWSTR, eMatchMode: Windows.Win32.Media.Speech.SPMATCHINGMODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPhoneticAlphabet(self, phoneticALphabet: Windows.Win32.Media.Speech.PHONETICALPHABET) -> Windows.Win32.Foundation.HRESULT: ...
class ISpLexicon(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{da41a7c2-5383-4db2-916b-6c1719e3db58}')
    @commethod(3)
    def GetPronunciations(self, pszWord: Windows.Win32.Foundation.PWSTR, LangID: UInt16, dwFlags: UInt32, pWordPronunciationList: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATIONLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPronunciation(self, pszWord: Windows.Win32.Foundation.PWSTR, LangID: UInt16, ePartOfSpeech: Windows.Win32.Media.Speech.SPPARTOFSPEECH, pszPronunciation: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemovePronunciation(self, pszWord: Windows.Win32.Foundation.PWSTR, LangID: UInt16, ePartOfSpeech: Windows.Win32.Media.Speech.SPPARTOFSPEECH, pszPronunciation: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGeneration(self, pdwGeneration: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGenerationChange(self, dwFlags: UInt32, pdwGeneration: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(self, dwFlags: UInt32, pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpMMSysAudio(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpAudio
    _iid_ = Guid('{15806f6e-1d70-4b48-98e6-3b1a007509ab}')
    @commethod(26)
    def GetDeviceId(self, puDeviceId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetDeviceId(self, uDeviceId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetMMHandle(self, pHandle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetLineId(self, puLineId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetLineId(self, uLineId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpNotifyCallback(ComPtr):
    extends: None
    @commethod(0)
    def NotifyCallback(self, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class ISpNotifySink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{259684dc-37c3-11d2-9603-00c04f8ee628}')
    @commethod(3)
    def Notify(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpNotifySource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5eff4aef-8487-11d2-961c-00c04f8ee628}')
    @commethod(3)
    def SetNotifySink(self, pNotifySink: Windows.Win32.Media.Speech.ISpNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNotifyWindowMessage(self, hWnd: Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNotifyCallbackFunction(self, pfnCallback: POINTER(Windows.Win32.Media.Speech.SPNOTIFYCALLBACK), wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetNotifyCallbackInterface(self, pSpCallback: Windows.Win32.Media.Speech.ISpNotifyCallback_head, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetNotifyWin32Event(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WaitForNotifyEvent(self, dwMilliseconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNotifyEventHandle(self) -> Windows.Win32.Foundation.HANDLE: ...
class ISpNotifyTranslator(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpNotifySink
    _iid_ = Guid('{aca16614-5d3d-11d2-960e-00c04f8ee628}')
    @commethod(4)
    def InitWindowMessage(self, hWnd: Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitCallback(self, pfnCallback: POINTER(Windows.Win32.Media.Speech.SPNOTIFYCALLBACK), wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitSpNotifyCallback(self, pSpCallback: Windows.Win32.Media.Speech.ISpNotifyCallback_head, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InitWin32Event(self, hEvent: Windows.Win32.Foundation.HANDLE, fCloseHandleOnRelease: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Wait(self, dwMilliseconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEventHandle(self) -> Windows.Win32.Foundation.HANDLE: ...
class ISpObjectToken(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpDataKey
    _iid_ = Guid('{14056589-e16c-11d2-bb90-00c04f8ee6c0}')
    @commethod(15)
    def SetId(self, pszCategoryId: Windows.Win32.Foundation.PWSTR, pszTokenId: Windows.Win32.Foundation.PWSTR, fCreateIfNotExist: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetId(self, ppszCoMemTokenId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCategory(self, ppTokenCategory: POINTER(Windows.Win32.Media.Speech.ISpObjectTokenCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateInstance(self, pUnkOuter: Windows.Win32.System.Com.IUnknown_head, dwClsContext: UInt32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetStorageFileName(self, clsidCaller: POINTER(Guid), pszValueName: Windows.Win32.Foundation.PWSTR, pszFileNameSpecifier: Windows.Win32.Foundation.PWSTR, nFolder: UInt32, ppszFilePath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RemoveStorageFileName(self, clsidCaller: POINTER(Guid), pszKeyName: Windows.Win32.Foundation.PWSTR, fDeleteFile: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Remove(self, pclsidCaller: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsUISupported(self, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, punkObject: Windows.Win32.System.Com.IUnknown_head, pfSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DisplayUI(self, hwndParent: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, punkObject: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def MatchesAttributes(self, pszAttributes: Windows.Win32.Foundation.PWSTR, pfMatches: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpObjectTokenCategory(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpDataKey
    _iid_ = Guid('{2d3d3845-39af-4850-bbf9-40b49780011d}')
    @commethod(15)
    def SetId(self, pszCategoryId: Windows.Win32.Foundation.PWSTR, fCreateIfNotExist: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetId(self, ppszCoMemCategoryId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDataKey(self, spdkl: Windows.Win32.Media.Speech.SPDATAKEYLOCATION, ppDataKey: POINTER(Windows.Win32.Media.Speech.ISpDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumTokens(self, pzsReqAttribs: Windows.Win32.Foundation.PWSTR, pszOptAttribs: Windows.Win32.Foundation.PWSTR, ppEnum: POINTER(Windows.Win32.Media.Speech.IEnumSpObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDefaultTokenId(self, pszTokenId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultTokenId(self, ppszCoMemTokenId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpObjectTokenInit(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpObjectToken
    _iid_ = Guid('{b8aab0cf-346f-49d8-9499-c8b03f161d51}')
    @commethod(25)
    def InitFromDataKey(self, pszCategoryId: Windows.Win32.Foundation.PWSTR, pszTokenId: Windows.Win32.Foundation.PWSTR, pDataKey: Windows.Win32.Media.Speech.ISpDataKey_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpObjectWithToken(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b559f40-e952-11d2-bb91-00c04f8ee6c0}')
    @commethod(3)
    def SetObjectToken(self, pToken: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectToken(self, ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneConverter(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpObjectWithToken
    _iid_ = Guid('{8445c581-0cac-4a38-abfe-9b2ce2826455}')
    @commethod(5)
    def PhoneToId(self, pszPhone: Windows.Win32.Foundation.PWSTR, pId: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IdToPhone(self, pId: POINTER(UInt16), pszPhone: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneticAlphabetConverter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{133adcd4-19b4-4020-9fdc-842e78253b17}')
    @commethod(3)
    def GetLangId(self, pLangID: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLangId(self, LangID: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SAPI2UPS(self, pszSAPIId: POINTER(UInt16), pszUPSId: POINTER(UInt16), cMaxLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UPS2SAPI(self, pszUPSId: POINTER(UInt16), pszSAPIId: POINTER(UInt16), cMaxLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxConvertLength(self, cSrcLength: UInt32, bSAPI2UPS: Windows.Win32.Foundation.BOOL, pcMaxDestLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneticAlphabetSelection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b2745efd-42ce-48ca-81f1-a96e02538a90}')
    @commethod(3)
    def IsAlphabetUPS(self, pfIsUPS: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAlphabetToUPS(self, fForceUPS: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhrase(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a5c0354-b621-4b5a-8791-d306ed379e53}')
    @commethod(3)
    def GetPhrase(self, ppCoMemPhrase: POINTER(POINTER(Windows.Win32.Media.Speech.SPPHRASE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSerializedPhrase(self, ppCoMemPhrase: POINTER(POINTER(Windows.Win32.Media.Speech.SPSERIALIZEDPHRASE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetText(self, ulStart: UInt32, ulCount: UInt32, fUseTextReplacements: Windows.Win32.Foundation.BOOL, ppszCoMemText: POINTER(Windows.Win32.Foundation.PWSTR), pbDisplayAttributes: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Discard(self, dwValueTypes: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhrase2(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpPhrase
    _iid_ = Guid('{f264da52-e457-4696-b856-a737b717af79}')
    @commethod(7)
    def GetXMLResult(self, ppszCoMemXMLResult: POINTER(Windows.Win32.Foundation.PWSTR), Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetXMLErrorInfo(self, pSemanticErrorInfo: POINTER(Windows.Win32.Media.Speech.SPSEMANTICERRORINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAudio(self, ulStartElement: UInt32, cElements: UInt32, ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhraseAlt(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpPhrase
    _iid_ = Guid('{8fcebc98-4e49-4067-9c6c-d86a0e092e3d}')
    @commethod(7)
    def GetAltInfo(self, ppParent: POINTER(Windows.Win32.Media.Speech.ISpPhrase_head), pulStartElementInParent: POINTER(UInt32), pcElementsInParent: POINTER(UInt32), pcElementsInAlt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b4fb971-b115-4de1-ad97-e482e3bf6ee4}')
    @commethod(3)
    def SetPropertyNum(self, pName: Windows.Win32.Foundation.PWSTR, lValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyNum(self, pName: Windows.Win32.Foundation.PWSTR, plValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPropertyString(self, pName: Windows.Win32.Foundation.PWSTR, pValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyString(self, pName: Windows.Win32.Foundation.PWSTR, ppCoMemValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoContext(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpEventSource
    _iid_ = Guid('{f740a62f-7c15-489e-8234-940a33d9272d}')
    @commethod(13)
    def GetRecognizer(self, ppRecognizer: POINTER(Windows.Win32.Media.Speech.ISpRecognizer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateGrammar(self, ullGrammarId: UInt64, ppGrammar: POINTER(Windows.Win32.Media.Speech.ISpRecoGrammar_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStatus(self, pStatus: POINTER(Windows.Win32.Media.Speech.SPRECOCONTEXTSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMaxAlternates(self, pcAlternates: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetMaxAlternates(self, cAlternates: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetAudioOptions(self, Options: Windows.Win32.Media.Speech.SPAUDIOOPTIONS, pAudioFormatId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAudioOptions(self, pOptions: POINTER(Windows.Win32.Media.Speech.SPAUDIOOPTIONS), pAudioFormatId: POINTER(Guid), ppCoMemWFEX: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeserializeResult(self, pSerializedResult: POINTER(Windows.Win32.Media.Speech.SPSERIALIZEDRESULT_head), ppResult: POINTER(Windows.Win32.Media.Speech.ISpRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Bookmark(self, Options: Windows.Win32.Media.Speech.SPBOOKMARKOPTIONS, ullStreamPosition: UInt64, lparamEvent: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetAdaptationData(self, pAdaptationData: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Pause(self, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Resume(self, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetVoice(self, pVoice: Windows.Win32.Media.Speech.ISpVoice_head, fAllowFormatChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetVoice(self, ppVoice: POINTER(Windows.Win32.Media.Speech.ISpVoice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetVoicePurgeEvent(self, ullEventInterest: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetVoicePurgeEvent(self, pullEventInterest: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetContextState(self, eContextState: Windows.Win32.Media.Speech.SPCONTEXTSTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetContextState(self, peContextState: POINTER(Windows.Win32.Media.Speech.SPCONTEXTSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoContext2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bead311c-52ff-437f-9464-6b21054ca73d}')
    @commethod(3)
    def SetGrammarOptions(self, eGrammarOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGrammarOptions(self, peGrammarOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAdaptationData2(self, pAdaptationData: Windows.Win32.Foundation.PWSTR, cch: UInt32, pTopicName: Windows.Win32.Foundation.PWSTR, eAdaptationSettings: UInt32, eRelevance: Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoGrammar(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpGrammarBuilder
    _iid_ = Guid('{2177db29-7f45-47d0-8554-067e91c80502}')
    @commethod(11)
    def GetGrammarId(self, pullGrammarId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecoContext(self, ppRecoCtxt: POINTER(Windows.Win32.Media.Speech.ISpRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def LoadCmdFromFile(self, pszFileName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def LoadCmdFromObject(self, rcid: POINTER(Guid), pszGrammarName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LoadCmdFromResource(self, hModule: Windows.Win32.Foundation.HMODULE, pszResourceName: Windows.Win32.Foundation.PWSTR, pszResourceType: Windows.Win32.Foundation.PWSTR, wLanguage: UInt16, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def LoadCmdFromMemory(self, pGrammar: POINTER(Windows.Win32.Media.Speech.SPBINARYGRAMMAR_head), Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def LoadCmdFromProprietaryGrammar(self, rguidParam: POINTER(Guid), pszStringParam: Windows.Win32.Foundation.PWSTR, pvDataPrarm: c_void_p, cbDataSize: UInt32, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRuleState(self, pszName: Windows.Win32.Foundation.PWSTR, pReserved: c_void_p, NewState: Windows.Win32.Media.Speech.SPRULESTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetRuleIdState(self, ulRuleId: UInt32, NewState: Windows.Win32.Media.Speech.SPRULESTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def LoadDictation(self, pszTopicName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def UnloadDictation(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetDictationState(self, NewState: Windows.Win32.Media.Speech.SPRULESTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWordSequenceData(self, pText: Windows.Win32.Foundation.PWSTR, cchText: UInt32, pInfo: POINTER(Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTextSelection(self, pInfo: POINTER(Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsPronounceable(self, pszWord: Windows.Win32.Foundation.PWSTR, pWordPronounceable: POINTER(Windows.Win32.Media.Speech.SPWORDPRONOUNCEABLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetGrammarState(self, eGrammarState: Windows.Win32.Media.Speech.SPGRAMMARSTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SaveCmd(self, pStream: Windows.Win32.System.Com.IStream_head, ppszCoMemErrorText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetGrammarState(self, peGrammarState: POINTER(Windows.Win32.Media.Speech.SPGRAMMARSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoGrammar2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b37bc9e-9ed6-44a3-93d3-18f022b79ec3}')
    @commethod(3)
    def GetRules(self, ppCoMemRules: POINTER(POINTER(Windows.Win32.Media.Speech.SPRULE_head)), puNumRules: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadCmdFromFile2(self, pszFileName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS, pszSharingUri: Windows.Win32.Foundation.PWSTR, pszBaseUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadCmdFromMemory2(self, pGrammar: POINTER(Windows.Win32.Media.Speech.SPBINARYGRAMMAR_head), Options: Windows.Win32.Media.Speech.SPLOADOPTIONS, pszSharingUri: Windows.Win32.Foundation.PWSTR, pszBaseUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRulePriority(self, pszRuleName: Windows.Win32.Foundation.PWSTR, ulRuleId: UInt32, nRulePriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRuleWeight(self, pszRuleName: Windows.Win32.Foundation.PWSTR, ulRuleId: UInt32, flWeight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDictationWeight(self, flWeight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetGrammarLoader(self, pLoader: Windows.Win32.Media.Speech.ISpeechResourceLoader_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSMLSecurityManager(self, pSMLSecurityManager: Windows.Win32.System.Com.Urlmon.IInternetSecurityManager_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoResult(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpPhrase
    _iid_ = Guid('{20b053be-e235-43cd-9a2a-8d17a48b7842}')
    @commethod(7)
    def GetResultTimes(self, pTimes: POINTER(Windows.Win32.Media.Speech.SPRECORESULTTIMES_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAlternates(self, ulStartElement: UInt32, cElements: UInt32, ulRequestCount: UInt32, ppPhrases: POINTER(Windows.Win32.Media.Speech.ISpPhraseAlt_head), pcPhrasesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAudio(self, ulStartElement: UInt32, cElements: UInt32, ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SpeakAudio(self, ulStartElement: UInt32, cElements: UInt32, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Serialize(self, ppCoMemSerializedResult: POINTER(POINTER(Windows.Win32.Media.Speech.SPSERIALIZEDRESULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ScaleAudio(self, pAudioFormatId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecoContext(self, ppRecoContext: POINTER(Windows.Win32.Media.Speech.ISpRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoResult2(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpRecoResult
    _iid_ = Guid('{27cac6c4-88f2-41f2-8817-0c95e59f1e6e}')
    @commethod(14)
    def CommitAlternate(self, pPhraseAlt: Windows.Win32.Media.Speech.ISpPhraseAlt_head, ppNewResult: POINTER(Windows.Win32.Media.Speech.ISpRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CommitText(self, ulStartElement: UInt32, cElements: UInt32, pszCorrectedData: Windows.Win32.Foundation.PWSTR, eCommitFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetTextFeedback(self, pszFeedback: Windows.Win32.Foundation.PWSTR, fSuccessful: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecognizer(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpProperties
    _iid_ = Guid('{c2b5f241-daa0-4507-9e16-5a1eaa2b7a5c}')
    @commethod(7)
    def SetRecognizer(self, pRecognizer: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecognizer(self, ppRecognizer: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetInput(self, pUnkInput: Windows.Win32.System.Com.IUnknown_head, fAllowFormatChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInputObjectToken(self, ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInputStream(self, ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateRecoContext(self, ppNewCtxt: POINTER(Windows.Win32.Media.Speech.ISpRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecoProfile(self, ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetRecoProfile(self, pToken: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsSharedInstance(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecoState(self, pState: POINTER(Windows.Win32.Media.Speech.SPRECOSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetRecoState(self, NewState: Windows.Win32.Media.Speech.SPRECOSTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStatus(self, pStatus: POINTER(Windows.Win32.Media.Speech.SPRECOGNIZERSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFormat(self, WaveFormatType: Windows.Win32.Media.Speech.SPSTREAMFORMATTYPE, pFormatId: POINTER(Guid), ppCoMemWFEX: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def IsUISupported(self, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, pfSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DisplayUI(self, hwndParent: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EmulateRecognition(self, pPhrase: Windows.Win32.Media.Speech.ISpPhrase_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecognizer2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fc6d974-c81e-4098-93c5-0147f61ed4d3}')
    @commethod(3)
    def EmulateRecognitionEx(self, pPhrase: Windows.Win32.Media.Speech.ISpPhrase_head, dwCompareFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTrainingState(self, fDoingTraining: Windows.Win32.Foundation.BOOL, fAdaptFromTrainingData: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ResetAcousticModelAdaptation(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRegDataKey(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpDataKey
    _iid_ = Guid('{92a66e2b-c830-4149-83df-6fc2ba1e7a5b}')
    @commethod(15)
    def SetKey(self, hkey: Windows.Win32.System.Registry.HKEY, fReadOnly: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpResourceManager(ComPtr):
    extends: Windows.Win32.System.Com.IServiceProvider
    _iid_ = Guid('{93384e18-5014-43d5-adbb-a78e055926bd}')
    @commethod(4)
    def SetObject(self, guidServiceId: POINTER(Guid), pUnkObject: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObject(self, guidServiceId: POINTER(Guid), ObjectCLSID: POINTER(Guid), ObjectIID: POINTER(Guid), fReleaseWhenLastExternalRefReleased: Windows.Win32.Foundation.BOOL, ppObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpSerializeState(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{21b501a0-0ec7-46c9-92c3-a2bc784c54b9}')
    @commethod(3)
    def GetSerializedState(self, ppbData: POINTER(POINTER(Byte)), pulSize: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSerializedState(self, pbData: POINTER(Byte), ulSize: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpShortcut(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3df681e2-ea56-11d9-8bde-f66bad1e3f3a}')
    @commethod(3)
    def AddShortcut(self, pszDisplay: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pszSpoken: Windows.Win32.Foundation.PWSTR, shType: Windows.Win32.Media.Speech.SPSHORTCUTTYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveShortcut(self, pszDisplay: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pszSpoken: Windows.Win32.Foundation.PWSTR, shType: Windows.Win32.Media.Speech.SPSHORTCUTTYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetShortcuts(self, LangID: UInt16, pShortcutpairList: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGeneration(self, pdwGeneration: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetWordsFromGenerationChange(self, pdwGeneration: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(self, pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetShortcutsForGeneration(self, pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pShortcutpairList: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGenerationChange(self, pdwGeneration: POINTER(UInt32), pShortcutpairList: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpStream(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpStreamFormat
    _iid_ = Guid('{12e3cca9-7518-44c5-a5e7-ba5a79cb929e}')
    @commethod(15)
    def SetBaseStream(self, pStream: Windows.Win32.System.Com.IStream_head, rguidFormat: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetBaseStream(self, ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def BindToFile(self, pszFileName: Windows.Win32.Foundation.PWSTR, eMode: Windows.Win32.Media.Speech.SPFILEMODE, pFormatId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), ullEventInterest: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpStreamFormat(ComPtr):
    extends: Windows.Win32.System.Com.IStream
    _iid_ = Guid('{bed530be-2606-4f4d-a1c0-54c5cda5566f}')
    @commethod(14)
    def GetFormat(self, pguidFormatId: POINTER(Guid), ppCoMemWaveFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ISpStreamFormatConverter(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpStreamFormat
    _iid_ = Guid('{678a932c-ea71-4446-9b41-78fda6280a29}')
    @commethod(15)
    def SetBaseStream(self, pStream: Windows.Win32.Media.Speech.ISpStreamFormat_head, fSetFormatToBaseStreamFormat: Windows.Win32.Foundation.BOOL, fWriteToBaseStream: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetBaseStream(self, ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetFormat(self, rguidFormatIdOfConvertedStream: POINTER(Guid), pWaveFormatExOfConvertedStream: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ResetSeekPosition(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ScaleConvertedToBaseOffset(self, ullOffsetConvertedStream: UInt64, pullOffsetBaseStream: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ScaleBaseToConvertedOffset(self, ullOffsetBaseStream: UInt64, pullOffsetConvertedStream: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpTranscript(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10f63bce-201a-11d3-ac70-00c04f8ee6c0}')
    @commethod(3)
    def GetTranscript(self, ppszTranscript: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AppendTranscript(self, pszTranscript: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpVoice(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpEventSource
    _iid_ = Guid('{6c44df74-72b9-4992-a1ec-ef996e0422d4}')
    @commethod(13)
    def SetOutput(self, pUnkOutput: Windows.Win32.System.Com.IUnknown_head, fAllowFormatChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetOutputObjectToken(self, ppObjectToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetOutputStream(self, ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetVoice(self, pToken: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetVoice(self, ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Speak(self, pwcs: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SpeakStream(self, pStream: Windows.Win32.System.Com.IStream_head, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetStatus(self, pStatus: POINTER(Windows.Win32.Media.Speech.SPVOICESTATUS_head), ppszLastBookmark: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Skip(self, pItemType: Windows.Win32.Foundation.PWSTR, lNumItems: Int32, pulNumSkipped: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetPriority(self, ePriority: Windows.Win32.Media.Speech.SPVPRIORITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPriority(self, pePriority: POINTER(Windows.Win32.Media.Speech.SPVPRIORITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetAlertBoundary(self, eBoundary: Windows.Win32.Media.Speech.SPEVENTENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetAlertBoundary(self, peBoundary: POINTER(Windows.Win32.Media.Speech.SPEVENTENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetRate(self, RateAdjust: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetRate(self, pRateAdjust: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetVolume(self, usVolume: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetVolume(self, pusVolume: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def WaitUntilDone(self, msTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetSyncSpeakTimeout(self, msTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetSyncSpeakTimeout(self, pmsTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SpeakCompleteEvent(self) -> Windows.Win32.Foundation.HANDLE: ...
    @commethod(36)
    def IsUISupported(self, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, pfSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def DisplayUI(self, hwndParent: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpXMLRecoResult(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpRecoResult
    _iid_ = Guid('{ae39362b-45a8-4074-9b9e-ccf49aa2d0b6}')
    @commethod(14)
    def GetXMLResult(self, ppszCoMemXMLResult: POINTER(Windows.Win32.Foundation.PWSTR), Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetXMLErrorInfo(self, pSemanticErrorInfo: POINTER(Windows.Win32.Media.Speech.SPSEMANTICERRORINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudio(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{cff8e175-019e-11d3-a08e-00c04f8ef9b5}')
    @commethod(12)
    def get_Status(self, Status: POINTER(Windows.Win32.Media.Speech.ISpeechAudioStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_BufferInfo(self, BufferInfo: POINTER(Windows.Win32.Media.Speech.ISpeechAudioBufferInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_DefaultFormat(self, StreamFormat: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Volume(self, Volume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Volume(self, Volume: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BufferNotifySize(self, BufferNotifySize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BufferNotifySize(self, BufferNotifySize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EventHandle(self, EventHandle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetState(self, State: Windows.Win32.Media.Speech.SpeechAudioState) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioBufferInfo(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{11b103d8-1142-4edf-a093-82fb3915f8cc}')
    @commethod(7)
    def get_MinNotification(self, MinNotification: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_MinNotification(self, MinNotification: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BufferSize(self, BufferSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_BufferSize(self, BufferSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_EventBias(self, EventBias: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_EventBias(self, EventBias: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioFormat(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e6e9c590-3e18-40e3-8299-061f98bde7c7}')
    @commethod(7)
    def get_Type(self, AudioFormat: POINTER(Windows.Win32.Media.Speech.SpeechAudioFormatType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Type(self, AudioFormat: Windows.Win32.Media.Speech.SpeechAudioFormatType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Guid(self, Guid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Guid(self, Guid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetWaveFormatEx(self, SpeechWaveFormatEx: POINTER(Windows.Win32.Media.Speech.ISpeechWaveFormatEx_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetWaveFormatEx(self, SpeechWaveFormatEx: Windows.Win32.Media.Speech.ISpeechWaveFormatEx_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioStatus(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c62d9c91-7458-47f6-862d-1ef86fb0b278}')
    @commethod(7)
    def get_FreeBufferSpace(self, FreeBufferSpace: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_NonBlockingIO(self, NonBlockingIO: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_State(self, State: POINTER(Windows.Win32.Media.Speech.SpeechAudioState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentSeekPosition(self, CurrentSeekPosition: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentDevicePosition(self, CurrentDevicePosition: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechBaseStream(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6450336f-7d49-4ced-8097-49d6dee37294}')
    @commethod(7)
    def get_Format(self, AudioFormat: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def putref_Format(self, AudioFormat: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Read(self, Buffer: POINTER(Windows.Win32.System.Variant.VARIANT_head), NumberOfBytes: Int32, BytesRead: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Write(self, Buffer: Windows.Win32.System.Variant.VARIANT, BytesWritten: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Seek(self, Position: Windows.Win32.System.Variant.VARIANT, Origin: Windows.Win32.Media.Speech.SpeechStreamSeekPositionType, NewPosition: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechCustomStream(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{1a9e9f4f-104f-4db8-a115-efd7fd0c97ae}')
    @commethod(12)
    def get_BaseStream(self, ppUnkStream: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_BaseStream(self, pUnkStream: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechDataKey(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ce17c09b-4efa-44d5-a4c9-59d9585ab0cd}')
    @commethod(7)
    def SetBinaryValue(self, ValueName: Windows.Win32.Foundation.BSTR, Value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBinaryValue(self, ValueName: Windows.Win32.Foundation.BSTR, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetStringValue(self, ValueName: Windows.Win32.Foundation.BSTR, Value: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStringValue(self, ValueName: Windows.Win32.Foundation.BSTR, Value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLongValue(self, ValueName: Windows.Win32.Foundation.BSTR, Value: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLongValue(self, ValueName: Windows.Win32.Foundation.BSTR, Value: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OpenKey(self, SubKeyName: Windows.Win32.Foundation.BSTR, SubKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateKey(self, SubKeyName: Windows.Win32.Foundation.BSTR, SubKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def DeleteKey(self, SubKeyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteValue(self, ValueName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumKeys(self, Index: Int32, SubKeyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumValues(self, Index: Int32, ValueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechFileStream(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{af67f125-ab39-4e93-b4a2-cc2e66e182a7}')
    @commethod(12)
    def Open(self, FileName: Windows.Win32.Foundation.BSTR, FileMode: Windows.Win32.Media.Speech.SpeechStreamFileMode, DoEvents: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRule(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{afe719cf-5dd1-44f2-999c-7a399f1cfccc}')
    @commethod(7)
    def get_Attributes(self, Attributes: POINTER(Windows.Win32.Media.Speech.SpeechRuleAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_InitialState(self, State: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(self, Id: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddResource(self, ResourceName: Windows.Win32.Foundation.BSTR, ResourceValue: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddState(self, State: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleState(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d4286f2c-ee67-45ae-b928-28d695362eda}')
    @commethod(7)
    def get_Rule(self, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Transitions(self, Transitions: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleStateTransitions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddWordTransition(self, DestState: Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head, Words: Windows.Win32.Foundation.BSTR, Separators: Windows.Win32.Foundation.BSTR, Type: Windows.Win32.Media.Speech.SpeechGrammarWordType, PropertyName: Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), Weight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddRuleTransition(self, DestinationState: Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head, Rule: Windows.Win32.Media.Speech.ISpeechGrammarRule_head, PropertyName: Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), Weight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddSpecialTransition(self, DestinationState: Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head, Type: Windows.Win32.Media.Speech.SpeechSpecialTransitionType, PropertyName: Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), Weight: Single) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleStateTransition(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafd1db1-41d1-4a06-9863-e2e81da17a9a}')
    @commethod(7)
    def get_Type(self, Type: POINTER(Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Text(self, Text: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Rule(self, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Weight(self, Weight: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PropertyName(self, PropertyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PropertyId(self, PropertyId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PropertyValue(self, PropertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NextState(self, NextState: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleStateTransitions(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{eabce657-75bc-44a2-aa7f-c56476742963}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Transition: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleStateTransition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRules(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6ffa3b44-fc2d-40d1-8afc-32911c7f1ad1}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindRule(self, RuleNameOrId: Windows.Win32.System.Variant.VARIANT, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, Index: Int32, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Dynamic(self, Dynamic: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Add(self, RuleName: Windows.Win32.Foundation.BSTR, Attributes: Windows.Win32.Media.Speech.SpeechRuleAttributes, RuleId: Int32, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CommitAndSave(self, ErrorText: POINTER(Windows.Win32.Foundation.BSTR), SaveStream: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexicon(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3da7627a-c7ae-4b23-8708-638c50362c25}')
    @commethod(7)
    def get_GenerationId(self, GenerationId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(self, Flags: Windows.Win32.Media.Speech.SpeechLexiconType, GenerationID: POINTER(Int32), Words: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconWords_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddPronunciation(self, bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, bstrPronunciation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddPronunciationByPhoneIds(self, bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, PhoneIds: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemovePronunciation(self, bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, bstrPronunciation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemovePronunciationByPhoneIds(self, bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, PhoneIds: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPronunciations(self, bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, TypeFlags: Windows.Win32.Media.Speech.SpeechLexiconType, ppPronunciations: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconPronunciations_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetGenerationChange(self, GenerationID: POINTER(Int32), ppWords: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconWords_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconPronunciation(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{95252c5d-9e43-4f4a-9899-48ee73352f9f}')
    @commethod(7)
    def get_Type(self, LexiconType: POINTER(Windows.Win32.Media.Speech.SpeechLexiconType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LangId(self, LangId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PartOfSpeech(self, PartOfSpeech: POINTER(Windows.Win32.Media.Speech.SpeechPartOfSpeech)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PhoneIds(self, PhoneIds: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Symbolic(self, Symbolic: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconPronunciations(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{72829128-5682-4704-a0d4-3e2bb6f2ead3}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Pronunciation: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconPronunciation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconWord(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4e5b933c-c9be-48ed-8842-1ee51bb1d4ff}')
    @commethod(7)
    def get_LangId(self, LangId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Type(self, WordType: POINTER(Windows.Win32.Media.Speech.SpeechWordType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Word(self, Word: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Pronunciations(self, Pronunciations: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconPronunciations_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconWords(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8d199862-415e-47d5-ac4f-faa608b424e6}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Word: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconWord_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechMMSysAudio(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpeechAudio
    _iid_ = Guid('{3c76af6d-1fd7-4831-81d1-3b71d5a13c44}')
    @commethod(21)
    def get_DeviceId(self, DeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DeviceId(self, DeviceId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LineId(self, LineId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_LineId(self, LineId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MMHandle(self, Handle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechMemoryStream(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{eeb14b68-808b-4abe-a5ea-b51da7588008}')
    @commethod(12)
    def SetData(self, Data: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetData(self, pData: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectToken(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c74a3adc-b727-4500-a84a-b526721c8b8c}')
    @commethod(7)
    def get_Id(self, ObjectId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DataKey(self, DataKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Category(self, Category: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokenCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDescription(self, Locale: Int32, Description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetId(self, Id: Windows.Win32.Foundation.BSTR, CategoryID: Windows.Win32.Foundation.BSTR, CreateIfNotExist: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAttribute(self, AttributeName: Windows.Win32.Foundation.BSTR, AttributeValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateInstance(self, pUnkOuter: Windows.Win32.System.Com.IUnknown_head, ClsContext: Windows.Win32.Media.Speech.SpeechTokenContext, Object: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Remove(self, ObjectStorageCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStorageFileName(self, ObjectStorageCLSID: Windows.Win32.Foundation.BSTR, KeyName: Windows.Win32.Foundation.BSTR, FileName: Windows.Win32.Foundation.BSTR, Folder: Windows.Win32.Media.Speech.SpeechTokenShellFolder, FilePath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveStorageFileName(self, ObjectStorageCLSID: Windows.Win32.Foundation.BSTR, KeyName: Windows.Win32.Foundation.BSTR, DeleteFile: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def IsUISupported(self, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Variant.VARIANT_head), Object: Windows.Win32.System.Com.IUnknown_head, Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DisplayUI(self, hWnd: Int32, Title: Windows.Win32.Foundation.BSTR, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Variant.VARIANT_head), Object: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def MatchesAttributes(self, Attributes: Windows.Win32.Foundation.BSTR, Matches: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectTokenCategory(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ca7eac50-2d01-4145-86d4-5ae7d70f4469}')
    @commethod(7)
    def get_Id(self, Id: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Default(self, TokenId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Default(self, TokenId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetId(self, Id: Windows.Win32.Foundation.BSTR, CreateIfNotExist: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDataKey(self, Location: Windows.Win32.Media.Speech.SpeechDataKeyLocation, DataKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumerateTokens(self, RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, Tokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectTokens(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9285b776-2e7b-4bc0-b53e-580eb6fa967f}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Token: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhoneConverter(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c3e4f353-433f-43d6-89a1-6a62a7054c3d}')
    @commethod(7)
    def get_LanguageId(self, LanguageId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LanguageId(self, LanguageId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PhoneToId(self, Phonemes: Windows.Win32.Foundation.BSTR, IdArray: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IdToPhone(self, IdArray: Windows.Win32.System.Variant.VARIANT, Phonemes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseAlternate(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27864a2a-2b9f-4cb8-92d3-0d2722fd1e73}')
    @commethod(7)
    def get_RecoResult(self, RecoResult: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_StartElementInResult(self, StartElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NumberOfElementsInResult(self, NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PhraseInfo(self, PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseAlternates(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b238b6d5-f276-4c3d-a6c1-2974801c3cc2}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, PhraseAlternate: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseAlternate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseElement(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e6176f96-e373-4801-b223-3b62c068c0b4}')
    @commethod(7)
    def get_AudioTimeOffset(self, AudioTimeOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AudioSizeTime(self, AudioSizeTime: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AudioStreamOffset(self, AudioStreamOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioSizeBytes(self, AudioSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RetainedStreamOffset(self, RetainedStreamOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RetainedSizeBytes(self, RetainedSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisplayText(self, DisplayText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_LexicalForm(self, LexicalForm: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Pronunciation(self, Pronunciation: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_DisplayAttributes(self, DisplayAttributes: POINTER(Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RequiredConfidence(self, RequiredConfidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ActualConfidence(self, ActualConfidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EngineConfidence(self, EngineConfidence: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseElements(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0626b328-3478-467d-a0b3-d0853b93dda3}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Element: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseInfo(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{961559cf-4e67-4662-8bf0-d93f1fcd61b3}')
    @commethod(7)
    def get_LanguageId(self, LanguageId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GrammarId(self, GrammarId: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StartTime(self, StartTime: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioStreamPosition(self, AudioStreamPosition: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AudioSizeBytes(self, pAudioSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RetainedSizeBytes(self, RetainedSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AudioSizeTime(self, AudioSizeTime: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Rule(self, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Properties(self, Properties: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Elements(self, Elements: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseElements_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Replacements(self, Replacements: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseReplacements_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_EngineId(self, EngineIdGuid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EnginePrivateData(self, PrivateData: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SaveToMemory(self, PhraseBlock: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetText(self, StartElement: Int32, Elements: Int32, UseReplacements: Windows.Win32.Foundation.VARIANT_BOOL, Text: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetDisplayAttributes(self, StartElement: Int32, Elements: Int32, UseReplacements: Windows.Win32.Foundation.VARIANT_BOOL, DisplayAttributes: POINTER(Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseInfoBuilder(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3b151836-df3a-4e0a-846c-d2adc9334333}')
    @commethod(7)
    def RestorePhraseFromMemory(self, PhraseInMemory: POINTER(Windows.Win32.System.Variant.VARIANT_head), PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseProperties(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{08166b47-102e-4b23-a599-bdb98dbfd1f4}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Property: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseProperty(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ce563d48-961e-4732-a2e1-378a42b430be}')
    @commethod(7)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, Id: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(self, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FirstElement(self, FirstElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_NumberOfElements(self, NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_EngineConfidence(self, Confidence: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Confidence(self, Confidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Parent(self, ParentProperty: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Children(self, Children: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseReplacement(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2890a410-53a7-4fb5-94ec-06d4998e3d02}')
    @commethod(7)
    def get_DisplayAttributes(self, DisplayAttributes: POINTER(Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Text(self, Text: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FirstElement(self, FirstElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfElements(self, NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseReplacements(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{38bc662f-2257-4525-959e-2069d2596c05}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Reps: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseReplacement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseRule(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a7bfe112-a4a0-48d9-b602-c313843f6964}')
    @commethod(7)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, Id: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FirstElement(self, FirstElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfElements(self, NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Parent(self, Parent: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Children(self, Children: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Confidence(self, ActualConfidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_EngineConfidence(self, EngineConfidence: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseRules(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9047d593-01dd-4b72-81a3-e4a0ca69f407}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoContext(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{580aa49d-7e1e-4809-b8e2-57da806104b8}')
    @commethod(7)
    def get_Recognizer(self, Recognizer: POINTER(Windows.Win32.Media.Speech.ISpeechRecognizer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AudioInputInterferenceStatus(self, Interference: POINTER(Windows.Win32.Media.Speech.SpeechInterference)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_RequestedUIType(self, UIType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def putref_Voice(self, Voice: Windows.Win32.Media.Speech.ISpeechVoice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Voice(self, Voice: POINTER(Windows.Win32.Media.Speech.ISpeechVoice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowVoiceFormatMatchingOnNextSet(self, Allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowVoiceFormatMatchingOnNextSet(self, pAllow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_VoicePurgeEvent(self, EventInterest: Windows.Win32.Media.Speech.SpeechRecoEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_VoicePurgeEvent(self, EventInterest: POINTER(Windows.Win32.Media.Speech.SpeechRecoEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EventInterests(self, EventInterest: Windows.Win32.Media.Speech.SpeechRecoEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_EventInterests(self, EventInterest: POINTER(Windows.Win32.Media.Speech.SpeechRecoEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_CmdMaxAlternates(self, MaxAlternates: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CmdMaxAlternates(self, MaxAlternates: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_State(self, State: Windows.Win32.Media.Speech.SpeechRecoContextState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_State(self, State: POINTER(Windows.Win32.Media.Speech.SpeechRecoContextState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_RetainedAudio(self, Option: Windows.Win32.Media.Speech.SpeechRetainedAudioOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RetainedAudio(self, Option: POINTER(Windows.Win32.Media.Speech.SpeechRetainedAudioOptions)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def putref_RetainedAudioFormat(self, Format: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_RetainedAudioFormat(self, Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreateGrammar(self, GrammarId: Windows.Win32.System.Variant.VARIANT, Grammar: POINTER(Windows.Win32.Media.Speech.ISpeechRecoGrammar_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateResultFromMemory(self, ResultBlock: POINTER(Windows.Win32.System.Variant.VARIANT_head), Result: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Bookmark(self, Options: Windows.Win32.Media.Speech.SpeechBookmarkOptions, StreamPos: Windows.Win32.System.Variant.VARIANT, BookmarkId: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetAdaptationData(self, AdaptationString: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoGrammar(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b6d6f79f-2158-4e50-b5bc-9a9ccd852a09}')
    @commethod(7)
    def get_Id(self, Id: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RecoContext(self, RecoContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_State(self, State: Windows.Win32.Media.Speech.SpeechGrammarState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(self, State: POINTER(Windows.Win32.Media.Speech.SpeechGrammarState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Rules(self, Rules: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Reset(self, NewLanguage: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CmdLoadFromFile(self, FileName: Windows.Win32.Foundation.BSTR, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CmdLoadFromObject(self, ClassId: Windows.Win32.Foundation.BSTR, GrammarName: Windows.Win32.Foundation.BSTR, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CmdLoadFromResource(self, hModule: Int32, ResourceName: Windows.Win32.System.Variant.VARIANT, ResourceType: Windows.Win32.System.Variant.VARIANT, LanguageId: Int32, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CmdLoadFromMemory(self, GrammarData: Windows.Win32.System.Variant.VARIANT, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CmdLoadFromProprietaryGrammar(self, ProprietaryGuid: Windows.Win32.Foundation.BSTR, ProprietaryString: Windows.Win32.Foundation.BSTR, ProprietaryData: Windows.Win32.System.Variant.VARIANT, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CmdSetRuleState(self, Name: Windows.Win32.Foundation.BSTR, State: Windows.Win32.Media.Speech.SpeechRuleState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CmdSetRuleIdState(self, RuleId: Int32, State: Windows.Win32.Media.Speech.SpeechRuleState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DictationLoad(self, TopicName: Windows.Win32.Foundation.BSTR, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DictationUnload(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DictationSetState(self, State: Windows.Win32.Media.Speech.SpeechRuleState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWordSequenceData(self, Text: Windows.Win32.Foundation.BSTR, TextLength: Int32, Info: Windows.Win32.Media.Speech.ISpeechTextSelectionInformation_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTextSelection(self, Info: Windows.Win32.Media.Speech.ISpeechTextSelectionInformation_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsPronounceable(self, Word: Windows.Win32.Foundation.BSTR, WordPronounceable: POINTER(Windows.Win32.Media.Speech.SpeechWordPronounceable)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResult(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ed2879cf-ced9-4ee6-a534-de0191d5468d}')
    @commethod(7)
    def get_RecoContext(self, RecoContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Times(self, Times: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResultTimes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_AudioFormat(self, Format: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioFormat(self, Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PhraseInfo(self, PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Alternates(self, RequestCount: Int32, StartElement: Int32, Elements: Int32, Alternates: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseAlternates_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Audio(self, StartElement: Int32, Elements: Int32, Stream: POINTER(Windows.Win32.Media.Speech.ISpeechMemoryStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SpeakAudio(self, StartElement: Int32, Elements: Int32, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveToMemory(self, ResultBlock: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscardResultInfo(self, ValueTypes: Windows.Win32.Media.Speech.SpeechDiscardType) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResult2(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpeechRecoResult
    _iid_ = Guid('{8e0a246d-d3c8-45de-8657-04290c458c3c}')
    @commethod(17)
    def SetTextFeedback(self, Feedback: Windows.Win32.Foundation.BSTR, WasSuccessful: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResultDispatch(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6d60eb64-aced-40a6-bbf3-4e557f71dee2}')
    @commethod(7)
    def get_RecoContext(self, RecoContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Times(self, Times: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResultTimes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_AudioFormat(self, Format: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioFormat(self, Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PhraseInfo(self, PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Alternates(self, RequestCount: Int32, StartElement: Int32, Elements: Int32, Alternates: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseAlternates_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Audio(self, StartElement: Int32, Elements: Int32, Stream: POINTER(Windows.Win32.Media.Speech.ISpeechMemoryStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SpeakAudio(self, StartElement: Int32, Elements: Int32, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveToMemory(self, ResultBlock: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscardResultInfo(self, ValueTypes: Windows.Win32.Media.Speech.SpeechDiscardType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetXMLResult(self, Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetXMLErrorInfo(self, LineNumber: POINTER(Int32), ScriptLine: POINTER(Windows.Win32.Foundation.BSTR), Source: POINTER(Windows.Win32.Foundation.BSTR), Description: POINTER(Windows.Win32.Foundation.BSTR), ResultCode: POINTER(Windows.Win32.Foundation.HRESULT), IsError: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetTextFeedback(self, Feedback: Windows.Win32.Foundation.BSTR, WasSuccessful: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResultTimes(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{62b3b8fb-f6e7-41be-bdcb-056b1c29efc0}')
    @commethod(7)
    def get_StreamTime(self, Time: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Length(self, Length: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TickCount(self, TickCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OffsetFromStart(self, OffsetFromStart: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecognizer(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2d5f1c0c-bd75-4b08-9478-3b11fea2586c}')
    @commethod(7)
    def putref_Recognizer(self, Recognizer: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Recognizer(self, Recognizer: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_AllowAudioInputFormatChangesOnNextSet(self, Allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AllowAudioInputFormatChangesOnNextSet(self, Allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_AudioInput(self, AudioInput: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_AudioInput(self, AudioInput: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_AudioInputStream(self, AudioInputStream: Windows.Win32.Media.Speech.ISpeechBaseStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AudioInputStream(self, AudioInputStream: POINTER(Windows.Win32.Media.Speech.ISpeechBaseStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsShared(self, Shared: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_State(self, State: Windows.Win32.Media.Speech.SpeechRecognizerState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_State(self, State: POINTER(Windows.Win32.Media.Speech.SpeechRecognizerState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Status(self, Status: POINTER(Windows.Win32.Media.Speech.ISpeechRecognizerStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def putref_Profile(self, Profile: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Profile(self, Profile: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EmulateRecognition(self, TextElements: Windows.Win32.System.Variant.VARIANT, ElementDisplayAttributes: POINTER(Windows.Win32.System.Variant.VARIANT_head), LanguageId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateRecoContext(self, NewContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetFormat(self, Type: Windows.Win32.Media.Speech.SpeechFormatType, Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetPropertyNumber(self, Name: Windows.Win32.Foundation.BSTR, Value: Int32, Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPropertyNumber(self, Name: Windows.Win32.Foundation.BSTR, Value: POINTER(Int32), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetPropertyString(self, Name: Windows.Win32.Foundation.BSTR, Value: Windows.Win32.Foundation.BSTR, Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetPropertyString(self, Name: Windows.Win32.Foundation.BSTR, Value: POINTER(Windows.Win32.Foundation.BSTR), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def IsUISupported(self, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Variant.VARIANT_head), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DisplayUI(self, hWndParent: Int32, Title: Windows.Win32.Foundation.BSTR, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetRecognizers(self, RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetAudioInputs(self, RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetProfiles(self, RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecognizerStatus(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bff9e781-53ec-484e-bb8a-0e1b5551e35c}')
    @commethod(7)
    def get_AudioStatus(self, AudioStatus: POINTER(Windows.Win32.Media.Speech.ISpeechAudioStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentStreamPosition(self, pCurrentStreamPos: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentStreamNumber(self, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfActiveRules(self, NumberOfActiveRules: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ClsidEngine(self, ClsidEngine: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SupportedLanguages(self, SupportedLanguages: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechResourceLoader(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b9ac5783-fcd0-4b21-b119-b4f8da8fd2c3}')
    @commethod(7)
    def LoadResource(self, bstrResourceUri: Windows.Win32.Foundation.BSTR, fAlwaysReload: Windows.Win32.Foundation.VARIANT_BOOL, pStream: POINTER(Windows.Win32.System.Com.IUnknown_head), pbstrMIMEType: POINTER(Windows.Win32.Foundation.BSTR), pfModified: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), pbstrRedirectUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLocalCopy(self, bstrResourceUri: Windows.Win32.Foundation.BSTR, pbstrLocalPath: POINTER(Windows.Win32.Foundation.BSTR), pbstrMIMEType: POINTER(Windows.Win32.Foundation.BSTR), pbstrRedirectUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ReleaseLocalCopy(self, pbstrLocalPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechTextSelectionInformation(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3b9c7e7a-6eee-4ded-9092-11657279adbe}')
    @commethod(7)
    def put_ActiveOffset(self, ActiveOffset: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActiveOffset(self, ActiveOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ActiveLength(self, ActiveLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ActiveLength(self, ActiveLength: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_SelectionOffset(self, SelectionOffset: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SelectionOffset(self, SelectionOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_SelectionLength(self, SelectionLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SelectionLength(self, SelectionLength: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechVoice(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{269316d8-57bd-11d2-9eee-00c04f797396}')
    @commethod(7)
    def get_Status(self, Status: POINTER(Windows.Win32.Media.Speech.ISpeechVoiceStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Voice(self, Voice: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_Voice(self, Voice: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioOutput(self, AudioOutput: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_AudioOutput(self, AudioOutput: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_AudioOutputStream(self, AudioOutputStream: POINTER(Windows.Win32.Media.Speech.ISpeechBaseStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_AudioOutputStream(self, AudioOutputStream: Windows.Win32.Media.Speech.ISpeechBaseStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Rate(self, Rate: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Rate(self, Rate: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Volume(self, Volume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Volume(self, Volume: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowAudioOutputFormatChangesOnNextSet(self, Allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_AllowAudioOutputFormatChangesOnNextSet(self, Allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_EventInterests(self, EventInterestFlags: POINTER(Windows.Win32.Media.Speech.SpeechVoiceEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_EventInterests(self, EventInterestFlags: Windows.Win32.Media.Speech.SpeechVoiceEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Priority(self, Priority: Windows.Win32.Media.Speech.SpeechVoicePriority) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Priority(self, Priority: POINTER(Windows.Win32.Media.Speech.SpeechVoicePriority)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AlertBoundary(self, Boundary: Windows.Win32.Media.Speech.SpeechVoiceEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AlertBoundary(self, Boundary: POINTER(Windows.Win32.Media.Speech.SpeechVoiceEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_SynchronousSpeakTimeout(self, msTimeout: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_SynchronousSpeakTimeout(self, msTimeout: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Speak(self, Text: Windows.Win32.Foundation.BSTR, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SpeakStream(self, Stream: Windows.Win32.Media.Speech.ISpeechBaseStream_head, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Skip(self, Type: Windows.Win32.Foundation.BSTR, NumItems: Int32, NumSkipped: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetVoices(self, RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetAudioOutputs(self, RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def WaitUntilDone(self, msTimeout: Int32, Done: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SpeakCompleteEvent(self, Handle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def IsUISupported(self, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Variant.VARIANT_head), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def DisplayUI(self, hWndParent: Int32, Title: Windows.Win32.Foundation.BSTR, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechVoiceStatus(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8be47b07-57f6-11d2-9eee-00c04f797396}')
    @commethod(7)
    def get_CurrentStreamNumber(self, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LastStreamNumberQueued(self, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LastHResult(self, HResult: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RunningState(self, State: POINTER(Windows.Win32.Media.Speech.SpeechRunState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InputWordPosition(self, Position: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InputWordLength(self, Length: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_InputSentencePosition(self, Position: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_InputSentenceLength(self, Length: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LastBookmark(self, Bookmark: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_LastBookmarkId(self, BookmarkId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_PhonemeId(self, PhoneId: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_VisemeId(self, VisemeId: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechWaveFormatEx(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7a1ef0d5-1581-4741-88e4-209a49f11a10}')
    @commethod(7)
    def get_FormatTag(self, FormatTag: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_FormatTag(self, FormatTag: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Channels(self, Channels: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Channels(self, Channels: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SamplesPerSec(self, SamplesPerSec: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SamplesPerSec(self, SamplesPerSec: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AvgBytesPerSec(self, AvgBytesPerSec: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AvgBytesPerSec(self, AvgBytesPerSec: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_BlockAlign(self, BlockAlign: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_BlockAlign(self, BlockAlign: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BitsPerSample(self, BitsPerSample: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BitsPerSample(self, BitsPerSample: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ExtraData(self, ExtraData: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ExtraData(self, ExtraData: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechXMLRecoResult(ComPtr):
    extends: Windows.Win32.Media.Speech.ISpeechRecoResult
    _iid_ = Guid('{aaec54af-8f85-4924-944d-b79d39d72e19}')
    @commethod(17)
    def GetXMLResult(self, Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetXMLErrorInfo(self, LineNumber: POINTER(Int32), ScriptLine: POINTER(Windows.Win32.Foundation.BSTR), Source: POINTER(Windows.Win32.Foundation.BSTR), Description: POINTER(Windows.Win32.Foundation.BSTR), ResultCode: POINTER(Int32), IsError: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
PHONETICALPHABET = Int32
PA_Ipa: PHONETICALPHABET = 0
PA_Ups: PHONETICALPHABET = 1
PA_Sapi: PHONETICALPHABET = 2
SPADAPTATIONRELEVANCE = Int32
SPAR_Unknown: SPADAPTATIONRELEVANCE = 0
SPAR_Low: SPADAPTATIONRELEVANCE = 1
SPAR_Medium: SPADAPTATIONRELEVANCE = 2
SPAR_High: SPADAPTATIONRELEVANCE = 3
SPADAPTATIONSETTINGS = Int32
SPADS_Default: SPADAPTATIONSETTINGS = 0
SPADS_CurrentRecognizer: SPADAPTATIONSETTINGS = 1
SPADS_RecoProfile: SPADAPTATIONSETTINGS = 2
SPADS_Immediate: SPADAPTATIONSETTINGS = 4
SPADS_Reset: SPADAPTATIONSETTINGS = 8
SPADS_HighVolumeDataSource: SPADAPTATIONSETTINGS = 16
class SPAUDIOBUFFERINFO(EasyCastStructure):
    ulMsMinNotification: UInt32
    ulMsBufferSize: UInt32
    ulMsEventBias: UInt32
SPAUDIOOPTIONS = Int32
SPAO_NONE: SPAUDIOOPTIONS = 0
SPAO_RETAIN_AUDIO: SPAUDIOOPTIONS = 1
SPAUDIOSTATE = Int32
SPAS_CLOSED: SPAUDIOSTATE = 0
SPAS_STOP: SPAUDIOSTATE = 1
SPAS_PAUSE: SPAUDIOSTATE = 2
SPAS_RUN: SPAUDIOSTATE = 3
class SPAUDIOSTATUS(EasyCastStructure):
    cbFreeBuffSpace: Int32
    cbNonBlockingIO: UInt32
    State: Windows.Win32.Media.Speech.SPAUDIOSTATE
    CurSeekPos: UInt64
    CurDevicePos: UInt64
    dwAudioLevel: UInt32
    dwReserved2: UInt32
class SPBINARYGRAMMAR(EasyCastStructure):
    ulTotalSerializedSize: UInt32
SPBOOKMARKOPTIONS = Int32
SPBO_NONE: SPBOOKMARKOPTIONS = 0
SPBO_PAUSE: SPBOOKMARKOPTIONS = 1
SPBO_AHEAD: SPBOOKMARKOPTIONS = 2
SPBO_TIME_UNITS: SPBOOKMARKOPTIONS = 4
SPCFGRULEATTRIBUTES = Int32
SPRAF_TopLevel: SPCFGRULEATTRIBUTES = 1
SPRAF_Active: SPCFGRULEATTRIBUTES = 2
SPRAF_Export: SPCFGRULEATTRIBUTES = 4
SPRAF_Import: SPCFGRULEATTRIBUTES = 8
SPRAF_Interpreter: SPCFGRULEATTRIBUTES = 16
SPRAF_Dynamic: SPCFGRULEATTRIBUTES = 32
SPRAF_Root: SPCFGRULEATTRIBUTES = 64
SPRAF_AutoPause: SPCFGRULEATTRIBUTES = 65536
SPRAF_UserDelimited: SPCFGRULEATTRIBUTES = 131072
SPCOMMITFLAGS = Int32
SPCF_NONE: SPCOMMITFLAGS = 0
SPCF_ADD_TO_USER_LEXICON: SPCOMMITFLAGS = 1
SPCF_DEFINITE_CORRECTION: SPCOMMITFLAGS = 2
SPCONTEXTSTATE = Int32
SPCS_DISABLED: SPCONTEXTSTATE = 0
SPCS_ENABLED: SPCONTEXTSTATE = 1
SPDATAKEYLOCATION = Int32
SPDKL_DefaultLocation: SPDATAKEYLOCATION = 0
SPDKL_CurrentUser: SPDATAKEYLOCATION = 1
SPDKL_LocalMachine: SPDATAKEYLOCATION = 2
SPDKL_CurrentConfig: SPDATAKEYLOCATION = 5
SPDISPLAYATTRIBUTES = Int32
SPAF_ONE_TRAILING_SPACE: SPDISPLAYATTRIBUTES = 2
SPAF_TWO_TRAILING_SPACES: SPDISPLAYATTRIBUTES = 4
SPAF_CONSUME_LEADING_SPACES: SPDISPLAYATTRIBUTES = 8
SPAF_BUFFER_POSITION: SPDISPLAYATTRIBUTES = 16
SPAF_ALL: SPDISPLAYATTRIBUTES = 31
SPAF_USER_SPECIFIED: SPDISPLAYATTRIBUTES = 128
class SPDISPLAYPHRASE(EasyCastStructure):
    ulNumTokens: UInt32
    pTokens: POINTER(Windows.Win32.Media.Speech.SPDISPLAYTOKEN_head)
class SPDISPLAYTOKEN(EasyCastStructure):
    pszLexical: Windows.Win32.Foundation.PWSTR
    pszDisplay: Windows.Win32.Foundation.PWSTR
    bDisplayAttributes: Byte
SPEAKFLAGS = Int32
SPF_DEFAULT: SPEAKFLAGS = 0
SPF_ASYNC: SPEAKFLAGS = 1
SPF_PURGEBEFORESPEAK: SPEAKFLAGS = 2
SPF_IS_FILENAME: SPEAKFLAGS = 4
SPF_IS_XML: SPEAKFLAGS = 8
SPF_IS_NOT_XML: SPEAKFLAGS = 16
SPF_PERSIST_XML: SPEAKFLAGS = 32
SPF_NLP_SPEAK_PUNC: SPEAKFLAGS = 64
SPF_PARSE_SAPI: SPEAKFLAGS = 128
SPF_PARSE_SSML: SPEAKFLAGS = 256
SPF_PARSE_AUTODETECT: SPEAKFLAGS = 0
SPF_NLP_MASK: SPEAKFLAGS = 64
SPF_PARSE_MASK: SPEAKFLAGS = 384
SPF_VOICE_MASK: SPEAKFLAGS = 511
SPF_UNUSED_FLAGS: SPEAKFLAGS = -512
SPENDSRSTREAMFLAGS = Int32
SPESF_NONE: SPENDSRSTREAMFLAGS = 0
SPESF_STREAM_RELEASED: SPENDSRSTREAMFLAGS = 1
SPESF_EMULATED: SPENDSRSTREAMFLAGS = 2
class SPEVENT(EasyCastStructure):
    _bitfield: Int32
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    wParam: Windows.Win32.Foundation.WPARAM
    lParam: Windows.Win32.Foundation.LPARAM
SPEVENTENUM = Int32
SPEI_UNDEFINED: SPEVENTENUM = 0
SPEI_START_INPUT_STREAM: SPEVENTENUM = 1
SPEI_END_INPUT_STREAM: SPEVENTENUM = 2
SPEI_VOICE_CHANGE: SPEVENTENUM = 3
SPEI_TTS_BOOKMARK: SPEVENTENUM = 4
SPEI_WORD_BOUNDARY: SPEVENTENUM = 5
SPEI_PHONEME: SPEVENTENUM = 6
SPEI_SENTENCE_BOUNDARY: SPEVENTENUM = 7
SPEI_VISEME: SPEVENTENUM = 8
SPEI_TTS_AUDIO_LEVEL: SPEVENTENUM = 9
SPEI_TTS_PRIVATE: SPEVENTENUM = 15
SPEI_MIN_TTS: SPEVENTENUM = 1
SPEI_MAX_TTS: SPEVENTENUM = 15
SPEI_END_SR_STREAM: SPEVENTENUM = 34
SPEI_SOUND_START: SPEVENTENUM = 35
SPEI_SOUND_END: SPEVENTENUM = 36
SPEI_PHRASE_START: SPEVENTENUM = 37
SPEI_RECOGNITION: SPEVENTENUM = 38
SPEI_HYPOTHESIS: SPEVENTENUM = 39
SPEI_SR_BOOKMARK: SPEVENTENUM = 40
SPEI_PROPERTY_NUM_CHANGE: SPEVENTENUM = 41
SPEI_PROPERTY_STRING_CHANGE: SPEVENTENUM = 42
SPEI_FALSE_RECOGNITION: SPEVENTENUM = 43
SPEI_INTERFERENCE: SPEVENTENUM = 44
SPEI_REQUEST_UI: SPEVENTENUM = 45
SPEI_RECO_STATE_CHANGE: SPEVENTENUM = 46
SPEI_ADAPTATION: SPEVENTENUM = 47
SPEI_START_SR_STREAM: SPEVENTENUM = 48
SPEI_RECO_OTHER_CONTEXT: SPEVENTENUM = 49
SPEI_SR_AUDIO_LEVEL: SPEVENTENUM = 50
SPEI_SR_RETAINEDAUDIO: SPEVENTENUM = 51
SPEI_SR_PRIVATE: SPEVENTENUM = 52
SPEI_RESERVED4: SPEVENTENUM = 53
SPEI_RESERVED5: SPEVENTENUM = 54
SPEI_RESERVED6: SPEVENTENUM = 55
SPEI_MIN_SR: SPEVENTENUM = 34
SPEI_MAX_SR: SPEVENTENUM = 55
SPEI_RESERVED1: SPEVENTENUM = 30
SPEI_RESERVED2: SPEVENTENUM = 33
SPEI_RESERVED3: SPEVENTENUM = 63
class SPEVENTEX(EasyCastStructure):
    _bitfield: Int32
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    wParam: Windows.Win32.Foundation.WPARAM
    lParam: Windows.Win32.Foundation.LPARAM
    ullAudioTimeOffset: UInt64
SPEVENTLPARAMTYPE = Int32
SPET_LPARAM_IS_UNDEFINED: SPEVENTLPARAMTYPE = 0
SPET_LPARAM_IS_TOKEN: SPEVENTLPARAMTYPE = 1
SPET_LPARAM_IS_OBJECT: SPEVENTLPARAMTYPE = 2
SPET_LPARAM_IS_POINTER: SPEVENTLPARAMTYPE = 3
SPET_LPARAM_IS_STRING: SPEVENTLPARAMTYPE = 4
class SPEVENTSOURCEINFO(EasyCastStructure):
    ullEventInterest: UInt64
    ullQueuedInterest: UInt64
    ulCount: UInt32
SPFILEMODE = Int32
SPFM_OPEN_READONLY: SPFILEMODE = 0
SPFM_OPEN_READWRITE: SPFILEMODE = 1
SPFM_CREATE: SPFILEMODE = 2
SPFM_CREATE_ALWAYS: SPFILEMODE = 3
SPFM_NUM_MODES: SPFILEMODE = 4
SPGRAMMARHANDLE = IntPtr
SPGRAMMAROPTIONS = Int32
SPGO_SAPI: SPGRAMMAROPTIONS = 1
SPGO_SRGS: SPGRAMMAROPTIONS = 2
SPGO_UPS: SPGRAMMAROPTIONS = 4
SPGO_SRGS_MS_SCRIPT: SPGRAMMAROPTIONS = 8
SPGO_SRGS_W3C_SCRIPT: SPGRAMMAROPTIONS = 256
SPGO_SRGS_STG_SCRIPT: SPGRAMMAROPTIONS = 512
SPGO_SRGS_SCRIPT: SPGRAMMAROPTIONS = 778
SPGO_FILE: SPGRAMMAROPTIONS = 16
SPGO_HTTP: SPGRAMMAROPTIONS = 32
SPGO_RES: SPGRAMMAROPTIONS = 64
SPGO_OBJECT: SPGRAMMAROPTIONS = 128
SPGO_DEFAULT: SPGRAMMAROPTIONS = 1019
SPGO_ALL: SPGRAMMAROPTIONS = 1023
SPGRAMMARSTATE = Int32
SPGS_DISABLED: SPGRAMMARSTATE = 0
SPGS_ENABLED: SPGRAMMARSTATE = 1
SPGS_EXCLUSIVE: SPGRAMMARSTATE = 3
SPGRAMMARWORDTYPE = Int32
SPWT_DISPLAY: SPGRAMMARWORDTYPE = 0
SPWT_LEXICAL: SPGRAMMARWORDTYPE = 1
SPWT_PRONUNCIATION: SPGRAMMARWORDTYPE = 2
SPWT_LEXICAL_NO_SPECIAL_CHARS: SPGRAMMARWORDTYPE = 3
SPINTERFERENCE = Int32
SPINTERFERENCE_NONE: SPINTERFERENCE = 0
SPINTERFERENCE_NOISE: SPINTERFERENCE = 1
SPINTERFERENCE_NOSIGNAL: SPINTERFERENCE = 2
SPINTERFERENCE_TOOLOUD: SPINTERFERENCE = 3
SPINTERFERENCE_TOOQUIET: SPINTERFERENCE = 4
SPINTERFERENCE_TOOFAST: SPINTERFERENCE = 5
SPINTERFERENCE_TOOSLOW: SPINTERFERENCE = 6
SPINTERFERENCE_LATENCY_WARNING: SPINTERFERENCE = 7
SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN: SPINTERFERENCE = 8
SPINTERFERENCE_LATENCY_TRUNCATE_END: SPINTERFERENCE = 9
SPLEXICONTYPE = Int32
eLEXTYPE_USER: SPLEXICONTYPE = 1
eLEXTYPE_APP: SPLEXICONTYPE = 2
eLEXTYPE_VENDORLEXICON: SPLEXICONTYPE = 4
eLEXTYPE_LETTERTOSOUND: SPLEXICONTYPE = 8
eLEXTYPE_MORPHOLOGY: SPLEXICONTYPE = 16
eLEXTYPE_RESERVED4: SPLEXICONTYPE = 32
eLEXTYPE_USER_SHORTCUT: SPLEXICONTYPE = 64
eLEXTYPE_RESERVED6: SPLEXICONTYPE = 128
eLEXTYPE_RESERVED7: SPLEXICONTYPE = 256
eLEXTYPE_RESERVED8: SPLEXICONTYPE = 512
eLEXTYPE_RESERVED9: SPLEXICONTYPE = 1024
eLEXTYPE_RESERVED10: SPLEXICONTYPE = 2048
eLEXTYPE_PRIVATE1: SPLEXICONTYPE = 4096
eLEXTYPE_PRIVATE2: SPLEXICONTYPE = 8192
eLEXTYPE_PRIVATE3: SPLEXICONTYPE = 16384
eLEXTYPE_PRIVATE4: SPLEXICONTYPE = 32768
eLEXTYPE_PRIVATE5: SPLEXICONTYPE = 65536
eLEXTYPE_PRIVATE6: SPLEXICONTYPE = 131072
eLEXTYPE_PRIVATE7: SPLEXICONTYPE = 262144
eLEXTYPE_PRIVATE8: SPLEXICONTYPE = 524288
eLEXTYPE_PRIVATE9: SPLEXICONTYPE = 1048576
eLEXTYPE_PRIVATE10: SPLEXICONTYPE = 2097152
eLEXTYPE_PRIVATE11: SPLEXICONTYPE = 4194304
eLEXTYPE_PRIVATE12: SPLEXICONTYPE = 8388608
eLEXTYPE_PRIVATE13: SPLEXICONTYPE = 16777216
eLEXTYPE_PRIVATE14: SPLEXICONTYPE = 33554432
eLEXTYPE_PRIVATE15: SPLEXICONTYPE = 67108864
eLEXTYPE_PRIVATE16: SPLEXICONTYPE = 134217728
eLEXTYPE_PRIVATE17: SPLEXICONTYPE = 268435456
eLEXTYPE_PRIVATE18: SPLEXICONTYPE = 536870912
eLEXTYPE_PRIVATE19: SPLEXICONTYPE = 1073741824
eLEXTYPE_PRIVATE20: SPLEXICONTYPE = -2147483648
SPLOADOPTIONS = Int32
SPLO_STATIC: SPLOADOPTIONS = 0
SPLO_DYNAMIC: SPLOADOPTIONS = 1
SPMATCHINGMODE = Int32
SPMATCHINGMODE_AllWords: SPMATCHINGMODE = 0
SPMATCHINGMODE_Subsequence: SPMATCHINGMODE = 1
SPMATCHINGMODE_OrderedSubset: SPMATCHINGMODE = 3
SPMATCHINGMODE_SubsequenceContentRequired: SPMATCHINGMODE = 5
SPMATCHINGMODE_OrderedSubsetContentRequired: SPMATCHINGMODE = 7
class SPNORMALIZATIONLIST(EasyCastStructure):
    ulSize: UInt32
    ppszzNormalizedList: POINTER(POINTER(UInt16))
@winfunctype_pointer
def SPNOTIFYCALLBACK(wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Void: ...
SPPARTOFSPEECH = Int32
SPPS_NotOverriden: SPPARTOFSPEECH = -1
SPPS_Unknown: SPPARTOFSPEECH = 0
SPPS_Noun: SPPARTOFSPEECH = 4096
SPPS_Verb: SPPARTOFSPEECH = 8192
SPPS_Modifier: SPPARTOFSPEECH = 12288
SPPS_Function: SPPARTOFSPEECH = 16384
SPPS_Interjection: SPPARTOFSPEECH = 20480
SPPS_Noncontent: SPPARTOFSPEECH = 24576
SPPS_LMA: SPPARTOFSPEECH = 28672
SPPS_SuppressWord: SPPARTOFSPEECH = 61440
class SPPHRASE(EasyCastStructure):
    Base: Windows.Win32.Media.Speech.SPPHRASE_50
    pSML: Windows.Win32.Foundation.PWSTR
    pSemanticErrorInfo: POINTER(Windows.Win32.Media.Speech.SPSEMANTICERRORINFO_head)
class SPPHRASEELEMENT(EasyCastStructure):
    ulAudioTimeOffset: UInt32
    ulAudioSizeTime: UInt32
    ulAudioStreamOffset: UInt32
    ulAudioSizeBytes: UInt32
    ulRetainedStreamOffset: UInt32
    ulRetainedSizeBytes: UInt32
    pszDisplayText: Windows.Win32.Foundation.PWSTR
    pszLexicalForm: Windows.Win32.Foundation.PWSTR
    pszPronunciation: POINTER(UInt16)
    bDisplayAttributes: Byte
    RequiredConfidence: SByte
    ActualConfidence: SByte
    Reserved: Byte
    SREngineConfidence: Single
class SPPHRASEPROPERTY(EasyCastStructure):
    pszName: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    pszValue: Windows.Win32.Foundation.PWSTR
    vValue: Windows.Win32.System.Variant.VARIANT
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
    pNextSibling: POINTER(Windows.Win32.Media.Speech.SPPHRASEPROPERTY_head)
    pFirstChild: POINTER(Windows.Win32.Media.Speech.SPPHRASEPROPERTY_head)
    SREngineConfidence: Single
    Confidence: SByte
    class _Anonymous_e__Union(EasyCastUnion):
        ulId: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            bType: Byte
            bReserved: Byte
            usArrayIndex: UInt16
SPPHRASEPROPERTYHANDLE = IntPtr
SPPHRASEPROPERTYUNIONTYPE = Int32
SPPPUT_UNUSED: SPPHRASEPROPERTYUNIONTYPE = 0
SPPPUT_ARRAY_INDEX: SPPHRASEPROPERTYUNIONTYPE = 1
class SPPHRASEREPLACEMENT(EasyCastStructure):
    bDisplayAttributes: Byte
    pszReplacementText: Windows.Win32.Foundation.PWSTR
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
SPPHRASERNG = Int32
SPPR_ALL_ELEMENTS: SPPHRASERNG = -1
class SPPHRASERULE(EasyCastStructure):
    pszName: Windows.Win32.Foundation.PWSTR
    ulId: UInt32
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
    pNextSibling: POINTER(Windows.Win32.Media.Speech.SPPHRASERULE_head)
    pFirstChild: POINTER(Windows.Win32.Media.Speech.SPPHRASERULE_head)
    SREngineConfidence: Single
    Confidence: SByte
SPPHRASERULEHANDLE = IntPtr
class SPPHRASE_50(EasyCastStructure):
    cbSize: UInt32
    LangID: UInt16
    wHomophoneGroupId: UInt16
    ullGrammarID: UInt64
    ftStartTime: UInt64
    ullAudioStreamPosition: UInt64
    ulAudioSizeBytes: UInt32
    ulRetainedSizeBytes: UInt32
    ulAudioSizeTime: UInt32
    Rule: Windows.Win32.Media.Speech.SPPHRASERULE
    pProperties: POINTER(Windows.Win32.Media.Speech.SPPHRASEPROPERTY_head)
    pElements: POINTER(Windows.Win32.Media.Speech.SPPHRASEELEMENT_head)
    cReplacements: UInt32
    pReplacements: POINTER(Windows.Win32.Media.Speech.SPPHRASEREPLACEMENT_head)
    SREngineID: Guid
    ulSREnginePrivateDataSize: UInt32
    pSREnginePrivateData: POINTER(Byte)
SPPRONUNCIATIONFLAGS = Int32
ePRONFLAG_USED: SPPRONUNCIATIONFLAGS = 1
class SPPROPERTYINFO(EasyCastStructure):
    pszName: Windows.Win32.Foundation.PWSTR
    ulId: UInt32
    pszValue: Windows.Win32.Foundation.PWSTR
    vValue: Windows.Win32.System.Variant.VARIANT
SPRECOCONTEXTHANDLE = IntPtr
class SPRECOCONTEXTSTATUS(EasyCastStructure):
    eInterference: Windows.Win32.Media.Speech.SPINTERFERENCE
    szRequestTypeOfUI: Char * 255
    dwReserved1: UInt32
    dwReserved2: UInt32
SPRECOEVENTFLAGS = Int32
SPREF_AutoPause: SPRECOEVENTFLAGS = 1
SPREF_Emulated: SPRECOEVENTFLAGS = 2
SPREF_SMLTimeout: SPRECOEVENTFLAGS = 4
SPREF_ExtendableParse: SPRECOEVENTFLAGS = 8
SPREF_ReSent: SPRECOEVENTFLAGS = 16
SPREF_Hypothesis: SPRECOEVENTFLAGS = 32
SPREF_FalseRecognition: SPRECOEVENTFLAGS = 64
class SPRECOGNIZERSTATUS(EasyCastStructure):
    AudioStatus: Windows.Win32.Media.Speech.SPAUDIOSTATUS
    ullRecognitionStreamPos: UInt64
    ulStreamNumber: UInt32
    ulNumActive: UInt32
    clsidEngine: Guid
    cLangIDs: UInt32
    aLangID: UInt16 * 20
    ullRecognitionStreamTime: UInt64
class SPRECORESULTTIMES(EasyCastStructure):
    ftStreamTime: Windows.Win32.Foundation.FILETIME
    ullLength: UInt64
    dwTickCount: UInt32
    ullStart: UInt64
SPRECOSTATE = Int32
SPRST_INACTIVE: SPRECOSTATE = 0
SPRST_ACTIVE: SPRECOSTATE = 1
SPRST_ACTIVE_ALWAYS: SPRECOSTATE = 2
SPRST_INACTIVE_WITH_PURGE: SPRECOSTATE = 3
SPRST_NUM_STATES: SPRECOSTATE = 4
class SPRULE(EasyCastStructure):
    pszRuleName: Windows.Win32.Foundation.PWSTR
    ulRuleId: UInt32
    dwAttributes: UInt32
SPRULEHANDLE = IntPtr
SPRULESTATE = Int32
SPRS_INACTIVE: SPRULESTATE = 0
SPRS_ACTIVE: SPRULESTATE = 1
SPRS_ACTIVE_WITH_AUTO_PAUSE: SPRULESTATE = 3
SPRS_ACTIVE_USER_DELIMITED: SPRULESTATE = 4
SPRUNSTATE = Int32
SPRS_DONE: SPRUNSTATE = 1
SPRS_IS_SPEAKING: SPRUNSTATE = 2
class SPSEMANTICERRORINFO(EasyCastStructure):
    ulLineNumber: UInt32
    pszScriptLine: Windows.Win32.Foundation.PWSTR
    pszSource: Windows.Win32.Foundation.PWSTR
    pszDescription: Windows.Win32.Foundation.PWSTR
    hrResultCode: Windows.Win32.Foundation.HRESULT
SPSEMANTICFORMAT = Int32
SPSMF_SAPI_PROPERTIES: SPSEMANTICFORMAT = 0
SPSMF_SRGS_SEMANTICINTERPRETATION_MS: SPSEMANTICFORMAT = 1
SPSMF_SRGS_SAPIPROPERTIES: SPSEMANTICFORMAT = 2
SPSMF_UPS: SPSEMANTICFORMAT = 4
SPSMF_SRGS_SEMANTICINTERPRETATION_W3C: SPSEMANTICFORMAT = 8
class SPSERIALIZEDEVENT(EasyCastStructure):
    _bitfield: Int32
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    SerializedwParam: UInt32
    SerializedlParam: Int32
class SPSERIALIZEDEVENT64(EasyCastStructure):
    _bitfield: Int32
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    SerializedwParam: UInt64
    SerializedlParam: Int64
class SPSERIALIZEDPHRASE(EasyCastStructure):
    ulSerializedSize: UInt32
class SPSERIALIZEDRESULT(EasyCastStructure):
    ulSerializedSize: UInt32
class SPSHORTCUTPAIR(EasyCastStructure):
    pNextSHORTCUTPAIR: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIR_head)
    LangID: UInt16
    shType: Windows.Win32.Media.Speech.SPSHORTCUTTYPE
    pszDisplay: Windows.Win32.Foundation.PWSTR
    pszSpoken: Windows.Win32.Foundation.PWSTR
class SPSHORTCUTPAIRLIST(EasyCastStructure):
    ulSize: UInt32
    pvBuffer: POINTER(Byte)
    pFirstShortcutPair: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIR_head)
SPSHORTCUTTYPE = Int32
SPSHT_NotOverriden: SPSHORTCUTTYPE = -1
SPSHT_Unknown: SPSHORTCUTTYPE = 0
SPSHT_EMAIL: SPSHORTCUTTYPE = 4096
SPSHT_OTHER: SPSHORTCUTTYPE = 8192
SPPS_RESERVED1: SPSHORTCUTTYPE = 12288
SPPS_RESERVED2: SPSHORTCUTTYPE = 16384
SPPS_RESERVED3: SPSHORTCUTTYPE = 20480
SPPS_RESERVED4: SPSHORTCUTTYPE = 61440
SPSTATEHANDLE = IntPtr
SPSTREAMFORMAT = Int32
SPSF_Default: SPSTREAMFORMAT = -1
SPSF_NoAssignedFormat: SPSTREAMFORMAT = 0
SPSF_Text: SPSTREAMFORMAT = 1
SPSF_NonStandardFormat: SPSTREAMFORMAT = 2
SPSF_ExtendedAudioFormat: SPSTREAMFORMAT = 3
SPSF_8kHz8BitMono: SPSTREAMFORMAT = 4
SPSF_8kHz8BitStereo: SPSTREAMFORMAT = 5
SPSF_8kHz16BitMono: SPSTREAMFORMAT = 6
SPSF_8kHz16BitStereo: SPSTREAMFORMAT = 7
SPSF_11kHz8BitMono: SPSTREAMFORMAT = 8
SPSF_11kHz8BitStereo: SPSTREAMFORMAT = 9
SPSF_11kHz16BitMono: SPSTREAMFORMAT = 10
SPSF_11kHz16BitStereo: SPSTREAMFORMAT = 11
SPSF_12kHz8BitMono: SPSTREAMFORMAT = 12
SPSF_12kHz8BitStereo: SPSTREAMFORMAT = 13
SPSF_12kHz16BitMono: SPSTREAMFORMAT = 14
SPSF_12kHz16BitStereo: SPSTREAMFORMAT = 15
SPSF_16kHz8BitMono: SPSTREAMFORMAT = 16
SPSF_16kHz8BitStereo: SPSTREAMFORMAT = 17
SPSF_16kHz16BitMono: SPSTREAMFORMAT = 18
SPSF_16kHz16BitStereo: SPSTREAMFORMAT = 19
SPSF_22kHz8BitMono: SPSTREAMFORMAT = 20
SPSF_22kHz8BitStereo: SPSTREAMFORMAT = 21
SPSF_22kHz16BitMono: SPSTREAMFORMAT = 22
SPSF_22kHz16BitStereo: SPSTREAMFORMAT = 23
SPSF_24kHz8BitMono: SPSTREAMFORMAT = 24
SPSF_24kHz8BitStereo: SPSTREAMFORMAT = 25
SPSF_24kHz16BitMono: SPSTREAMFORMAT = 26
SPSF_24kHz16BitStereo: SPSTREAMFORMAT = 27
SPSF_32kHz8BitMono: SPSTREAMFORMAT = 28
SPSF_32kHz8BitStereo: SPSTREAMFORMAT = 29
SPSF_32kHz16BitMono: SPSTREAMFORMAT = 30
SPSF_32kHz16BitStereo: SPSTREAMFORMAT = 31
SPSF_44kHz8BitMono: SPSTREAMFORMAT = 32
SPSF_44kHz8BitStereo: SPSTREAMFORMAT = 33
SPSF_44kHz16BitMono: SPSTREAMFORMAT = 34
SPSF_44kHz16BitStereo: SPSTREAMFORMAT = 35
SPSF_48kHz8BitMono: SPSTREAMFORMAT = 36
SPSF_48kHz8BitStereo: SPSTREAMFORMAT = 37
SPSF_48kHz16BitMono: SPSTREAMFORMAT = 38
SPSF_48kHz16BitStereo: SPSTREAMFORMAT = 39
SPSF_TrueSpeech_8kHz1BitMono: SPSTREAMFORMAT = 40
SPSF_CCITT_ALaw_8kHzMono: SPSTREAMFORMAT = 41
SPSF_CCITT_ALaw_8kHzStereo: SPSTREAMFORMAT = 42
SPSF_CCITT_ALaw_11kHzMono: SPSTREAMFORMAT = 43
SPSF_CCITT_ALaw_11kHzStereo: SPSTREAMFORMAT = 44
SPSF_CCITT_ALaw_22kHzMono: SPSTREAMFORMAT = 45
SPSF_CCITT_ALaw_22kHzStereo: SPSTREAMFORMAT = 46
SPSF_CCITT_ALaw_44kHzMono: SPSTREAMFORMAT = 47
SPSF_CCITT_ALaw_44kHzStereo: SPSTREAMFORMAT = 48
SPSF_CCITT_uLaw_8kHzMono: SPSTREAMFORMAT = 49
SPSF_CCITT_uLaw_8kHzStereo: SPSTREAMFORMAT = 50
SPSF_CCITT_uLaw_11kHzMono: SPSTREAMFORMAT = 51
SPSF_CCITT_uLaw_11kHzStereo: SPSTREAMFORMAT = 52
SPSF_CCITT_uLaw_22kHzMono: SPSTREAMFORMAT = 53
SPSF_CCITT_uLaw_22kHzStereo: SPSTREAMFORMAT = 54
SPSF_CCITT_uLaw_44kHzMono: SPSTREAMFORMAT = 55
SPSF_CCITT_uLaw_44kHzStereo: SPSTREAMFORMAT = 56
SPSF_ADPCM_8kHzMono: SPSTREAMFORMAT = 57
SPSF_ADPCM_8kHzStereo: SPSTREAMFORMAT = 58
SPSF_ADPCM_11kHzMono: SPSTREAMFORMAT = 59
SPSF_ADPCM_11kHzStereo: SPSTREAMFORMAT = 60
SPSF_ADPCM_22kHzMono: SPSTREAMFORMAT = 61
SPSF_ADPCM_22kHzStereo: SPSTREAMFORMAT = 62
SPSF_ADPCM_44kHzMono: SPSTREAMFORMAT = 63
SPSF_ADPCM_44kHzStereo: SPSTREAMFORMAT = 64
SPSF_GSM610_8kHzMono: SPSTREAMFORMAT = 65
SPSF_GSM610_11kHzMono: SPSTREAMFORMAT = 66
SPSF_GSM610_22kHzMono: SPSTREAMFORMAT = 67
SPSF_GSM610_44kHzMono: SPSTREAMFORMAT = 68
SPSF_NUM_FORMATS: SPSTREAMFORMAT = 69
SPSTREAMFORMATTYPE = Int32
SPWF_INPUT: SPSTREAMFORMATTYPE = 0
SPWF_SRENGINE: SPSTREAMFORMATTYPE = 1
class SPTEXTSELECTIONINFO(EasyCastStructure):
    ulStartActiveOffset: UInt32
    cchActiveChars: UInt32
    ulStartSelection: UInt32
    cchSelection: UInt32
SPTRANSITIONID = IntPtr
SPVACTIONS = Int32
SPVA_Speak: SPVACTIONS = 0
SPVA_Silence: SPVACTIONS = 1
SPVA_Pronounce: SPVACTIONS = 2
SPVA_Bookmark: SPVACTIONS = 3
SPVA_SpellOut: SPVACTIONS = 4
SPVA_Section: SPVACTIONS = 5
SPVA_ParseUnknownTag: SPVACTIONS = 6
SPVALUETYPE = Int32
SPDF_PROPERTY: SPVALUETYPE = 1
SPDF_REPLACEMENT: SPVALUETYPE = 2
SPDF_RULE: SPVALUETYPE = 4
SPDF_DISPLAYTEXT: SPVALUETYPE = 8
SPDF_LEXICALFORM: SPVALUETYPE = 16
SPDF_PRONUNCIATION: SPVALUETYPE = 32
SPDF_AUDIO: SPVALUETYPE = 64
SPDF_ALTERNATES: SPVALUETYPE = 128
SPDF_ALL: SPVALUETYPE = 255
class SPVCONTEXT(EasyCastStructure):
    pCategory: Windows.Win32.Foundation.PWSTR
    pBefore: Windows.Win32.Foundation.PWSTR
    pAfter: Windows.Win32.Foundation.PWSTR
SPVFEATURE = Int32
SPVFEATURE_STRESSED: SPVFEATURE = 1
SPVFEATURE_EMPHASIS: SPVFEATURE = 2
SPVISEMES = Int32
SP_VISEME_0: SPVISEMES = 0
SP_VISEME_1: SPVISEMES = 1
SP_VISEME_2: SPVISEMES = 2
SP_VISEME_3: SPVISEMES = 3
SP_VISEME_4: SPVISEMES = 4
SP_VISEME_5: SPVISEMES = 5
SP_VISEME_6: SPVISEMES = 6
SP_VISEME_7: SPVISEMES = 7
SP_VISEME_8: SPVISEMES = 8
SP_VISEME_9: SPVISEMES = 9
SP_VISEME_10: SPVISEMES = 10
SP_VISEME_11: SPVISEMES = 11
SP_VISEME_12: SPVISEMES = 12
SP_VISEME_13: SPVISEMES = 13
SP_VISEME_14: SPVISEMES = 14
SP_VISEME_15: SPVISEMES = 15
SP_VISEME_16: SPVISEMES = 16
SP_VISEME_17: SPVISEMES = 17
SP_VISEME_18: SPVISEMES = 18
SP_VISEME_19: SPVISEMES = 19
SP_VISEME_20: SPVISEMES = 20
SP_VISEME_21: SPVISEMES = 21
SPVLIMITS = Int32
SPMIN_VOLUME: SPVLIMITS = 0
SPMAX_VOLUME: SPVLIMITS = 100
SPMIN_RATE: SPVLIMITS = -10
SPMAX_RATE: SPVLIMITS = 10
class SPVOICESTATUS(EasyCastStructure):
    ulCurrentStream: UInt32
    ulLastStreamQueued: UInt32
    hrLastResult: Windows.Win32.Foundation.HRESULT
    dwRunningState: UInt32
    ulInputWordPos: UInt32
    ulInputWordLen: UInt32
    ulInputSentPos: UInt32
    ulInputSentLen: UInt32
    lBookmarkId: Int32
    PhonemeId: UInt16
    VisemeId: Windows.Win32.Media.Speech.SPVISEMES
    dwReserved1: UInt32
    dwReserved2: UInt32
class SPVPITCH(EasyCastStructure):
    MiddleAdj: Int32
    RangeAdj: Int32
SPVPRIORITY = Int32
SPVPRI_NORMAL: SPVPRIORITY = 0
SPVPRI_ALERT: SPVPRIORITY = 1
SPVPRI_OVER: SPVPRIORITY = 2
class SPVSTATE(EasyCastStructure):
    eAction: Windows.Win32.Media.Speech.SPVACTIONS
    LangID: UInt16
    wReserved: UInt16
    EmphAdj: Int32
    RateAdj: Int32
    Volume: UInt32
    PitchAdj: Windows.Win32.Media.Speech.SPVPITCH
    SilenceMSecs: UInt32
    pPhoneIds: POINTER(UInt16)
    ePartOfSpeech: Windows.Win32.Media.Speech.SPPARTOFSPEECH
    Context: Windows.Win32.Media.Speech.SPVCONTEXT
class SPWORD(EasyCastStructure):
    pNextWord: POINTER(Windows.Win32.Media.Speech.SPWORD_head)
    LangID: UInt16
    wReserved: UInt16
    eWordType: Windows.Win32.Media.Speech.SPWORDTYPE
    pszWord: Windows.Win32.Foundation.PWSTR
    pFirstWordPronunciation: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATION_head)
SPWORDHANDLE = IntPtr
class SPWORDLIST(EasyCastStructure):
    ulSize: UInt32
    pvBuffer: POINTER(Byte)
    pFirstWord: POINTER(Windows.Win32.Media.Speech.SPWORD_head)
SPWORDPRONOUNCEABLE = Int32
SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE: SPWORDPRONOUNCEABLE = 0
SPWP_UNKNOWN_WORD_PRONOUNCEABLE: SPWORDPRONOUNCEABLE = 1
SPWP_KNOWN_WORD_PRONOUNCEABLE: SPWORDPRONOUNCEABLE = 2
class SPWORDPRONUNCIATION(EasyCastStructure):
    pNextWordPronunciation: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATION_head)
    eLexiconType: Windows.Win32.Media.Speech.SPLEXICONTYPE
    LangID: UInt16
    wPronunciationFlags: UInt16
    ePartOfSpeech: Windows.Win32.Media.Speech.SPPARTOFSPEECH
    szPronunciation: UInt16 * 1
class SPWORDPRONUNCIATIONLIST(EasyCastStructure):
    ulSize: UInt32
    pvBuffer: POINTER(Byte)
    pFirstWordPronunciation: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATION_head)
SPWORDTYPE = Int32
eWORDTYPE_ADDED: SPWORDTYPE = 1
eWORDTYPE_DELETED: SPWORDTYPE = 2
SPXMLRESULTOPTIONS = Int32
SPXRO_SML: SPXMLRESULTOPTIONS = 0
SPXRO_Alternates_SML: SPXMLRESULTOPTIONS = 1
SpAudioFormat = Guid('{9ef96870-e160-4792-820d-48cf0649e4ec}')
SpCompressedLexicon = Guid('{90903716-2f42-11d3-9c26-00c04f8ef87c}')
SpCustomStream = Guid('{8dbef13f-1948-4aa8-8cf0-048eebed95d8}')
SpFileStream = Guid('{947812b3-2ae1-4644-ba86-9e90ded7ec91}')
SpInProcRecoContext = Guid('{73ad6842-ace0-45e8-a4dd-8795881a2c2a}')
SpInprocRecognizer = Guid('{41b89b6b-9399-11d2-9623-00c04f8ee628}')
SpLexicon = Guid('{0655e396-25d0-11d3-9c26-00c04f8ef87c}')
SpMMAudioEnum = Guid('{ab1890a0-e91f-11d2-bb91-00c04f8ee6c0}')
SpMMAudioIn = Guid('{cf3d2e50-53f2-11d2-960c-00c04f8ee628}')
SpMMAudioOut = Guid('{a8c680eb-3d32-11d2-9ee7-00c04f797396}')
SpMemoryStream = Guid('{5fb7ef7d-dff4-468a-b6b7-2fcbd188f994}')
SpNotifyTranslator = Guid('{e2ae5372-5d40-11d2-960e-00c04f8ee628}')
SpNullPhoneConverter = Guid('{455f24e9-7396-4a16-9715-7c0fdbe3efe3}')
SpObjectToken = Guid('{ef411752-3736-4cb4-9c8c-8ef4ccb58efe}')
SpObjectTokenCategory = Guid('{a910187f-0c7a-45ac-92cc-59edafb77b53}')
SpPhoneConverter = Guid('{9185f743-1143-4c28-86b5-bff14f20e5c8}')
SpPhoneticAlphabetConverter = Guid('{4f414126-dfe3-4629-99ee-797978317ead}')
SpPhraseInfoBuilder = Guid('{c23fc28d-c55f-4720-8b32-91f73c2bd5d1}')
SpResourceManager = Guid('{96749373-3391-11d2-9ee3-00c04f797396}')
SpSharedRecoContext = Guid('{47206204-5eca-11d2-960f-00c04f8ee628}')
SpSharedRecognizer = Guid('{3bee4890-4fe9-4a37-8c1e-5e7e12791c1f}')
SpShortcut = Guid('{0d722f1a-9fcf-4e62-96d8-6df8f01a26aa}')
SpStream = Guid('{715d9c59-4442-11d2-9605-00c04f8ee628}')
SpStreamFormatConverter = Guid('{7013943a-e2ec-11d2-a086-00c04f8ef9b5}')
SpTextSelectionInformation = Guid('{0f92030a-cbfd-4ab8-a164-ff5985547ff6}')
SpUnCompressedLexicon = Guid('{c9e37c15-df92-4727-85d6-72e5eeb6995a}')
SpVoice = Guid('{96749377-3391-11d2-9ee3-00c04f797396}')
SpWaveFormatEx = Guid('{c79a574c-63be-44b9-801f-283f87f898be}')
SpeechAudioFormatType = Int32
SpeechAudioFormatType_SAFTDefault: SpeechAudioFormatType = -1
SpeechAudioFormatType_SAFTNoAssignedFormat: SpeechAudioFormatType = 0
SpeechAudioFormatType_SAFTText: SpeechAudioFormatType = 1
SpeechAudioFormatType_SAFTNonStandardFormat: SpeechAudioFormatType = 2
SpeechAudioFormatType_SAFTExtendedAudioFormat: SpeechAudioFormatType = 3
SpeechAudioFormatType_SAFT8kHz8BitMono: SpeechAudioFormatType = 4
SpeechAudioFormatType_SAFT8kHz8BitStereo: SpeechAudioFormatType = 5
SpeechAudioFormatType_SAFT8kHz16BitMono: SpeechAudioFormatType = 6
SpeechAudioFormatType_SAFT8kHz16BitStereo: SpeechAudioFormatType = 7
SpeechAudioFormatType_SAFT11kHz8BitMono: SpeechAudioFormatType = 8
SpeechAudioFormatType_SAFT11kHz8BitStereo: SpeechAudioFormatType = 9
SpeechAudioFormatType_SAFT11kHz16BitMono: SpeechAudioFormatType = 10
SpeechAudioFormatType_SAFT11kHz16BitStereo: SpeechAudioFormatType = 11
SpeechAudioFormatType_SAFT12kHz8BitMono: SpeechAudioFormatType = 12
SpeechAudioFormatType_SAFT12kHz8BitStereo: SpeechAudioFormatType = 13
SpeechAudioFormatType_SAFT12kHz16BitMono: SpeechAudioFormatType = 14
SpeechAudioFormatType_SAFT12kHz16BitStereo: SpeechAudioFormatType = 15
SpeechAudioFormatType_SAFT16kHz8BitMono: SpeechAudioFormatType = 16
SpeechAudioFormatType_SAFT16kHz8BitStereo: SpeechAudioFormatType = 17
SpeechAudioFormatType_SAFT16kHz16BitMono: SpeechAudioFormatType = 18
SpeechAudioFormatType_SAFT16kHz16BitStereo: SpeechAudioFormatType = 19
SpeechAudioFormatType_SAFT22kHz8BitMono: SpeechAudioFormatType = 20
SpeechAudioFormatType_SAFT22kHz8BitStereo: SpeechAudioFormatType = 21
SpeechAudioFormatType_SAFT22kHz16BitMono: SpeechAudioFormatType = 22
SpeechAudioFormatType_SAFT22kHz16BitStereo: SpeechAudioFormatType = 23
SpeechAudioFormatType_SAFT24kHz8BitMono: SpeechAudioFormatType = 24
SpeechAudioFormatType_SAFT24kHz8BitStereo: SpeechAudioFormatType = 25
SpeechAudioFormatType_SAFT24kHz16BitMono: SpeechAudioFormatType = 26
SpeechAudioFormatType_SAFT24kHz16BitStereo: SpeechAudioFormatType = 27
SpeechAudioFormatType_SAFT32kHz8BitMono: SpeechAudioFormatType = 28
SpeechAudioFormatType_SAFT32kHz8BitStereo: SpeechAudioFormatType = 29
SpeechAudioFormatType_SAFT32kHz16BitMono: SpeechAudioFormatType = 30
SpeechAudioFormatType_SAFT32kHz16BitStereo: SpeechAudioFormatType = 31
SpeechAudioFormatType_SAFT44kHz8BitMono: SpeechAudioFormatType = 32
SpeechAudioFormatType_SAFT44kHz8BitStereo: SpeechAudioFormatType = 33
SpeechAudioFormatType_SAFT44kHz16BitMono: SpeechAudioFormatType = 34
SpeechAudioFormatType_SAFT44kHz16BitStereo: SpeechAudioFormatType = 35
SpeechAudioFormatType_SAFT48kHz8BitMono: SpeechAudioFormatType = 36
SpeechAudioFormatType_SAFT48kHz8BitStereo: SpeechAudioFormatType = 37
SpeechAudioFormatType_SAFT48kHz16BitMono: SpeechAudioFormatType = 38
SpeechAudioFormatType_SAFT48kHz16BitStereo: SpeechAudioFormatType = 39
SpeechAudioFormatType_SAFTTrueSpeech_8kHz1BitMono: SpeechAudioFormatType = 40
SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzMono: SpeechAudioFormatType = 41
SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzStereo: SpeechAudioFormatType = 42
SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzMono: SpeechAudioFormatType = 43
SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzStereo: SpeechAudioFormatType = 44
SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzMono: SpeechAudioFormatType = 45
SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzStereo: SpeechAudioFormatType = 46
SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzMono: SpeechAudioFormatType = 47
SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzStereo: SpeechAudioFormatType = 48
SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzMono: SpeechAudioFormatType = 49
SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzStereo: SpeechAudioFormatType = 50
SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzMono: SpeechAudioFormatType = 51
SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzStereo: SpeechAudioFormatType = 52
SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzMono: SpeechAudioFormatType = 53
SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzStereo: SpeechAudioFormatType = 54
SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzMono: SpeechAudioFormatType = 55
SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzStereo: SpeechAudioFormatType = 56
SpeechAudioFormatType_SAFTADPCM_8kHzMono: SpeechAudioFormatType = 57
SpeechAudioFormatType_SAFTADPCM_8kHzStereo: SpeechAudioFormatType = 58
SpeechAudioFormatType_SAFTADPCM_11kHzMono: SpeechAudioFormatType = 59
SpeechAudioFormatType_SAFTADPCM_11kHzStereo: SpeechAudioFormatType = 60
SpeechAudioFormatType_SAFTADPCM_22kHzMono: SpeechAudioFormatType = 61
SpeechAudioFormatType_SAFTADPCM_22kHzStereo: SpeechAudioFormatType = 62
SpeechAudioFormatType_SAFTADPCM_44kHzMono: SpeechAudioFormatType = 63
SpeechAudioFormatType_SAFTADPCM_44kHzStereo: SpeechAudioFormatType = 64
SpeechAudioFormatType_SAFTGSM610_8kHzMono: SpeechAudioFormatType = 65
SpeechAudioFormatType_SAFTGSM610_11kHzMono: SpeechAudioFormatType = 66
SpeechAudioFormatType_SAFTGSM610_22kHzMono: SpeechAudioFormatType = 67
SpeechAudioFormatType_SAFTGSM610_44kHzMono: SpeechAudioFormatType = 68
SpeechAudioState = Int32
SpeechAudioState_SASClosed: SpeechAudioState = 0
SpeechAudioState_SASStop: SpeechAudioState = 1
SpeechAudioState_SASPause: SpeechAudioState = 2
SpeechAudioState_SASRun: SpeechAudioState = 3
SpeechBookmarkOptions = Int32
SpeechBookmarkOptions_SBONone: SpeechBookmarkOptions = 0
SpeechBookmarkOptions_SBOPause: SpeechBookmarkOptions = 1
SpeechDataKeyLocation = Int32
SpeechDataKeyLocation_SDKLDefaultLocation: SpeechDataKeyLocation = 0
SpeechDataKeyLocation_SDKLCurrentUser: SpeechDataKeyLocation = 1
SpeechDataKeyLocation_SDKLLocalMachine: SpeechDataKeyLocation = 2
SpeechDataKeyLocation_SDKLCurrentConfig: SpeechDataKeyLocation = 5
SpeechDiscardType = Int32
SpeechDiscardType_SDTProperty: SpeechDiscardType = 1
SpeechDiscardType_SDTReplacement: SpeechDiscardType = 2
SpeechDiscardType_SDTRule: SpeechDiscardType = 4
SpeechDiscardType_SDTDisplayText: SpeechDiscardType = 8
SpeechDiscardType_SDTLexicalForm: SpeechDiscardType = 16
SpeechDiscardType_SDTPronunciation: SpeechDiscardType = 32
SpeechDiscardType_SDTAudio: SpeechDiscardType = 64
SpeechDiscardType_SDTAlternates: SpeechDiscardType = 128
SpeechDiscardType_SDTAll: SpeechDiscardType = 255
SpeechDisplayAttributes = Int32
SDA_No_Trailing_Space: SpeechDisplayAttributes = 0
SDA_One_Trailing_Space: SpeechDisplayAttributes = 2
SDA_Two_Trailing_Spaces: SpeechDisplayAttributes = 4
SDA_Consume_Leading_Spaces: SpeechDisplayAttributes = 8
SpeechEmulationCompareFlags = Int32
SpeechEmulationCompareFlags_SECFIgnoreCase: SpeechEmulationCompareFlags = 1
SpeechEmulationCompareFlags_SECFIgnoreKanaType: SpeechEmulationCompareFlags = 65536
SpeechEmulationCompareFlags_SECFIgnoreWidth: SpeechEmulationCompareFlags = 131072
SpeechEmulationCompareFlags_SECFNoSpecialChars: SpeechEmulationCompareFlags = 536870912
SpeechEmulationCompareFlags_SECFEmulateResult: SpeechEmulationCompareFlags = 1073741824
SpeechEmulationCompareFlags_SECFDefault: SpeechEmulationCompareFlags = 196609
SpeechEngineConfidence = Int32
SpeechEngineConfidence_SECLowConfidence: SpeechEngineConfidence = -1
SpeechEngineConfidence_SECNormalConfidence: SpeechEngineConfidence = 0
SpeechEngineConfidence_SECHighConfidence: SpeechEngineConfidence = 1
SpeechFormatType = Int32
SpeechFormatType_SFTInput: SpeechFormatType = 0
SpeechFormatType_SFTSREngine: SpeechFormatType = 1
SpeechGrammarRuleStateTransitionType = Int32
SpeechGrammarRuleStateTransitionType_SGRSTTEpsilon: SpeechGrammarRuleStateTransitionType = 0
SpeechGrammarRuleStateTransitionType_SGRSTTWord: SpeechGrammarRuleStateTransitionType = 1
SpeechGrammarRuleStateTransitionType_SGRSTTRule: SpeechGrammarRuleStateTransitionType = 2
SpeechGrammarRuleStateTransitionType_SGRSTTDictation: SpeechGrammarRuleStateTransitionType = 3
SpeechGrammarRuleStateTransitionType_SGRSTTWildcard: SpeechGrammarRuleStateTransitionType = 4
SpeechGrammarRuleStateTransitionType_SGRSTTTextBuffer: SpeechGrammarRuleStateTransitionType = 5
SpeechGrammarState = Int32
SpeechGrammarState_SGSEnabled: SpeechGrammarState = 1
SpeechGrammarState_SGSDisabled: SpeechGrammarState = 0
SpeechGrammarState_SGSExclusive: SpeechGrammarState = 3
SpeechGrammarWordType = Int32
SpeechGrammarWordType_SGDisplay: SpeechGrammarWordType = 0
SpeechGrammarWordType_SGLexical: SpeechGrammarWordType = 1
SpeechGrammarWordType_SGPronounciation: SpeechGrammarWordType = 2
SpeechGrammarWordType_SGLexicalNoSpecialChars: SpeechGrammarWordType = 3
SpeechInterference = Int32
SpeechInterference_SINone: SpeechInterference = 0
SpeechInterference_SINoise: SpeechInterference = 1
SpeechInterference_SINoSignal: SpeechInterference = 2
SpeechInterference_SITooLoud: SpeechInterference = 3
SpeechInterference_SITooQuiet: SpeechInterference = 4
SpeechInterference_SITooFast: SpeechInterference = 5
SpeechInterference_SITooSlow: SpeechInterference = 6
SpeechLexiconType = Int32
SpeechLexiconType_SLTUser: SpeechLexiconType = 1
SpeechLexiconType_SLTApp: SpeechLexiconType = 2
SpeechLoadOption = Int32
SpeechLoadOption_SLOStatic: SpeechLoadOption = 0
SpeechLoadOption_SLODynamic: SpeechLoadOption = 1
SpeechPartOfSpeech = Int32
SpeechPartOfSpeech_SPSNotOverriden: SpeechPartOfSpeech = -1
SpeechPartOfSpeech_SPSUnknown: SpeechPartOfSpeech = 0
SpeechPartOfSpeech_SPSNoun: SpeechPartOfSpeech = 4096
SpeechPartOfSpeech_SPSVerb: SpeechPartOfSpeech = 8192
SpeechPartOfSpeech_SPSModifier: SpeechPartOfSpeech = 12288
SpeechPartOfSpeech_SPSFunction: SpeechPartOfSpeech = 16384
SpeechPartOfSpeech_SPSInterjection: SpeechPartOfSpeech = 20480
SpeechPartOfSpeech_SPSLMA: SpeechPartOfSpeech = 28672
SpeechPartOfSpeech_SPSSuppressWord: SpeechPartOfSpeech = 61440
SpeechRecoContextState = Int32
SRCS_Disabled: SpeechRecoContextState = 0
SRCS_Enabled: SpeechRecoContextState = 1
SpeechRecoEvents = Int32
SpeechRecoEvents_SREStreamEnd: SpeechRecoEvents = 1
SpeechRecoEvents_SRESoundStart: SpeechRecoEvents = 2
SpeechRecoEvents_SRESoundEnd: SpeechRecoEvents = 4
SpeechRecoEvents_SREPhraseStart: SpeechRecoEvents = 8
SpeechRecoEvents_SRERecognition: SpeechRecoEvents = 16
SpeechRecoEvents_SREHypothesis: SpeechRecoEvents = 32
SpeechRecoEvents_SREBookmark: SpeechRecoEvents = 64
SpeechRecoEvents_SREPropertyNumChange: SpeechRecoEvents = 128
SpeechRecoEvents_SREPropertyStringChange: SpeechRecoEvents = 256
SpeechRecoEvents_SREFalseRecognition: SpeechRecoEvents = 512
SpeechRecoEvents_SREInterference: SpeechRecoEvents = 1024
SpeechRecoEvents_SRERequestUI: SpeechRecoEvents = 2048
SpeechRecoEvents_SREStateChange: SpeechRecoEvents = 4096
SpeechRecoEvents_SREAdaptation: SpeechRecoEvents = 8192
SpeechRecoEvents_SREStreamStart: SpeechRecoEvents = 16384
SpeechRecoEvents_SRERecoOtherContext: SpeechRecoEvents = 32768
SpeechRecoEvents_SREAudioLevel: SpeechRecoEvents = 65536
SpeechRecoEvents_SREPrivate: SpeechRecoEvents = 262144
SpeechRecoEvents_SREAllEvents: SpeechRecoEvents = 393215
SpeechRecognitionType = Int32
SpeechRecognitionType_SRTStandard: SpeechRecognitionType = 0
SpeechRecognitionType_SRTAutopause: SpeechRecognitionType = 1
SpeechRecognitionType_SRTEmulated: SpeechRecognitionType = 2
SpeechRecognitionType_SRTSMLTimeout: SpeechRecognitionType = 4
SpeechRecognitionType_SRTExtendableParse: SpeechRecognitionType = 8
SpeechRecognitionType_SRTReSent: SpeechRecognitionType = 16
SpeechRecognizerState = Int32
SpeechRecognizerState_SRSInactive: SpeechRecognizerState = 0
SpeechRecognizerState_SRSActive: SpeechRecognizerState = 1
SpeechRecognizerState_SRSActiveAlways: SpeechRecognizerState = 2
SpeechRecognizerState_SRSInactiveWithPurge: SpeechRecognizerState = 3
SpeechRetainedAudioOptions = Int32
SpeechRetainedAudioOptions_SRAONone: SpeechRetainedAudioOptions = 0
SpeechRetainedAudioOptions_SRAORetainAudio: SpeechRetainedAudioOptions = 1
SpeechRuleAttributes = Int32
SpeechRuleAttributes_SRATopLevel: SpeechRuleAttributes = 1
SpeechRuleAttributes_SRADefaultToActive: SpeechRuleAttributes = 2
SpeechRuleAttributes_SRAExport: SpeechRuleAttributes = 4
SpeechRuleAttributes_SRAImport: SpeechRuleAttributes = 8
SpeechRuleAttributes_SRAInterpreter: SpeechRuleAttributes = 16
SpeechRuleAttributes_SRADynamic: SpeechRuleAttributes = 32
SpeechRuleAttributes_SRARoot: SpeechRuleAttributes = 64
SpeechRuleState = Int32
SpeechRuleState_SGDSInactive: SpeechRuleState = 0
SpeechRuleState_SGDSActive: SpeechRuleState = 1
SpeechRuleState_SGDSActiveWithAutoPause: SpeechRuleState = 3
SpeechRuleState_SGDSActiveUserDelimited: SpeechRuleState = 4
SpeechRunState = Int32
SpeechRunState_SRSEDone: SpeechRunState = 1
SpeechRunState_SRSEIsSpeaking: SpeechRunState = 2
SpeechSpecialTransitionType = Int32
SpeechSpecialTransitionType_SSTTWildcard: SpeechSpecialTransitionType = 1
SpeechSpecialTransitionType_SSTTDictation: SpeechSpecialTransitionType = 2
SpeechSpecialTransitionType_SSTTTextBuffer: SpeechSpecialTransitionType = 3
SpeechStreamFileMode = Int32
SpeechStreamFileMode_SSFMOpenForRead: SpeechStreamFileMode = 0
SpeechStreamFileMode_SSFMOpenReadWrite: SpeechStreamFileMode = 1
SpeechStreamFileMode_SSFMCreate: SpeechStreamFileMode = 2
SpeechStreamFileMode_SSFMCreateForWrite: SpeechStreamFileMode = 3
SpeechStreamSeekPositionType = UInt32
SpeechStreamSeekPositionType_SSSPTRelativeToStart: SpeechStreamSeekPositionType = 0
SpeechStreamSeekPositionType_SSSPTRelativeToCurrentPosition: SpeechStreamSeekPositionType = 1
SpeechStreamSeekPositionType_SSSPTRelativeToEnd: SpeechStreamSeekPositionType = 2
SpeechTokenContext = UInt32
SpeechTokenContext_STCInprocServer: SpeechTokenContext = 1
SpeechTokenContext_STCInprocHandler: SpeechTokenContext = 2
SpeechTokenContext_STCLocalServer: SpeechTokenContext = 4
SpeechTokenContext_STCRemoteServer: SpeechTokenContext = 16
SpeechTokenContext_STCAll: SpeechTokenContext = 23
SpeechTokenShellFolder = Int32
STSF_AppData: SpeechTokenShellFolder = 26
STSF_LocalAppData: SpeechTokenShellFolder = 28
STSF_CommonAppData: SpeechTokenShellFolder = 35
STSF_FlagCreate: SpeechTokenShellFolder = 32768
SpeechVisemeFeature = Int32
SVF_None: SpeechVisemeFeature = 0
SVF_Stressed: SpeechVisemeFeature = 1
SVF_Emphasis: SpeechVisemeFeature = 2
SpeechVisemeType = Int32
SVP_0: SpeechVisemeType = 0
SVP_1: SpeechVisemeType = 1
SVP_2: SpeechVisemeType = 2
SVP_3: SpeechVisemeType = 3
SVP_4: SpeechVisemeType = 4
SVP_5: SpeechVisemeType = 5
SVP_6: SpeechVisemeType = 6
SVP_7: SpeechVisemeType = 7
SVP_8: SpeechVisemeType = 8
SVP_9: SpeechVisemeType = 9
SVP_10: SpeechVisemeType = 10
SVP_11: SpeechVisemeType = 11
SVP_12: SpeechVisemeType = 12
SVP_13: SpeechVisemeType = 13
SVP_14: SpeechVisemeType = 14
SVP_15: SpeechVisemeType = 15
SVP_16: SpeechVisemeType = 16
SVP_17: SpeechVisemeType = 17
SVP_18: SpeechVisemeType = 18
SVP_19: SpeechVisemeType = 19
SVP_20: SpeechVisemeType = 20
SVP_21: SpeechVisemeType = 21
SpeechVoiceEvents = Int32
SpeechVoiceEvents_SVEStartInputStream: SpeechVoiceEvents = 2
SpeechVoiceEvents_SVEEndInputStream: SpeechVoiceEvents = 4
SpeechVoiceEvents_SVEVoiceChange: SpeechVoiceEvents = 8
SpeechVoiceEvents_SVEBookmark: SpeechVoiceEvents = 16
SpeechVoiceEvents_SVEWordBoundary: SpeechVoiceEvents = 32
SpeechVoiceEvents_SVEPhoneme: SpeechVoiceEvents = 64
SpeechVoiceEvents_SVESentenceBoundary: SpeechVoiceEvents = 128
SpeechVoiceEvents_SVEViseme: SpeechVoiceEvents = 256
SpeechVoiceEvents_SVEAudioLevel: SpeechVoiceEvents = 512
SpeechVoiceEvents_SVEPrivate: SpeechVoiceEvents = 32768
SpeechVoiceEvents_SVEAllEvents: SpeechVoiceEvents = 33790
SpeechVoicePriority = Int32
SpeechVoicePriority_SVPNormal: SpeechVoicePriority = 0
SpeechVoicePriority_SVPAlert: SpeechVoicePriority = 1
SpeechVoicePriority_SVPOver: SpeechVoicePriority = 2
SpeechVoiceSpeakFlags = Int32
SpeechVoiceSpeakFlags_SVSFDefault: SpeechVoiceSpeakFlags = 0
SpeechVoiceSpeakFlags_SVSFlagsAsync: SpeechVoiceSpeakFlags = 1
SpeechVoiceSpeakFlags_SVSFPurgeBeforeSpeak: SpeechVoiceSpeakFlags = 2
SpeechVoiceSpeakFlags_SVSFIsFilename: SpeechVoiceSpeakFlags = 4
SpeechVoiceSpeakFlags_SVSFIsXML: SpeechVoiceSpeakFlags = 8
SpeechVoiceSpeakFlags_SVSFIsNotXML: SpeechVoiceSpeakFlags = 16
SpeechVoiceSpeakFlags_SVSFPersistXML: SpeechVoiceSpeakFlags = 32
SpeechVoiceSpeakFlags_SVSFNLPSpeakPunc: SpeechVoiceSpeakFlags = 64
SpeechVoiceSpeakFlags_SVSFParseSapi: SpeechVoiceSpeakFlags = 128
SpeechVoiceSpeakFlags_SVSFParseSsml: SpeechVoiceSpeakFlags = 256
SpeechVoiceSpeakFlags_SVSFParseAutodetect: SpeechVoiceSpeakFlags = 0
SpeechVoiceSpeakFlags_SVSFNLPMask: SpeechVoiceSpeakFlags = 64
SpeechVoiceSpeakFlags_SVSFParseMask: SpeechVoiceSpeakFlags = 384
SpeechVoiceSpeakFlags_SVSFVoiceMask: SpeechVoiceSpeakFlags = 511
SpeechVoiceSpeakFlags_SVSFUnusedFlags: SpeechVoiceSpeakFlags = -512
SpeechWordPronounceable = Int32
SpeechWordPronounceable_SWPUnknownWordUnpronounceable: SpeechWordPronounceable = 0
SpeechWordPronounceable_SWPUnknownWordPronounceable: SpeechWordPronounceable = 1
SpeechWordPronounceable_SWPKnownWordPronounceable: SpeechWordPronounceable = 2
SpeechWordType = Int32
SpeechWordType_SWTAdded: SpeechWordType = 1
SpeechWordType_SWTDeleted: SpeechWordType = 2
class _ISpeechRecoContextEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7b8fcb42-0e9d-4f00-a048-7b04d6179d3d}')
class _ISpeechVoiceEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a372acd1-3bef-4bbd-8ffb-cb3e2b416af8}')
make_head(_module, 'IEnumSpObjectTokens')
make_head(_module, 'ISpAudio')
make_head(_module, 'ISpContainerLexicon')
make_head(_module, 'ISpDataKey')
make_head(_module, 'ISpDisplayAlternates')
make_head(_module, 'ISpEnginePronunciation')
make_head(_module, 'ISpEventSink')
make_head(_module, 'ISpEventSource')
make_head(_module, 'ISpEventSource2')
make_head(_module, 'ISpGrammarBuilder')
make_head(_module, 'ISpGrammarBuilder2')
make_head(_module, 'ISpLexicon')
make_head(_module, 'ISpMMSysAudio')
make_head(_module, 'ISpNotifyCallback')
make_head(_module, 'ISpNotifySink')
make_head(_module, 'ISpNotifySource')
make_head(_module, 'ISpNotifyTranslator')
make_head(_module, 'ISpObjectToken')
make_head(_module, 'ISpObjectTokenCategory')
make_head(_module, 'ISpObjectTokenInit')
make_head(_module, 'ISpObjectWithToken')
make_head(_module, 'ISpPhoneConverter')
make_head(_module, 'ISpPhoneticAlphabetConverter')
make_head(_module, 'ISpPhoneticAlphabetSelection')
make_head(_module, 'ISpPhrase')
make_head(_module, 'ISpPhrase2')
make_head(_module, 'ISpPhraseAlt')
make_head(_module, 'ISpProperties')
make_head(_module, 'ISpRecoContext')
make_head(_module, 'ISpRecoContext2')
make_head(_module, 'ISpRecoGrammar')
make_head(_module, 'ISpRecoGrammar2')
make_head(_module, 'ISpRecoResult')
make_head(_module, 'ISpRecoResult2')
make_head(_module, 'ISpRecognizer')
make_head(_module, 'ISpRecognizer2')
make_head(_module, 'ISpRegDataKey')
make_head(_module, 'ISpResourceManager')
make_head(_module, 'ISpSerializeState')
make_head(_module, 'ISpShortcut')
make_head(_module, 'ISpStream')
make_head(_module, 'ISpStreamFormat')
make_head(_module, 'ISpStreamFormatConverter')
make_head(_module, 'ISpTranscript')
make_head(_module, 'ISpVoice')
make_head(_module, 'ISpXMLRecoResult')
make_head(_module, 'ISpeechAudio')
make_head(_module, 'ISpeechAudioBufferInfo')
make_head(_module, 'ISpeechAudioFormat')
make_head(_module, 'ISpeechAudioStatus')
make_head(_module, 'ISpeechBaseStream')
make_head(_module, 'ISpeechCustomStream')
make_head(_module, 'ISpeechDataKey')
make_head(_module, 'ISpeechFileStream')
make_head(_module, 'ISpeechGrammarRule')
make_head(_module, 'ISpeechGrammarRuleState')
make_head(_module, 'ISpeechGrammarRuleStateTransition')
make_head(_module, 'ISpeechGrammarRuleStateTransitions')
make_head(_module, 'ISpeechGrammarRules')
make_head(_module, 'ISpeechLexicon')
make_head(_module, 'ISpeechLexiconPronunciation')
make_head(_module, 'ISpeechLexiconPronunciations')
make_head(_module, 'ISpeechLexiconWord')
make_head(_module, 'ISpeechLexiconWords')
make_head(_module, 'ISpeechMMSysAudio')
make_head(_module, 'ISpeechMemoryStream')
make_head(_module, 'ISpeechObjectToken')
make_head(_module, 'ISpeechObjectTokenCategory')
make_head(_module, 'ISpeechObjectTokens')
make_head(_module, 'ISpeechPhoneConverter')
make_head(_module, 'ISpeechPhraseAlternate')
make_head(_module, 'ISpeechPhraseAlternates')
make_head(_module, 'ISpeechPhraseElement')
make_head(_module, 'ISpeechPhraseElements')
make_head(_module, 'ISpeechPhraseInfo')
make_head(_module, 'ISpeechPhraseInfoBuilder')
make_head(_module, 'ISpeechPhraseProperties')
make_head(_module, 'ISpeechPhraseProperty')
make_head(_module, 'ISpeechPhraseReplacement')
make_head(_module, 'ISpeechPhraseReplacements')
make_head(_module, 'ISpeechPhraseRule')
make_head(_module, 'ISpeechPhraseRules')
make_head(_module, 'ISpeechRecoContext')
make_head(_module, 'ISpeechRecoGrammar')
make_head(_module, 'ISpeechRecoResult')
make_head(_module, 'ISpeechRecoResult2')
make_head(_module, 'ISpeechRecoResultDispatch')
make_head(_module, 'ISpeechRecoResultTimes')
make_head(_module, 'ISpeechRecognizer')
make_head(_module, 'ISpeechRecognizerStatus')
make_head(_module, 'ISpeechResourceLoader')
make_head(_module, 'ISpeechTextSelectionInformation')
make_head(_module, 'ISpeechVoice')
make_head(_module, 'ISpeechVoiceStatus')
make_head(_module, 'ISpeechWaveFormatEx')
make_head(_module, 'ISpeechXMLRecoResult')
make_head(_module, 'SPAUDIOBUFFERINFO')
make_head(_module, 'SPAUDIOSTATUS')
make_head(_module, 'SPBINARYGRAMMAR')
make_head(_module, 'SPDISPLAYPHRASE')
make_head(_module, 'SPDISPLAYTOKEN')
make_head(_module, 'SPEVENT')
make_head(_module, 'SPEVENTEX')
make_head(_module, 'SPEVENTSOURCEINFO')
make_head(_module, 'SPNORMALIZATIONLIST')
make_head(_module, 'SPNOTIFYCALLBACK')
make_head(_module, 'SPPHRASE')
make_head(_module, 'SPPHRASEELEMENT')
make_head(_module, 'SPPHRASEPROPERTY')
make_head(_module, 'SPPHRASEREPLACEMENT')
make_head(_module, 'SPPHRASERULE')
make_head(_module, 'SPPHRASE_50')
make_head(_module, 'SPPROPERTYINFO')
make_head(_module, 'SPRECOCONTEXTSTATUS')
make_head(_module, 'SPRECOGNIZERSTATUS')
make_head(_module, 'SPRECORESULTTIMES')
make_head(_module, 'SPRULE')
make_head(_module, 'SPSEMANTICERRORINFO')
make_head(_module, 'SPSERIALIZEDEVENT')
make_head(_module, 'SPSERIALIZEDEVENT64')
make_head(_module, 'SPSERIALIZEDPHRASE')
make_head(_module, 'SPSERIALIZEDRESULT')
make_head(_module, 'SPSHORTCUTPAIR')
make_head(_module, 'SPSHORTCUTPAIRLIST')
make_head(_module, 'SPTEXTSELECTIONINFO')
make_head(_module, 'SPVCONTEXT')
make_head(_module, 'SPVOICESTATUS')
make_head(_module, 'SPVPITCH')
make_head(_module, 'SPVSTATE')
make_head(_module, 'SPWORD')
make_head(_module, 'SPWORDLIST')
make_head(_module, 'SPWORDPRONUNCIATION')
make_head(_module, 'SPWORDPRONUNCIATIONLIST')
make_head(_module, '_ISpeechRecoContextEvents')
make_head(_module, '_ISpeechVoiceEvents')
