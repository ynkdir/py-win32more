from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Speech
import Windows.Win32.System.Com
import Windows.Win32.System.Com.Urlmon
import Windows.Win32.System.Registry
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
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
class IEnumSpObjectTokens(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('06b64f9e-7fda-11d2-b4-f2-00-c0-4f-79-73-96')
    @commethod(3)
    def Next(celt: UInt32, pelt: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(Windows.Win32.Media.Speech.IEnumSpObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Item(Index: UInt32, ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpAudio(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpStreamFormat
    Guid = Guid('c05c768f-fae8-4ec2-8e-07-33-83-21-c1-24-52')
    @commethod(15)
    def SetState(NewState: Windows.Win32.Media.Speech.SPAUDIOSTATE, ullReserved: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetFormat(rguidFmtId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStatus(pStatus: POINTER(Windows.Win32.Media.Speech.SPAUDIOSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetBufferInfo(pBuffInfo: POINTER(Windows.Win32.Media.Speech.SPAUDIOBUFFERINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetBufferInfo(pBuffInfo: POINTER(Windows.Win32.Media.Speech.SPAUDIOBUFFERINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultFormat(pFormatId: POINTER(Guid), ppCoMemWaveFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EventHandle() -> Windows.Win32.Foundation.HANDLE: ...
    @commethod(22)
    def GetVolumeLevel(pLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetVolumeLevel(Level: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBufferNotifySize(pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetBufferNotifySize(cbSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpContainerLexicon(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpLexicon
    Guid = Guid('8565572f-c094-41cc-b5-6e-10-bd-9c-3f-f0-44')
    @commethod(9)
    def AddLexicon(pAddLexicon: Windows.Win32.Media.Speech.ISpLexicon_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpDataKey(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('14056581-e16c-11d2-bb-90-00-c0-4f-8e-e6-c0')
    @commethod(3)
    def SetData(pszValueName: Windows.Win32.Foundation.PWSTR, cbData: UInt32, pData: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetData(pszValueName: Windows.Win32.Foundation.PWSTR, pcbData: POINTER(UInt32), pData: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStringValue(pszValueName: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringValue(pszValueName: Windows.Win32.Foundation.PWSTR, ppszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDWORD(pszValueName: Windows.Win32.Foundation.PWSTR, dwValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDWORD(pszValueName: Windows.Win32.Foundation.PWSTR, pdwValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OpenKey(pszSubKeyName: Windows.Win32.Foundation.PWSTR, ppSubKey: POINTER(Windows.Win32.Media.Speech.ISpDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateKey(pszSubKey: Windows.Win32.Foundation.PWSTR, ppSubKey: POINTER(Windows.Win32.Media.Speech.ISpDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteKey(pszSubKey: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteValue(pszValueName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnumKeys(Index: UInt32, ppszSubKeyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumValues(Index: UInt32, ppszValueName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpDisplayAlternates(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c8d7c7e2-0dde-44b7-af-e3-b0-c9-91-fb-eb-5e')
    @commethod(3)
    def GetDisplayAlternates(pPhrase: POINTER(Windows.Win32.Media.Speech.SPDISPLAYPHRASE_head), cRequestCount: UInt32, ppCoMemPhrases: POINTER(POINTER(Windows.Win32.Media.Speech.SPDISPLAYPHRASE_head)), pcPhrasesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFullStopTrailSpace(ulTrailSpace: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEnginePronunciation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c360ce4b-76d1-4214-ad-68-52-65-7d-50-83-da')
    @commethod(3)
    def Normalize(pszWord: Windows.Win32.Foundation.PWSTR, pszLeftContext: Windows.Win32.Foundation.PWSTR, pszRightContext: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pNormalizationList: POINTER(Windows.Win32.Media.Speech.SPNORMALIZATIONLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPronunciations(pszWord: Windows.Win32.Foundation.PWSTR, pszLeftContext: Windows.Win32.Foundation.PWSTR, pszRightContext: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pEnginePronunciationList: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATIONLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEventSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('be7a9cc9-5f9e-11d2-96-0f-00-c0-4f-8e-e6-28')
    @commethod(3)
    def AddEvents(pEventArray: POINTER(Windows.Win32.Media.Speech.SPEVENT_head), ulCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEventInterest(pullEventInterest: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEventSource(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpNotifySource
    Guid = Guid('be7a9cce-5f9e-11d2-96-0f-00-c0-4f-8e-e6-28')
    @commethod(10)
    def SetInterest(ullEventInterest: UInt64, ullQueuedInterest: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEvents(ulCount: UInt32, pEventArray: POINTER(Windows.Win32.Media.Speech.SPEVENT_head), pulFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInfo(pInfo: POINTER(Windows.Win32.Media.Speech.SPEVENTSOURCEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpEventSource2(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpEventSource
    Guid = Guid('2373a435-6a4b-429e-a6-ac-d4-23-1a-61-97-5b')
    @commethod(13)
    def GetEventsEx(ulCount: UInt32, pEventArray: POINTER(Windows.Win32.Media.Speech.SPEVENTEX_head), pulFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpGrammarBuilder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8137828f-591a-4a42-be-58-49-ea-7e-ba-ac-68')
    @commethod(3)
    def ResetGrammar(NewLanguage: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRule(pszRuleName: Windows.Win32.Foundation.PWSTR, dwRuleId: UInt32, dwAttributes: UInt32, fCreateIfNotExist: Windows.Win32.Foundation.BOOL, phInitialState: POINTER(POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearRule(hState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateNewState(hState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), phState: POINTER(POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddWordTransition(hFromState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), hToState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), psz: Windows.Win32.Foundation.PWSTR, pszSeparators: Windows.Win32.Foundation.PWSTR, eWordType: Windows.Win32.Media.Speech.SPGRAMMARWORDTYPE, Weight: Single, pPropInfo: POINTER(Windows.Win32.Media.Speech.SPPROPERTYINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddRuleTransition(hFromState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), hToState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), hRule: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), Weight: Single, pPropInfo: POINTER(Windows.Win32.Media.Speech.SPPROPERTYINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddResource(hRuleState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), pszResourceName: Windows.Win32.Foundation.PWSTR, pszResourceValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Commit(dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpGrammarBuilder2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8ab10026-20cc-4b20-8c-22-a4-9c-9b-a7-8f-60')
    @commethod(3)
    def AddTextSubset(hFromState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), hToState: POINTER(Windows.Win32.Media.Speech.SPSTATEHANDLE___head), psz: Windows.Win32.Foundation.PWSTR, eMatchMode: Windows.Win32.Media.Speech.SPMATCHINGMODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPhoneticAlphabet(phoneticALphabet: Windows.Win32.Media.Speech.PHONETICALPHABET) -> Windows.Win32.Foundation.HRESULT: ...
class ISpLexicon(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('da41a7c2-5383-4db2-91-6b-6c-17-19-e3-db-58')
    @commethod(3)
    def GetPronunciations(pszWord: Windows.Win32.Foundation.PWSTR, LangID: UInt16, dwFlags: UInt32, pWordPronunciationList: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATIONLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPronunciation(pszWord: Windows.Win32.Foundation.PWSTR, LangID: UInt16, ePartOfSpeech: Windows.Win32.Media.Speech.SPPARTOFSPEECH, pszPronunciation: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemovePronunciation(pszWord: Windows.Win32.Foundation.PWSTR, LangID: UInt16, ePartOfSpeech: Windows.Win32.Media.Speech.SPPARTOFSPEECH, pszPronunciation: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGeneration(pdwGeneration: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGenerationChange(dwFlags: UInt32, pdwGeneration: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(dwFlags: UInt32, pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpMMSysAudio(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpAudio
    Guid = Guid('15806f6e-1d70-4b48-98-e6-3b-1a-00-75-09-ab')
    @commethod(26)
    def GetDeviceId(puDeviceId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetDeviceId(uDeviceId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetMMHandle(pHandle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetLineId(puLineId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetLineId(uLineId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpNotifyCallback(c_void_p):
    extends: None
    @commethod(0)
    def NotifyCallback(wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class ISpNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('259684dc-37c3-11d2-96-03-00-c0-4f-8e-e6-28')
    @commethod(3)
    def Notify() -> Windows.Win32.Foundation.HRESULT: ...
class ISpNotifySource(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5eff4aef-8487-11d2-96-1c-00-c0-4f-8e-e6-28')
    @commethod(3)
    def SetNotifySink(pNotifySink: Windows.Win32.Media.Speech.ISpNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNotifyWindowMessage(hWnd: Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNotifyCallbackFunction(pfnCallback: POINTER(Windows.Win32.Media.Speech.SPNOTIFYCALLBACK), wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetNotifyCallbackInterface(pSpCallback: Windows.Win32.Media.Speech.ISpNotifyCallback_head, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetNotifyWin32Event() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WaitForNotifyEvent(dwMilliseconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNotifyEventHandle() -> Windows.Win32.Foundation.HANDLE: ...
class ISpNotifyTranslator(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpNotifySink
    Guid = Guid('aca16614-5d3d-11d2-96-0e-00-c0-4f-8e-e6-28')
    @commethod(4)
    def InitWindowMessage(hWnd: Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitCallback(pfnCallback: POINTER(Windows.Win32.Media.Speech.SPNOTIFYCALLBACK), wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitSpNotifyCallback(pSpCallback: Windows.Win32.Media.Speech.ISpNotifyCallback_head, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InitWin32Event(hEvent: Windows.Win32.Foundation.HANDLE, fCloseHandleOnRelease: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Wait(dwMilliseconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEventHandle() -> Windows.Win32.Foundation.HANDLE: ...
class ISpObjectToken(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpDataKey
    Guid = Guid('14056589-e16c-11d2-bb-90-00-c0-4f-8e-e6-c0')
    @commethod(15)
    def SetId(pszCategoryId: Windows.Win32.Foundation.PWSTR, pszTokenId: Windows.Win32.Foundation.PWSTR, fCreateIfNotExist: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetId(ppszCoMemTokenId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCategory(ppTokenCategory: POINTER(Windows.Win32.Media.Speech.ISpObjectTokenCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateInstance(pUnkOuter: Windows.Win32.System.Com.IUnknown_head, dwClsContext: UInt32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetStorageFileName(clsidCaller: POINTER(Guid), pszValueName: Windows.Win32.Foundation.PWSTR, pszFileNameSpecifier: Windows.Win32.Foundation.PWSTR, nFolder: UInt32, ppszFilePath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RemoveStorageFileName(clsidCaller: POINTER(Guid), pszKeyName: Windows.Win32.Foundation.PWSTR, fDeleteFile: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Remove(pclsidCaller: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsUISupported(pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, punkObject: Windows.Win32.System.Com.IUnknown_head, pfSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DisplayUI(hwndParent: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, punkObject: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def MatchesAttributes(pszAttributes: Windows.Win32.Foundation.PWSTR, pfMatches: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpObjectTokenCategory(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpDataKey
    Guid = Guid('2d3d3845-39af-4850-bb-f9-40-b4-97-80-01-1d')
    @commethod(15)
    def SetId(pszCategoryId: Windows.Win32.Foundation.PWSTR, fCreateIfNotExist: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetId(ppszCoMemCategoryId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDataKey(spdkl: Windows.Win32.Media.Speech.SPDATAKEYLOCATION, ppDataKey: POINTER(Windows.Win32.Media.Speech.ISpDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumTokens(pzsReqAttribs: Windows.Win32.Foundation.PWSTR, pszOptAttribs: Windows.Win32.Foundation.PWSTR, ppEnum: POINTER(Windows.Win32.Media.Speech.IEnumSpObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDefaultTokenId(pszTokenId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultTokenId(ppszCoMemTokenId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpObjectTokenInit(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpObjectToken
    Guid = Guid('b8aab0cf-346f-49d8-94-99-c8-b0-3f-16-1d-51')
    @commethod(25)
    def InitFromDataKey(pszCategoryId: Windows.Win32.Foundation.PWSTR, pszTokenId: Windows.Win32.Foundation.PWSTR, pDataKey: Windows.Win32.Media.Speech.ISpDataKey_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpObjectWithToken(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5b559f40-e952-11d2-bb-91-00-c0-4f-8e-e6-c0')
    @commethod(3)
    def SetObjectToken(pToken: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectToken(ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneConverter(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpObjectWithToken
    Guid = Guid('8445c581-0cac-4a38-ab-fe-9b-2c-e2-82-64-55')
    @commethod(5)
    def PhoneToId(pszPhone: Windows.Win32.Foundation.PWSTR, pId: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IdToPhone(pId: POINTER(UInt16), pszPhone: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneticAlphabetConverter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('133adcd4-19b4-4020-9f-dc-84-2e-78-25-3b-17')
    @commethod(3)
    def GetLangId(pLangID: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLangId(LangID: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SAPI2UPS(pszSAPIId: POINTER(UInt16), pszUPSId: POINTER(UInt16), cMaxLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UPS2SAPI(pszUPSId: POINTER(UInt16), pszSAPIId: POINTER(UInt16), cMaxLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxConvertLength(cSrcLength: UInt32, bSAPI2UPS: Windows.Win32.Foundation.BOOL, pcMaxDestLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneticAlphabetSelection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b2745efd-42ce-48ca-81-f1-a9-6e-02-53-8a-90')
    @commethod(3)
    def IsAlphabetUPS(pfIsUPS: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAlphabetToUPS(fForceUPS: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhrase(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1a5c0354-b621-4b5a-87-91-d3-06-ed-37-9e-53')
    @commethod(3)
    def GetPhrase(ppCoMemPhrase: POINTER(POINTER(Windows.Win32.Media.Speech.SPPHRASE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSerializedPhrase(ppCoMemPhrase: POINTER(POINTER(Windows.Win32.Media.Speech.SPSERIALIZEDPHRASE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetText(ulStart: UInt32, ulCount: UInt32, fUseTextReplacements: Windows.Win32.Foundation.BOOL, ppszCoMemText: POINTER(Windows.Win32.Foundation.PWSTR), pbDisplayAttributes: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Discard(dwValueTypes: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhrase2(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpPhrase
    Guid = Guid('f264da52-e457-4696-b8-56-a7-37-b7-17-af-79')
    @commethod(7)
    def GetXMLResult(ppszCoMemXMLResult: POINTER(Windows.Win32.Foundation.PWSTR), Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetXMLErrorInfo(pSemanticErrorInfo: POINTER(Windows.Win32.Media.Speech.SPSEMANTICERRORINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAudio(ulStartElement: UInt32, cElements: UInt32, ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpPhraseAlt(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpPhrase
    Guid = Guid('8fcebc98-4e49-4067-9c-6c-d8-6a-0e-09-2e-3d')
    @commethod(7)
    def GetAltInfo(ppParent: POINTER(Windows.Win32.Media.Speech.ISpPhrase_head), pulStartElementInParent: POINTER(UInt32), pcElementsInParent: POINTER(UInt32), pcElementsInAlt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Commit() -> Windows.Win32.Foundation.HRESULT: ...
class ISpProperties(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5b4fb971-b115-4de1-ad-97-e4-82-e3-bf-6e-e4')
    @commethod(3)
    def SetPropertyNum(pName: Windows.Win32.Foundation.PWSTR, lValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyNum(pName: Windows.Win32.Foundation.PWSTR, plValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPropertyString(pName: Windows.Win32.Foundation.PWSTR, pValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyString(pName: Windows.Win32.Foundation.PWSTR, ppCoMemValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoContext(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpEventSource
    Guid = Guid('f740a62f-7c15-489e-82-34-94-0a-33-d9-27-2d')
    @commethod(13)
    def GetRecognizer(ppRecognizer: POINTER(Windows.Win32.Media.Speech.ISpRecognizer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateGrammar(ullGrammarId: UInt64, ppGrammar: POINTER(Windows.Win32.Media.Speech.ISpRecoGrammar_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStatus(pStatus: POINTER(Windows.Win32.Media.Speech.SPRECOCONTEXTSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMaxAlternates(pcAlternates: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetMaxAlternates(cAlternates: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetAudioOptions(Options: Windows.Win32.Media.Speech.SPAUDIOOPTIONS, pAudioFormatId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAudioOptions(pOptions: POINTER(Windows.Win32.Media.Speech.SPAUDIOOPTIONS), pAudioFormatId: POINTER(Guid), ppCoMemWFEX: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeserializeResult(pSerializedResult: POINTER(Windows.Win32.Media.Speech.SPSERIALIZEDRESULT_head), ppResult: POINTER(Windows.Win32.Media.Speech.ISpRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Bookmark(Options: Windows.Win32.Media.Speech.SPBOOKMARKOPTIONS, ullStreamPosition: UInt64, lparamEvent: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetAdaptationData(pAdaptationData: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Pause(dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Resume(dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetVoice(pVoice: Windows.Win32.Media.Speech.ISpVoice_head, fAllowFormatChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetVoice(ppVoice: POINTER(Windows.Win32.Media.Speech.ISpVoice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetVoicePurgeEvent(ullEventInterest: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetVoicePurgeEvent(pullEventInterest: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetContextState(eContextState: Windows.Win32.Media.Speech.SPCONTEXTSTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetContextState(peContextState: POINTER(Windows.Win32.Media.Speech.SPCONTEXTSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoContext2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bead311c-52ff-437f-94-64-6b-21-05-4c-a7-3d')
    @commethod(3)
    def SetGrammarOptions(eGrammarOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGrammarOptions(peGrammarOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAdaptationData2(pAdaptationData: Windows.Win32.Foundation.PWSTR, cch: UInt32, pTopicName: Windows.Win32.Foundation.PWSTR, eAdaptationSettings: UInt32, eRelevance: Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoGrammar(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpGrammarBuilder
    Guid = Guid('2177db29-7f45-47d0-85-54-06-7e-91-c8-05-02')
    @commethod(11)
    def GetGrammarId(pullGrammarId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecoContext(ppRecoCtxt: POINTER(Windows.Win32.Media.Speech.ISpRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def LoadCmdFromFile(pszFileName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def LoadCmdFromObject(rcid: POINTER(Guid), pszGrammarName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LoadCmdFromResource(hModule: Windows.Win32.Foundation.HINSTANCE, pszResourceName: Windows.Win32.Foundation.PWSTR, pszResourceType: Windows.Win32.Foundation.PWSTR, wLanguage: UInt16, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def LoadCmdFromMemory(pGrammar: POINTER(Windows.Win32.Media.Speech.SPBINARYGRAMMAR_head), Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def LoadCmdFromProprietaryGrammar(rguidParam: POINTER(Guid), pszStringParam: Windows.Win32.Foundation.PWSTR, pvDataPrarm: c_void_p, cbDataSize: UInt32, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRuleState(pszName: Windows.Win32.Foundation.PWSTR, pReserved: c_void_p, NewState: Windows.Win32.Media.Speech.SPRULESTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetRuleIdState(ulRuleId: UInt32, NewState: Windows.Win32.Media.Speech.SPRULESTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def LoadDictation(pszTopicName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def UnloadDictation() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetDictationState(NewState: Windows.Win32.Media.Speech.SPRULESTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWordSequenceData(pText: Windows.Win32.Foundation.PWSTR, cchText: UInt32, pInfo: POINTER(Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTextSelection(pInfo: POINTER(Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsPronounceable(pszWord: Windows.Win32.Foundation.PWSTR, pWordPronounceable: POINTER(Windows.Win32.Media.Speech.SPWORDPRONOUNCEABLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetGrammarState(eGrammarState: Windows.Win32.Media.Speech.SPGRAMMARSTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SaveCmd(pStream: Windows.Win32.System.Com.IStream_head, ppszCoMemErrorText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetGrammarState(peGrammarState: POINTER(Windows.Win32.Media.Speech.SPGRAMMARSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoGrammar2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4b37bc9e-9ed6-44a3-93-d3-18-f0-22-b7-9e-c3')
    @commethod(3)
    def GetRules(ppCoMemRules: POINTER(POINTER(Windows.Win32.Media.Speech.SPRULE_head)), puNumRules: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadCmdFromFile2(pszFileName: Windows.Win32.Foundation.PWSTR, Options: Windows.Win32.Media.Speech.SPLOADOPTIONS, pszSharingUri: Windows.Win32.Foundation.PWSTR, pszBaseUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadCmdFromMemory2(pGrammar: POINTER(Windows.Win32.Media.Speech.SPBINARYGRAMMAR_head), Options: Windows.Win32.Media.Speech.SPLOADOPTIONS, pszSharingUri: Windows.Win32.Foundation.PWSTR, pszBaseUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRulePriority(pszRuleName: Windows.Win32.Foundation.PWSTR, ulRuleId: UInt32, nRulePriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRuleWeight(pszRuleName: Windows.Win32.Foundation.PWSTR, ulRuleId: UInt32, flWeight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDictationWeight(flWeight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetGrammarLoader(pLoader: Windows.Win32.Media.Speech.ISpeechResourceLoader_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSMLSecurityManager(pSMLSecurityManager: Windows.Win32.System.Com.Urlmon.IInternetSecurityManager_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoResult(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpPhrase
    Guid = Guid('20b053be-e235-43cd-9a-2a-8d-17-a4-8b-78-42')
    @commethod(7)
    def GetResultTimes(pTimes: POINTER(Windows.Win32.Media.Speech.SPRECORESULTTIMES_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAlternates(ulStartElement: UInt32, cElements: UInt32, ulRequestCount: UInt32, ppPhrases: POINTER(Windows.Win32.Media.Speech.ISpPhraseAlt_head), pcPhrasesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAudio(ulStartElement: UInt32, cElements: UInt32, ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SpeakAudio(ulStartElement: UInt32, cElements: UInt32, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Serialize(ppCoMemSerializedResult: POINTER(POINTER(Windows.Win32.Media.Speech.SPSERIALIZEDRESULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ScaleAudio(pAudioFormatId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecoContext(ppRecoContext: POINTER(Windows.Win32.Media.Speech.ISpRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecoResult2(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpRecoResult
    Guid = Guid('27cac6c4-88f2-41f2-88-17-0c-95-e5-9f-1e-6e')
    @commethod(14)
    def CommitAlternate(pPhraseAlt: Windows.Win32.Media.Speech.ISpPhraseAlt_head, ppNewResult: POINTER(Windows.Win32.Media.Speech.ISpRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CommitText(ulStartElement: UInt32, cElements: UInt32, pszCorrectedData: Windows.Win32.Foundation.PWSTR, eCommitFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetTextFeedback(pszFeedback: Windows.Win32.Foundation.PWSTR, fSuccessful: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecognizer(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpProperties
    Guid = Guid('c2b5f241-daa0-4507-9e-16-5a-1e-aa-2b-7a-5c')
    @commethod(7)
    def SetRecognizer(pRecognizer: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecognizer(ppRecognizer: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetInput(pUnkInput: Windows.Win32.System.Com.IUnknown_head, fAllowFormatChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInputObjectToken(ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInputStream(ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateRecoContext(ppNewCtxt: POINTER(Windows.Win32.Media.Speech.ISpRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecoProfile(ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetRecoProfile(pToken: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsSharedInstance() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecoState(pState: POINTER(Windows.Win32.Media.Speech.SPRECOSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetRecoState(NewState: Windows.Win32.Media.Speech.SPRECOSTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStatus(pStatus: POINTER(Windows.Win32.Media.Speech.SPRECOGNIZERSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFormat(WaveFormatType: Windows.Win32.Media.Speech.SPSTREAMFORMATTYPE, pFormatId: POINTER(Guid), ppCoMemWFEX: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def IsUISupported(pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, pfSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DisplayUI(hwndParent: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EmulateRecognition(pPhrase: Windows.Win32.Media.Speech.ISpPhrase_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpRecognizer2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8fc6d974-c81e-4098-93-c5-01-47-f6-1e-d4-d3')
    @commethod(3)
    def EmulateRecognitionEx(pPhrase: Windows.Win32.Media.Speech.ISpPhrase_head, dwCompareFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTrainingState(fDoingTraining: Windows.Win32.Foundation.BOOL, fAdaptFromTrainingData: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ResetAcousticModelAdaptation() -> Windows.Win32.Foundation.HRESULT: ...
class ISpRegDataKey(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpDataKey
    Guid = Guid('92a66e2b-c830-4149-83-df-6f-c2-ba-1e-7a-5b')
    @commethod(15)
    def SetKey(hkey: Windows.Win32.System.Registry.HKEY, fReadOnly: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpResourceManager(c_void_p):
    extends: Windows.Win32.System.Com.IServiceProvider
    Guid = Guid('93384e18-5014-43d5-ad-bb-a7-8e-05-59-26-bd')
    @commethod(4)
    def SetObject(guidServiceId: POINTER(Guid), pUnkObject: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObject(guidServiceId: POINTER(Guid), ObjectCLSID: POINTER(Guid), ObjectIID: POINTER(Guid), fReleaseWhenLastExternalRefReleased: Windows.Win32.Foundation.BOOL, ppObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpSerializeState(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('21b501a0-0ec7-46c9-92-c3-a2-bc-78-4c-54-b9')
    @commethod(3)
    def GetSerializedState(ppbData: POINTER(c_char_p_no), pulSize: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSerializedState(pbData: c_char_p_no, ulSize: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpShortcut(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3df681e2-ea56-11d9-8b-de-f6-6b-ad-1e-3f-3a')
    @commethod(3)
    def AddShortcut(pszDisplay: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pszSpoken: Windows.Win32.Foundation.PWSTR, shType: Windows.Win32.Media.Speech.SPSHORTCUTTYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveShortcut(pszDisplay: Windows.Win32.Foundation.PWSTR, LangID: UInt16, pszSpoken: Windows.Win32.Foundation.PWSTR, shType: Windows.Win32.Media.Speech.SPSHORTCUTTYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetShortcuts(LangID: UInt16, pShortcutpairList: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGeneration(pdwGeneration: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetWordsFromGenerationChange(pdwGeneration: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pWordList: POINTER(Windows.Win32.Media.Speech.SPWORDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetShortcutsForGeneration(pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pShortcutpairList: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGenerationChange(pdwGeneration: POINTER(UInt32), pShortcutpairList: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpStream(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpStreamFormat
    Guid = Guid('12e3cca9-7518-44c5-a5-e7-ba-5a-79-cb-92-9e')
    @commethod(15)
    def SetBaseStream(pStream: Windows.Win32.System.Com.IStream_head, rguidFormat: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetBaseStream(ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def BindToFile(pszFileName: Windows.Win32.Foundation.PWSTR, eMode: Windows.Win32.Media.Speech.SPFILEMODE, pFormatId: POINTER(Guid), pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), ullEventInterest: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
class ISpStreamFormat(c_void_p):
    extends: Windows.Win32.System.Com.IStream
    Guid = Guid('bed530be-2606-4f4d-a1-c0-54-c5-cd-a5-56-6f')
    @commethod(14)
    def GetFormat(pguidFormatId: POINTER(Guid), ppCoMemWaveFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ISpStreamFormatConverter(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpStreamFormat
    Guid = Guid('678a932c-ea71-4446-9b-41-78-fd-a6-28-0a-29')
    @commethod(15)
    def SetBaseStream(pStream: Windows.Win32.Media.Speech.ISpStreamFormat_head, fSetFormatToBaseStreamFormat: Windows.Win32.Foundation.BOOL, fWriteToBaseStream: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetBaseStream(ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetFormat(rguidFormatIdOfConvertedStream: POINTER(Guid), pWaveFormatExOfConvertedStream: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ResetSeekPosition() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ScaleConvertedToBaseOffset(ullOffsetConvertedStream: UInt64, pullOffsetBaseStream: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ScaleBaseToConvertedOffset(ullOffsetBaseStream: UInt64, pullOffsetConvertedStream: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpTranscript(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('10f63bce-201a-11d3-ac-70-00-c0-4f-8e-e6-c0')
    @commethod(3)
    def GetTranscript(ppszTranscript: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AppendTranscript(pszTranscript: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpVoice(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpEventSource
    Guid = Guid('6c44df74-72b9-4992-a1-ec-ef-99-6e-04-22-d4')
    @commethod(13)
    def SetOutput(pUnkOutput: Windows.Win32.System.Com.IUnknown_head, fAllowFormatChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetOutputObjectToken(ppObjectToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetOutputStream(ppStream: POINTER(Windows.Win32.Media.Speech.ISpStreamFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Pause() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Resume() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetVoice(pToken: Windows.Win32.Media.Speech.ISpObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetVoice(ppToken: POINTER(Windows.Win32.Media.Speech.ISpObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Speak(pwcs: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SpeakStream(pStream: Windows.Win32.System.Com.IStream_head, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetStatus(pStatus: POINTER(Windows.Win32.Media.Speech.SPVOICESTATUS_head), ppszLastBookmark: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Skip(pItemType: Windows.Win32.Foundation.PWSTR, lNumItems: Int32, pulNumSkipped: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetPriority(ePriority: Windows.Win32.Media.Speech.SPVPRIORITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPriority(pePriority: POINTER(Windows.Win32.Media.Speech.SPVPRIORITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetAlertBoundary(eBoundary: Windows.Win32.Media.Speech.SPEVENTENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetAlertBoundary(peBoundary: POINTER(Windows.Win32.Media.Speech.SPEVENTENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetRate(RateAdjust: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetRate(pRateAdjust: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetVolume(usVolume: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetVolume(pusVolume: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def WaitUntilDone(msTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetSyncSpeakTimeout(msTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetSyncSpeakTimeout(pmsTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SpeakCompleteEvent() -> Windows.Win32.Foundation.HANDLE: ...
    @commethod(36)
    def IsUISupported(pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32, pfSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def DisplayUI(hwndParent: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszTypeOfUI: Windows.Win32.Foundation.PWSTR, pvExtraData: c_void_p, cbExtraData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpXMLRecoResult(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpRecoResult
    Guid = Guid('ae39362b-45a8-4074-9b-9e-cc-f4-9a-a2-d0-b6')
    @commethod(14)
    def GetXMLResult(ppszCoMemXMLResult: POINTER(Windows.Win32.Foundation.PWSTR), Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetXMLErrorInfo(pSemanticErrorInfo: POINTER(Windows.Win32.Media.Speech.SPSEMANTICERRORINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudio(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    Guid = Guid('cff8e175-019e-11d3-a0-8e-00-c0-4f-8e-f9-b5')
    @commethod(12)
    def get_Status(Status: POINTER(Windows.Win32.Media.Speech.ISpeechAudioStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_BufferInfo(BufferInfo: POINTER(Windows.Win32.Media.Speech.ISpeechAudioBufferInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_DefaultFormat(StreamFormat: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Volume(Volume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Volume(Volume: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BufferNotifySize(BufferNotifySize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BufferNotifySize(BufferNotifySize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EventHandle(EventHandle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetState(State: Windows.Win32.Media.Speech.SpeechAudioState) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioBufferInfo(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('11b103d8-1142-4edf-a0-93-82-fb-39-15-f8-cc')
    @commethod(7)
    def get_MinNotification(MinNotification: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_MinNotification(MinNotification: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BufferSize(BufferSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_BufferSize(BufferSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_EventBias(EventBias: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_EventBias(EventBias: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioFormat(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e6e9c590-3e18-40e3-82-99-06-1f-98-bd-e7-c7')
    @commethod(7)
    def get_Type(AudioFormat: POINTER(Windows.Win32.Media.Speech.SpeechAudioFormatType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Type(AudioFormat: Windows.Win32.Media.Speech.SpeechAudioFormatType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Guid(Guid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Guid(Guid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetWaveFormatEx(SpeechWaveFormatEx: POINTER(Windows.Win32.Media.Speech.ISpeechWaveFormatEx_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetWaveFormatEx(SpeechWaveFormatEx: Windows.Win32.Media.Speech.ISpeechWaveFormatEx_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioStatus(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c62d9c91-7458-47f6-86-2d-1e-f8-6f-b0-b2-78')
    @commethod(7)
    def get_FreeBufferSpace(FreeBufferSpace: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_NonBlockingIO(NonBlockingIO: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_State(State: POINTER(Windows.Win32.Media.Speech.SpeechAudioState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentSeekPosition(CurrentSeekPosition: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentDevicePosition(CurrentDevicePosition: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechBaseStream(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('6450336f-7d49-4ced-80-97-49-d6-de-e3-72-94')
    @commethod(7)
    def get_Format(AudioFormat: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def putref_Format(AudioFormat: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Read(Buffer: POINTER(Windows.Win32.System.Com.VARIANT_head), NumberOfBytes: Int32, BytesRead: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Write(Buffer: Windows.Win32.System.Com.VARIANT, BytesWritten: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Seek(Position: Windows.Win32.System.Com.VARIANT, Origin: Windows.Win32.Media.Speech.SpeechStreamSeekPositionType, NewPosition: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechCustomStream(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    Guid = Guid('1a9e9f4f-104f-4db8-a1-15-ef-d7-fd-0c-97-ae')
    @commethod(12)
    def get_BaseStream(ppUnkStream: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_BaseStream(pUnkStream: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechDataKey(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ce17c09b-4efa-44d5-a4-c9-59-d9-58-5a-b0-cd')
    @commethod(7)
    def SetBinaryValue(ValueName: Windows.Win32.Foundation.BSTR, Value: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBinaryValue(ValueName: Windows.Win32.Foundation.BSTR, Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetStringValue(ValueName: Windows.Win32.Foundation.BSTR, Value: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStringValue(ValueName: Windows.Win32.Foundation.BSTR, Value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLongValue(ValueName: Windows.Win32.Foundation.BSTR, Value: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLongValue(ValueName: Windows.Win32.Foundation.BSTR, Value: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OpenKey(SubKeyName: Windows.Win32.Foundation.BSTR, SubKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateKey(SubKeyName: Windows.Win32.Foundation.BSTR, SubKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def DeleteKey(SubKeyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteValue(ValueName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumKeys(Index: Int32, SubKeyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumValues(Index: Int32, ValueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechFileStream(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    Guid = Guid('af67f125-ab39-4e93-b4-a2-cc-2e-66-e1-82-a7')
    @commethod(12)
    def Open(FileName: Windows.Win32.Foundation.BSTR, FileMode: Windows.Win32.Media.Speech.SpeechStreamFileMode, DoEvents: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRule(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('afe719cf-5dd1-44f2-99-9c-7a-39-9f-1c-fc-cc')
    @commethod(7)
    def get_Attributes(Attributes: POINTER(Windows.Win32.Media.Speech.SpeechRuleAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_InitialState(State: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(Id: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clear() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddResource(ResourceName: Windows.Win32.Foundation.BSTR, ResourceValue: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddState(State: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleState(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d4286f2c-ee67-45ae-b9-28-28-d6-95-36-2e-da')
    @commethod(7)
    def get_Rule(Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Transitions(Transitions: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleStateTransitions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddWordTransition(DestState: Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head, Words: Windows.Win32.Foundation.BSTR, Separators: Windows.Win32.Foundation.BSTR, Type: Windows.Win32.Media.Speech.SpeechGrammarWordType, PropertyName: Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head), Weight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddRuleTransition(DestinationState: Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head, Rule: Windows.Win32.Media.Speech.ISpeechGrammarRule_head, PropertyName: Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head), Weight: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddSpecialTransition(DestinationState: Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head, Type: Windows.Win32.Media.Speech.SpeechSpecialTransitionType, PropertyName: Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head), Weight: Single) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleStateTransition(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('cafd1db1-41d1-4a06-98-63-e2-e8-1d-a1-7a-9a')
    @commethod(7)
    def get_Type(Type: POINTER(Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Text(Text: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Rule(Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Weight(Weight: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PropertyName(PropertyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PropertyId(PropertyId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PropertyValue(PropertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NextState(NextState: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleState_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleStateTransitions(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('eabce657-75bc-44a2-aa-7f-c5-64-76-74-29-63')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Transition: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRuleStateTransition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRules(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('6ffa3b44-fc2d-40d1-8a-fc-32-91-1c-7f-1a-d1')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindRule(RuleNameOrId: Windows.Win32.System.Com.VARIANT, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(Index: Int32, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Dynamic(Dynamic: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Add(RuleName: Windows.Win32.Foundation.BSTR, Attributes: Windows.Win32.Media.Speech.SpeechRuleAttributes, RuleId: Int32, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Commit() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CommitAndSave(ErrorText: POINTER(Windows.Win32.Foundation.BSTR), SaveStream: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexicon(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3da7627a-c7ae-4b23-87-08-63-8c-50-36-2c-25')
    @commethod(7)
    def get_GenerationId(GenerationId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(Flags: Windows.Win32.Media.Speech.SpeechLexiconType, GenerationID: POINTER(Int32), Words: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconWords_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddPronunciation(bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, bstrPronunciation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddPronunciationByPhoneIds(bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, PhoneIds: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemovePronunciation(bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, bstrPronunciation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemovePronunciationByPhoneIds(bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: Windows.Win32.Media.Speech.SpeechPartOfSpeech, PhoneIds: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPronunciations(bstrWord: Windows.Win32.Foundation.BSTR, LangId: Int32, TypeFlags: Windows.Win32.Media.Speech.SpeechLexiconType, ppPronunciations: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconPronunciations_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetGenerationChange(GenerationID: POINTER(Int32), ppWords: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconWords_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconPronunciation(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('95252c5d-9e43-4f4a-98-99-48-ee-73-35-2f-9f')
    @commethod(7)
    def get_Type(LexiconType: POINTER(Windows.Win32.Media.Speech.SpeechLexiconType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LangId(LangId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PartOfSpeech(PartOfSpeech: POINTER(Windows.Win32.Media.Speech.SpeechPartOfSpeech)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PhoneIds(PhoneIds: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Symbolic(Symbolic: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconPronunciations(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('72829128-5682-4704-a0-d4-3e-2b-b6-f2-ea-d3')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Pronunciation: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconPronunciation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconWord(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4e5b933c-c9be-48ed-88-42-1e-e5-1b-b1-d4-ff')
    @commethod(7)
    def get_LangId(LangId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Type(WordType: POINTER(Windows.Win32.Media.Speech.SpeechWordType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Word(Word: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Pronunciations(Pronunciations: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconPronunciations_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconWords(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8d199862-415e-47d5-ac-4f-fa-a6-08-b4-24-e6')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Word: POINTER(Windows.Win32.Media.Speech.ISpeechLexiconWord_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechMMSysAudio(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpeechAudio
    Guid = Guid('3c76af6d-1fd7-4831-81-d1-3b-71-d5-a1-3c-44')
    @commethod(21)
    def get_DeviceId(DeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DeviceId(DeviceId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LineId(LineId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_LineId(LineId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MMHandle(Handle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechMemoryStream(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpeechBaseStream
    Guid = Guid('eeb14b68-808b-4abe-a5-ea-b5-1d-a7-58-80-08')
    @commethod(12)
    def SetData(Data: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetData(pData: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectToken(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c74a3adc-b727-4500-a8-4a-b5-26-72-1c-8b-8c')
    @commethod(7)
    def get_Id(ObjectId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DataKey(DataKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Category(Category: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokenCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDescription(Locale: Int32, Description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetId(Id: Windows.Win32.Foundation.BSTR, CategoryID: Windows.Win32.Foundation.BSTR, CreateIfNotExist: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAttribute(AttributeName: Windows.Win32.Foundation.BSTR, AttributeValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateInstance(pUnkOuter: Windows.Win32.System.Com.IUnknown_head, ClsContext: Windows.Win32.Media.Speech.SpeechTokenContext, Object: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Remove(ObjectStorageCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStorageFileName(ObjectStorageCLSID: Windows.Win32.Foundation.BSTR, KeyName: Windows.Win32.Foundation.BSTR, FileName: Windows.Win32.Foundation.BSTR, Folder: Windows.Win32.Media.Speech.SpeechTokenShellFolder, FilePath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveStorageFileName(ObjectStorageCLSID: Windows.Win32.Foundation.BSTR, KeyName: Windows.Win32.Foundation.BSTR, DeleteFile: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def IsUISupported(TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Com.VARIANT_head), Object: Windows.Win32.System.Com.IUnknown_head, Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DisplayUI(hWnd: Int32, Title: Windows.Win32.Foundation.BSTR, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Com.VARIANT_head), Object: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def MatchesAttributes(Attributes: Windows.Win32.Foundation.BSTR, Matches: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectTokenCategory(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ca7eac50-2d01-4145-86-d4-5a-e7-d7-0f-44-69')
    @commethod(7)
    def get_Id(Id: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Default(TokenId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Default(TokenId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetId(Id: Windows.Win32.Foundation.BSTR, CreateIfNotExist: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDataKey(Location: Windows.Win32.Media.Speech.SpeechDataKeyLocation, DataKey: POINTER(Windows.Win32.Media.Speech.ISpeechDataKey_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumerateTokens(RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, Tokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectTokens(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9285b776-2e7b-4bc0-b5-3e-58-0e-b6-fa-96-7f')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Token: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhoneConverter(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c3e4f353-433f-43d6-89-a1-6a-62-a7-05-4c-3d')
    @commethod(7)
    def get_LanguageId(LanguageId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LanguageId(LanguageId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PhoneToId(Phonemes: Windows.Win32.Foundation.BSTR, IdArray: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IdToPhone(IdArray: Windows.Win32.System.Com.VARIANT, Phonemes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseAlternate(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('27864a2a-2b9f-4cb8-92-d3-0d-27-22-fd-1e-73')
    @commethod(7)
    def get_RecoResult(RecoResult: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_StartElementInResult(StartElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NumberOfElementsInResult(NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PhraseInfo(PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Commit() -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseAlternates(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b238b6d5-f276-4c3d-a6-c1-29-74-80-1c-3c-c2')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, PhraseAlternate: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseAlternate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseElement(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e6176f96-e373-4801-b2-23-3b-62-c0-68-c0-b4')
    @commethod(7)
    def get_AudioTimeOffset(AudioTimeOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AudioSizeTime(AudioSizeTime: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AudioStreamOffset(AudioStreamOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioSizeBytes(AudioSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RetainedStreamOffset(RetainedStreamOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RetainedSizeBytes(RetainedSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisplayText(DisplayText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_LexicalForm(LexicalForm: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Pronunciation(Pronunciation: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_DisplayAttributes(DisplayAttributes: POINTER(Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RequiredConfidence(RequiredConfidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ActualConfidence(ActualConfidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EngineConfidence(EngineConfidence: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseElements(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0626b328-3478-467d-a0-b3-d0-85-3b-93-dd-a3')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Element: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseInfo(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('961559cf-4e67-4662-8b-f0-d9-3f-1f-cd-61-b3')
    @commethod(7)
    def get_LanguageId(LanguageId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GrammarId(GrammarId: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StartTime(StartTime: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioStreamPosition(AudioStreamPosition: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AudioSizeBytes(pAudioSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RetainedSizeBytes(RetainedSizeBytes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AudioSizeTime(AudioSizeTime: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Rule(Rule: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Properties(Properties: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Elements(Elements: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseElements_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Replacements(Replacements: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseReplacements_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_EngineId(EngineIdGuid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EnginePrivateData(PrivateData: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SaveToMemory(PhraseBlock: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetText(StartElement: Int32, Elements: Int32, UseReplacements: Windows.Win32.Foundation.VARIANT_BOOL, Text: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetDisplayAttributes(StartElement: Int32, Elements: Int32, UseReplacements: Windows.Win32.Foundation.VARIANT_BOOL, DisplayAttributes: POINTER(Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseInfoBuilder(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3b151836-df3a-4e0a-84-6c-d2-ad-c9-33-43-33')
    @commethod(7)
    def RestorePhraseFromMemory(PhraseInMemory: POINTER(Windows.Win32.System.Com.VARIANT_head), PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseProperties(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('08166b47-102e-4b23-a5-99-bd-b9-8d-bf-d1-f4')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Property: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseProperty(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ce563d48-961e-4732-a2-e1-37-8a-42-b4-30-be')
    @commethod(7)
    def get_Name(Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(Id: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FirstElement(FirstElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_NumberOfElements(NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_EngineConfidence(Confidence: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Confidence(Confidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Parent(ParentProperty: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Children(Children: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseReplacement(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2890a410-53a7-4fb5-94-ec-06-d4-99-8e-3d-02')
    @commethod(7)
    def get_DisplayAttributes(DisplayAttributes: POINTER(Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Text(Text: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FirstElement(FirstElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfElements(NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseReplacements(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('38bc662f-2257-4525-95-9e-20-69-d2-59-6c-05')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Reps: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseReplacement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseRule(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('a7bfe112-a4a0-48d9-b6-02-c3-13-84-3f-69-64')
    @commethod(7)
    def get_Name(Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(Id: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FirstElement(FirstElement: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfElements(NumberOfElements: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Parent(Parent: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Children(Children: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Confidence(ActualConfidence: POINTER(Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_EngineConfidence(EngineConfidence: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseRules(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9047d593-01dd-4b72-81-a3-e4-a0-ca-69-f4-07')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Rule: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(EnumVARIANT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoContext(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('580aa49d-7e1e-4809-b8-e2-57-da-80-61-04-b8')
    @commethod(7)
    def get_Recognizer(Recognizer: POINTER(Windows.Win32.Media.Speech.ISpeechRecognizer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AudioInputInterferenceStatus(Interference: POINTER(Windows.Win32.Media.Speech.SpeechInterference)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_RequestedUIType(UIType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def putref_Voice(Voice: Windows.Win32.Media.Speech.ISpeechVoice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Voice(Voice: POINTER(Windows.Win32.Media.Speech.ISpeechVoice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowVoiceFormatMatchingOnNextSet(Allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowVoiceFormatMatchingOnNextSet(pAllow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_VoicePurgeEvent(EventInterest: Windows.Win32.Media.Speech.SpeechRecoEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_VoicePurgeEvent(EventInterest: POINTER(Windows.Win32.Media.Speech.SpeechRecoEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EventInterests(EventInterest: Windows.Win32.Media.Speech.SpeechRecoEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_EventInterests(EventInterest: POINTER(Windows.Win32.Media.Speech.SpeechRecoEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_CmdMaxAlternates(MaxAlternates: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CmdMaxAlternates(MaxAlternates: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_State(State: Windows.Win32.Media.Speech.SpeechRecoContextState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_State(State: POINTER(Windows.Win32.Media.Speech.SpeechRecoContextState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_RetainedAudio(Option: Windows.Win32.Media.Speech.SpeechRetainedAudioOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RetainedAudio(Option: POINTER(Windows.Win32.Media.Speech.SpeechRetainedAudioOptions)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def putref_RetainedAudioFormat(Format: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_RetainedAudioFormat(Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Pause() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Resume() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreateGrammar(GrammarId: Windows.Win32.System.Com.VARIANT, Grammar: POINTER(Windows.Win32.Media.Speech.ISpeechRecoGrammar_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateResultFromMemory(ResultBlock: POINTER(Windows.Win32.System.Com.VARIANT_head), Result: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Bookmark(Options: Windows.Win32.Media.Speech.SpeechBookmarkOptions, StreamPos: Windows.Win32.System.Com.VARIANT, BookmarkId: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetAdaptationData(AdaptationString: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoGrammar(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b6d6f79f-2158-4e50-b5-bc-9a-9c-cd-85-2a-09')
    @commethod(7)
    def get_Id(Id: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RecoContext(RecoContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_State(State: Windows.Win32.Media.Speech.SpeechGrammarState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(State: POINTER(Windows.Win32.Media.Speech.SpeechGrammarState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Rules(Rules: POINTER(Windows.Win32.Media.Speech.ISpeechGrammarRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Reset(NewLanguage: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CmdLoadFromFile(FileName: Windows.Win32.Foundation.BSTR, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CmdLoadFromObject(ClassId: Windows.Win32.Foundation.BSTR, GrammarName: Windows.Win32.Foundation.BSTR, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CmdLoadFromResource(hModule: Int32, ResourceName: Windows.Win32.System.Com.VARIANT, ResourceType: Windows.Win32.System.Com.VARIANT, LanguageId: Int32, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CmdLoadFromMemory(GrammarData: Windows.Win32.System.Com.VARIANT, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CmdLoadFromProprietaryGrammar(ProprietaryGuid: Windows.Win32.Foundation.BSTR, ProprietaryString: Windows.Win32.Foundation.BSTR, ProprietaryData: Windows.Win32.System.Com.VARIANT, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CmdSetRuleState(Name: Windows.Win32.Foundation.BSTR, State: Windows.Win32.Media.Speech.SpeechRuleState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CmdSetRuleIdState(RuleId: Int32, State: Windows.Win32.Media.Speech.SpeechRuleState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DictationLoad(TopicName: Windows.Win32.Foundation.BSTR, LoadOption: Windows.Win32.Media.Speech.SpeechLoadOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DictationUnload() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DictationSetState(State: Windows.Win32.Media.Speech.SpeechRuleState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWordSequenceData(Text: Windows.Win32.Foundation.BSTR, TextLength: Int32, Info: Windows.Win32.Media.Speech.ISpeechTextSelectionInformation_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTextSelection(Info: Windows.Win32.Media.Speech.ISpeechTextSelectionInformation_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsPronounceable(Word: Windows.Win32.Foundation.BSTR, WordPronounceable: POINTER(Windows.Win32.Media.Speech.SpeechWordPronounceable)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResult(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ed2879cf-ced9-4ee6-a5-34-de-01-91-d5-46-8d')
    @commethod(7)
    def get_RecoContext(RecoContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Times(Times: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResultTimes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_AudioFormat(Format: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioFormat(Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PhraseInfo(PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Alternates(RequestCount: Int32, StartElement: Int32, Elements: Int32, Alternates: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseAlternates_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Audio(StartElement: Int32, Elements: Int32, Stream: POINTER(Windows.Win32.Media.Speech.ISpeechMemoryStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SpeakAudio(StartElement: Int32, Elements: Int32, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveToMemory(ResultBlock: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscardResultInfo(ValueTypes: Windows.Win32.Media.Speech.SpeechDiscardType) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResult2(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpeechRecoResult
    Guid = Guid('8e0a246d-d3c8-45de-86-57-04-29-0c-45-8c-3c')
    @commethod(17)
    def SetTextFeedback(Feedback: Windows.Win32.Foundation.BSTR, WasSuccessful: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResultDispatch(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('6d60eb64-aced-40a6-bb-f3-4e-55-7f-71-de-e2')
    @commethod(7)
    def get_RecoContext(RecoContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Times(Times: POINTER(Windows.Win32.Media.Speech.ISpeechRecoResultTimes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_AudioFormat(Format: Windows.Win32.Media.Speech.ISpeechAudioFormat_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioFormat(Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PhraseInfo(PhraseInfo: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Alternates(RequestCount: Int32, StartElement: Int32, Elements: Int32, Alternates: POINTER(Windows.Win32.Media.Speech.ISpeechPhraseAlternates_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Audio(StartElement: Int32, Elements: Int32, Stream: POINTER(Windows.Win32.Media.Speech.ISpeechMemoryStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SpeakAudio(StartElement: Int32, Elements: Int32, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveToMemory(ResultBlock: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscardResultInfo(ValueTypes: Windows.Win32.Media.Speech.SpeechDiscardType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetXMLResult(Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetXMLErrorInfo(LineNumber: POINTER(Int32), ScriptLine: POINTER(Windows.Win32.Foundation.BSTR), Source: POINTER(Windows.Win32.Foundation.BSTR), Description: POINTER(Windows.Win32.Foundation.BSTR), ResultCode: POINTER(Windows.Win32.Foundation.HRESULT), IsError: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetTextFeedback(Feedback: Windows.Win32.Foundation.BSTR, WasSuccessful: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResultTimes(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('62b3b8fb-f6e7-41be-bd-cb-05-6b-1c-29-ef-c0')
    @commethod(7)
    def get_StreamTime(Time: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Length(Length: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TickCount(TickCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OffsetFromStart(OffsetFromStart: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecognizer(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2d5f1c0c-bd75-4b08-94-78-3b-11-fe-a2-58-6c')
    @commethod(7)
    def putref_Recognizer(Recognizer: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Recognizer(Recognizer: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_AllowAudioInputFormatChangesOnNextSet(Allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AllowAudioInputFormatChangesOnNextSet(Allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_AudioInput(AudioInput: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_AudioInput(AudioInput: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_AudioInputStream(AudioInputStream: Windows.Win32.Media.Speech.ISpeechBaseStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AudioInputStream(AudioInputStream: POINTER(Windows.Win32.Media.Speech.ISpeechBaseStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsShared(Shared: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_State(State: Windows.Win32.Media.Speech.SpeechRecognizerState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_State(State: POINTER(Windows.Win32.Media.Speech.SpeechRecognizerState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Status(Status: POINTER(Windows.Win32.Media.Speech.ISpeechRecognizerStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def putref_Profile(Profile: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Profile(Profile: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EmulateRecognition(TextElements: Windows.Win32.System.Com.VARIANT, ElementDisplayAttributes: POINTER(Windows.Win32.System.Com.VARIANT_head), LanguageId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateRecoContext(NewContext: POINTER(Windows.Win32.Media.Speech.ISpeechRecoContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetFormat(Type: Windows.Win32.Media.Speech.SpeechFormatType, Format: POINTER(Windows.Win32.Media.Speech.ISpeechAudioFormat_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetPropertyNumber(Name: Windows.Win32.Foundation.BSTR, Value: Int32, Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPropertyNumber(Name: Windows.Win32.Foundation.BSTR, Value: POINTER(Int32), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetPropertyString(Name: Windows.Win32.Foundation.BSTR, Value: Windows.Win32.Foundation.BSTR, Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetPropertyString(Name: Windows.Win32.Foundation.BSTR, Value: POINTER(Windows.Win32.Foundation.BSTR), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def IsUISupported(TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Com.VARIANT_head), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DisplayUI(hWndParent: Int32, Title: Windows.Win32.Foundation.BSTR, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetRecognizers(RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetAudioInputs(RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetProfiles(RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecognizerStatus(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('bff9e781-53ec-484e-bb-8a-0e-1b-55-51-e3-5c')
    @commethod(7)
    def get_AudioStatus(AudioStatus: POINTER(Windows.Win32.Media.Speech.ISpeechAudioStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentStreamPosition(pCurrentStreamPos: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentStreamNumber(StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfActiveRules(NumberOfActiveRules: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ClsidEngine(ClsidEngine: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SupportedLanguages(SupportedLanguages: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechResourceLoader(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b9ac5783-fcd0-4b21-b1-19-b4-f8-da-8f-d2-c3')
    @commethod(7)
    def LoadResource(bstrResourceUri: Windows.Win32.Foundation.BSTR, fAlwaysReload: Windows.Win32.Foundation.VARIANT_BOOL, pStream: POINTER(Windows.Win32.System.Com.IUnknown_head), pbstrMIMEType: POINTER(Windows.Win32.Foundation.BSTR), pfModified: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), pbstrRedirectUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLocalCopy(bstrResourceUri: Windows.Win32.Foundation.BSTR, pbstrLocalPath: POINTER(Windows.Win32.Foundation.BSTR), pbstrMIMEType: POINTER(Windows.Win32.Foundation.BSTR), pbstrRedirectUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ReleaseLocalCopy(pbstrLocalPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechTextSelectionInformation(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3b9c7e7a-6eee-4ded-90-92-11-65-72-79-ad-be')
    @commethod(7)
    def put_ActiveOffset(ActiveOffset: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActiveOffset(ActiveOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ActiveLength(ActiveLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ActiveLength(ActiveLength: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_SelectionOffset(SelectionOffset: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SelectionOffset(SelectionOffset: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_SelectionLength(SelectionLength: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SelectionLength(SelectionLength: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechVoice(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('269316d8-57bd-11d2-9e-ee-00-c0-4f-79-73-96')
    @commethod(7)
    def get_Status(Status: POINTER(Windows.Win32.Media.Speech.ISpeechVoiceStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Voice(Voice: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_Voice(Voice: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioOutput(AudioOutput: POINTER(Windows.Win32.Media.Speech.ISpeechObjectToken_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_AudioOutput(AudioOutput: Windows.Win32.Media.Speech.ISpeechObjectToken_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_AudioOutputStream(AudioOutputStream: POINTER(Windows.Win32.Media.Speech.ISpeechBaseStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_AudioOutputStream(AudioOutputStream: Windows.Win32.Media.Speech.ISpeechBaseStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Rate(Rate: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Rate(Rate: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Volume(Volume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Volume(Volume: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowAudioOutputFormatChangesOnNextSet(Allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_AllowAudioOutputFormatChangesOnNextSet(Allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_EventInterests(EventInterestFlags: POINTER(Windows.Win32.Media.Speech.SpeechVoiceEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_EventInterests(EventInterestFlags: Windows.Win32.Media.Speech.SpeechVoiceEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Priority(Priority: Windows.Win32.Media.Speech.SpeechVoicePriority) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Priority(Priority: POINTER(Windows.Win32.Media.Speech.SpeechVoicePriority)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AlertBoundary(Boundary: Windows.Win32.Media.Speech.SpeechVoiceEvents) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AlertBoundary(Boundary: POINTER(Windows.Win32.Media.Speech.SpeechVoiceEvents)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_SynchronousSpeakTimeout(msTimeout: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_SynchronousSpeakTimeout(msTimeout: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Speak(Text: Windows.Win32.Foundation.BSTR, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SpeakStream(Stream: Windows.Win32.Media.Speech.ISpeechBaseStream_head, Flags: Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Pause() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Resume() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Skip(Type: Windows.Win32.Foundation.BSTR, NumItems: Int32, NumSkipped: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetVoices(RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetAudioOutputs(RequiredAttributes: Windows.Win32.Foundation.BSTR, OptionalAttributes: Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(Windows.Win32.Media.Speech.ISpeechObjectTokens_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def WaitUntilDone(msTimeout: Int32, Done: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SpeakCompleteEvent(Handle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def IsUISupported(TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Com.VARIANT_head), Supported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def DisplayUI(hWndParent: Int32, Title: Windows.Win32.Foundation.BSTR, TypeOfUI: Windows.Win32.Foundation.BSTR, ExtraData: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechVoiceStatus(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8be47b07-57f6-11d2-9e-ee-00-c0-4f-79-73-96')
    @commethod(7)
    def get_CurrentStreamNumber(StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LastStreamNumberQueued(StreamNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LastHResult(HResult: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RunningState(State: POINTER(Windows.Win32.Media.Speech.SpeechRunState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InputWordPosition(Position: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InputWordLength(Length: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_InputSentencePosition(Position: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_InputSentenceLength(Length: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LastBookmark(Bookmark: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_LastBookmarkId(BookmarkId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_PhonemeId(PhoneId: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_VisemeId(VisemeId: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechWaveFormatEx(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7a1ef0d5-1581-4741-88-e4-20-9a-49-f1-1a-10')
    @commethod(7)
    def get_FormatTag(FormatTag: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_FormatTag(FormatTag: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Channels(Channels: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Channels(Channels: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SamplesPerSec(SamplesPerSec: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SamplesPerSec(SamplesPerSec: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AvgBytesPerSec(AvgBytesPerSec: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AvgBytesPerSec(AvgBytesPerSec: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_BlockAlign(BlockAlign: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_BlockAlign(BlockAlign: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BitsPerSample(BitsPerSample: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BitsPerSample(BitsPerSample: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ExtraData(ExtraData: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ExtraData(ExtraData: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class ISpeechXMLRecoResult(c_void_p):
    extends: Windows.Win32.Media.Speech.ISpeechRecoResult
    Guid = Guid('aaec54af-8f85-4924-94-4d-b7-9d-39-d7-2e-19')
    @commethod(17)
    def GetXMLResult(Options: Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetXMLErrorInfo(LineNumber: POINTER(Int32), ScriptLine: POINTER(Windows.Win32.Foundation.BSTR), Source: POINTER(Windows.Win32.Foundation.BSTR), Description: POINTER(Windows.Win32.Foundation.BSTR), ResultCode: POINTER(Int32), IsError: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
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
class SPAUDIOBUFFERINFO(Structure):
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
class SPAUDIOSTATUS(Structure):
    cbFreeBuffSpace: Int32
    cbNonBlockingIO: UInt32
    State: Windows.Win32.Media.Speech.SPAUDIOSTATE
    CurSeekPos: UInt64
    CurDevicePos: UInt64
    dwAudioLevel: UInt32
    dwReserved2: UInt32
class SPBINARYGRAMMAR(Structure):
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
class SPDISPLAYPHRASE(Structure):
    ulNumTokens: UInt32
    pTokens: POINTER(Windows.Win32.Media.Speech.SPDISPLAYTOKEN_head)
class SPDISPLAYTOKEN(Structure):
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
class SPEVENT(Structure):
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
class SPEVENTEX(Structure):
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
class SPEVENTSOURCEINFO(Structure):
    ullEventInterest: UInt64
    ullQueuedInterest: UInt64
    ulCount: UInt32
SPFILEMODE = Int32
SPFM_OPEN_READONLY: SPFILEMODE = 0
SPFM_OPEN_READWRITE: SPFILEMODE = 1
SPFM_CREATE: SPFILEMODE = 2
SPFM_CREATE_ALWAYS: SPFILEMODE = 3
SPFM_NUM_MODES: SPFILEMODE = 4
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
class SPNORMALIZATIONLIST(Structure):
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
class SPPHRASE(Structure):
    Base: Windows.Win32.Media.Speech.SPPHRASE_50
    pSML: Windows.Win32.Foundation.PWSTR
    pSemanticErrorInfo: POINTER(Windows.Win32.Media.Speech.SPSEMANTICERRORINFO_head)
class SPPHRASEELEMENT(Structure):
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
class SPPHRASEPROPERTY(Structure):
    pszName: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    pszValue: Windows.Win32.Foundation.PWSTR
    vValue: Windows.Win32.System.Com.VARIANT
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
    pNextSibling: POINTER(Windows.Win32.Media.Speech.SPPHRASEPROPERTY_head)
    pFirstChild: POINTER(Windows.Win32.Media.Speech.SPPHRASEPROPERTY_head)
    SREngineConfidence: Single
    Confidence: SByte
    class _Anonymous_e__Union(Union):
        ulId: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            bType: Byte
            bReserved: Byte
            usArrayIndex: UInt16
SPPHRASEPROPERTYUNIONTYPE = Int32
SPPPUT_UNUSED: SPPHRASEPROPERTYUNIONTYPE = 0
SPPPUT_ARRAY_INDEX: SPPHRASEPROPERTYUNIONTYPE = 1
class SPPHRASEREPLACEMENT(Structure):
    bDisplayAttributes: Byte
    pszReplacementText: Windows.Win32.Foundation.PWSTR
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
SPPHRASERNG = Int32
SPPR_ALL_ELEMENTS: SPPHRASERNG = -1
class SPPHRASERULE(Structure):
    pszName: Windows.Win32.Foundation.PWSTR
    ulId: UInt32
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
    pNextSibling: POINTER(Windows.Win32.Media.Speech.SPPHRASERULE_head)
    pFirstChild: POINTER(Windows.Win32.Media.Speech.SPPHRASERULE_head)
    SREngineConfidence: Single
    Confidence: SByte
class SPPHRASE_50(Structure):
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
    pSREnginePrivateData: c_char_p_no
SPPRONUNCIATIONFLAGS = Int32
ePRONFLAG_USED: SPPRONUNCIATIONFLAGS = 1
class SPPROPERTYINFO(Structure):
    pszName: Windows.Win32.Foundation.PWSTR
    ulId: UInt32
    pszValue: Windows.Win32.Foundation.PWSTR
    vValue: Windows.Win32.System.Com.VARIANT
class SPRECOCONTEXTSTATUS(Structure):
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
class SPRECOGNIZERSTATUS(Structure):
    AudioStatus: Windows.Win32.Media.Speech.SPAUDIOSTATUS
    ullRecognitionStreamPos: UInt64
    ulStreamNumber: UInt32
    ulNumActive: UInt32
    clsidEngine: Guid
    cLangIDs: UInt32
    aLangID: UInt16 * 20
    ullRecognitionStreamTime: UInt64
class SPRECORESULTTIMES(Structure):
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
class SPRULE(Structure):
    pszRuleName: Windows.Win32.Foundation.PWSTR
    ulRuleId: UInt32
    dwAttributes: UInt32
SPRULESTATE = Int32
SPRS_INACTIVE: SPRULESTATE = 0
SPRS_ACTIVE: SPRULESTATE = 1
SPRS_ACTIVE_WITH_AUTO_PAUSE: SPRULESTATE = 3
SPRS_ACTIVE_USER_DELIMITED: SPRULESTATE = 4
SPRUNSTATE = Int32
SPRS_DONE: SPRUNSTATE = 1
SPRS_IS_SPEAKING: SPRUNSTATE = 2
class SPSEMANTICERRORINFO(Structure):
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
class SPSERIALIZEDEVENT(Structure):
    _bitfield: Int32
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    SerializedwParam: UInt32
    SerializedlParam: Int32
class SPSERIALIZEDEVENT64(Structure):
    _bitfield: Int32
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    SerializedwParam: UInt64
    SerializedlParam: Int64
class SPSERIALIZEDPHRASE(Structure):
    ulSerializedSize: UInt32
class SPSERIALIZEDRESULT(Structure):
    ulSerializedSize: UInt32
class SPSHORTCUTPAIR(Structure):
    pNextSHORTCUTPAIR: POINTER(Windows.Win32.Media.Speech.SPSHORTCUTPAIR_head)
    LangID: UInt16
    shType: Windows.Win32.Media.Speech.SPSHORTCUTTYPE
    pszDisplay: Windows.Win32.Foundation.PWSTR
    pszSpoken: Windows.Win32.Foundation.PWSTR
class SPSHORTCUTPAIRLIST(Structure):
    ulSize: UInt32
    pvBuffer: c_char_p_no
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
class SPSTATEHANDLE__(Structure):
    unused: Int32
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
class SPTEXTSELECTIONINFO(Structure):
    ulStartActiveOffset: UInt32
    cchActiveChars: UInt32
    ulStartSelection: UInt32
    cchSelection: UInt32
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
class SPVCONTEXT(Structure):
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
class SPVOICESTATUS(Structure):
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
class SPVPITCH(Structure):
    MiddleAdj: Int32
    RangeAdj: Int32
SPVPRIORITY = Int32
SPVPRI_NORMAL: SPVPRIORITY = 0
SPVPRI_ALERT: SPVPRIORITY = 1
SPVPRI_OVER: SPVPRIORITY = 2
class SPVSTATE(Structure):
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
class SPWORD(Structure):
    pNextWord: POINTER(Windows.Win32.Media.Speech.SPWORD_head)
    LangID: UInt16
    wReserved: UInt16
    eWordType: Windows.Win32.Media.Speech.SPWORDTYPE
    pszWord: Windows.Win32.Foundation.PWSTR
    pFirstWordPronunciation: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATION_head)
class SPWORDLIST(Structure):
    ulSize: UInt32
    pvBuffer: c_char_p_no
    pFirstWord: POINTER(Windows.Win32.Media.Speech.SPWORD_head)
SPWORDPRONOUNCEABLE = Int32
SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE: SPWORDPRONOUNCEABLE = 0
SPWP_UNKNOWN_WORD_PRONOUNCEABLE: SPWORDPRONOUNCEABLE = 1
SPWP_KNOWN_WORD_PRONOUNCEABLE: SPWORDPRONOUNCEABLE = 2
class SPWORDPRONUNCIATION(Structure):
    pNextWordPronunciation: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATION_head)
    eLexiconType: Windows.Win32.Media.Speech.SPLEXICONTYPE
    LangID: UInt16
    wPronunciationFlags: UInt16
    ePartOfSpeech: Windows.Win32.Media.Speech.SPPARTOFSPEECH
    szPronunciation: UInt16 * 1
class SPWORDPRONUNCIATIONLIST(Structure):
    ulSize: UInt32
    pvBuffer: c_char_p_no
    pFirstWordPronunciation: POINTER(Windows.Win32.Media.Speech.SPWORDPRONUNCIATION_head)
SPWORDTYPE = Int32
eWORDTYPE_ADDED: SPWORDTYPE = 1
eWORDTYPE_DELETED: SPWORDTYPE = 2
SPXMLRESULTOPTIONS = Int32
SPXRO_SML: SPXMLRESULTOPTIONS = 0
SPXRO_Alternates_SML: SPXMLRESULTOPTIONS = 1
SpAudioFormat = Guid('9ef96870-e160-4792-82-0d-48-cf-06-49-e4-ec')
SpCompressedLexicon = Guid('90903716-2f42-11d3-9c-26-00-c0-4f-8e-f8-7c')
SpCustomStream = Guid('8dbef13f-1948-4aa8-8c-f0-04-8e-eb-ed-95-d8')
SpFileStream = Guid('947812b3-2ae1-4644-ba-86-9e-90-de-d7-ec-91')
SpInProcRecoContext = Guid('73ad6842-ace0-45e8-a4-dd-87-95-88-1a-2c-2a')
SpInprocRecognizer = Guid('41b89b6b-9399-11d2-96-23-00-c0-4f-8e-e6-28')
SpLexicon = Guid('0655e396-25d0-11d3-9c-26-00-c0-4f-8e-f8-7c')
SpMMAudioEnum = Guid('ab1890a0-e91f-11d2-bb-91-00-c0-4f-8e-e6-c0')
SpMMAudioIn = Guid('cf3d2e50-53f2-11d2-96-0c-00-c0-4f-8e-e6-28')
SpMMAudioOut = Guid('a8c680eb-3d32-11d2-9e-e7-00-c0-4f-79-73-96')
SpMemoryStream = Guid('5fb7ef7d-dff4-468a-b6-b7-2f-cb-d1-88-f9-94')
SpNotifyTranslator = Guid('e2ae5372-5d40-11d2-96-0e-00-c0-4f-8e-e6-28')
SpNullPhoneConverter = Guid('455f24e9-7396-4a16-97-15-7c-0f-db-e3-ef-e3')
SpObjectToken = Guid('ef411752-3736-4cb4-9c-8c-8e-f4-cc-b5-8e-fe')
SpObjectTokenCategory = Guid('a910187f-0c7a-45ac-92-cc-59-ed-af-b7-7b-53')
SpPhoneConverter = Guid('9185f743-1143-4c28-86-b5-bf-f1-4f-20-e5-c8')
SpPhoneticAlphabetConverter = Guid('4f414126-dfe3-4629-99-ee-79-79-78-31-7e-ad')
SpPhraseInfoBuilder = Guid('c23fc28d-c55f-4720-8b-32-91-f7-3c-2b-d5-d1')
SpResourceManager = Guid('96749373-3391-11d2-9e-e3-00-c0-4f-79-73-96')
SpSharedRecoContext = Guid('47206204-5eca-11d2-96-0f-00-c0-4f-8e-e6-28')
SpSharedRecognizer = Guid('3bee4890-4fe9-4a37-8c-1e-5e-7e-12-79-1c-1f')
SpShortcut = Guid('0d722f1a-9fcf-4e62-96-d8-6d-f8-f0-1a-26-aa')
SpStream = Guid('715d9c59-4442-11d2-96-05-00-c0-4f-8e-e6-28')
SpStreamFormatConverter = Guid('7013943a-e2ec-11d2-a0-86-00-c0-4f-8e-f9-b5')
SpTextSelectionInformation = Guid('0f92030a-cbfd-4ab8-a1-64-ff-59-85-54-7f-f6')
SpUnCompressedLexicon = Guid('c9e37c15-df92-4727-85-d6-72-e5-ee-b6-99-5a')
SpVoice = Guid('96749377-3391-11d2-9e-e3-00-c0-4f-79-73-96')
SpWaveFormatEx = Guid('c79a574c-63be-44b9-80-1f-28-3f-87-f8-98-be')
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
class _ISpeechRecoContextEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7b8fcb42-0e9d-4f00-a0-48-7b-04-d6-17-9d-3d')
class _ISpeechVoiceEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('a372acd1-3bef-4bbd-8f-fb-cb-3e-2b-41-6a-f8')
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
make_head(_module, 'SPSTATEHANDLE__')
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
__all__ = [
    "DEFAULT_WEIGHT",
    "DISPIDSPRG",
    "DISPIDSPTSI",
    "DISPIDSPTSI_ActiveLength",
    "DISPIDSPTSI_ActiveOffset",
    "DISPIDSPTSI_SelectionLength",
    "DISPIDSPTSI_SelectionOffset",
    "DISPID_SABIBufferSize",
    "DISPID_SABIEventBias",
    "DISPID_SABIMinNotification",
    "DISPID_SABufferInfo",
    "DISPID_SABufferNotifySize",
    "DISPID_SADefaultFormat",
    "DISPID_SAEventHandle",
    "DISPID_SAFGetWaveFormatEx",
    "DISPID_SAFGuid",
    "DISPID_SAFSetWaveFormatEx",
    "DISPID_SAFType",
    "DISPID_SASCurrentDevicePosition",
    "DISPID_SASCurrentSeekPosition",
    "DISPID_SASFreeBufferSpace",
    "DISPID_SASNonBlockingIO",
    "DISPID_SASState",
    "DISPID_SASetState",
    "DISPID_SAStatus",
    "DISPID_SAVolume",
    "DISPID_SBSFormat",
    "DISPID_SBSRead",
    "DISPID_SBSSeek",
    "DISPID_SBSWrite",
    "DISPID_SCSBaseStream",
    "DISPID_SDKCreateKey",
    "DISPID_SDKDeleteKey",
    "DISPID_SDKDeleteValue",
    "DISPID_SDKEnumKeys",
    "DISPID_SDKEnumValues",
    "DISPID_SDKGetBinaryValue",
    "DISPID_SDKGetStringValue",
    "DISPID_SDKGetlongValue",
    "DISPID_SDKOpenKey",
    "DISPID_SDKSetBinaryValue",
    "DISPID_SDKSetLongValue",
    "DISPID_SDKSetStringValue",
    "DISPID_SFSClose",
    "DISPID_SFSOpen",
    "DISPID_SGRAddResource",
    "DISPID_SGRAddState",
    "DISPID_SGRAttributes",
    "DISPID_SGRClear",
    "DISPID_SGRId",
    "DISPID_SGRInitialState",
    "DISPID_SGRName",
    "DISPID_SGRSAddRuleTransition",
    "DISPID_SGRSAddSpecialTransition",
    "DISPID_SGRSAddWordTransition",
    "DISPID_SGRSRule",
    "DISPID_SGRSTNextState",
    "DISPID_SGRSTPropertyId",
    "DISPID_SGRSTPropertyName",
    "DISPID_SGRSTPropertyValue",
    "DISPID_SGRSTRule",
    "DISPID_SGRSTText",
    "DISPID_SGRSTType",
    "DISPID_SGRSTWeight",
    "DISPID_SGRSTransitions",
    "DISPID_SGRSTsCount",
    "DISPID_SGRSTsItem",
    "DISPID_SGRSTs_NewEnum",
    "DISPID_SGRsAdd",
    "DISPID_SGRsCommit",
    "DISPID_SGRsCommitAndSave",
    "DISPID_SGRsCount",
    "DISPID_SGRsDynamic",
    "DISPID_SGRsFindRule",
    "DISPID_SGRsItem",
    "DISPID_SGRs_NewEnum",
    "DISPID_SLAddPronunciation",
    "DISPID_SLAddPronunciationByPhoneIds",
    "DISPID_SLGenerationId",
    "DISPID_SLGetGenerationChange",
    "DISPID_SLGetPronunciations",
    "DISPID_SLGetWords",
    "DISPID_SLPLangId",
    "DISPID_SLPPartOfSpeech",
    "DISPID_SLPPhoneIds",
    "DISPID_SLPSymbolic",
    "DISPID_SLPType",
    "DISPID_SLPsCount",
    "DISPID_SLPsItem",
    "DISPID_SLPs_NewEnum",
    "DISPID_SLRemovePronunciation",
    "DISPID_SLRemovePronunciationByPhoneIds",
    "DISPID_SLWLangId",
    "DISPID_SLWPronunciations",
    "DISPID_SLWType",
    "DISPID_SLWWord",
    "DISPID_SLWsCount",
    "DISPID_SLWsItem",
    "DISPID_SLWs_NewEnum",
    "DISPID_SMSADeviceId",
    "DISPID_SMSALineId",
    "DISPID_SMSAMMHandle",
    "DISPID_SMSGetData",
    "DISPID_SMSSetData",
    "DISPID_SOTCDefault",
    "DISPID_SOTCEnumerateTokens",
    "DISPID_SOTCGetDataKey",
    "DISPID_SOTCId",
    "DISPID_SOTCSetId",
    "DISPID_SOTCategory",
    "DISPID_SOTCreateInstance",
    "DISPID_SOTDataKey",
    "DISPID_SOTDisplayUI",
    "DISPID_SOTGetAttribute",
    "DISPID_SOTGetDescription",
    "DISPID_SOTGetStorageFileName",
    "DISPID_SOTId",
    "DISPID_SOTIsUISupported",
    "DISPID_SOTMatchesAttributes",
    "DISPID_SOTRemove",
    "DISPID_SOTRemoveStorageFileName",
    "DISPID_SOTSetId",
    "DISPID_SOTsCount",
    "DISPID_SOTsItem",
    "DISPID_SOTs_NewEnum",
    "DISPID_SPACommit",
    "DISPID_SPANumberOfElementsInResult",
    "DISPID_SPAPhraseInfo",
    "DISPID_SPARecoResult",
    "DISPID_SPAStartElementInResult",
    "DISPID_SPAsCount",
    "DISPID_SPAsItem",
    "DISPID_SPAs_NewEnum",
    "DISPID_SPCIdToPhone",
    "DISPID_SPCLangId",
    "DISPID_SPCPhoneToId",
    "DISPID_SPEActualConfidence",
    "DISPID_SPEAudioSizeBytes",
    "DISPID_SPEAudioSizeTime",
    "DISPID_SPEAudioStreamOffset",
    "DISPID_SPEAudioTimeOffset",
    "DISPID_SPEDisplayAttributes",
    "DISPID_SPEDisplayText",
    "DISPID_SPEEngineConfidence",
    "DISPID_SPELexicalForm",
    "DISPID_SPEPronunciation",
    "DISPID_SPERequiredConfidence",
    "DISPID_SPERetainedSizeBytes",
    "DISPID_SPERetainedStreamOffset",
    "DISPID_SPEsCount",
    "DISPID_SPEsItem",
    "DISPID_SPEs_NewEnum",
    "DISPID_SPIAudioSizeBytes",
    "DISPID_SPIAudioSizeTime",
    "DISPID_SPIAudioStreamPosition",
    "DISPID_SPIElements",
    "DISPID_SPIEngineId",
    "DISPID_SPIEnginePrivateData",
    "DISPID_SPIGetDisplayAttributes",
    "DISPID_SPIGetText",
    "DISPID_SPIGrammarId",
    "DISPID_SPILanguageId",
    "DISPID_SPIProperties",
    "DISPID_SPIReplacements",
    "DISPID_SPIRetainedSizeBytes",
    "DISPID_SPIRule",
    "DISPID_SPISaveToMemory",
    "DISPID_SPIStartTime",
    "DISPID_SPPBRestorePhraseFromMemory",
    "DISPID_SPPChildren",
    "DISPID_SPPConfidence",
    "DISPID_SPPEngineConfidence",
    "DISPID_SPPFirstElement",
    "DISPID_SPPId",
    "DISPID_SPPName",
    "DISPID_SPPNumberOfElements",
    "DISPID_SPPParent",
    "DISPID_SPPValue",
    "DISPID_SPPsCount",
    "DISPID_SPPsItem",
    "DISPID_SPPs_NewEnum",
    "DISPID_SPRDisplayAttributes",
    "DISPID_SPRFirstElement",
    "DISPID_SPRNumberOfElements",
    "DISPID_SPRText",
    "DISPID_SPRsCount",
    "DISPID_SPRsItem",
    "DISPID_SPRs_NewEnum",
    "DISPID_SPRuleChildren",
    "DISPID_SPRuleConfidence",
    "DISPID_SPRuleEngineConfidence",
    "DISPID_SPRuleFirstElement",
    "DISPID_SPRuleId",
    "DISPID_SPRuleName",
    "DISPID_SPRuleNumberOfElements",
    "DISPID_SPRuleParent",
    "DISPID_SPRulesCount",
    "DISPID_SPRulesItem",
    "DISPID_SPRules_NewEnum",
    "DISPID_SRAllowAudioInputFormatChangesOnNextSet",
    "DISPID_SRAllowVoiceFormatMatchingOnNextSet",
    "DISPID_SRAudioInput",
    "DISPID_SRAudioInputStream",
    "DISPID_SRCAudioInInterferenceStatus",
    "DISPID_SRCBookmark",
    "DISPID_SRCCmdMaxAlternates",
    "DISPID_SRCCreateGrammar",
    "DISPID_SRCCreateResultFromMemory",
    "DISPID_SRCEAdaptation",
    "DISPID_SRCEAudioLevel",
    "DISPID_SRCEBookmark",
    "DISPID_SRCEEndStream",
    "DISPID_SRCEEnginePrivate",
    "DISPID_SRCEFalseRecognition",
    "DISPID_SRCEHypothesis",
    "DISPID_SRCEInterference",
    "DISPID_SRCEPhraseStart",
    "DISPID_SRCEPropertyNumberChange",
    "DISPID_SRCEPropertyStringChange",
    "DISPID_SRCERecognition",
    "DISPID_SRCERecognitionForOtherContext",
    "DISPID_SRCERecognizerStateChange",
    "DISPID_SRCERequestUI",
    "DISPID_SRCESoundEnd",
    "DISPID_SRCESoundStart",
    "DISPID_SRCEStartStream",
    "DISPID_SRCEventInterests",
    "DISPID_SRCPause",
    "DISPID_SRCRecognizer",
    "DISPID_SRCRequestedUIType",
    "DISPID_SRCResume",
    "DISPID_SRCRetainedAudio",
    "DISPID_SRCRetainedAudioFormat",
    "DISPID_SRCSetAdaptationData",
    "DISPID_SRCState",
    "DISPID_SRCVoice",
    "DISPID_SRCVoicePurgeEvent",
    "DISPID_SRCreateRecoContext",
    "DISPID_SRDisplayUI",
    "DISPID_SREmulateRecognition",
    "DISPID_SRGCmdLoadFromFile",
    "DISPID_SRGCmdLoadFromMemory",
    "DISPID_SRGCmdLoadFromObject",
    "DISPID_SRGCmdLoadFromProprietaryGrammar",
    "DISPID_SRGCmdLoadFromResource",
    "DISPID_SRGCmdSetRuleIdState",
    "DISPID_SRGCmdSetRuleState",
    "DISPID_SRGCommit",
    "DISPID_SRGDictationLoad",
    "DISPID_SRGDictationSetState",
    "DISPID_SRGDictationUnload",
    "DISPID_SRGId",
    "DISPID_SRGIsPronounceable",
    "DISPID_SRGRecoContext",
    "DISPID_SRGReset",
    "DISPID_SRGRules",
    "DISPID_SRGSetTextSelection",
    "DISPID_SRGSetWordSequenceData",
    "DISPID_SRGState",
    "DISPID_SRGetFormat",
    "DISPID_SRGetPropertyNumber",
    "DISPID_SRGetPropertyString",
    "DISPID_SRGetRecognizers",
    "DISPID_SRIsShared",
    "DISPID_SRIsUISupported",
    "DISPID_SRProfile",
    "DISPID_SRRAlternates",
    "DISPID_SRRAudio",
    "DISPID_SRRAudioFormat",
    "DISPID_SRRDiscardResultInfo",
    "DISPID_SRRGetXMLErrorInfo",
    "DISPID_SRRGetXMLResult",
    "DISPID_SRRPhraseInfo",
    "DISPID_SRRRecoContext",
    "DISPID_SRRSaveToMemory",
    "DISPID_SRRSetTextFeedback",
    "DISPID_SRRSpeakAudio",
    "DISPID_SRRTLength",
    "DISPID_SRRTOffsetFromStart",
    "DISPID_SRRTStreamTime",
    "DISPID_SRRTTickCount",
    "DISPID_SRRTimes",
    "DISPID_SRRecognizer",
    "DISPID_SRSAudioStatus",
    "DISPID_SRSClsidEngine",
    "DISPID_SRSCurrentStreamNumber",
    "DISPID_SRSCurrentStreamPosition",
    "DISPID_SRSNumberOfActiveRules",
    "DISPID_SRSSupportedLanguages",
    "DISPID_SRSetPropertyNumber",
    "DISPID_SRSetPropertyString",
    "DISPID_SRState",
    "DISPID_SRStatus",
    "DISPID_SVAlertBoundary",
    "DISPID_SVAllowAudioOuputFormatChangesOnNextSet",
    "DISPID_SVAudioOutput",
    "DISPID_SVAudioOutputStream",
    "DISPID_SVDisplayUI",
    "DISPID_SVEAudioLevel",
    "DISPID_SVEBookmark",
    "DISPID_SVEEnginePrivate",
    "DISPID_SVEPhoneme",
    "DISPID_SVESentenceBoundary",
    "DISPID_SVEStreamEnd",
    "DISPID_SVEStreamStart",
    "DISPID_SVEViseme",
    "DISPID_SVEVoiceChange",
    "DISPID_SVEWord",
    "DISPID_SVEventInterests",
    "DISPID_SVGetAudioInputs",
    "DISPID_SVGetAudioOutputs",
    "DISPID_SVGetProfiles",
    "DISPID_SVGetVoices",
    "DISPID_SVIsUISupported",
    "DISPID_SVPause",
    "DISPID_SVPriority",
    "DISPID_SVRate",
    "DISPID_SVResume",
    "DISPID_SVSCurrentStreamNumber",
    "DISPID_SVSInputSentenceLength",
    "DISPID_SVSInputSentencePosition",
    "DISPID_SVSInputWordLength",
    "DISPID_SVSInputWordPosition",
    "DISPID_SVSLastBookmark",
    "DISPID_SVSLastBookmarkId",
    "DISPID_SVSLastResult",
    "DISPID_SVSLastStreamNumberQueued",
    "DISPID_SVSPhonemeId",
    "DISPID_SVSRunningState",
    "DISPID_SVSVisemeId",
    "DISPID_SVSkip",
    "DISPID_SVSpeak",
    "DISPID_SVSpeakCompleteEvent",
    "DISPID_SVSpeakStream",
    "DISPID_SVStatus",
    "DISPID_SVSyncronousSpeakTimeout",
    "DISPID_SVVoice",
    "DISPID_SVVolume",
    "DISPID_SVWaitUntilDone",
    "DISPID_SWFEAvgBytesPerSec",
    "DISPID_SWFEBitsPerSample",
    "DISPID_SWFEBlockAlign",
    "DISPID_SWFEChannels",
    "DISPID_SWFEExtraData",
    "DISPID_SWFEFormatTag",
    "DISPID_SWFESamplesPerSec",
    "DISPID_SpeechAudio",
    "DISPID_SpeechAudioBufferInfo",
    "DISPID_SpeechAudioFormat",
    "DISPID_SpeechAudioStatus",
    "DISPID_SpeechBaseStream",
    "DISPID_SpeechCustomStream",
    "DISPID_SpeechDataKey",
    "DISPID_SpeechFileStream",
    "DISPID_SpeechGrammarRule",
    "DISPID_SpeechGrammarRuleState",
    "DISPID_SpeechGrammarRuleStateTransition",
    "DISPID_SpeechGrammarRuleStateTransitions",
    "DISPID_SpeechGrammarRules",
    "DISPID_SpeechLexicon",
    "DISPID_SpeechLexiconProns",
    "DISPID_SpeechLexiconPronunciation",
    "DISPID_SpeechLexiconWord",
    "DISPID_SpeechLexiconWords",
    "DISPID_SpeechMMSysAudio",
    "DISPID_SpeechMemoryStream",
    "DISPID_SpeechObjectToken",
    "DISPID_SpeechObjectTokenCategory",
    "DISPID_SpeechObjectTokens",
    "DISPID_SpeechPhoneConverter",
    "DISPID_SpeechPhraseAlternate",
    "DISPID_SpeechPhraseAlternates",
    "DISPID_SpeechPhraseBuilder",
    "DISPID_SpeechPhraseElement",
    "DISPID_SpeechPhraseElements",
    "DISPID_SpeechPhraseInfo",
    "DISPID_SpeechPhraseProperties",
    "DISPID_SpeechPhraseProperty",
    "DISPID_SpeechPhraseReplacement",
    "DISPID_SpeechPhraseReplacements",
    "DISPID_SpeechPhraseRule",
    "DISPID_SpeechPhraseRules",
    "DISPID_SpeechRecoContext",
    "DISPID_SpeechRecoContextEvents",
    "DISPID_SpeechRecoResult",
    "DISPID_SpeechRecoResult2",
    "DISPID_SpeechRecoResultTimes",
    "DISPID_SpeechRecognizer",
    "DISPID_SpeechRecognizerStatus",
    "DISPID_SpeechVoice",
    "DISPID_SpeechVoiceEvent",
    "DISPID_SpeechVoiceStatus",
    "DISPID_SpeechWaveFormatEx",
    "DISPID_SpeechXMLRecoResult",
    "IEnumSpObjectTokens",
    "ISpAudio",
    "ISpContainerLexicon",
    "ISpDataKey",
    "ISpDisplayAlternates",
    "ISpEnginePronunciation",
    "ISpEventSink",
    "ISpEventSource",
    "ISpEventSource2",
    "ISpGrammarBuilder",
    "ISpGrammarBuilder2",
    "ISpLexicon",
    "ISpMMSysAudio",
    "ISpNotifyCallback",
    "ISpNotifySink",
    "ISpNotifySource",
    "ISpNotifyTranslator",
    "ISpObjectToken",
    "ISpObjectTokenCategory",
    "ISpObjectTokenInit",
    "ISpObjectWithToken",
    "ISpPhoneConverter",
    "ISpPhoneticAlphabetConverter",
    "ISpPhoneticAlphabetSelection",
    "ISpPhrase",
    "ISpPhrase2",
    "ISpPhraseAlt",
    "ISpProperties",
    "ISpRecoContext",
    "ISpRecoContext2",
    "ISpRecoGrammar",
    "ISpRecoGrammar2",
    "ISpRecoResult",
    "ISpRecoResult2",
    "ISpRecognizer",
    "ISpRecognizer2",
    "ISpRegDataKey",
    "ISpResourceManager",
    "ISpSerializeState",
    "ISpShortcut",
    "ISpStream",
    "ISpStreamFormat",
    "ISpStreamFormatConverter",
    "ISpTranscript",
    "ISpVoice",
    "ISpXMLRecoResult",
    "ISpeechAudio",
    "ISpeechAudioBufferInfo",
    "ISpeechAudioFormat",
    "ISpeechAudioStatus",
    "ISpeechBaseStream",
    "ISpeechCustomStream",
    "ISpeechDataKey",
    "ISpeechFileStream",
    "ISpeechGrammarRule",
    "ISpeechGrammarRuleState",
    "ISpeechGrammarRuleStateTransition",
    "ISpeechGrammarRuleStateTransitions",
    "ISpeechGrammarRules",
    "ISpeechLexicon",
    "ISpeechLexiconPronunciation",
    "ISpeechLexiconPronunciations",
    "ISpeechLexiconWord",
    "ISpeechLexiconWords",
    "ISpeechMMSysAudio",
    "ISpeechMemoryStream",
    "ISpeechObjectToken",
    "ISpeechObjectTokenCategory",
    "ISpeechObjectTokens",
    "ISpeechPhoneConverter",
    "ISpeechPhraseAlternate",
    "ISpeechPhraseAlternates",
    "ISpeechPhraseElement",
    "ISpeechPhraseElements",
    "ISpeechPhraseInfo",
    "ISpeechPhraseInfoBuilder",
    "ISpeechPhraseProperties",
    "ISpeechPhraseProperty",
    "ISpeechPhraseReplacement",
    "ISpeechPhraseReplacements",
    "ISpeechPhraseRule",
    "ISpeechPhraseRules",
    "ISpeechRecoContext",
    "ISpeechRecoGrammar",
    "ISpeechRecoResult",
    "ISpeechRecoResult2",
    "ISpeechRecoResultDispatch",
    "ISpeechRecoResultTimes",
    "ISpeechRecognizer",
    "ISpeechRecognizerStatus",
    "ISpeechResourceLoader",
    "ISpeechTextSelectionInformation",
    "ISpeechVoice",
    "ISpeechVoiceStatus",
    "ISpeechWaveFormatEx",
    "ISpeechXMLRecoResult",
    "PA_Ipa",
    "PA_Sapi",
    "PA_Ups",
    "PHONETICALPHABET",
    "SAPI_ERROR_BASE",
    "SDA_Consume_Leading_Spaces",
    "SDA_No_Trailing_Space",
    "SDA_One_Trailing_Space",
    "SDA_Two_Trailing_Spaces",
    "SPADAPTATIONRELEVANCE",
    "SPADAPTATIONSETTINGS",
    "SPADS_CurrentRecognizer",
    "SPADS_Default",
    "SPADS_HighVolumeDataSource",
    "SPADS_Immediate",
    "SPADS_RecoProfile",
    "SPADS_Reset",
    "SPAF_ALL",
    "SPAF_BUFFER_POSITION",
    "SPAF_CONSUME_LEADING_SPACES",
    "SPAF_ONE_TRAILING_SPACE",
    "SPAF_TWO_TRAILING_SPACES",
    "SPAF_USER_SPECIFIED",
    "SPALTERNATESCLSID",
    "SPAO_NONE",
    "SPAO_RETAIN_AUDIO",
    "SPAR_High",
    "SPAR_Low",
    "SPAR_Medium",
    "SPAR_Unknown",
    "SPAS_CLOSED",
    "SPAS_PAUSE",
    "SPAS_RUN",
    "SPAS_STOP",
    "SPAUDIOBUFFERINFO",
    "SPAUDIOOPTIONS",
    "SPAUDIOSTATE",
    "SPAUDIOSTATUS",
    "SPBINARYGRAMMAR",
    "SPBOOKMARKOPTIONS",
    "SPBO_AHEAD",
    "SPBO_NONE",
    "SPBO_PAUSE",
    "SPBO_TIME_UNITS",
    "SPCAT_APPLEXICONS",
    "SPCAT_AUDIOIN",
    "SPCAT_AUDIOOUT",
    "SPCAT_PHONECONVERTERS",
    "SPCAT_RECOGNIZERS",
    "SPCAT_RECOPROFILES",
    "SPCAT_TEXTNORMALIZERS",
    "SPCAT_VOICES",
    "SPCFGRULEATTRIBUTES",
    "SPCF_ADD_TO_USER_LEXICON",
    "SPCF_DEFINITE_CORRECTION",
    "SPCF_NONE",
    "SPCOMMITFLAGS",
    "SPCONTEXTSTATE",
    "SPCS_DISABLED",
    "SPCS_ENABLED",
    "SPCURRENT_USER_LEXICON_TOKEN_ID",
    "SPCURRENT_USER_SHORTCUT_TOKEN_ID",
    "SPDATAKEYLOCATION",
    "SPDF_ALL",
    "SPDF_ALTERNATES",
    "SPDF_AUDIO",
    "SPDF_DISPLAYTEXT",
    "SPDF_LEXICALFORM",
    "SPDF_PRONUNCIATION",
    "SPDF_PROPERTY",
    "SPDF_REPLACEMENT",
    "SPDF_RULE",
    "SPDICTATION",
    "SPDISPLAYATTRIBUTES",
    "SPDISPLAYPHRASE",
    "SPDISPLAYTOKEN",
    "SPDKL_CurrentConfig",
    "SPDKL_CurrentUser",
    "SPDKL_DefaultLocation",
    "SPDKL_LocalMachine",
    "SPDUI_AddRemoveWord",
    "SPDUI_AudioProperties",
    "SPDUI_AudioVolume",
    "SPDUI_EngineProperties",
    "SPDUI_MicTraining",
    "SPDUI_RecoProfileProperties",
    "SPDUI_ShareData",
    "SPDUI_Tutorial",
    "SPDUI_UserEnrollment",
    "SPDUI_UserTraining",
    "SPEAKFLAGS",
    "SPEI_ADAPTATION",
    "SPEI_END_INPUT_STREAM",
    "SPEI_END_SR_STREAM",
    "SPEI_FALSE_RECOGNITION",
    "SPEI_HYPOTHESIS",
    "SPEI_INTERFERENCE",
    "SPEI_MAX_SR",
    "SPEI_MAX_TTS",
    "SPEI_MIN_SR",
    "SPEI_MIN_TTS",
    "SPEI_PHONEME",
    "SPEI_PHRASE_START",
    "SPEI_PROPERTY_NUM_CHANGE",
    "SPEI_PROPERTY_STRING_CHANGE",
    "SPEI_RECOGNITION",
    "SPEI_RECO_OTHER_CONTEXT",
    "SPEI_RECO_STATE_CHANGE",
    "SPEI_REQUEST_UI",
    "SPEI_RESERVED1",
    "SPEI_RESERVED2",
    "SPEI_RESERVED3",
    "SPEI_RESERVED4",
    "SPEI_RESERVED5",
    "SPEI_RESERVED6",
    "SPEI_SENTENCE_BOUNDARY",
    "SPEI_SOUND_END",
    "SPEI_SOUND_START",
    "SPEI_SR_AUDIO_LEVEL",
    "SPEI_SR_BOOKMARK",
    "SPEI_SR_PRIVATE",
    "SPEI_SR_RETAINEDAUDIO",
    "SPEI_START_INPUT_STREAM",
    "SPEI_START_SR_STREAM",
    "SPEI_TTS_AUDIO_LEVEL",
    "SPEI_TTS_BOOKMARK",
    "SPEI_TTS_PRIVATE",
    "SPEI_UNDEFINED",
    "SPEI_VISEME",
    "SPEI_VOICE_CHANGE",
    "SPEI_WORD_BOUNDARY",
    "SPENDSRSTREAMFLAGS",
    "SPESF_EMULATED",
    "SPESF_NONE",
    "SPESF_STREAM_RELEASED",
    "SPET_LPARAM_IS_OBJECT",
    "SPET_LPARAM_IS_POINTER",
    "SPET_LPARAM_IS_STRING",
    "SPET_LPARAM_IS_TOKEN",
    "SPET_LPARAM_IS_UNDEFINED",
    "SPEVENT",
    "SPEVENTENUM",
    "SPEVENTEX",
    "SPEVENTLPARAMTYPE",
    "SPEVENTSOURCEINFO",
    "SPFILEMODE",
    "SPFM_CREATE",
    "SPFM_CREATE_ALWAYS",
    "SPFM_NUM_MODES",
    "SPFM_OPEN_READONLY",
    "SPFM_OPEN_READWRITE",
    "SPF_ASYNC",
    "SPF_DEFAULT",
    "SPF_IS_FILENAME",
    "SPF_IS_NOT_XML",
    "SPF_IS_XML",
    "SPF_NLP_MASK",
    "SPF_NLP_SPEAK_PUNC",
    "SPF_PARSE_AUTODETECT",
    "SPF_PARSE_MASK",
    "SPF_PARSE_SAPI",
    "SPF_PARSE_SSML",
    "SPF_PERSIST_XML",
    "SPF_PURGEBEFORESPEAK",
    "SPF_UNUSED_FLAGS",
    "SPF_VOICE_MASK",
    "SPGO_ALL",
    "SPGO_DEFAULT",
    "SPGO_FILE",
    "SPGO_HTTP",
    "SPGO_OBJECT",
    "SPGO_RES",
    "SPGO_SAPI",
    "SPGO_SRGS",
    "SPGO_SRGS_MS_SCRIPT",
    "SPGO_SRGS_SCRIPT",
    "SPGO_SRGS_STG_SCRIPT",
    "SPGO_SRGS_W3C_SCRIPT",
    "SPGO_UPS",
    "SPGRAMMAROPTIONS",
    "SPGRAMMARSTATE",
    "SPGRAMMARWORDTYPE",
    "SPGS_DISABLED",
    "SPGS_ENABLED",
    "SPGS_EXCLUSIVE",
    "SPINFDICTATION",
    "SPINTERFERENCE",
    "SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN",
    "SPINTERFERENCE_LATENCY_TRUNCATE_END",
    "SPINTERFERENCE_LATENCY_WARNING",
    "SPINTERFERENCE_NOISE",
    "SPINTERFERENCE_NONE",
    "SPINTERFERENCE_NOSIGNAL",
    "SPINTERFERENCE_TOOFAST",
    "SPINTERFERENCE_TOOLOUD",
    "SPINTERFERENCE_TOOQUIET",
    "SPINTERFERENCE_TOOSLOW",
    "SPLEXICONTYPE",
    "SPLOADOPTIONS",
    "SPLO_DYNAMIC",
    "SPLO_STATIC",
    "SPMATCHINGMODE",
    "SPMATCHINGMODE_AllWords",
    "SPMATCHINGMODE_OrderedSubset",
    "SPMATCHINGMODE_OrderedSubsetContentRequired",
    "SPMATCHINGMODE_Subsequence",
    "SPMATCHINGMODE_SubsequenceContentRequired",
    "SPMAX_RATE",
    "SPMAX_VOLUME",
    "SPMIN_RATE",
    "SPMIN_VOLUME",
    "SPMMSYS_AUDIO_IN_TOKEN_ID",
    "SPMMSYS_AUDIO_OUT_TOKEN_ID",
    "SPNORMALIZATIONLIST",
    "SPNOTIFYCALLBACK",
    "SPPARTOFSPEECH",
    "SPPHRASE",
    "SPPHRASEELEMENT",
    "SPPHRASEPROPERTY",
    "SPPHRASEPROPERTYUNIONTYPE",
    "SPPHRASEREPLACEMENT",
    "SPPHRASERNG",
    "SPPHRASERULE",
    "SPPHRASE_50",
    "SPPPUT_ARRAY_INDEX",
    "SPPPUT_UNUSED",
    "SPPRONUNCIATIONFLAGS",
    "SPPROPERTYINFO",
    "SPPROP_ADAPTATION_ON",
    "SPPROP_COMPLEX_RESPONSE_SPEED",
    "SPPROP_HIGH_CONFIDENCE_THRESHOLD",
    "SPPROP_LOW_CONFIDENCE_THRESHOLD",
    "SPPROP_NORMAL_CONFIDENCE_THRESHOLD",
    "SPPROP_PERSISTED_BACKGROUND_ADAPTATION",
    "SPPROP_PERSISTED_LANGUAGE_MODEL_ADAPTATION",
    "SPPROP_RESOURCE_USAGE",
    "SPPROP_RESPONSE_SPEED",
    "SPPROP_UX_IS_LISTENING",
    "SPPR_ALL_ELEMENTS",
    "SPPS_Function",
    "SPPS_Interjection",
    "SPPS_LMA",
    "SPPS_Modifier",
    "SPPS_Noncontent",
    "SPPS_NotOverriden",
    "SPPS_Noun",
    "SPPS_RESERVED1",
    "SPPS_RESERVED2",
    "SPPS_RESERVED3",
    "SPPS_RESERVED4",
    "SPPS_SuppressWord",
    "SPPS_Unknown",
    "SPPS_Verb",
    "SPRAF_Active",
    "SPRAF_AutoPause",
    "SPRAF_Dynamic",
    "SPRAF_Export",
    "SPRAF_Import",
    "SPRAF_Interpreter",
    "SPRAF_Root",
    "SPRAF_TopLevel",
    "SPRAF_UserDelimited",
    "SPRECOCONTEXTSTATUS",
    "SPRECOEVENTFLAGS",
    "SPRECOEXTENSION",
    "SPRECOGNIZERSTATUS",
    "SPRECORESULTTIMES",
    "SPRECOSTATE",
    "SPREF_AutoPause",
    "SPREF_Emulated",
    "SPREF_ExtendableParse",
    "SPREF_FalseRecognition",
    "SPREF_Hypothesis",
    "SPREF_ReSent",
    "SPREF_SMLTimeout",
    "SPREG_LOCAL_MACHINE_ROOT",
    "SPREG_SAFE_USER_TOKENS",
    "SPREG_USER_ROOT",
    "SPRP_NORMAL",
    "SPRST_ACTIVE",
    "SPRST_ACTIVE_ALWAYS",
    "SPRST_INACTIVE",
    "SPRST_INACTIVE_WITH_PURGE",
    "SPRST_NUM_STATES",
    "SPRS_ACTIVE",
    "SPRS_ACTIVE_USER_DELIMITED",
    "SPRS_ACTIVE_WITH_AUTO_PAUSE",
    "SPRS_DONE",
    "SPRS_INACTIVE",
    "SPRS_IS_SPEAKING",
    "SPRULE",
    "SPRULESTATE",
    "SPRUNSTATE",
    "SPSEMANTICERRORINFO",
    "SPSEMANTICFORMAT",
    "SPSERIALIZEDEVENT",
    "SPSERIALIZEDEVENT64",
    "SPSERIALIZEDPHRASE",
    "SPSERIALIZEDRESULT",
    "SPSF_11kHz16BitMono",
    "SPSF_11kHz16BitStereo",
    "SPSF_11kHz8BitMono",
    "SPSF_11kHz8BitStereo",
    "SPSF_12kHz16BitMono",
    "SPSF_12kHz16BitStereo",
    "SPSF_12kHz8BitMono",
    "SPSF_12kHz8BitStereo",
    "SPSF_16kHz16BitMono",
    "SPSF_16kHz16BitStereo",
    "SPSF_16kHz8BitMono",
    "SPSF_16kHz8BitStereo",
    "SPSF_22kHz16BitMono",
    "SPSF_22kHz16BitStereo",
    "SPSF_22kHz8BitMono",
    "SPSF_22kHz8BitStereo",
    "SPSF_24kHz16BitMono",
    "SPSF_24kHz16BitStereo",
    "SPSF_24kHz8BitMono",
    "SPSF_24kHz8BitStereo",
    "SPSF_32kHz16BitMono",
    "SPSF_32kHz16BitStereo",
    "SPSF_32kHz8BitMono",
    "SPSF_32kHz8BitStereo",
    "SPSF_44kHz16BitMono",
    "SPSF_44kHz16BitStereo",
    "SPSF_44kHz8BitMono",
    "SPSF_44kHz8BitStereo",
    "SPSF_48kHz16BitMono",
    "SPSF_48kHz16BitStereo",
    "SPSF_48kHz8BitMono",
    "SPSF_48kHz8BitStereo",
    "SPSF_8kHz16BitMono",
    "SPSF_8kHz16BitStereo",
    "SPSF_8kHz8BitMono",
    "SPSF_8kHz8BitStereo",
    "SPSF_ADPCM_11kHzMono",
    "SPSF_ADPCM_11kHzStereo",
    "SPSF_ADPCM_22kHzMono",
    "SPSF_ADPCM_22kHzStereo",
    "SPSF_ADPCM_44kHzMono",
    "SPSF_ADPCM_44kHzStereo",
    "SPSF_ADPCM_8kHzMono",
    "SPSF_ADPCM_8kHzStereo",
    "SPSF_CCITT_ALaw_11kHzMono",
    "SPSF_CCITT_ALaw_11kHzStereo",
    "SPSF_CCITT_ALaw_22kHzMono",
    "SPSF_CCITT_ALaw_22kHzStereo",
    "SPSF_CCITT_ALaw_44kHzMono",
    "SPSF_CCITT_ALaw_44kHzStereo",
    "SPSF_CCITT_ALaw_8kHzMono",
    "SPSF_CCITT_ALaw_8kHzStereo",
    "SPSF_CCITT_uLaw_11kHzMono",
    "SPSF_CCITT_uLaw_11kHzStereo",
    "SPSF_CCITT_uLaw_22kHzMono",
    "SPSF_CCITT_uLaw_22kHzStereo",
    "SPSF_CCITT_uLaw_44kHzMono",
    "SPSF_CCITT_uLaw_44kHzStereo",
    "SPSF_CCITT_uLaw_8kHzMono",
    "SPSF_CCITT_uLaw_8kHzStereo",
    "SPSF_Default",
    "SPSF_ExtendedAudioFormat",
    "SPSF_GSM610_11kHzMono",
    "SPSF_GSM610_22kHzMono",
    "SPSF_GSM610_44kHzMono",
    "SPSF_GSM610_8kHzMono",
    "SPSF_NUM_FORMATS",
    "SPSF_NoAssignedFormat",
    "SPSF_NonStandardFormat",
    "SPSF_Text",
    "SPSF_TrueSpeech_8kHz1BitMono",
    "SPSHORTCUTPAIR",
    "SPSHORTCUTPAIRLIST",
    "SPSHORTCUTTYPE",
    "SPSHT_EMAIL",
    "SPSHT_NotOverriden",
    "SPSHT_OTHER",
    "SPSHT_Unknown",
    "SPSMF_SAPI_PROPERTIES",
    "SPSMF_SRGS_SAPIPROPERTIES",
    "SPSMF_SRGS_SEMANTICINTERPRETATION_MS",
    "SPSMF_SRGS_SEMANTICINTERPRETATION_W3C",
    "SPSMF_UPS",
    "SPSTATEHANDLE__",
    "SPSTREAMFORMAT",
    "SPSTREAMFORMATTYPE",
    "SPTEXTSELECTIONINFO",
    "SPTOKENKEY_ATTRIBUTES",
    "SPTOKENKEY_AUDIO_LATENCY_TRUNCATE",
    "SPTOKENKEY_AUDIO_LATENCY_UPDATE_INTERVAL",
    "SPTOKENKEY_AUDIO_LATENCY_WARNING",
    "SPTOKENKEY_FILES",
    "SPTOKENKEY_RETAINEDAUDIO",
    "SPTOKENKEY_UI",
    "SPTOKENVALUE_CLSID",
    "SPTOPIC_SPELLING",
    "SPVACTIONS",
    "SPVALUETYPE",
    "SPVA_Bookmark",
    "SPVA_ParseUnknownTag",
    "SPVA_Pronounce",
    "SPVA_Section",
    "SPVA_Silence",
    "SPVA_Speak",
    "SPVA_SpellOut",
    "SPVCONTEXT",
    "SPVFEATURE",
    "SPVFEATURE_EMPHASIS",
    "SPVFEATURE_STRESSED",
    "SPVISEMES",
    "SPVLIMITS",
    "SPVOICECATEGORY_TTSRATE",
    "SPVOICESTATUS",
    "SPVPITCH",
    "SPVPRIORITY",
    "SPVPRI_ALERT",
    "SPVPRI_NORMAL",
    "SPVPRI_OVER",
    "SPVSTATE",
    "SPWF_INPUT",
    "SPWF_SRENGINE",
    "SPWILDCARD",
    "SPWORD",
    "SPWORDLIST",
    "SPWORDPRONOUNCEABLE",
    "SPWORDPRONUNCIATION",
    "SPWORDPRONUNCIATIONLIST",
    "SPWORDTYPE",
    "SPWP_KNOWN_WORD_PRONOUNCEABLE",
    "SPWP_UNKNOWN_WORD_PRONOUNCEABLE",
    "SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE",
    "SPWT_DISPLAY",
    "SPWT_LEXICAL",
    "SPWT_LEXICAL_NO_SPECIAL_CHARS",
    "SPWT_PRONUNCIATION",
    "SPXMLRESULTOPTIONS",
    "SPXRO_Alternates_SML",
    "SPXRO_SML",
    "SP_EMULATE_RESULT",
    "SP_LOW_CONFIDENCE",
    "SP_MAX_LANGIDS",
    "SP_MAX_PRON_LENGTH",
    "SP_MAX_WORD_LENGTH",
    "SP_NORMAL_CONFIDENCE",
    "SP_STREAMPOS_ASAP",
    "SP_STREAMPOS_REALTIME",
    "SP_VISEME_0",
    "SP_VISEME_1",
    "SP_VISEME_10",
    "SP_VISEME_11",
    "SP_VISEME_12",
    "SP_VISEME_13",
    "SP_VISEME_14",
    "SP_VISEME_15",
    "SP_VISEME_16",
    "SP_VISEME_17",
    "SP_VISEME_18",
    "SP_VISEME_19",
    "SP_VISEME_2",
    "SP_VISEME_20",
    "SP_VISEME_21",
    "SP_VISEME_3",
    "SP_VISEME_4",
    "SP_VISEME_5",
    "SP_VISEME_6",
    "SP_VISEME_7",
    "SP_VISEME_8",
    "SP_VISEME_9",
    "SRCS_Disabled",
    "SRCS_Enabled",
    "SR_LOCALIZED_DESCRIPTION",
    "STSF_AppData",
    "STSF_CommonAppData",
    "STSF_FlagCreate",
    "STSF_LocalAppData",
    "SVF_Emphasis",
    "SVF_None",
    "SVF_Stressed",
    "SVP_0",
    "SVP_1",
    "SVP_10",
    "SVP_11",
    "SVP_12",
    "SVP_13",
    "SVP_14",
    "SVP_15",
    "SVP_16",
    "SVP_17",
    "SVP_18",
    "SVP_19",
    "SVP_2",
    "SVP_20",
    "SVP_21",
    "SVP_3",
    "SVP_4",
    "SVP_5",
    "SVP_6",
    "SVP_7",
    "SVP_8",
    "SVP_9",
    "SpAudioFormat",
    "SpCompressedLexicon",
    "SpCustomStream",
    "SpFileStream",
    "SpInProcRecoContext",
    "SpInprocRecognizer",
    "SpLexicon",
    "SpMMAudioEnum",
    "SpMMAudioIn",
    "SpMMAudioOut",
    "SpMemoryStream",
    "SpNotifyTranslator",
    "SpNullPhoneConverter",
    "SpObjectToken",
    "SpObjectTokenCategory",
    "SpPhoneConverter",
    "SpPhoneticAlphabetConverter",
    "SpPhraseInfoBuilder",
    "SpResourceManager",
    "SpSharedRecoContext",
    "SpSharedRecognizer",
    "SpShortcut",
    "SpStream",
    "SpStreamFormatConverter",
    "SpTextSelectionInformation",
    "SpUnCompressedLexicon",
    "SpVoice",
    "SpWaveFormatEx",
    "SpeechAllElements",
    "SpeechAudioFormatType",
    "SpeechAudioFormatType_SAFT11kHz16BitMono",
    "SpeechAudioFormatType_SAFT11kHz16BitStereo",
    "SpeechAudioFormatType_SAFT11kHz8BitMono",
    "SpeechAudioFormatType_SAFT11kHz8BitStereo",
    "SpeechAudioFormatType_SAFT12kHz16BitMono",
    "SpeechAudioFormatType_SAFT12kHz16BitStereo",
    "SpeechAudioFormatType_SAFT12kHz8BitMono",
    "SpeechAudioFormatType_SAFT12kHz8BitStereo",
    "SpeechAudioFormatType_SAFT16kHz16BitMono",
    "SpeechAudioFormatType_SAFT16kHz16BitStereo",
    "SpeechAudioFormatType_SAFT16kHz8BitMono",
    "SpeechAudioFormatType_SAFT16kHz8BitStereo",
    "SpeechAudioFormatType_SAFT22kHz16BitMono",
    "SpeechAudioFormatType_SAFT22kHz16BitStereo",
    "SpeechAudioFormatType_SAFT22kHz8BitMono",
    "SpeechAudioFormatType_SAFT22kHz8BitStereo",
    "SpeechAudioFormatType_SAFT24kHz16BitMono",
    "SpeechAudioFormatType_SAFT24kHz16BitStereo",
    "SpeechAudioFormatType_SAFT24kHz8BitMono",
    "SpeechAudioFormatType_SAFT24kHz8BitStereo",
    "SpeechAudioFormatType_SAFT32kHz16BitMono",
    "SpeechAudioFormatType_SAFT32kHz16BitStereo",
    "SpeechAudioFormatType_SAFT32kHz8BitMono",
    "SpeechAudioFormatType_SAFT32kHz8BitStereo",
    "SpeechAudioFormatType_SAFT44kHz16BitMono",
    "SpeechAudioFormatType_SAFT44kHz16BitStereo",
    "SpeechAudioFormatType_SAFT44kHz8BitMono",
    "SpeechAudioFormatType_SAFT44kHz8BitStereo",
    "SpeechAudioFormatType_SAFT48kHz16BitMono",
    "SpeechAudioFormatType_SAFT48kHz16BitStereo",
    "SpeechAudioFormatType_SAFT48kHz8BitMono",
    "SpeechAudioFormatType_SAFT48kHz8BitStereo",
    "SpeechAudioFormatType_SAFT8kHz16BitMono",
    "SpeechAudioFormatType_SAFT8kHz16BitStereo",
    "SpeechAudioFormatType_SAFT8kHz8BitMono",
    "SpeechAudioFormatType_SAFT8kHz8BitStereo",
    "SpeechAudioFormatType_SAFTADPCM_11kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_11kHzStereo",
    "SpeechAudioFormatType_SAFTADPCM_22kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_22kHzStereo",
    "SpeechAudioFormatType_SAFTADPCM_44kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_44kHzStereo",
    "SpeechAudioFormatType_SAFTADPCM_8kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_8kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzStereo",
    "SpeechAudioFormatType_SAFTDefault",
    "SpeechAudioFormatType_SAFTExtendedAudioFormat",
    "SpeechAudioFormatType_SAFTGSM610_11kHzMono",
    "SpeechAudioFormatType_SAFTGSM610_22kHzMono",
    "SpeechAudioFormatType_SAFTGSM610_44kHzMono",
    "SpeechAudioFormatType_SAFTGSM610_8kHzMono",
    "SpeechAudioFormatType_SAFTNoAssignedFormat",
    "SpeechAudioFormatType_SAFTNonStandardFormat",
    "SpeechAudioFormatType_SAFTText",
    "SpeechAudioFormatType_SAFTTrueSpeech_8kHz1BitMono",
    "SpeechAudioState",
    "SpeechAudioState_SASClosed",
    "SpeechAudioState_SASPause",
    "SpeechAudioState_SASRun",
    "SpeechAudioState_SASStop",
    "SpeechBookmarkOptions",
    "SpeechBookmarkOptions_SBONone",
    "SpeechBookmarkOptions_SBOPause",
    "SpeechDataKeyLocation",
    "SpeechDataKeyLocation_SDKLCurrentConfig",
    "SpeechDataKeyLocation_SDKLCurrentUser",
    "SpeechDataKeyLocation_SDKLDefaultLocation",
    "SpeechDataKeyLocation_SDKLLocalMachine",
    "SpeechDiscardType",
    "SpeechDiscardType_SDTAll",
    "SpeechDiscardType_SDTAlternates",
    "SpeechDiscardType_SDTAudio",
    "SpeechDiscardType_SDTDisplayText",
    "SpeechDiscardType_SDTLexicalForm",
    "SpeechDiscardType_SDTPronunciation",
    "SpeechDiscardType_SDTProperty",
    "SpeechDiscardType_SDTReplacement",
    "SpeechDiscardType_SDTRule",
    "SpeechDisplayAttributes",
    "SpeechEmulationCompareFlags",
    "SpeechEmulationCompareFlags_SECFDefault",
    "SpeechEmulationCompareFlags_SECFEmulateResult",
    "SpeechEmulationCompareFlags_SECFIgnoreCase",
    "SpeechEmulationCompareFlags_SECFIgnoreKanaType",
    "SpeechEmulationCompareFlags_SECFIgnoreWidth",
    "SpeechEmulationCompareFlags_SECFNoSpecialChars",
    "SpeechEngineConfidence",
    "SpeechEngineConfidence_SECHighConfidence",
    "SpeechEngineConfidence_SECLowConfidence",
    "SpeechEngineConfidence_SECNormalConfidence",
    "SpeechFormatType",
    "SpeechFormatType_SFTInput",
    "SpeechFormatType_SFTSREngine",
    "SpeechGrammarRuleStateTransitionType",
    "SpeechGrammarRuleStateTransitionType_SGRSTTDictation",
    "SpeechGrammarRuleStateTransitionType_SGRSTTEpsilon",
    "SpeechGrammarRuleStateTransitionType_SGRSTTRule",
    "SpeechGrammarRuleStateTransitionType_SGRSTTTextBuffer",
    "SpeechGrammarRuleStateTransitionType_SGRSTTWildcard",
    "SpeechGrammarRuleStateTransitionType_SGRSTTWord",
    "SpeechGrammarState",
    "SpeechGrammarState_SGSDisabled",
    "SpeechGrammarState_SGSEnabled",
    "SpeechGrammarState_SGSExclusive",
    "SpeechGrammarWordType",
    "SpeechGrammarWordType_SGDisplay",
    "SpeechGrammarWordType_SGLexical",
    "SpeechGrammarWordType_SGLexicalNoSpecialChars",
    "SpeechGrammarWordType_SGPronounciation",
    "SpeechInterference",
    "SpeechInterference_SINoSignal",
    "SpeechInterference_SINoise",
    "SpeechInterference_SINone",
    "SpeechInterference_SITooFast",
    "SpeechInterference_SITooLoud",
    "SpeechInterference_SITooQuiet",
    "SpeechInterference_SITooSlow",
    "SpeechLexiconType",
    "SpeechLexiconType_SLTApp",
    "SpeechLexiconType_SLTUser",
    "SpeechLoadOption",
    "SpeechLoadOption_SLODynamic",
    "SpeechLoadOption_SLOStatic",
    "SpeechPartOfSpeech",
    "SpeechPartOfSpeech_SPSFunction",
    "SpeechPartOfSpeech_SPSInterjection",
    "SpeechPartOfSpeech_SPSLMA",
    "SpeechPartOfSpeech_SPSModifier",
    "SpeechPartOfSpeech_SPSNotOverriden",
    "SpeechPartOfSpeech_SPSNoun",
    "SpeechPartOfSpeech_SPSSuppressWord",
    "SpeechPartOfSpeech_SPSUnknown",
    "SpeechPartOfSpeech_SPSVerb",
    "SpeechRecoContextState",
    "SpeechRecoEvents",
    "SpeechRecoEvents_SREAdaptation",
    "SpeechRecoEvents_SREAllEvents",
    "SpeechRecoEvents_SREAudioLevel",
    "SpeechRecoEvents_SREBookmark",
    "SpeechRecoEvents_SREFalseRecognition",
    "SpeechRecoEvents_SREHypothesis",
    "SpeechRecoEvents_SREInterference",
    "SpeechRecoEvents_SREPhraseStart",
    "SpeechRecoEvents_SREPrivate",
    "SpeechRecoEvents_SREPropertyNumChange",
    "SpeechRecoEvents_SREPropertyStringChange",
    "SpeechRecoEvents_SRERecoOtherContext",
    "SpeechRecoEvents_SRERecognition",
    "SpeechRecoEvents_SRERequestUI",
    "SpeechRecoEvents_SRESoundEnd",
    "SpeechRecoEvents_SRESoundStart",
    "SpeechRecoEvents_SREStateChange",
    "SpeechRecoEvents_SREStreamEnd",
    "SpeechRecoEvents_SREStreamStart",
    "SpeechRecognitionType",
    "SpeechRecognitionType_SRTAutopause",
    "SpeechRecognitionType_SRTEmulated",
    "SpeechRecognitionType_SRTExtendableParse",
    "SpeechRecognitionType_SRTReSent",
    "SpeechRecognitionType_SRTSMLTimeout",
    "SpeechRecognitionType_SRTStandard",
    "SpeechRecognizerState",
    "SpeechRecognizerState_SRSActive",
    "SpeechRecognizerState_SRSActiveAlways",
    "SpeechRecognizerState_SRSInactive",
    "SpeechRecognizerState_SRSInactiveWithPurge",
    "SpeechRetainedAudioOptions",
    "SpeechRetainedAudioOptions_SRAONone",
    "SpeechRetainedAudioOptions_SRAORetainAudio",
    "SpeechRuleAttributes",
    "SpeechRuleAttributes_SRADefaultToActive",
    "SpeechRuleAttributes_SRADynamic",
    "SpeechRuleAttributes_SRAExport",
    "SpeechRuleAttributes_SRAImport",
    "SpeechRuleAttributes_SRAInterpreter",
    "SpeechRuleAttributes_SRARoot",
    "SpeechRuleAttributes_SRATopLevel",
    "SpeechRuleState",
    "SpeechRuleState_SGDSActive",
    "SpeechRuleState_SGDSActiveUserDelimited",
    "SpeechRuleState_SGDSActiveWithAutoPause",
    "SpeechRuleState_SGDSInactive",
    "SpeechRunState",
    "SpeechRunState_SRSEDone",
    "SpeechRunState_SRSEIsSpeaking",
    "SpeechSpecialTransitionType",
    "SpeechSpecialTransitionType_SSTTDictation",
    "SpeechSpecialTransitionType_SSTTTextBuffer",
    "SpeechSpecialTransitionType_SSTTWildcard",
    "SpeechStreamFileMode",
    "SpeechStreamFileMode_SSFMCreate",
    "SpeechStreamFileMode_SSFMCreateForWrite",
    "SpeechStreamFileMode_SSFMOpenForRead",
    "SpeechStreamFileMode_SSFMOpenReadWrite",
    "SpeechStreamSeekPositionType",
    "SpeechStreamSeekPositionType_SSSPTRelativeToCurrentPosition",
    "SpeechStreamSeekPositionType_SSSPTRelativeToEnd",
    "SpeechStreamSeekPositionType_SSSPTRelativeToStart",
    "SpeechTokenContext",
    "SpeechTokenContext_STCAll",
    "SpeechTokenContext_STCInprocHandler",
    "SpeechTokenContext_STCInprocServer",
    "SpeechTokenContext_STCLocalServer",
    "SpeechTokenContext_STCRemoteServer",
    "SpeechTokenShellFolder",
    "SpeechVisemeFeature",
    "SpeechVisemeType",
    "SpeechVoiceEvents",
    "SpeechVoiceEvents_SVEAllEvents",
    "SpeechVoiceEvents_SVEAudioLevel",
    "SpeechVoiceEvents_SVEBookmark",
    "SpeechVoiceEvents_SVEEndInputStream",
    "SpeechVoiceEvents_SVEPhoneme",
    "SpeechVoiceEvents_SVEPrivate",
    "SpeechVoiceEvents_SVESentenceBoundary",
    "SpeechVoiceEvents_SVEStartInputStream",
    "SpeechVoiceEvents_SVEViseme",
    "SpeechVoiceEvents_SVEVoiceChange",
    "SpeechVoiceEvents_SVEWordBoundary",
    "SpeechVoicePriority",
    "SpeechVoicePriority_SVPAlert",
    "SpeechVoicePriority_SVPNormal",
    "SpeechVoicePriority_SVPOver",
    "SpeechVoiceSpeakFlags",
    "SpeechVoiceSpeakFlags_SVSFDefault",
    "SpeechVoiceSpeakFlags_SVSFIsFilename",
    "SpeechVoiceSpeakFlags_SVSFIsNotXML",
    "SpeechVoiceSpeakFlags_SVSFIsXML",
    "SpeechVoiceSpeakFlags_SVSFNLPMask",
    "SpeechVoiceSpeakFlags_SVSFNLPSpeakPunc",
    "SpeechVoiceSpeakFlags_SVSFParseAutodetect",
    "SpeechVoiceSpeakFlags_SVSFParseMask",
    "SpeechVoiceSpeakFlags_SVSFParseSapi",
    "SpeechVoiceSpeakFlags_SVSFParseSsml",
    "SpeechVoiceSpeakFlags_SVSFPersistXML",
    "SpeechVoiceSpeakFlags_SVSFPurgeBeforeSpeak",
    "SpeechVoiceSpeakFlags_SVSFUnusedFlags",
    "SpeechVoiceSpeakFlags_SVSFVoiceMask",
    "SpeechVoiceSpeakFlags_SVSFlagsAsync",
    "SpeechWordPronounceable",
    "SpeechWordPronounceable_SWPKnownWordPronounceable",
    "SpeechWordPronounceable_SWPUnknownWordPronounceable",
    "SpeechWordPronounceable_SWPUnknownWordUnpronounceable",
    "SpeechWordType",
    "SpeechWordType_SWTAdded",
    "SpeechWordType_SWTDeleted",
    "Speech_Default_Weight",
    "Speech_Max_Pron_Length",
    "Speech_Max_Word_Length",
    "Speech_StreamPos_Asap",
    "Speech_StreamPos_RealTime",
    "_ISpeechRecoContextEvents",
    "_ISpeechVoiceEvents",
    "eLEXTYPE_APP",
    "eLEXTYPE_LETTERTOSOUND",
    "eLEXTYPE_MORPHOLOGY",
    "eLEXTYPE_PRIVATE1",
    "eLEXTYPE_PRIVATE10",
    "eLEXTYPE_PRIVATE11",
    "eLEXTYPE_PRIVATE12",
    "eLEXTYPE_PRIVATE13",
    "eLEXTYPE_PRIVATE14",
    "eLEXTYPE_PRIVATE15",
    "eLEXTYPE_PRIVATE16",
    "eLEXTYPE_PRIVATE17",
    "eLEXTYPE_PRIVATE18",
    "eLEXTYPE_PRIVATE19",
    "eLEXTYPE_PRIVATE2",
    "eLEXTYPE_PRIVATE20",
    "eLEXTYPE_PRIVATE3",
    "eLEXTYPE_PRIVATE4",
    "eLEXTYPE_PRIVATE5",
    "eLEXTYPE_PRIVATE6",
    "eLEXTYPE_PRIVATE7",
    "eLEXTYPE_PRIVATE8",
    "eLEXTYPE_PRIVATE9",
    "eLEXTYPE_RESERVED10",
    "eLEXTYPE_RESERVED4",
    "eLEXTYPE_RESERVED6",
    "eLEXTYPE_RESERVED7",
    "eLEXTYPE_RESERVED8",
    "eLEXTYPE_RESERVED9",
    "eLEXTYPE_USER",
    "eLEXTYPE_USER_SHORTCUT",
    "eLEXTYPE_VENDORLEXICON",
    "ePRONFLAG_USED",
    "eWORDTYPE_ADDED",
    "eWORDTYPE_DELETED",
]
_arch_optional = [
]
