from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Speech
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.Urlmon
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Variant
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
DISPID_SRGId: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 1
DISPID_SRGRecoContext: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 2
DISPID_SRGState: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 3
DISPID_SRGRules: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 4
DISPID_SRGReset: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 5
DISPID_SRGCommit: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 6
DISPID_SRGCmdLoadFromFile: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 7
DISPID_SRGCmdLoadFromObject: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 8
DISPID_SRGCmdLoadFromResource: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 9
DISPID_SRGCmdLoadFromMemory: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 10
DISPID_SRGCmdLoadFromProprietaryGrammar: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 11
DISPID_SRGCmdSetRuleState: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 12
DISPID_SRGCmdSetRuleIdState: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 13
DISPID_SRGDictationLoad: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 14
DISPID_SRGDictationUnload: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 15
DISPID_SRGDictationSetState: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 16
DISPID_SRGSetWordSequenceData: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 17
DISPID_SRGSetTextSelection: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 18
DISPID_SRGIsPronounceable: win32more.Windows.Win32.Media.Speech.DISPIDSPRG = 19
DISPIDSPTSI = Int32
DISPIDSPTSI_ActiveOffset: win32more.Windows.Win32.Media.Speech.DISPIDSPTSI = 1
DISPIDSPTSI_ActiveLength: win32more.Windows.Win32.Media.Speech.DISPIDSPTSI = 2
DISPIDSPTSI_SelectionOffset: win32more.Windows.Win32.Media.Speech.DISPIDSPTSI = 3
DISPIDSPTSI_SelectionLength: win32more.Windows.Win32.Media.Speech.DISPIDSPTSI = 4
DISPID_SpeechAudio = Int32
DISPID_SAStatus: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudio = 200
DISPID_SABufferInfo: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudio = 201
DISPID_SADefaultFormat: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudio = 202
DISPID_SAVolume: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudio = 203
DISPID_SABufferNotifySize: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudio = 204
DISPID_SAEventHandle: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudio = 205
DISPID_SASetState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudio = 206
DISPID_SpeechAudioBufferInfo = Int32
DISPID_SABIMinNotification: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioBufferInfo = 1
DISPID_SABIBufferSize: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioBufferInfo = 2
DISPID_SABIEventBias: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioBufferInfo = 3
DISPID_SpeechAudioFormat = Int32
DISPID_SAFType: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioFormat = 1
DISPID_SAFGuid: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioFormat = 2
DISPID_SAFGetWaveFormatEx: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioFormat = 3
DISPID_SAFSetWaveFormatEx: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioFormat = 4
DISPID_SpeechAudioStatus = Int32
DISPID_SASFreeBufferSpace: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioStatus = 1
DISPID_SASNonBlockingIO: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioStatus = 2
DISPID_SASState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioStatus = 3
DISPID_SASCurrentSeekPosition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioStatus = 4
DISPID_SASCurrentDevicePosition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechAudioStatus = 5
DISPID_SpeechBaseStream = Int32
DISPID_SBSFormat: win32more.Windows.Win32.Media.Speech.DISPID_SpeechBaseStream = 1
DISPID_SBSRead: win32more.Windows.Win32.Media.Speech.DISPID_SpeechBaseStream = 2
DISPID_SBSWrite: win32more.Windows.Win32.Media.Speech.DISPID_SpeechBaseStream = 3
DISPID_SBSSeek: win32more.Windows.Win32.Media.Speech.DISPID_SpeechBaseStream = 4
DISPID_SpeechCustomStream = Int32
DISPID_SCSBaseStream: win32more.Windows.Win32.Media.Speech.DISPID_SpeechCustomStream = 100
DISPID_SpeechDataKey = Int32
DISPID_SDKSetBinaryValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 1
DISPID_SDKGetBinaryValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 2
DISPID_SDKSetStringValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 3
DISPID_SDKGetStringValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 4
DISPID_SDKSetLongValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 5
DISPID_SDKGetlongValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 6
DISPID_SDKOpenKey: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 7
DISPID_SDKCreateKey: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 8
DISPID_SDKDeleteKey: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 9
DISPID_SDKDeleteValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 10
DISPID_SDKEnumKeys: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 11
DISPID_SDKEnumValues: win32more.Windows.Win32.Media.Speech.DISPID_SpeechDataKey = 12
DISPID_SpeechFileStream = Int32
DISPID_SFSOpen: win32more.Windows.Win32.Media.Speech.DISPID_SpeechFileStream = 100
DISPID_SFSClose: win32more.Windows.Win32.Media.Speech.DISPID_SpeechFileStream = 101
DISPID_SpeechGrammarRule = Int32
DISPID_SGRAttributes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRule = 1
DISPID_SGRInitialState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRule = 2
DISPID_SGRName: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRule = 3
DISPID_SGRId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRule = 4
DISPID_SGRClear: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRule = 5
DISPID_SGRAddResource: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRule = 6
DISPID_SGRAddState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRule = 7
DISPID_SpeechGrammarRuleState = Int32
DISPID_SGRSRule: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleState = 1
DISPID_SGRSTransitions: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleState = 2
DISPID_SGRSAddWordTransition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleState = 3
DISPID_SGRSAddRuleTransition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleState = 4
DISPID_SGRSAddSpecialTransition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleState = 5
DISPID_SpeechGrammarRuleStateTransition = Int32
DISPID_SGRSTType: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 1
DISPID_SGRSTText: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 2
DISPID_SGRSTRule: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 3
DISPID_SGRSTWeight: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 4
DISPID_SGRSTPropertyName: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 5
DISPID_SGRSTPropertyId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 6
DISPID_SGRSTPropertyValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 7
DISPID_SGRSTNextState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransition = 8
DISPID_SpeechGrammarRuleStateTransitions = Int32
DISPID_SGRSTsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransitions = 1
DISPID_SGRSTsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransitions = 0
DISPID_SGRSTs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRuleStateTransitions = -4
DISPID_SpeechGrammarRules = Int32
DISPID_SGRsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = 1
DISPID_SGRsDynamic: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = 2
DISPID_SGRsAdd: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = 3
DISPID_SGRsCommit: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = 4
DISPID_SGRsCommitAndSave: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = 5
DISPID_SGRsFindRule: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = 6
DISPID_SGRsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = 0
DISPID_SGRs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechGrammarRules = -4
DISPID_SpeechLexicon = Int32
DISPID_SLGenerationId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 1
DISPID_SLGetWords: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 2
DISPID_SLAddPronunciation: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 3
DISPID_SLAddPronunciationByPhoneIds: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 4
DISPID_SLRemovePronunciation: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 5
DISPID_SLRemovePronunciationByPhoneIds: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 6
DISPID_SLGetPronunciations: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 7
DISPID_SLGetGenerationChange: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexicon = 8
DISPID_SpeechLexiconProns = Int32
DISPID_SLPsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconProns = 1
DISPID_SLPsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconProns = 0
DISPID_SLPs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconProns = -4
DISPID_SpeechLexiconPronunciation = Int32
DISPID_SLPType: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconPronunciation = 1
DISPID_SLPLangId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconPronunciation = 2
DISPID_SLPPartOfSpeech: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconPronunciation = 3
DISPID_SLPPhoneIds: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconPronunciation = 4
DISPID_SLPSymbolic: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconPronunciation = 5
DISPID_SpeechLexiconWord = Int32
DISPID_SLWLangId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconWord = 1
DISPID_SLWType: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconWord = 2
DISPID_SLWWord: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconWord = 3
DISPID_SLWPronunciations: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconWord = 4
DISPID_SpeechLexiconWords = Int32
DISPID_SLWsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconWords = 1
DISPID_SLWsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconWords = 0
DISPID_SLWs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechLexiconWords = -4
DISPID_SpeechMMSysAudio = Int32
DISPID_SMSADeviceId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechMMSysAudio = 300
DISPID_SMSALineId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechMMSysAudio = 301
DISPID_SMSAMMHandle: win32more.Windows.Win32.Media.Speech.DISPID_SpeechMMSysAudio = 302
DISPID_SpeechMemoryStream = Int32
DISPID_SMSSetData: win32more.Windows.Win32.Media.Speech.DISPID_SpeechMemoryStream = 100
DISPID_SMSGetData: win32more.Windows.Win32.Media.Speech.DISPID_SpeechMemoryStream = 101
DISPID_SpeechObjectToken = Int32
DISPID_SOTId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 1
DISPID_SOTDataKey: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 2
DISPID_SOTCategory: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 3
DISPID_SOTGetDescription: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 4
DISPID_SOTSetId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 5
DISPID_SOTGetAttribute: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 6
DISPID_SOTCreateInstance: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 7
DISPID_SOTRemove: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 8
DISPID_SOTGetStorageFileName: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 9
DISPID_SOTRemoveStorageFileName: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 10
DISPID_SOTIsUISupported: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 11
DISPID_SOTDisplayUI: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 12
DISPID_SOTMatchesAttributes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectToken = 13
DISPID_SpeechObjectTokenCategory = Int32
DISPID_SOTCId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokenCategory = 1
DISPID_SOTCDefault: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokenCategory = 2
DISPID_SOTCSetId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokenCategory = 3
DISPID_SOTCGetDataKey: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokenCategory = 4
DISPID_SOTCEnumerateTokens: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokenCategory = 5
DISPID_SpeechObjectTokens = Int32
DISPID_SOTsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokens = 1
DISPID_SOTsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokens = 0
DISPID_SOTs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechObjectTokens = -4
DISPID_SpeechPhoneConverter = Int32
DISPID_SPCLangId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhoneConverter = 1
DISPID_SPCPhoneToId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhoneConverter = 2
DISPID_SPCIdToPhone: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhoneConverter = 3
DISPID_SpeechPhraseAlternate = Int32
DISPID_SPARecoResult: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternate = 1
DISPID_SPAStartElementInResult: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternate = 2
DISPID_SPANumberOfElementsInResult: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternate = 3
DISPID_SPAPhraseInfo: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternate = 4
DISPID_SPACommit: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternate = 5
DISPID_SpeechPhraseAlternates = Int32
DISPID_SPAsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternates = 1
DISPID_SPAsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternates = 0
DISPID_SPAs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseAlternates = -4
DISPID_SpeechPhraseBuilder = Int32
DISPID_SPPBRestorePhraseFromMemory: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseBuilder = 1
DISPID_SpeechPhraseElement = Int32
DISPID_SPEAudioTimeOffset: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 1
DISPID_SPEAudioSizeTime: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 2
DISPID_SPEAudioStreamOffset: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 3
DISPID_SPEAudioSizeBytes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 4
DISPID_SPERetainedStreamOffset: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 5
DISPID_SPERetainedSizeBytes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 6
DISPID_SPEDisplayText: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 7
DISPID_SPELexicalForm: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 8
DISPID_SPEPronunciation: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 9
DISPID_SPEDisplayAttributes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 10
DISPID_SPERequiredConfidence: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 11
DISPID_SPEActualConfidence: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 12
DISPID_SPEEngineConfidence: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElement = 13
DISPID_SpeechPhraseElements = Int32
DISPID_SPEsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElements = 1
DISPID_SPEsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElements = 0
DISPID_SPEs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseElements = -4
DISPID_SpeechPhraseInfo = Int32
DISPID_SPILanguageId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 1
DISPID_SPIGrammarId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 2
DISPID_SPIStartTime: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 3
DISPID_SPIAudioStreamPosition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 4
DISPID_SPIAudioSizeBytes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 5
DISPID_SPIRetainedSizeBytes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 6
DISPID_SPIAudioSizeTime: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 7
DISPID_SPIRule: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 8
DISPID_SPIProperties: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 9
DISPID_SPIElements: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 10
DISPID_SPIReplacements: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 11
DISPID_SPIEngineId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 12
DISPID_SPIEnginePrivateData: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 13
DISPID_SPISaveToMemory: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 14
DISPID_SPIGetText: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 15
DISPID_SPIGetDisplayAttributes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseInfo = 16
DISPID_SpeechPhraseProperties = Int32
DISPID_SPPsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperties = 1
DISPID_SPPsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperties = 0
DISPID_SPPs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperties = -4
DISPID_SpeechPhraseProperty = Int32
DISPID_SPPName: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 1
DISPID_SPPId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 2
DISPID_SPPValue: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 3
DISPID_SPPFirstElement: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 4
DISPID_SPPNumberOfElements: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 5
DISPID_SPPEngineConfidence: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 6
DISPID_SPPConfidence: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 7
DISPID_SPPParent: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 8
DISPID_SPPChildren: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseProperty = 9
DISPID_SpeechPhraseReplacement = Int32
DISPID_SPRDisplayAttributes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseReplacement = 1
DISPID_SPRText: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseReplacement = 2
DISPID_SPRFirstElement: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseReplacement = 3
DISPID_SPRNumberOfElements: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseReplacement = 4
DISPID_SpeechPhraseReplacements = Int32
DISPID_SPRsCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseReplacements = 1
DISPID_SPRsItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseReplacements = 0
DISPID_SPRs_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseReplacements = -4
DISPID_SpeechPhraseRule = Int32
DISPID_SPRuleName: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 1
DISPID_SPRuleId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 2
DISPID_SPRuleFirstElement: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 3
DISPID_SPRuleNumberOfElements: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 4
DISPID_SPRuleParent: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 5
DISPID_SPRuleChildren: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 6
DISPID_SPRuleConfidence: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 7
DISPID_SPRuleEngineConfidence: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRule = 8
DISPID_SpeechPhraseRules = Int32
DISPID_SPRulesCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRules = 1
DISPID_SPRulesItem: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRules = 0
DISPID_SPRules_NewEnum: win32more.Windows.Win32.Media.Speech.DISPID_SpeechPhraseRules = -4
DISPID_SpeechRecoContext = Int32
DISPID_SRCRecognizer: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 1
DISPID_SRCAudioInInterferenceStatus: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 2
DISPID_SRCRequestedUIType: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 3
DISPID_SRCVoice: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 4
DISPID_SRAllowVoiceFormatMatchingOnNextSet: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 5
DISPID_SRCVoicePurgeEvent: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 6
DISPID_SRCEventInterests: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 7
DISPID_SRCCmdMaxAlternates: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 8
DISPID_SRCState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 9
DISPID_SRCRetainedAudio: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 10
DISPID_SRCRetainedAudioFormat: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 11
DISPID_SRCPause: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 12
DISPID_SRCResume: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 13
DISPID_SRCCreateGrammar: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 14
DISPID_SRCCreateResultFromMemory: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 15
DISPID_SRCBookmark: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 16
DISPID_SRCSetAdaptationData: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContext = 17
DISPID_SpeechRecoContextEvents = Int32
DISPID_SRCEStartStream: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 1
DISPID_SRCEEndStream: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 2
DISPID_SRCEBookmark: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 3
DISPID_SRCESoundStart: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 4
DISPID_SRCESoundEnd: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 5
DISPID_SRCEPhraseStart: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 6
DISPID_SRCERecognition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 7
DISPID_SRCEHypothesis: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 8
DISPID_SRCEPropertyNumberChange: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 9
DISPID_SRCEPropertyStringChange: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 10
DISPID_SRCEFalseRecognition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 11
DISPID_SRCEInterference: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 12
DISPID_SRCERequestUI: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 13
DISPID_SRCERecognizerStateChange: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 14
DISPID_SRCEAdaptation: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 15
DISPID_SRCERecognitionForOtherContext: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 16
DISPID_SRCEAudioLevel: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 17
DISPID_SRCEEnginePrivate: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoContextEvents = 18
DISPID_SpeechRecoResult = Int32
DISPID_SRRRecoContext: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 1
DISPID_SRRTimes: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 2
DISPID_SRRAudioFormat: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 3
DISPID_SRRPhraseInfo: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 4
DISPID_SRRAlternates: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 5
DISPID_SRRAudio: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 6
DISPID_SRRSpeakAudio: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 7
DISPID_SRRSaveToMemory: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 8
DISPID_SRRDiscardResultInfo: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult = 9
DISPID_SpeechRecoResult2 = Int32
DISPID_SRRSetTextFeedback: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResult2 = 12
DISPID_SpeechRecoResultTimes = Int32
DISPID_SRRTStreamTime: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResultTimes = 1
DISPID_SRRTLength: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResultTimes = 2
DISPID_SRRTTickCount: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResultTimes = 3
DISPID_SRRTOffsetFromStart: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecoResultTimes = 4
DISPID_SpeechRecognizer = Int32
DISPID_SRRecognizer: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 1
DISPID_SRAllowAudioInputFormatChangesOnNextSet: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 2
DISPID_SRAudioInput: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 3
DISPID_SRAudioInputStream: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 4
DISPID_SRIsShared: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 5
DISPID_SRState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 6
DISPID_SRStatus: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 7
DISPID_SRProfile: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 8
DISPID_SREmulateRecognition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 9
DISPID_SRCreateRecoContext: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 10
DISPID_SRGetFormat: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 11
DISPID_SRSetPropertyNumber: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 12
DISPID_SRGetPropertyNumber: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 13
DISPID_SRSetPropertyString: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 14
DISPID_SRGetPropertyString: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 15
DISPID_SRIsUISupported: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 16
DISPID_SRDisplayUI: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 17
DISPID_SRGetRecognizers: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 18
DISPID_SVGetAudioInputs: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 19
DISPID_SVGetProfiles: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizer = 20
DISPID_SpeechRecognizerStatus = Int32
DISPID_SRSAudioStatus: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizerStatus = 1
DISPID_SRSCurrentStreamPosition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizerStatus = 2
DISPID_SRSCurrentStreamNumber: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizerStatus = 3
DISPID_SRSNumberOfActiveRules: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizerStatus = 4
DISPID_SRSClsidEngine: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizerStatus = 5
DISPID_SRSSupportedLanguages: win32more.Windows.Win32.Media.Speech.DISPID_SpeechRecognizerStatus = 6
DISPID_SpeechVoice = Int32
DISPID_SVStatus: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 1
DISPID_SVVoice: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 2
DISPID_SVAudioOutput: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 3
DISPID_SVAudioOutputStream: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 4
DISPID_SVRate: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 5
DISPID_SVVolume: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 6
DISPID_SVAllowAudioOuputFormatChangesOnNextSet: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 7
DISPID_SVEventInterests: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 8
DISPID_SVPriority: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 9
DISPID_SVAlertBoundary: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 10
DISPID_SVSyncronousSpeakTimeout: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 11
DISPID_SVSpeak: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 12
DISPID_SVSpeakStream: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 13
DISPID_SVPause: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 14
DISPID_SVResume: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 15
DISPID_SVSkip: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 16
DISPID_SVGetVoices: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 17
DISPID_SVGetAudioOutputs: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 18
DISPID_SVWaitUntilDone: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 19
DISPID_SVSpeakCompleteEvent: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 20
DISPID_SVIsUISupported: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 21
DISPID_SVDisplayUI: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoice = 22
DISPID_SpeechVoiceEvent = Int32
DISPID_SVEStreamStart: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 1
DISPID_SVEStreamEnd: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 2
DISPID_SVEVoiceChange: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 3
DISPID_SVEBookmark: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 4
DISPID_SVEWord: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 5
DISPID_SVEPhoneme: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 6
DISPID_SVESentenceBoundary: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 7
DISPID_SVEViseme: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 8
DISPID_SVEAudioLevel: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 9
DISPID_SVEEnginePrivate: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceEvent = 10
DISPID_SpeechVoiceStatus = Int32
DISPID_SVSCurrentStreamNumber: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 1
DISPID_SVSLastStreamNumberQueued: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 2
DISPID_SVSLastResult: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 3
DISPID_SVSRunningState: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 4
DISPID_SVSInputWordPosition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 5
DISPID_SVSInputWordLength: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 6
DISPID_SVSInputSentencePosition: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 7
DISPID_SVSInputSentenceLength: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 8
DISPID_SVSLastBookmark: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 9
DISPID_SVSLastBookmarkId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 10
DISPID_SVSPhonemeId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 11
DISPID_SVSVisemeId: win32more.Windows.Win32.Media.Speech.DISPID_SpeechVoiceStatus = 12
DISPID_SpeechWaveFormatEx = Int32
DISPID_SWFEFormatTag: win32more.Windows.Win32.Media.Speech.DISPID_SpeechWaveFormatEx = 1
DISPID_SWFEChannels: win32more.Windows.Win32.Media.Speech.DISPID_SpeechWaveFormatEx = 2
DISPID_SWFESamplesPerSec: win32more.Windows.Win32.Media.Speech.DISPID_SpeechWaveFormatEx = 3
DISPID_SWFEAvgBytesPerSec: win32more.Windows.Win32.Media.Speech.DISPID_SpeechWaveFormatEx = 4
DISPID_SWFEBlockAlign: win32more.Windows.Win32.Media.Speech.DISPID_SpeechWaveFormatEx = 5
DISPID_SWFEBitsPerSample: win32more.Windows.Win32.Media.Speech.DISPID_SpeechWaveFormatEx = 6
DISPID_SWFEExtraData: win32more.Windows.Win32.Media.Speech.DISPID_SpeechWaveFormatEx = 7
DISPID_SpeechXMLRecoResult = Int32
DISPID_SRRGetXMLResult: win32more.Windows.Win32.Media.Speech.DISPID_SpeechXMLRecoResult = 10
DISPID_SRRGetXMLErrorInfo: win32more.Windows.Win32.Media.Speech.DISPID_SpeechXMLRecoResult = 11
class IEnumSpObjectTokens(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{06b64f9e-7fda-11d2-b4f2-00c04f797396}')
    @commethod(3)
    def Next(self, celt: UInt32, pelt: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Media.Speech.IEnumSpObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Item(self, Index: UInt32, ppToken: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpAudio(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpStreamFormat
    _iid_ = Guid('{c05c768f-fae8-4ec2-8e07-338321c12452}')
    @commethod(15)
    def SetState(self, NewState: win32more.Windows.Win32.Media.Speech.SPAUDIOSTATE, ullReserved: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetFormat(self, rguidFmtId: POINTER(Guid), pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStatus(self, pStatus: POINTER(win32more.Windows.Win32.Media.Speech.SPAUDIOSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetBufferInfo(self, pBuffInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPAUDIOBUFFERINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetBufferInfo(self, pBuffInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPAUDIOBUFFERINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultFormat(self, pFormatId: POINTER(Guid), ppCoMemWaveFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EventHandle(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
    @commethod(22)
    def GetVolumeLevel(self, pLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetVolumeLevel(self, Level: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBufferNotifySize(self, pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetBufferNotifySize(self, cbSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpCFGInterpreter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f3d3f926-11fc-11d3-bb97-00c04f8ee6c0}')
    @commethod(3)
    def InitGrammar(self, pszGrammarName: win32more.Windows.Win32.Foundation.PWSTR, pvGrammarData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Interpret(self, pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhraseBuilder, ulFirstElement: UInt32, ulCountOfElements: UInt32, pSite: win32more.Windows.Win32.Media.Speech.ISpCFGInterpreterSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpCFGInterpreterSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a6ffad8-78b6-473d-b844-98152e4fb16b}')
    @commethod(3)
    def AddTextReplacement(self, pReplace: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEREPLACEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddProperty(self, pProperty: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetResourceValue(self, pszResourceName: win32more.Windows.Win32.Foundation.PWSTR, ppCoMemResource: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpContainerLexicon(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpLexicon
    _iid_ = Guid('{8565572f-c094-41cc-b56e-10bd9c3ff044}')
    @commethod(9)
    def AddLexicon(self, pAddLexicon: win32more.Windows.Win32.Media.Speech.ISpLexicon, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpDataKey(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{14056581-e16c-11d2-bb90-00c04f8ee6c0}')
    @commethod(3)
    def SetData(self, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, cbData: UInt32, pData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetData(self, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, pcbData: POINTER(UInt32), pData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStringValue(self, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringValue(self, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, ppszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDWORD(self, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, dwValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDWORD(self, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, pdwValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OpenKey(self, pszSubKeyName: win32more.Windows.Win32.Foundation.PWSTR, ppSubKey: POINTER(win32more.Windows.Win32.Media.Speech.ISpDataKey)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateKey(self, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, ppSubKey: POINTER(win32more.Windows.Win32.Media.Speech.ISpDataKey)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteKey(self, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteValue(self, pszValueName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnumKeys(self, Index: UInt32, ppszSubKeyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumValues(self, Index: UInt32, ppszValueName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpDisplayAlternates(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8d7c7e2-0dde-44b7-afe3-b0c991fbeb5e}')
    @commethod(3)
    def GetDisplayAlternates(self, pPhrase: POINTER(win32more.Windows.Win32.Media.Speech.SPDISPLAYPHRASE), cRequestCount: UInt32, ppCoMemPhrases: POINTER(POINTER(win32more.Windows.Win32.Media.Speech.SPDISPLAYPHRASE)), pcPhrasesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFullStopTrailSpace(self, ulTrailSpace: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpEnginePronunciation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c360ce4b-76d1-4214-ad68-52657d5083da}')
    @commethod(3)
    def Normalize(self, pszWord: win32more.Windows.Win32.Foundation.PWSTR, pszLeftContext: win32more.Windows.Win32.Foundation.PWSTR, pszRightContext: win32more.Windows.Win32.Foundation.PWSTR, LangID: UInt16, pNormalizationList: POINTER(win32more.Windows.Win32.Media.Speech.SPNORMALIZATIONLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPronunciations(self, pszWord: win32more.Windows.Win32.Foundation.PWSTR, pszLeftContext: win32more.Windows.Win32.Foundation.PWSTR, pszRightContext: win32more.Windows.Win32.Foundation.PWSTR, LangID: UInt16, pEnginePronunciationList: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDPRONUNCIATIONLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpErrorLog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4711347-e608-11d2-a086-00c04f8ef9b5}')
    @commethod(3)
    def AddError(self, lLineNumber: Int32, hr: win32more.Windows.Win32.Foundation.HRESULT, pszDescription: win32more.Windows.Win32.Foundation.PWSTR, pszHelpFile: win32more.Windows.Win32.Foundation.PWSTR, dwHelpContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{be7a9cc9-5f9e-11d2-960f-00c04f8ee628}')
    @commethod(3)
    def AddEvents(self, pEventArray: POINTER(win32more.Windows.Win32.Media.Speech.SPEVENT), ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEventInterest(self, pullEventInterest: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpEventSource(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpNotifySource
    _iid_ = Guid('{be7a9cce-5f9e-11d2-960f-00c04f8ee628}')
    @commethod(10)
    def SetInterest(self, ullEventInterest: UInt64, ullQueuedInterest: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEvents(self, ulCount: UInt32, pEventArray: POINTER(win32more.Windows.Win32.Media.Speech.SPEVENT), pulFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInfo(self, pInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPEVENTSOURCEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpEventSource2(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpEventSource
    _iid_ = Guid('{2373a435-6a4b-429e-a6ac-d4231a61975b}')
    @commethod(13)
    def GetEventsEx(self, ulCount: UInt32, pEventArray: POINTER(win32more.Windows.Win32.Media.Speech.SPEVENTEX), pulFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpGramCompBackend(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpGrammarBuilder
    _iid_ = Guid('{3ddca27c-665c-4786-9f97-8c90c3488b61}')
    @commethod(11)
    def SetSaveObjects(self, pStream: win32more.Windows.Win32.System.Com.IStream, pErrorLog: win32more.Windows.Win32.Media.Speech.ISpErrorLog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def InitFromBinaryGrammar(self, pBinaryData: POINTER(win32more.Windows.Win32.Media.Speech.SPBINARYGRAMMAR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpGrammarBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8137828f-591a-4a42-be58-49ea7ebaac68}')
    @commethod(3)
    def ResetGrammar(self, NewLanguage: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRule(self, pszRuleName: win32more.Windows.Win32.Foundation.PWSTR, dwRuleId: UInt32, dwAttributes: UInt32, fCreateIfNotExist: win32more.Windows.Win32.Foundation.BOOL, phInitialState: POINTER(win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearRule(self, hState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateNewState(self, hState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, phState: POINTER(win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddWordTransition(self, hFromState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, hToState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, psz: win32more.Windows.Win32.Foundation.PWSTR, pszSeparators: win32more.Windows.Win32.Foundation.PWSTR, eWordType: win32more.Windows.Win32.Media.Speech.SPGRAMMARWORDTYPE, Weight: Single, pPropInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPPROPERTYINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddRuleTransition(self, hFromState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, hToState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, hRule: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, Weight: Single, pPropInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPPROPERTYINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddResource(self, hRuleState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, pszResourceName: win32more.Windows.Win32.Foundation.PWSTR, pszResourceValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Commit(self, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpGrammarBuilder2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ab10026-20cc-4b20-8c22-a49c9ba78f60}')
    @commethod(3)
    def AddTextSubset(self, hFromState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, hToState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, psz: win32more.Windows.Win32.Foundation.PWSTR, eMatchMode: win32more.Windows.Win32.Media.Speech.SPMATCHINGMODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPhoneticAlphabet(self, phoneticALphabet: win32more.Windows.Win32.Media.Speech.PHONETICALPHABET) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpGrammarCompiler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b1e29d58-a675-11d2-8302-00c04f8ee6c0}')
    @commethod(3)
    def CompileStream(self, pSource: win32more.Windows.Win32.System.Com.IStream, pDest: win32more.Windows.Win32.System.Com.IStream, pHeader: win32more.Windows.Win32.System.Com.IStream, pReserved: win32more.Windows.Win32.System.Com.IUnknown, pErrorLog: win32more.Windows.Win32.Media.Speech.ISpErrorLog, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpITNProcessor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{12d7360f-a1c9-11d3-bc90-00c04f72df9f}')
    @commethod(3)
    def LoadITNGrammar(self, pszCLSID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ITNPhrase(self, pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhraseBuilder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpLexicon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{da41a7c2-5383-4db2-916b-6c1719e3db58}')
    @commethod(3)
    def GetPronunciations(self, pszWord: win32more.Windows.Win32.Foundation.PWSTR, LangID: UInt16, dwFlags: UInt32, pWordPronunciationList: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDPRONUNCIATIONLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPronunciation(self, pszWord: win32more.Windows.Win32.Foundation.PWSTR, LangID: UInt16, ePartOfSpeech: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH, pszPronunciation: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemovePronunciation(self, pszWord: win32more.Windows.Win32.Foundation.PWSTR, LangID: UInt16, ePartOfSpeech: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH, pszPronunciation: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGeneration(self, pdwGeneration: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGenerationChange(self, dwFlags: UInt32, pdwGeneration: POINTER(UInt32), pWordList: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(self, dwFlags: UInt32, pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pWordList: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpMMSysAudio(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpAudio
    _iid_ = Guid('{15806f6e-1d70-4b48-98e6-3b1a007509ab}')
    @commethod(26)
    def GetDeviceId(self, puDeviceId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetDeviceId(self, uDeviceId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetMMHandle(self, pHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetLineId(self, puLineId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetLineId(self, uLineId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpNotifyCallback(ComPtr):
    extends: None
    @commethod(0)
    def NotifyCallback(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{259684dc-37c3-11d2-9603-00c04f8ee628}')
    @commethod(3)
    def Notify(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpNotifySource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5eff4aef-8487-11d2-961c-00c04f8ee628}')
    @commethod(3)
    def SetNotifySink(self, pNotifySink: win32more.Windows.Win32.Media.Speech.ISpNotifySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNotifyWindowMessage(self, hWnd: win32more.Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNotifyCallbackFunction(self, pfnCallback: POINTER(win32more.Windows.Win32.Media.Speech.SPNOTIFYCALLBACK), wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetNotifyCallbackInterface(self, pSpCallback: win32more.Windows.Win32.Media.Speech.ISpNotifyCallback, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetNotifyWin32Event(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WaitForNotifyEvent(self, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNotifyEventHandle(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
class ISpNotifyTranslator(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpNotifySink
    _iid_ = Guid('{aca16614-5d3d-11d2-960e-00c04f8ee628}')
    @commethod(4)
    def InitWindowMessage(self, hWnd: win32more.Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitCallback(self, pfnCallback: POINTER(win32more.Windows.Win32.Media.Speech.SPNOTIFYCALLBACK), wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitSpNotifyCallback(self, pSpCallback: win32more.Windows.Win32.Media.Speech.ISpNotifyCallback, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InitWin32Event(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE, fCloseHandleOnRelease: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Wait(self, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEventHandle(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
class ISpObjectToken(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpDataKey
    _iid_ = Guid('{14056589-e16c-11d2-bb90-00c04f8ee6c0}')
    @commethod(15)
    def SetId(self, pszCategoryId: win32more.Windows.Win32.Foundation.PWSTR, pszTokenId: win32more.Windows.Win32.Foundation.PWSTR, fCreateIfNotExist: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetId(self, ppszCoMemTokenId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCategory(self, ppTokenCategory: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectTokenCategory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateInstance(self, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, dwClsContext: UInt32, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetStorageFileName(self, clsidCaller: POINTER(Guid), pszValueName: win32more.Windows.Win32.Foundation.PWSTR, pszFileNameSpecifier: win32more.Windows.Win32.Foundation.PWSTR, nFolder: UInt32, ppszFilePath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RemoveStorageFileName(self, clsidCaller: POINTER(Guid), pszKeyName: win32more.Windows.Win32.Foundation.PWSTR, fDeleteFile: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Remove(self, pclsidCaller: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsUISupported(self, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32, punkObject: win32more.Windows.Win32.System.Com.IUnknown, pfSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DisplayUI(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32, punkObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def MatchesAttributes(self, pszAttributes: win32more.Windows.Win32.Foundation.PWSTR, pfMatches: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpObjectTokenCategory(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpDataKey
    _iid_ = Guid('{2d3d3845-39af-4850-bbf9-40b49780011d}')
    @commethod(15)
    def SetId(self, pszCategoryId: win32more.Windows.Win32.Foundation.PWSTR, fCreateIfNotExist: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetId(self, ppszCoMemCategoryId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDataKey(self, spdkl: win32more.Windows.Win32.Media.Speech.SPDATAKEYLOCATION, ppDataKey: POINTER(win32more.Windows.Win32.Media.Speech.ISpDataKey)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumTokens(self, pzsReqAttribs: win32more.Windows.Win32.Foundation.PWSTR, pszOptAttribs: win32more.Windows.Win32.Foundation.PWSTR, ppEnum: POINTER(win32more.Windows.Win32.Media.Speech.IEnumSpObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDefaultTokenId(self, pszTokenId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultTokenId(self, ppszCoMemTokenId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpObjectTokenEnumBuilder(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.IEnumSpObjectTokens
    _iid_ = Guid('{06b64f9f-7fda-11d2-b4f2-00c04f797396}')
    @commethod(9)
    def SetAttribs(self, pszReqAttribs: win32more.Windows.Win32.Foundation.PWSTR, pszOptAttribs: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddTokens(self, cTokens: UInt32, pToken: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddTokensFromDataKey(self, pDataKey: win32more.Windows.Win32.Media.Speech.ISpDataKey, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pszCategoryId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddTokensFromTokenEnum(self, pTokenEnum: win32more.Windows.Win32.Media.Speech.IEnumSpObjectTokens) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Sort(self, pszTokenIdToListFirst: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpObjectTokenInit(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpObjectToken
    _iid_ = Guid('{b8aab0cf-346f-49d8-9499-c8b03f161d51}')
    @commethod(25)
    def InitFromDataKey(self, pszCategoryId: win32more.Windows.Win32.Foundation.PWSTR, pszTokenId: win32more.Windows.Win32.Foundation.PWSTR, pDataKey: win32more.Windows.Win32.Media.Speech.ISpDataKey) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpObjectWithToken(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b559f40-e952-11d2-bb91-00c04f8ee6c0}')
    @commethod(3)
    def SetObjectToken(self, pToken: win32more.Windows.Win32.Media.Speech.ISpObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectToken(self, ppToken: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneConverter(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpObjectWithToken
    _iid_ = Guid('{8445c581-0cac-4a38-abfe-9b2ce2826455}')
    @commethod(5)
    def PhoneToId(self, pszPhone: win32more.Windows.Win32.Foundation.PWSTR, pId: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IdToPhone(self, pId: POINTER(UInt16), pszPhone: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneticAlphabetConverter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{133adcd4-19b4-4020-9fdc-842e78253b17}')
    @commethod(3)
    def GetLangId(self, pLangID: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLangId(self, LangID: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SAPI2UPS(self, pszSAPIId: POINTER(UInt16), pszUPSId: POINTER(UInt16), cMaxLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UPS2SAPI(self, pszUPSId: POINTER(UInt16), pszSAPIId: POINTER(UInt16), cMaxLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxConvertLength(self, cSrcLength: UInt32, bSAPI2UPS: win32more.Windows.Win32.Foundation.BOOL, pcMaxDestLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPhoneticAlphabetSelection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b2745efd-42ce-48ca-81f1-a96e02538a90}')
    @commethod(3)
    def IsAlphabetUPS(self, pfIsUPS: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAlphabetToUPS(self, fForceUPS: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPhrase(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a5c0354-b621-4b5a-8791-d306ed379e53}')
    @commethod(3)
    def GetPhrase(self, ppCoMemPhrase: POINTER(POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSerializedPhrase(self, ppCoMemPhrase: POINTER(POINTER(win32more.Windows.Win32.Media.Speech.SPSERIALIZEDPHRASE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetText(self, ulStart: UInt32, ulCount: UInt32, fUseTextReplacements: win32more.Windows.Win32.Foundation.BOOL, ppszCoMemText: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pbDisplayAttributes: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Discard(self, dwValueTypes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPhrase2(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpPhrase
    _iid_ = Guid('{f264da52-e457-4696-b856-a737b717af79}')
    @commethod(7)
    def GetXMLResult(self, ppszCoMemXMLResult: POINTER(win32more.Windows.Win32.Foundation.PWSTR), Options: win32more.Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetXMLErrorInfo(self, pSemanticErrorInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPSEMANTICERRORINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAudio(self, ulStartElement: UInt32, cElements: UInt32, ppStream: POINTER(win32more.Windows.Win32.Media.Speech.ISpStreamFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPhraseAlt(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpPhrase
    _iid_ = Guid('{8fcebc98-4e49-4067-9c6c-d86a0e092e3d}')
    @commethod(7)
    def GetAltInfo(self, ppParent: POINTER(win32more.Windows.Win32.Media.Speech.ISpPhrase), pulStartElementInParent: POINTER(UInt32), pcElementsInParent: POINTER(UInt32), pcElementsInAlt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPhraseBuilder(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpPhrase
    _iid_ = Guid('{88a3342a-0bed-4834-922b-88d43173162f}')
    @commethod(7)
    def InitFromPhrase(self, pPhrase: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InitFromSerializedPhrase(self, pPhrase: POINTER(win32more.Windows.Win32.Media.Speech.SPSERIALIZEDPHRASE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddElements(self, cElements: UInt32, pElement: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddRules(self, hParent: win32more.Windows.Win32.Media.Speech.SPPHRASERULEHANDLE, pRule: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASERULE), phNewRule: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASERULEHANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddProperties(self, hParent: win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTYHANDLE, pProperty: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTY), phNewProperty: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTYHANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddReplacements(self, cReplacements: UInt32, pReplacements: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEREPLACEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpPrivateEngineCallEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{defd682a-fe0a-42b9-bfa1-56d3d6cecfaf}')
    @commethod(3)
    def CallEngineSynchronize(self, pInFrame: VoidPtr, ulInFrameSize: UInt32, ppCoMemOutFrame: POINTER(VoidPtr), pulOutFrameSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CallEngineImmediate(self, pInFrame: VoidPtr, ulInFrameSize: UInt32, ppCoMemOutFrame: POINTER(VoidPtr), pulOutFrameSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b4fb971-b115-4de1-ad97-e482e3bf6ee4}')
    @commethod(3)
    def SetPropertyNum(self, pName: win32more.Windows.Win32.Foundation.PWSTR, lValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyNum(self, pName: win32more.Windows.Win32.Foundation.PWSTR, plValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPropertyString(self, pName: win32more.Windows.Win32.Foundation.PWSTR, pValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyString(self, pName: win32more.Windows.Win32.Foundation.PWSTR, ppCoMemValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecoContext(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpEventSource
    _iid_ = Guid('{f740a62f-7c15-489e-8234-940a33d9272d}')
    @commethod(13)
    def GetRecognizer(self, ppRecognizer: POINTER(win32more.Windows.Win32.Media.Speech.ISpRecognizer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateGrammar(self, ullGrammarId: UInt64, ppGrammar: POINTER(win32more.Windows.Win32.Media.Speech.ISpRecoGrammar)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStatus(self, pStatus: POINTER(win32more.Windows.Win32.Media.Speech.SPRECOCONTEXTSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMaxAlternates(self, pcAlternates: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetMaxAlternates(self, cAlternates: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetAudioOptions(self, Options: win32more.Windows.Win32.Media.Speech.SPAUDIOOPTIONS, pAudioFormatId: POINTER(Guid), pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAudioOptions(self, pOptions: POINTER(win32more.Windows.Win32.Media.Speech.SPAUDIOOPTIONS), pAudioFormatId: POINTER(Guid), ppCoMemWFEX: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeserializeResult(self, pSerializedResult: POINTER(win32more.Windows.Win32.Media.Speech.SPSERIALIZEDRESULT), ppResult: POINTER(win32more.Windows.Win32.Media.Speech.ISpRecoResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Bookmark(self, Options: win32more.Windows.Win32.Media.Speech.SPBOOKMARKOPTIONS, ullStreamPosition: UInt64, lparamEvent: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetAdaptationData(self, pAdaptationData: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Pause(self, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Resume(self, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetVoice(self, pVoice: win32more.Windows.Win32.Media.Speech.ISpVoice, fAllowFormatChanges: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetVoice(self, ppVoice: POINTER(win32more.Windows.Win32.Media.Speech.ISpVoice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetVoicePurgeEvent(self, ullEventInterest: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetVoicePurgeEvent(self, pullEventInterest: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetContextState(self, eContextState: win32more.Windows.Win32.Media.Speech.SPCONTEXTSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetContextState(self, peContextState: POINTER(win32more.Windows.Win32.Media.Speech.SPCONTEXTSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecoContext2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bead311c-52ff-437f-9464-6b21054ca73d}')
    @commethod(3)
    def SetGrammarOptions(self, eGrammarOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGrammarOptions(self, peGrammarOptions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAdaptationData2(self, pAdaptationData: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pTopicName: win32more.Windows.Win32.Foundation.PWSTR, eAdaptationSettings: UInt32, eRelevance: win32more.Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecoGrammar(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpGrammarBuilder
    _iid_ = Guid('{2177db29-7f45-47d0-8554-067e91c80502}')
    @commethod(11)
    def GetGrammarId(self, pullGrammarId: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecoContext(self, ppRecoCtxt: POINTER(win32more.Windows.Win32.Media.Speech.ISpRecoContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def LoadCmdFromFile(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def LoadCmdFromObject(self, rcid: POINTER(Guid), pszGrammarName: win32more.Windows.Win32.Foundation.PWSTR, Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LoadCmdFromResource(self, hModule: win32more.Windows.Win32.Foundation.HMODULE, pszResourceName: win32more.Windows.Win32.Foundation.PWSTR, pszResourceType: win32more.Windows.Win32.Foundation.PWSTR, wLanguage: UInt16, Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def LoadCmdFromMemory(self, pGrammar: POINTER(win32more.Windows.Win32.Media.Speech.SPBINARYGRAMMAR), Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def LoadCmdFromProprietaryGrammar(self, rguidParam: POINTER(Guid), pszStringParam: win32more.Windows.Win32.Foundation.PWSTR, pvDataPrarm: VoidPtr, cbDataSize: UInt32, Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRuleState(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pReserved: VoidPtr, NewState: win32more.Windows.Win32.Media.Speech.SPRULESTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetRuleIdState(self, ulRuleId: UInt32, NewState: win32more.Windows.Win32.Media.Speech.SPRULESTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def LoadDictation(self, pszTopicName: win32more.Windows.Win32.Foundation.PWSTR, Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def UnloadDictation(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetDictationState(self, NewState: win32more.Windows.Win32.Media.Speech.SPRULESTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWordSequenceData(self, pText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32, pInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTextSelection(self, pInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsPronounceable(self, pszWord: win32more.Windows.Win32.Foundation.PWSTR, pWordPronounceable: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDPRONOUNCEABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetGrammarState(self, eGrammarState: win32more.Windows.Win32.Media.Speech.SPGRAMMARSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SaveCmd(self, pStream: win32more.Windows.Win32.System.Com.IStream, ppszCoMemErrorText: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetGrammarState(self, peGrammarState: POINTER(win32more.Windows.Win32.Media.Speech.SPGRAMMARSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecoGrammar2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b37bc9e-9ed6-44a3-93d3-18f022b79ec3}')
    @commethod(3)
    def GetRules(self, ppCoMemRules: POINTER(POINTER(win32more.Windows.Win32.Media.Speech.SPRULE)), puNumRules: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadCmdFromFile2(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS, pszSharingUri: win32more.Windows.Win32.Foundation.PWSTR, pszBaseUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadCmdFromMemory2(self, pGrammar: POINTER(win32more.Windows.Win32.Media.Speech.SPBINARYGRAMMAR), Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS, pszSharingUri: win32more.Windows.Win32.Foundation.PWSTR, pszBaseUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRulePriority(self, pszRuleName: win32more.Windows.Win32.Foundation.PWSTR, ulRuleId: UInt32, nRulePriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRuleWeight(self, pszRuleName: win32more.Windows.Win32.Foundation.PWSTR, ulRuleId: UInt32, flWeight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDictationWeight(self, flWeight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetGrammarLoader(self, pLoader: win32more.Windows.Win32.Media.Speech.ISpeechResourceLoader) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSMLSecurityManager(self, pSMLSecurityManager: win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityManager) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecoResult(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpPhrase
    _iid_ = Guid('{20b053be-e235-43cd-9a2a-8d17a48b7842}')
    @commethod(7)
    def GetResultTimes(self, pTimes: POINTER(win32more.Windows.Win32.Media.Speech.SPRECORESULTTIMES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAlternates(self, ulStartElement: UInt32, cElements: UInt32, ulRequestCount: UInt32, ppPhrases: POINTER(win32more.Windows.Win32.Media.Speech.ISpPhraseAlt), pcPhrasesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAudio(self, ulStartElement: UInt32, cElements: UInt32, ppStream: POINTER(win32more.Windows.Win32.Media.Speech.ISpStreamFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SpeakAudio(self, ulStartElement: UInt32, cElements: UInt32, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Serialize(self, ppCoMemSerializedResult: POINTER(POINTER(win32more.Windows.Win32.Media.Speech.SPSERIALIZEDRESULT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ScaleAudio(self, pAudioFormatId: POINTER(Guid), pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecoContext(self, ppRecoContext: POINTER(win32more.Windows.Win32.Media.Speech.ISpRecoContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecoResult2(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpRecoResult
    _iid_ = Guid('{27cac6c4-88f2-41f2-8817-0c95e59f1e6e}')
    @commethod(14)
    def CommitAlternate(self, pPhraseAlt: win32more.Windows.Win32.Media.Speech.ISpPhraseAlt, ppNewResult: POINTER(win32more.Windows.Win32.Media.Speech.ISpRecoResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CommitText(self, ulStartElement: UInt32, cElements: UInt32, pszCorrectedData: win32more.Windows.Win32.Foundation.PWSTR, eCommitFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetTextFeedback(self, pszFeedback: win32more.Windows.Win32.Foundation.PWSTR, fSuccessful: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecognizer(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpProperties
    _iid_ = Guid('{c2b5f241-daa0-4507-9e16-5a1eaa2b7a5c}')
    @commethod(7)
    def SetRecognizer(self, pRecognizer: win32more.Windows.Win32.Media.Speech.ISpObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecognizer(self, ppRecognizer: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetInput(self, pUnkInput: win32more.Windows.Win32.System.Com.IUnknown, fAllowFormatChanges: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInputObjectToken(self, ppToken: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInputStream(self, ppStream: POINTER(win32more.Windows.Win32.Media.Speech.ISpStreamFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateRecoContext(self, ppNewCtxt: POINTER(win32more.Windows.Win32.Media.Speech.ISpRecoContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecoProfile(self, ppToken: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetRecoProfile(self, pToken: win32more.Windows.Win32.Media.Speech.ISpObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsSharedInstance(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecoState(self, pState: POINTER(win32more.Windows.Win32.Media.Speech.SPRECOSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetRecoState(self, NewState: win32more.Windows.Win32.Media.Speech.SPRECOSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStatus(self, pStatus: POINTER(win32more.Windows.Win32.Media.Speech.SPRECOGNIZERSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFormat(self, WaveFormatType: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMATTYPE, pFormatId: POINTER(Guid), ppCoMemWFEX: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def IsUISupported(self, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32, pfSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DisplayUI(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EmulateRecognition(self, pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhrase) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRecognizer2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fc6d974-c81e-4098-93c5-0147f61ed4d3}')
    @commethod(3)
    def EmulateRecognitionEx(self, pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhrase, dwCompareFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTrainingState(self, fDoingTraining: win32more.Windows.Win32.Foundation.BOOL, fAdaptFromTrainingData: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ResetAcousticModelAdaptation(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpRegDataKey(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpDataKey
    _iid_ = Guid('{92a66e2b-c830-4149-83df-6fc2ba1e7a5b}')
    @commethod(15)
    def SetKey(self, hkey: win32more.Windows.Win32.System.Registry.HKEY, fReadOnly: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpResourceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IServiceProvider
    _iid_ = Guid('{93384e18-5014-43d5-adbb-a78e055926bd}')
    @commethod(4)
    def SetObject(self, guidServiceId: POINTER(Guid), pUnkObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObject(self, guidServiceId: POINTER(Guid), ObjectCLSID: POINTER(Guid), ObjectIID: POINTER(Guid), fReleaseWhenLastExternalRefReleased: win32more.Windows.Win32.Foundation.BOOL, ppObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpSRAlternates(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fece8294-2be1-408f-8e68-2de377092f0e}')
    @commethod(3)
    def GetAlternates(self, pAltRequest: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEALTREQUEST), ppAlts: POINTER(POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEALT)), pcAlts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Commit(self, pAltRequest: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEALTREQUEST), pAlt: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEALT), ppvResultExtra: POINTER(VoidPtr), pcbResultExtra: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpSRAlternates2(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpSRAlternates
    _iid_ = Guid('{f338f437-cb33-4020-9cab-c71ff9ce12d3}')
    @commethod(5)
    def CommitText(self, pAltRequest: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEALTREQUEST), pcszNewText: win32more.Windows.Win32.Foundation.PWSTR, commitFlags: win32more.Windows.Win32.Media.Speech.SPCOMMITFLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpSREngine(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f472991-854b-4465-b613-fbafb3ad8ed8}')
    @commethod(3)
    def SetSite(self, pSite: win32more.Windows.Win32.Media.Speech.ISpSREngineSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInputAudioFormat(self, pguidSourceFormatId: POINTER(Guid), pSourceWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pguidDesiredFormatId: POINTER(Guid), ppCoMemDesiredWaveFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RecognizeStream(self, rguidFmtId: POINTER(Guid), pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), hRequestSync: win32more.Windows.Win32.Foundation.HANDLE, hDataAvailable: win32more.Windows.Win32.Foundation.HANDLE, hExit: win32more.Windows.Win32.Foundation.HANDLE, fNewAudioStream: win32more.Windows.Win32.Foundation.BOOL, fRealTimeAudio: win32more.Windows.Win32.Foundation.BOOL, pAudioObjectToken: win32more.Windows.Win32.Media.Speech.ISpObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRecoProfile(self, pProfile: win32more.Windows.Win32.Media.Speech.ISpObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnCreateGrammar(self, pvEngineRecoContext: VoidPtr, hSAPIGrammar: win32more.Windows.Win32.Media.Speech.SPGRAMMARHANDLE, ppvEngineGrammarContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnDeleteGrammar(self, pvEngineGrammar: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def LoadProprietaryGrammar(self, pvEngineGrammar: VoidPtr, rguidParam: POINTER(Guid), pszStringParam: win32more.Windows.Win32.Foundation.PWSTR, pvDataParam: VoidPtr, ulDataSize: UInt32, Options: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnloadProprietaryGrammar(self, pvEngineGrammar: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetProprietaryRuleState(self, pvEngineGrammar: VoidPtr, pszName: win32more.Windows.Win32.Foundation.PWSTR, pReserved: VoidPtr, NewState: win32more.Windows.Win32.Media.Speech.SPRULESTATE, pcRulesChanged: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetProprietaryRuleIdState(self, pvEngineGrammar: VoidPtr, dwRuleId: UInt32, NewState: win32more.Windows.Win32.Media.Speech.SPRULESTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def LoadSLM(self, pvEngineGrammar: VoidPtr, pszTopicName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnloadSLM(self, pvEngineGrammar: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetSLMState(self, pvEngineGrammar: VoidPtr, NewState: win32more.Windows.Win32.Media.Speech.SPRULESTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetWordSequenceData(self, pvEngineGrammar: VoidPtr, pText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32, pInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTextSelection(self, pvEngineGrammar: VoidPtr, pInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPTEXTSELECTIONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def IsPronounceable(self, pvEngineGrammar: VoidPtr, pszWord: win32more.Windows.Win32.Foundation.PWSTR, pWordPronounceable: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDPRONOUNCEABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def OnCreateRecoContext(self, hSAPIRecoContext: win32more.Windows.Win32.Media.Speech.SPRECOCONTEXTHANDLE, ppvEngineContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnDeleteRecoContext(self, pvEngineContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def PrivateCall(self, pvEngineContext: VoidPtr, pCallFrame: VoidPtr, ulCallFrameSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetAdaptationData(self, pvEngineContext: VoidPtr, pAdaptationData: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetPropertyNum(self, eSrc: win32more.Windows.Win32.Media.Speech.SPPROPSRC, pvSrcObj: VoidPtr, pName: win32more.Windows.Win32.Foundation.PWSTR, lValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetPropertyNum(self, eSrc: win32more.Windows.Win32.Media.Speech.SPPROPSRC, pvSrcObj: VoidPtr, pName: win32more.Windows.Win32.Foundation.PWSTR, lValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetPropertyString(self, eSrc: win32more.Windows.Win32.Media.Speech.SPPROPSRC, pvSrcObj: VoidPtr, pName: win32more.Windows.Win32.Foundation.PWSTR, pValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetPropertyString(self, eSrc: win32more.Windows.Win32.Media.Speech.SPPROPSRC, pvSrcObj: VoidPtr, pName: win32more.Windows.Win32.Foundation.PWSTR, ppCoMemValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetGrammarState(self, pvEngineGrammar: VoidPtr, eGrammarState: win32more.Windows.Win32.Media.Speech.SPGRAMMARSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def WordNotify(self, Action: win32more.Windows.Win32.Media.Speech.SPCFGNOTIFY, cWords: UInt32, pWords: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def RuleNotify(self, Action: win32more.Windows.Win32.Media.Speech.SPCFGNOTIFY, cRules: UInt32, pRules: POINTER(win32more.Windows.Win32.Media.Speech.SPRULEENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def PrivateCallEx(self, pvEngineContext: VoidPtr, pInCallFrame: VoidPtr, ulInCallFrameSize: UInt32, ppvCoMemResponse: POINTER(VoidPtr), pulResponseSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetContextState(self, pvEngineContext: VoidPtr, eContextState: win32more.Windows.Win32.Media.Speech.SPCONTEXTSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpSREngine2(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpSREngine
    _iid_ = Guid('{7ba627d8-33f9-4375-90c5-9985aee5ede5}')
    @commethod(32)
    def PrivateCallImmediate(self, pvEngineContext: VoidPtr, pInCallFrame: VoidPtr, ulInCallFrameSize: UInt32, ppvCoMemResponse: POINTER(VoidPtr), pulResponseSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetAdaptationData2(self, pvEngineContext: VoidPtr, pAdaptationData: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pTopicName: win32more.Windows.Win32.Foundation.PWSTR, eSettings: win32more.Windows.Win32.Media.Speech.SPADAPTATIONSETTINGS, eRelevance: win32more.Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetGrammarPrefix(self, pvEngineGrammar: VoidPtr, pszPrefix: win32more.Windows.Win32.Foundation.PWSTR, fIsPrefixRequired: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetRulePriority(self, hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE, pvClientRuleContext: VoidPtr, nRulePriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def EmulateRecognition(self, pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhrase, dwCompareFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetSLMWeight(self, pvEngineGrammar: VoidPtr, flWeight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetRuleWeight(self, hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE, pvClientRuleContext: VoidPtr, flWeight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetTrainingState(self, fDoingTraining: win32more.Windows.Win32.Foundation.BOOL, fAdaptFromTrainingData: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def ResetAcousticModelAdaptation(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def OnLoadCFG(self, pvEngineGrammar: VoidPtr, pGrammarData: POINTER(win32more.Windows.Win32.Media.Speech.SPBINARYGRAMMAR), ulGrammarID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def OnUnloadCFG(self, pvEngineGrammar: VoidPtr, ulGrammarID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpSREngineSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3b414aec-720c-4883-b9ef-178cd394fb3a}')
    @commethod(3)
    def Read(self, pv: VoidPtr, cb: UInt32, pcbRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DataAvailable(self, pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetBufferNotifySize(self, cbSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ParseFromTransitions(self, pParseInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPPARSEINFO), ppNewPhrase: POINTER(win32more.Windows.Win32.Media.Speech.ISpPhraseBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Recognition(self, pResultInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPRECORESULTINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddEvent(self, pEvent: POINTER(win32more.Windows.Win32.Media.Speech.SPEVENT), hSAPIRecoContext: win32more.Windows.Win32.Media.Speech.SPRECOCONTEXTHANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Synchronize(self, ullProcessedThruPos: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetWordInfo(self, pWordEntry: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDENTRY), Options: win32more.Windows.Win32.Media.Speech.SPWORDINFOOPT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetWordClientContext(self, hWord: win32more.Windows.Win32.Media.Speech.SPWORDHANDLE, pvClientContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRuleInfo(self, pRuleEntry: POINTER(win32more.Windows.Win32.Media.Speech.SPRULEENTRY), Options: win32more.Windows.Win32.Media.Speech.SPRULEINFOOPT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetRuleClientContext(self, hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE, pvClientContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStateInfo(self, hState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE, pStateInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPSTATEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetResource(self, hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE, pszResourceName: win32more.Windows.Win32.Foundation.PWSTR, ppCoMemResource: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTransitionProperty(self, ID: win32more.Windows.Win32.Media.Speech.SPTRANSITIONID, ppCoMemProperty: POINTER(POINTER(win32more.Windows.Win32.Media.Speech.SPTRANSITIONPROPERTY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def IsAlternate(self, hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE, hAltRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetMaxAlternates(self, hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE, pulNumAlts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetContextMaxAlternates(self, hContext: win32more.Windows.Win32.Media.Speech.SPRECOCONTEXTHANDLE, pulNumAlts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def UpdateRecoPos(self, ullCurrentRecoPos: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpSREngineSite2(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpSREngineSite
    _iid_ = Guid('{7bc6e012-684a-493e-bdd4-2bf5fbf48cfe}')
    @commethod(21)
    def AddEventEx(self, pEvent: POINTER(win32more.Windows.Win32.Media.Speech.SPEVENTEX), hSAPIRecoContext: win32more.Windows.Win32.Media.Speech.SPRECOCONTEXTHANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def UpdateRecoPosEx(self, ullCurrentRecoPos: UInt64, ullCurrentRecoTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRuleTransition(self, ulGrammarID: UInt32, RuleIndex: UInt32, pTrans: POINTER(win32more.Windows.Win32.Media.Speech.SPTRANSITIONENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def RecognitionEx(self, pResultInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPRECORESULTINFOEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpSerializeState(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{21b501a0-0ec7-46c9-92c3-a2bc784c54b9}')
    @commethod(3)
    def GetSerializedState(self, ppbData: POINTER(POINTER(Byte)), pulSize: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSerializedState(self, pbData: POINTER(Byte), ulSize: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpShortcut(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3df681e2-ea56-11d9-8bde-f66bad1e3f3a}')
    @commethod(3)
    def AddShortcut(self, pszDisplay: win32more.Windows.Win32.Foundation.PWSTR, LangID: UInt16, pszSpoken: win32more.Windows.Win32.Foundation.PWSTR, shType: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveShortcut(self, pszDisplay: win32more.Windows.Win32.Foundation.PWSTR, LangID: UInt16, pszSpoken: win32more.Windows.Win32.Foundation.PWSTR, shType: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetShortcuts(self, LangID: UInt16, pShortcutpairList: POINTER(win32more.Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGeneration(self, pdwGeneration: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetWordsFromGenerationChange(self, pdwGeneration: POINTER(UInt32), pWordList: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(self, pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pWordList: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetShortcutsForGeneration(self, pdwGeneration: POINTER(UInt32), pdwCookie: POINTER(UInt32), pShortcutpairList: POINTER(win32more.Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGenerationChange(self, pdwGeneration: POINTER(UInt32), pShortcutpairList: POINTER(win32more.Windows.Win32.Media.Speech.SPSHORTCUTPAIRLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpStream(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpStreamFormat
    _iid_ = Guid('{12e3cca9-7518-44c5-a5e7-ba5a79cb929e}')
    @commethod(15)
    def SetBaseStream(self, pStream: win32more.Windows.Win32.System.Com.IStream, rguidFormat: POINTER(Guid), pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetBaseStream(self, ppStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def BindToFile(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, eMode: win32more.Windows.Win32.Media.Speech.SPFILEMODE, pFormatId: POINTER(Guid), pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), ullEventInterest: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpStreamFormat(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IStream
    _iid_ = Guid('{bed530be-2606-4f4d-a1c0-54c5cda5566f}')
    @commethod(14)
    def GetFormat(self, pguidFormatId: POINTER(Guid), ppCoMemWaveFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpStreamFormatConverter(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpStreamFormat
    _iid_ = Guid('{678a932c-ea71-4446-9b41-78fda6280a29}')
    @commethod(15)
    def SetBaseStream(self, pStream: win32more.Windows.Win32.Media.Speech.ISpStreamFormat, fSetFormatToBaseStreamFormat: win32more.Windows.Win32.Foundation.BOOL, fWriteToBaseStream: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetBaseStream(self, ppStream: POINTER(win32more.Windows.Win32.Media.Speech.ISpStreamFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetFormat(self, rguidFormatIdOfConvertedStream: POINTER(Guid), pWaveFormatExOfConvertedStream: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ResetSeekPosition(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ScaleConvertedToBaseOffset(self, ullOffsetConvertedStream: UInt64, pullOffsetBaseStream: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ScaleBaseToConvertedOffset(self, ullOffsetBaseStream: UInt64, pullOffsetConvertedStream: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpTTSEngine(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a74d7c8e-4cc5-4f2f-a6eb-804dee18500e}')
    @commethod(3)
    def Speak(self, dwSpeakFlags: UInt32, rguidFormatId: POINTER(Guid), pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pTextFragList: POINTER(win32more.Windows.Win32.Media.Speech.SPVTEXTFRAG), pOutputSite: win32more.Windows.Win32.Media.Speech.ISpTTSEngineSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputFormat(self, pTargetFmtId: POINTER(Guid), pTargetWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pOutputFormatId: POINTER(Guid), ppCoMemOutputWaveFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpTTSEngineSite(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpEventSink
    _iid_ = Guid('{9880499b-cce9-11d2-b503-00c04f797396}')
    @commethod(5)
    def GetActions(self) -> UInt32: ...
    @commethod(6)
    def Write(self, pBuff: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRate(self, pRateAdjust: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVolume(self, pusVolume: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSkipInfo(self, peType: POINTER(win32more.Windows.Win32.Media.Speech.SPVSKIPTYPE), plNumItems: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CompleteSkip(self, ulNumSkipped: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpTask(ComPtr):
    extends: None
    @commethod(0)
    def Execute(self, pvTaskData: VoidPtr, pfContinueProcessing: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpTaskManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2baeef81-2ca3-4331-98f3-26ec5abefb03}')
    @commethod(3)
    def SetThreadPoolInfo(self, pPoolInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPTMTHREADINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetThreadPoolInfo(self, pPoolInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPTMTHREADINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueueTask(self, pTask: win32more.Windows.Win32.Media.Speech.ISpTask, pvTaskData: VoidPtr, hCompEvent: win32more.Windows.Win32.Foundation.HANDLE, pdwGroupId: POINTER(UInt32), pTaskID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateReoccurringTask(self, pTask: win32more.Windows.Win32.Media.Speech.ISpTask, pvTaskData: VoidPtr, hCompEvent: win32more.Windows.Win32.Foundation.HANDLE, ppTaskCtrl: POINTER(win32more.Windows.Win32.Media.Speech.ISpNotifySink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateThreadControl(self, pTask: win32more.Windows.Win32.Media.Speech.ISpThreadTask, pvTaskData: VoidPtr, nPriority: Int32, ppTaskCtrl: POINTER(win32more.Windows.Win32.Media.Speech.ISpThreadControl)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def TerminateTask(self, dwTaskId: UInt32, ulWaitPeriod: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def TerminateTaskGroup(self, dwGroupId: UInt32, ulWaitPeriod: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpThreadControl(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpNotifySink
    _iid_ = Guid('{a6be4d73-4403-4358-b22d-0346e23b1764}')
    @commethod(4)
    def StartThread(self, dwFlags: UInt32, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WaitForThreadDone(self, fForceStop: win32more.Windows.Win32.Foundation.BOOL, phrThreadResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT), msTimeOut: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TerminateThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ThreadHandle(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
    @commethod(8)
    def ThreadId(self) -> UInt32: ...
    @commethod(9)
    def NotifyEvent(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
    @commethod(10)
    def WindowHandle(self) -> win32more.Windows.Win32.Foundation.HWND: ...
    @commethod(11)
    def ThreadCompleteEvent(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
    @commethod(12)
    def ExitThreadEvent(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
class ISpThreadTask(ComPtr):
    extends: None
    @commethod(0)
    def InitThread(self, pvTaskData: VoidPtr, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(1)
    def ThreadProc(self, pvTaskData: VoidPtr, hExitThreadEvent: win32more.Windows.Win32.Foundation.HANDLE, hNotifyEvent: win32more.Windows.Win32.Foundation.HANDLE, hwndWorker: win32more.Windows.Win32.Foundation.HWND, pfContinueProcessing: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(2)
    def WindowMessage(self, pvTaskData: VoidPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
class ISpTokenUI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f8e690f0-39cb-4843-b8d7-c84696e1119d}')
    @commethod(3)
    def IsUISupported(self, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32, punkObject: win32more.Windows.Win32.System.Com.IUnknown, pfSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisplayUI(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32, pToken: win32more.Windows.Win32.Media.Speech.ISpObjectToken, punkObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpTranscript(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10f63bce-201a-11d3-ac70-00c04f8ee6c0}')
    @commethod(3)
    def GetTranscript(self, ppszTranscript: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AppendTranscript(self, pszTranscript: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpVoice(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpEventSource
    _iid_ = Guid('{6c44df74-72b9-4992-a1ec-ef996e0422d4}')
    @commethod(13)
    def SetOutput(self, pUnkOutput: win32more.Windows.Win32.System.Com.IUnknown, fAllowFormatChanges: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetOutputObjectToken(self, ppObjectToken: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetOutputStream(self, ppStream: POINTER(win32more.Windows.Win32.Media.Speech.ISpStreamFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetVoice(self, pToken: win32more.Windows.Win32.Media.Speech.ISpObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetVoice(self, ppToken: POINTER(win32more.Windows.Win32.Media.Speech.ISpObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Speak(self, pwcs: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SpeakStream(self, pStream: win32more.Windows.Win32.System.Com.IStream, dwFlags: UInt32, pulStreamNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetStatus(self, pStatus: POINTER(win32more.Windows.Win32.Media.Speech.SPVOICESTATUS), ppszLastBookmark: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Skip(self, pItemType: win32more.Windows.Win32.Foundation.PWSTR, lNumItems: Int32, pulNumSkipped: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetPriority(self, ePriority: win32more.Windows.Win32.Media.Speech.SPVPRIORITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPriority(self, pePriority: POINTER(win32more.Windows.Win32.Media.Speech.SPVPRIORITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetAlertBoundary(self, eBoundary: win32more.Windows.Win32.Media.Speech.SPEVENTENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetAlertBoundary(self, peBoundary: POINTER(win32more.Windows.Win32.Media.Speech.SPEVENTENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetRate(self, RateAdjust: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetRate(self, pRateAdjust: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetVolume(self, usVolume: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetVolume(self, pusVolume: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def WaitUntilDone(self, msTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetSyncSpeakTimeout(self, msTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetSyncSpeakTimeout(self, pmsTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SpeakCompleteEvent(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
    @commethod(36)
    def IsUISupported(self, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32, pfSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def DisplayUI(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszTypeOfUI: win32more.Windows.Win32.Foundation.PWSTR, pvExtraData: VoidPtr, cbExtraData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpXMLRecoResult(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpRecoResult
    _iid_ = Guid('{ae39362b-45a8-4074-9b9e-ccf49aa2d0b6}')
    @commethod(14)
    def GetXMLResult(self, ppszCoMemXMLResult: POINTER(win32more.Windows.Win32.Foundation.PWSTR), Options: win32more.Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetXMLErrorInfo(self, pSemanticErrorInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPSEMANTICERRORINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudio(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{cff8e175-019e-11d3-a08e-00c04f8ef9b5}')
    @commethod(12)
    def get_Status(self, Status: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_BufferInfo(self, BufferInfo: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioBufferInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_DefaultFormat(self, StreamFormat: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Volume(self, Volume: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Volume(self, Volume: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BufferNotifySize(self, BufferNotifySize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BufferNotifySize(self, BufferNotifySize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EventHandle(self, EventHandle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetState(self, State: win32more.Windows.Win32.Media.Speech.SpeechAudioState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioBufferInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{11b103d8-1142-4edf-a093-82fb3915f8cc}')
    @commethod(7)
    def get_MinNotification(self, MinNotification: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_MinNotification(self, MinNotification: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BufferSize(self, BufferSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_BufferSize(self, BufferSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_EventBias(self, EventBias: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_EventBias(self, EventBias: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioFormat(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e6e9c590-3e18-40e3-8299-061f98bde7c7}')
    @commethod(7)
    def get_Type(self, AudioFormat: POINTER(win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Type(self, AudioFormat: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Guid(self, Guid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Guid(self, Guid: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetWaveFormatEx(self, SpeechWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechWaveFormatEx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetWaveFormatEx(self, SpeechWaveFormatEx: win32more.Windows.Win32.Media.Speech.ISpeechWaveFormatEx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechAudioStatus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c62d9c91-7458-47f6-862d-1ef86fb0b278}')
    @commethod(7)
    def get_FreeBufferSpace(self, FreeBufferSpace: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_NonBlockingIO(self, NonBlockingIO: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_State(self, State: POINTER(win32more.Windows.Win32.Media.Speech.SpeechAudioState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentSeekPosition(self, CurrentSeekPosition: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentDevicePosition(self, CurrentDevicePosition: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechBaseStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6450336f-7d49-4ced-8097-49d6dee37294}')
    @commethod(7)
    def get_Format(self, AudioFormat: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def putref_Format(self, AudioFormat: win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Read(self, Buffer: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), NumberOfBytes: Int32, BytesRead: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Write(self, Buffer: win32more.Windows.Win32.System.Variant.VARIANT, BytesWritten: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Seek(self, Position: win32more.Windows.Win32.System.Variant.VARIANT, Origin: win32more.Windows.Win32.Media.Speech.SpeechStreamSeekPositionType, NewPosition: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechCustomStream(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{1a9e9f4f-104f-4db8-a115-efd7fd0c97ae}')
    @commethod(12)
    def get_BaseStream(self, ppUnkStream: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_BaseStream(self, pUnkStream: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechDataKey(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ce17c09b-4efa-44d5-a4c9-59d9585ab0cd}')
    @commethod(7)
    def SetBinaryValue(self, ValueName: win32more.Windows.Win32.Foundation.BSTR, Value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBinaryValue(self, ValueName: win32more.Windows.Win32.Foundation.BSTR, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetStringValue(self, ValueName: win32more.Windows.Win32.Foundation.BSTR, Value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStringValue(self, ValueName: win32more.Windows.Win32.Foundation.BSTR, Value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLongValue(self, ValueName: win32more.Windows.Win32.Foundation.BSTR, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLongValue(self, ValueName: win32more.Windows.Win32.Foundation.BSTR, Value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OpenKey(self, SubKeyName: win32more.Windows.Win32.Foundation.BSTR, SubKey: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechDataKey)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateKey(self, SubKeyName: win32more.Windows.Win32.Foundation.BSTR, SubKey: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechDataKey)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def DeleteKey(self, SubKeyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteValue(self, ValueName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumKeys(self, Index: Int32, SubKeyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumValues(self, Index: Int32, ValueName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechFileStream(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{af67f125-ab39-4e93-b4a2-cc2e66e182a7}')
    @commethod(12)
    def Open(self, FileName: win32more.Windows.Win32.Foundation.BSTR, FileMode: win32more.Windows.Win32.Media.Speech.SpeechStreamFileMode, DoEvents: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRule(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{afe719cf-5dd1-44f2-999c-7a399f1cfccc}')
    @commethod(7)
    def get_Attributes(self, Attributes: POINTER(win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_InitialState(self, State: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(self, Id: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddResource(self, ResourceName: win32more.Windows.Win32.Foundation.BSTR, ResourceValue: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddState(self, State: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleState(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d4286f2c-ee67-45ae-b928-28d695362eda}')
    @commethod(7)
    def get_Rule(self, Rule: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Transitions(self, Transitions: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleStateTransitions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddWordTransition(self, DestState: win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleState, Words: win32more.Windows.Win32.Foundation.BSTR, Separators: win32more.Windows.Win32.Foundation.BSTR, Type: win32more.Windows.Win32.Media.Speech.SpeechGrammarWordType, PropertyName: win32more.Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Weight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddRuleTransition(self, DestinationState: win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleState, Rule: win32more.Windows.Win32.Media.Speech.ISpeechGrammarRule, PropertyName: win32more.Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Weight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddSpecialTransition(self, DestinationState: win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleState, Type: win32more.Windows.Win32.Media.Speech.SpeechSpecialTransitionType, PropertyName: win32more.Windows.Win32.Foundation.BSTR, PropertyId: Int32, PropertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Weight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleStateTransition(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafd1db1-41d1-4a06-9863-e2e81da17a9a}')
    @commethod(7)
    def get_Type(self, Type: POINTER(win32more.Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Text(self, Text: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Rule(self, Rule: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Weight(self, Weight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PropertyName(self, PropertyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PropertyId(self, PropertyId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PropertyValue(self, PropertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NextState(self, NextState: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRuleStateTransitions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{eabce657-75bc-44a2-aa7f-c56476742963}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Transition: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRuleStateTransition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechGrammarRules(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6ffa3b44-fc2d-40d1-8afc-32911c7f1ad1}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindRule(self, RuleNameOrId: win32more.Windows.Win32.System.Variant.VARIANT, Rule: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, Index: Int32, Rule: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Dynamic(self, Dynamic: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Add(self, RuleName: win32more.Windows.Win32.Foundation.BSTR, Attributes: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes, RuleId: Int32, Rule: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CommitAndSave(self, ErrorText: POINTER(win32more.Windows.Win32.Foundation.BSTR), SaveStream: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexicon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3da7627a-c7ae-4b23-8708-638c50362c25}')
    @commethod(7)
    def get_GenerationId(self, GenerationId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(self, Flags: win32more.Windows.Win32.Media.Speech.SpeechLexiconType, GenerationID: POINTER(Int32), Words: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechLexiconWords)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddPronunciation(self, bstrWord: win32more.Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech, bstrPronunciation: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddPronunciationByPhoneIds(self, bstrWord: win32more.Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech, PhoneIds: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemovePronunciation(self, bstrWord: win32more.Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech, bstrPronunciation: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemovePronunciationByPhoneIds(self, bstrWord: win32more.Windows.Win32.Foundation.BSTR, LangId: Int32, PartOfSpeech: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech, PhoneIds: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPronunciations(self, bstrWord: win32more.Windows.Win32.Foundation.BSTR, LangId: Int32, TypeFlags: win32more.Windows.Win32.Media.Speech.SpeechLexiconType, ppPronunciations: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechLexiconPronunciations)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetGenerationChange(self, GenerationID: POINTER(Int32), ppWords: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechLexiconWords)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconPronunciation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{95252c5d-9e43-4f4a-9899-48ee73352f9f}')
    @commethod(7)
    def get_Type(self, LexiconType: POINTER(win32more.Windows.Win32.Media.Speech.SpeechLexiconType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LangId(self, LangId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PartOfSpeech(self, PartOfSpeech: POINTER(win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PhoneIds(self, PhoneIds: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Symbolic(self, Symbolic: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconPronunciations(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{72829128-5682-4704-a0d4-3e2bb6f2ead3}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Pronunciation: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechLexiconPronunciation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconWord(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4e5b933c-c9be-48ed-8842-1ee51bb1d4ff}')
    @commethod(7)
    def get_LangId(self, LangId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Type(self, WordType: POINTER(win32more.Windows.Win32.Media.Speech.SpeechWordType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Word(self, Word: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Pronunciations(self, Pronunciations: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechLexiconPronunciations)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechLexiconWords(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8d199862-415e-47d5-ac4f-faa608b424e6}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Word: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechLexiconWord)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechMMSysAudio(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpeechAudio
    _iid_ = Guid('{3c76af6d-1fd7-4831-81d1-3b71d5a13c44}')
    @commethod(21)
    def get_DeviceId(self, DeviceId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DeviceId(self, DeviceId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LineId(self, LineId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_LineId(self, LineId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MMHandle(self, Handle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechMemoryStream(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpeechBaseStream
    _iid_ = Guid('{eeb14b68-808b-4abe-a5ea-b51da7588008}')
    @commethod(12)
    def SetData(self, Data: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetData(self, pData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectToken(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c74a3adc-b727-4500-a84a-b526721c8b8c}')
    @commethod(7)
    def get_Id(self, ObjectId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DataKey(self, DataKey: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechDataKey)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Category(self, Category: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectTokenCategory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDescription(self, Locale: Int32, Description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetId(self, Id: win32more.Windows.Win32.Foundation.BSTR, CategoryID: win32more.Windows.Win32.Foundation.BSTR, CreateIfNotExist: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAttribute(self, AttributeName: win32more.Windows.Win32.Foundation.BSTR, AttributeValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateInstance(self, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, ClsContext: win32more.Windows.Win32.Media.Speech.SpeechTokenContext, Object: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Remove(self, ObjectStorageCLSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStorageFileName(self, ObjectStorageCLSID: win32more.Windows.Win32.Foundation.BSTR, KeyName: win32more.Windows.Win32.Foundation.BSTR, FileName: win32more.Windows.Win32.Foundation.BSTR, Folder: win32more.Windows.Win32.Media.Speech.SpeechTokenShellFolder, FilePath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveStorageFileName(self, ObjectStorageCLSID: win32more.Windows.Win32.Foundation.BSTR, KeyName: win32more.Windows.Win32.Foundation.BSTR, DeleteFile: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def IsUISupported(self, TypeOfUI: win32more.Windows.Win32.Foundation.BSTR, ExtraData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Object: win32more.Windows.Win32.System.Com.IUnknown, Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DisplayUI(self, hWnd: Int32, Title: win32more.Windows.Win32.Foundation.BSTR, TypeOfUI: win32more.Windows.Win32.Foundation.BSTR, ExtraData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Object: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def MatchesAttributes(self, Attributes: win32more.Windows.Win32.Foundation.BSTR, Matches: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectTokenCategory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ca7eac50-2d01-4145-86d4-5ae7d70f4469}')
    @commethod(7)
    def get_Id(self, Id: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Default(self, TokenId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Default(self, TokenId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetId(self, Id: win32more.Windows.Win32.Foundation.BSTR, CreateIfNotExist: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDataKey(self, Location: win32more.Windows.Win32.Media.Speech.SpeechDataKeyLocation, DataKey: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechDataKey)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumerateTokens(self, RequiredAttributes: win32more.Windows.Win32.Foundation.BSTR, OptionalAttributes: win32more.Windows.Win32.Foundation.BSTR, Tokens: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechObjectTokens(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9285b776-2e7b-4bc0-b53e-580eb6fa967f}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Token: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhoneConverter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c3e4f353-433f-43d6-89a1-6a62a7054c3d}')
    @commethod(7)
    def get_LanguageId(self, LanguageId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LanguageId(self, LanguageId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PhoneToId(self, Phonemes: win32more.Windows.Win32.Foundation.BSTR, IdArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IdToPhone(self, IdArray: win32more.Windows.Win32.System.Variant.VARIANT, Phonemes: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseAlternate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27864a2a-2b9f-4cb8-92d3-0d2722fd1e73}')
    @commethod(7)
    def get_RecoResult(self, RecoResult: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_StartElementInResult(self, StartElement: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NumberOfElementsInResult(self, NumberOfElements: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PhraseInfo(self, PhraseInfo: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseAlternates(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b238b6d5-f276-4c3d-a6c1-2974801c3cc2}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, PhraseAlternate: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseAlternate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseElement(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e6176f96-e373-4801-b223-3b62c068c0b4}')
    @commethod(7)
    def get_AudioTimeOffset(self, AudioTimeOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AudioSizeTime(self, AudioSizeTime: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AudioStreamOffset(self, AudioStreamOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioSizeBytes(self, AudioSizeBytes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RetainedStreamOffset(self, RetainedStreamOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RetainedSizeBytes(self, RetainedSizeBytes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisplayText(self, DisplayText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_LexicalForm(self, LexicalForm: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Pronunciation(self, Pronunciation: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_DisplayAttributes(self, DisplayAttributes: POINTER(win32more.Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RequiredConfidence(self, RequiredConfidence: POINTER(win32more.Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ActualConfidence(self, ActualConfidence: POINTER(win32more.Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EngineConfidence(self, EngineConfidence: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseElements(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0626b328-3478-467d-a0b3-d0853b93dda3}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Element: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{961559cf-4e67-4662-8bf0-d93f1fcd61b3}')
    @commethod(7)
    def get_LanguageId(self, LanguageId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GrammarId(self, GrammarId: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StartTime(self, StartTime: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioStreamPosition(self, AudioStreamPosition: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AudioSizeBytes(self, pAudioSizeBytes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RetainedSizeBytes(self, RetainedSizeBytes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AudioSizeTime(self, AudioSizeTime: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Rule(self, Rule: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Properties(self, Properties: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Elements(self, Elements: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseElements)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Replacements(self, Replacements: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseReplacements)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_EngineId(self, EngineIdGuid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EnginePrivateData(self, PrivateData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SaveToMemory(self, PhraseBlock: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetText(self, StartElement: Int32, Elements: Int32, UseReplacements: win32more.Windows.Win32.Foundation.VARIANT_BOOL, Text: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetDisplayAttributes(self, StartElement: Int32, Elements: Int32, UseReplacements: win32more.Windows.Win32.Foundation.VARIANT_BOOL, DisplayAttributes: POINTER(win32more.Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseInfoBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3b151836-df3a-4e0a-846c-d2adc9334333}')
    @commethod(7)
    def RestorePhraseFromMemory(self, PhraseInMemory: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), PhraseInfo: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{08166b47-102e-4b23-a599-bdb98dbfd1f4}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Property: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ce563d48-961e-4732-a2e1-378a42b430be}')
    @commethod(7)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, Id: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(self, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FirstElement(self, FirstElement: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_NumberOfElements(self, NumberOfElements: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_EngineConfidence(self, Confidence: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Confidence(self, Confidence: POINTER(win32more.Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Parent(self, ParentProperty: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Children(self, Children: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseReplacement(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2890a410-53a7-4fb5-94ec-06d4998e3d02}')
    @commethod(7)
    def get_DisplayAttributes(self, DisplayAttributes: POINTER(win32more.Windows.Win32.Media.Speech.SpeechDisplayAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Text(self, Text: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FirstElement(self, FirstElement: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfElements(self, NumberOfElements: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseReplacements(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{38bc662f-2257-4525-959e-2069d2596c05}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Reps: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseReplacement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseRule(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a7bfe112-a4a0-48d9-b602-c313843f6964}')
    @commethod(7)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, Id: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FirstElement(self, FirstElement: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfElements(self, NumberOfElements: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Parent(self, Parent: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Children(self, Children: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseRules)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Confidence(self, ActualConfidence: POINTER(win32more.Windows.Win32.Media.Speech.SpeechEngineConfidence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_EngineConfidence(self, EngineConfidence: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechPhraseRules(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9047d593-01dd-4b72-81a3-e4a0ca69f407}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Rule: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, EnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{580aa49d-7e1e-4809-b8e2-57da806104b8}')
    @commethod(7)
    def get_Recognizer(self, Recognizer: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecognizer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AudioInputInterferenceStatus(self, Interference: POINTER(win32more.Windows.Win32.Media.Speech.SpeechInterference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_RequestedUIType(self, UIType: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def putref_Voice(self, Voice: win32more.Windows.Win32.Media.Speech.ISpeechVoice) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Voice(self, Voice: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechVoice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowVoiceFormatMatchingOnNextSet(self, Allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowVoiceFormatMatchingOnNextSet(self, pAllow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_VoicePurgeEvent(self, EventInterest: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_VoicePurgeEvent(self, EventInterest: POINTER(win32more.Windows.Win32.Media.Speech.SpeechRecoEvents)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EventInterests(self, EventInterest: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_EventInterests(self, EventInterest: POINTER(win32more.Windows.Win32.Media.Speech.SpeechRecoEvents)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_CmdMaxAlternates(self, MaxAlternates: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CmdMaxAlternates(self, MaxAlternates: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_State(self, State: win32more.Windows.Win32.Media.Speech.SpeechRecoContextState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_State(self, State: POINTER(win32more.Windows.Win32.Media.Speech.SpeechRecoContextState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_RetainedAudio(self, Option: win32more.Windows.Win32.Media.Speech.SpeechRetainedAudioOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RetainedAudio(self, Option: POINTER(win32more.Windows.Win32.Media.Speech.SpeechRetainedAudioOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def putref_RetainedAudioFormat(self, Format: win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_RetainedAudioFormat(self, Format: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreateGrammar(self, GrammarId: win32more.Windows.Win32.System.Variant.VARIANT, Grammar: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoGrammar)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateResultFromMemory(self, ResultBlock: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Result: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Bookmark(self, Options: win32more.Windows.Win32.Media.Speech.SpeechBookmarkOptions, StreamPos: win32more.Windows.Win32.System.Variant.VARIANT, BookmarkId: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetAdaptationData(self, AdaptationString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoGrammar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b6d6f79f-2158-4e50-b5bc-9a9ccd852a09}')
    @commethod(7)
    def get_Id(self, Id: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RecoContext(self, RecoContext: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_State(self, State: win32more.Windows.Win32.Media.Speech.SpeechGrammarState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(self, State: POINTER(win32more.Windows.Win32.Media.Speech.SpeechGrammarState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Rules(self, Rules: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechGrammarRules)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Reset(self, NewLanguage: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CmdLoadFromFile(self, FileName: win32more.Windows.Win32.Foundation.BSTR, LoadOption: win32more.Windows.Win32.Media.Speech.SpeechLoadOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CmdLoadFromObject(self, ClassId: win32more.Windows.Win32.Foundation.BSTR, GrammarName: win32more.Windows.Win32.Foundation.BSTR, LoadOption: win32more.Windows.Win32.Media.Speech.SpeechLoadOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CmdLoadFromResource(self, hModule: Int32, ResourceName: win32more.Windows.Win32.System.Variant.VARIANT, ResourceType: win32more.Windows.Win32.System.Variant.VARIANT, LanguageId: Int32, LoadOption: win32more.Windows.Win32.Media.Speech.SpeechLoadOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CmdLoadFromMemory(self, GrammarData: win32more.Windows.Win32.System.Variant.VARIANT, LoadOption: win32more.Windows.Win32.Media.Speech.SpeechLoadOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CmdLoadFromProprietaryGrammar(self, ProprietaryGuid: win32more.Windows.Win32.Foundation.BSTR, ProprietaryString: win32more.Windows.Win32.Foundation.BSTR, ProprietaryData: win32more.Windows.Win32.System.Variant.VARIANT, LoadOption: win32more.Windows.Win32.Media.Speech.SpeechLoadOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CmdSetRuleState(self, Name: win32more.Windows.Win32.Foundation.BSTR, State: win32more.Windows.Win32.Media.Speech.SpeechRuleState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CmdSetRuleIdState(self, RuleId: Int32, State: win32more.Windows.Win32.Media.Speech.SpeechRuleState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DictationLoad(self, TopicName: win32more.Windows.Win32.Foundation.BSTR, LoadOption: win32more.Windows.Win32.Media.Speech.SpeechLoadOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DictationUnload(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DictationSetState(self, State: win32more.Windows.Win32.Media.Speech.SpeechRuleState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWordSequenceData(self, Text: win32more.Windows.Win32.Foundation.BSTR, TextLength: Int32, Info: win32more.Windows.Win32.Media.Speech.ISpeechTextSelectionInformation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTextSelection(self, Info: win32more.Windows.Win32.Media.Speech.ISpeechTextSelectionInformation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsPronounceable(self, Word: win32more.Windows.Win32.Foundation.BSTR, WordPronounceable: POINTER(win32more.Windows.Win32.Media.Speech.SpeechWordPronounceable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ed2879cf-ced9-4ee6-a534-de0191d5468d}')
    @commethod(7)
    def get_RecoContext(self, RecoContext: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Times(self, Times: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoResultTimes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_AudioFormat(self, Format: win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioFormat(self, Format: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PhraseInfo(self, PhraseInfo: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Alternates(self, RequestCount: Int32, StartElement: Int32, Elements: Int32, Alternates: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseAlternates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Audio(self, StartElement: Int32, Elements: Int32, Stream: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechMemoryStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SpeakAudio(self, StartElement: Int32, Elements: Int32, Flags: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveToMemory(self, ResultBlock: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscardResultInfo(self, ValueTypes: win32more.Windows.Win32.Media.Speech.SpeechDiscardType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResult2(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpeechRecoResult
    _iid_ = Guid('{8e0a246d-d3c8-45de-8657-04290c458c3c}')
    @commethod(17)
    def SetTextFeedback(self, Feedback: win32more.Windows.Win32.Foundation.BSTR, WasSuccessful: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResultDispatch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6d60eb64-aced-40a6-bbf3-4e557f71dee2}')
    @commethod(7)
    def get_RecoContext(self, RecoContext: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Times(self, Times: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoResultTimes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_AudioFormat(self, Format: win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioFormat(self, Format: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PhraseInfo(self, PhraseInfo: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Alternates(self, RequestCount: Int32, StartElement: Int32, Elements: Int32, Alternates: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechPhraseAlternates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Audio(self, StartElement: Int32, Elements: Int32, Stream: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechMemoryStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SpeakAudio(self, StartElement: Int32, Elements: Int32, Flags: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveToMemory(self, ResultBlock: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscardResultInfo(self, ValueTypes: win32more.Windows.Win32.Media.Speech.SpeechDiscardType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetXMLResult(self, Options: win32more.Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS, pResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetXMLErrorInfo(self, LineNumber: POINTER(Int32), ScriptLine: POINTER(win32more.Windows.Win32.Foundation.BSTR), Source: POINTER(win32more.Windows.Win32.Foundation.BSTR), Description: POINTER(win32more.Windows.Win32.Foundation.BSTR), ResultCode: POINTER(win32more.Windows.Win32.Foundation.HRESULT), IsError: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetTextFeedback(self, Feedback: win32more.Windows.Win32.Foundation.BSTR, WasSuccessful: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecoResultTimes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{62b3b8fb-f6e7-41be-bdcb-056b1c29efc0}')
    @commethod(7)
    def get_StreamTime(self, Time: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Length(self, Length: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TickCount(self, TickCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OffsetFromStart(self, OffsetFromStart: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2d5f1c0c-bd75-4b08-9478-3b11fea2586c}')
    @commethod(7)
    def putref_Recognizer(self, Recognizer: win32more.Windows.Win32.Media.Speech.ISpeechObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Recognizer(self, Recognizer: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_AllowAudioInputFormatChangesOnNextSet(self, Allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AllowAudioInputFormatChangesOnNextSet(self, Allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_AudioInput(self, AudioInput: win32more.Windows.Win32.Media.Speech.ISpeechObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_AudioInput(self, AudioInput: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_AudioInputStream(self, AudioInputStream: win32more.Windows.Win32.Media.Speech.ISpeechBaseStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AudioInputStream(self, AudioInputStream: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechBaseStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsShared(self, Shared: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_State(self, State: win32more.Windows.Win32.Media.Speech.SpeechRecognizerState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_State(self, State: POINTER(win32more.Windows.Win32.Media.Speech.SpeechRecognizerState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Status(self, Status: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecognizerStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def putref_Profile(self, Profile: win32more.Windows.Win32.Media.Speech.ISpeechObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Profile(self, Profile: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EmulateRecognition(self, TextElements: win32more.Windows.Win32.System.Variant.VARIANT, ElementDisplayAttributes: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), LanguageId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateRecoContext(self, NewContext: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechRecoContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetFormat(self, Type: win32more.Windows.Win32.Media.Speech.SpeechFormatType, Format: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetPropertyNumber(self, Name: win32more.Windows.Win32.Foundation.BSTR, Value: Int32, Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPropertyNumber(self, Name: win32more.Windows.Win32.Foundation.BSTR, Value: POINTER(Int32), Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetPropertyString(self, Name: win32more.Windows.Win32.Foundation.BSTR, Value: win32more.Windows.Win32.Foundation.BSTR, Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetPropertyString(self, Name: win32more.Windows.Win32.Foundation.BSTR, Value: POINTER(win32more.Windows.Win32.Foundation.BSTR), Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def IsUISupported(self, TypeOfUI: win32more.Windows.Win32.Foundation.BSTR, ExtraData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DisplayUI(self, hWndParent: Int32, Title: win32more.Windows.Win32.Foundation.BSTR, TypeOfUI: win32more.Windows.Win32.Foundation.BSTR, ExtraData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetRecognizers(self, RequiredAttributes: win32more.Windows.Win32.Foundation.BSTR, OptionalAttributes: win32more.Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetAudioInputs(self, RequiredAttributes: win32more.Windows.Win32.Foundation.BSTR, OptionalAttributes: win32more.Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetProfiles(self, RequiredAttributes: win32more.Windows.Win32.Foundation.BSTR, OptionalAttributes: win32more.Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechRecognizerStatus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bff9e781-53ec-484e-bb8a-0e1b5551e35c}')
    @commethod(7)
    def get_AudioStatus(self, AudioStatus: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechAudioStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentStreamPosition(self, pCurrentStreamPos: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentStreamNumber(self, StreamNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NumberOfActiveRules(self, NumberOfActiveRules: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ClsidEngine(self, ClsidEngine: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SupportedLanguages(self, SupportedLanguages: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechResourceLoader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b9ac5783-fcd0-4b21-b119-b4f8da8fd2c3}')
    @commethod(7)
    def LoadResource(self, bstrResourceUri: win32more.Windows.Win32.Foundation.BSTR, fAlwaysReload: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pStream: POINTER(win32more.Windows.Win32.System.Com.IUnknown), pbstrMIMEType: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfModified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), pbstrRedirectUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLocalCopy(self, bstrResourceUri: win32more.Windows.Win32.Foundation.BSTR, pbstrLocalPath: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrMIMEType: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrRedirectUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ReleaseLocalCopy(self, pbstrLocalPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechTextSelectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3b9c7e7a-6eee-4ded-9092-11657279adbe}')
    @commethod(7)
    def put_ActiveOffset(self, ActiveOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActiveOffset(self, ActiveOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ActiveLength(self, ActiveLength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ActiveLength(self, ActiveLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_SelectionOffset(self, SelectionOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SelectionOffset(self, SelectionOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_SelectionLength(self, SelectionLength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SelectionLength(self, SelectionLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechVoice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{269316d8-57bd-11d2-9eee-00c04f797396}')
    @commethod(7)
    def get_Status(self, Status: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechVoiceStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Voice(self, Voice: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_Voice(self, Voice: win32more.Windows.Win32.Media.Speech.ISpeechObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AudioOutput(self, AudioOutput: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_AudioOutput(self, AudioOutput: win32more.Windows.Win32.Media.Speech.ISpeechObjectToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_AudioOutputStream(self, AudioOutputStream: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechBaseStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_AudioOutputStream(self, AudioOutputStream: win32more.Windows.Win32.Media.Speech.ISpeechBaseStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Rate(self, Rate: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Rate(self, Rate: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Volume(self, Volume: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Volume(self, Volume: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowAudioOutputFormatChangesOnNextSet(self, Allow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_AllowAudioOutputFormatChangesOnNextSet(self, Allow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_EventInterests(self, EventInterestFlags: POINTER(win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_EventInterests(self, EventInterestFlags: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Priority(self, Priority: win32more.Windows.Win32.Media.Speech.SpeechVoicePriority) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Priority(self, Priority: POINTER(win32more.Windows.Win32.Media.Speech.SpeechVoicePriority)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AlertBoundary(self, Boundary: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AlertBoundary(self, Boundary: POINTER(win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_SynchronousSpeakTimeout(self, msTimeout: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_SynchronousSpeakTimeout(self, msTimeout: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Speak(self, Text: win32more.Windows.Win32.Foundation.BSTR, Flags: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SpeakStream(self, Stream: win32more.Windows.Win32.Media.Speech.ISpeechBaseStream, Flags: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags, StreamNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Skip(self, Type: win32more.Windows.Win32.Foundation.BSTR, NumItems: Int32, NumSkipped: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetVoices(self, RequiredAttributes: win32more.Windows.Win32.Foundation.BSTR, OptionalAttributes: win32more.Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetAudioOutputs(self, RequiredAttributes: win32more.Windows.Win32.Foundation.BSTR, OptionalAttributes: win32more.Windows.Win32.Foundation.BSTR, ObjectTokens: POINTER(win32more.Windows.Win32.Media.Speech.ISpeechObjectTokens)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def WaitUntilDone(self, msTimeout: Int32, Done: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SpeakCompleteEvent(self, Handle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def IsUISupported(self, TypeOfUI: win32more.Windows.Win32.Foundation.BSTR, ExtraData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def DisplayUI(self, hWndParent: Int32, Title: win32more.Windows.Win32.Foundation.BSTR, TypeOfUI: win32more.Windows.Win32.Foundation.BSTR, ExtraData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechVoiceStatus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8be47b07-57f6-11d2-9eee-00c04f797396}')
    @commethod(7)
    def get_CurrentStreamNumber(self, StreamNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LastStreamNumberQueued(self, StreamNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LastHResult(self, HResult: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RunningState(self, State: POINTER(win32more.Windows.Win32.Media.Speech.SpeechRunState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InputWordPosition(self, Position: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InputWordLength(self, Length: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_InputSentencePosition(self, Position: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_InputSentenceLength(self, Length: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LastBookmark(self, Bookmark: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_LastBookmarkId(self, BookmarkId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_PhonemeId(self, PhoneId: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_VisemeId(self, VisemeId: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechWaveFormatEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7a1ef0d5-1581-4741-88e4-209a49f11a10}')
    @commethod(7)
    def get_FormatTag(self, FormatTag: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_FormatTag(self, FormatTag: Int16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Channels(self, Channels: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Channels(self, Channels: Int16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SamplesPerSec(self, SamplesPerSec: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SamplesPerSec(self, SamplesPerSec: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AvgBytesPerSec(self, AvgBytesPerSec: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AvgBytesPerSec(self, AvgBytesPerSec: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_BlockAlign(self, BlockAlign: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_BlockAlign(self, BlockAlign: Int16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BitsPerSample(self, BitsPerSample: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BitsPerSample(self, BitsPerSample: Int16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ExtraData(self, ExtraData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ExtraData(self, ExtraData: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpeechXMLRecoResult(ComPtr):
    extends: win32more.Windows.Win32.Media.Speech.ISpeechRecoResult
    _iid_ = Guid('{aaec54af-8f85-4924-944d-b79d39d72e19}')
    @commethod(17)
    def GetXMLResult(self, Options: win32more.Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS, pResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetXMLErrorInfo(self, LineNumber: POINTER(Int32), ScriptLine: POINTER(win32more.Windows.Win32.Foundation.BSTR), Source: POINTER(win32more.Windows.Win32.Foundation.BSTR), Description: POINTER(win32more.Windows.Win32.Foundation.BSTR), ResultCode: POINTER(Int32), IsError: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PHONETICALPHABET = Int32
PA_Ipa: win32more.Windows.Win32.Media.Speech.PHONETICALPHABET = 0
PA_Ups: win32more.Windows.Win32.Media.Speech.PHONETICALPHABET = 1
PA_Sapi: win32more.Windows.Win32.Media.Speech.PHONETICALPHABET = 2
SPADAPTATIONRELEVANCE = Int32
SPAR_Unknown: win32more.Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE = 0
SPAR_Low: win32more.Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE = 1
SPAR_Medium: win32more.Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE = 2
SPAR_High: win32more.Windows.Win32.Media.Speech.SPADAPTATIONRELEVANCE = 3
SPADAPTATIONSETTINGS = Int32
SPADS_Default: win32more.Windows.Win32.Media.Speech.SPADAPTATIONSETTINGS = 0
SPADS_CurrentRecognizer: win32more.Windows.Win32.Media.Speech.SPADAPTATIONSETTINGS = 1
SPADS_RecoProfile: win32more.Windows.Win32.Media.Speech.SPADAPTATIONSETTINGS = 2
SPADS_Immediate: win32more.Windows.Win32.Media.Speech.SPADAPTATIONSETTINGS = 4
SPADS_Reset: win32more.Windows.Win32.Media.Speech.SPADAPTATIONSETTINGS = 8
SPADS_HighVolumeDataSource: win32more.Windows.Win32.Media.Speech.SPADAPTATIONSETTINGS = 16
class SPAUDIOBUFFERINFO(Structure):
    ulMsMinNotification: UInt32
    ulMsBufferSize: UInt32
    ulMsEventBias: UInt32
SPAUDIOOPTIONS = Int32
SPAO_NONE: win32more.Windows.Win32.Media.Speech.SPAUDIOOPTIONS = 0
SPAO_RETAIN_AUDIO: win32more.Windows.Win32.Media.Speech.SPAUDIOOPTIONS = 1
SPAUDIOSTATE = Int32
SPAS_CLOSED: win32more.Windows.Win32.Media.Speech.SPAUDIOSTATE = 0
SPAS_STOP: win32more.Windows.Win32.Media.Speech.SPAUDIOSTATE = 1
SPAS_PAUSE: win32more.Windows.Win32.Media.Speech.SPAUDIOSTATE = 2
SPAS_RUN: win32more.Windows.Win32.Media.Speech.SPAUDIOSTATE = 3
class SPAUDIOSTATUS(Structure):
    cbFreeBuffSpace: Int32
    cbNonBlockingIO: UInt32
    State: win32more.Windows.Win32.Media.Speech.SPAUDIOSTATE
    CurSeekPos: UInt64
    CurDevicePos: UInt64
    dwAudioLevel: UInt32
    dwReserved2: UInt32
class SPBINARYGRAMMAR(Structure):
    ulTotalSerializedSize: UInt32
SPBOOKMARKOPTIONS = Int32
SPBO_NONE: win32more.Windows.Win32.Media.Speech.SPBOOKMARKOPTIONS = 0
SPBO_PAUSE: win32more.Windows.Win32.Media.Speech.SPBOOKMARKOPTIONS = 1
SPBO_AHEAD: win32more.Windows.Win32.Media.Speech.SPBOOKMARKOPTIONS = 2
SPBO_TIME_UNITS: win32more.Windows.Win32.Media.Speech.SPBOOKMARKOPTIONS = 4
SPCFGNOTIFY = Int32
SPCFGN_ADD: win32more.Windows.Win32.Media.Speech.SPCFGNOTIFY = 0
SPCFGN_REMOVE: win32more.Windows.Win32.Media.Speech.SPCFGNOTIFY = 1
SPCFGN_INVALIDATE: win32more.Windows.Win32.Media.Speech.SPCFGNOTIFY = 2
SPCFGN_ACTIVATE: win32more.Windows.Win32.Media.Speech.SPCFGNOTIFY = 3
SPCFGN_DEACTIVATE: win32more.Windows.Win32.Media.Speech.SPCFGNOTIFY = 4
SPCFGRULEATTRIBUTES = Int32
SPRAF_TopLevel: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 1
SPRAF_Active: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 2
SPRAF_Export: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 4
SPRAF_Import: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 8
SPRAF_Interpreter: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 16
SPRAF_Dynamic: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 32
SPRAF_Root: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 64
SPRAF_AutoPause: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 65536
SPRAF_UserDelimited: win32more.Windows.Win32.Media.Speech.SPCFGRULEATTRIBUTES = 131072
SPCOMMITFLAGS = Int32
SPCF_NONE: win32more.Windows.Win32.Media.Speech.SPCOMMITFLAGS = 0
SPCF_ADD_TO_USER_LEXICON: win32more.Windows.Win32.Media.Speech.SPCOMMITFLAGS = 1
SPCF_DEFINITE_CORRECTION: win32more.Windows.Win32.Media.Speech.SPCOMMITFLAGS = 2
SPCONTEXTSTATE = Int32
SPCS_DISABLED: win32more.Windows.Win32.Media.Speech.SPCONTEXTSTATE = 0
SPCS_ENABLED: win32more.Windows.Win32.Media.Speech.SPCONTEXTSTATE = 1
SPDATAKEYLOCATION = Int32
SPDKL_DefaultLocation: win32more.Windows.Win32.Media.Speech.SPDATAKEYLOCATION = 0
SPDKL_CurrentUser: win32more.Windows.Win32.Media.Speech.SPDATAKEYLOCATION = 1
SPDKL_LocalMachine: win32more.Windows.Win32.Media.Speech.SPDATAKEYLOCATION = 2
SPDKL_CurrentConfig: win32more.Windows.Win32.Media.Speech.SPDATAKEYLOCATION = 5
SPDISPLAYATTRIBUTES = Int32
SPAF_ONE_TRAILING_SPACE: win32more.Windows.Win32.Media.Speech.SPDISPLAYATTRIBUTES = 2
SPAF_TWO_TRAILING_SPACES: win32more.Windows.Win32.Media.Speech.SPDISPLAYATTRIBUTES = 4
SPAF_CONSUME_LEADING_SPACES: win32more.Windows.Win32.Media.Speech.SPDISPLAYATTRIBUTES = 8
SPAF_BUFFER_POSITION: win32more.Windows.Win32.Media.Speech.SPDISPLAYATTRIBUTES = 16
SPAF_ALL: win32more.Windows.Win32.Media.Speech.SPDISPLAYATTRIBUTES = 31
SPAF_USER_SPECIFIED: win32more.Windows.Win32.Media.Speech.SPDISPLAYATTRIBUTES = 128
class SPDISPLAYPHRASE(Structure):
    ulNumTokens: UInt32
    pTokens: POINTER(win32more.Windows.Win32.Media.Speech.SPDISPLAYTOKEN)
class SPDISPLAYTOKEN(Structure):
    pszLexical: win32more.Windows.Win32.Foundation.PWSTR
    pszDisplay: win32more.Windows.Win32.Foundation.PWSTR
    bDisplayAttributes: Byte
SPEAKFLAGS = Int32
SPF_DEFAULT: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 0
SPF_ASYNC: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 1
SPF_PURGEBEFORESPEAK: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 2
SPF_IS_FILENAME: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 4
SPF_IS_XML: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 8
SPF_IS_NOT_XML: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 16
SPF_PERSIST_XML: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 32
SPF_NLP_SPEAK_PUNC: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 64
SPF_PARSE_SAPI: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 128
SPF_PARSE_SSML: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 256
SPF_PARSE_AUTODETECT: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 0
SPF_NLP_MASK: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 64
SPF_PARSE_MASK: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 384
SPF_VOICE_MASK: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = 511
SPF_UNUSED_FLAGS: win32more.Windows.Win32.Media.Speech.SPEAKFLAGS = -512
SPENDSRSTREAMFLAGS = Int32
SPESF_NONE: win32more.Windows.Win32.Media.Speech.SPENDSRSTREAMFLAGS = 0
SPESF_STREAM_RELEASED: win32more.Windows.Win32.Media.Speech.SPENDSRSTREAMFLAGS = 1
SPESF_EMULATED: win32more.Windows.Win32.Media.Speech.SPENDSRSTREAMFLAGS = 2
class SPEVENT(Structure):
    eEventId: Annotated[Int32, 16]
    elParamType: Annotated[Int32, 16]
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    wParam: win32more.Windows.Win32.Foundation.WPARAM
    lParam: win32more.Windows.Win32.Foundation.LPARAM
SPEVENTENUM = Int32
SPEI_UNDEFINED: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 0
SPEI_START_INPUT_STREAM: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 1
SPEI_END_INPUT_STREAM: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 2
SPEI_VOICE_CHANGE: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 3
SPEI_TTS_BOOKMARK: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 4
SPEI_WORD_BOUNDARY: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 5
SPEI_PHONEME: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 6
SPEI_SENTENCE_BOUNDARY: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 7
SPEI_VISEME: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 8
SPEI_TTS_AUDIO_LEVEL: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 9
SPEI_TTS_PRIVATE: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 15
SPEI_MIN_TTS: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 1
SPEI_MAX_TTS: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 15
SPEI_END_SR_STREAM: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 34
SPEI_SOUND_START: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 35
SPEI_SOUND_END: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 36
SPEI_PHRASE_START: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 37
SPEI_RECOGNITION: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 38
SPEI_HYPOTHESIS: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 39
SPEI_SR_BOOKMARK: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 40
SPEI_PROPERTY_NUM_CHANGE: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 41
SPEI_PROPERTY_STRING_CHANGE: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 42
SPEI_FALSE_RECOGNITION: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 43
SPEI_INTERFERENCE: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 44
SPEI_REQUEST_UI: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 45
SPEI_RECO_STATE_CHANGE: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 46
SPEI_ADAPTATION: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 47
SPEI_START_SR_STREAM: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 48
SPEI_RECO_OTHER_CONTEXT: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 49
SPEI_SR_AUDIO_LEVEL: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 50
SPEI_SR_RETAINEDAUDIO: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 51
SPEI_SR_PRIVATE: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 52
SPEI_RESERVED4: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 53
SPEI_RESERVED5: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 54
SPEI_RESERVED6: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 55
SPEI_MIN_SR: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 34
SPEI_MAX_SR: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 55
SPEI_RESERVED1: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 30
SPEI_RESERVED2: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 33
SPEI_RESERVED3: win32more.Windows.Win32.Media.Speech.SPEVENTENUM = 63
class SPEVENTEX(Structure):
    eEventId: Annotated[Int32, 16]
    elParamType: Annotated[Int32, 16]
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    wParam: win32more.Windows.Win32.Foundation.WPARAM
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    ullAudioTimeOffset: UInt64
SPEVENTLPARAMTYPE = Int32
SPET_LPARAM_IS_UNDEFINED: win32more.Windows.Win32.Media.Speech.SPEVENTLPARAMTYPE = 0
SPET_LPARAM_IS_TOKEN: win32more.Windows.Win32.Media.Speech.SPEVENTLPARAMTYPE = 1
SPET_LPARAM_IS_OBJECT: win32more.Windows.Win32.Media.Speech.SPEVENTLPARAMTYPE = 2
SPET_LPARAM_IS_POINTER: win32more.Windows.Win32.Media.Speech.SPEVENTLPARAMTYPE = 3
SPET_LPARAM_IS_STRING: win32more.Windows.Win32.Media.Speech.SPEVENTLPARAMTYPE = 4
class SPEVENTSOURCEINFO(Structure):
    ullEventInterest: UInt64
    ullQueuedInterest: UInt64
    ulCount: UInt32
SPFILEMODE = Int32
SPFM_OPEN_READONLY: win32more.Windows.Win32.Media.Speech.SPFILEMODE = 0
SPFM_OPEN_READWRITE: win32more.Windows.Win32.Media.Speech.SPFILEMODE = 1
SPFM_CREATE: win32more.Windows.Win32.Media.Speech.SPFILEMODE = 2
SPFM_CREATE_ALWAYS: win32more.Windows.Win32.Media.Speech.SPFILEMODE = 3
SPFM_NUM_MODES: win32more.Windows.Win32.Media.Speech.SPFILEMODE = 4
SPGRAMMARHANDLE = VoidPtr
SPGRAMMAROPTIONS = Int32
SPGO_SAPI: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 1
SPGO_SRGS: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 2
SPGO_UPS: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 4
SPGO_SRGS_MS_SCRIPT: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 8
SPGO_SRGS_W3C_SCRIPT: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 256
SPGO_SRGS_STG_SCRIPT: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 512
SPGO_SRGS_SCRIPT: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 778
SPGO_FILE: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 16
SPGO_HTTP: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 32
SPGO_RES: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 64
SPGO_OBJECT: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 128
SPGO_DEFAULT: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 1019
SPGO_ALL: win32more.Windows.Win32.Media.Speech.SPGRAMMAROPTIONS = 1023
SPGRAMMARSTATE = Int32
SPGS_DISABLED: win32more.Windows.Win32.Media.Speech.SPGRAMMARSTATE = 0
SPGS_ENABLED: win32more.Windows.Win32.Media.Speech.SPGRAMMARSTATE = 1
SPGS_EXCLUSIVE: win32more.Windows.Win32.Media.Speech.SPGRAMMARSTATE = 3
SPGRAMMARWORDTYPE = Int32
SPWT_DISPLAY: win32more.Windows.Win32.Media.Speech.SPGRAMMARWORDTYPE = 0
SPWT_LEXICAL: win32more.Windows.Win32.Media.Speech.SPGRAMMARWORDTYPE = 1
SPWT_PRONUNCIATION: win32more.Windows.Win32.Media.Speech.SPGRAMMARWORDTYPE = 2
SPWT_LEXICAL_NO_SPECIAL_CHARS: win32more.Windows.Win32.Media.Speech.SPGRAMMARWORDTYPE = 3
SPINTERFERENCE = Int32
SPINTERFERENCE_NONE: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 0
SPINTERFERENCE_NOISE: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 1
SPINTERFERENCE_NOSIGNAL: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 2
SPINTERFERENCE_TOOLOUD: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 3
SPINTERFERENCE_TOOQUIET: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 4
SPINTERFERENCE_TOOFAST: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 5
SPINTERFERENCE_TOOSLOW: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 6
SPINTERFERENCE_LATENCY_WARNING: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 7
SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 8
SPINTERFERENCE_LATENCY_TRUNCATE_END: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE = 9
SPLEXICONTYPE = Int32
eLEXTYPE_USER: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 1
eLEXTYPE_APP: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 2
eLEXTYPE_VENDORLEXICON: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 4
eLEXTYPE_LETTERTOSOUND: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 8
eLEXTYPE_MORPHOLOGY: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 16
eLEXTYPE_RESERVED4: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 32
eLEXTYPE_USER_SHORTCUT: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 64
eLEXTYPE_RESERVED6: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 128
eLEXTYPE_RESERVED7: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 256
eLEXTYPE_RESERVED8: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 512
eLEXTYPE_RESERVED9: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 1024
eLEXTYPE_RESERVED10: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 2048
eLEXTYPE_PRIVATE1: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 4096
eLEXTYPE_PRIVATE2: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 8192
eLEXTYPE_PRIVATE3: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 16384
eLEXTYPE_PRIVATE4: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 32768
eLEXTYPE_PRIVATE5: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 65536
eLEXTYPE_PRIVATE6: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 131072
eLEXTYPE_PRIVATE7: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 262144
eLEXTYPE_PRIVATE8: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 524288
eLEXTYPE_PRIVATE9: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 1048576
eLEXTYPE_PRIVATE10: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 2097152
eLEXTYPE_PRIVATE11: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 4194304
eLEXTYPE_PRIVATE12: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 8388608
eLEXTYPE_PRIVATE13: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 16777216
eLEXTYPE_PRIVATE14: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 33554432
eLEXTYPE_PRIVATE15: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 67108864
eLEXTYPE_PRIVATE16: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 134217728
eLEXTYPE_PRIVATE17: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 268435456
eLEXTYPE_PRIVATE18: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 536870912
eLEXTYPE_PRIVATE19: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = 1073741824
eLEXTYPE_PRIVATE20: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE = -2147483648
SPLOADOPTIONS = Int32
SPLO_STATIC: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS = 0
SPLO_DYNAMIC: win32more.Windows.Win32.Media.Speech.SPLOADOPTIONS = 1
SPMATCHINGMODE = Int32
AllWords: win32more.Windows.Win32.Media.Speech.SPMATCHINGMODE = 0
Subsequence: win32more.Windows.Win32.Media.Speech.SPMATCHINGMODE = 1
OrderedSubset: win32more.Windows.Win32.Media.Speech.SPMATCHINGMODE = 3
SubsequenceContentRequired: win32more.Windows.Win32.Media.Speech.SPMATCHINGMODE = 5
OrderedSubsetContentRequired: win32more.Windows.Win32.Media.Speech.SPMATCHINGMODE = 7
class SPNORMALIZATIONLIST(Structure):
    ulSize: UInt32
    ppszzNormalizedList: POINTER(POINTER(UInt16))
@winfunctype_pointer
def SPNOTIFYCALLBACK(wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> Void: ...
class SPPARSEINFO(Structure):
    cbSize: UInt32
    hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE
    ullAudioStreamPosition: UInt64
    ulAudioSize: UInt32
    cTransitions: UInt32
    pPath: POINTER(win32more.Windows.Win32.Media.Speech.SPPATHENTRY)
    SREngineID: Guid
    ulSREnginePrivateDataSize: UInt32
    pSREnginePrivateData: POINTER(Byte)
    fHypothesis: win32more.Windows.Win32.Foundation.BOOL
SPPARTOFSPEECH = Int32
SPPS_NotOverriden: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = -1
SPPS_Unknown: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 0
SPPS_Noun: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 4096
SPPS_Verb: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 8192
SPPS_Modifier: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 12288
SPPS_Function: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 16384
SPPS_Interjection: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 20480
SPPS_Noncontent: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 24576
SPPS_LMA: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 28672
SPPS_SuppressWord: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH = 61440
class SPPATHENTRY(Structure):
    hTransition: win32more.Windows.Win32.Media.Speech.SPTRANSITIONID
    elem: win32more.Windows.Win32.Media.Speech.SPPHRASEELEMENT
class SPPHRASE(Structure):
    Base: win32more.Windows.Win32.Media.Speech.SPPHRASE_50
    pSML: win32more.Windows.Win32.Foundation.PWSTR
    pSemanticErrorInfo: POINTER(win32more.Windows.Win32.Media.Speech.SPSEMANTICERRORINFO)
class SPPHRASEALT(Structure):
    pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhraseBuilder
    ulStartElementInParent: UInt32
    cElementsInParent: UInt32
    cElementsInAlternate: UInt32
    pvAltExtra: VoidPtr
    cbAltExtra: UInt32
class SPPHRASEALTREQUEST(Structure):
    ulStartElement: UInt32
    cElements: UInt32
    ulRequestAltCount: UInt32
    pvResultExtra: VoidPtr
    cbResultExtra: UInt32
    pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhrase
    pRecoContext: win32more.Windows.Win32.Media.Speech.ISpRecoContext
class SPPHRASEELEMENT(Structure):
    ulAudioTimeOffset: UInt32
    ulAudioSizeTime: UInt32
    ulAudioStreamOffset: UInt32
    ulAudioSizeBytes: UInt32
    ulRetainedStreamOffset: UInt32
    ulRetainedSizeBytes: UInt32
    pszDisplayText: win32more.Windows.Win32.Foundation.PWSTR
    pszLexicalForm: win32more.Windows.Win32.Foundation.PWSTR
    pszPronunciation: POINTER(UInt16)
    bDisplayAttributes: Byte
    RequiredConfidence: SByte
    ActualConfidence: SByte
    Reserved: Byte
    SREngineConfidence: Single
class SPPHRASEPROPERTY(Structure):
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    pszValue: win32more.Windows.Win32.Foundation.PWSTR
    vValue: win32more.Windows.Win32.System.Variant.VARIANT
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
    pNextSibling: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTY)
    pFirstChild: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTY)
    SREngineConfidence: Single
    Confidence: SByte
    class _Anonymous_e__Union(Union):
        ulId: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            bType: Byte
            bReserved: Byte
            usArrayIndex: UInt16
SPPHRASEPROPERTYHANDLE = VoidPtr
SPPHRASEPROPERTYUNIONTYPE = Int32
SPPPUT_UNUSED: win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTYUNIONTYPE = 0
SPPPUT_ARRAY_INDEX: win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTYUNIONTYPE = 1
class SPPHRASEREPLACEMENT(Structure):
    bDisplayAttributes: Byte
    pszReplacementText: win32more.Windows.Win32.Foundation.PWSTR
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
SPPHRASERNG = Int32
SPPR_ALL_ELEMENTS: win32more.Windows.Win32.Media.Speech.SPPHRASERNG = -1
class SPPHRASERULE(Structure):
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    ulId: UInt32
    ulFirstElement: UInt32
    ulCountOfElements: UInt32
    pNextSibling: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASERULE)
    pFirstChild: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASERULE)
    SREngineConfidence: Single
    Confidence: SByte
SPPHRASERULEHANDLE = VoidPtr
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
    Rule: win32more.Windows.Win32.Media.Speech.SPPHRASERULE
    pProperties: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEPROPERTY)
    pElements: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEELEMENT)
    cReplacements: UInt32
    pReplacements: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEREPLACEMENT)
    SREngineID: Guid
    ulSREnginePrivateDataSize: UInt32
    pSREnginePrivateData: POINTER(Byte)
SPPRONUNCIATIONFLAGS = Int32
ePRONFLAG_USED: win32more.Windows.Win32.Media.Speech.SPPRONUNCIATIONFLAGS = 1
class SPPROPERTYINFO(Structure):
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    ulId: UInt32
    pszValue: win32more.Windows.Win32.Foundation.PWSTR
    vValue: win32more.Windows.Win32.System.Variant.VARIANT
SPPROPSRC = Int32
SPPROPSRC_RECO_INST: win32more.Windows.Win32.Media.Speech.SPPROPSRC = 0
SPPROPSRC_RECO_CTX: win32more.Windows.Win32.Media.Speech.SPPROPSRC = 1
SPPROPSRC_RECO_GRAMMAR: win32more.Windows.Win32.Media.Speech.SPPROPSRC = 2
SPRECOCONTEXTHANDLE = VoidPtr
class SPRECOCONTEXTSTATUS(Structure):
    eInterference: win32more.Windows.Win32.Media.Speech.SPINTERFERENCE
    szRequestTypeOfUI: Char * 255
    dwReserved1: UInt32
    dwReserved2: UInt32
SPRECOEVENTFLAGS = Int32
SPREF_AutoPause: win32more.Windows.Win32.Media.Speech.SPRECOEVENTFLAGS = 1
SPREF_Emulated: win32more.Windows.Win32.Media.Speech.SPRECOEVENTFLAGS = 2
SPREF_SMLTimeout: win32more.Windows.Win32.Media.Speech.SPRECOEVENTFLAGS = 4
SPREF_ExtendableParse: win32more.Windows.Win32.Media.Speech.SPRECOEVENTFLAGS = 8
SPREF_ReSent: win32more.Windows.Win32.Media.Speech.SPRECOEVENTFLAGS = 16
SPREF_Hypothesis: win32more.Windows.Win32.Media.Speech.SPRECOEVENTFLAGS = 32
SPREF_FalseRecognition: win32more.Windows.Win32.Media.Speech.SPRECOEVENTFLAGS = 64
class SPRECOGNIZERSTATUS(Structure):
    AudioStatus: win32more.Windows.Win32.Media.Speech.SPAUDIOSTATUS
    ullRecognitionStreamPos: UInt64
    ulStreamNumber: UInt32
    ulNumActive: UInt32
    clsidEngine: Guid
    cLangIDs: UInt32
    aLangID: UInt16 * 20
    ullRecognitionStreamTime: UInt64
class SPRECORESULTINFO(Structure):
    cbSize: UInt32
    eResultType: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE
    fHypothesis: win32more.Windows.Win32.Foundation.BOOL
    fProprietaryAutoPause: win32more.Windows.Win32.Foundation.BOOL
    ullStreamPosStart: UInt64
    ullStreamPosEnd: UInt64
    hGrammar: win32more.Windows.Win32.Media.Speech.SPGRAMMARHANDLE
    ulSizeEngineData: UInt32
    pvEngineData: VoidPtr
    pPhrase: win32more.Windows.Win32.Media.Speech.ISpPhraseBuilder
    aPhraseAlts: POINTER(win32more.Windows.Win32.Media.Speech.SPPHRASEALT)
    ulNumAlts: UInt32
class SPRECORESULTINFOEX(Structure):
    Base: win32more.Windows.Win32.Media.Speech.SPRECORESULTINFO
    ullStreamTimeStart: UInt64
    ullStreamTimeEnd: UInt64
class SPRECORESULTTIMES(Structure):
    ftStreamTime: win32more.Windows.Win32.Foundation.FILETIME
    ullLength: UInt64
    dwTickCount: UInt32
    ullStart: UInt64
SPRECOSTATE = Int32
SPRST_INACTIVE: win32more.Windows.Win32.Media.Speech.SPRECOSTATE = 0
SPRST_ACTIVE: win32more.Windows.Win32.Media.Speech.SPRECOSTATE = 1
SPRST_ACTIVE_ALWAYS: win32more.Windows.Win32.Media.Speech.SPRECOSTATE = 2
SPRST_INACTIVE_WITH_PURGE: win32more.Windows.Win32.Media.Speech.SPRECOSTATE = 3
SPRST_NUM_STATES: win32more.Windows.Win32.Media.Speech.SPRECOSTATE = 4
SPRESULTTYPE = Int32
SPRT_CFG: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE = 0
SPRT_SLM: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE = 1
SPRT_PROPRIETARY: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE = 2
SPRT_FALSE_RECOGNITION: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE = 4
SPRT_TYPE_MASK: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE = 3
SPRT_EMULATED: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE = 8
SPRT_EXTENDABLE_PARSE: win32more.Windows.Win32.Media.Speech.SPRESULTTYPE = 16
class SPRULE(Structure):
    pszRuleName: win32more.Windows.Win32.Foundation.PWSTR
    ulRuleId: UInt32
    dwAttributes: UInt32
class SPRULEENTRY(Structure):
    hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE
    hInitialState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE
    Attributes: UInt32
    pvClientRuleContext: VoidPtr
    pvClientGrammarContext: VoidPtr
SPRULEHANDLE = VoidPtr
SPRULEINFOOPT = Int32
SPRIO_NONE: win32more.Windows.Win32.Media.Speech.SPRULEINFOOPT = 0
SPRULESTATE = Int32
SPRS_INACTIVE: win32more.Windows.Win32.Media.Speech.SPRULESTATE = 0
SPRS_ACTIVE: win32more.Windows.Win32.Media.Speech.SPRULESTATE = 1
SPRS_ACTIVE_WITH_AUTO_PAUSE: win32more.Windows.Win32.Media.Speech.SPRULESTATE = 3
SPRS_ACTIVE_USER_DELIMITED: win32more.Windows.Win32.Media.Speech.SPRULESTATE = 4
SPRUNSTATE = Int32
SPRS_DONE: win32more.Windows.Win32.Media.Speech.SPRUNSTATE = 1
SPRS_IS_SPEAKING: win32more.Windows.Win32.Media.Speech.SPRUNSTATE = 2
class SPSEMANTICERRORINFO(Structure):
    ulLineNumber: UInt32
    pszScriptLine: win32more.Windows.Win32.Foundation.PWSTR
    pszSource: win32more.Windows.Win32.Foundation.PWSTR
    pszDescription: win32more.Windows.Win32.Foundation.PWSTR
    hrResultCode: win32more.Windows.Win32.Foundation.HRESULT
SPSEMANTICFORMAT = Int32
SPSMF_SAPI_PROPERTIES: win32more.Windows.Win32.Media.Speech.SPSEMANTICFORMAT = 0
SPSMF_SRGS_SEMANTICINTERPRETATION_MS: win32more.Windows.Win32.Media.Speech.SPSEMANTICFORMAT = 1
SPSMF_SRGS_SAPIPROPERTIES: win32more.Windows.Win32.Media.Speech.SPSEMANTICFORMAT = 2
SPSMF_UPS: win32more.Windows.Win32.Media.Speech.SPSEMANTICFORMAT = 4
SPSMF_SRGS_SEMANTICINTERPRETATION_W3C: win32more.Windows.Win32.Media.Speech.SPSEMANTICFORMAT = 8
class SPSERIALIZEDEVENT(Structure):
    eEventId: Annotated[Int32, 16]
    elParamType: Annotated[Int32, 16]
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    SerializedwParam: UInt32
    SerializedlParam: Int32
class SPSERIALIZEDEVENT64(Structure):
    eEventId: Annotated[Int32, 16]
    elParamType: Annotated[Int32, 16]
    ulStreamNum: UInt32
    ullAudioStreamOffset: UInt64
    SerializedwParam: UInt64
    SerializedlParam: Int64
class SPSERIALIZEDPHRASE(Structure):
    ulSerializedSize: UInt32
class SPSERIALIZEDRESULT(Structure):
    ulSerializedSize: UInt32
class SPSHORTCUTPAIR(Structure):
    pNextSHORTCUTPAIR: POINTER(win32more.Windows.Win32.Media.Speech.SPSHORTCUTPAIR)
    LangID: UInt16
    shType: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE
    pszDisplay: win32more.Windows.Win32.Foundation.PWSTR
    pszSpoken: win32more.Windows.Win32.Foundation.PWSTR
class SPSHORTCUTPAIRLIST(Structure):
    ulSize: UInt32
    pvBuffer: POINTER(Byte)
    pFirstShortcutPair: POINTER(win32more.Windows.Win32.Media.Speech.SPSHORTCUTPAIR)
SPSHORTCUTTYPE = Int32
SPSHT_NotOverriden: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = -1
SPSHT_Unknown: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = 0
SPSHT_EMAIL: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = 4096
SPSHT_OTHER: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = 8192
SPPS_RESERVED1: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = 12288
SPPS_RESERVED2: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = 16384
SPPS_RESERVED3: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = 20480
SPPS_RESERVED4: win32more.Windows.Win32.Media.Speech.SPSHORTCUTTYPE = 61440
SPSTATEHANDLE = VoidPtr
class SPSTATEINFO(Structure):
    cAllocatedEntries: UInt32
    pTransitions: POINTER(win32more.Windows.Win32.Media.Speech.SPTRANSITIONENTRY)
    cEpsilons: UInt32
    cRules: UInt32
    cWords: UInt32
    cSpecialTransitions: UInt32
SPSTREAMFORMAT = Int32
SPSF_Default: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = -1
SPSF_NoAssignedFormat: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 0
SPSF_Text: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 1
SPSF_NonStandardFormat: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 2
SPSF_ExtendedAudioFormat: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 3
SPSF_8kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 4
SPSF_8kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 5
SPSF_8kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 6
SPSF_8kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 7
SPSF_11kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 8
SPSF_11kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 9
SPSF_11kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 10
SPSF_11kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 11
SPSF_12kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 12
SPSF_12kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 13
SPSF_12kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 14
SPSF_12kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 15
SPSF_16kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 16
SPSF_16kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 17
SPSF_16kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 18
SPSF_16kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 19
SPSF_22kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 20
SPSF_22kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 21
SPSF_22kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 22
SPSF_22kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 23
SPSF_24kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 24
SPSF_24kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 25
SPSF_24kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 26
SPSF_24kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 27
SPSF_32kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 28
SPSF_32kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 29
SPSF_32kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 30
SPSF_32kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 31
SPSF_44kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 32
SPSF_44kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 33
SPSF_44kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 34
SPSF_44kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 35
SPSF_48kHz8BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 36
SPSF_48kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 37
SPSF_48kHz16BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 38
SPSF_48kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 39
SPSF_TrueSpeech_8kHz1BitMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 40
SPSF_CCITT_ALaw_8kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 41
SPSF_CCITT_ALaw_8kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 42
SPSF_CCITT_ALaw_11kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 43
SPSF_CCITT_ALaw_11kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 44
SPSF_CCITT_ALaw_22kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 45
SPSF_CCITT_ALaw_22kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 46
SPSF_CCITT_ALaw_44kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 47
SPSF_CCITT_ALaw_44kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 48
SPSF_CCITT_uLaw_8kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 49
SPSF_CCITT_uLaw_8kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 50
SPSF_CCITT_uLaw_11kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 51
SPSF_CCITT_uLaw_11kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 52
SPSF_CCITT_uLaw_22kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 53
SPSF_CCITT_uLaw_22kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 54
SPSF_CCITT_uLaw_44kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 55
SPSF_CCITT_uLaw_44kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 56
SPSF_ADPCM_8kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 57
SPSF_ADPCM_8kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 58
SPSF_ADPCM_11kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 59
SPSF_ADPCM_11kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 60
SPSF_ADPCM_22kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 61
SPSF_ADPCM_22kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 62
SPSF_ADPCM_44kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 63
SPSF_ADPCM_44kHzStereo: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 64
SPSF_GSM610_8kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 65
SPSF_GSM610_11kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 66
SPSF_GSM610_22kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 67
SPSF_GSM610_44kHzMono: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 68
SPSF_NUM_FORMATS: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMAT = 69
SPSTREAMFORMATTYPE = Int32
SPWF_INPUT: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMATTYPE = 0
SPWF_SRENGINE: win32more.Windows.Win32.Media.Speech.SPSTREAMFORMATTYPE = 1
class SPTEXTSELECTIONINFO(Structure):
    ulStartActiveOffset: UInt32
    cchActiveChars: UInt32
    ulStartSelection: UInt32
    cchSelection: UInt32
class SPTMTHREADINFO(Structure):
    lPoolSize: Int32
    lPriority: Int32
    ulConcurrencyLimit: UInt32
    ulMaxQuickAllocThreads: UInt32
class SPTRANSITIONENTRY(Structure):
    ID: win32more.Windows.Win32.Media.Speech.SPTRANSITIONID
    hNextState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE
    Type: Byte
    RequiredConfidence: Byte
    Anonymous1: _Anonymous1_e__Struct
    Weight: Single
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Struct(Structure):
        fHasProperty: UInt32
    class _Anonymous2_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        Anonymous3: _Anonymous3_e__Struct
        class _Anonymous1_e__Struct(Structure):
            hRuleInitialState: win32more.Windows.Win32.Media.Speech.SPSTATEHANDLE
            hRule: win32more.Windows.Win32.Media.Speech.SPRULEHANDLE
            pvClientRuleContext: VoidPtr
        class _Anonymous2_e__Struct(Structure):
            hWord: win32more.Windows.Win32.Media.Speech.SPWORDHANDLE
            pvClientWordContext: VoidPtr
        class _Anonymous3_e__Struct(Structure):
            pvGrammarCookie: VoidPtr
SPTRANSITIONID = VoidPtr
class SPTRANSITIONPROPERTY(Structure):
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    ulId: UInt32
    pszValue: win32more.Windows.Win32.Foundation.PWSTR
    vValue: win32more.Windows.Win32.System.Variant.VARIANT
SPTRANSITIONTYPE = Int32
SPTRANSEPSILON: win32more.Windows.Win32.Media.Speech.SPTRANSITIONTYPE = 0
SPTRANSWORD: win32more.Windows.Win32.Media.Speech.SPTRANSITIONTYPE = 1
SPTRANSRULE: win32more.Windows.Win32.Media.Speech.SPTRANSITIONTYPE = 2
SPTRANSTEXTBUF: win32more.Windows.Win32.Media.Speech.SPTRANSITIONTYPE = 3
SPTRANSWILDCARD: win32more.Windows.Win32.Media.Speech.SPTRANSITIONTYPE = 4
SPTRANSDICTATION: win32more.Windows.Win32.Media.Speech.SPTRANSITIONTYPE = 5
SPVACTIONS = Int32
SPVA_Speak: win32more.Windows.Win32.Media.Speech.SPVACTIONS = 0
SPVA_Silence: win32more.Windows.Win32.Media.Speech.SPVACTIONS = 1
SPVA_Pronounce: win32more.Windows.Win32.Media.Speech.SPVACTIONS = 2
SPVA_Bookmark: win32more.Windows.Win32.Media.Speech.SPVACTIONS = 3
SPVA_SpellOut: win32more.Windows.Win32.Media.Speech.SPVACTIONS = 4
SPVA_Section: win32more.Windows.Win32.Media.Speech.SPVACTIONS = 5
SPVA_ParseUnknownTag: win32more.Windows.Win32.Media.Speech.SPVACTIONS = 6
SPVALUETYPE = Int32
SPDF_PROPERTY: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 1
SPDF_REPLACEMENT: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 2
SPDF_RULE: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 4
SPDF_DISPLAYTEXT: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 8
SPDF_LEXICALFORM: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 16
SPDF_PRONUNCIATION: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 32
SPDF_AUDIO: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 64
SPDF_ALTERNATES: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 128
SPDF_ALL: win32more.Windows.Win32.Media.Speech.SPVALUETYPE = 255
class SPVCONTEXT(Structure):
    pCategory: win32more.Windows.Win32.Foundation.PWSTR
    pBefore: win32more.Windows.Win32.Foundation.PWSTR
    pAfter: win32more.Windows.Win32.Foundation.PWSTR
SPVESACTIONS = Int32
SPVES_CONTINUE: win32more.Windows.Win32.Media.Speech.SPVESACTIONS = 0
SPVES_ABORT: win32more.Windows.Win32.Media.Speech.SPVESACTIONS = 1
SPVES_SKIP: win32more.Windows.Win32.Media.Speech.SPVESACTIONS = 2
SPVES_RATE: win32more.Windows.Win32.Media.Speech.SPVESACTIONS = 4
SPVES_VOLUME: win32more.Windows.Win32.Media.Speech.SPVESACTIONS = 8
SPVFEATURE = Int32
SPVFEATURE_STRESSED: win32more.Windows.Win32.Media.Speech.SPVFEATURE = 1
SPVFEATURE_EMPHASIS: win32more.Windows.Win32.Media.Speech.SPVFEATURE = 2
SPVISEMES = Int32
SP_VISEME_0: win32more.Windows.Win32.Media.Speech.SPVISEMES = 0
SP_VISEME_1: win32more.Windows.Win32.Media.Speech.SPVISEMES = 1
SP_VISEME_2: win32more.Windows.Win32.Media.Speech.SPVISEMES = 2
SP_VISEME_3: win32more.Windows.Win32.Media.Speech.SPVISEMES = 3
SP_VISEME_4: win32more.Windows.Win32.Media.Speech.SPVISEMES = 4
SP_VISEME_5: win32more.Windows.Win32.Media.Speech.SPVISEMES = 5
SP_VISEME_6: win32more.Windows.Win32.Media.Speech.SPVISEMES = 6
SP_VISEME_7: win32more.Windows.Win32.Media.Speech.SPVISEMES = 7
SP_VISEME_8: win32more.Windows.Win32.Media.Speech.SPVISEMES = 8
SP_VISEME_9: win32more.Windows.Win32.Media.Speech.SPVISEMES = 9
SP_VISEME_10: win32more.Windows.Win32.Media.Speech.SPVISEMES = 10
SP_VISEME_11: win32more.Windows.Win32.Media.Speech.SPVISEMES = 11
SP_VISEME_12: win32more.Windows.Win32.Media.Speech.SPVISEMES = 12
SP_VISEME_13: win32more.Windows.Win32.Media.Speech.SPVISEMES = 13
SP_VISEME_14: win32more.Windows.Win32.Media.Speech.SPVISEMES = 14
SP_VISEME_15: win32more.Windows.Win32.Media.Speech.SPVISEMES = 15
SP_VISEME_16: win32more.Windows.Win32.Media.Speech.SPVISEMES = 16
SP_VISEME_17: win32more.Windows.Win32.Media.Speech.SPVISEMES = 17
SP_VISEME_18: win32more.Windows.Win32.Media.Speech.SPVISEMES = 18
SP_VISEME_19: win32more.Windows.Win32.Media.Speech.SPVISEMES = 19
SP_VISEME_20: win32more.Windows.Win32.Media.Speech.SPVISEMES = 20
SP_VISEME_21: win32more.Windows.Win32.Media.Speech.SPVISEMES = 21
SPVLIMITS = Int32
SPMIN_VOLUME: win32more.Windows.Win32.Media.Speech.SPVLIMITS = 0
SPMAX_VOLUME: win32more.Windows.Win32.Media.Speech.SPVLIMITS = 100
SPMIN_RATE: win32more.Windows.Win32.Media.Speech.SPVLIMITS = -10
SPMAX_RATE: win32more.Windows.Win32.Media.Speech.SPVLIMITS = 10
class SPVOICESTATUS(Structure):
    ulCurrentStream: UInt32
    ulLastStreamQueued: UInt32
    hrLastResult: win32more.Windows.Win32.Foundation.HRESULT
    dwRunningState: UInt32
    ulInputWordPos: UInt32
    ulInputWordLen: UInt32
    ulInputSentPos: UInt32
    ulInputSentLen: UInt32
    lBookmarkId: Int32
    PhonemeId: UInt16
    VisemeId: win32more.Windows.Win32.Media.Speech.SPVISEMES
    dwReserved1: UInt32
    dwReserved2: UInt32
class SPVPITCH(Structure):
    MiddleAdj: Int32
    RangeAdj: Int32
SPVPRIORITY = Int32
SPVPRI_NORMAL: win32more.Windows.Win32.Media.Speech.SPVPRIORITY = 0
SPVPRI_ALERT: win32more.Windows.Win32.Media.Speech.SPVPRIORITY = 1
SPVPRI_OVER: win32more.Windows.Win32.Media.Speech.SPVPRIORITY = 2
SPVSKIPTYPE = Int32
SPVST_SENTENCE: win32more.Windows.Win32.Media.Speech.SPVSKIPTYPE = 1
class SPVSTATE(Structure):
    eAction: win32more.Windows.Win32.Media.Speech.SPVACTIONS
    LangID: UInt16
    wReserved: UInt16
    EmphAdj: Int32
    RateAdj: Int32
    Volume: UInt32
    PitchAdj: win32more.Windows.Win32.Media.Speech.SPVPITCH
    SilenceMSecs: UInt32
    pPhoneIds: POINTER(UInt16)
    ePartOfSpeech: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH
    Context: win32more.Windows.Win32.Media.Speech.SPVCONTEXT
class SPVTEXTFRAG(Structure):
    pNext: POINTER(win32more.Windows.Win32.Media.Speech.SPVTEXTFRAG)
    State: win32more.Windows.Win32.Media.Speech.SPVSTATE
    pTextStart: win32more.Windows.Win32.Foundation.PWSTR
    ulTextLen: UInt32
    ulTextSrcOffset: UInt32
class SPWORD(Structure):
    pNextWord: POINTER(win32more.Windows.Win32.Media.Speech.SPWORD)
    LangID: UInt16
    wReserved: UInt16
    eWordType: win32more.Windows.Win32.Media.Speech.SPWORDTYPE
    pszWord: win32more.Windows.Win32.Foundation.PWSTR
    pFirstWordPronunciation: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDPRONUNCIATION)
class SPWORDENTRY(Structure):
    hWord: win32more.Windows.Win32.Media.Speech.SPWORDHANDLE
    LangID: UInt16
    pszDisplayText: win32more.Windows.Win32.Foundation.PWSTR
    pszLexicalForm: win32more.Windows.Win32.Foundation.PWSTR
    aPhoneId: POINTER(UInt16)
    pvClientContext: VoidPtr
SPWORDHANDLE = VoidPtr
SPWORDINFOOPT = Int32
SPWIO_NONE: win32more.Windows.Win32.Media.Speech.SPWORDINFOOPT = 0
SPWIO_WANT_TEXT: win32more.Windows.Win32.Media.Speech.SPWORDINFOOPT = 1
class SPWORDLIST(Structure):
    ulSize: UInt32
    pvBuffer: POINTER(Byte)
    pFirstWord: POINTER(win32more.Windows.Win32.Media.Speech.SPWORD)
SPWORDPRONOUNCEABLE = Int32
SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE: win32more.Windows.Win32.Media.Speech.SPWORDPRONOUNCEABLE = 0
SPWP_UNKNOWN_WORD_PRONOUNCEABLE: win32more.Windows.Win32.Media.Speech.SPWORDPRONOUNCEABLE = 1
SPWP_KNOWN_WORD_PRONOUNCEABLE: win32more.Windows.Win32.Media.Speech.SPWORDPRONOUNCEABLE = 2
class SPWORDPRONUNCIATION(Structure):
    pNextWordPronunciation: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDPRONUNCIATION)
    eLexiconType: win32more.Windows.Win32.Media.Speech.SPLEXICONTYPE
    LangID: UInt16
    wPronunciationFlags: UInt16
    ePartOfSpeech: win32more.Windows.Win32.Media.Speech.SPPARTOFSPEECH
    szPronunciation: UInt16 * 1
class SPWORDPRONUNCIATIONLIST(Structure):
    ulSize: UInt32
    pvBuffer: POINTER(Byte)
    pFirstWordPronunciation: POINTER(win32more.Windows.Win32.Media.Speech.SPWORDPRONUNCIATION)
SPWORDTYPE = Int32
eWORDTYPE_ADDED: win32more.Windows.Win32.Media.Speech.SPWORDTYPE = 1
eWORDTYPE_DELETED: win32more.Windows.Win32.Media.Speech.SPWORDTYPE = 2
SPXMLRESULTOPTIONS = Int32
SPXRO_SML: win32more.Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS = 0
SPXRO_Alternates_SML: win32more.Windows.Win32.Media.Speech.SPXMLRESULTOPTIONS = 1
SpAudioFormat = Guid('{9ef96870-e160-4792-820d-48cf0649e4ec}')
SpCompressedLexicon = Guid('{90903716-2f42-11d3-9c26-00c04f8ef87c}')
SpCustomStream = Guid('{8dbef13f-1948-4aa8-8cf0-048eebed95d8}')
SpDataKey = Guid('{d9f6ee60-58c9-458b-88e1-2f908fd7f87c}')
SpFileStream = Guid('{947812b3-2ae1-4644-ba86-9e90ded7ec91}')
SpGramCompBackend = Guid('{da93e903-c843-11d2-a084-00c04f8ef9b5}')
SpGrammarCompiler = Guid('{b1e29d59-a675-11d2-8302-00c04f8ee6c0}')
SpITNProcessor = Guid('{12d73610-a1c9-11d3-bc90-00c04f72df9f}')
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
SpObjectTokenEnum = Guid('{3918d75f-0acb-41f2-b733-92aa15bcecf6}')
SpPhoneConverter = Guid('{9185f743-1143-4c28-86b5-bff14f20e5c8}')
SpPhoneticAlphabetConverter = Guid('{4f414126-dfe3-4629-99ee-797978317ead}')
SpPhraseBuilder = Guid('{777b6bbd-2ff2-11d3-88fe-00c04f8ef9b5}')
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
SpW3CGrammarCompiler = Guid('{d2c13906-51ef-454e-bc67-a52475ff074c}')
SpWaveFormatEx = Guid('{c79a574c-63be-44b9-801f-283f87f898be}')
SpeechAudioFormatType = Int32
SAFTDefault: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = -1
SAFTNoAssignedFormat: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 0
SAFTText: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 1
SAFTNonStandardFormat: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 2
SAFTExtendedAudioFormat: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 3
SAFT8kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 4
SAFT8kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 5
SAFT8kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 6
SAFT8kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 7
SAFT11kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 8
SAFT11kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 9
SAFT11kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 10
SAFT11kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 11
SAFT12kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 12
SAFT12kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 13
SAFT12kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 14
SAFT12kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 15
SAFT16kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 16
SAFT16kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 17
SAFT16kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 18
SAFT16kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 19
SAFT22kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 20
SAFT22kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 21
SAFT22kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 22
SAFT22kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 23
SAFT24kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 24
SAFT24kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 25
SAFT24kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 26
SAFT24kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 27
SAFT32kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 28
SAFT32kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 29
SAFT32kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 30
SAFT32kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 31
SAFT44kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 32
SAFT44kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 33
SAFT44kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 34
SAFT44kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 35
SAFT48kHz8BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 36
SAFT48kHz8BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 37
SAFT48kHz16BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 38
SAFT48kHz16BitStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 39
SAFTTrueSpeech_8kHz1BitMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 40
SAFTCCITT_ALaw_8kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 41
SAFTCCITT_ALaw_8kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 42
SAFTCCITT_ALaw_11kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 43
SAFTCCITT_ALaw_11kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 44
SAFTCCITT_ALaw_22kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 45
SAFTCCITT_ALaw_22kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 46
SAFTCCITT_ALaw_44kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 47
SAFTCCITT_ALaw_44kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 48
SAFTCCITT_uLaw_8kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 49
SAFTCCITT_uLaw_8kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 50
SAFTCCITT_uLaw_11kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 51
SAFTCCITT_uLaw_11kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 52
SAFTCCITT_uLaw_22kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 53
SAFTCCITT_uLaw_22kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 54
SAFTCCITT_uLaw_44kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 55
SAFTCCITT_uLaw_44kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 56
SAFTADPCM_8kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 57
SAFTADPCM_8kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 58
SAFTADPCM_11kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 59
SAFTADPCM_11kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 60
SAFTADPCM_22kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 61
SAFTADPCM_22kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 62
SAFTADPCM_44kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 63
SAFTADPCM_44kHzStereo: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 64
SAFTGSM610_8kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 65
SAFTGSM610_11kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 66
SAFTGSM610_22kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 67
SAFTGSM610_44kHzMono: win32more.Windows.Win32.Media.Speech.SpeechAudioFormatType = 68
SpeechAudioState = Int32
SASClosed: win32more.Windows.Win32.Media.Speech.SpeechAudioState = 0
SASStop: win32more.Windows.Win32.Media.Speech.SpeechAudioState = 1
SASPause: win32more.Windows.Win32.Media.Speech.SpeechAudioState = 2
SASRun: win32more.Windows.Win32.Media.Speech.SpeechAudioState = 3
SpeechBookmarkOptions = Int32
SBONone: win32more.Windows.Win32.Media.Speech.SpeechBookmarkOptions = 0
SBOPause: win32more.Windows.Win32.Media.Speech.SpeechBookmarkOptions = 1
SpeechDataKeyLocation = Int32
SDKLDefaultLocation: win32more.Windows.Win32.Media.Speech.SpeechDataKeyLocation = 0
SDKLCurrentUser: win32more.Windows.Win32.Media.Speech.SpeechDataKeyLocation = 1
SDKLLocalMachine: win32more.Windows.Win32.Media.Speech.SpeechDataKeyLocation = 2
SDKLCurrentConfig: win32more.Windows.Win32.Media.Speech.SpeechDataKeyLocation = 5
SpeechDiscardType = Int32
SDTProperty: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 1
SDTReplacement: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 2
SDTRule: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 4
SDTDisplayText: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 8
SDTLexicalForm: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 16
SDTPronunciation: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 32
SDTAudio: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 64
SDTAlternates: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 128
SDTAll: win32more.Windows.Win32.Media.Speech.SpeechDiscardType = 255
SpeechDisplayAttributes = Int32
SDA_No_Trailing_Space: win32more.Windows.Win32.Media.Speech.SpeechDisplayAttributes = 0
SDA_One_Trailing_Space: win32more.Windows.Win32.Media.Speech.SpeechDisplayAttributes = 2
SDA_Two_Trailing_Spaces: win32more.Windows.Win32.Media.Speech.SpeechDisplayAttributes = 4
SDA_Consume_Leading_Spaces: win32more.Windows.Win32.Media.Speech.SpeechDisplayAttributes = 8
SpeechEmulationCompareFlags = Int32
SECFIgnoreCase: win32more.Windows.Win32.Media.Speech.SpeechEmulationCompareFlags = 1
SECFIgnoreKanaType: win32more.Windows.Win32.Media.Speech.SpeechEmulationCompareFlags = 65536
SECFIgnoreWidth: win32more.Windows.Win32.Media.Speech.SpeechEmulationCompareFlags = 131072
SECFNoSpecialChars: win32more.Windows.Win32.Media.Speech.SpeechEmulationCompareFlags = 536870912
SECFEmulateResult: win32more.Windows.Win32.Media.Speech.SpeechEmulationCompareFlags = 1073741824
SECFDefault: win32more.Windows.Win32.Media.Speech.SpeechEmulationCompareFlags = 196609
SpeechEngineConfidence = Int32
SECLowConfidence: win32more.Windows.Win32.Media.Speech.SpeechEngineConfidence = -1
SECNormalConfidence: win32more.Windows.Win32.Media.Speech.SpeechEngineConfidence = 0
SECHighConfidence: win32more.Windows.Win32.Media.Speech.SpeechEngineConfidence = 1
SpeechFormatType = Int32
SFTInput: win32more.Windows.Win32.Media.Speech.SpeechFormatType = 0
SFTSREngine: win32more.Windows.Win32.Media.Speech.SpeechFormatType = 1
SpeechGrammarRuleStateTransitionType = Int32
SGRSTTEpsilon: win32more.Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType = 0
SGRSTTWord: win32more.Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType = 1
SGRSTTRule: win32more.Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType = 2
SGRSTTDictation: win32more.Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType = 3
SGRSTTWildcard: win32more.Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType = 4
SGRSTTTextBuffer: win32more.Windows.Win32.Media.Speech.SpeechGrammarRuleStateTransitionType = 5
SpeechGrammarState = Int32
SGSEnabled: win32more.Windows.Win32.Media.Speech.SpeechGrammarState = 1
SGSDisabled: win32more.Windows.Win32.Media.Speech.SpeechGrammarState = 0
SGSExclusive: win32more.Windows.Win32.Media.Speech.SpeechGrammarState = 3
SpeechGrammarWordType = Int32
SGDisplay: win32more.Windows.Win32.Media.Speech.SpeechGrammarWordType = 0
SGLexical: win32more.Windows.Win32.Media.Speech.SpeechGrammarWordType = 1
SGPronounciation: win32more.Windows.Win32.Media.Speech.SpeechGrammarWordType = 2
SGLexicalNoSpecialChars: win32more.Windows.Win32.Media.Speech.SpeechGrammarWordType = 3
SpeechInterference = Int32
SINone: win32more.Windows.Win32.Media.Speech.SpeechInterference = 0
SINoise: win32more.Windows.Win32.Media.Speech.SpeechInterference = 1
SINoSignal: win32more.Windows.Win32.Media.Speech.SpeechInterference = 2
SITooLoud: win32more.Windows.Win32.Media.Speech.SpeechInterference = 3
SITooQuiet: win32more.Windows.Win32.Media.Speech.SpeechInterference = 4
SITooFast: win32more.Windows.Win32.Media.Speech.SpeechInterference = 5
SITooSlow: win32more.Windows.Win32.Media.Speech.SpeechInterference = 6
SpeechLexiconType = Int32
SLTUser: win32more.Windows.Win32.Media.Speech.SpeechLexiconType = 1
SLTApp: win32more.Windows.Win32.Media.Speech.SpeechLexiconType = 2
SpeechLoadOption = Int32
SLOStatic: win32more.Windows.Win32.Media.Speech.SpeechLoadOption = 0
SLODynamic: win32more.Windows.Win32.Media.Speech.SpeechLoadOption = 1
SpeechPartOfSpeech = Int32
SPSNotOverriden: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = -1
SPSUnknown: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 0
SPSNoun: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 4096
SPSVerb: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 8192
SPSModifier: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 12288
SPSFunction: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 16384
SPSInterjection: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 20480
SPSLMA: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 28672
SPSSuppressWord: win32more.Windows.Win32.Media.Speech.SpeechPartOfSpeech = 61440
SpeechRecoContextState = Int32
SRCS_Disabled: win32more.Windows.Win32.Media.Speech.SpeechRecoContextState = 0
SRCS_Enabled: win32more.Windows.Win32.Media.Speech.SpeechRecoContextState = 1
SpeechRecoEvents = Int32
SREStreamEnd: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 1
SRESoundStart: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 2
SRESoundEnd: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 4
SREPhraseStart: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 8
SRERecognition: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 16
SREHypothesis: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 32
SREBookmark: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 64
SREPropertyNumChange: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 128
SREPropertyStringChange: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 256
SREFalseRecognition: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 512
SREInterference: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 1024
SRERequestUI: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 2048
SREStateChange: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 4096
SREAdaptation: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 8192
SREStreamStart: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 16384
SRERecoOtherContext: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 32768
SREAudioLevel: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 65536
SREPrivate: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 262144
SREAllEvents: win32more.Windows.Win32.Media.Speech.SpeechRecoEvents = 393215
SpeechRecognitionType = Int32
SRTStandard: win32more.Windows.Win32.Media.Speech.SpeechRecognitionType = 0
SRTAutopause: win32more.Windows.Win32.Media.Speech.SpeechRecognitionType = 1
SRTEmulated: win32more.Windows.Win32.Media.Speech.SpeechRecognitionType = 2
SRTSMLTimeout: win32more.Windows.Win32.Media.Speech.SpeechRecognitionType = 4
SRTExtendableParse: win32more.Windows.Win32.Media.Speech.SpeechRecognitionType = 8
SRTReSent: win32more.Windows.Win32.Media.Speech.SpeechRecognitionType = 16
SpeechRecognizerState = Int32
SRSInactive: win32more.Windows.Win32.Media.Speech.SpeechRecognizerState = 0
SRSActive: win32more.Windows.Win32.Media.Speech.SpeechRecognizerState = 1
SRSActiveAlways: win32more.Windows.Win32.Media.Speech.SpeechRecognizerState = 2
SRSInactiveWithPurge: win32more.Windows.Win32.Media.Speech.SpeechRecognizerState = 3
SpeechRetainedAudioOptions = Int32
SRAONone: win32more.Windows.Win32.Media.Speech.SpeechRetainedAudioOptions = 0
SRAORetainAudio: win32more.Windows.Win32.Media.Speech.SpeechRetainedAudioOptions = 1
SpeechRuleAttributes = Int32
SRATopLevel: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes = 1
SRADefaultToActive: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes = 2
SRAExport: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes = 4
SRAImport: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes = 8
SRAInterpreter: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes = 16
SRADynamic: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes = 32
SRARoot: win32more.Windows.Win32.Media.Speech.SpeechRuleAttributes = 64
SpeechRuleState = Int32
SGDSInactive: win32more.Windows.Win32.Media.Speech.SpeechRuleState = 0
SGDSActive: win32more.Windows.Win32.Media.Speech.SpeechRuleState = 1
SGDSActiveWithAutoPause: win32more.Windows.Win32.Media.Speech.SpeechRuleState = 3
SGDSActiveUserDelimited: win32more.Windows.Win32.Media.Speech.SpeechRuleState = 4
SpeechRunState = Int32
SRSEDone: win32more.Windows.Win32.Media.Speech.SpeechRunState = 1
SRSEIsSpeaking: win32more.Windows.Win32.Media.Speech.SpeechRunState = 2
SpeechSpecialTransitionType = Int32
SSTTWildcard: win32more.Windows.Win32.Media.Speech.SpeechSpecialTransitionType = 1
SSTTDictation: win32more.Windows.Win32.Media.Speech.SpeechSpecialTransitionType = 2
SSTTTextBuffer: win32more.Windows.Win32.Media.Speech.SpeechSpecialTransitionType = 3
SpeechStreamFileMode = Int32
SSFMOpenForRead: win32more.Windows.Win32.Media.Speech.SpeechStreamFileMode = 0
SSFMOpenReadWrite: win32more.Windows.Win32.Media.Speech.SpeechStreamFileMode = 1
SSFMCreate: win32more.Windows.Win32.Media.Speech.SpeechStreamFileMode = 2
SSFMCreateForWrite: win32more.Windows.Win32.Media.Speech.SpeechStreamFileMode = 3
SpeechStreamSeekPositionType = UInt32
SSSPTRelativeToStart: win32more.Windows.Win32.Media.Speech.SpeechStreamSeekPositionType = 0
SSSPTRelativeToCurrentPosition: win32more.Windows.Win32.Media.Speech.SpeechStreamSeekPositionType = 1
SSSPTRelativeToEnd: win32more.Windows.Win32.Media.Speech.SpeechStreamSeekPositionType = 2
SpeechTokenContext = UInt32
STCInprocServer: win32more.Windows.Win32.Media.Speech.SpeechTokenContext = 1
STCInprocHandler: win32more.Windows.Win32.Media.Speech.SpeechTokenContext = 2
STCLocalServer: win32more.Windows.Win32.Media.Speech.SpeechTokenContext = 4
STCRemoteServer: win32more.Windows.Win32.Media.Speech.SpeechTokenContext = 16
STCAll: win32more.Windows.Win32.Media.Speech.SpeechTokenContext = 23
SpeechTokenShellFolder = Int32
STSF_AppData: win32more.Windows.Win32.Media.Speech.SpeechTokenShellFolder = 26
STSF_LocalAppData: win32more.Windows.Win32.Media.Speech.SpeechTokenShellFolder = 28
STSF_CommonAppData: win32more.Windows.Win32.Media.Speech.SpeechTokenShellFolder = 35
STSF_FlagCreate: win32more.Windows.Win32.Media.Speech.SpeechTokenShellFolder = 32768
SpeechVisemeFeature = Int32
SVF_None: win32more.Windows.Win32.Media.Speech.SpeechVisemeFeature = 0
SVF_Stressed: win32more.Windows.Win32.Media.Speech.SpeechVisemeFeature = 1
SVF_Emphasis: win32more.Windows.Win32.Media.Speech.SpeechVisemeFeature = 2
SpeechVisemeType = Int32
SVP_0: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 0
SVP_1: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 1
SVP_2: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 2
SVP_3: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 3
SVP_4: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 4
SVP_5: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 5
SVP_6: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 6
SVP_7: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 7
SVP_8: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 8
SVP_9: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 9
SVP_10: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 10
SVP_11: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 11
SVP_12: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 12
SVP_13: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 13
SVP_14: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 14
SVP_15: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 15
SVP_16: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 16
SVP_17: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 17
SVP_18: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 18
SVP_19: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 19
SVP_20: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 20
SVP_21: win32more.Windows.Win32.Media.Speech.SpeechVisemeType = 21
SpeechVoiceEvents = Int32
SVEStartInputStream: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 2
SVEEndInputStream: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 4
SVEVoiceChange: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 8
SVEBookmark: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 16
SVEWordBoundary: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 32
SVEPhoneme: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 64
SVESentenceBoundary: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 128
SVEViseme: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 256
SVEAudioLevel: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 512
SVEPrivate: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 32768
SVEAllEvents: win32more.Windows.Win32.Media.Speech.SpeechVoiceEvents = 33790
SpeechVoicePriority = Int32
SVPNormal: win32more.Windows.Win32.Media.Speech.SpeechVoicePriority = 0
SVPAlert: win32more.Windows.Win32.Media.Speech.SpeechVoicePriority = 1
SVPOver: win32more.Windows.Win32.Media.Speech.SpeechVoicePriority = 2
SpeechVoiceSpeakFlags = Int32
SVSFDefault: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 0
SVSFlagsAsync: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 1
SVSFPurgeBeforeSpeak: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 2
SVSFIsFilename: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 4
SVSFIsXML: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 8
SVSFIsNotXML: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 16
SVSFPersistXML: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 32
SVSFNLPSpeakPunc: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 64
SVSFParseSapi: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 128
SVSFParseSsml: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 256
SVSFParseAutodetect: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 0
SVSFNLPMask: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 64
SVSFParseMask: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 384
SVSFVoiceMask: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = 511
SVSFUnusedFlags: win32more.Windows.Win32.Media.Speech.SpeechVoiceSpeakFlags = -512
SpeechWordPronounceable = Int32
SWPUnknownWordUnpronounceable: win32more.Windows.Win32.Media.Speech.SpeechWordPronounceable = 0
SWPUnknownWordPronounceable: win32more.Windows.Win32.Media.Speech.SpeechWordPronounceable = 1
SWPKnownWordPronounceable: win32more.Windows.Win32.Media.Speech.SpeechWordPronounceable = 2
SpeechWordType = Int32
SWTAdded: win32more.Windows.Win32.Media.Speech.SpeechWordType = 1
SWTDeleted: win32more.Windows.Win32.Media.Speech.SpeechWordType = 2
class _ISpPrivateEngineCall(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8e7c791e-4467-11d3-9723-00c04f72db08}')
    @commethod(3)
    def CallEngine(self, pCallFrame: VoidPtr, ulCallFrameSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CallEngineEx(self, pInFrame: VoidPtr, ulInFrameSize: UInt32, ppCoMemOutFrame: POINTER(VoidPtr), pulOutFrameSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class _ISpeechRecoContextEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7b8fcb42-0e9d-4f00-a048-7b04d6179d3d}')
class _ISpeechVoiceEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a372acd1-3bef-4bbd-8ffb-cb3e2b416af8}')


make_ready(__name__)
